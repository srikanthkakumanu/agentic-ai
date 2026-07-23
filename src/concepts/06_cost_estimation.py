"""Estimating and tracking the dollar cost of API calls.

Pricing is hardcoded below (per 1M tokens, July 2026 list prices) since none
of the SDKs expose pricing programmatically -- keep this table in sync with
docs/LLM_Providers.md when rates change. Groq and Gemini are both $0 here
because the models used are on free tiers (no per-token billing while under
the rate limit) -- the calculation still runs so the same code path works
unchanged if you later move to a paid tier or a different model.

Run: uv run python src/concepts/06_cost_estimation.py
"""

from dotenv import load_dotenv
import tiktoken
from openai import OpenAI
from anthropic import Anthropic
from groq import Groq
from google import genai
from google.genai import types as genai_types

load_dotenv()

OPENAI_MODEL = "gpt-5-nano"
ANTHROPIC_MODEL = "claude-haiku-4-5"
GEMINI_MODEL = "gemini-3.1-flash-lite"
GROQ_MODEL = "openai/gpt-oss-20b"

# $ per 1M tokens: (input_rate, output_rate)
PRICING = {
    "gpt-5-nano": (0.05, 0.40),
    "claude-haiku-4-5": (1.00, 5.00),
    "gemini-3.1-flash-lite": (0.00, 0.00),  # free tier
    "openai/gpt-oss-20b": (0.00, 0.00),  # Groq free tier
}

PROMPT = "Summarize why cost estimation matters for LLM applications, in two sentences."
ASSUMED_MAX_OUTPUT = 150


def estimate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    input_rate, output_rate = PRICING[model]
    return (input_tokens / 1_000_000) * input_rate + (
        output_tokens / 1_000_000
    ) * output_rate


def openai_cost_walkthrough() -> None:
    print("\n=== OpenAI cost estimation ===")
    client = OpenAI()

    encoding = tiktoken.encoding_for_model("gpt-4o")
    estimated_input = len(encoding.encode(PROMPT))
    pre_call = estimate_cost(OPENAI_MODEL, estimated_input, ASSUMED_MAX_OUTPUT)
    print(f"pre-call estimate (worst case @ max_tokens): ${pre_call:.6f}")

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        max_completion_tokens=ASSUMED_MAX_OUTPUT,
        messages=[{"role": "user", "content": PROMPT}],
    )
    actual = estimate_cost(
        OPENAI_MODEL,
        response.usage.prompt_tokens,
        response.usage.completion_tokens,
    )
    print(
        f"actual cost: ${actual:.6f} "
        f"({response.usage.prompt_tokens} in / {response.usage.completion_tokens} out)"
    )


def anthropic_cost_walkthrough() -> None:
    print("\n=== Anthropic cost estimation ===")
    client = Anthropic()

    count = client.messages.count_tokens(
        model=ANTHROPIC_MODEL,
        messages=[{"role": "user", "content": PROMPT}],
    )
    pre_call = estimate_cost(ANTHROPIC_MODEL, count.input_tokens, ASSUMED_MAX_OUTPUT)
    print(f"pre-call estimate (worst case @ max_tokens): ${pre_call:.6f}")

    response = client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=ASSUMED_MAX_OUTPUT,
        messages=[{"role": "user", "content": PROMPT}],
    )
    actual = estimate_cost(
        ANTHROPIC_MODEL,
        response.usage.input_tokens,
        response.usage.output_tokens,
    )
    print(
        f"actual cost: ${actual:.6f} "
        f"({response.usage.input_tokens} in / {response.usage.output_tokens} out)"
    )


def groq_cost_walkthrough() -> None:
    print("\n=== Groq cost estimation ===")
    client = Groq()

    # No pre-call estimate available (see 05_token_counting.py) -- cost is
    # computed from the actual post-call usage only. Rate is $0 on the free
    # tier, so this always prints $0.000000; swap PRICING to a paid Groq
    # tier's rate if you're ever billed per-token.
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        max_completion_tokens=ASSUMED_MAX_OUTPUT,
        messages=[{"role": "user", "content": PROMPT}],
    )
    actual = estimate_cost(
        GROQ_MODEL,
        response.usage.prompt_tokens,
        response.usage.completion_tokens,
    )
    print(
        f"actual cost: ${actual:.6f} "
        f"({response.usage.prompt_tokens} in / {response.usage.completion_tokens} out, free tier)"
    )


def gemini_cost_walkthrough() -> None:
    print("\n=== Gemini cost estimation ===")
    client = genai.Client()

    count = client.models.count_tokens(model=GEMINI_MODEL, contents=PROMPT)
    pre_call = estimate_cost(GEMINI_MODEL, count.total_tokens, ASSUMED_MAX_OUTPUT)
    print(f"pre-call estimate (worst case @ max_tokens): ${pre_call:.6f}")

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=PROMPT,
        config=genai_types.GenerateContentConfig(max_output_tokens=ASSUMED_MAX_OUTPUT),
    )
    usage = response.usage_metadata
    actual = estimate_cost(
        GEMINI_MODEL, usage.prompt_token_count, usage.candidates_token_count
    )
    print(
        f"actual cost: ${actual:.6f} "
        f"({usage.prompt_token_count} in / {usage.candidates_token_count} out, free tier)"
    )


if __name__ == "__main__":
    openai_cost_walkthrough()
    # anthropic_cost_walkthrough()
    groq_cost_walkthrough()
    gemini_cost_walkthrough()
