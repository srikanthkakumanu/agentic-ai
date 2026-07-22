"""Counting tokens before and after a call.

Pre-call estimation is only as good as the tokenizer you use:
- OpenAI: `tiktoken` (its own tokenizer) for a local pre-call estimate.
- Anthropic: the `count_tokens` endpoint -- never tiktoken, it undercounts
  Claude tokens significantly.
- Gemini: the `count_tokens` endpoint -- free, model-specific, accurate.
- Groq: no official tokenizer or count endpoint for arbitrary hosted models
  (gpt-oss, qwen, etc. each tokenize differently) -- only the actual
  post-call `usage` is reliable, so that's all this shows for Groq.

Run: uv run python src/concepts/05_token_counting.py
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

PROMPT = "Explain the difference between prompt tokens and completion tokens."


def count_openai_tokens() -> None:
    print("\n=== OpenAI token counting ===")
    client = OpenAI()

    # Pre-call estimate via tiktoken (local, no API call).
    encoding = tiktoken.encoding_for_model("gpt-4o")  # closest available encoding
    estimated = len(encoding.encode(PROMPT))
    print(f"estimated prompt tokens (tiktoken): {estimated}")

    # Actual count comes back on the response after the call.
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        max_completion_tokens=150,
        messages=[{"role": "user", "content": PROMPT}],
    )
    print(f"actual prompt tokens    : {response.usage.prompt_tokens}")
    print(f"actual completion tokens: {response.usage.completion_tokens}")


def count_anthropic_tokens() -> None:
    print("\n=== Anthropic token counting ===")
    client = Anthropic()

    # Pre-call estimate via the dedicated count_tokens endpoint (free, no
    # generation happens) -- this is model-specific and accurate, unlike
    # a borrowed tokenizer.
    count = client.messages.count_tokens(
        model=ANTHROPIC_MODEL,
        messages=[{"role": "user", "content": PROMPT}],
    )
    print(f"estimated prompt tokens (count_tokens): {count.input_tokens}")

    response = client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=150,
        messages=[{"role": "user", "content": PROMPT}],
    )
    print(f"actual input tokens : {response.usage.input_tokens}")
    print(f"actual output tokens: {response.usage.output_tokens}")


def count_groq_tokens() -> None:
    print("\n=== Groq token counting ===")
    client = Groq()

    # No pre-call estimate: Groq hosts several model families (gpt-oss, qwen,
    # llama, ...) each with a different tokenizer, and there's no count_tokens
    # endpoint -- only the actual usage returned after the call is reliable.
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        max_completion_tokens=150,
        messages=[{"role": "user", "content": PROMPT}],
    )
    print(f"actual prompt tokens    : {response.usage.prompt_tokens}")
    print(f"actual completion tokens: {response.usage.completion_tokens}")


def count_gemini_tokens() -> None:
    print("\n=== Gemini token counting ===")
    client = genai.Client()

    # Pre-call estimate via the dedicated count_tokens endpoint (free).
    count = client.models.count_tokens(model=GEMINI_MODEL, contents=PROMPT)
    print(f"estimated prompt tokens (count_tokens): {count.total_tokens}")

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=PROMPT,
        config=genai_types.GenerateContentConfig(max_output_tokens=150),
    )
    usage = response.usage_metadata
    print(f"actual prompt tokens    : {usage.prompt_token_count}")
    print(f"actual candidates tokens: {usage.candidates_token_count}")


if __name__ == "__main__":
    count_openai_tokens()
    count_anthropic_tokens()
    count_groq_tokens()
    count_gemini_tokens()
