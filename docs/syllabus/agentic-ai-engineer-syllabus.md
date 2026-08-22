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

- **Building with an agent** vs **building an agent**.
- Coding agent as engineering collaborator vs LLM/agent as a runtime component of your product.
- Why `CLAUDE.md`, skills, hooks, and coding subagents do not replace RAG, runtime memory, model APIs, evals, or application-agent orchestration.
- Why application-agent frameworks do not replace a well-engineered coding harness.

## 0.2 Agentic Coding

- One coding agent operating over repository context.
- Read → reason/plan → edit → execute → inspect → iterate.
- Human review of diffs and side effects.
- Appropriate autonomy boundaries.
- Task scoping and acceptance criteria.

## 0.3 Agentic Engineering

- Plan → Execute → Verify.
- Specialized roles: planner, implementer, tester, reviewer, security reviewer.
- Separation of concerns between agents.
- Context isolation.
- Human checkpoints at consequential boundaries.

## 0.4 Harness Engineering

- Engineer the environment rather than merely improve prompts.
- Context, tools, permissions, hooks, sandboxes, tests, feedback loops, observability.
- Deterministic enforcement vs probabilistic instructions.
- Principle: if a rule **must** hold, enforce it outside the model where practical.

## 0.5 Product Agentic AI

- Agent = model + instructions/context + tools + state/memory + control loop + goal + guardrails.
- Agent vs deterministic workflow.
- Autonomy spectrum.
- When **not** to use an agent.

### 🧪 Project Assignment — Architecture Classification Exercise

Take 15 requirements from a realistic payments platform. Classify each as: 1. conventional software, 2. deterministic AI workflow, 3. application agent, 4. coding-agent task, 5. harness concern.

For every classification, document why additional autonomy is or is not justified.


---


---

# 🐍 Phase 1 — Python/Java AI Engineering Foundation + LLM Fundamentals

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 1.1 Python for enterprise engineers

- Python 3.12/3.13.
- Type hints, protocols, dataclasses, generators.
- `async`/`await`, concurrency and I/O.
- Context managers and decorators.
- `uv`, Ruff, pytest.
- Pydantic v2.
- FastAPI.
- Map concepts to Java records, generics, Bean Validation, Jackson and `CompletableFuture`.

## 1.2 Java continuity

- Modern Java 21+.
- Spring Boot.
- HTTP clients and reactive/asynchronous integration.
- Jackson/schema validation.
- Resilience4j.
- Why Python should be learned without abandoning Java enterprise leverage.

## 1.3 LLM fundamentals

- Tokens and tokenization.
- Context windows.
- Transformer/attention intuition.
- Inference vs training.
- Temperature/top-p and deterministic output needs.
- Hallucination and uncertainty.
- Reasoning models vs general chat/instruction models.
- Closed vs open-weight models.
- Cost/latency/quality trade-offs.

## 1.4 Embeddings fundamentals

- Vector representations.
- Cosine similarity/dot product.
- Embedding dimensionality.
- Semantic similarity vs lexical similarity.
- Embedding model selection.

### 🧪 Additional Project Assignment — Smart Ticket Classifier API

Build a **FastAPI** service that classifies free-text support tickets into structured JSON fields such as category, priority, sentiment, and destination team using direct OpenAI/Anthropic SDK calls plus Pydantic validation. Add streaming, retry with exponential backoff, per-request token/cost logging, pytest coverage, and Docker packaging.

### 🧪 Project Assignment — Multi-Model Playground

Build a FastAPI service that calls at least two model providers, records latency/token usage/cost, validates responses with Pydantic, and exposes a common provider-neutral interface. Add pytest tests and Docker packaging.


---


---

# 🔌 Phase 2 — Direct Model APIs, Structured Outputs & Tool Calling

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 2.1 Learn direct SDKs before frameworks

- OpenAI SDK.
- Anthropic SDK.
- Gemini API awareness.
- Request/response lifecycle.
- System/developer/user instruction roles where supported.
- Streaming.
- Retries and backoff.
- Timeouts.
- Rate limits.
- Token accounting.
- Error taxonomy.

## 2.2 Structured generation

- JSON output.
- Schema-constrained generation.
- Pydantic models.
- Enum and nested schemas.
- Optional vs required fields.
- Validation and repair strategies.
- Structured outputs as an API contract.

## 2.3 Tool/function calling

- Tool definitions and schemas.
- Tool selection.
- Arguments.
- Parallel tool calls.
- Tool result messages.
- Multiple-turn tool loops.
- Tool error handling.
- Tool descriptions as routing signals.
- Idempotency for tools with side effects.

## 2.4 Provider abstraction

- When an internal abstraction is worthwhile.
- LiteLLM or equivalent gateway/abstraction concepts.
- Avoiding lowest-common-denominator abstractions.
- Model routing and fallback.

### 🧪 Project Assignment — Payment Dispute Assistant Core

Without LangChain or LangGraph, build a service that: - accepts a payment dispute, - returns structured classification, - calls customer/transaction mock tools, - handles tool failures, - streams progress, - logs token/cost/latency, - supports OpenAI and Anthropic behind the same application interface.


---


---

# 🧩 Phase 3 — Prompt Engineering, Context Engineering & Composition Patterns

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 3.1 Production prompt engineering

- Instruction hierarchy.
- Role/task/context/constraints/output contract.
- Few-shot prompting.
- Delimiters and XML-style structure.
- Prompt templates.
- Prompt versioning.
- Prompt-as-code.
- Regression tests.

## 3.2 Reasoning-aware prompting

- Do not depend on exposing hidden chain-of-thought.
- Request concise rationale/evidence when needed.
- Decomposition.
- Self-checks.
- Critique/revision.
- Model-native reasoning controls.

## 3.3 Prompt composition patterns

- Prompt chaining.
- Routing.
- Parallelization.
- Map-reduce style decomposition.
- Orchestrator-workers.
- Evaluator-optimizer.
- Planner-executor.
- Generator-critic.
- Reflection/retry.

## 3.4 Context engineering

- Context selection rather than context dumping.
- Static vs dynamic context.
- Retrieved context.
- Tool results.
- Conversation history.
- Summarization.
- Context compaction.
- Context isolation between agents.
- Token budgeting.
- Lost-in-the-middle risks.
- Relevance vs completeness.

### 🧪 Project Assignment — Prompt & Context Benchmark

Create 30 representative support/payment tasks. Implement at least four prompt/context strategies. Compare schema validity, task success, latency, tokens, and cost. Store prompts and evaluation cases in Git.


---


---

# 🤖 Phase 4 — Agent Internals & Reasoning/Workflow Patterns

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 4.1 Build the mental model

- Goal.
- Model.
- Instructions.
- Tools.
- State.
- Memory.
- Control loop.
- Stop conditions.
- Guardrails.
- Evaluation.

## 4.2 Core patterns

- ReAct.
- Plan-and-Execute.
- Routing.
- Parallel fan-out/fan-in.
- Orchestrator-workers.
- Evaluator-optimizer.
- Reflection/self-critique.
- Tree/search approaches: when worth the cost.
- Human-in-the-loop.

## 4.3 Control-loop engineering

- Maximum iterations.
- Termination criteria.
- Budget limits.
- Retry policy.
- Tool failures.
- Partial success.
- State transition validation.
- Deterministic vs model-selected routing.

## 4.4 Workflow vs agent

- Fixed DAG.
- State machine.
- Dynamic graph.
- Autonomous loop.
- Escalation to humans.
- Choosing minimum necessary autonomy.

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

- Repository-aware coding agent.
- CLI and IDE/VS Code usage.
- Interactive vs headless/scripted execution.
- Planning and review.
- Permission boundaries.
- Diff review.
- Session lifecycle.

## 5.2 Layered context system

Learn the responsibility and scope of: - global/user instructions, - project `CLAUDE.md`, - nested `CLAUDE.md`, - local/personal context where supported, - `.claude/rules/*.md`, - skills, - subagent definitions, - session/work notes. - `CLAUDE.local.md` for gitignored developer-local overrides where supported, such as local ports, seed data, or personal test shortcuts. Keep durable team rules out of this file.

## 5.3 `CLAUDE.md`

Include durable project-wide facts: - architecture, - build/test/run commands, - repository map, - coding conventions, - validation commands, - security boundaries, - architectural invariants, - explicit “do not” constraints.

Avoid: - task-specific prompts, - huge reference manuals, - secrets, - volatile session state, - instructions better enforced by hooks/tests.

## 5.4 Context hygiene

- Small durable context.
- Progressive disclosure.
- Localize rules.
- Avoid duplication.
- Single source of truth.
- Context drift.
- Instruction conflicts.

### 🧪 Project Assignment — Production Repository Bootstrap

Take an existing Java/Spring microservice repository and create a production-quality Claude Code context hierarchy. Ask Claude Code to implement one API feature and compare: 1. no repository instructions, 2. oversized monolithic instructions, 3. properly layered context.

Record errors, unnecessary changes, tokens, and review effort.


---


---

# 📚 Phase 6 — Retrieval Engineering: Loading, Splitting, Chunking & Basic RAG

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 6.1 Document ingestion

- PDF/HTML/Markdown/Office/document loaders.
- Parsing quality.
- Metadata extraction.
- Document normalization.
- Tables and structured content.
- OCR only when necessary.

## 6.2 Splitting and chunking

- Fixed-size.
- Recursive.
- Sentence/paragraph.
- Semantic.
- Heading/document-structure aware.
- Parent-child.
- Sliding/window approaches.
- Chunk overlap.
- Chunk size vs retrieval precision.
- Preserve provenance.

## 6.3 Vector storage

- PostgreSQL + pgvector.
- Qdrant.
- Pinecone awareness.
- Chroma for prototyping.
- Index design.
- Metadata filtering.
- Multi-tenancy and access control.

## 6.4 Basic RAG pipeline

`load → normalize → split → embed → index → retrieve → construct context → generate → cite`

- top-k.
- similarity thresholds.
- grounding.
- citations.
- abstention.
- retrieval failure modes.

## 6.5 LangChain/LlamaIndex ingestion layer

- Learn abstractions after implementing the pipeline once yourself.
- Loaders.
- Splitters.
- Embeddings.
- Vector stores.
- Retrievers.

### 🧪 Project Assignment — Regulation RAG v1

Ingest a corpus of payment/regulatory documents. Implement two chunking strategies and compare retrieval quality. Store vectors in pgvector, return source citations, enforce metadata filtering, and build a small retrieval evaluation dataset.


---


---

# 🕸️ Phase 7 — Advanced, Graph & Agentic RAG

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 7.1 Advanced retrieval

- Dense + sparse/BM25.
- Hybrid search.
- Reciprocal Rank Fusion.
- Cross-encoder re-ranking.
- Query expansion.
- Multi-query.
- HyDE.
- Query decomposition.
- Parent-document retrieval.
- Contextual retrieval.
- Metadata/security filtering.

## 7.2 Graph RAG

- Entity extraction.
- Relationship extraction.
- Knowledge graphs.
- Neo4j.
- Graph traversal.
- Multi-hop retrieval.
- Vector + graph hybrid.
- Corpus/global summarization approaches.

## 7.3 Agentic RAG

- Agent decides whether retrieval is necessary.
- Router selects corpus/tool.
- Retrieval grader.
- Query rewrite.
- Retry.
- Web/tool fallback.
- Corrective RAG.
- Self-RAG concepts.
- Multi-index routing.

## 7.4 RAG evaluation

- Faithfulness.
- Answer relevancy.
- Context precision.
- Context recall.
- Retrieval hit rate/MRR/nDCG awareness.
- RAGAS and alternative eval tooling.

### 🧪 Project Assignment — Regulation RAG v2

Upgrade Phase 6 to hybrid retrieval + re-ranking + agentic retrieval grading. Add a small Neo4j graph for regulation/article/obligation relationships. Produce before/after evaluation results and a failure-analysis report.

### 🧪 Additional Project Assignment — Regulatory Knowledge Assistant

Ingest PSD2/PCI-DSS-style payment-regulation documents using LangChain plus pgvector, add hybrid dense+BM25 retrieval, re-ranking, an agentic grade → rewrite → retry/fallback loop, and a small Neo4j entity graph for multi-hop questions. Evaluate retrieval and generation separately with RAGAS-style metrics.


---


---

# 🧠 Phase 8 — State, Memory & Long-Running Agent Context

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 8.1 Do not confuse context with memory

- Prompt/context window.
- Runtime state.
- Checkpoint state.
- Conversation memory.
- Long-term semantic memory.
- Episodic memory.
- User/profile memory.
- External source of truth.

## 8.2 Short-term memory

- Thread/session state.
- Message history.
- Summarization.
- Sliding history.
- Token-aware compaction.

## 8.3 Long-term memory

- Explicit writes.
- Semantic retrieval.
- Facts/preferences.
- Episodic records.
- Memory consolidation.
- TTL/retention.
- Conflict resolution.
- Forget/update semantics.

## 8.4 Durable execution

- Checkpointing.
- Resume after crash.
- Exactly-once illusion vs idempotency.
- Side-effect tracking.
- Replay.
- State versioning.

## 8.5 Memory security

- Tenant isolation.
- PII.
- Consent.
- Retention/deletion.
- Poisoning.
- Incorrect memories.
- Auditability.

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

- Graph only where state/control flow merits it.
- Deterministic edges where business policy is deterministic.
- Model routing only where semantic judgment is necessary.
- Explicit side-effect boundaries.
- Idempotent nodes.
- Failure/retry semantics.

### 🧪 Project Assignment — LangGraph Migration

Rebuild the framework-free Phase 4 agent using LangGraph. Add checkpointing, HITL, conditional routing and durable restart. Compare code complexity, control, observability, and failure recovery against the framework-free version.


---


---

# 🧰 Phase 10 — Claude Code Skills, Rules, Commands & Subagents

> 🟡 **Path:** `P1` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 10.1 Rules

- `.claude/rules/*.md`.
- Domain/directory-scoped conventions.
- Architecture rules.
- Testing rules.
- Security rules.
- Avoid repeating root project memory.

## 10.2 Skills

- `.claude/skills/<skill>/SKILL.md`.
- Frontmatter/metadata.
- Trigger-oriented descriptions.
- Progressive disclosure.
- Optional scripts/templates/reference material.
- Skill vs rule vs subagent vs MCP.
- Reusable domain expertise.

Example skill domains: - Kafka capacity review. - Spring Boot API review. - payment idempotency review. - threat modeling. - migration readiness. - ADR generation.

## 10.3 Commands

- Reusable explicit workflows.
- Parameterized task invocation.
- When a command should invoke a skill or subagent.
- Keep commands task-oriented rather than storing project knowledge.

## 10.4 Subagents

- `.claude/agents/*.md`.
- Role.
- Goal.
- Scope.
- Allowed tools.
- Inputs/outputs.
- Model choice.
- Context isolation.
- Reviewer/tester/security/architecture roles.
- Preventing role overlap.

## 10.5 Work/session notes

- Plans and session continuity.
- Decisions made.
- Remaining work.
- Verification status.
- Do not convert transient notes into permanent global instructions.

### 🧪 Project Assignment — Claude Code Engineering Toolkit

For the same Java service, build: - architecture rules, - API-review skill, - Kafka-review skill, - implementation command, - test subagent, - code-review subagent, - security subagent.

Run one feature through the toolkit and measure human review effort and defects found.


---


---

# 👥 Phase 11 — Multi-Agent Architecture & Vendor Agent SDKs

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 11.1 Multi-agent topologies

- Supervisor.
- Hierarchical.
- Router + specialists.
- Handoffs.
- Network/swarm concepts.
- Blackboard/shared-state patterns.
- Parallel specialists.

## 11.2 Context boundaries

- Give each agent only necessary context.
- Shared vs private state.
- Handoff contracts.
- Structured inter-agent messages.
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

- Host.
- Client.
- Server.
- Tools.
- Resources.
- Prompts.
- Capability negotiation.
- Local vs remote servers.
- stdio.
- Streamable HTTP.
- Sessions.

## 12.2 Build MCP servers

- Python official MCP SDK/FastMCP.
- TypeScript SDK awareness.
- Java/Spring AI MCP.
- Wrap REST APIs.
- Wrap RAG.
- Wrap databases safely.
- Long-running operations.
- Errors and structured results.

## 12.3 🔌 Consume MCP

From: - Claude Code. - Claude Agent SDK. - OpenAI agent tooling where supported. - LangGraph adapters. - custom clients.

## 12.4 🔐 MCP security

- Authentication/OAuth.
- Least privilege.
- Tool allowlists.
- Tool poisoning.
- Prompt injection through tool metadata/results.
- Confused deputy.
- Secret management.
- Egress controls.
- Audit logs.
- Approval for side effects.

## 12.5 MCP architecture

- One MCP server per domain capability rather than blindly per microservice.
- Gateway/aggregation when governance, discovery, auth or policy warrants it.
- Avoid exposing internal service topology directly to agents.
- Stable capability-oriented contracts.

## 12.6 MCP in both paths

**P1:** expands the coding agent’s external tool surface.  
**P2:** provides a protocol boundary between application agents and enterprise capabilities.

## 12.7 A2A and protocol boundaries

- Understand the conceptual split: **MCP = agent/client ↔ tools/resources**, while **A2A = agent ↔ agent** interoperability.
- Agent Cards/capability discovery.
- Tasks, messages, status and long-running task lifecycle concepts.
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

- Requirement interpretation.
- Repository reconnaissance.
- Impact analysis.
- Explicit plan.
- Files/components expected to change.
- Test strategy.
- Risk assessment.
- Human plan approval for non-trivial work.

## 13.2 Execution

- Delegate bounded work.
- Independent implementation/test/documentation tasks.
- Context isolation.
- Parallelization only when dependencies permit it.
- Preserve architectural invariants.

## 13.3 Verification

- Tests.
- Static analysis.
- security checks.
- reviewer subagent.
- architectural review.
- acceptance criteria.
- diff inspection.
- evidence, not “looks good.”

## 13.4 Specialized agents

- Planner.
- Implementer.
- Tester.
- Reviewer.
- Security reviewer.
- Performance reviewer.
- Migration reviewer.

## 13.5 Failure patterns

- Agents editing the same files.
- Unclear ownership.
- reviewers sharing implementation bias/context.
- excessive agent count.
- circular delegation.
- no deterministic verification.
- autonomous merge/deployment without policy controls.

### 🧪 Project Assignment — Multi-Agent Feature Delivery

Implement a realistic payment-refund feature using separate planning, implementation, test, security and review roles. Produce a final verification packet containing plan, diffs, test evidence, security findings and unresolved risks.


---


---

# 🛡️ Phase 14 — Harness Engineering: Hooks, Permissions, Sandboxes & Guardrails

> 🟡 **Path:** `P1` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 14.1 🪝 Hooks

- Pre-tool checks.
- Post-tool checks.
- session lifecycle hooks where available.
- Deterministic formatting.
- test execution.
- blocking forbidden writes.
- secret scanning.
- architecture checks.

## 14.2 🔐 Permissions

- Read vs write.
- Shell command policies.
- Network access.
- filesystem scope.
- allowed/denied tools.
- human approval boundaries.

## 14.3 📦 Sandboxing

- Container/devcontainer.
- disposable environments.
- restricted credentials.
- network egress policy.
- safe command execution.

## 14.4 Feedback loops

- Compile.
- Unit test.
- Integration test.
- lint.
- static analysis.
- architecture tests.
- security scan.
- evals for AI behavior.

## 14.5 Harness observability

- Agent action logs.
- tool-call logs.
- test outcomes.
- retry loops.
- failure classifications.
- cost/time where measurable.

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

- Package reusable skills.
- Subagents.
- commands.
- hooks.
- MCP servers/configuration.
- `.claude-plugin/plugin.json` or the current plugin manifest format.
- versioning.

## 15.2 Design for reuse

- Generic capability vs project-specific knowledge.
- Configuration.
- semantic versioning.
- backward compatibility.
- documentation.
- tests.
- secure defaults.

## 15.3 Organizational distribution

- Team standards.
- internal marketplace/catalog.
- approved MCP servers.
- centrally maintained security hooks.
- shared review agents.
- upgrade governance.

### 🧪 Project Assignment — Enterprise Engineering Plugin

Package the Phase 10 and 14 capabilities as a reusable internal plugin/toolkit for Spring Boot teams. Install it into a second repository without copying project-specific instructions.

### 🧪 Additional Project Assignment — Clean-Checkout Plugin Verification

Bundle the policy reviewer/test writer, at least one reusable skill, one hook, and an MCP capability into a single plugin/toolkit. Install it from a clean checkout and verify that the agents, MCP capability, hooks, and skill are discoverable without manual file copying.


---


---

# ☁️ Phase 16 — Cloud Agent Platforms & Deployment

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 16.1 AWS

- Amazon Bedrock model access.
- Knowledge Bases.
- Guardrails.
- Bedrock AgentCore capabilities such as Runtime, Gateway, Memory, Identity, code/browser tooling, and observability where appropriate.
- Strands Agents SDK awareness and comparison with LangGraph/vendor SDK approaches.
- Identity.
- memory.
- gateways/tools.
- observability.
- VPC/private networking.
- IAM.
- cost controls.

## 16.2 Microsoft/Azure

**Depth: Working**

- Microsoft Foundry / Foundry Agent Service.
- Microsoft Agent Framework awareness, including its relationship to prior AutoGen/Semantic Kernel ecosystems.
- Azure AI Search.
- Entra/enterprise agent identity and governance concepts.
- OpenTelemetry integration.

## 16.3 Google Cloud

**Depth: Aware/Working** - Vertex AI agent services. - ADK. - Gemini integration. - managed deployment.

## 16.4 Deployment patterns

- Containers.
- Kubernetes.
- Serverless.
- Long-running workers.
- SSE/WebSockets.
- queues/events.
- asynchronous jobs.
- session affinity/state externalization.

### 🧪 Project Assignment — Cloud Deployment

Deploy the fraud-triage system with managed identity, private enterprise tools, persisted state, guardrails and observability. Document scaling, failure domains and estimated cost drivers.

### 🧪 Additional Project Assignment — Deploy Fraud Triage to AWS AgentCore

Deploy the fraud-triage workflow using Bedrock/AgentCore capabilities: MCP-backed enterprise tools through a managed gateway where appropriate, managed identity, durable memory, Bedrock Guardrails, and CloudWatch/OpenTelemetry observability. Rebuild one small specialist with Strands Agents SDK and document the trade-offs.


---


---

# 📈 Phase 17 — AgentOps: Evals, Observability, Security & Reliability

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 17.1 🧪 Evaluation

- Golden datasets.
- Unit-style prompt/model tests.
- Structured-output validity.
- LLM-as-judge with calibration.
- Human review.
- A/B tests.
- regression suites.
- trajectory evaluation.
- tool-selection correctness.
- task completion.
- cost/latency budgets.

Tools to know: - LangSmith. - RAGAS. - DeepEval. - promptfoo. - Langfuse. - Arize Phoenix awareness.

## 17.2 🔭 Observability

- LLM spans.
- tool spans.
- retrieval spans.
- agent graph transitions.
- token/cost attribution.
- p50/p95/p99 latency.
- tool failure rates.
- retry counts.
- model fallback.
- OpenTelemetry GenAI conventions.

## 17.3 🛡️ Security

- OWASP Top 10 for LLM/GenAI applications as a threat-modeling baseline.
- Prompt injection.
- indirect prompt injection.
- insecure output handling.
- excessive agency.
- sensitive information disclosure.
- tool abuse.
- data exfiltration.
- poisoned retrieval.
- poisoned MCP tools.
- supply-chain risk.

## 17.4 ⚙️ Reliability

- Timeouts.
- circuit breakers.
- retry with jitter.
- rate limiting.
- bulkheads.
- idempotency.
- compensation.
- durable checkpoints.
- graceful degradation.
- model fallback.
- semantic caching where appropriate.

## 17.5 🏛️ Governance

- Prompt/model/version registry.
- evaluation gates.
- auditability.
- EU AI Act awareness, especially risk classification, transparency, human oversight and governance implications for European deployments.
- Guardrail framework awareness: NeMo Guardrails, Guardrails AI, and managed cloud/vendor guardrails.
- data residency.
- retention.
- human oversight.

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

- Unit tests for deterministic code.
- Contract tests for tools/MCP.
- Retrieval tests.
- prompt regression.
- agent trajectory tests.
- security/adversarial tests.
- end-to-end business tests.

## 18.3 CI/CD

- Build/test/lint.
- architecture checks.
- dependency scanning.
- prompt/eval regression.
- model change validation.
- deployment approval.
- canary model/prompt releases.

## 18.4 Code review with coding agents

- Agent-generated code is not exempt from normal review.
- Verify requirements and architectural fit.
- Security and dependency scrutiny.
- Detect plausible but nonexistent APIs.
- Require evidence for tests.
- Small reviewable diffs.
- Human accountability remains explicit.

## 18.5 Governance of coding-agent autonomy

Define autonomy levels: 1. read/explain, 2. propose plan, 3. edit with approval, 4. execute tests/tools, 5. open PR, 6. autonomous bounded workflow, 7. deployment/production action — heavily controlled.

### 🧪 Project Assignment — AI-Native Delivery Pipeline

Create a GitHub Actions pipeline that runs conventional tests plus AI evals, MCP contract tests, security checks and architecture tests. Use Claude Code to implement a change, but make the harness independently prove whether the change is acceptable.


---


---

# ☕ Phase 19 — Java/Spring Enterprise Agentic AI Track

> 🟢 **Path:** `P2` &nbsp;&nbsp;|&nbsp;&nbsp; 🎯 **Depth:** **Deep**


## 19.1 Spring AI

- Chat/model clients.
- structured outputs.
- tool calling.
- advisors.
- RAG.
- vector-store abstraction.
- MCP client/server.
- observability integration.

## 19.2 LangChain4j

- AI services.
- tools.
- RAG.
- memory.
- model providers.
- enterprise Java integration.

## 19.3 LangGraph4j / Java orchestration awareness

- Graph/state concepts in Java.
- When to keep orchestration in Python vs Java.
- Interoperability through HTTP/events/MCP.

## 19.4 Enterprise integration

- Existing Spring microservices.
- OAuth/OIDC.
- API gateway.
- Kafka.
- transaction boundaries.
- Resilience4j.
- OpenTelemetry.
- Kubernetes.
- secrets/IAM.

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

- Confirm Claude Code and credentials work before the session.
- Keep a minimal, reusable `CLAUDE.md` skeleton ready.
- Have a scratch repository initialized and complete one full test round-trip beforehand.
- Avoid spending assessment time debugging tooling setup.

## 21.2 During the assessment

- Restate the requirement and constraints.
- Sketch architecture before coding.
- Establish project context deliberately.
- Use planning mode for non-trivial work and explain why.
- Delegate only genuinely separable concerns to subagents.
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
