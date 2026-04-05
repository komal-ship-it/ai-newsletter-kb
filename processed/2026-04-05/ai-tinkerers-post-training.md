# AI Tinkerers Post-Training — 2026-04-05

**Source:** post-training@mail.aitinkerers.org
**Date:** 2026-04-05
**Original items:** 7 demos featured

## Key Announcements
- None today.

## Tools & Products
- **gjalla (Version Control for Agentic Engineering)** — Tracks meaningful change types rather than raw diffs in agentic coding workflows; guardrail-first approach to prevent regression burial. Tech: LangChain, Claude Code, Codex, Gemini. | No URL provided | Effort: weekend
- **OmniNode Protocol** — Pipeline-parallelizes LLM inference across consumer Macs over LAN via Rust + QUIC + zero-copy GGUF sharding into MLX. Built by Leonard Wang / SUM INNOVATION INC. | No URL provided | Effort: major
- **Headshotify** — Turns portrait photos into passport-quality headshots with auto-framing and background removal. Tech: TypeScript, Vite, PayPal API. Built by Ethel Zhang (Google AI Researcher). | No URL provided | Effort: weekend
- **Your Brand Translator** — Open-source WhatsApp-first agent for brand-consistent social post creation and scheduling. Runs locally on Qwen 3.5 35B with OpenClaw orchestration. Built by Filipp Trigub. | No URL provided | Effort: weekend
- **ModelWar: Core War for Agents** — Agent competition platform (Core War format). Built by PJ Gray. | No URL provided | Effort: weekend
- **GitClaw** — Voice AI companion for GitHub. Built by Nelson PROIA. | No URL provided | Effort: weekend

## Techniques & Methods
- **AI-driven content iteration for community growth** — Jerónimo Lopera used Sora 2 + Gemini + ChatGPT pipeline for rapid ideation and posting feedback loops; grew Instagram community to 106k followers in 26 days.
- **Pipeline-parallel LLM inference** — Split model layers across consumer devices using GGUF sharding + QUIC transport; enables running large models without data-center GPU access.
- **Guardrail-first agentic version control** — Group diffs by intent/type rather than line-by-line; surface regressions before they compound across long agent runs.
- **BLAKE3-CID content addressing for tensors** — OmniNode uses BLAKE3 content identifiers for memmapped tensor chunks, enabling efficient zero-copy distribution.
- **Local RAG benchmarking with VLLM + Qdrant** — Docker-based stack (LLM + embedding model + vector DB) for GPU-focused comparison against sequential runners.

## Research Papers
- None today.

## Industry Trends
- Multi-agent orchestration emerging as a primary engineering challenge — version control and coordination primitives now as important as the models themselves.
- Consumer-hardware LLM inference becoming viable — pipeline-parallel approaches let developers run models that previously required server GPUs.
- Agentic tooling ecosystem maturing: voice interfaces for dev tools (GitClaw), competition frameworks (ModelWar), and knowledge graph orchestration (Metaphorex).

## Actionable Items
- [ ] Evaluate gjalla for agentic version control: test diff-grouping approach on a Claude Code project to see if it reduces regression churn. — *weekend* — action-2026-04-05-004
- [ ] Prototype OmniNode-style pipeline-parallel inference on two local Macs if available — demonstrates $0 inference cost for mid-size models. — *major* — action-2026-04-05-005
- [ ] Review AI-driven social growth pipeline (Sora 2 + Gemini + ChatGPT) used by Lopera — adapt ideation → rapid post → feedback loop for content channels. — *weekend* — action-2026-04-05-006

## Notable Links
- None today.
