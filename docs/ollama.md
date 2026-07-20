# Ollama

[Ollama](https://www.ollama.com) is a LLM inference server written in Rust.

## Installation

```bash
brew install ollama
```

## Importing/Installing LLMs

```bash
ollama install gemma3:270m # Google Gemini lightweight LLM 
ollama install phi3 # Microsoft lightweight LLM
ollama install gpt-oss # OpenAI lightweight GPT LLM
ollama install llama3.2 # Meta LLaMA 3.2 LLM
```

## Running LLMs Locally using Ollama

```bash
ollama run gemma3:270m
```

## Accessing Local LLMs via Ollama

We can access it using http://localhost:11434/v1

