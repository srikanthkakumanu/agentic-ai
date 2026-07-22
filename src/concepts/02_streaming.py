"""Streaming responses token-by-token from each provider.

Run: uv run python src/concepts/02_streaming.py
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

PROMPT = "List three benefits of streaming LLM responses, one sentence each."


def stream_openai() -> None:
    print("\n=== OpenAI streaming ===")
    client = OpenAI()

    stream = client.chat.completions.create(
        model=OPENAI_MODEL,
        max_completion_tokens=300,
        messages=[{"role": "user", "content": PROMPT}],
        stream=True,
        stream_options={"include_usage": True},  # last chunk carries usage totals
    )

    usage = None
    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
        if chunk.usage:
            usage = chunk.usage

    print()
    if usage:
        print(f"tokens: prompt={usage.prompt_tokens} completion={usage.completion_tokens}")


def stream_anthropic() -> None:
    print("\n=== Anthropic streaming ===")
    client = Anthropic()

    with client.messages.stream(
        model=ANTHROPIC_MODEL,
        max_tokens=300,
        messages=[{"role": "user", "content": PROMPT}],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)

        final_message = stream.get_final_message()

    print()
    print(f"tokens: input={final_message.usage.input_tokens} output={final_message.usage.output_tokens}")


def stream_groq() -> None:
    print("\n=== Groq streaming ===")
    client = Groq()

    # Unlike OpenAI, the Groq SDK doesn't support stream_options -- usage
    # for a streamed response arrives on the final chunk's `x_groq.usage`.
    stream = client.chat.completions.create(
        model=GROQ_MODEL,
        max_completion_tokens=300,
        messages=[{"role": "user", "content": PROMPT}],
        stream=True,
    )

    last_chunk = None
    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
        last_chunk = chunk

    print()
    if last_chunk is not None and last_chunk.x_groq is not None:
        usage = last_chunk.x_groq.usage
        print(f"tokens: prompt={usage.prompt_tokens} completion={usage.completion_tokens}")


def stream_gemini() -> None:
    print("\n=== Gemini streaming ===")
    client = genai.Client()

    stream = client.models.generate_content_stream(
        model=GEMINI_MODEL,
        contents=PROMPT,
        config=genai_types.GenerateContentConfig(max_output_tokens=300),
    )

    last_chunk = None
    for chunk in stream:
        if chunk.text:
            print(chunk.text, end="", flush=True)
        last_chunk = chunk

    print()
    if last_chunk is not None and last_chunk.usage_metadata:
        usage = last_chunk.usage_metadata
        print(f"tokens: prompt={usage.prompt_token_count} candidates={usage.candidates_token_count}")


if __name__ == "__main__":
    stream_openai()
    # stream_anthropic()
    stream_groq()
    stream_gemini()
