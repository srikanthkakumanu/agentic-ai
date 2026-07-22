# Ollama

[Ollama](https://www.ollama.com) is an LLM inference server written in Go, for running open-weight models locally.

## Installation

```bash
brew install ollama
```

## Pulling Models

`ollama pull` downloads a model without running it:

```bash
ollama pull gemma3:270m  # Google Gemma lightweight LLM
ollama pull phi3         # Microsoft lightweight LLM
ollama pull gpt-oss      # OpenAI open-weight GPT LLM
ollama pull llama3.2     # Meta Llama 3.2 LLM
```

## Running LLMs Locally

`ollama run` pulls the model if it isn't already local, then drops into an interactive prompt:

```bash
ollama run gemma3:270m
```

## Accessing Local LLMs via the API

Ollama exposes an OpenAI-compatible API, so any OpenAI-client code can point at it by swapping the base URL:

```text
http://localhost:11434/v1
```
