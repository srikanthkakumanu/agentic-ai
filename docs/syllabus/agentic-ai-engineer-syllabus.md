<div align="center">

# 🧭 Agentic AI Engineer
### Phased Course Syllabus — July 2026 Edition

![Duration](https://img.shields.io/badge/duration-18--20%20weeks%20part--time-4FD8E8?style=flat-square)
![Phases](https://img.shields.io/badge/phases-8-9D8CFF?style=flat-square)
![Track](https://img.shields.io/badge/track-Python%20first%20%2B%20Java%20native-FFB454?style=flat-square)
![Level](https://img.shields.io/badge/level-senior%20%2F%2018%2B%20yrs-F27FBE?style=flat-square)

</div>

<br>

> **Designed for:** a senior engineer with 18+ years in Java, REST APIs, production microservices, CI/CD, SCEA, and AWS SA Professional certification.
>
> **Goal:** transition into an **Agentic AI Developer / Engineer** role via a path that leverages your existing architecture, distributed-systems, and cloud strengths — rather than starting over.

<br>

## 📋 Table of Contents

| | | |
|---|---|---|
| [🔎 0 · Job Market Snapshot](#-0--job-market-snapshot) | [🐍 1 · Python + LLM Fundamentals](#-phase-1--foundations-python--llm-fundamentals) | [🧩 2 · Reasoning Patterns](#-phase-2--prompting--agentic-reasoning-patterns) |
| [📚 3 · RAG (Basic→Agentic)](#-phase-3--rag-basic--advanced--graph--agentic) | [🕸️ 4 · Agent Frameworks](#-phase-4--agent-frameworks--multi-agent-orchestration) | [🔌 5 · MCP & A2A](#-phase-5--mcp--a2a-the-agent-protocol-layer) |
| [☁️ 6 · Cloud Platforms](#-phase-6--cloud-based-agentic-ai-platforms) | [🛡️ 7 · AgentOps](#-phase-7--agentops-evaluation-observability-security--production) | [🏆 8 · Java Track + Capstone](#-phase-8--java-native-track--capstone-portfolio) |
| [✅ Tools Checklist](#-complete-tools--frameworks-checklist) | | |

<br>

---

## 🔎 0 · Job Market Snapshot
##### *Why this syllabus is shaped this way*

<table>
<tr><td width="33%" align="center"><b>+280%</b><br><sub>YoY growth in agentic-AI skill mentions<br>— Stanford AI Index 2026</sub></td>
<td width="33%" align="center"><b>#1</b><br><sub>"AI Engineer" — LinkedIn's fastest-growing<br>US job title, 2026</sub></td>
<td width="33%" align="center"><b>~90,000</b><br><sub>US job postings citing<br>agentic-AI skills</sub></td></tr>
</table>

- Agentic AI is the fastest-growing skill cluster in tech hiring, while traditional programmer roles contracted.
- The market rewards **production-grade skills, not demos**: hiring managers screen for orchestration, evaluation (evals), guardrails, observability, and reliability — not just prompt familiarity.
- **What employers actually list, in order of frequency:** Python → LangGraph/LangChain → RAG (vector DBs, hybrid search, Graph RAG) → MCP → one vendor Agent SDK (OpenAI / Claude / Google ADK) → a cloud agent platform (AWS Bedrock AgentCore or Azure/Microsoft Foundry) → evals & observability (LangSmith / Langfuse / RAGAS) → agent security.
- **🎯 Your advantage:** ~70% of an agentic system is classic distributed-systems engineering — state machines, sagas, retries, idempotency, event streaming, observability. You already know this. The syllabus front-loads only what is genuinely new (LLM behavior, prompting patterns, RAG, agent frameworks, protocols) and maps everything else onto what you know.
- **☕ Java note:** the market is Python-first, so Python is mandatory. However, **Spring AI, LangChain4j, and LangGraph4j** are now production-grade and increasingly demanded in enterprise banking/fintech job posts — a differentiator for you. A Java-native track is included in Phase 8.

<br>

---

## 🐍 Phase 1 — Foundations: Python + LLM Fundamentals
![Duration](https://img.shields.io/badge/duration-2--3%20weeks-4FD8E8?style=flat-square)

### 1.1 · Python for Senior Java Engineers
- Python 3.12/3.13 syntax fast-track: type hints, dataclasses, `async/await`, context managers, decorators — mapped to Java generics, records, `CompletableFuture`, try-with-resources, annotations
- Modern tooling: **uv** (package/env manager — 2026 standard, replaces pip/poetry) · **ruff** (lint/format) · **pytest**
- **Pydantic v2** — data validation & schemas; the backbone of structured LLM outputs *(think Bean Validation + Jackson combined)*
- **FastAPI `0.11x`** — async REST APIs; you'll wrap every agent you build in a FastAPI service

### 1.2 · LLM Fundamentals *(concepts, not math)*
- Transformer intuition: tokens, context windows, attention, temperature/top-p, why LLMs hallucinate
- The 2026 model landscape: **OpenAI GPT-5.x** · **Claude Opus 4.8 / Sonnet 4.6 / Haiku 4.5** · **Gemini 2.5/3** · open-weight (**Llama 4, Mistral, Qwen 3**) — cost/latency/capability trade-offs
- Calling LLM APIs directly: **OpenAI SDK**, **Anthropic SDK** — streaming, retries, rate limits, token counting, cost estimation
- **Structured outputs** — JSON mode, schema-constrained generation with Pydantic; *the single most important production skill*
- Embeddings: cosine similarity, embedding models (`text-embedding-3-large`, Cohere embed v4, open-source BGE/E5)
- Local model serving basics with **Ollama** (cheap experimentation)

> #### 📌 Phase 1 Assignment — *"Smart Ticket Classifier API"*
> Build a **FastAPI** service that accepts free-text support tickets and returns a structured JSON classification (category, priority, sentiment, suggested team) using the **Anthropic or OpenAI SDK** with **Pydantic**-validated structured output. Add streaming responses, retry logic with exponential backoff, and per-request token/cost logging. Containerize with **Docker**.
>
> **✅ Covers:** Python · FastAPI · Pydantic · direct LLM API usage · structured outputs · production hygiene

<br>

---

## 🧩 Phase 2 — Prompting & Agentic Reasoning Patterns
![Duration](https://img.shields.io/badge/duration-2%20weeks-58C0FF?style=flat-square)

### 2.1 · Prompt Engineering *(production-grade)*
- System vs. user prompts, few-shot examples, delimiters/XML tags, output constraints
- Prompt templates, versioning, prompt-as-code — store prompts in git, test them like code
- **Context engineering** *(the 2026 evolution of prompt engineering)* — what goes in the window, what gets retrieved, what gets summarized

### 2.2 · Reasoning Patterns *(know when to use each — interviewers ask this)*
| Pattern | What it does |
|---|---|
| **CoT** *(Chain-of-Thought)* | Step-by-step reasoning; native "thinking" models (GPT-5 thinking, Claude extended thinking) have absorbed manual CoT |
| **ReAct** *(Reason + Act)* | The foundational agent loop: thought → action (tool call) → observation → repeat. Every framework implements this |
| **ToT** *(Tree-of-Thoughts)* | Branching exploration for search-type problems; when it's worth the cost |
| **Reflexion / Self-critique** | Agent evaluates and retries its own output |
| **Plan-and-Execute** | Planner produces a task list, executor works it — contrast with pure ReAct |
| **Self-consistency** | Sample multiple reasoning paths, vote |
| **Tool / function calling** | How models emit tool calls, parallel tool calls, tool schemas — the bridge from "chatbot" to "agent" |

### 2.3 · What an "Agent" Actually Is
- Agent = LLM + tools + memory + loop + goal. Workflow vs. agent — Anthropic's *"Building Effective Agents"* taxonomy: prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer
- Autonomy spectrum and when **not** to build an agent *(a deterministic workflow is often the right answer — a strong interview talking point)*

> #### 📌 Phase 2 Assignment — *"ReAct Research Agent from Scratch (no framework)"*
> Build a ReAct agent in **pure Python** (only the OpenAI/Anthropic SDK) with 3 tools: a calculator, a web search (Tavily API), and a file writer. Implement the thought/action/observation loop, tool-call parsing, max-iteration guard, and a Reflexion step that critiques the final answer and retries once if quality is low. Log every step.
>
> **✅ Covers:** ReAct · CoT · Reflexion · tool calling · agent-loop internals — *building it framework-free is the best interview preparation you can do*

<br>

---

## 📚 Phase 3 — RAG: Basic → Advanced → Graph → Agentic
![Duration](https://img.shields.io/badge/duration-3%20weeks-7FA4FF?style=flat-square)

### 3.1 · Basic (Naive) RAG
- Pipeline: load → chunk → embed → store → retrieve (top-k) → generate
- Chunking strategies: fixed, recursive, semantic, document-structure-aware
- Vector databases: **pgvector `0.8.x`** on PostgreSQL *(enterprise default — leverage your SQL skills)* · **Qdrant `1.x`** · **Chroma** *(prototyping)* · managed options (**Pinecone**)
- **Frameworks:** **LangChain `1.x`** (loaders/splitters/retrievers) or **LlamaIndex `0.14.x`** (the ingestion/indexing specialist) — learn LangChain first; know LlamaIndex for complex document ingestion

### 3.2 · Advanced RAG
- Hybrid search: dense vectors + **BM25** keyword search, Reciprocal Rank Fusion
- **Re-ranking** with cross-encoders (**Cohere Rerank `3.5`**, open-source BGE-reranker)
- Query transformation: **HyDE** (hypothetical document embeddings), multi-query expansion, query routing
- Parent-document / sentence-window retrieval, contextual retrieval (Anthropic's contextual embeddings technique)
- Metadata filtering and access-control-aware retrieval *(critical in fintech/regulated domains — your niche)*
- **RAG evaluation with RAGAS `0.3.x`**: faithfulness, answer relevancy, context precision/recall — *non-negotiable in 2026 interviews*

### 3.3 · Graph RAG
- When vector RAG fails: multi-hop questions, entity relationships, "global" summarization questions
- **Frameworks:** **Neo4j `5.x`** + `neo4j-graphrag` (entity/relationship extraction, Cypher-based retrieval) for enterprise knowledge graphs; **Microsoft GraphRAG `2.x`** (community detection + hierarchical summarization) for corpus-wide "global questions"
- Hybrid pattern: vector search for entry points + graph traversal for context expansion

### 3.4 · Agentic RAG
- The retrieval pipeline becomes an agent: decides *whether* to retrieve, *which* index/tool to query, grades retrieved docs, rewrites the query, loops until confident
- Patterns: **Corrective RAG (CRAG)** · **Self-RAG** · router-based multi-index RAG
- **Framework:** **LangGraph `1.2.x`** — model the flow as a state graph with conditional edges (retrieve → grade → rewrite → generate). *This is the standard Agentic RAG stack in job postings.*

> #### 📌 Phase 3 Assignment — *"Regulatory Knowledge Assistant (Agentic RAG)"*
> Ingest payment-regulation PDFs (e.g., PSD2/PCI-DSS — your fintech domain) with **LangChain + pgvector**: hybrid search (BM25 + vectors) with **Cohere re-ranking**. Wrap it in a **LangGraph** agentic loop: grade retrieved chunks, rewrite weak queries, fall back to web search if the corpus lacks the answer. Add a small **Neo4j** entity graph (regulations → articles → obligations) for multi-hop questions. Evaluate with **RAGAS** and report faithfulness before/after re-ranking.
>
> **✅ Covers:** basic RAG · hybrid search · re-ranking · HyDE-style rewriting · Graph RAG · Agentic RAG · RAG evals

<br>

---

## 🕸️ Phase 4 — Agent Frameworks & Multi-Agent Orchestration
![Duration](https://img.shields.io/badge/duration-3%20weeks-9D8CFF?style=flat-square)

### 4.1 · LangGraph `1.2.x` *(primary framework — deepest job demand)*
- StateGraph: typed state, nodes, edges, conditional routing, cycles
- `create_agent()` prebuilt, middleware (LangChain 1.0 concept), typed streaming
- **Durable execution & checkpointers** (SQLite/Postgres savers) — resume after crash; maps directly to your saga/workflow experience
- **Human-in-the-loop (HITL)**: interrupts, approval gates, time-travel/replay
- Memory: short-term (thread state) vs. long-term (store API); conversation summarization
- Multi-agent architectures: **supervisor** · **hierarchical teams** · **swarm/handoffs** · network

### 4.2 · Vendor Agent SDKs *(know all three; go deep on one)*
| SDK | Positioning | Your depth |
|---|---|---|
| **OpenAI Agents SDK** `0.1x` | Agents, Handoffs, three-tier Guardrails, Sessions, sandboxed execution, built-in tracing — lightweight, model-agnostic, fastest-growing in postings | Deep |
| **Claude Agent SDK** `0.1.x` | "Give the agent a computer" paradigm: subagents, lifecycle hooks, filesystem/OS tools, deepest **MCP** integration; powers Claude Code | Deep |
| **Google ADK** `2.0` | Code-first, multi-language (Python/**Java**/Go/TS), graph workflows + collaborative agent teams, native **A2A**; its Java support is a differentiator for you | Working |
| **CrewAI** `1.x` | Role-based crews (role/goal/backstory), Flows for deterministic orchestration; rapid business-process automation | Aware |
| **Pydantic AI** `1.x` | Type-safe, minimal agent framework, growing fast | Aware |

### 4.3 · Agent Design Patterns *(cross-framework)*
- Orchestrator-workers, evaluator-optimizer, router, parallelization (fan-out/fan-in)
- Saga-style compensation for agent actions with side effects *(directly reuses your microservices patterns)*
- Context management at scale: summarization, scratchpads, sub-agent context isolation

> #### 📌 Phase 4 Assignment — *"Multi-Agent Fraud Triage System"*
> Build a **LangGraph supervisor** system with three specialists: a *transaction-analysis agent* (mock transaction API + rules engine), a *customer-history agent* (RAG over the Phase 3 stack), and a *report-writer agent*. Add a **human-in-the-loop interrupt** before any "block account" action, with **Postgres checkpointing** so the workflow survives restarts. Rebuild a simplified 2-agent version with the **OpenAI Agents SDK** (handoffs + guardrails) and write a one-page comparison.
>
> **✅ Covers:** LangGraph state/HITL/durability · supervisor pattern · vendor SDK hands-on · framework trade-off reasoning

<br>

---

## 🔌 Phase 5 — MCP & A2A: The Agent Protocol Layer
![Duration](https://img.shields.io/badge/duration-2%20weeks-C77FF2?style=flat-square)

### 5.1 · MCP — Model Context Protocol *(spec rev. 2025-11-25; Linux Foundation-governed)*
- Architecture: hosts, clients, servers; primitives — **tools, resources, prompts**; client capabilities — sampling, elicitation, progress
- Transports: stdio (local) and **Streamable HTTP** (remote/production); stateless vs. stateful sessions
- **OAuth 2.1 authorization** for remote MCP servers — enterprise security is where senior engineers stand out
- **Frameworks to build MCP solutions with:**
  - 🐍 **Python** → official **MCP Python SDK `1.x`** and **FastMCP `2.x`** *(the productivity standard — decorators, auth, deployment helpers)*
  - 📘 **TypeScript** → official MCP TypeScript SDK
  - ☕ **Java** → **MCP Java SDK / Spring AI MCP** (`Spring AI 1.1.x`) — build MCP servers as Spring Boot apps. *Your Java superpower applies directly here.*
  - Consuming MCP: Claude Agent SDK (native) · LangGraph via `langchain-mcp-adapters` · OpenAI Agents SDK (native)
- MCP security: prompt injection via tool descriptions, tool poisoning, confused-deputy problems, allowlisting

### 5.2 · A2A — Agent-to-Agent Protocol *(Linux Foundation; ACP merged into A2A in 2026)*
- Agent Cards (capability discovery), tasks, messages, artifacts; long-running task lifecycle
- **MCP = agent↔tool** · **A2A = agent↔agent** *(cross-team, cross-vendor)*
- Build with: **a2a-python SDK**; native support in **Google ADK** and **CrewAI**

> #### 📌 Phase 5 Assignment — *"Enterprise MCP Gateway"*
> Build two MCP servers: **(1)** a **FastMCP `2.x`** Python server exposing your Phase 3 RAG pipeline as tools (`search_regulations`, `get_entity_graph`); **(2)** a **Spring AI MCP** Java server wrapping a mock core-banking REST API with OAuth-protected Streamable HTTP. Connect both to **Claude Desktop/Claude Code** and to your Phase 4 LangGraph agent via `langchain-mcp-adapters`. Bonus: expose the fraud-triage supervisor as an **A2A** agent with an Agent Card.
>
> **✅ Covers:** MCP servers in Python & Java · transports · auth · MCP clients across frameworks · A2A basics

<br>

---

## ☁️ Phase 6 — Cloud-Based Agentic AI Platforms
![Duration](https://img.shields.io/badge/duration-3%20weeks-F27FBE?style=flat-square)

### 6.1 · AWS *(primary — matches your AWS SA-Pro certification)*
- **Amazon Bedrock**: model access, Converse API, Knowledge Bases (managed RAG), **Bedrock Guardrails**
- **Amazon Bedrock AgentCore** *(GA)* — the managed agent runtime:
  - **Runtime** (serverless, session-isolated microVMs, 8-hour sessions) · **Gateway** (APIs/Lambdas → MCP tools) · **Memory** (short/long-term) · **Identity** (OAuth) · **Code Interpreter** · **Browser** · **Observability** (CloudWatch/OTel) · Web Search tool
  - Framework-agnostic: deploy LangGraph, CrewAI, or Strands agents; host MCP servers on it
- **Strands Agents SDK `1.x`** — AWS's open-source, model-driven agent framework; the idiomatic AgentCore pairing
- Architecture depth: VPC/private connectivity, IAM for agents, cost controls — senior-level differentiators

### 6.2 · Azure / Microsoft *(secondary — highest enterprise demand in Europe)*
- **Microsoft Foundry** *(formerly Azure AI Foundry)*: model catalog, **Foundry Agent Service** (Azure AI Search, code interpreter, **MCP server endpoints**, Foundry Toolbox)
- **Microsoft Agent Framework `1.0`** *(GA April 2026; the AutoGen + Semantic Kernel merger)* — Python and .NET; workflows, agent teams, built-in OpenTelemetry
- **Agent 365 / Entra Agent ID** governance model *(conceptual)* — a strong Director-level talking point

### 6.3 · Google Cloud *(awareness level)*
- **Vertex AI Agent Engine / Agent Builder** + **ADK `2.0`** deployment; Gemini models — one conceptual walkthrough is sufficient unless targeting GCP shops

> #### 📌 Phase 6 Assignment — *"Deploy the Fraud Triage System to AWS AgentCore"*
> Deploy your Phase 4 system on **Bedrock AgentCore Runtime**: banking API → MCP tools via **Gateway**, memory → **AgentCore Memory**, OAuth via **Identity**, **Bedrock Guardrails** (PII masking + prompt-injection filtering), tracing → CloudWatch via **Observability**. Rebuild one specialist agent in **Strands Agents SDK** to compare developer experience. Write a short architecture doc with cost model and scaling assumptions.
>
> **✅ Covers:** AgentCore end-to-end · Strands · managed guardrails · cloud-native agent architecture

<br>

---

## 🛡️ Phase 7 — AgentOps: Evaluation, Observability, Security & Production
![Duration](https://img.shields.io/badge/duration-2--3%20weeks-FF8F70?style=flat-square)

### 7.1 · Evaluation *(the #1 skill gap employers cite)*
- Eval types: unit-style prompt tests, LLM-as-judge, human review, regression suites, A/B testing
- Agent-specific: **trajectory evaluation** (right tools, right order?), task-completion rate, cost/latency budgets
- Tools: **LangSmith** (datasets, experiments, online evals) · **RAGAS `0.3.x`** (RAG metrics) · **DeepEval / promptfoo** (CI-friendly runners)
- Evals in CI/CD: gate deployments on eval scores — maps onto your existing GitHub Actions expertise

### 7.2 · Observability
- Tracing agent runs: spans for LLM calls, tool calls, retrievals; token/cost attribution per user/session
- **OpenTelemetry GenAI semantic conventions** *(vendor-neutral standard)* + **LangSmith** or **Langfuse `3.x`** *(self-hostable, popular in EU/regulated firms)* or **Arize Phoenix**
- Production monitoring: drift, failure-mode dashboards, alerting on tool-error rates

### 7.3 · Security & Guardrails
- **OWASP Top 10 for LLM Applications (2025)**: prompt injection, insecure output handling, excessive agency, data exfiltration
- Defense-in-depth: **NeMo Guardrails** · **Guardrails AI** · Bedrock Guardrails · OpenAI Agents SDK guardrails; least-privilege tools, sandboxed execution, HITL for irreversible actions
- **EU AI Act** awareness (transparency/risk tiers) — highly relevant to your Amsterdam/London/Berlin targets

### 7.4 · Production Engineering for Agents
- Deployment: containerized agents on **Kubernetes**, serverless (AgentCore/Lambda), streaming over SSE/WebSockets
- Reliability: timeouts, circuit breakers, idempotent tools, compensation/rollback (sagas), semantic caching
- Versioning: prompts, models, and eval datasets as versioned artifacts; canary rollouts of model upgrades

> #### 📌 Phase 7 Assignment — *"Harden and Ship"*
> Make the fraud-triage system production-grade: build a **LangSmith** eval dataset of 30 test cases (5 prompt-injection attacks + 5 tool-failure scenarios); add **trajectory evals** gating **GitHub Actions**; instrument with **OpenTelemetry GenAI conventions** exporting to **Langfuse**; add **NeMo Guardrails** input rails. Produce a dashboard for cost-per-triage, p95 latency, and eval-score trend. Publish "what broke, what I measured, what I fixed."
>
> **✅ Covers:** evals · LLM-as-judge · CI/CD gating · OTel tracing · guardrails · security testing

<br>

---

## 🏆 Phase 8 — Java-Native Track + Capstone Portfolio
![Duration](https://img.shields.io/badge/duration-2--3%20weeks%20·%20parallel--friendly-FFB454?style=flat-square)

### 8.1 · Java/Spring Agentic Stack *(your differentiator in enterprise hiring)*
- **Spring AI `1.1.x`** — ChatClient, tool calling, RAG advisors, vector-store abstraction, **MCP client & server starters**; the Spring Boot-native way to build agents
- **LangChain4j `1.x`** — AiServices, tools, RAG; framework-agnostic Java option
- **LangGraph4j `1.8.x`** — LangGraph's graph model in Java (works with Spring AI or LangChain4j)
- **Positioning:** *"I can bring agentic AI into an existing Java/Spring estate without a Python rewrite"* — a rare, valuable pitch for banks and payment companies

### 8.2 · Capstone *(pick ONE, build deep, publish on GitHub with a demo video)*
| Option | What it does |
|---|---|
| **A · Agentic Payment-Operations Copilot** | Multi-agent (LangGraph) failed-payment investigator: **Spring AI MCP** data server, Agentic RAG for regulations, human-approved refunds, deployed on **AgentCore**, fully eval-gated |
| **B · Engineering-Intelligence Agent** | Ingests repos/CI via GitHub MCP + a custom DORA-metrics MCP server; answers "why did deployment frequency drop?" — plays to your engineering-leadership narrative |

### 8.3 · Interview & Positioning Prep
- System-design drills: *"Design a customer-support agent platform for 10M users"* (retrieval, orchestration, evals, guardrails, cost)
- Trade-off narratives: LangGraph vs. vendor SDKs · workflow vs. agent · vector vs. graph RAG · build vs. AgentCore-managed
- Portfolio: 3 pinned GitHub repos (Phases 3, 5/6, capstone), each with architecture diagram, eval results, and a 3-minute demo video

> #### 📌 Capstone Deliverable — *One production-grade system, publicly shipped*
> The eight assignments compound into a single portfolio system: RAG stack → multi-agent supervisor → MCP-wrapped → cloud-deployed → eval-gated. Finish with **one substantial system**, not eight toy projects.
>
> **✅ Covers:** full-stack synthesis · Java track · portfolio · interview narratives

<br>

---

## ✅ Complete Tools & Frameworks Checklist
##### *What you will have learned*

| Category | Tools / Frameworks (version) | Depth |
|---|---|:---:|
| 🐍 Language & core | Python 3.13, uv, Pydantic v2, FastAPI 0.11x | 🟢 Deep |
| 🔗 LLM APIs | OpenAI SDK, Anthropic SDK, Gemini API; Ollama (local) | 🟢 Deep |
| 🧩 Reasoning patterns | CoT, ReAct, ToT, Reflexion, Plan-and-Execute, Self-consistency | 🟢 Deep |
| 🕸️ Orchestration | **LangGraph 1.2.x**, LangChain 1.x | 🟢 Deep |
| 🤖 Vendor Agent SDKs | **OpenAI Agents SDK 0.1x**, **Claude Agent SDK 0.1.x**, Google ADK 2.0; CrewAI 1.x, Pydantic AI 1.x | 🟢🟡⚪ Mixed |
| 📚 RAG | pgvector 0.8, Qdrant 1.x, Chroma, LlamaIndex 0.14.x, BM25 hybrid, Cohere Rerank 3.5, HyDE, Contextual Retrieval | 🟢 Deep |
| 🕸️ Graph RAG | Neo4j 5.x + neo4j-graphrag, Microsoft GraphRAG 2.x | 🟡 Working |
| 🔁 Agentic RAG | CRAG / Self-RAG on LangGraph | 🟢 Deep |
| 🔌 Protocols | **MCP (spec 2025-11-25)** — MCP Python SDK 1.x, FastMCP 2.x, Spring AI MCP; **A2A** (a2a-python, ADK) | 🟢🟡 Mixed |
| ☁️ AWS | Bedrock, **AgentCore** (Runtime, Gateway, Memory, Identity, Observability), Strands Agents 1.x, Bedrock Guardrails | 🟢 Deep |
| ☁️ Azure | Microsoft Foundry, Foundry Agent Service, **Microsoft Agent Framework 1.0** | 🟡 Working |
| ☁️ GCP | Vertex AI Agent Engine, ADK deployment | ⚪ Aware |
| 📊 Evals | LangSmith, RAGAS 0.3.x, DeepEval / promptfoo | 🟢 Deep |
| 📡 Observability | OpenTelemetry GenAI conventions, Langfuse 3.x, Arize Phoenix | 🟡 Working |
| 🛡️ Guardrails & security | NeMo Guardrails, Guardrails AI, OWASP LLM Top 10, EU AI Act awareness | 🟡 Working |
| ☕ Java track | Spring AI 1.1.x, LangChain4j 1.x, LangGraph4j 1.8.x | 🟡🟢 Working–Deep |
| 🚀 Delivery | Docker, Kubernetes, GitHub Actions (eval-gated CI/CD) | 🟢 Already expert |

<sub>🟢 Deep — build & defend in interviews &nbsp;·&nbsp; 🟡 Working — built at least once &nbsp;·&nbsp; ⚪ Aware — can compare & discuss</sub>

<br>

<div align="center">

**⏱ Total duration:** ~18–20 weeks part-time (10–12 hrs/week) or ~10–12 weeks intensive

> 💡 **Sequencing rule:** never skip the assignment — in the 2026 market, **one shipped, evaluated, instrumented agent on GitHub outweighs every certificate.**

</div>
