# AI Tinkerers Post-Training — Raw — 2026-04-07

**Message ID:** 19d6531d31acf601
**From:** post-training@mail.aitinkerers.org
**Subject:** ⚡ Tinkering at Scale: Agentic Orchestration, Knowledge Graphs & Creative AI Wins (AI Tinkerers - Post-Training)
**Date:** 2026-04-06T23:47:36Z

---

Tinkering at Scale: Agentic Orchestration, Knowledge Graphs & Creative AI Wins
April 06, 2026
Joe Heitzeberg • Founder at AI Tinkerers

Creating space for leading builders to share ideas, grow, and make an impact.

This week, we saw builders tackling complex systems with AI, from developer tooling to agent orchestration. Robin Guignard-Perret in Paris demonstrated how to add video editing capabilities to OpenClaw, while Mikayla Thompson in Denver explored performance trade-offs in Playwright's MCP vs CLI for testing agents. Several projects focused on orchestrating AI agents for specific tasks. Jenny Wong in Hong Kong built an AI Cantonese Lyric Generator for cultural preservation, and Leonardo González in Manizales showcased OpenSymphony for agentic engineering. Marcus Waldman in Denver even turned a textbook into an architecture consultant using a knowledge graph and AI agents with MCP. We also saw concrete applications of AI in specialized domains. Eliezer Zarpelao in São Paulo combined Neo4j and XGBoost for Fraud Detection, highlighting graph features' power. Meanwhile, Haoping Yang in Toronto presented Print Anything, enabling 3D printing from natural language descriptions.

Top 5 Picks (April 6)

1. TOP PICK: OpenClaw: AI Video Editing
Robin Guignard-Perret, CEO/CTO at tellers.ai — AI Tinkerers Paris, Mar 26
Robin showed how OpenClaw gets extended with a video-editing "skill" so builders can trigger editing workflows from the same chat-based agent gateway. The demo routes multi-step tasks, generates edit decisions and branded outputs like transcripts and edit notes, and exports industry-friendly timelines such as FCPXML.
Tech Stack: OpenClaw, tellers

2. RUNNER UP: AI Cantonese Lyric Generator
Jenny Wong — AI Tinkerers Hong Kong, Mar 26
Jenny presented the first Cantonese Lyrics AI in HK, where Cantolyrics.ai automates Cantonese songwriting using a custom ML workflow with Jyutping-based tonal to melodic alignment. Her Solfege-to-0243 tool turns MIDI input into Cantopop "0243" tones via relative-scale engines.
Tech Stack: LLM, Machine Learning, Audio-to-MIDI transcription, Jyutping, 0243 principle

3. COMMUNITY FAVORITE: Playwright: MCP vs CLI Benchmarking
Mikayla Thompson, Software Engineer at Ranger — AI Tinkerers Denver-Boulder, Mar 25
Mikayla benchmarks swapping a Playwright MCP setup with a CLI for browser-testing agents. Using her own Ranger-integrated agent workflow (Claude Code plus Playwright-driven automation), she runs comparative tests on both effectiveness and latency.
Tech Stack: Playwright MCP, Playwright CLI, Claude Code SDK, agent-browser

4. STANDOUT: OpenSymphony: Agentic Engineering Orchestration
Leonardo González, VP AI Center of Excellence at Trilogy — AI Tinkerers Manizales, Mar 25
Leonardo presented OpenSymphony, a Rust implementation of the OpenAI Symphony orchestration design, wired to an OpenHands agent server. OpenSymphony runs multi-agent coding workflows combining issue tracking via Linear, a scheduler-owned cache for concurrent agent state, and adapters like REST and WebSocket.
Tech Stack: OpenAI Symphony, OpenHands, Rust, Linear, FrankenTUI

5. NOTABLE: Neo4j and XGBoost Fraud Detection
Eliezer Zarpelao, Sr Solutions Engineer at Neo4j — AI Tinkerers São Paulo, Mar 26
Eliezer presented Graph-Enhanced XGBoost, where a Neo4j graph model of IEEE-CIS fraud data is built and graph-topology features computed in Neo4j GDS (PageRank, Louvain, Degree Centrality). Those scores get written back as node properties and used to train an XGBoost classifier, improving results over flat tabular inputs.
Tech Stack: Neo4j, Neo4j Graph Data Science (GDS), Cypher, Python, XGBoost

More Great Builds:
- elluminate live (Daniel Albensoeder, AI Tinkerers Bremen): Enforces natural-language guardrails for LLMs and explains why simple allow/deny lists get bypassed.
- Reachy: Voice and Vision Robot (Damien Soichet, AI Tinkerers Montreal): Voice and vision AI robot that sees, speaks, remembers, and reasons through graph-based orchestration using Databricks.
- Hive: Local-First AI Gateway (John Alexander Paez Arias, AI Tinkerers Pereira): Local-first AI agent gateway running on Bun and TypeScript, orchestrating agents across Telegram, Discord, WhatsApp, and CLI.
- MiroFish: Multi-agent swarm prediction (Jaime Restrepo, AI Tinkerers Manizales): Multi-agent swarm prediction demo using GraphRAG to ground agents in retrieved context.
- MCP: Knowledge Graph Architecture Consultant (Marcus Waldman, AI Tinkerers Denver-Boulder): MCP server turning Agentic Architectural Patterns into a knowledge graph, running structured architecture consultations inside Claude Code. Extracts 138 concepts and hundreds of typed relationships.
- Loupe: GTM with Claude Code (Jimmy Gambier, AI Tinkerers Seattle): One-person watch market intelligence platform shipping full GTM content using Claude Code.
