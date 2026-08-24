# 🧭 Production Agentic AI + Agentic Software Engineering

## 🚀 Integrated Learning Syllabus — August 2026 Edition

> **Two complementary paths. One production-grade engineering track.**  
> Build reliable AI/agent systems **and** engineer the AI-native development environment used to deliver them.

> **Purpose:** A single, ordered curriculum combining two complementary paths:
>
> - **Path 1 — Agentic Coding / Agentic Engineering / Harness Engineering:** Claude Code and equivalent coding-agent workflows; layered context, `CLAUDE.md`, rules, skills, subagents, commands, hooks, MCP, plugins, deterministic guardrails, and reusable engineering harnesses.
> - **Path 2 — Agentic AI / LLM Application Engineering:** direct LLM APIs, structured outputs, prompt/context engineering, agent patterns, RAG, memory, LangChain/LangGraph, vendor agent SDKs, MCP/A2A, cloud agent platforms, evaluation, observability, security, and production operations.
>
> **Recommended emphasis:** Learn **Path 2 as the engineering foundation**, while using Path 1 throughout as the development workflow. Approximate initial depth allocation: **75% Path 2 / 25% Path 1**, moving toward **60% / 40%** after production-agent fundamentals are established.
>
> **Primary stack:** Python + Java/Spring, OpenAI/Anthropic SDKs, LangChain/LangGraph, Spring AI, MCP, PostgreSQL/pgvector, AWS, Docker/Kubernetes, OpenTelemetry.
>
> **Outcome:** Be able both to **build production AI/agent systems** and to **engineer the coding-agent environment used to build and maintain them**.
> **How to use each bullet:** Treat each item as a mini learning objective. First understand **what it is and why it exists**, then complete the **Practice** action so you can explain and demonstrate it rather than only recognize the term.


---


## 📑 Table of Contents

- [🗺️ Learning Order at a Glance](#️-learning-order-at-a-glance)
- [🧠 Phase 0 — Mental Models](#-phase-0--mental-models-two-paths-one-engineering-discipline)
- [🐍 Phase 1 — Python/Java + LLM Fundamentals](#-phase-1--pythonjava-ai-engineering-foundation--llm-fundamentals)
- [🔌 Phase 2 — Direct Model APIs & Tool Calling](#-phase-2--direct-model-apis-structured-outputs--tool-calling)
- [🧩 Phase 3 — Prompt & Context Engineering](#-phase-3--prompt-engineering-context-engineering--composition-patterns)
- [🤖 Phase 4 — Agent Internals](#-phase-4--agent-internals--reasoningworkflow-patterns)
- [🟡 Phase 5 — Claude Code Fundamentals](#-phase-5--claude-code-fundamentals--layered-context)
- [📚 Phase 6 — Retrieval Engineering](#-phase-6--retrieval-engineering-loading-splitting-chunking--basic-rag)
- [🕸️ Phase 7 — Advanced / Graph / Agentic RAG](#️-phase-7--advanced-graph--agentic-rag)
- [🧠 Phase 8 — State & Memory](#-phase-8--state-memory--long-running-agent-context)
- [🔀 Phase 9 — LangChain & LangGraph](#-phase-9--langchain--langgraph-orchestration)
- [🧰 Phase 10 — Claude Skills, Rules & Subagents](#-phase-10--claude-code-skills-rules-commands--subagents)
- [👥 Phase 11 — Multi-Agent & Vendor SDKs](#-phase-11--multi-agent-architecture--vendor-agent-sdks)
- [🔗 Phase 12 — MCP](#-phase-12--mcp-build-consume-secure--govern)
- [🏗️ Phase 13 — Agentic Engineering](#️-phase-13--agentic-engineering-plan--execute--verify)
- [🛡️ Phase 14 — Harness Engineering](#️-phase-14--harness-engineering-hooks-permissions-sandboxes--guardrails)
- [🧩 Phase 15 — Plugins](#-phase-15--plugins-reusable-agent-capabilities--distribution)
- [☁️ Phase 16 — Cloud](#️-phase-16--cloud-agent-platforms--deployment)
- [📈 Phase 17 — AgentOps](#-phase-17--agentops-evals-observability-security--reliability)
- [🔄 Phase 18 — AI-Native SDLC](#-phase-18--ai-native-sdlc-cicd-testing-code-review--governance)
- [☕ Phase 19 — Java/Spring Track](#-phase-19--javaspring-enterprise-agentic-ai-track)
- [🏆 Phase 20 — Integrated Capstone](#-phase-20--integrated-production-capstone)
- [🎯 Competency Matrix](#-competency-matrix)
- [✅ Completion Criteria](#-completion-criteria)

---

## 🏷️ Legend


| Badge | Track | Meaning |
|---|---|---|
| 🟡 **P1** | Agentic Coding / Engineering / Harness | Engineer **with** coding agents |
| 🟢 **P2** | Agentic AI / LLM Application Engineering | Engineer **AI/agent systems** |
| 🟣 **P1+P2** | Integrated | Shared capability across both paths |

> **Depth scale:** **Deep** = build, explain, troubleshoot and defend trade-offs · **Working** = implement confidently · **Aware** = compare and choose appropriately


| Path      | Meaning                                                    |
|:----------|:-----------------------------------------------------------|
| **P1**    | Agentic Coding / Agentic Engineering / Harness Engineering |
| **P2**    | Agentic AI / LLM Application Engineering                   |
| **P1+P2** | Shared or deliberately integrated competency               |

| Depth       | Expectation                                                                         |
|:------------|:------------------------------------------------------------------------------------|
| **Deep**    | Build independently, explain internals/trade-offs, troubleshoot production failures |
| **Working** | Implement confidently with documentation; understand architecture and limitations   |
| **Aware**   | Recognize, compare, and know when it is appropriate                                 |


---


# 🗺️ Learning Order at a Glance

| Order | Phase                                                           | Primary Path | Depth   |
|------:|:----------------------------------------------------------------|:-------------|:--------|
|     0 | Mental Models: Two Paths, One Engineering Discipline            | P1+P2        | Deep    |
|     1 | Python/Java AI Engineering Foundation + LLM Fundamentals        | P2           | Deep    |
|     2 | Direct Model APIs, Structured Outputs & Tool Calling            | P2           | Deep    |
|     3 | Prompt Engineering, Context Engineering & Composition Patterns  | P2           | Deep    |
|     4 | Agent Internals & Reasoning/Workflow Patterns                   | P2           | Deep    |
|     5 | Claude Code Fundamentals & Layered Context                      | P1           | Deep    |
|     6 | Retrieval Engineering: Loading, Splitting, Chunking & Basic RAG | P2           | Deep    |
|     7 | Advanced, Graph & Agentic RAG                                   | P2           | Deep    |
|     8 | State, Memory & Long-Running Agent Context                      | P2           | Deep    |
|     9 | LangChain & LangGraph Orchestration                             | P2           | Deep    |
|    10 | Claude Code Skills, Rules, Commands & Subagents                 | P1           | Deep    |
|    11 | Multi-Agent Architecture & Vendor Agent SDKs                    | P2           | Deep    |
|    12 | MCP: Build, Consume, Secure & Govern                            | P1+P2        | Deep    |
|    13 | Agentic Engineering: Plan → Execute → Verify                    | P1           | Deep    |
|    14 | Harness Engineering: Hooks, Permissions, Sandboxes & Guardrails | P1           | Deep    |
|    15 | Plugins, Reusable Agent Capabilities & Distribution             | P1           | Working |
|    16 | Cloud Agent Platforms & Deployment                              | P2           | Deep    |
|    17 | AgentOps: Evals, Observability, Security & Reliability          | P2           | Deep    |
|    18 | AI-Native SDLC: CI/CD, Testing, Code Review & Governance        | P1+P2        | Deep    |
|    19 | Java/Spring Enterprise Agentic AI Track                         | P2           | Deep    |
|    20 | Integrated Production Capstone                                  | P1+P2        | Deep    |


---


---

# 🧠 Phase 0 — Mental Models: Two Paths, One Engineering Discipline

> 🟣 **Path:** `P1+P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 0.1 Distinguish the two paths

- **Building with an agent** vs **building an agent** — Distinguish using an AI coding agent to create software from embedding an agent as a runtime component of the product. **Practice:** classify a few features from one of your systems into “AI helps build it” versus “AI runs inside it,” and explain the architecture implications.
- Coding agent as engineering collaborator vs LLM/agent as a runtime component of your product.
- Why `CLAUDE.md`, skills, hooks, and coding subagents do not replace RAG, runtime memory, model APIs, evals, or application-agent orchestration.
- Why application-agent frameworks do not replace a well-engineered coding harness.

## 0.2 Agentic Coding

- **One coding agent operating over repository context** — Agentic Coding usually starts with one coding agent that can inspect and modify a bounded repository to complete a scoped task. **Practice:** give Claude Code one small feature with explicit acceptance criteria and review every changed file before accepting it.
- **Read → reason/plan → edit → execute → inspect → iterate** — This is the core coding-agent feedback loop: gather context, decide what to change, make the change, run tools/tests, inspect evidence, and refine. **Practice:** narrate this loop while implementing a small API change and stop the agent whenever it skips verification.
- **Human review of diffs and side effects** — Generated code can compile while still violating architecture, security, or business constraints, so a human must review both the diff and any external side effects. **Practice:** review one AI-generated PR exactly as you would review a teammate’s PR and record defects the agent missed.
- **Appropriate autonomy boundaries** — Autonomy should increase only when the action is reversible, well-scoped, observable, and protected by deterministic checks. **Practice:** define which actions your coding agent may perform automatically and which require approval, such as dependency changes, migrations, or deployment.
- **Task scoping and acceptance criteria** — Agents perform better when the task has a clear boundary, expected files/components, and measurable completion criteria. **Practice:** rewrite an ambiguous feature request into a scoped task with inputs, outputs, constraints, tests, and explicit “done” conditions.

## 0.3 Agentic Engineering

- **Plan → Execute → Verify** — Agentic Engineering separates understanding/planning from implementation and independent verification to reduce premature or biased changes. **Practice:** require a written plan before non-trivial work, then verify the result with tests and a separate reviewer role.
- Specialized roles: planner, implementer, tester, reviewer, security reviewer.
- **Separation of concerns between agents** — Different agents should own distinct responsibilities so implementation, testing, and review do not collapse into one biased context. **Practice:** assign author, tester, and reviewer roles with non-overlapping responsibilities for one feature.
- **Context isolation** — Each agent should receive only the context needed for its role, which reduces token waste, accidental coupling, and reviewer bias. **Practice:** compare a reviewer given the entire implementation conversation with one given only requirements, diff, and test evidence.
- **Human checkpoints at consequential boundaries** — Irreversible or high-impact actions such as deleting data, changing access controls, or deploying to production should pause for explicit human approval. **Practice:** add an approval checkpoint before one side-effecting action in your agent workflow.

## 0.4 Harness Engineering

- **Engineer the environment rather than merely improve prompts** — Harness Engineering improves reliability by changing tools, permissions, tests, hooks, and execution boundaries instead of expecting better wording alone to control the model. **Practice:** take one important “do not” instruction and enforce it with code or configuration rather than prose.
- **Context, tools, permissions, hooks, sandboxes, tests, feedback loops, observability** — Learn what **Context, tools, permissions, hooks, sandboxes, tests, feedback loops, observability** means in Harness Engineering, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Deterministic enforcement vs probabilistic instructions** — A prompt asks the model to comply probabilistically, while a hook, permission, test, or policy can enforce a rule deterministically. **Practice:** identify five critical rules and move at least two of them from instructions into executable checks.
- Principle: if a rule **must** hold, enforce it outside the model where practical.

## 0.5 Product Agentic AI

- Agent = model + instructions/context + tools + state/memory + control loop + goal + guardrails.
- **Agent vs deterministic workflow** — An agent chooses actions dynamically, whereas a deterministic workflow follows predefined transitions; use the latter when the business path is known and repeatable. **Practice:** model the same use case both ways and justify which parts genuinely need model judgment.
- **Autonomy spectrum** — Agent systems range from advisory-only to fully tool-executing workflows, and the right level depends on risk, reversibility, and observability. **Practice:** assign autonomy levels to common tasks such as code explanation, code editing, PR creation, refund approval, and deployment.
- When **not** to use an agent — Do not introduce an agent where deterministic code, rules, search, or workflow orchestration can solve the problem more reliably and cheaply. **Practice:** list three requirements where an agent would add unnecessary uncertainty and implement one as a normal service/workflow.

### 🧪 Project Assignment — Architecture Classification Exercise

Take 15 requirements from a realistic payments platform. Classify each as: 1. conventional software, 2. deterministic AI workflow, 3. application agent, 4. coding-agent task, 5. harness concern.

For every classification, document why additional autonomy is or is not justified.


---


---

# 🐍 Phase 1 — Python/Java AI Engineering Foundation + LLM Fundamentals

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 1.1 Python for enterprise engineers

- **Python 3.12/3.13** — Use a current Python runtime so you learn the language features and package ecosystem used by modern AI SDKs. **Practice:** create a `uv`-managed project, pin the Python version, and run it locally and in Docker.
- **Type hints, protocols, dataclasses, generators** — These features let you build typed, composable Python services that are easier to test and reason about, especially when passing structured agent state. **Practice:** model tool inputs/outputs and agent state with typed classes and use a generator for a streaming example.
- `async`/`await`, concurrency and I/O — Most agent applications are I/O-heavy because they call models, tools, databases, and APIs, so asynchronous programming directly affects latency and throughput. **Practice:** call two independent tools concurrently and compare latency with sequential execution.
- **Context managers and decorators** — Context managers handle lifecycle/resources safely, while decorators are useful for cross-cutting concerns such as tracing, retries, authorization, and timing. **Practice:** write a timing/tracing decorator and a context manager around a mock external resource.
- `uv`, Ruff, pytest — Use `uv` for fast dependency/environment management, Ruff for linting/formatting, and pytest for automated tests. **Practice:** configure all three in one repository and make the test/lint commands part of CI.
- **Pydantic v2** — Pydantic turns untrusted model or API output into validated Python objects and is central to production structured-output workflows. **Practice:** define nested schemas with enums and validation rules, then deliberately feed malformed output to observe validation failures.
- **FastAPI** — FastAPI is a lightweight typed web framework well suited to exposing AI services, streaming endpoints, and tool APIs. **Practice:** expose one model-backed endpoint and add request/response schemas, error handling, and an async streaming route.
- Map concepts to Java records, generics, Bean Validation, Jackson and `CompletableFuture`.

## 1.2 Java continuity

- **Modern Java 21+** — Keep your enterprise Java skills current because Java remains highly relevant for production integration around AI services. **Practice:** use records, sealed types, virtual threads or modern concurrency where appropriate in a small AI-facing Spring service.
- **Spring Boot** — Spring Boot provides the enterprise service foundation for security, configuration, observability, APIs, and integration around AI capabilities. **Practice:** build a small Spring Boot service that calls an AI component and exposes health, metrics, and configuration cleanly.
- **HTTP clients and reactive/asynchronous integration** — Learn what **HTTP clients and reactive/asynchronous integration** means in Java continuity, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Jackson/schema validation** — Jackson maps JSON into Java types, while validation protects your application from malformed model/tool payloads. **Practice:** define DTOs/records for structured model output and reject invalid fields before business logic executes.
- **Resilience4j** — Resilience4j supplies timeouts, retries, circuit breakers, rate limiting, and bulkheads for unreliable external model/tool dependencies. **Practice:** wrap an LLM or mock tool call with a timeout, bounded retry, and circuit breaker, then simulate failures.
- Why Python should be learned without abandoning Java enterprise leverage.

## 1.3 LLM fundamentals

- **Tokens and tokenization** — Tokens are the units models read and generate, so token count affects context capacity, latency, and cost. **Practice:** tokenize representative prompts/documents and estimate input/output token budgets for one workflow.
- **Context windows** — The context window is the model’s finite working input space, including instructions, history, retrieved text, tool results, and output allowance. **Practice:** design a token budget that reserves space for each context source instead of filling the window indiscriminately.
- **Transformer/attention intuition** — Understand attention at a conceptual level so you can reason about why models weigh context differently and why long prompts can dilute important information. **Practice:** explain attention and position effects in plain language and relate them to context placement decisions.
- **Inference vs training** — Training changes model parameters; inference uses a trained model to generate results from prompts and context. **Practice:** be able to explain which production problems require prompt/RAG/tool changes versus fine-tuning or model training.
- **Temperature/top-p and deterministic output needs** — Sampling controls affect variability, but production correctness should rely on schemas and validation rather than assuming a low temperature guarantees truth. **Practice:** run the same prompt at several sampling settings and measure output consistency.
- **Hallucination and uncertainty** — Models can produce fluent but unsupported claims, so systems need grounding, abstention, validation, and explicit uncertainty handling. **Practice:** create adversarial questions that lack evidence and require the application to abstain rather than invent an answer.
- **Reasoning models vs general chat/instruction models** — Reasoning-oriented models spend more compute on complex problem solving, while general models may be faster and cheaper for routine extraction or transformation. **Practice:** benchmark both model types on one simple and one complex task and compare quality, latency, and cost.
- **Closed vs open-weight models** — Closed models offer managed capabilities and APIs, while open-weight models provide more control over hosting, privacy, tuning, and cost structure. **Practice:** compare one managed model with one locally served/open-weight model for deployment constraints and total operational responsibility.
- **Cost/latency/quality trade-offs** — Production model choice is a multi-objective decision rather than a single benchmark score. **Practice:** create a small evaluation matrix across at least two models and choose a default plus fallback based on measurable requirements.

## 1.4 Embeddings fundamentals

- **Vector representations** — Embeddings map text or other content into numeric vectors whose geometry captures semantic relationships. **Practice:** embed a small set of related and unrelated sentences and inspect which examples cluster together.
- **Cosine similarity/dot product** — These similarity functions rank vectors by closeness and are the mathematical basis of many semantic retrieval systems. **Practice:** calculate similarity for a few vectors manually or in Python and compare it with vector-database results.
- **Embedding dimensionality** — Dimensionality is the size of an embedding vector and affects storage, index cost, and the representation space available to the model. **Practice:** inspect dimensions from different embedding models and estimate storage for your target corpus.
- **Semantic similarity vs lexical similarity** — Semantic retrieval matches meaning even when wording differs, whereas lexical search such as BM25 rewards shared terms. **Practice:** create queries where semantic and lexical retrieval disagree, then explain why hybrid search can outperform either alone.
- **Embedding model selection** — Choose embedding models based on language/domain coverage, retrieval quality, dimension, latency, cost, and deployment constraints. **Practice:** evaluate two embedding models on a small labeled query-document set rather than choosing by popularity.

### 🧪 Additional Project Assignment — Smart Ticket Classifier API

Build a **FastAPI** service that classifies free-text support tickets into structured JSON fields such as category, priority, sentiment, and destination team using direct OpenAI/Anthropic SDK calls plus Pydantic validation. Add streaming, retry with exponential backoff, per-request token/cost logging, pytest coverage, and Docker packaging.

### 🧪 Project Assignment — Multi-Model Playground

Build a FastAPI service that calls at least two model providers, records latency/token usage/cost, validates responses with Pydantic, and exposes a common provider-neutral interface. Add pytest tests and Docker packaging.


---


---

# 🔌 Phase 2 — Direct Model APIs, Structured Outputs & Tool Calling

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 2.1 Learn direct SDKs before frameworks

- **OpenAI SDK** — Learn the provider SDK directly so you understand messages, structured outputs, tools, streaming, usage metadata, and errors before a framework abstracts them. **Practice:** build one end-to-end model call with streaming, schema validation, and a tool call.
- **Anthropic SDK** — Use the Anthropic SDK to learn Claude-specific message/tool patterns and compare provider behavior without relying on a framework. **Practice:** implement the same small task you built with OpenAI and document API/model differences.
- **Gemini API awareness** — You should understand Gemini’s basic API and multimodal/tool capabilities even if it is not your primary provider. **Practice:** port one structured-output example to Gemini and note compatibility gaps in your abstraction layer.
- **Request/response lifecycle** — Trace how an application constructs a model request, sends it, receives model content/tool requests, validates results, and records usage. **Practice:** log every stage of a request and draw a sequence diagram for one model interaction.
- System/developer/user instruction roles where supported.
- **Streaming** — Streaming returns partial output/events as they are generated, improving perceived latency and enabling live agent progress. **Practice:** expose a streaming endpoint and handle disconnects, partial output, and final usage metadata correctly.
- **Retries and backoff** — Transient provider failures should be retried carefully with bounded exponential backoff and jitter rather than immediate repeated calls. **Practice:** simulate 429/5xx failures and verify retry limits do not create retry storms.
- **Timeouts** — Timeouts bound dependency delay and prevent one hung model/tool from consuming the entire request budget. **Practice:** define per-call and end-to-end deadlines and test timeout recovery.
- **Rate limits** — Providers restrict request/token throughput, so applications must shape concurrency and respond correctly to throttling. **Practice:** implement a basic limiter/queue and verify the client handles 429 responses without data loss.
- **Token accounting** — Capture input, output, cached, and reasoning/token usage where available so cost and capacity can be attributed to features and users. **Practice:** log usage per request and calculate cost-per-successful-task for a small evaluation set.
- **Error taxonomy** — Separate validation, authentication, throttling, timeout, provider, tool, and application errors because each requires a different recovery strategy. **Practice:** define typed error categories and map each to retry, fallback, user error, or escalation behavior.

## 2.2 Structured generation

- **JSON output** — JSON is useful for machine-readable results, but syntactically valid JSON alone does not guarantee that required business fields are correct. **Practice:** request JSON output and validate it before any downstream action.
- **Schema-constrained generation** — Schema constraints narrow the model’s allowed output shape and reduce parsing failures. **Practice:** define a strict schema with nested objects and enums and test invalid/edge-case inputs.
- **Pydantic models** — Pydantic models provide a typed contract between model output and application code. **Practice:** use Pydantic for tool arguments and final outputs and handle validation errors explicitly.
- **Enum and nested schemas** — Enums constrain decisions to known values, while nested schemas represent richer business structures without free-form parsing. **Practice:** model a realistic payment case with nested customer/transaction fields and bounded status values.
- **Optional vs required fields** — Required fields express invariants, while optional fields should only be used when absence has a legitimate meaning. **Practice:** make the schema intentionally strict and document why each optional field may be missing.
- **Validation and repair strategies** — When output fails validation, decide whether to reject, retry with validation feedback, repair deterministically, or escalate. **Practice:** implement a bounded retry path for malformed structured output and measure its success rate.
- **Structured outputs as an API contract** — Treat model output like any other external API: version the schema, validate it, and protect downstream consumers from silent shape changes. **Practice:** add schema tests and a versioning strategy to one model-backed endpoint.

## 2.3 Tool/function calling

- **Tool definitions and schemas** — A tool definition tells the model what capability exists and what typed arguments it accepts. **Practice:** design tools with narrow responsibilities, explicit schemas, and descriptions that distinguish them clearly from one another.
- **Tool selection** — The model may choose which tool to call based on descriptions and context, so selection quality is part of agent correctness. **Practice:** create overlapping tools, evaluate misroutes, then improve their names/descriptions or add deterministic routing.
- **Arguments** — Tool arguments are model-generated inputs and therefore untrusted data that must be validated and authorized. **Practice:** validate ranges, identifiers, tenant scope, and required fields before executing the tool.
- **Parallel tool calls** — Independent tools can be invoked concurrently to reduce end-to-end latency, but only when they do not depend on one another or conflict through side effects. **Practice:** parallelize two read-only tools and compare timing with sequential calls.
- **Tool result messages** — Tool results feed external evidence back into the model and should be concise, structured, provenance-aware, and safe from injection. **Practice:** standardize tool result envelopes with status, data, source, and error fields.
- **Multiple-turn tool loops** — Agents often alternate between model decisions and tool observations until the goal or a stop condition is reached. **Practice:** implement a bounded loop and log each decision/action/observation as a traceable event.
- **Tool error handling** — A tool failure should become structured state that the agent can retry, choose an alternative for, or escalate—not an opaque exception. **Practice:** simulate timeout, validation, authorization, and not-found failures and define behavior for each.
- **Tool descriptions as routing signals** — The wording and specificity of a tool description materially affect model selection. **Practice:** run an evaluation set against alternate descriptions and choose the version with fewer incorrect tool calls.
- **Idempotency for tools with side effects** — Side-effecting tools must tolerate retries without duplicating actions such as payments, emails, or account changes. **Practice:** add idempotency keys and verify that replaying the same tool request does not repeat the side effect.

## 2.4 Provider abstraction

- When an internal abstraction is worthwhile.
- **LiteLLM or equivalent gateway/abstraction concepts** — A model gateway can normalize provider access, routing, observability, keys, and fallbacks, but it also introduces another operational layer. **Practice:** route two providers through one abstraction and document what provider-specific features you lose or retain.
- **Avoiding lowest-common-denominator abstractions** — Learn what **Avoiding lowest-common-denominator abstractions** means in Provider abstraction, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Model routing and fallback** — Routing selects a model based on task/risk/cost, while fallback handles provider or quality failure. **Practice:** implement one simple routing rule plus a fallback and verify that output contracts remain consistent.

### 🧪 Project Assignment — Payment Dispute Assistant Core

Without LangChain or LangGraph, build a service that: - accepts a payment dispute, - returns structured classification, - calls customer/transaction mock tools, - handles tool failures, - streams progress, - logs token/cost/latency, - supports OpenAI and Anthropic behind the same application interface.


---


---

# 🧩 Phase 3 — Prompt Engineering, Context Engineering & Composition Patterns

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 3.1 Production prompt engineering

- **Instruction hierarchy** — Models receive instructions from multiple sources with different precedence, so conflicts must be designed deliberately. **Practice:** write a prompt stack with system/developer/user constraints and test conflicting user instructions.
- **Role/task/context/constraints/output contract** — A production prompt should clearly state who/what the model is doing, the task, relevant context, hard constraints, and the required output shape. **Practice:** refactor one vague prompt into these components and compare evaluation results.
- **Few-shot prompting** — Few-shot examples teach desired behavior by demonstration and are especially useful for nuanced classification or formatting. **Practice:** add two to five high-quality examples, including one edge case, and measure whether consistency improves.
- **Delimiters and XML-style structure** — Explicit sections make prompts easier for both humans and models to parse and reduce accidental blending of instructions and data. **Practice:** wrap instructions, source data, and expected output in distinct tagged blocks.
- **Prompt templates** — Templates make prompts parameterized and reusable while keeping instructions separate from runtime values. **Practice:** build typed template inputs and ensure untrusted user data cannot alter fixed instructions.
- **Prompt versioning** — Prompts change production behavior and should be versioned like code so regressions can be traced and rolled back. **Practice:** store prompt versions with evaluation results and include the active version in traces.
- **Prompt-as-code** — Treat prompts as reviewed, tested, deployable artifacts rather than ad-hoc strings hidden in application logic. **Practice:** move prompts into dedicated files/modules and require code review plus automated evaluation for changes.
- **Regression tests** — A prompt/model change can silently break previously solved cases, so maintain a stable evaluation set that must continue to pass. **Practice:** capture known-good examples and run them automatically in CI.

## 3.2 Reasoning-aware prompting

- Do not depend on exposing hidden chain-of-thought.
- Request concise rationale/evidence when needed.
- **Decomposition** — Break complex tasks into smaller decisions or transformations when one-shot generation is unreliable. **Practice:** compare a single large prompt with a two- or three-stage pipeline and measure accuracy/cost.
- **Self-checks** — A self-check asks the model to verify explicit constraints or evidence before finalizing, but it should complement rather than replace external validation. **Practice:** add a checklist-based verification step and compare it with deterministic validators.
- **Critique/revision** — One model pass generates a draft and another critiques it against criteria before revision. **Practice:** implement a bounded generate→critique→revise loop and stop when measurable criteria are satisfied.
- **Model-native reasoning controls** — Learn what **Model-native reasoning controls** means in Reasoning-aware prompting, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.

## 3.3 Prompt composition patterns

- **Prompt chaining** — Prompt chaining decomposes a task into ordered model calls whose outputs become controlled inputs to the next step. **Practice:** build a two-stage extract→summarize or classify→respond workflow with schema validation between stages.
- **Routing** — Routing chooses a specialized prompt, model, retriever, or agent based on the request. **Practice:** implement a small intent router and evaluate confusion between neighboring categories.
- **Parallelization** — Independent model/tool tasks can run concurrently and then be merged, reducing latency or enabling diverse perspectives. **Practice:** fan out three independent analyses and combine their structured outputs.
- **Map-reduce style decomposition** — Map-reduce processes many chunks/items independently and then aggregates them, which is useful for large corpora or batch analysis. **Practice:** summarize several document sections in parallel and reduce them into one final report.
- **Orchestrator-workers** — An orchestrator breaks work into subproblems and delegates them to workers with bounded scopes. **Practice:** implement one orchestrator that creates worker tasks and combines validated outputs.
- **Evaluator-optimizer** — An evaluator scores an output against explicit criteria and an optimizer revises it until a threshold or budget is reached. **Practice:** define a numeric rubric and stop after a maximum number of revisions.
- **Planner-executor** — A planner decides the steps while an executor performs them, improving control on multi-step tasks. **Practice:** persist the plan separately and prevent the executor from silently changing it without justification.
- **Generator-critic** — One component proposes an answer or artifact and another independently searches for defects. **Practice:** give the critic only requirements plus output—not the generator’s reasoning—to reduce shared bias.
- **Reflection/retry** — Reflection uses evidence from a failed attempt to change the next attempt rather than blindly repeating it. **Practice:** record the failure reason in state and ensure the retry modifies strategy or inputs.

## 3.4 Context engineering

- **Context selection rather than context dumping** — More context is not automatically better; select only the information that is relevant, trustworthy, and timely for the current decision. **Practice:** compare a full-document prompt with retrieved minimal context and measure answer quality and token use.
- **Static vs dynamic context** — Static context is durable project/domain guidance; dynamic context is assembled per request from state, retrieval, tools, or user data. **Practice:** explicitly label which information belongs in each category in one application.
- **Retrieved context** — Retrieved context supplies external evidence selected by a search/retrieval process. **Practice:** include document identifiers and relevance metadata and test whether removing low-relevance chunks improves results.
- **Tool results** — Tool results are runtime facts and should be included only when useful for the next model decision. **Practice:** normalize large tool outputs and pass concise structured summaries instead of raw payloads.
- **Conversation history** — History can preserve continuity but grows quickly and may contain stale or conflicting instructions. **Practice:** define which turns to retain, summarize, or drop based on task state.
- **Summarization** — Summarization compresses older context while preserving facts and decisions needed later. **Practice:** create a structured conversation summary with decisions, open issues, and stable facts, then test whether the agent can resume accurately.
- **Context compaction** — Compaction deliberately reduces context size using summaries, references, or persisted state before the window becomes overloaded. **Practice:** trigger compaction at a threshold and compare token usage and task continuity.
- **Context isolation between agents** — Specialist agents should not inherit unrelated histories or secrets simply because another agent saw them. **Practice:** define explicit handoff payloads and verify each agent receives only required fields.
- **Token budgeting** — Allocate the context window across instructions, user input, retrieval, history, tool results, and output rather than treating it as unlimited space. **Practice:** create a budget table and add truncation/summarization rules for overflow.
- **Lost-in-the-middle risks** — Models may underuse information buried inside very long contexts, especially when many similar passages compete for attention. **Practice:** test important evidence at different positions and prefer retrieval/reranking over indiscriminate context stuffing.
- **Relevance vs completeness** — Complete context can be noisy, while highly relevant context may omit dependencies; production systems balance both deliberately. **Practice:** tune top-k/context size on an evaluation set rather than maximizing retrieved text.

### 🧪 Project Assignment — Prompt & Context Benchmark

Create 30 representative support/payment tasks. Implement at least four prompt/context strategies. Compare schema validity, task success, latency, tokens, and cost. Store prompts and evaluation cases in Git.


---


---

# 🤖 Phase 4 — Agent Internals & Reasoning/Workflow Patterns

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 4.1 Build the mental model

- **Goal** — A subagent goal states the measurable outcome it should produce for its delegated task. **Practice:** make the goal output-oriented, such as a findings report with severity and evidence.
- **Model** — The model supplies probabilistic language/reasoning capability but should be selected according to task complexity, latency, cost, and risk. **Practice:** benchmark at least two models for the same agent node.
- **Instructions** — Instructions define role, constraints, policies, and expected behavior for the model. **Practice:** keep stable policy separate from task-specific input and test instruction conflicts.
- **Tools** — Tools let the agent read external state or cause actions outside the model. **Practice:** implement at least one read-only and one side-effecting tool with validation and authorization.
- **State** — State is the explicit data carried between workflow steps, such as decisions, intermediate outputs, and status. **Practice:** define a typed state schema and avoid relying only on free-form conversation history.
- **Memory** — Memory persists useful information beyond the immediate step or session and must have explicit write/read/retention rules. **Practice:** decide which facts deserve persistence and which should remain ephemeral state.
- **Control loop** — The control loop repeatedly decides what to do, executes an action, observes the result, and determines whether to continue. **Practice:** make each transition observable and bounded by iteration/time/cost limits.
- **Stop conditions** — Stop conditions prevent infinite loops and define what constitutes success, failure, escalation, or exhaustion. **Practice:** implement explicit success plus max-iteration/time-budget exits.
- **Guardrails** — Managed guardrails can filter or constrain model inputs/outputs according to policy categories and sensitive information rules. **Practice:** configure a small policy and test both allowed and blocked examples.
- **Evaluation** — Evaluation tells you whether the agent actually completes the task correctly, safely, and economically. **Practice:** define measurable success criteria before optimizing prompts or models.

## 4.2 Core patterns

- **ReAct** — ReAct alternates model reasoning/decision making with tool actions and observations, forming the basic tool-using agent loop. **Practice:** implement it once without a framework so you understand exactly what LangGraph/SDKs automate.
- **Plan-and-Execute** — This pattern creates a plan first and then executes individual steps, making long tasks easier to inspect and recover. **Practice:** persist the plan and mark each step complete/failed with evidence.
- **Routing** — Routing chooses a specialized prompt, model, retriever, or agent based on the request. **Practice:** implement a small intent router and evaluate confusion between neighboring categories.
- **Parallel fan-out/fan-in** — Fan-out sends independent work to multiple workers and fan-in combines their outputs. **Practice:** run several analyses concurrently and define a deterministic aggregation schema.
- **Orchestrator-workers** — An orchestrator breaks work into subproblems and delegates them to workers with bounded scopes. **Practice:** implement one orchestrator that creates worker tasks and combines validated outputs.
- **Evaluator-optimizer** — An evaluator scores an output against explicit criteria and an optimizer revises it until a threshold or budget is reached. **Practice:** define a numeric rubric and stop after a maximum number of revisions.
- **Reflection/self-critique** — The agent reviews its own result against criteria and may revise it, which can improve quality but also increases cost and loop risk. **Practice:** cap revisions and compare against an independent evaluator.
- Tree/search approaches: when worth the cost.
- **Human-in-the-loop** — HITL inserts human review, choice, or approval at points where confidence is low or consequences are high. **Practice:** add an interrupt before an irreversible tool call and support approve/reject/edit outcomes.

## 4.3 Control-loop engineering

- **Maximum iterations** — A hard iteration cap prevents runaway loops even if the model never decides to stop. **Practice:** set a limit and return a diagnosable “budget exhausted” state rather than silently failing.
- **Termination criteria** — Define semantic and deterministic conditions for completion instead of relying on a vague “done” response. **Practice:** express success and failure states explicitly in workflow code.
- **Budget limits** — Agents should have caps on tokens, time, model calls, or monetary cost. **Practice:** track cumulative usage in state and stop or downgrade when the budget is reached.
- **Retry policy** — Retries should specify which failures are retryable, how many attempts are allowed, and whether strategy/input changes. **Practice:** distinguish transient infrastructure retry from reasoning retry.
- **Tool failures** — Tool errors are normal operating states and should be surfaced to the controller with enough information to recover. **Practice:** model failures as structured results and test alternative/fallback paths.
- **Partial success** — Multi-step tasks may complete some work before another step fails, so the system must preserve useful progress without pretending the whole task succeeded. **Practice:** define partial-completion state and user-visible recovery options.
- **State transition validation** — Validate that each workflow transition is legal and that required state fields exist before entering the next node. **Practice:** encode transition invariants and test invalid transitions.
- **Deterministic vs model-selected routing** — Use deterministic routing for known business rules and model-selected routing only where semantic judgment is genuinely required. **Practice:** replace one unnecessary LLM router with code and compare reliability/cost.

## 4.4 Workflow vs agent

- **Fixed DAG** — A fixed directed acyclic graph suits predictable workflows with no loops and known step order. **Practice:** model a simple extract→validate→store pipeline as a DAG.
- **State machine** — A state machine makes allowed states and transitions explicit, which is valuable for auditable business workflows. **Practice:** draw and implement states for a ticket or payment investigation lifecycle.
- **Dynamic graph** — A dynamic graph chooses paths or generates work at runtime based on state or model decisions. **Practice:** allow routing among specialist nodes while constraining possible destinations.
- **Autonomous loop** — An autonomous loop repeatedly chooses actions until a goal or limit is reached and therefore needs strong stop, cost, and tool controls. **Practice:** instrument every loop cycle and force bounded execution.
- **Escalation to humans** — Escalation is a normal terminal or intermediate state when confidence, permissions, or automated recovery are insufficient. **Practice:** define explicit escalation reasons and pass complete evidence to the human reviewer.
- **Choosing minimum necessary autonomy** — Use only as much model discretion as the task needs; extra autonomy increases failure surface and evaluation burden. **Practice:** progressively replace model decisions with deterministic logic where requirements are stable.

### 🧪 Project Assignment — Framework-Free ReAct Research Agent

Using only a model SDK, implement: - calculator, - web/search adapter, - document/file tool, - ReAct-style tool loop, - iteration limit, - structured event log, - retry/error handling, - final critique/evaluation step.

Write an architecture note explaining what LangGraph would later provide for you.

### 🧪 Additional Project Assignment — ReAct Agent with Search + File Output

Build a second framework-free ReAct agent using three concrete tools: calculator, a web-search adapter such as Tavily, and a file-writer tool. Add max-iteration protection, explicit action/observation logging, a final critique/reflection pass, and tests for malformed tool arguments and tool failures.


---


---

# 🟡 Phase 5 — Claude Code Fundamentals & Layered Context

> 🟡 **Path:** `P1` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 5.1 Claude Code operating model

- **Repository-aware coding agent** — A repository-aware agent can inspect files, conventions, tests, history, and dependencies rather than responding to isolated snippets. **Practice:** ask Claude Code to explain the architecture and verify its claims against the repository before editing.
- **CLI and IDE/VS Code usage** — Learn both terminal and IDE workflows because real teams mix interactive coding, review, and automation. **Practice:** complete one task from the CLI and another through the IDE integration while using the same project context.
- **Interactive vs headless/scripted execution** — Interactive sessions are useful for exploration and steering; headless execution suits repeatable CI or automation tasks. **Practice:** run the same bounded analysis once interactively and once non-interactively with deterministic inputs.
- **Planning and review** — Planning reduces unnecessary edits and review checks whether implementation matches the plan and repository constraints. **Practice:** require plan approval for a medium-size change and compare the final diff against the proposed file list.
- **Permission boundaries** — Tool and filesystem permissions define what the coding agent can actually do, independently of what prompts ask it to do. **Practice:** deny at least one sensitive path/command and verify the agent cannot bypass it.
- **Diff review** — The diff is the primary evidence of what the coding agent changed, including accidental unrelated edits. **Practice:** inspect every file, run tests, and reject/revert non-essential changes.
- **Session lifecycle** — Long coding tasks span initialization, context loading, execution, compaction/resume, verification, and closure. **Practice:** maintain a small work note that allows a fresh session to resume without re-reading everything.

## 5.2 Layered context system

Learn the responsibility and scope of: - global/user instructions, - project `CLAUDE.md`, - nested `CLAUDE.md`, - local/personal context where supported, - `.claude/rules/*.md`, - skills, - subagent definitions, - session/work notes. - `CLAUDE.local.md` for gitignored developer-local overrides where supported, such as local ports, seed data, or personal test shortcuts. Keep durable team rules out of this file.

## 5.3 `CLAUDE.md`

Include durable project-wide facts: - architecture, - build/test/run commands, - repository map, - coding conventions, - validation commands, - security boundaries, - architectural invariants, - explicit “do not” constraints.

Avoid: - task-specific prompts, - huge reference manuals, - secrets, - volatile session state, - instructions better enforced by hooks/tests.

## 5.4 Context hygiene

- **Small durable context** — Keep globally loaded instructions short and stable so important rules remain visible and token-efficient. **Practice:** remove task-specific or rarely used material from `CLAUDE.md` and move it to scoped files/skills.
- **Progressive disclosure** — Load detailed instructions only when a task or directory requires them instead of putting everything into the root context. **Practice:** move a specialized procedure into a skill or scoped rule and confirm it appears only when relevant.
- **Localize rules** — Place rules near the code/domain they govern so unrelated work is not burdened by them. **Practice:** create a path-scoped rule for one module and test behavior inside and outside that path.
- **Avoid duplication** — Duplicated instructions drift and can conflict, so each policy or fact should have one authoritative home. **Practice:** search your context files for repeated rules and consolidate them.
- **Single source of truth** — Every durable fact or policy should have one canonical artifact that other instructions reference rather than copy. **Practice:** decide where architecture, commands, security policy, and task notes each belong.
- **Context drift** — Context drift occurs when instructions no longer match the evolving codebase or process. **Practice:** add context-file review to architecture/process changes and delete stale guidance.
- **Instruction conflicts** — Conflicting rules force the model to guess which guidance to follow and make behavior unstable. **Practice:** intentionally create a conflict, observe it, then redesign scope/precedence to remove ambiguity.

### 🧪 Project Assignment — Production Repository Bootstrap

Take an existing Java/Spring microservice repository and create a production-quality Claude Code context hierarchy. Ask Claude Code to implement one API feature and compare: 1. no repository instructions, 2. oversized monolithic instructions, 3. properly layered context.

Record errors, unnecessary changes, tokens, and review effort.


---


---

# 📚 Phase 6 — Retrieval Engineering: Loading, Splitting, Chunking & Basic RAG

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 6.1 Document ingestion

- **PDF/HTML/Markdown/Office/document loaders** — Loaders convert source formats into text plus metadata that your ingestion pipeline can normalize and index. **Practice:** ingest at least three formats and inspect where structure or metadata is lost.
- **Parsing quality** — Poor parsing produces bad chunks before retrieval even begins, so extraction quality is a first-class RAG concern. **Practice:** manually inspect parsed output from tables, headings, lists, and page breaks.
- **Metadata extraction** — Metadata such as source, page, section, date, tenant, and permissions enables filtering and trustworthy citations. **Practice:** define a metadata schema and preserve it through chunking and indexing.
- **Document normalization** — Normalization standardizes whitespace, encoding, headings, boilerplate, and repeated artifacts before chunking. **Practice:** build a small preprocessing step and compare chunks before and after normalization.
- **Tables and structured content** — Tables often lose meaning when flattened to plain text, so they may require specialized parsing or row/section representations. **Practice:** test retrieval over at least one table and preserve column/header context in chunks.
- **OCR only when necessary** — OCR should be reserved for image-based/scanned documents because it introduces recognition errors and extra cost. **Practice:** detect whether text extraction already works and apply OCR only to pages that need it.

## 6.2 Splitting and chunking

- **Fixed-size** — Fixed-size chunking splits by token/character count and is simple but may cut semantic units. **Practice:** use it as a baseline so you can measure whether smarter strategies actually improve retrieval.
- **Recursive** — Recursive splitters try larger semantic separators first and fall back to smaller ones until chunks fit the target size. **Practice:** tune separators and target size on representative documents.
- **Sentence/paragraph** — Sentence or paragraph chunking preserves natural language boundaries and is useful when source structure is clean. **Practice:** compare its retrieval quality with fixed-size chunks on the same questions.
- **Semantic** — Semantic chunking groups text based on meaning changes rather than only length. **Practice:** inspect boundaries produced by a semantic splitter and verify the added embedding cost improves retrieval.
- **Heading/document-structure aware** — Structure-aware chunking keeps headings and sections together so retrieved text retains its document hierarchy. **Practice:** attach heading paths to each chunk and use them in citations or reranking.
- **Parent-child** — Parent-child retrieval indexes small chunks for precision but returns a larger parent section for answer context. **Practice:** retrieve child chunks and expand to parent sections, then measure context precision/recall.
- **Sliding/window approaches** — Sliding windows overlap neighboring text so facts near boundaries remain retrievable. **Practice:** vary overlap and observe duplicate retrieval versus missed boundary context.
- **Chunk overlap** — Overlap repeats context between adjacent chunks; too little loses continuity while too much wastes storage/context and causes duplicates. **Practice:** evaluate at least two overlap values on a small labeled dataset.
- **Chunk size vs retrieval precision** — Smaller chunks improve pinpoint retrieval but may lack context; larger chunks provide context but dilute relevance. **Practice:** benchmark multiple chunk sizes and choose based on retrieval metrics, not intuition.
- **Preserve provenance** — Every chunk should retain enough source metadata to trace an answer back to the exact document/section/page. **Practice:** make citations clickable or inspectable in your RAG response.

## 6.3 Vector storage

- **PostgreSQL + pgvector** — pgvector adds vector search to PostgreSQL, making it attractive when relational data, transactions, and vector retrieval need one operational store. **Practice:** create an embedding table, vector index, metadata filters, and a top-k query.
- **Qdrant** — Qdrant is a purpose-built vector database with strong filtering and vector-search capabilities. **Practice:** implement the same retrieval dataset in Qdrant and compare operational/API differences with pgvector.
- **Pinecone awareness** — Pinecone is a managed vector database; understand its managed scaling and operational model even if you do not choose it for your project. **Practice:** compare pricing, filtering, namespaces/tenancy, and deployment responsibility with self-managed options.
- **Chroma for prototyping** — Chroma is convenient for local prototypes and learning but is not automatically the right production choice. **Practice:** use it for a small experiment, then document what would change for production scale, HA, security, and governance.
- **Index design** — Vector index type and parameters trade recall, memory, build time, and query latency. **Practice:** learn the index your chosen store uses and benchmark a small parameter change instead of accepting defaults blindly.
- **Metadata filtering** — Metadata filters restrict retrieval by tenant, document type, date, permissions, or business context before/with vector similarity. **Practice:** enforce at least one authorization-sensitive filter and test cross-tenant leakage.
- **Multi-tenancy and access control** — RAG must prevent one tenant or user from retrieving documents they are not authorized to see. **Practice:** design tenant-aware indexing/filtering and add negative tests for unauthorized queries.

## 6.4 Basic RAG pipeline

`load → normalize → split → embed → index → retrieve → construct context → generate → cite`

- **top-k** — Top-k controls how many candidate chunks are retrieved; higher values increase recall but also noise and token use. **Practice:** tune k on a labeled evaluation set and inspect both misses and irrelevant additions.
- **similarity thresholds** — A minimum similarity threshold can reject weak matches instead of forcing unrelated context into the prompt. **Practice:** plot/inspect scores for relevant and irrelevant queries and choose a threshold empirically.
- **grounding** — Grounding requires the answer to rely on retrieved or tool-provided evidence rather than unsupported model memory. **Practice:** require evidence references and fail/abstain when supporting context is absent.
- **citations** — Citations let users and evaluators trace generated claims to source evidence. **Practice:** return document/section/page metadata and verify citations actually support each claim.
- **abstention** — A RAG system should sometimes say it lacks sufficient evidence instead of fabricating an answer. **Practice:** include unanswerable questions in evaluation and score correct abstention.
- **retrieval failure modes** — Failures include no hit, wrong hit, stale hit, unauthorized hit, redundant chunks, or evidence split across documents. **Practice:** build examples for each and document the mitigation path.

## 6.5 LangChain/LlamaIndex ingestion layer

- Learn abstractions after implementing the pipeline once yourself.
- **Loaders** — Framework loaders standardize ingestion from common source types but may hide parser limitations. **Practice:** inspect the raw document objects and metadata rather than assuming the loader preserved everything.
- **Splitters** — Framework splitters implement chunking strategies and should be tuned against your corpus rather than used with tutorial defaults. **Practice:** compare at least two splitters on the same retrieval questions.
- **Embeddings** — Framework embedding abstractions let you swap providers, but dimensions, normalization, and behavior still differ by model. **Practice:** verify stored vector dimensions and re-index deliberately when changing models.
- **Vector stores** — Vector-store integrations provide indexing and similarity search but differ in metadata filtering, tenancy, index management, and operations. **Practice:** implement one production-oriented store end to end and understand its query/index API.
- **Retrievers** — A retriever is the application interface that turns a query into ranked context and may compose filters, query transforms, and rerankers. **Practice:** expose a retriever independently and evaluate it before connecting generation.

### 🧪 Project Assignment — Regulation RAG v1

Ingest a corpus of payment/regulatory documents. Implement two chunking strategies and compare retrieval quality. Store vectors in pgvector, return source citations, enforce metadata filtering, and build a small retrieval evaluation dataset.


---


---

# 🕸️ Phase 7 — Advanced, Graph & Agentic RAG

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 7.1 Advanced retrieval

- **Dense + sparse/BM25** — Dense retrieval captures semantics while sparse/BM25 captures exact lexical signals; combining them improves robustness. **Practice:** find queries where each wins and keep both candidate lists for hybrid experiments.
- **Hybrid search** — Hybrid search merges semantic and lexical retrieval to balance meaning and exact terminology. **Practice:** implement a hybrid candidate stage and compare recall with dense-only retrieval.
- **Reciprocal Rank Fusion** — RRF combines rankings from different retrievers without requiring directly comparable raw scores. **Practice:** fuse BM25 and vector result lists and measure ranking changes on labeled queries.
- **Cross-encoder re-ranking** — A cross-encoder scores query-document pairs more accurately than embedding similarity but is more expensive, so it is commonly used on a small candidate set. **Practice:** retrieve broadly, rerank the top candidates, and measure quality/latency trade-offs.
- **Query expansion** — Query expansion adds related terms or formulations to improve recall when the original query is too narrow. **Practice:** generate controlled expansions and verify they do not drift away from user intent.
- **Multi-query** — Multi-query retrieval generates several alternate queries and merges their results to improve coverage. **Practice:** compare unique relevant hits versus extra noise/cost from three to five variants.
- **HyDE** — HyDE generates a hypothetical answer/document and embeds that to retrieve semantically similar real documents. **Practice:** use it on difficult queries and compare retrieval against direct query embeddings.
- **Query decomposition** — Complex questions can be split into subqueries whose evidence is retrieved separately and combined. **Practice:** decompose one multi-hop question and verify each sub-answer has evidence before synthesis.
- **Parent-document retrieval** — Retrieve precise child chunks but return their richer parent sections to the generator. **Practice:** tune child/parent sizes and evaluate whether added context improves answer completeness.
- **Contextual retrieval** — Contextual retrieval enriches chunks with document/section context so isolated excerpts remain meaningful during search. **Practice:** add concise context labels before embedding and measure retrieval improvement.
- **Metadata/security filtering** — Advanced retrieval must apply authorization and business filters as part of candidate selection, not after sensitive text is retrieved. **Practice:** enforce filters at query time and add security regression tests.

## 7.2 Graph RAG

- **Entity extraction** — Entity extraction identifies domain objects such as customers, accounts, regulations, products, or organizations from source text. **Practice:** define an entity schema and validate extracted entities before graph insertion.
- **Relationship extraction** — Relationship extraction turns text into typed links between entities, enabling multi-hop graph queries. **Practice:** define allowed relationship types and inspect false links on a sample corpus.
- **Knowledge graphs** — A knowledge graph stores entities and explicit relationships, making relational reasoning and traversal auditable. **Practice:** model a small domain ontology and load a few documents into it.
- **Neo4j** — Neo4j is a graph database commonly used for property-graph storage and Cypher traversal. **Practice:** create a small graph, write Cypher queries, and expose one graph retrieval tool to your agent.
- **Graph traversal** — Traversal follows explicit relationships to gather evidence that vector similarity alone may miss. **Practice:** implement a bounded multi-hop query and return the traversed path as provenance.
- **Multi-hop retrieval** — Multi-hop questions require combining evidence across multiple entities/documents or relations. **Practice:** create questions that cannot be answered from a single chunk and evaluate graph/decomposed retrieval.
- **Vector + graph hybrid** — Use vector search to find entry entities/documents and graph traversal to expand structured relationships. **Practice:** implement this two-stage retrieval pattern and compare it with vector-only RAG.
- **Corpus/global summarization approaches** — Learn what **Corpus/global summarization approaches** means in Graph RAG, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.

## 7.3 Agentic RAG

- **Agent decides whether retrieval is necessary** — An Agentic RAG controller can skip retrieval for trivial tasks and invoke it only when external evidence is needed. **Practice:** create queries that should and should not retrieve, then measure routing accuracy.
- **Router selects corpus/tool** — The router chooses among knowledge bases, web search, databases, or domain tools based on the request. **Practice:** define explicit routing criteria and test ambiguous queries.
- **Retrieval grader** — A retrieval grader judges whether returned evidence is relevant/sufficient before generation. **Practice:** grade retrieved chunks against the question and trigger rewrite/fallback when quality is low.
- **Query rewrite** — The agent reformulates a poor query using failure evidence to improve the next retrieval attempt. **Practice:** log the original and rewritten queries and verify each retry changes meaning purposefully.
- **Retry** — Retrieval retry should be bounded and strategy-aware rather than repeatedly issuing the same query. **Practice:** retry with a changed query, retriever, or filter and cap attempts.
- **Web/tool fallback** — When the primary corpus cannot answer, the system may use an approved alternate source such as web search or an enterprise API. **Practice:** make fallback explicit, provenance-tagged, and security-controlled.
- **Corrective RAG** — Corrective RAG evaluates retrieved evidence and performs corrective actions such as query rewriting or external search when evidence is weak. **Practice:** implement a grade→correct→retrieve path in LangGraph.
- **Self-RAG concepts** — Self-RAG adds model decisions around when to retrieve and how to critique evidence/answers. **Practice:** understand the control ideas and implement a simplified retrieval/critique decision rather than copying research code blindly.
- **Multi-index routing** — Large systems may maintain separate indexes by domain, tenant, language, or data type, requiring a reliable routing layer. **Practice:** build two small indexes and evaluate routing plus fallback between them.

## 7.4 RAG evaluation

- **Faithfulness** — Faithfulness measures whether generated claims are supported by provided context. **Practice:** include unsupported-answer cases and use human or automated evaluation to detect invented claims.
- **Answer relevancy** — Answer relevancy measures how directly the response addresses the user’s question rather than merely repeating context. **Practice:** evaluate concise and verbose outputs against the same question set.
- **Context precision** — Context precision asks how much of the retrieved evidence is actually relevant, exposing noisy retrieval. **Practice:** label relevant chunks for a small set and reduce unnecessary retrieved context.
- **Context recall** — Context recall asks whether retrieval found all evidence needed to answer correctly. **Practice:** create questions with known supporting passages and count missed evidence.
- **Retrieval hit rate/MRR/nDCG awareness** — These information-retrieval metrics measure whether relevant documents are found and how highly they rank. **Practice:** compute at least hit rate and MRR on a small labeled query set before tuning generation.
- **RAGAS and alternative eval tooling** — RAG evaluation frameworks automate common metrics but their scores still need calibration against human judgments. **Practice:** run a small RAGAS evaluation and manually inspect disagreements.

### 🧪 Project Assignment — Regulation RAG v2

Upgrade Phase 6 to hybrid retrieval + re-ranking + agentic retrieval grading. Add a small Neo4j graph for regulation/article/obligation relationships. Produce before/after evaluation results and a failure-analysis report.

### 🧪 Additional Project Assignment — Regulatory Knowledge Assistant

Ingest PSD2/PCI-DSS-style payment-regulation documents using LangChain plus pgvector, add hybrid dense+BM25 retrieval, re-ranking, an agentic grade → rewrite → retry/fallback loop, and a small Neo4j entity graph for multi-hop questions. Evaluate retrieval and generation separately with RAGAS-style metrics.


---


---

# 🧠 Phase 8 — State, Memory & Long-Running Agent Context

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 8.1 Do not confuse context with memory

- **Prompt/context window** — The context window is transient working input, not durable memory. **Practice:** identify what disappears after a call/session and move only necessary persistent information into state or memory.
- **Runtime state** — Runtime state stores explicit variables needed during an executing workflow, such as current step, tool results, or approvals. **Practice:** model state as typed fields rather than relying on conversational text.
- **Checkpoint state** — A checkpoint persists workflow state at safe boundaries so execution can resume after interruption or failure. **Practice:** stop a workflow mid-run, restart the process, and verify it resumes from the last checkpoint.
- **Conversation memory** — Conversation memory preserves interaction continuity, but it should be summarized/filtered to avoid unlimited history growth. **Practice:** define retention and compaction rules for a multi-turn assistant.
- **Long-term semantic memory** — Semantic memory stores facts that can later be retrieved by meaning rather than exact key. **Practice:** explicitly write a small set of approved facts and retrieve them in later sessions.
- **Episodic memory** — Episodic memory stores prior events or experiences, such as what happened in a past task, not just timeless facts. **Practice:** save a task outcome and use it to influence a later similar task.
- **User/profile memory** — Profile memory stores durable user preferences or attributes and therefore needs consent, correction, and deletion semantics. **Practice:** implement explicit opt-in write/update/delete paths instead of silently storing everything.
- **External source of truth** — Authoritative business state should remain in systems of record rather than being duplicated as unreliable model memory. **Practice:** store only references/summaries and re-read critical current facts from the source system when needed.

## 8.2 Short-term memory

- **Thread/session state** — Session state keeps short-lived information for one conversation or task thread. **Practice:** give each thread an identifier and ensure state does not leak between sessions.
- **Message history** — Message history preserves conversational turns but can become noisy and expensive. **Practice:** retain only relevant messages and test behavior after pruning old chatter.
- **Summarization** — Summarization compresses older context while preserving facts and decisions needed later. **Practice:** create a structured conversation summary with decisions, open issues, and stable facts, then test whether the agent can resume accurately.
- **Sliding history** — A sliding window keeps only the most recent turns within a fixed budget. **Practice:** implement a token- or turn-based window and verify older required facts are summarized before eviction.
- **Token-aware compaction** — Token-aware compaction summarizes or externalizes context based on actual token usage rather than a fixed number of turns. **Practice:** trigger compaction at a threshold and measure continuity after compaction.

## 8.3 Long-term memory

- **Explicit writes** — Long-term memory should be written intentionally based on rules, not as an automatic dump of every message. **Practice:** create a memory-write decision with allowed memory types and user/policy controls.
- **Semantic retrieval** — Memory retrieval should return only facts relevant to the current task, ranked and filtered by scope. **Practice:** retrieve memories with embeddings plus metadata and verify irrelevant memories stay out of context.
- **Facts/preferences** — Distinguish stable factual memory from user preferences because they have different update and conflict semantics. **Practice:** define schemas and example update rules for both.
- **Episodic records** — Episodic records capture a time-stamped event, outcome, and context from prior work. **Practice:** save structured episodes and retrieve them only for sufficiently similar future tasks.
- **Memory consolidation** — Consolidation merges repetitive or fragmented memories into a smaller, coherent representation over time. **Practice:** deduplicate several similar facts and preserve provenance/date of the merged result.
- **TTL/retention** — Memories should expire or be retained according to usefulness, privacy, and policy rather than forever by default. **Practice:** assign TTL/retention classes and test automatic expiration.
- **Conflict resolution** — New information may contradict stored memory, so the system needs rules for source authority, recency, and uncertainty. **Practice:** create conflicting facts and implement an update/flagging strategy.
- **Forget/update semantics** — Users and systems must be able to correct or delete persisted memories explicitly. **Practice:** build update/delete operations and verify removed memory no longer appears in retrieval.

## 8.4 Durable execution

- **Checkpointing** — Checkpointing persists workflow state after meaningful steps to support recovery, inspection, and HITL. **Practice:** checkpoint before and after a side effect and inspect stored state.
- **Resume after crash** — Durable agents should restart without repeating completed work or losing approvals. **Practice:** kill the process mid-workflow and verify correct recovery.
- **Exactly-once illusion vs idempotency** — Distributed systems rarely guarantee true exactly-once effects, so idempotency is the practical defense against duplicate execution. **Practice:** replay a checkpointed side-effecting node and prove the external action occurs once.
- **Side-effect tracking** — Record side effects and their identifiers so retries/recovery know what has already happened. **Practice:** persist tool action IDs/status alongside workflow checkpoints.
- **Replay** — Replay re-runs workflow logic from recorded state/events for debugging or recovery and must avoid accidental duplicate external effects. **Practice:** implement a dry-run or idempotent replay path.
- **State versioning** — Persisted state schemas evolve, so old checkpoints may need migration or compatibility handling. **Practice:** change a state schema and write a migration/version check for old data.

## 8.5 Memory security

- **Tenant isolation** — Memory and state must be partitioned so one tenant can never access another tenant’s data. **Practice:** include tenant IDs in storage and negative-test cross-tenant reads.
- **PII** — Personally identifiable information requires minimization, appropriate protection, and controlled model/tool exposure. **Practice:** classify which fields are sensitive and mask or avoid persisting them where possible.
- **Consent** — Some memories or personalization data should only be stored or used with clear user consent and policy support. **Practice:** model consent state and block memory writes/reads when consent is absent.
- **Retention/deletion** — Retention policies determine how long data is kept and deletion must remove it from all relevant memory/index layers. **Practice:** implement and test a deletion request end to end.
- **Poisoning** — Memory poisoning occurs when untrusted or malicious content is persisted and later treated as trusted context. **Practice:** validate memory sources and prevent retrieved instructions from overriding higher-priority policy.
- **Incorrect memories** — Stored memories can become false, stale, or misattributed and need confidence/source/update mechanisms. **Practice:** attach provenance and timestamps and provide a correction path.
- **Auditability** — You should be able to explain when a memory was written, changed, read, or deleted and by whom/what. **Practice:** log memory lifecycle events with identifiers and policy decisions.

### 🧪 Project Assignment — Durable Customer-Service Agent

Create a multi-session assistant with: - short-term thread state, - long-term explicit memory, - Postgres persistence, - summarization, - crash/restart recovery, - memory update/delete, - tenant isolation tests.


---


---

# 🔀 Phase 9 — LangChain & LangGraph Orchestration

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 9.1 LangChain

**Depth: Working-to-Deep** - Model abstraction. - Messages. - Prompt templates. - Tools. - Retrievers. - Structured output. - Middleware concepts. - Runnables/composition as applicable. - Use selectively; do not hide fundamentals behind framework abstractions.

## 9.2 LangGraph

**Depth: Deep** - Typed state. - Nodes. - Edges. - Conditional edges. - Cycles. - Command/routing concepts. - Streaming. - Checkpointers. - Durable execution. - Interrupts. - Human approval. - State inspection/replay. - Long-running workflows.

## 9.3 Design principles

- **Graph only where state/control flow merits it** — Learn what **Graph only where state/control flow merits it** means in Design principles, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Deterministic edges where business policy is deterministic** — Learn what **Deterministic edges where business policy is deterministic** means in Design principles, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Model routing only where semantic judgment is necessary** — Learn what **Model routing only where semantic judgment is necessary** means in Design principles, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Explicit side-effect boundaries** — Learn what **Explicit side-effect boundaries** means in Design principles, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Idempotent nodes** — Learn what **Idempotent nodes** means in Design principles, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Failure/retry semantics** — Learn what **Failure/retry semantics** means in Design principles, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.

### 🧪 Project Assignment — LangGraph Migration

Rebuild the framework-free Phase 4 agent using LangGraph. Add checkpointing, HITL, conditional routing and durable restart. Compare code complexity, control, observability, and failure recovery against the framework-free version.


---


---

# 🧰 Phase 10 — Claude Code Skills, Rules, Commands & Subagents

> 🟡 **Path:** `P1` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 10.1 Rules

- `.claude/rules/*.md` — Learn what **.claude/rules/.md** means in Rules, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Domain/directory-scoped conventions** — Conventions should apply only to the module or file types that need them. **Practice:** encode a module-specific convention and test an unrelated module remains unaffected.
- **Architecture rules** — Architecture rules express boundaries such as allowed dependencies, layering, or communication patterns. **Practice:** document them for the agent and enforce critical ones with architecture tests where possible.
- **Testing rules** — Testing rules tell the coding agent which test levels, naming, fixtures, and commands are expected for changed code. **Practice:** require tests for a small feature and verify the agent runs the prescribed command.
- **Security rules** — Security rules capture secure coding constraints such as secrets, auth checks, data handling, and forbidden APIs. **Practice:** pair written rules with scanners/hooks for rules that must never be violated.
- Avoid repeating root project memory.

## 10.2 Skills

- `.claude/skills/<skill>/SKILL.md` — A skill packages reusable domain procedure/instructions so the agent can invoke expertise on demand rather than re-derive it every session. **Practice:** create one skill with a narrow trigger, procedure, and supporting script/reference.
- **Frontmatter/metadata** — Skill metadata describes identity, purpose, and triggering information so tools/agents can discover it correctly. **Practice:** keep metadata precise and test whether the skill is selected for intended requests but not unrelated ones.
- **Trigger-oriented descriptions** — A good skill description explains when the capability should be used, not merely what files it contains. **Practice:** write positive and negative trigger examples and refine the wording.
- **Progressive disclosure** — Load detailed instructions only when a task or directory requires them instead of putting everything into the root context. **Practice:** move a specialized procedure into a skill or scoped rule and confirm it appears only when relevant.
- **Optional scripts/templates/reference material** — Put deterministic calculations, templates, or long reference content beside the skill rather than bloating the instruction body. **Practice:** move one repeated manual procedure into a script the skill invokes.
- **Skill vs rule vs subagent vs MCP** — Use a rule for durable constraints, a skill for reusable know-how, a subagent for an isolated role, and MCP for external capabilities/data. **Practice:** classify ten pieces of project context into the correct mechanism.
- **Reusable domain expertise** — Skills should capture organization/domain knowledge that can be applied consistently across tasks. **Practice:** package a repeatable review such as payment idempotency or Kafka capacity analysis.

Example skill domains: - Kafka capacity review. - Spring Boot API review. - payment idempotency review. - threat modeling. - migration readiness. - ADR generation.

## 10.3 Commands

- **Reusable explicit workflows** — Commands provide user-invoked repeatable workflows for tasks that should start consistently. **Practice:** create a command for “implement + test + review” with well-defined inputs.
- **Parameterized task invocation** — Commands become more reusable when task-specific values are parameters rather than hard-coded instructions. **Practice:** add parameters for feature name/path or target module and validate missing inputs.
- **When a command should invoke a skill or subagent** — A command orchestrates the workflow, while skills/subagents supply expertise or isolated execution roles. **Practice:** design one command that delegates review to a specialist rather than duplicating its instructions.
- Keep commands task-oriented rather than storing project knowledge.

## 10.4 Subagents

- `.claude/agents/*.md` — Learn what **.claude/agents/.md** means in Subagents, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Role** — The role defines the specialist perspective and responsibility of the subagent. **Practice:** use a concrete role such as “API security reviewer” rather than a generic “helper.”
- **Goal** — A subagent goal states the measurable outcome it should produce for its delegated task. **Practice:** make the goal output-oriented, such as a findings report with severity and evidence.
- **Scope** — Scope constrains which files, concerns, or decisions belong to the subagent. **Practice:** explicitly state what it must not modify or decide.
- **Allowed tools** — Tool restrictions enforce least privilege for each role. **Practice:** give a reviewer read/search tools but no write/deploy capability and verify enforcement.
- **Inputs/outputs** — Clear handoff contracts prevent agents from relying on hidden conversational context. **Practice:** define a structured input packet and expected output schema for one subagent.
- **Model choice** — Different roles may need different model capability, latency, or cost profiles. **Practice:** benchmark a smaller model for deterministic review/extraction and a stronger model for complex planning.
- **Context isolation** — Each agent should receive only the context needed for its role, which reduces token waste, accidental coupling, and reviewer bias. **Practice:** compare a reviewer given the entire implementation conversation with one given only requirements, diff, and test evidence.
- **Reviewer/tester/security/architecture roles** — Specialized agents are most valuable when their responsibilities and evidence differ meaningfully. **Practice:** run at least two independent roles and compare the defects each detects.
- **Preventing role overlap** — Overlapping roles duplicate work, increase cost, and create conflicting edits. **Practice:** create a responsibility matrix showing who can read, write, decide, and approve each artifact.

## 10.5 Work/session notes

- **Plans and session continuity** — Work notes preserve the current objective, plan, and state across context compaction or new sessions. **Practice:** write a concise resumption section that a fresh agent can follow.
- **Decisions made** — Record decisions and rationale so future sessions do not repeatedly revisit settled choices. **Practice:** log only decisions with lasting effect and link to evidence/ADR where appropriate.
- **Remaining work** — A clear remaining-work list prevents resumed sessions from guessing what is complete. **Practice:** keep actionable unchecked items with dependencies and acceptance criteria.
- **Verification status** — Track what has actually been tested/reviewed versus what merely appears implemented. **Practice:** record exact commands/checks and results before marking work complete.
- Do not convert transient notes into permanent global instructions.

### 🧪 Project Assignment — Claude Code Engineering Toolkit

For the same Java service, build: - architecture rules, - API-review skill, - Kafka-review skill, - implementation command, - test subagent, - code-review subagent, - security subagent.

Run one feature through the toolkit and measure human review effort and defects found.


---


---

# 👥 Phase 11 — Multi-Agent Architecture & Vendor Agent SDKs

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 11.1 Multi-agent topologies

- **Supervisor** — A supervisor agent delegates tasks to specialists and decides what should happen next. **Practice:** define bounded worker capabilities and keep business state in explicit workflow state, not only supervisor conversation.
- **Hierarchical** — Hierarchical systems use multiple supervisory levels for large problem decompositions, but add coordination cost. **Practice:** sketch when a second supervisory layer is justified versus unnecessary complexity.
- **Router + specialists** — A router chooses the most appropriate specialist based on the request without requiring a general supervisor to perform all reasoning. **Practice:** evaluate routing accuracy on ambiguous and out-of-scope requests.
- **Handoffs** — A handoff transfers responsibility and a structured context packet from one agent to another. **Practice:** define what state is transferred and what remains private to the sending agent.
- **Network/swarm concepts** — Peer-agent network patterns allow decentralized collaboration but are harder to bound, debug, and evaluate. **Practice:** understand the pattern and use it only for a problem where dynamic peer selection has clear value.
- **Blackboard/shared-state patterns** — Agents coordinate through a shared structured workspace rather than passing full conversations to one another. **Practice:** implement a shared task/result store with ownership and update rules.
- **Parallel specialists** — Independent specialists can analyze different dimensions concurrently, such as security, performance, and correctness. **Practice:** fan out the same artifact to several read-only reviewers and aggregate findings by severity.

## 11.2 Context boundaries

- **Give each agent only necessary context** — Learn what **Give each agent only necessary context** means in Context boundaries, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Shared vs private state** — Learn what **Shared vs private state** means in Context boundaries, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Handoff contracts** — Learn what **Handoff contracts** means in Context boundaries, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Structured inter-agent messages** — Learn what **Structured inter-agent messages** means in Context boundaries, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- Avoid “multi-agent because it looks sophisticated.”

## 11.3 Vendor SDKs

Learn at least: - **OpenAI Agents SDK — Deep** - **Claude Agent SDK — Deep** - **Google ADK — Working** - CrewAI — Aware/Working - Pydantic AI — Aware/Working

## 11.4 Framework selection

Compare: - explicit graph orchestration, - handoff-centric SDKs, - role-based agent teams, - model-native tool loops, - deterministic workflow engines.

### 🧪 Project Assignment — Multi-Agent Fraud Triage

Build transaction-analysis, customer-history, regulation, and report agents. Require human approval before irreversible account actions. Implement one version in LangGraph and a smaller version in one vendor SDK. Write a trade-off ADR.

### 🧪 Additional Project Assignment — Two-Agent Vendor-SDK Rebuild

Rebuild a deliberately smaller version of the fraud-triage workflow with one vendor-native agent SDK. Keep only two agents and compare handoff semantics, tracing, guardrails, state management, and developer ergonomics against the LangGraph version.


---


---

# 🔗 Phase 12 — MCP: Build, Consume, Secure & Govern

> 🟣 **Path:** `P1+P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 12.1 MCP fundamentals

- **Host** — Learn what **Host** means in MCP fundamentals, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Client** — Learn what **Client** means in MCP fundamentals, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Server** — Learn what **Server** means in MCP fundamentals, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Tools** — Tools let the agent read external state or cause actions outside the model. **Practice:** implement at least one read-only and one side-effecting tool with validation and authorization.
- **Resources** — Learn what **Resources** means in MCP fundamentals, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Prompts** — Learn what **Prompts** means in MCP fundamentals, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Capability negotiation** — Learn what **Capability negotiation** means in MCP fundamentals, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Local vs remote servers** — Learn what **Local vs remote servers** means in MCP fundamentals, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **stdio** — Learn what **stdio** means in MCP fundamentals, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Streamable HTTP** — Learn what **Streamable HTTP** means in MCP fundamentals, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Sessions** — Learn what **Sessions** means in MCP fundamentals, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.

## 12.2 Build MCP servers

- **Python official MCP SDK/FastMCP** — Learn what **Python official MCP SDK/FastMCP** means in Build MCP servers, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **TypeScript SDK awareness** — Learn what **TypeScript SDK awareness** means in Build MCP servers, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Java/Spring AI MCP** — Learn what **Java/Spring AI MCP** means in Build MCP servers, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Wrap REST APIs** — Learn what **Wrap REST APIs** means in Build MCP servers, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Wrap RAG** — Learn what **Wrap RAG** means in Build MCP servers, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Wrap databases safely** — Learn what **Wrap databases safely** means in Build MCP servers, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Long-running operations** — Learn what **Long-running operations** means in Build MCP servers, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Errors and structured results** — Learn what **Errors and structured results** means in Build MCP servers, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.

## 12.3 🔌 Consume MCP

From: - Claude Code. - Claude Agent SDK. - OpenAI agent tooling where supported. - LangGraph adapters. - custom clients.

## 12.4 🔐 MCP security

- **Authentication/OAuth** — Learn what **Authentication/OAuth** means in 🔐 MCP security, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Least privilege** — Learn what **Least privilege** means in 🔐 MCP security, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Tool allowlists** — Learn what **Tool allowlists** means in 🔐 MCP security, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Tool poisoning** — Learn what **Tool poisoning** means in 🔐 MCP security, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Prompt injection through tool metadata/results** — Learn what **Prompt injection through tool metadata/results** means in 🔐 MCP security, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Confused deputy** — Learn what **Confused deputy** means in 🔐 MCP security, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Secret management** — Learn what **Secret management** means in 🔐 MCP security, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Egress controls** — Learn what **Egress controls** means in 🔐 MCP security, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Audit logs** — Learn what **Audit logs** means in 🔐 MCP security, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Approval for side effects** — Learn what **Approval for side effects** means in 🔐 MCP security, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.

## 12.5 MCP architecture

- One MCP server per domain capability rather than blindly per microservice.
- Gateway/aggregation when governance, discovery, auth or policy warrants it.
- Avoid exposing internal service topology directly to agents.
- **Stable capability-oriented contracts** — Learn what **Stable capability-oriented contracts** means in MCP architecture, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.

## 12.6 MCP in both paths

**P1:** expands the coding agent’s external tool surface.  
**P2:** provides a protocol boundary between application agents and enterprise capabilities.

## 12.7 A2A and protocol boundaries

- Understand the conceptual split: **MCP = agent/client ↔ tools/resources**, while **A2A = agent ↔ agent** interoperability.
- **Agent Cards/capability discovery** — A2A Agent Cards advertise an agent’s identity, endpoint, skills/capabilities, and interaction contract so other agents can discover it. **Practice:** create an Agent Card for one specialist and validate that another client can select it based on capability.
- **Tasks, messages, status and long-running task lifecycle concepts** — A2A represents work as stateful tasks/messages that can continue asynchronously across systems. **Practice:** model submitted, working, input-required, completed, and failed states for one long-running agent interaction.
- Use A2A when independently owned agents/services need an explicit cross-team or cross-vendor protocol boundary; do not use it merely to connect internal functions in one process.

### 🧪 Project Assignment — Enterprise MCP Capability Layer

Build: 1. Python MCP server exposing Regulation RAG. 2. Spring Boot MCP server exposing a mock payments capability. 3. OAuth/authorization policy. 4. Claude Code client configuration. 5. LangGraph/application-agent consumption. 6. Threat model and audit logging.

### 🧪 Additional Project Assignment — Enterprise MCP Gateway + A2A Bonus

Build two MCP servers: a Python/FastMCP server exposing your regulatory RAG capability and a Spring AI MCP server wrapping a mock banking API over authenticated remote transport. Connect both to the application-agent workflow. As an optional extension, expose the fraud-triage supervisor as an A2A-capable agent with an Agent Card and long-running task status.


---


---

# 🏗️ Phase 13 — Agentic Engineering: Plan → Execute → Verify

> 🟡 **Path:** `P1` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 13.1 Planning

- **Requirement interpretation** — Before editing code, translate the request into explicit behavior, constraints, dependencies, and unknowns. **Practice:** restate the requirement and list assumptions that need validation.
- **Repository reconnaissance** — Inspect architecture, neighboring implementations, tests, build files, and conventions before deciding how to change the code. **Practice:** require the agent to cite relevant files before proposing a plan.
- **Impact analysis** — Identify which modules, APIs, schemas, tests, consumers, and operational concerns a change may affect. **Practice:** create a change-impact checklist before implementation.
- **Explicit plan** — A written plan makes intended changes reviewable before code is modified. **Practice:** include steps, files, risks, test strategy, and rollback concerns for a medium-size feature.
- **Files/components expected to change** — Naming expected change locations helps detect scope creep and unrelated edits. **Practice:** compare the final diff against the planned file list and investigate surprises.
- **Test strategy** — Define how correctness will be proven at unit, integration, contract, and acceptance levels before implementation. **Practice:** write tests/commands into the plan and execute them during verification.
- **Risk assessment** — Assess security, data, backward compatibility, performance, migration, and operational risks before granting autonomy. **Practice:** classify risks by likelihood/impact and add approval or checks for high-risk items.
- **Human plan approval for non-trivial work** — Learn what **Human plan approval for non-trivial work** means in Planning, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.

## 13.2 Execution

- **Delegate bounded work** — Delegation works best when each agent receives a self-contained task with explicit inputs, permissions, and expected output. **Practice:** split one feature into independently verifiable units instead of delegating “build the whole thing.”
- **Independent implementation/test/documentation tasks** — Parallelize only tasks that do not write the same artifacts or depend on unfinished outputs. **Practice:** identify dependencies and let independent test/documentation analysis run concurrently.
- **Context isolation** — Each agent should receive only the context needed for its role, which reduces token waste, accidental coupling, and reviewer bias. **Practice:** compare a reviewer given the entire implementation conversation with one given only requirements, diff, and test evidence.
- **Parallelization only when dependencies permit it** — Concurrency saves time only when tasks are truly independent; otherwise it creates merge conflicts and inconsistent assumptions. **Practice:** draw a dependency graph before parallel delegation.
- **Preserve architectural invariants** — Agent-generated changes must continue to respect boundaries such as layering, ownership, APIs, and data flow. **Practice:** encode critical invariants in tests/static rules and run them automatically.

## 13.3 Verification

- **Tests** — Tests provide executable evidence that behavior still meets requirements. **Practice:** run relevant tests yourself and inspect failure/output rather than trusting the agent’s summary.
- **Static analysis** — Static analysis detects type, quality, dependency, or vulnerability issues without executing the program. **Practice:** integrate your project’s linters/analyzers into the verification gate.
- **security checks** — Security verification should independently check secrets, dependencies, authz, input validation, and common vulnerability patterns. **Practice:** run automated scans plus a focused security-review agent for sensitive changes.
- **reviewer subagent** — A reviewer subagent should independently inspect requirements, diff, tests, and risks without editing the implementation. **Practice:** make it read-only and require evidence-linked findings.
- **architectural review** — Architectural review checks whether local code correctness still fits system-wide boundaries and non-functional requirements. **Practice:** review dependencies, data ownership, APIs, and operational impact for one change.
- **acceptance criteria** — Acceptance criteria convert the requirement into verifiable outcomes. **Practice:** map each criterion to a test, manual check, or observable evidence item.
- **diff inspection** — Inspecting the diff catches unrelated edits, removed safeguards, generated noise, and suspicious dependency/config changes. **Practice:** reject any change that cannot be tied to the approved plan.
- **evidence, not “looks good.”** — Learn what **evidence, not “looks good.”** means in Verification, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.

## 13.4 Specialized agents

- **Planner** — The planner analyzes requirements, repository context, risks, and sequencing without prematurely implementing. **Practice:** keep the planner read-only for significant work and require a structured plan artifact.
- **Implementer** — The implementer executes the approved plan within explicit scope and permissions. **Practice:** limit it to intended modules and require it to report deviations from plan.
- **Tester** — The tester independently derives test cases from requirements and changed behavior, reducing confirmation bias. **Practice:** have it create edge/failure tests the implementer did not propose.
- **Reviewer** — The reviewer evaluates code quality, correctness, maintainability, and scope using evidence rather than rewriting everything. **Practice:** require severity, file/line evidence, and actionable recommendations.
- **Security reviewer** — The security reviewer focuses on trust boundaries, inputs, secrets, authn/authz, data exposure, and unsafe dependencies/tools. **Practice:** use a dedicated checklist based on the change type.
- **Performance reviewer** — The performance reviewer looks for latency, allocation, concurrency, query, and scaling regressions. **Practice:** ask for measurable bottleneck hypotheses and relevant benchmarks rather than generic advice.
- **Migration reviewer** — The migration reviewer checks schema/config/API compatibility, rollout order, rollback, and data migration safety. **Practice:** use it whenever changes require versioned rollout or persistent-state transformation.

## 13.5 Failure patterns

- **Agents editing the same files** — Concurrent writers to the same files create merge conflicts and inconsistent assumptions. **Practice:** partition ownership or serialize dependent edits.
- **Unclear ownership** — If multiple agents can decide the same thing, responsibilities blur and findings/actions conflict. **Practice:** define a RACI-like responsibility table for each workflow stage.
- **reviewers sharing implementation bias/context** — Learn what **reviewers sharing implementation bias/context** means in Failure patterns, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **excessive agent count** — More agents increase coordination, token use, latency, and failure paths and should not be treated as inherently better. **Practice:** justify each agent by a distinct capability or trust boundary.
- **circular delegation** — Agents delegating back and forth without a terminal owner can create unbounded loops. **Practice:** define allowed delegation directions and maximum depth.
- **no deterministic verification** — Model review alone can agree with model-generated mistakes, so critical correctness needs executable checks. **Practice:** require tests, schema validation, scanners, or policy engines before completion.
- **autonomous merge/deployment without policy controls** — Code merge or deployment changes shared/production state and should be guarded by CI, approvals, and least privilege. **Practice:** keep production actions behind explicit policy gates even if the agent can open a PR.

### 🧪 Project Assignment — Multi-Agent Feature Delivery

Implement a realistic payment-refund feature using separate planning, implementation, test, security and review roles. Produce a final verification packet containing plan, diffs, test evidence, security findings and unresolved risks.


---


---

# 🛡️ Phase 14 — Harness Engineering: Hooks, Permissions, Sandboxes & Guardrails

> 🟡 **Path:** `P1` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 14.1 🪝 Hooks

- **Pre-tool checks** — Pre-tool hooks validate or block an action before it executes, making them suitable for security and scope enforcement. **Practice:** block writes to a protected path and verify the tool call fails before modification.
- **Post-tool checks** — Post-tool hooks inspect outcomes after an action, such as formatting changed files or validating generated artifacts. **Practice:** run targeted tests/formatting after a write and surface failures back to the agent.
- **session lifecycle hooks where available** — Learn what **session lifecycle hooks where available** means in 🪝 Hooks, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Deterministic formatting** — Automatic formatters eliminate style arguments and stop agents from generating unnecessary formatting drift. **Practice:** run the project formatter automatically on changed files.
- **test execution** — Automated hooks can trigger the most relevant tests after changes so feedback reaches the agent quickly. **Practice:** start with fast scoped tests and run broader suites before completion.
- **blocking forbidden writes** — Hard-block sensitive files or directories rather than asking the agent not to touch them. **Practice:** deny `.env`, credentials, generated secrets, or protected migrations and test the block directly.
- **secret scanning** — Secret scanners detect accidentally introduced credentials before they are committed or shared. **Practice:** integrate a scanner into hooks/CI and deliberately test it with a fake secret pattern.
- **architecture checks** — Automated architecture constraints prevent local AI-generated changes from eroding system design. **Practice:** gate CI on dependency/module rules that matter to your platform.

## 14.2 🔐 Permissions

- **Read vs write** — Separate read and write capabilities according to role and risk; many reviewers need no write access at all. **Practice:** use least privilege for each subagent/tool profile.
- **Shell command policies** — Shell access is powerful and should restrict dangerous commands, paths, flags, and arbitrary network/download behavior. **Practice:** allow common build/test commands while requiring approval or denying destructive ones.
- **Network access** — Network egress can leak data or download untrusted artifacts, so it should be explicitly controlled. **Practice:** restrict outbound access in a sandbox and allow only required endpoints.
- **filesystem scope** — Constrain which directories the agent can read or modify to reduce accidental and malicious impact. **Practice:** run an agent in a workspace with protected parent/system paths.
- **allowed/denied tools** — Explicit tool allow/deny lists implement least privilege and make the execution surface auditable. **Practice:** document each tool’s purpose and remove capabilities unused by the role.
- **human approval boundaries** — Approval should be tied to action risk, not inserted randomly into every step. **Practice:** define approval-required actions such as destructive commands, credential changes, or external side effects.

## 14.3 📦 Sandboxing

- **Container/devcontainer** — A containerized workspace provides reproducible dependencies and isolates many filesystem/process effects from the host. **Practice:** run the coding agent inside a devcontainer with only required mounts.
- **disposable environments** — Ephemeral workspaces can be recreated from source if an agent corrupts state, reducing recovery cost. **Practice:** prove you can destroy and recreate the environment with one command.
- **restricted credentials** — Agents should receive short-lived, least-privilege credentials rather than broad developer or production secrets. **Practice:** issue a scoped test credential and verify prohibited operations fail.
- **network egress policy** — Egress policy controls where tools can send data or fetch code, reducing exfiltration and supply-chain risk. **Practice:** whitelist necessary domains and log denied attempts.
- **safe command execution** — Command execution should be bounded by working directory, timeouts, resource limits, and validation. **Practice:** wrap shell execution with timeout and command/path policy checks.

## 14.4 Feedback loops

- **Compile** — Compilation/type checking catches syntax and contract failures early. **Practice:** make compilation a mandatory fast gate after relevant code changes.
- **Unit test** — Unit tests verify local behavior quickly and should cover changed logic and edge cases. **Practice:** run focused unit tests during iteration and the full relevant suite before completion.
- **Integration test** — Integration tests validate interactions with databases, queues, services, or model/tool adapters. **Practice:** run at least one realistic integration path for every externally connected feature.
- **lint** — Linting catches style and common correctness issues cheaply. **Practice:** enforce the project linter automatically rather than relying on the agent to remember conventions.
- **static analysis** — Learn what **static analysis** means in Feedback loops, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **architecture tests** — Architecture tests encode module/dependency invariants as executable rules. **Practice:** add one rule for layering or package dependencies and make it part of CI.
- **security scan** — Automated security scanning checks dependencies, secrets, source patterns, or containers for known risks. **Practice:** include scan results in the final verification packet.
- **evals for AI behavior** — Agent/LLM behavior needs evaluation cases beyond normal code tests because outputs are probabilistic. **Practice:** run a stable eval dataset whenever prompts, models, tools, or retrieval logic change.

## 14.5 Harness observability

- **Agent action logs** — Record what the coding/production agent attempted so failures and risky behavior can be reconstructed. **Practice:** log action type, actor/agent, target, timestamp, outcome, and correlation ID.
- **tool-call logs** — Tool-call traces expose arguments, results, latency, and errors at the execution boundary. **Practice:** redact secrets while retaining enough data to debug wrong tool selection or payloads.
- **test outcomes** — Persist test/check results as evidence rather than only a final “done” message. **Practice:** attach command, exit code, and summary to the task record.
- **retry loops** — Observe how often agents repeat model/tool attempts because excessive retries indicate poor prompts, tools, or unstable dependencies. **Practice:** count retries by reason and set alerts/budgets.
- **failure classifications** — Classify failures into model, retrieval, tool, validation, policy, infrastructure, and user-input categories so improvements target the right layer. **Practice:** tag failures during evaluation and review the distribution.
- **cost/time where measurable** — Track resource consumption so agentic workflows do not become economically or operationally unbounded. **Practice:** record duration and model/tool cost per completed engineering task.

## 14.6 Deterministic vs probabilistic enforcement

Put in code/harness when possible: - “never edit `.env`.” - “tests must pass.” - “generated migration must be reversible.” - “PII must not be logged.” - “no production deployment without approval.”

### 🧪 Project Assignment — Self-Checking Engineering Harness

Create hooks/scripts/policies that: - prevent secret/config writes, - auto-format changed files, - run relevant tests, - enforce architecture boundaries, - run dependency/security checks, - prevent completion when required checks fail.

Demonstrate at least five intentionally bad agent changes being blocked.

### 🧪 Additional Project Assignment — `.env` Write-Block Harness Lab

Implement a `PreToolUse` hook in `.claude/settings.json` that rejects writes to `.env*`/secret files. Test the hook independently with representative JSON tool input and a non-zero exit/result for blocked operations. Then demonstrate the same protection during a real Claude Code session.


---


---

# 🧩 Phase 15 — Plugins, Reusable Agent Capabilities & Distribution

> 🟡 **Path:** `P1` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Working**


## 15.1 Plugin model

- **Package reusable skills** — A plugin can distribute proven skills across teams instead of copying instructions manually. **Practice:** include at least one generic skill with tests/examples and no project-specific secrets.
- **Subagents** — Reusable subagents package specialized roles and permissions for consistent team-wide behavior. **Practice:** ship a read-only reviewer or security analyst with clear tool restrictions.
- **commands** — Plugin commands provide standard entry points to workflows such as review, migration analysis, or test generation. **Practice:** keep command names and parameters stable and document expected outputs.
- **hooks** — Bundled hooks make mandatory guardrails/install-time behavior consistent across repositories. **Practice:** include a non-destructive hook and verify it works after clean installation.
- **MCP servers/configuration** — Plugins may package or configure external capabilities so agents can access approved systems consistently. **Practice:** document authentication, required permissions, and failure behavior for each server.
- `.claude-plugin/plugin.json` or the current plugin manifest format — Learn what **.claude-plugin/plugin.json or the current plugin manifest format** means in Plugin model, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **versioning** — Reusable agent tooling changes behavior across many repositories, so versions and changelogs are essential. **Practice:** tag releases and test upgrades/rollback in a sample project.

## 15.2 Design for reuse

- **Generic capability vs project-specific knowledge** — Learn what **Generic capability vs project-specific knowledge** means in Design for reuse, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Configuration** — Separate environment/project-specific values from reusable plugin logic. **Practice:** expose documented settings with safe defaults and validation.
- **semantic versioning** — Use version numbers to communicate compatible features versus breaking behavior changes. **Practice:** define what counts as major/minor/patch for your plugin contracts.
- **backward compatibility** — Updates should avoid silently breaking existing commands, skills, hooks, or MCP configurations. **Practice:** maintain compatibility tests across at least one previous version.
- **documentation** — Reusable organizational tooling needs concise installation, usage, permission, and troubleshooting documentation. **Practice:** validate docs by installing from a clean checkout.
- **tests** — Plugin components need automated tests for scripts, hooks, manifests, and expected behavior. **Practice:** run them in CI before publishing a new version.
- **secure defaults** — Default configuration should grant the least privilege and avoid risky behavior until explicitly enabled. **Practice:** audit the clean install and verify destructive/network capabilities are off or approval-gated.

## 15.3 Organizational distribution

- **Team standards** — Centralized plugins/harnesses can encode common engineering expectations while projects retain local context. **Practice:** separate organization-wide policy from project-specific rules.
- **internal marketplace/catalog** — A catalog helps teams discover approved plugins, skills, and MCP servers instead of creating shadow tooling. **Practice:** define metadata such as owner, version, risk level, and supported use cases.
- **approved MCP servers** — Enterprise teams should curate which external capability servers are trusted and supported. **Practice:** create an allowlist with ownership, auth method, data classification, and review date.
- **centrally maintained security hooks** — Critical organization-wide controls should be maintained once and distributed consistently. **Practice:** package a secret/write policy hook and verify teams cannot silently disable it where policy forbids that.
- **shared review agents** — Shared reviewer agents standardize checks such as security, API design, or architecture across repositories. **Practice:** benchmark them on known-good and known-bad changes before broad rollout.
- **upgrade governance** — Tooling updates can alter agent autonomy and behavior, so upgrades need testing, version control, and rollback. **Practice:** introduce a staging repository/canary process for new plugin versions.

### 🧪 Project Assignment — Enterprise Engineering Plugin

Package the Phase 10 and 14 capabilities as a reusable internal plugin/toolkit for Spring Boot teams. Install it into a second repository without copying project-specific instructions.

### 🧪 Additional Project Assignment — Clean-Checkout Plugin Verification

Bundle the policy reviewer/test writer, at least one reusable skill, one hook, and an MCP capability into a single plugin/toolkit. Install it from a clean checkout and verify that the agents, MCP capability, hooks, and skill are discoverable without manual file copying.


---


---

# ☁️ Phase 16 — Cloud Agent Platforms & Deployment

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 16.1 AWS

- **Amazon Bedrock model access** — Bedrock provides managed access to multiple foundation models under AWS identity, networking, and governance controls. **Practice:** call a model with IAM-authenticated code and capture model/usage metadata.
- **Knowledge Bases** — Bedrock Knowledge Bases provide managed ingestion/retrieval capabilities for RAG use cases. **Practice:** build a small managed knowledge base and compare control/quality with your custom RAG pipeline.
- **Guardrails** — Managed guardrails can filter or constrain model inputs/outputs according to policy categories and sensitive information rules. **Practice:** configure a small policy and test both allowed and blocked examples.
- Bedrock AgentCore capabilities such as Runtime, Gateway, Memory, Identity, code/browser tooling, and observability where appropriate.
- Strands Agents SDK awareness and comparison with LangGraph/vendor SDK approaches.
- **Identity** — Agent platforms need workload/user identity so tools and data access can be authorized per principal. **Practice:** trace a user/agent identity through one tool call and verify least-privilege access.
- **memory** — LangChain4j memory abstractions manage conversational context but should not be confused with durable business state. **Practice:** implement bounded chat memory and compare it with external persistent state.
- **gateways/tools** — Managed gateways can expose enterprise APIs/tools to agents with centralized discovery and policy. **Practice:** connect one internal mock API and enforce authentication plus an action scope.
- **observability** — Cloud-native tracing/metrics should make model, tool, and workflow behavior visible alongside ordinary service telemetry. **Practice:** trace one end-to-end agent request through model and tool spans.
- **VPC/private networking** — Private networking keeps sensitive model/tool traffic off public paths and controls egress to enterprise systems. **Practice:** draw the network path and identify which endpoints/security groups/policies are required.
- **IAM** — AWS IAM defines which identities can invoke models, tools, stores, and infrastructure. **Practice:** create a least-privilege policy for one agent runtime rather than using broad developer permissions.
- **cost controls** — Cloud agents can generate variable inference/tool/compute cost and need budgets, quotas, and usage attribution. **Practice:** estimate cost per task and define alarms or routing rules for expensive workloads.

## 16.2 Microsoft/Azure

**Depth: Working**

- **Microsoft Foundry / Foundry Agent Service** — Learn what **Microsoft Foundry / Foundry Agent Service** means in Microsoft/Azure, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- Microsoft Agent Framework awareness, including its relationship to prior AutoGen/Semantic Kernel ecosystems.
- **Azure AI Search** — Azure AI Search provides enterprise search/vector/hybrid retrieval integrated with Microsoft’s cloud ecosystem. **Practice:** build a small hybrid index and compare its filtering/security model with your primary vector store.
- **Entra/enterprise agent identity and governance concepts** — Learn what **Entra/enterprise agent identity and governance concepts** means in Microsoft/Azure, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **OpenTelemetry integration** — OpenTelemetry gives a vendor-neutral way to correlate AI spans with normal distributed traces. **Practice:** emit model/tool/retrieval spans into your chosen backend and follow one request end to end.

## 16.3 Google Cloud

**Depth: Aware/Working** - Vertex AI agent services. - ADK. - Gemini integration. - managed deployment.

## 16.4 Deployment patterns

- **Containers** — Containers package your agent service and dependencies consistently across environments. **Practice:** build a minimal non-root image with health checks and externalized configuration.
- **Kubernetes** — Deploy Java AI services with the same resource, scaling, secret, health, and network controls as other workloads. **Practice:** configure probes, resource limits, and externalized state.
- **Serverless** — Serverless is useful for bursty or short-lived agent components but may be constrained by execution duration, connection model, or cold starts. **Practice:** identify which nodes fit serverless and which need long-running workers.
- **Long-running workers** — Durable agent workflows may require workers that outlive a single HTTP request. **Practice:** process one job asynchronously from a queue and persist status/checkpoints.
- **SSE/WebSockets** — SSE and WebSockets stream agent progress/events to clients; SSE is simpler for one-way server streaming while WebSockets support bidirectional interaction. **Practice:** implement progress streaming and reconnect behavior.
- **queues/events** — Queues decouple long-running work, absorb bursts, and support retry/dead-letter semantics. **Practice:** place one agent task behind a queue and define idempotent consumer behavior.
- **asynchronous jobs** — Long AI work should often return a job ID and complete asynchronously rather than holding a synchronous request open. **Practice:** expose submit/status/result endpoints for one workflow.
- **session affinity/state externalization** — Do not rely on one process holding conversation/workflow state if the service must scale horizontally. **Practice:** persist state externally and prove a request can resume on another instance.

### 🧪 Project Assignment — Cloud Deployment

Deploy the fraud-triage system with managed identity, private enterprise tools, persisted state, guardrails and observability. Document scaling, failure domains and estimated cost drivers.

### 🧪 Additional Project Assignment — Deploy Fraud Triage to AWS AgentCore

Deploy the fraud-triage workflow using Bedrock/AgentCore capabilities: MCP-backed enterprise tools through a managed gateway where appropriate, managed identity, durable memory, Bedrock Guardrails, and CloudWatch/OpenTelemetry observability. Rebuild one small specialist with Strands Agents SDK and document the trade-offs.


---


---

# 📈 Phase 17 — AgentOps: Evals, Observability, Security & Reliability

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 17.1 🧪 Evaluation

- **Golden datasets** — A golden dataset is a curated set of representative inputs with expected outcomes or grading criteria used for regression evaluation. **Practice:** start small with difficult/important production cases and version it with the system.
- **Unit-style prompt/model tests** — Small deterministic-ish checks catch obvious regressions in prompts, schemas, routing, or tool selection. **Practice:** run them frequently and reserve expensive end-to-end evaluations for broader gates.
- **Structured-output validity** — Track whether outputs satisfy required schemas because invalid structure is an objective production failure. **Practice:** measure schema pass rate and inspect recurring invalid fields.
- **LLM-as-judge with calibration** — A judge model can scale subjective evaluation, but its rubric and agreement with humans must be validated. **Practice:** compare judge scores with human labels and adjust the rubric until disagreement is understood.
- **Human review** — Human evaluation remains necessary for nuanced correctness, safety, and calibration of automated metrics. **Practice:** periodically sample outputs and use a consistent rubric rather than informal impressions.
- **A/B tests** — A/B tests compare model/prompt/retrieval variants on real or representative traffic while controlling other variables. **Practice:** define one success metric and evaluate statistical/practical significance before rollout.
- **regression suites** — Regression suites preserve known failure cases so fixed problems do not return. **Practice:** add every important production/eval failure as a permanent test case.
- **trajectory evaluation** — Agent evaluation should inspect the sequence of decisions/tool calls, not only the final answer. **Practice:** score whether the agent chose the correct tools, order, retries, and stop condition.
- **tool-selection correctness** — Wrong tool choice can be more harmful than a poorly worded answer. **Practice:** build labeled cases specifying expected/forbidden tools and measure selection accuracy.
- **task completion** — Task completion measures whether the intended business outcome occurred, not whether the model produced plausible text. **Practice:** define a verifiable completion signal for each major agent use case.
- **cost/latency budgets** — Set explicit service-level budgets so quality improvements do not create unacceptable expense or response time. **Practice:** fail or flag evaluations that exceed target cost or p95 latency.

Tools to know: - LangSmith. - RAGAS. - DeepEval. - promptfoo. - Langfuse. - Arize Phoenix awareness.

## 17.2 🔭 Observability

- **LLM spans** — Trace each model invocation with model, prompt/version identifiers, latency, tokens, status, and safe metadata. **Practice:** correlate model spans with the parent request/agent node.
- **tool spans** — Tool spans show what external capability was invoked, how long it took, and whether it succeeded. **Practice:** attach tool name, sanitized arguments, result status, and retry count.
- **retrieval spans** — Retrieval spans expose query, filters, candidate counts, ranking stages, and timing so RAG failures can be localized. **Practice:** log retrieved document IDs/scores without leaking sensitive content.
- **agent graph transitions** — Tracing node/edge transitions explains how the controller moved through the workflow and where it looped or escalated. **Practice:** visualize one successful and one failed trajectory.
- **token/cost attribution** — Attribute model usage to feature, tenant, workflow, and node so optimization targets the real cost drivers. **Practice:** produce cost-per-task and cost-by-node metrics.
- **p50/p95/p99 latency** — Percentile latency reveals tail behavior hidden by averages and is critical for multi-call agent workflows. **Practice:** measure end-to-end and per-node percentiles under representative concurrency.
- **tool failure rates** — Track failure rates by tool and reason to distinguish model mistakes from downstream reliability issues. **Practice:** dashboard timeout, validation, auth, and dependency failures separately.
- **retry counts** — High retry counts often signal weak routing, unstable dependencies, or overly strict schemas. **Practice:** track retries by reason and set a maximum budget per task.
- **model fallback** — Fallback switches to another model/provider when the preferred option is unavailable or fails quality/policy checks. **Practice:** test fallback explicitly and ensure output/tool contracts remain compatible.
- **OpenTelemetry GenAI conventions** — Use emerging GenAI semantic conventions so AI telemetry remains interoperable across observability backends. **Practice:** map your model/tool/retrieval attributes to standard OTel names where available.

## 17.3 🛡️ Security

- OWASP Top 10 for LLM/GenAI applications as a threat-modeling baseline.
- **Prompt injection** — Prompt injection tries to make the model ignore trusted instructions or misuse tools through malicious user/content instructions. **Practice:** create attack cases and enforce instruction boundaries, tool authorization, and content isolation.
- **indirect prompt injection** — Indirect injection arrives through retrieved documents, web pages, emails, or tool output rather than the direct user message. **Practice:** treat external content as untrusted data and test malicious instructions inside RAG documents.
- **insecure output handling** — Model output must not be blindly executed, rendered, queried, or passed to privileged systems. **Practice:** validate/escape outputs and use typed tool interfaces instead of executing generated commands/SQL directly.
- **excessive agency** — Giving the model broader permissions than the task needs increases impact when it makes a mistake or is manipulated. **Practice:** reduce tools/scopes and require approval for high-impact actions.
- **sensitive information disclosure** — Models or tools may leak secrets, PII, or cross-tenant data through prompts, logs, retrieval, or output. **Practice:** classify/redact sensitive fields and test isolation boundaries.
- **tool abuse** — A valid tool can be called for an invalid purpose, so authorization must verify intent, identity, and resource scope—not just schema validity. **Practice:** test unauthorized but syntactically valid tool requests.
- **data exfiltration** — Attackers may try to cause tools/models to send protected data to external destinations. **Practice:** restrict egress, tool destinations, and payload classes and monitor suspicious transfers.
- **poisoned retrieval** — Malicious or corrupted documents can manipulate generated answers or agent decisions. **Practice:** track provenance/trust levels and include adversarial documents in RAG security tests.
- **poisoned MCP tools** — A malicious or changed MCP server/tool description/result can influence agent behavior or steal data. **Practice:** approve servers, pin/trust versions, validate tool metadata/results, and use least privilege.
- **supply-chain risk** — Agent systems depend on SDKs, models, plugins, MCP servers, packages, and containers that can introduce compromised behavior. **Practice:** maintain dependency provenance, scanning, pinning, and controlled upgrades.

## 17.4 ⚙️ Reliability

- **Timeouts** — Timeouts bound dependency delay and prevent one hung model/tool from consuming the entire request budget. **Practice:** define per-call and end-to-end deadlines and test timeout recovery.
- **circuit breakers** — Circuit breakers stop repeatedly calling an unhealthy dependency and allow it time to recover. **Practice:** trip a breaker with simulated failures and verify fallback/degraded behavior.
- **retry with jitter** — Jitter spreads retry attempts so many workers do not hammer a recovering service simultaneously. **Practice:** implement bounded exponential backoff with randomness and observe retry timing.
- **rate limiting** — Rate limiting protects providers, tools, tenants, and your own cost envelope from excessive traffic. **Practice:** enforce both global and per-user/tenant limits where relevant.
- **bulkheads** — Bulkheads isolate capacity so one failing or expensive workflow cannot exhaust resources used by others. **Practice:** separate concurrency pools/queues for high-cost and normal tasks.
- **idempotency** — Idempotency lets duplicate requests/retries produce one logical side effect. **Practice:** assign idempotency keys to any payment, write, notification, or external mutation tool.
- **compensation** — When a multi-step workflow cannot roll back transactions atomically, compensating actions restore business consistency. **Practice:** design a saga-like compensation path for one failed side-effect sequence.
- **durable checkpoints** — Persistent checkpoints allow long workflows to survive process/node failures without restarting from scratch. **Practice:** verify checkpoint restore across a real application restart.
- **graceful degradation** — When advanced AI capabilities fail, the product should fall back to reduced but safe functionality where possible. **Practice:** define a non-agent/manual or simpler model path for one dependency outage.
- **model fallback** — Fallback switches to another model/provider when the preferred option is unavailable or fails quality/policy checks. **Practice:** test fallback explicitly and ensure output/tool contracts remain compatible.
- **semantic caching where appropriate** — Semantic caches reuse answers/results for meaningfully similar requests, reducing latency/cost but risking staleness or incorrect reuse. **Practice:** apply only to safe read-only tasks with TTL and similarity thresholds.

## 17.5 🏛️ Governance

- **Prompt/model/version registry** — Track which prompt, model, embedding, tool, and configuration versions produced a result so behavior is reproducible. **Practice:** include version identifiers in traces and deployment metadata.
- **evaluation gates** — Deployment should be blocked when critical quality, safety, cost, or latency metrics regress beyond thresholds. **Practice:** wire a small eval suite into CI and make one deliberate bad change fail the gate.
- **auditability** — Learn what **auditability** means in 🏛️ Governance, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- EU AI Act awareness, especially risk classification, transparency, human oversight and governance implications for European deployments.
- Guardrail framework awareness: NeMo Guardrails, Guardrails AI, and managed cloud/vendor guardrails.
- **data residency** — Regulated or enterprise data may be required to remain in specific geographic/legal regions. **Practice:** map where prompts, logs, vectors, memories, and backups are stored and processed.
- **retention** — Production logs, prompts, memory, and evaluation data need explicit retention periods based on policy and usefulness. **Practice:** define retention classes and deletion processes for each data type.
- **human oversight** — High-risk automated decisions should remain reviewable, interruptible, and attributable to responsible humans. **Practice:** define when humans can override, approve, or audit agent decisions.

### 🧪 Project Assignment — Harden and Ship

Create 40+ eval cases including injection, retrieval failure, malformed tool output and timeout scenarios. Gate CI on eval thresholds, export traces through OpenTelemetry, create reliability dashboards, and publish a failure-mode analysis.

### 🧪 Additional Project Assignment — LangSmith/Langfuse Hardening Lab

Create an evaluation dataset with normal, prompt-injection, and tool-failure cases; add trajectory/task-completion evaluation to CI; export OpenTelemetry GenAI traces to Langfuse or an equivalent backend; add an input guardrail layer; and chart cost-per-task, p95 latency, and eval-score trend.


---


---

# 🔄 Phase 18 — AI-Native SDLC: CI/CD, Testing, Code Review & Governance

> 🟣 **Path:** `P1+P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 18.1 AI-assisted development lifecycle

`Requirement → Plan → Context → Implement → Test → Review → Security → Eval → Deploy → Observe`

## 18.2 Testing layers

- **Unit tests for deterministic code** — Normal code around the agent still needs conventional fast tests for business logic, parsers, validators, and adapters. **Practice:** keep deterministic logic outside prompts where possible and test it normally.
- **Contract tests for tools/MCP** — Tool/MCP contracts should verify schemas, auth, error semantics, and backward compatibility independently of the model. **Practice:** test each server/tool with direct client calls.
- **Retrieval tests** — Retrieval tests measure whether expected evidence is returned for known questions before generation is involved. **Practice:** maintain labeled query→document expectations and run them in CI.
- **prompt regression** — Prompt regression testing checks that known behaviors remain stable across prompt/model changes. **Practice:** version prompts and run representative cases before merge.
- **agent trajectory tests** — Trajectory tests validate the expected sequence/constraints of tool calls and workflow transitions. **Practice:** assert forbidden tools are never called and required approvals occur.
- **security/adversarial tests** — Adversarial tests deliberately try injection, unauthorized access, data leakage, tool abuse, and unsafe outputs. **Practice:** maintain a red-team set and rerun it on meaningful architecture/model changes.
- **end-to-end business tests** — E2E tests verify the complete business outcome across model, tools, data, approvals, and side effects. **Practice:** automate at least a few critical happy/failure paths in a production-like environment.

## 18.3 CI/CD

- **Build/test/lint** — These conventional gates remain the baseline for AI-generated code. **Practice:** make them non-optional CI checks and expose the same commands to the coding agent.
- **architecture checks** — Automated architecture constraints prevent local AI-generated changes from eroding system design. **Practice:** gate CI on dependency/module rules that matter to your platform.
- **dependency scanning** — Scan libraries and containers for known vulnerabilities and risky licenses/supply-chain changes. **Practice:** fail or review upgrades that introduce high-severity issues.
- **prompt/eval regression** — AI artifacts should have their own CI gate so a code-clean change cannot silently degrade model behavior. **Practice:** run a small fast eval on every PR and broader evals before release.
- **model change validation** — Switching model/version can change reasoning, tool selection, latency, or output even when application code is unchanged. **Practice:** run the same regression suite before promoting a model change.
- **deployment approval** — High-impact releases should require policy/owner approval after automated evidence is available. **Practice:** tie approval to build, security, and eval results rather than informal confidence.
- **canary model/prompt releases** — Canary releases expose a small traffic slice to the new model/prompt before full rollout. **Practice:** define rollback thresholds for quality, error rate, latency, and cost.

## 18.4 Code review with coding agents

- **Agent-generated code is not exempt from normal review** — Learn what **Agent-generated code is not exempt from normal review** means in Code review with coding agents, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Verify requirements and architectural fit** — Learn what **Verify requirements and architectural fit** means in Code review with coding agents, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Security and dependency scrutiny** — Learn what **Security and dependency scrutiny** means in Code review with coding agents, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Detect plausible but nonexistent APIs** — Learn what **Detect plausible but nonexistent APIs** means in Code review with coding agents, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Require evidence for tests** — Learn what **Require evidence for tests** means in Code review with coding agents, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Small reviewable diffs** — Learn what **Small reviewable diffs** means in Code review with coding agents, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Human accountability remains explicit** — Learn what **Human accountability remains explicit** means in Code review with coding agents, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.

## 18.5 Governance of coding-agent autonomy

Define autonomy levels: 1. read/explain, 2. propose plan, 3. edit with approval, 4. execute tests/tools, 5. open PR, 6. autonomous bounded workflow, 7. deployment/production action — heavily controlled.

### 🧪 Project Assignment — AI-Native Delivery Pipeline

Create a GitHub Actions pipeline that runs conventional tests plus AI evals, MCP contract tests, security checks and architecture tests. Use Claude Code to implement a change, but make the harness independently prove whether the change is acceptable.


---


---

# ☕ Phase 19 — Java/Spring Enterprise Agentic AI Track

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 19.1 Spring AI

- **Chat/model clients** — Spring AI model clients provide a Java abstraction for invoking models and composing prompts/tools. **Practice:** implement a typed model call and inspect the underlying provider-specific behavior when necessary.
- **structured outputs** — Use Spring AI conversion/schema support to turn model results into validated Java types instead of parsing prose. **Practice:** map a result into a record/DTO and reject invalid values.
- **tool calling** — Spring AI can expose Java methods as model tools, but arguments still need authorization and validation. **Practice:** create one read-only tool and one side-effecting tool with explicit safeguards.
- **advisors** — Spring AI advisors add reusable cross-cutting behavior such as RAG/context around model calls. **Practice:** add one advisor and trace exactly what context it injects.
- **RAG** — Spring AI provides retrieval/advisor abstractions for Java-native RAG integration. **Practice:** connect a vector store, retrieve evidence, and return citations from a Spring service.
- **vector-store abstraction** — The abstraction standardizes common vector operations but underlying stores still differ in indexing, filtering, and operations. **Practice:** understand the native query produced by your chosen implementation.
- **MCP client/server** — Spring AI can participate in MCP as a Java client or server, letting enterprise services expose/consume agent capabilities. **Practice:** publish one Spring service capability over MCP and call it from another agent.
- **observability integration** — Instrument Spring AI interactions alongside standard Micrometer/OpenTelemetry telemetry so AI calls appear in normal service traces. **Practice:** correlate an HTTP request with model and tool spans.

## 19.2 LangChain4j

- **AI services** — LangChain4j AI Services provide declarative Java interfaces backed by models, tools, memory, and retrieval. **Practice:** define a small interface and inspect how types/tools are mapped.
- **tools** — Expose Java business capabilities to the model through typed, narrow methods. **Practice:** apply validation, authorization, and idempotency just as you would for any external API.
- **RAG** — Spring AI provides retrieval/advisor abstractions for Java-native RAG integration. **Practice:** connect a vector store, retrieve evidence, and return citations from a Spring service.
- **memory** — LangChain4j memory abstractions manage conversational context but should not be confused with durable business state. **Practice:** implement bounded chat memory and compare it with external persistent state.
- **model providers** — Provider abstractions allow Java applications to switch between supported LLM backends. **Practice:** configure two providers and identify features that do not abstract cleanly.
- **enterprise Java integration** — The goal is to integrate AI into existing security, transactions, messaging, observability, and deployment standards rather than create an isolated Python island. **Practice:** connect the agent feature to one real enterprise pattern such as Kafka or OAuth.

## 19.3 LangGraph4j / Java orchestration awareness

- **Graph/state concepts in Java** — Understand how graph nodes, typed state, edges, retries, and checkpoints map into Java orchestration libraries or your own workflow code. **Practice:** model a small stateful flow in Java and compare with LangGraph Python.
- **When to keep orchestration in Python vs Java** — Choose based on ecosystem maturity, team ownership, integration boundaries, latency, and operational consistency—not language ideology. **Practice:** write an ADR for one system deciding where the orchestrator belongs.
- **Interoperability through HTTP/events/MCP** — Use explicit protocols to connect Java and Python components so each can use its strongest ecosystem without tight coupling. **Practice:** integrate one cross-language call via MCP or an event/API contract.

## 19.4 Enterprise integration

- **Existing Spring microservices** — Agentic capabilities should fit existing bounded contexts and service ownership rather than bypass established architecture. **Practice:** add an AI capability behind a current service boundary instead of creating duplicate data ownership.
- **OAuth/OIDC** — Use existing identity standards for user/service authentication and propagate identity into tool authorization. **Practice:** protect an AI endpoint and verify downstream tool access uses the caller’s allowed scope.
- **API gateway** — An API gateway centralizes routing, auth, rate limits, and policy for external service access, while MCP may expose capability-oriented agent interfaces separately. **Practice:** document which traffic belongs through the gateway versus MCP.
- **Kafka** — Kafka supports asynchronous events and decoupled long-running workflows around agent decisions. **Practice:** publish one agent task/result event with correlation and idempotency identifiers.
- **transaction boundaries** — LLM/tool calls should not hold database transactions open for long unpredictable periods. **Practice:** separate durable DB transactions from external AI calls and use workflow/saga patterns where needed.
- **Resilience4j** — Resilience4j supplies timeouts, retries, circuit breakers, rate limiting, and bulkheads for unreliable external model/tool dependencies. **Practice:** wrap an LLM or mock tool call with a timeout, bounded retry, and circuit breaker, then simulate failures.
- **OpenTelemetry** — Use the same distributed tracing substrate for Java services and AI components to maintain one operational picture. **Practice:** propagate trace context across HTTP/Kafka/MCP boundaries.
- **Kubernetes** — Deploy Java AI services with the same resource, scaling, secret, health, and network controls as other workloads. **Practice:** configure probes, resource limits, and externalized state.
- **secrets/IAM** — Credentials for model providers, databases, and tools must stay outside prompts/source and use platform secret/identity mechanisms. **Practice:** use workload identity or secret manager integration and verify logs do not expose credentials.

## 19.5 Positioning

Be able to demonstrate: \> “I can introduce Agentic AI into an existing Java/Spring enterprise estate without requiring a wholesale Python rewrite.”

### 🧪 Project Assignment — Java Agentic Payments Service

Build a Spring Boot service using Spring AI that exposes tools, consumes an MCP server, uses RAG, produces structured output, emits OpenTelemetry traces, and integrates with an existing Python/LangGraph supervisor.


---


---

# 🏆 Phase 20 — Integrated Production Capstone

> 🟣 **Path:** `P1+P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


Choose **one** capstone and build it deeply. The objective is not another demo; it is evidence that you can engineer both the **runtime agent system** and the **AI-native engineering environment** used to deliver it.

## Option A — Agentic Payment Operations Copilot

Capabilities: - Failed-payment investigation. - Transaction/customer tools. - Regulation RAG. - Multi-agent orchestration. - Human-approved refunds/account actions. - MCP capability layer. - Durable state/memory. - Full eval suite. - Cloud deployment. - Java/Spring enterprise integration.

## Option B — Engineering Intelligence & Delivery Agent

Capabilities: - Repository/PR/CI ingestion. - DORA and engineering-health tools. - RAG over architecture/runbooks. - Root-cause analysis of delivery degradation. - Planner/reviewer/security agents. - MCP interfaces to engineering systems. - HITL before repository/CI changes.

## Mandatory Path 1 deliverables

- `CLAUDE.md`.
- scoped rules.
- at least 3 production-quality skills.
- at least 3 specialized subagents.
- reusable commands/workflows.
- deterministic hooks.
- MCP configuration.
- secure permission model.
- reusable plugin/toolkit.
- Plan → Execute → Verify workflow.
- session/work continuity strategy.

## Mandatory Path 2 deliverables

- direct model SDK integration.
- structured outputs.
- tool calling.
- RAG with retrieval evaluation.
- LangGraph orchestration.
- state + durable checkpointing.
- long-term memory where justified.
- MCP server(s).
- multi-agent workflow where justified.
- HITL.
- evaluation dataset.
- OpenTelemetry tracing.
- security/adversarial tests.
- cloud deployment.
- cost/latency/reliability metrics.

## Mandatory architecture documents

1.  Context architecture.
2.  Agent topology.
3.  RAG architecture.
4.  MCP capability architecture.
5.  Security/threat model.
6.  Memory/state model.
7.  Deployment architecture.
8.  Eval strategy.
9.  Reliability model.
10. Agent autonomy/governance matrix.

## Portfolio evidence

- Architecture diagram.
- README with business problem.
- 3–5 minute demo.
- Evaluation results.
- Failure cases and fixes.
- Cost/latency measurements.
- ADRs explaining major trade-offs.
- Screenshots/traces of observability.
- Example Claude Code Plan → Execute → Verify delivery.


---


---

# Phase 21 — Claude Code Assessment & Live Engineering Playbook

> 🟡 **Path:** `P1` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Working**


This is an interview/assessment-specific practice phase. It is not a substitute for production knowledge; it trains you to demonstrate that knowledge while directing a coding agent.

## 21.1 Before the assessment

- **Confirm Claude Code and credentials work before the session** — Learn what **Confirm Claude Code and credentials work before the session** means in Before the assessment, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- Keep a minimal, reusable `CLAUDE.md` skeleton ready — Learn what **Keep a minimal, reusable CLAUDE.md skeleton ready** means in Before the assessment, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- Have a scratch repository initialized and complete one full test round-trip beforehand.
- Avoid spending assessment time debugging tooling setup.

## 21.2 During the assessment

- **Restate the requirement and constraints** — Learn what **Restate the requirement and constraints** means in During the assessment, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Sketch architecture before coding** — Learn what **Sketch architecture before coding** means in During the assessment, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Establish project context deliberately** — Learn what **Establish project context deliberately** means in During the assessment, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Use planning mode for non-trivial work and explain why** — Learn what **Use planning mode for non-trivial work and explain why** means in During the assessment, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- **Delegate only genuinely separable concerns to subagents** — Learn what **Delegate only genuinely separable concerns to subagents** means in During the assessment, where it belongs in the architecture, and its main trade-offs or failure modes. **Practice:** implement or configure a minimal example and write down when you would choose it in production.
- Run tests and inspect diffs; do not accept generated code merely because it compiles.
- Narrate production concerns: idempotency, observability, rollback, security, reliability, and maintainability.
- Keep `NOTES.md` or equivalent evidence of plan, execution, and verification.

### 🎙️ Rehearsal Assignment — Live Round-Trip Dry Run

In a scratch repository, complete a timed 15–20 minute exercise: initialize context, write/refine `CLAUDE.md`, narrate a planning decision, delegate one isolated task to a subagent, run a real test, inspect the diff, challenge at least one questionable change if present, and close with a concise `NOTES.md` verification entry.


---


# 📅 Recommended Weekly Study Pattern

Do **not** study Path 1 and Path 2 as two isolated courses.

Use this loop:

1.  **Learn the Path 2 concept manually.**
2.  **Implement it without a heavy framework when feasible.**
3.  **Implement/rebuild it with the appropriate framework.**
4.  **Use Claude Code as the engineering agent while building it.**
5.  **Add the Path 1 context/skill/subagent/harness capability that makes the work repeatable.**
6.  **Evaluate both the application agent and the coding workflow.**

Example:

`Tool calling → framework-free agent → LangGraph agent → expose tool via MCP → connect MCP to Claude Code → create skill/subagent → enforce tests with hooks → add evals`

This prevents two common failure modes: - knowing Claude Code configuration without understanding production Agentic AI internals; - knowing LangChain/LangGraph APIs while still using coding agents as ungoverned chat assistants.


---


# 🎯 Competency Matrix

| Competency                  | Path  | Depth           |
|:----------------------------|:------|:----------------|
| Python                      | P2    | Deep            |
| Java/Spring                 | P2    | Deep            |
| LLM fundamentals            | P2    | Deep            |
| OpenAI SDK                  | P2    | Deep            |
| Anthropic SDK               | P2    | Deep            |
| Structured outputs          | P2    | Deep            |
| Tool/function calling       | P2    | Deep            |
| Prompt engineering          | P2    | Deep            |
| Context engineering         | P1+P2 | Deep            |
| Agent patterns              | P2    | Deep            |
| Loading/splitting/chunking  | P2    | Deep            |
| Embeddings/vector retrieval | P2    | Deep            |
| Basic/advanced RAG          | P2    | Deep            |
| Graph RAG                   | P2    | Working-to-Deep |
| Agentic RAG                 | P2    | Deep            |
| State/memory                | P2    | Deep            |
| LangChain                   | P2    | Working-to-Deep |
| LangGraph                   | P2    | Deep            |
| Multi-agent systems         | P2    | Deep            |
| OpenAI Agents SDK           | P2    | Deep            |
| Claude Agent SDK            | P2    | Deep            |
| Google ADK                  | P2    | Working         |
| Claude Code                 | P1    | Deep            |
| `CLAUDE.md` hierarchy       | P1    | Deep            |
| Rules                       | P1    | Deep            |
| Skills                      | P1    | Deep            |
| Commands                    | P1    | Working-to-Deep |
| Subagents                   | P1    | Deep            |
| Hooks                       | P1    | Deep            |
| Permissions/sandboxing      | P1    | Deep            |
| Plugins                     | P1    | Working         |
| MCP client                  | P1+P2 | Deep            |
| MCP server                  | P1+P2 | Deep            |
| MCP security                | P1+P2 | Deep            |
| A2A                         | P2    | Working         |
| Agentic Engineering         | P1    | Deep            |
| Harness Engineering         | P1    | Deep            |
| Cloud agent platforms       | P2    | Working-to-Deep |
| Evals                       | P2    | Deep            |
| Observability/OpenTelemetry | P2    | Deep            |
| Agent security              | P1+P2 | Deep            |
| AI-native CI/CD             | P1+P2 | Deep            |
| Autonomy governance         | P1+P2 | Deep            |


---


# 🥇 What to Learn First — Final Priority

## 🥇 Tier 1 — Foundation: do not skip

1.  Python/Pydantic/FastAPI.
2.  LLM fundamentals.
3.  Direct OpenAI/Anthropic SDK usage.
4.  Structured outputs.
5.  Tool calling.
6.  Prompt/context engineering.
7.  Framework-free agent loop.
8.  Embeddings, chunking and RAG.

## 🥈 Tier 2 — Production Agent Engineering

9.  Advanced/Agentic RAG.
10. State and memory.
11. LangGraph.
12. MCP.
13. Evaluation and observability.
14. Security and guardrails.
15. Production reliability.

## 🥉 Tier 3 — Deep Agentic Software Engineering

16. Claude Code layered context.
17. Rules and skills.
18. Subagents and commands.
19. Agentic Engineering.
20. Hooks, permissions and harness engineering.
21. Plugins/reusable organizational capabilities.

## 🚀 Tier 4 — Synthesis

22. Multi-agent/vendor SDKs.
23. Cloud agent platforms.
24. Java/Spring AI integration.
25. AI-native SDLC.
26. Integrated production capstone.


---


# ✅ Completion Criteria

You are ready to claim production-oriented competence only when you can answer **yes** to all of these:

- Can I build a tool-using agent without LangChain/LangGraph?
- Can I explain why a workflow should be deterministic or agentic?
- Can I design and evaluate chunking/retrieval rather than simply call a vector store?
- Can I measure RAG retrieval and generation quality separately?
- Can I design state, checkpointing and memory deliberately?
- Can I build and secure an MCP server?
- Can I explain MCP’s role in both coding-agent and application-agent architectures?
- Can I design LangGraph state/edges/retries/HITL rather than copy a tutorial graph?
- Can I instrument model/tool/retrieval calls and diagnose a failed agent trajectory?
- Can I create a small, maintainable `CLAUDE.md` instead of dumping all knowledge into it?
- Can I decide whether knowledge belongs in a rule, skill, subagent, MCP server, hook, or application RAG system?
- Can I enforce critical coding-agent constraints deterministically?
- Can I run Plan → Execute → Verify with specialized agents and clear ownership?
- Can I constrain coding-agent autonomy based on action risk?
- Can I integrate Agentic AI into a Java/Spring enterprise estate?
- Can I demonstrate one deployed system with evals, security, observability and measurable reliability?

If all are **yes**, the two learning paths have converged into the target capability:

> **Production Agentic AI Engineering + AI-Native Software Engineering**

---

## 🌟 Target End-State

> **Production Agentic AI Engineering + AI-Native Software Engineering**
>
> You should be able to **design, build, evaluate, secure, operate, and explain production AI agents** while also creating a **controlled, context-rich, verifiable coding-agent environment** for developing those systems.

**Edition:** August 2026  
**Primary learning principle:** *Understand the mechanism → build it manually → adopt the framework → automate it with a governed coding-agent harness.*
