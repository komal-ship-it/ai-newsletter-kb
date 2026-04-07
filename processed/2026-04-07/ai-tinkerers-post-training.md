# AI Tinkerers Post-Training — 2026-04-07

**Source:** post-training@mail.aitinkerers.org
**Date:** 2026-04-07
**Original items:** 10

## Key Announcements
- **OpenClaw video editing skill** — Robin Guignard-Perret (tellers.ai) extended OpenClaw with a video editing skill that routes multi-step tasks, generates edit decisions, and exports FCPXML timelines.
- **OpenSymphony** — Rust implementation of OpenAI Symphony orchestration wired to OpenHands. Runs multi-agent coding workflows with Linear issue tracking, concurrent agent state cache, and REST/WebSocket adapters.
- **MCP Knowledge Graph Architecture Consultant** — Marcus Waldman (Denver) built an MCP server that turns the Agentic Architectural Patterns textbook into a knowledge graph with 138 concepts and hundreds of typed relationships. Runs architecture consultations inside Claude Code.

## Tools & Products
- **OpenClaw video editing skill** — Extends OpenClaw agent gateway with video editing workflows; outputs FCPXML. | Stack: OpenClaw, tellers.ai | Effort: weekend
- **OpenSymphony** — Multi-agent Rust orchestration framework on top of OpenHands + OpenAI Symphony design | Stack: Rust, Linear, FrankenTUI | Effort: major
- **Hive local-first AI gateway** — Orchestrates agents across Telegram, Discord, WhatsApp, and CLI using Bun/TypeScript | Effort: weekend
- **MiroFish** — Multi-agent swarm prediction using GraphRAG for grounded context | Effort: weekend
- **elluminate live** — Natural-language LLM guardrails that explain why simple allow/deny lists fail | Effort: quick-win
- **Canto Lyrics AI (cantolyrics.ai)** — Cantonese songwriting with Jyutping tonal alignment and MIDI | Effort: major

## Techniques & Methods
- **Playwright MCP vs CLI benchmarking** — Mikayla Thompson ran comparative tests on effectiveness and latency of Playwright MCP vs Playwright CLI in Claude Code + Playwright-driven agent workflows. CLI outperformed in some configurations.
- **Graph-enhanced ML features** — Neo4j graph topology features (PageRank, Louvain, Degree Centrality) computed via Neo4j GDS and written back as node properties improve XGBoost classifier results over flat tabular inputs.
- **MCP as knowledge graph layer** — MCP server connecting structured knowledge graph (concepts + typed relationships) to Claude Code for architecture consultation. Pattern reusable for any textbook/domain.

## Research Papers
- None today.

## Industry Trends
- Knowledge graphs + MCP becoming a pattern for injecting structured domain knowledge into Claude Code sessions
- Multi-agent orchestration frameworks (OpenSymphony, MiroFish) converging on graph-based context grounding
- Local-first AI gateways gaining traction as alternative to cloud-dependent agent platforms

## Actionable Items
- [ ] Test Marcus Waldman's MCP Knowledge Graph Architecture Consultant pattern inside Claude Code — adapt for your own domain — *weekend* | action-2026-04-07-004
- [ ] Benchmark Playwright MCP vs CLI for your own browser-testing agents following Mikayla Thompson's methodology — *weekend* | action-2026-04-07-005
- [ ] Review elluminate live's approach to natural-language LLM guardrails — quick read on why deny-lists fail — *quick-win* | action-2026-04-07-006

## Notable Links
- MCP Knowledge Graph Architecture Consultant (Marcus Waldman, AI Tinkerers Denver-Boulder)
- OpenSymphony repo (Leonardo González, Trilogy)
- Playwright MCP vs CLI benchmark (Mikayla Thompson, Ranger)
- elluminate live guardrails demo (Daniel Albensoeder, AI Tinkerers Bremen)
