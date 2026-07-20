# LLM Providers and Cheapest Models

Free usage is the priority: the table below lists genuinely free-tier models first. Paid fallbacks are listed after, for when a free tier's quota isn't enough.

## Free Tier Models (use these first)

| Company Name | Model                 | Model Provider | Free Tier Limits (July 2026)                                                                        |
| ------------ | --------------------- | -------------- | --------------------------------------------------------------------------------------------------- |
| Groq         | openai/gpt-oss-20b    | groq           | 30 RPM / 1,000 RPD / 8,000 TPM -- no credit card required                                           |
| Groq         | openai/gpt-oss-120b   | groq           | 30 RPM / 1,000 RPD / 8,000 TPM -- no credit card required                                           |
| Groq         | qwen/qwen3.6-27b      | groq           | 30 RPM / 1,000 RPD / 8,000 TPM -- preview, vision-capable, no credit card required                  |
| Google       | gemini-3.1-flash-lite | google_genai   | Free tier available; exact RPM/RPD/TPM are account-specific -- check aistudio.google.com/rate-limit |
| Google       | gemini-2.5-flash-lite | google_genai   | Free tier available (retiring Oct 16, 2026); exact quota -- check aistudio.google.com/rate-limit    |
| Google       | gemini-2.5-flash      | google_genai   | Free tier available (retiring Oct 16, 2026); exact quota -- check aistudio.google.com/rate-limit    |

## Cheapest Paid Fallbacks

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
