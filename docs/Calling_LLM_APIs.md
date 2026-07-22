# Calling LLM APIs: Direct Calls, Streaming, Retries, Rate Limits, Tokens, and Cost

Six things every production LLM integration has to get right, beyond "and then I called the API." This tutorial covers each one — what it is, why it exists, its advantages, and the industry-standard way to implement it — with runnable code for **OpenAI, Anthropic, Groq, and Gemini** in [`src/concepts/`](../src/concepts/).

## Table of Contents

1. [Direct API Calls](#1-direct-api-calls)
2. [Streaming](#2-streaming)
3. [Retries](#3-retries)
4. [Rate Limits](#4-rate-limits)
5. [Token Counting](#5-token-counting)
6. [Cost Estimation](#6-cost-estimation)

Each section builds on the last: a direct call is the base case; streaming changes *how* you receive that call's response; retries and rate limits handle it failing; token counting and cost estimation handle its price. Together they're the difference between a script that works on your machine and one that survives production traffic.

## 1. Direct API Calls

**What it is:** Calling a provider's API through its **official SDK** (`OpenAI()`, `Anthropic()`, `Groq()`, `genai.Client()`) instead of hand-rolling HTTP requests or going through a heavier framework like LangChain.

**Why it's used:** Every LLM provider exposes an HTTP API under the hood, but you rarely want to speak raw HTTP to it. The official SDK handles auth headers, request/response serialization, typed errors, and retries for you — the same way you wouldn't hand-write SQL wire protocol when a database driver exists.

**Advantages:**

- **Fewer moving parts** — one dependency (the SDK) instead of `requests`/`httpx` plus your own error-handling and serialization code.
- **Day-one feature access** — new provider features (structured outputs, new tool types, new models) land in the SDK immediately; a framework wrapper around it lags behind.
- **Typed responses and errors** — `response.usage.prompt_tokens`, `anthropic.RateLimitError`, etc., instead of parsing raw JSON and guessing at field names.
- **Predictable debugging** — one less abstraction layer between your code and the actual API call when something goes wrong.

**Best industry practice:**

- Read credentials from environment variables (`.env` + `python-dotenv`), never hardcode an API key in source.
- Let the SDK's zero-arg constructor (`OpenAI()`, `Anthropic()`, `Groq()`, `genai.Client()`) auto-discover the key from its expected env var (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GROQ_API_KEY`, `GOOGLE_API_KEY`) rather than passing `api_key=` explicitly.
- Pin SDK versions in `pyproject.toml` — provider SDKs ship breaking changes between majors.
- Keep the model name in one constant per provider, not scattered as string literals through the codebase.
- Set an explicit `max_tokens` (OpenAI/Groq: `max_completion_tokens`; Anthropic: `max_tokens`; Gemini: `max_output_tokens`) on every call — providers don't default this to something small and safe.

```python
from openai import OpenAI

client = OpenAI()  # reads OPENAI_API_KEY from the environment
response = client.chat.completions.create(
    model="gpt-5-nano",
    max_completion_tokens=200,
    messages=[{"role": "user", "content": "In one sentence, what is RAG?"}],
)
print(response.choices[0].message.content)
```

| Provider | Client constructor | Env var read automatically | Call method |
| --- | --- | --- | --- |
| OpenAI | `OpenAI()` | `OPENAI_API_KEY` | `client.chat.completions.create(...)` |
| Anthropic | `Anthropic()` | `ANTHROPIC_API_KEY` | `client.messages.create(...)` |
| Groq | `Groq()` | `GROQ_API_KEY` | `client.chat.completions.create(...)` (OpenAI-compatible) |
| Gemini | `genai.Client()` | `GOOGLE_API_KEY` | `client.models.generate_content(...)` |

Full runnable example: [`src/concepts/01_direct_calls.py`](../src/concepts/01_direct_calls.py).

## 2. Streaming

**What it is:** Receiving the model's output incrementally — token by token, or chunk by chunk — over a persistent connection, instead of blocking until the entire response is generated and returned in one payload.

**Why it's used:** LLMs generate text one token at a time internally (see [`LLM_Engineering.md`](LLM_Engineering.md) for how the decoder loop works) — the model already *has* the first sentence long before it's finished the last one. Streaming just exposes that as it happens instead of buffering it all server-side first.

**Advantages:**

- **Lower perceived latency** — the first token can appear in a few hundred milliseconds instead of waiting for a multi-second full generation, which matters enormously for chat UX.
- **Avoids client/proxy timeouts** — a non-streaming request that takes minutes to generate a long response risks hitting an HTTP timeout before it ever returns; streaming keeps the connection active with continuous data.
- **Early cancellation** — you can stop consuming (and stop paying for further generation, on some providers) as soon as you have what you need.
- **Progressive processing** — you can start rendering, parsing, or acting on partial output before generation finishes.

**Best industry practice:**

- Default to streaming for anything user-facing (chat UIs) or with a large expected output — it's the difference between a spinner and a typing effect.
- Always capture the **final accumulated message** for usage/token accounting, not just the printed text — usage typically only arrives on the last chunk or via a dedicated accumulator (`stream.get_final_message()` for Anthropic).
- Handle a stream ending abnormally (network drop mid-generation) — you may have partial, unusable content.
- Don't assume every provider's streaming shape is identical — usage placement and opt-in flags differ (see below).

```python
with client.messages.stream(
    model="claude-haiku-4-5",
    max_tokens=300,
    messages=[{"role": "user", "content": "List three benefits of streaming."}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
    final_message = stream.get_final_message()  # usage lives here
```

Provider quirks worth knowing (all verified against the installed SDKs, not assumed):

| Provider | Streaming call | Where `usage` shows up |
| --- | --- | --- |
| OpenAI | `stream=True, stream_options={"include_usage": True}` | Final chunk's `.usage` |
| Anthropic | `client.messages.stream(...)` context manager | `stream.get_final_message().usage` |
| Groq | `stream=True` (no `stream_options` support — it 400s) | Final chunk's `.x_groq.usage` |
| Gemini | `client.models.generate_content_stream(...)` | Final chunk's `.usage_metadata` |

Full runnable example: [`src/concepts/02_streaming.py`](../src/concepts/02_streaming.py).

## 3. Retries

**What it is:** Automatically re-sending a failed request after a transient failure — a dropped connection, a `5xx` server error, or a `429` rate-limit response — usually with **exponential backoff** (each retry waits longer than the last) plus **jitter** (a small random offset) to avoid every failed client retrying at the exact same instant.

**Why it's used:** LLM APIs are distributed systems under heavy, bursty load. A `429` or `503` is often gone thirty seconds later with zero code changes needed — the failure is in the request's timing, not its content. Failing the user's entire request (or an agent's multi-step task) on the first transient hiccup wastes everything already done and produces a worse experience than a short, invisible retry.

**Advantages:**

- **Higher effective reliability** without touching application logic — most transient failures become invisible to the end user.
- **Protects sunk cost** in multi-step flows (an agent loop, a long conversation) where failing late is much more expensive than a short delay.
- **Backoff + jitter specifically** prevents a "thundering herd" — if 1,000 clients hit a `429` at once and all retry after exactly 1 second, they just cause the same spike again.

**Best industry practice:**

- **Prefer the SDK's built-in retry handling first.** OpenAI, Anthropic, and Groq all auto-retry connection errors, `408`/`409`/`429`, and `5xx` with backoff by default (`max_retries=2`); just raise it (`OpenAI(max_retries=5)`) rather than reimplementing the loop.
- **Only retry retryable failures.** A `429` or `5xx` is worth retrying; a `400` (malformed request) or `401` (bad credentials) will fail identically every time — retrying it just delays the real error.
- **Cap total attempts and total wall-clock time** so a persistently down dependency fails loudly instead of retrying forever.
- **Write a manual backoff loop only when you need something the SDK doesn't give you** — custom logging per attempt, a different backoff curve, or (for Gemini) working around an SDK without a dedicated `RateLimitError` class.

```python
# SDK built-in — the simplest, usually-correct option
client = OpenAI(max_retries=5, timeout=20.0)

# Manual backoff — only when you need custom behavior
import random, time
import openai

for attempt in range(5):
    try:
        response = client.chat.completions.create(model="gpt-5-nano", max_completion_tokens=20,
                                                    messages=[{"role": "user", "content": "Say OK."}])
        break
    except openai.RateLimitError:
        pass
    except openai.APIStatusError as e:
        if e.status_code < 500:
            raise  # non-retryable — don't waste a retry on a bad request
    delay = min(1.0 * (2**attempt) + random.uniform(0, 1), 30.0)
    time.sleep(delay)
```

Not every SDK exposes the same error shape — this is the kind of detail you only get right by checking each SDK, not by assuming they match:

| Provider | Retryable error classes | Retry config |
| --- | --- | --- |
| OpenAI | `openai.RateLimitError`, `openai.APIStatusError` (5xx), `openai.APIConnectionError` | `max_retries=` on the client |
| Anthropic | `anthropic.RateLimitError`, `anthropic.APIStatusError`, `anthropic.APIConnectionError` | `max_retries=` on the client |
| Groq | `groq.RateLimitError`, `groq.APIStatusError`, `groq.APIConnectionError` (OpenAI-shaped SDK) | `max_retries=` on the client |
| Gemini | `google.genai.errors.ClientError` (check `.code == 429`), `.ServerError` (5xx) — no dedicated rate-limit class | `http_options.retry_options` (`HttpRetryOptions(attempts=..., initial_delay=..., max_delay=...)`) |

Full runnable example: [`src/concepts/03_retries.py`](../src/concepts/03_retries.py).

## 4. Rate Limits

**What it is:** Caps a provider places on how much traffic your API key can send in a given window — requests per minute (RPM), tokens per minute (TPM), or requests per day (RPD) — enforced independently of whether any single request is otherwise valid.

**Why it's used:** From the provider's side, rate limits protect shared infrastructure from any one customer overwhelming it, and gate how much capacity your billing tier or free-tier allotment entitles you to. From your side, they're a hard ceiling you need to design around — hitting one isn't a bug in your code, it's the system working as intended.

**Advantages of handling them well:**

- **Predictable throughput** — knowing your ceiling lets you design a system (queue, worker pool, batching) that stays under it instead of bursting into failures.
- **Avoids cascading failures** — a flood of `429`s under load, each triggering a retry, can turn a brief rate-limit hit into a self-inflicted outage if nothing throttles the retries.
- **No surprise billing or suspension** — some providers pair "you can't exceed the limit" with usage-based billing; understanding your ceiling avoids both throttling and unexpected charges.

**Best industry practice:**

- **Read the rate-limit headers when they're available** and throttle proactively, before you're actually rejected — most providers return your remaining quota on every response, not just on failure.
- **Respect `retry-after`** when a `429` does happen instead of guessing a delay.
- For high-volume workloads, add **client-side request queuing/throttling** (a token-bucket or leaky-bucket limiter) rather than relying on reactive retries alone.
- **Know which providers don't expose quota headers at all.** Gemini's Developer API doesn't return `x-ratelimit-*` headers — the only real-time signal is catching the `429`; check free-tier quota in [AI Studio](https://aistudio.google.com/rate-limit) instead.

```python
raw = client.chat.completions.with_raw_response.create(
    model="gpt-5-nano", max_completion_tokens=20,
    messages=[{"role": "user", "content": "Say OK."}],
)
print(raw.headers.get("x-ratelimit-remaining-requests"))
print(raw.headers.get("x-ratelimit-remaining-tokens"))
```

| Provider | Rate-limit headers | 429 handling |
| --- | --- | --- |
| OpenAI | `x-ratelimit-{remaining,limit}-{requests,tokens}` | `openai.RateLimitError`, read `e.response.headers["retry-after"]` |
| Anthropic | `anthropic-ratelimit-{requests,input-tokens,output-tokens}-{remaining,limit}` | `anthropic.RateLimitError` |
| Groq | `x-ratelimit-{remaining,limit}-{requests,tokens}` (OpenAI-shaped) | `groq.RateLimitError` |
| Gemini | *(none returned)* | `google.genai.errors.ClientError` with `.code == 429` |

Full runnable example: [`src/concepts/04_rate_limits.py`](../src/concepts/04_rate_limits.py).

## 5. Token Counting

**What it is:** Determining how many tokens a piece of text will consume — before sending it (an estimate) or after the call returns (the actual count) — since every provider bills, rate-limits, and caps context by **tokens**, not characters or words.

**Why it's used:** A model's context window is a token budget, and its price is a token price. Without counting tokens you can't answer "will this prompt fit," "roughly what will this cost," or "how much history can I keep in this conversation before I need to trim it."

**Advantages:**

- **Predictable cost**, since cost estimation (next section) is entirely downstream of token counts.
- **Avoids context-window overflow errors** mid-conversation, by trimming history proactively instead of discovering the limit via a failed request.
- **Enables smarter context management** — deciding what to summarize, drop, or cache based on actual token weight rather than a rough guess.

**Best industry practice:**

- **Use each provider's own tokenizer or endpoint.** Tokenizers are model-specific — OpenAI's `tiktoken` undercounts Claude tokens by a wide margin because it's a different tokenizer entirely. Never borrow one provider's tokenizer to estimate another's.
- **Prefer a real counting endpoint over a heuristic** (word count, `len(text) / 4`) whenever the provider offers one — it's free and exact.
- **Recompute after any prompt or model change** — token counts aren't portable across models, even from the same provider.
- **Fall back to actual post-call `usage`** when a provider has no pre-call counting endpoint at all (Groq hosts several model families — gpt-oss, qwen, llama — each with its own tokenizer, and exposes no dedicated counting endpoint).

```python
# OpenAI — local tokenizer estimate, then actual usage from the response
import tiktoken
encoding = tiktoken.encoding_for_model("gpt-4o")
estimated = len(encoding.encode(prompt))

# Anthropic / Gemini — free server-side counting endpoint, no generation happens
count = client.messages.count_tokens(model="claude-haiku-4-5", messages=[...])       # Anthropic
count = client.models.count_tokens(model="gemini-3.1-flash-lite", contents=prompt)   # Gemini
```

| Provider | Pre-call estimate | Actual count source |
| --- | --- | --- |
| OpenAI | `tiktoken.encoding_for_model(...)` (local, free) | `response.usage.prompt_tokens` / `.completion_tokens` |
| Anthropic | `client.messages.count_tokens(...)` (free endpoint) | `response.usage.input_tokens` / `.output_tokens` |
| Groq | *(none — no shared tokenizer across hosted models)* | `response.usage.prompt_tokens` / `.completion_tokens` |
| Gemini | `client.models.count_tokens(...)` (free endpoint) | `response.usage_metadata.prompt_token_count` / `.candidates_token_count` |

Full runnable example: [`src/concepts/05_token_counting.py`](../src/concepts/05_token_counting.py).

## 6. Cost Estimation

**What it is:** Converting a token count into an actual dollar figure, using each model's published per-million-token input and output rates — typically computed both **before** a call (a worst-case estimate against `max_tokens`) and **after** it (the actual cost from real `usage`).

**Why it's used:** Cost scales with usage in ways that are easy to underestimate — long conversation histories re-sent on every turn, high request volume, or an expensive flagship model chosen where a cheaper one would do. Estimating cost isn't optional bookkeeping; it's what lets you pick the right model for a task and catch runaway spend before the bill does.

**Advantages:**

- **Prevents surprise bills** by making cost visible per-request instead of only discovering it in aggregate at the end of a billing cycle.
- **Informs model selection** — a $0.05/$0.40-per-MTok model that meets the quality bar beats a $5/$25 one for the same task, every time.
- **Enables cost attribution** — per-user, per-feature, or per-request cost tracking is what lets you find the one workflow that's actually expensive.

**Best industry practice:**

- **Keep a single pricing table as source of truth** (input/output rate per model) and keep it in sync with the provider's pricing page — rates change, and a stale table silently misleads every estimate downstream. See [`LLM_Providers.md`](LLM_Providers.md) for this project's current rates.
- **Estimate worst-case pre-call** using the pre-call token estimate and your `max_tokens` ceiling; **compute actual cost post-call** from real `usage` — the two will usually differ, since the model rarely uses its entire output budget.
- **Default to the cheapest model that clears the quality bar** for a given task, and reserve expensive/flagship models for the cases that actually need them — this project's examples default to `gpt-5-nano`, `claude-haiku-4-5`, `gemini-3.1-flash-lite`, and Groq's free tier for exactly this reason.
- **Remember free tiers aren't zero-cost forever** — they're bounded by rate limits, not token budgets; track usage against those limits so a burst of traffic doesn't silently spill onto a paid tier.

```python
PRICING = {  # $ per 1M tokens: (input_rate, output_rate)
    "gpt-5-nano": (0.05, 0.40),
    "claude-haiku-4-5": (1.00, 5.00),
    "gemini-3.1-flash-lite": (0.00, 0.00),  # free tier
}

def estimate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    input_rate, output_rate = PRICING[model]
    return (input_tokens / 1_000_000) * input_rate + (output_tokens / 1_000_000) * output_rate
```

Full runnable example: [`src/concepts/06_cost_estimation.py`](../src/concepts/06_cost_estimation.py).

## Summary

| # | Topic | Solves | Rule of thumb |
| --- | --- | --- | --- |
| 1 | Direct API calls | Talking to the provider at all | Official SDK, env-var credentials, explicit `max_tokens` |
| 2 | Streaming | Perceived latency, timeouts on long output | Default on for chat/long generations; capture the final message for usage |
| 3 | Retries | Transient failures (`429`, `5xx`, network) | Use the SDK's built-in `max_retries` first; only retry retryable errors |
| 4 | Rate limits | Provider-enforced traffic ceilings | Read headers proactively; respect `retry-after`; throttle client-side at volume |
| 5 | Token counting | "Will this fit / what will this cost" | Use the provider's own tokenizer/endpoint — never borrow another provider's |
| 6 | Cost estimation | Turning tokens into dollars | One pricing table, pre- and post-call estimates, cheapest model that clears the bar |

**Where to go next:** every example here uses a single-turn, non-agentic call. The natural next step is multi-turn conversation state (resending history each call, since these APIs are stateless) and tool/function calling — see [`Prompt_Engineering.md`](Prompt_Engineering.md) for the reasoning-pattern side of that, and each provider's own docs for tool-use syntax specifics.
