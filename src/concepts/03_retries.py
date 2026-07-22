"""Retry handling for transient API failures.

OpenAI, Anthropic, and Groq all auto-retry connection errors, 408/409/429,
and 5xx with exponential backoff (default max_retries=2) -- configure that
via `max_retries=` on the client. Gemini's SDK takes retry config differently
(`http_options.retry_options`) and its error hierarchy has no dedicated
RateLimitError -- you check `.code == 429` on a caught ClientError instead.

This file also shows a manual backoff loop for cases where you need custom
behavior (e.g. logging every attempt, or a different policy than the SDK's).

Run: uv run python src/concepts/03_retries.py
"""

import random
import time

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


def sdk_builtin_retries() -> None:
    """The simplest option: let the SDK retry for you."""
    print("\n=== SDK built-in retries ===")

    # OpenAI, Anthropic, Groq: retries connection errors, 429, and 5xx
    # automatically before raising, configured via max_retries.
    openai_client = OpenAI(max_retries=5, timeout=20.0)
    anthropic_client = Anthropic(max_retries=5, timeout=20.0)
    groq_client = Groq(max_retries=5, timeout=20.0)

    # Per-call override without mutating the client:
    openai_client = openai_client.with_options(max_retries=2)
    anthropic_client = anthropic_client.with_options(max_retries=2)
    groq_client = groq_client.with_options(max_retries=2)

    # Gemini: retry policy is configured via http_options.retry_options on
    # the client (attempts / initial_delay / max_delay / exp_base / jitter).
    gemini_client = genai.Client(
        http_options=genai_types.HttpOptions(
            retry_options=genai_types.HttpRetryOptions(
                attempts=5, initial_delay=1.0, max_delay=20.0
            )
        )
    )

    openai_client.chat.completions.create(
        model=OPENAI_MODEL,
        max_completion_tokens=20,
        messages=[{"role": "user", "content": PROMPT}],
    )
    anthropic_client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=20,
        messages=[{"role": "user", "content": PROMPT}],
    )
    groq_client.chat.completions.create(
        model=GROQ_MODEL,
        max_completion_tokens=GROQ_MAX_TOKENS,
        messages=[{"role": "user", "content": PROMPT}],
    )
    gemini_client.models.generate_content(
        model=GEMINI_MODEL,
        contents=PROMPT,
        config=genai_types.GenerateContentConfig(max_output_tokens=20),
    )
    print("all four calls succeeded (SDKs handled any transient retries silently)")


def manual_backoff_openai(max_retries: int = 5, base_delay: float = 1.0) -> str:
    client = OpenAI()
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=OPENAI_MODEL,
                max_completion_tokens=20,
                messages=[{"role": "user", "content": PROMPT}],
            )
            return response.choices[0].message.content
        except openai.RateLimitError:
            pass
        except openai.APIStatusError as e:
            if e.status_code < 500:
                raise  # non-retryable client error (4xx except 429)
        except openai.APIConnectionError:
            pass

        delay = min(base_delay * (2**attempt) + random.uniform(0, 1), 30.0)
        print(f"  openai retry {attempt + 1}/{max_retries} after {delay:.1f}s")
        time.sleep(delay)

    raise RuntimeError("openai: exhausted retries")


def manual_backoff_anthropic(max_retries: int = 5, base_delay: float = 1.0) -> str:
    client = Anthropic()
    for attempt in range(max_retries):
        try:
            response = client.messages.create(
                model=ANTHROPIC_MODEL,
                max_tokens=20,
                messages=[{"role": "user", "content": PROMPT}],
            )
            return next(b.text for b in response.content if b.type == "text")
        except anthropic.RateLimitError:
            pass
        except anthropic.APIStatusError as e:
            if e.status_code < 500:
                raise
        except anthropic.APIConnectionError:
            pass

        delay = min(base_delay * (2**attempt) + random.uniform(0, 1), 30.0)
        print(f"  anthropic retry {attempt + 1}/{max_retries} after {delay:.1f}s")
        time.sleep(delay)

    raise RuntimeError("anthropic: exhausted retries")


def manual_backoff_groq(max_retries: int = 5, base_delay: float = 1.0) -> str:
    client = Groq()
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=GROQ_MODEL,
                max_completion_tokens=GROQ_MAX_TOKENS,
                messages=[{"role": "user", "content": PROMPT}],
            )
            return response.choices[0].message.content
        except groq.RateLimitError:
            pass
        except groq.APIStatusError as e:
            if e.status_code < 500:
                raise
        except groq.APIConnectionError:
            pass

        delay = min(base_delay * (2**attempt) + random.uniform(0, 1), 30.0)
        print(f"  groq retry {attempt + 1}/{max_retries} after {delay:.1f}s")
        time.sleep(delay)

    raise RuntimeError("groq: exhausted retries")


def manual_backoff_gemini(max_retries: int = 5, base_delay: float = 1.0) -> str:
    # No dedicated RateLimitError here -- 4xx (incl. 429) raises ClientError,
    # 5xx raises ServerError, both carrying the HTTP status on `.code`.
    client = genai.Client()
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=PROMPT,
                config=genai_types.GenerateContentConfig(max_output_tokens=20),
            )
            return response.text
        except genai_errors.ClientError as e:
            if e.code != 429:
                raise  # non-retryable client error
        except genai_errors.ServerError:
            pass

        delay = min(base_delay * (2**attempt) + random.uniform(0, 1), 30.0)
        print(f"  gemini retry {attempt + 1}/{max_retries} after {delay:.1f}s")
        time.sleep(delay)

    raise RuntimeError("gemini: exhausted retries")


if __name__ == "__main__":
    sdk_builtin_retries()

    print("\n=== Manual exponential backoff ===")
    print("openai:", manual_backoff_openai())
    # print("anthropic:", manual_backoff_anthropic())
    print("groq:", manual_backoff_groq())
    print("gemini:", manual_backoff_gemini())
