"""Reading rate-limit headers and handling 429s gracefully.

OpenAI, Groq, and Anthropic all return `x-ratelimit-*` headers on every
response. Gemini's Developer API does not expose per-minute quota headers at
all -- there's nothing to read there; you find out you're throttled only by
catching a 429, and you check remaining free-tier quota in AI Studio instead
(see docs/LLM_Providers.md).

Run: uv run python src/concepts/04_rate_limits.py
"""

from dotenv import load_dotenv
import openai
from openai import OpenAI
import anthropic
from anthropic import Anthropic
import groq
from groq import Groq
from google import genai
from google.genai import errors as genai_errors
from google.genai import types as genai_types

load_dotenv()

OPENAI_MODEL = "gpt-5-nano"
ANTHROPIC_MODEL = "claude-haiku-4-5"
GEMINI_MODEL = "gemini-3.1-flash-lite"
GROQ_MODEL = "openai/gpt-oss-20b"

PROMPT = "Say OK."
# gpt-oss models reason internally before answering, so they need more
# completion budget than a non-reasoning model to leave room for the answer.
GROQ_MAX_TOKENS = 150


def inspect_openai_rate_limits() -> None:
    print("\n=== OpenAI rate-limit headers ===")
    client = OpenAI()

    # with_raw_response gives access to headers alongside the parsed response.
    raw = client.chat.completions.with_raw_response.create(
        model=OPENAI_MODEL,
        max_completion_tokens=20,
        messages=[{"role": "user", "content": PROMPT}],
    )
    headers = raw.headers
    print(f"requests remaining : {headers.get('x-ratelimit-remaining-requests')}")
    print(f"requests limit     : {headers.get('x-ratelimit-limit-requests')}")
    print(f"tokens remaining   : {headers.get('x-ratelimit-remaining-tokens')}")
    print(f"tokens limit       : {headers.get('x-ratelimit-limit-tokens')}")


def inspect_anthropic_rate_limits() -> None:
    print("\n=== Anthropic rate-limit headers ===")
    client = Anthropic()

    raw = client.messages.with_raw_response.create(
        model=ANTHROPIC_MODEL,
        max_tokens=20,
        messages=[{"role": "user", "content": PROMPT}],
    )
    headers = raw.headers
    print(f"requests remaining : {headers.get('anthropic-ratelimit-requests-remaining')}")
    print(f"requests limit     : {headers.get('anthropic-ratelimit-requests-limit')}")
    print(f"input tokens left  : {headers.get('anthropic-ratelimit-input-tokens-remaining')}")
    print(f"output tokens left : {headers.get('anthropic-ratelimit-output-tokens-remaining')}")


def inspect_groq_rate_limits() -> None:
    print("\n=== Groq rate-limit headers ===")
    client = Groq()

    raw = client.chat.completions.with_raw_response.create(
        model=GROQ_MODEL,
        max_completion_tokens=GROQ_MAX_TOKENS,
        messages=[{"role": "user", "content": PROMPT}],
    )
    headers = raw.headers
    print(f"requests remaining : {headers.get('x-ratelimit-remaining-requests')}")
    print(f"requests limit     : {headers.get('x-ratelimit-limit-requests')}")
    print(f"tokens remaining   : {headers.get('x-ratelimit-remaining-tokens')}")
    print(f"tokens limit       : {headers.get('x-ratelimit-limit-tokens')}")
    print(f"resets in (tokens) : {headers.get('x-ratelimit-reset-tokens')}")


def inspect_gemini_quota() -> None:
    print("\n=== Gemini quota ===")
    client = genai.Client()

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=PROMPT,
        config=genai_types.GenerateContentConfig(max_output_tokens=20),
    )
    print(f"response headers: {dict(response.sdk_http_response.headers)}")
    print("no x-ratelimit-* headers on this API -- check aistudio.google.com/rate-limit "
          "for free-tier quota, and rely on catching a 429 to detect throttling at runtime")


def handle_rate_limit_error_openai() -> None:
    """Pattern for reacting to a 429 with the server-provided retry delay."""
    client = OpenAI()
    try:
        client.chat.completions.create(
            model=OPENAI_MODEL,
            max_completion_tokens=20,
            messages=[{"role": "user", "content": PROMPT}],
        )
    except openai.RateLimitError as e:
        retry_after = int(e.response.headers.get("retry-after", "60"))
        print(f"openai: rate limited, would retry after {retry_after}s")


def handle_rate_limit_error_anthropic() -> None:
    client = Anthropic()
    try:
        client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=20,
            messages=[{"role": "user", "content": PROMPT}],
        )
    except anthropic.RateLimitError as e:
        retry_after = int(e.response.headers.get("retry-after", "60"))
        print(f"anthropic: rate limited, would retry after {retry_after}s")


def handle_rate_limit_error_groq() -> None:
    client = Groq()
    try:
        client.chat.completions.create(
            model=GROQ_MODEL,
            max_completion_tokens=20,
            messages=[{"role": "user", "content": PROMPT}],
        )
    except groq.RateLimitError as e:
        retry_after = int(e.response.headers.get("retry-after", "60"))
        print(f"groq: rate limited, would retry after {retry_after}s")


def handle_rate_limit_error_gemini() -> None:
    """Gemini has no dedicated RateLimitError -- 429 arrives as ClientError."""
    client = genai.Client()
    try:
        client.models.generate_content(
            model=GEMINI_MODEL,
            contents=PROMPT,
            config=genai_types.GenerateContentConfig(max_output_tokens=20),
        )
    except genai_errors.ClientError as e:
        if e.code == 429:
            print(f"gemini: rate limited ({e.message})")
        else:
            raise


if __name__ == "__main__":
    inspect_openai_rate_limits()
    inspect_anthropic_rate_limits()
    inspect_groq_rate_limits()
    inspect_gemini_quota()

    print("\n=== 429 handling (no-ops unless you're actually rate limited) ===")
    handle_rate_limit_error_openai()
    handle_rate_limit_error_anthropic()
    handle_rate_limit_error_groq()
    handle_rate_limit_error_gemini()
    print("no rate limit hit during this run")
