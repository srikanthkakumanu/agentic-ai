"""Calling LLM APIs directly with each provider's official SDK.

Models are the cheapest option per provider, per docs/LLM_Providers.md:
- OpenAI: gpt-5-nano (cheapest paid tier)
- Google Gemini: gemini-3.1-flash-lite (free tier)
- Groq: openai/gpt-oss-20b (free tier)
- Anthropic: claude-haiku-4-5 (cheapest Anthropic model -- not listed in
  docs/LLM_Providers.md, which only covers OpenAI/Gemini/Groq/Mistral)

Run: uv run python src/concepts/01_direct_calls.py
"""

from dotenv import load_dotenv
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

SYSTEM_PROMPT = "You are a concise assistant."
PROMPT = "In one sentence, what is Retrieval-Augmented Generation?"


def call_openai() -> None:
    print("\n=== OpenAI direct call ===")
    client = OpenAI()  # reads OPENAI_API_KEY from the environment

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        max_completion_tokens=200,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": PROMPT},
        ],
    )

    print(response.choices[0].message.content)
    print(f"tokens: prompt={response.usage.prompt_tokens} "
          f"completion={response.usage.completion_tokens} "
          f"total={response.usage.total_tokens}")


def call_anthropic() -> None:
    print("\n=== Anthropic direct call ===")
    client = Anthropic()  # reads ANTHROPIC_API_KEY from the environment

    response = client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=200,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": PROMPT}],
    )

    text = next(block.text for block in response.content if block.type == "text")
    print(text)
    print(f"tokens: input={response.usage.input_tokens} output={response.usage.output_tokens}")


def call_groq() -> None:
    print("\n=== Groq direct call ===")
    client = Groq()  # reads GROQ_API_KEY from the environment; API is OpenAI-compatible

    # gpt-oss models reason internally before answering, so give them enough
    # completion budget or the whole budget gets spent on hidden reasoning.
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        max_completion_tokens=300,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": PROMPT},
        ],
    )

    print(response.choices[0].message.content)
    print(f"tokens: prompt={response.usage.prompt_tokens} "
          f"completion={response.usage.completion_tokens} "
          f"total={response.usage.total_tokens}")


def call_gemini() -> None:
    print("\n=== Gemini direct call ===")
    client = genai.Client()  # reads GOOGLE_API_KEY from the environment

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=PROMPT,
        config=genai_types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            max_output_tokens=200,
        ),
    )

    print(response.text)
    usage = response.usage_metadata
    print(f"tokens: prompt={usage.prompt_token_count} "
          f"candidates={usage.candidates_token_count} "
          f"total={usage.total_token_count}")


if __name__ == "__main__":
    call_openai()
    # call_anthropic()
    call_groq()
    call_gemini()
