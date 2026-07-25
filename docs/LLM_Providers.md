# LLM Providers and Cheapest Models

Free usage is the priority: within each category below, genuinely free-tier models are listed first, with paid fallbacks listed after for when a free tier's quota isn't enough.

## Category: Text Generation Models

### Free Tier Models (use these first)

| Company Name | Model                 | Model Provider | Free Tier Limits (July 2026)                                                                        |
| ------------ | --------------------- | -------------- | --------------------------------------------------------------------------------------------------- |
| Groq         | openai/gpt-oss-20b    | groq           | 30 RPM / 1,000 RPD / 8,000 TPM -- no credit card required                                           |
| Groq         | openai/gpt-oss-120b   | groq           | 30 RPM / 1,000 RPD / 8,000 TPM -- no credit card required                                           |
| Groq         | qwen/qwen3.6-27b      | groq           | 30 RPM / 1,000 RPD / 8,000 TPM -- preview, vision-capable, no credit card required                  |
| Google       | gemini-3.1-flash-lite | google_genai   | Free tier available; exact RPM/RPD/TPM are account-specific -- check aistudio.google.com/rate-limit |
| Google       | gemini-2.5-flash-lite | google_genai   | Free tier available (retiring Oct 16, 2026); exact quota -- check aistudio.google.com/rate-limit    |
| Google       | gemini-2.5-flash      | google_genai   | Free tier available (retiring Oct 16, 2026); exact quota -- check aistudio.google.com/rate-limit    |

### Cheapest Paid Fallbacks

| Company Name | Model                | Model Provider | Cost Filter   | Paid Rate (per 1M tokens)  |
| ------------ | -------------------- | -------------- | ------------- | -------------------------- |
| Mistral      | ministral-3b-latest  | mistralai      | Cheapest Paid | $0.04 Input / $0.04 Output |
| OpenAI       | gpt-5-nano           | openai         | Low Cost Paid | $0.05 Input / $0.40 Output |
| Mistral      | mistral-small-latest | mistralai      | Low Cost Paid | $0.10 Input / $0.30 Output |
| Mistral      | mistral-large-latest | mistralai      | Costly Paid   | $2.00 Input / $6.00 Output |

**Notes (as of July 2026):**

- Groq's free tier has no credit card requirement and no per-token billing — only rate limits gate usage. `openai/gpt-oss-20b`, `openai/gpt-oss-120b`, and `qwen/qwen3.6-27b` replace the previously-listed `llama-3.1-8b-instant`, `llama-3.3-70b-versatile`, `qwen/qwen3-32b`, `meta-llama/llama-4-scout-17b-16e-instruct`, and `mixtral-8x7b-32768` — all of those are deprecated or scheduled to shut down by August 16, 2026.
- Google's free tier now covers only Flash and Flash-Lite models (Pro moved to paid-only on April 1, 2026). The Gemini 2.5 Flash / Flash-Lite line is being retired on October 16, 2026 — migrate to `gemini-3.1-flash-lite` before then. Exact free-tier RPM/RPD/TPM figures vary by account/project and region, so they're best confirmed directly in AI Studio rather than trusted from a static table.
- Once a Google Cloud project has billing enabled, the free tier disappears entirely for that project — keep free-tier usage on a project without billing attached.
- Paid pricing reflects each provider's publicly listed on-demand rates and is subject to change; verify against the provider's official pricing page before relying on it for cost-sensitive workloads.

## Category: Text Embedding Models

### Free Tier Embedding Models (use these first)

| Company Name | Model                                  | Model Provider                                 | Vector Dimensions                               | Free Tier Limits (July 2026)                                                                                                   |
| ------------ | -------------------------------------- | ---------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Google       | gemini-embedding-001                   | google_genai                                   | 3072 (truncatable to 1536 / 768 via Matryoshka) | Free tier available for text-only embeddings; exact quota is account-specific -- check aistudio.google.com/rate-limit          |
| Hugging Face | sentence-transformers/all-MiniLM-L6-v2 | huggingface (Inference Providers or self-host) | 384                                             | Free via rate-limited Serverless Inference API, or self-host at zero cost -- open weights (Apache 2.0)                         |
| Hugging Face | BAAI/bge-m3                            | huggingface (Inference Providers or self-host) | 1024                                            | Free via rate-limited Serverless Inference API, or self-host at zero cost -- open weights, 100+ languages, 8,192-token context |

### Cheapest Paid Embedding Models

| Company Name | Model                          | Model Provider | Vector Dimensions                 | Cost Filter   | Paid Rate (per 1M tokens)       |
| ------------ | ------------------------------ | -------------- | --------------------------------- | ------------- | ------------------------------- |
| OpenAI       | text-embedding-3-small         | openai         | 1536 (configurable 256-1536)      | Cheapest Paid | $0.02 Input                     |
| Mistral      | mistral-embed                  | mistralai      | 1024                              | Low Cost Paid | $0.10 Input                     |
| Google       | gemini-embedding-001           | google_genai   | 3072 (configurable to 1536 / 768) | Low Cost Paid | $0.15 Input (beyond free quota) |
| OpenAI       | text-embedding-3-large         | openai         | 3072 (configurable 256-3072)      | Costly Paid   | $0.13 Input                     |
| Anthropic *  | voyage-3-large (via Voyage AI) | voyageai       | 1024 (configurable)               | Costly Paid   | ~$0.18 Input                    |

\* Anthropic does not offer a first-party embedding model. Voyage AI is Anthropic's officially recommended embeddings partner for Claude-based RAG and semantic search — it's a separate account and bill, not part of the Claude API. Groq does not currently expose a dedicated embeddings endpoint on GroqCloud (it's an inference platform for hosted chat/vision/audio models) — use one of the providers above, or self-host, for embeddings.

**Notes (as of July 2026):**

- "Vector Dimensions" lists the default output size; several models (OpenAI's `text-embedding-3-*`, Google's `gemini-embedding-001`, Voyage's `voyage-3-large`) support Matryoshka-style truncation to a smaller dimension count to save storage, at a small quality cost.
- Hugging Face Inference Providers pass through each upstream provider's own price with no markup — cost for a given model depends on which provider you route through (Groq, Together, Fireworks, etc.), separate from the genuinely free self-host / rate-limited-serverless path listed above.
- Paid pricing reflects each provider's publicly listed on-demand rates and is subject to change; verify against the provider's official pricing page before relying on it for cost-sensitive workloads.

## Category: Multimodal Models (Video, Image, Audio)

### Free Tier Multimodal Models (use these first)

| Modality               | Company Name | Model                                                                  | Model Provider                                 | Free Tier Limits (July 2026)                                                                                                                 |
| ---------------------- | ------------ | ---------------------------------------------------------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Image                  | Google       | gemini-3-flash-image ("Nano Banana")                                   | google_genai                                   | Free tier in AI Studio; historically hundreds of images/day, now governed by a compute-credit system -- check aistudio.google.com/rate-limit |
| Audio (speech-to-text) | Groq         | whisper-large-v3-turbo                                                 | groq                                           | 2,000 requests/day, ~7,200 audio-seconds/hour (~2 hrs audio per clock-hour) -- no credit card required                                       |
| Audio (speech-to-text) | Groq         | whisper-large-v3                                                       | groq                                           | Same free-tier quota as turbo; higher accuracy, slower                                                                                       |
| Image / Audio          | Hugging Face | e.g. stabilityai/stable-diffusion-xl-base-1.0, openai/whisper-large-v3 | huggingface (Inference Providers or self-host) | Free via rate-limited Serverless Inference API, or self-host at zero cost -- open weights                                                    |

### Cheapest Paid Multimodal Models

| Modality    | Company Name | Model                                             | Model Provider | Cost Filter   | Paid Rate                                              |
| ----------- | ------------ | ------------------------------------------------- | -------------- | ------------- | ------------------------------------------------------ |
| Image       | OpenAI       | gpt-image-1-mini (low quality)                    | openai         | Cheapest Paid | $0.005 / image (1024x1024)                             |
| Audio (STT) | Groq         | whisper-large-v3-turbo (beyond free quota)        | groq           | Cheapest Paid | $0.04 / hour of audio                                  |
| Audio (STT) | OpenAI       | whisper-1                                         | openai         | Low Cost Paid | $0.006 / minute of audio                               |
| Image       | Google       | gemini-3-flash-image ("Nano Banana 2"), paid tier | google_genai   | Low Cost Paid | ~$0.045 / image (512px) up to ~$0.15 (4K)              |
| Video       | Google       | veo-3.1-lite                                      | google_genai   | Low Cost Paid | ~$0.05 / second (720p, no audio)                       |
| Audio (TTS) | Mistral      | voxtral-tts                                       | mistralai      | Low Cost Paid | $16 / 1M characters                                    |
| Audio (TTS) | OpenAI       | gpt-4o-mini-tts                                   | openai         | Low Cost Paid | $0.60 / 1M input tokens + $0.015 / minute audio output |
| Audio (TTS) | Groq         | playai-tts (Dialog v1.0)                          | groq           | Costly Paid   | $50 / 1M characters                                    |
| Video       | OpenAI       | sora-2                                            | openai         | Costly Paid   | $0.10 / second                                         |

**Notes (as of July 2026):**

- **Anthropic (Claude) has no native image, video, or audio generation models.** Claude accepts image input (vision) but does not generate images, video, or audio — there is nothing to list for Anthropic in this category.
- **Mistral** has no native image or video generation model. Vision is _input-only_, bundled into Mistral Small/Large (formerly the separate Pixtral line); Voxtral covers audio, split into `voxtral-tts` (generation, listed above) and separate Voxtral transcription/understanding models.
- **Groq** does not host native image or video generation models — it's an inference platform for hosted open-weight chat, vision-input, and audio (STT/TTS) models, which is why it only appears under Image/Video as "not offered."
- Video pricing is quoted per second of generated output and varies further by resolution and audio track (e.g. `sora-2-pro` and `veo-3.1` standard/fast tiers run well above the lite/mini rates shown here) — treat the rates above as a floor, not a full price list.
- Paid pricing reflects each provider's publicly listed on-demand rates and is subject to change; verify against the provider's official pricing page before relying on it for cost-sensitive workloads.
