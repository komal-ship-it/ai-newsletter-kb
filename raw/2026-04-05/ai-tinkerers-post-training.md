# AI Tinkerers Post-Training — 2026-04-05

**Source:** post-training@mail.aitinkerers.org
**Subject:** Agent Version Control & Pipeline-Parallel LLMs (AI Tinkerers - Post-Training)
**Message ID:** 19d5c1a932679470

---

March 30, 2026 — Joe Heitzeberg, Founder at AI Tinkerers

Creating space for leading builders to share ideas, grow, and make an impact. This issue's selected demos showcase builders tackling core system challenges. Strong patterns in multi-agent orchestration, LLM inference, and developer tooling.

## Top 5 Picks (March 30)

**1. TOP PICK: The Midnight Duck: AI Growth** — Jerónimo Lopera Espinosa (CEO at Meritum Corps, AI Tinkerers - Valencia, Mar 17) presented how he used AI-driven content iteration to grow an Instagram community to 106k followers in 26 days. The demo showed a repeatable pipeline for ideation, rapid posting, and feedback loops. Tech stack: Sora 2, Gemini, ChatGPT, Vora.

**2. RUNNER UP: VLLM and Qdrant Benchmarking** — Bob Prendergast (Solution architect at HP, AI Tinkerers - Manchester New Hampshire, Mar 18) showed how VLLM and Qdrant power a local RAG-style stack, spinning up Docker containers for an LLM, an embedding model, and a vector database. Ran GPU-focused benchmarks comparing VLLM against sequential model runners. Tech stack: VLLM, Qdrant, IBM Granite, RAG, Docker.

**3. COMMUNITY FAVORITE: Version Control for Agentic Engineering** — Ellie Daw (Founder at gjalla, AI Tinkerers - Chicago, Mar 17) presented a new version control approach for agentic engineering, focused on tracking meaningful changes over time when coding agents generate huge volumes of diffs. The system groups and records the "kinds" of changes that matter, so regressions and intent don't get buried, using a guardrail-first workflow. Tech stack: LangChain, Claude Code, Codex, Gemini, gjalla.

**4. STANDOUT: OmniNode: Pipeline-Parallel LLM Inference** — Leonard Wang (Co-Founder at SUM INNOVATION INC, AI Tinkerers - Los Angeles, Mar 19) presented OmniNode Protocol, a live two-device demo that pipeline-parallelizes LLM inference across consumer Macs over a LAN using Rust, QUIC, and zero-copy GGUF sharding feeding directly into MLX. Built omni-net for mDNS discovery and encrypted QUIC streams, omni-store for memmapped tensor chunking and BLAKE3-CID addressing, and a PyO3 zero-copy bridge. Tech stack: Rust, libp2p, PyO3, MLX, GGUF.

**5. NOTABLE: Headshotify: AI Passport Photos** — Ethel Zhang (AI Researcher at Google, AI Tinkerers - New York City, Mar 18) presented an app that turns any uploaded portrait into passport-worthy headshots by automatically framing the face and optionally removing the background. Tech stack: TypeScript, Vite, Face Recognition AI, Background Removal AI, PayPal API.

## More Great Builds

- **Your Brand Translator** (Filipp Trigub, AI Tinkerers - Paris): open source WhatsApp-first agent that creates brand-consistent social posts and schedules them. Runs locally using Qwen 3.5 35B core plus image and video tooling with OpenClaw-based orchestration.
- **ModelWar: Core War for Agents** (PJ Gray, AI Tinkerers - New York): unique agent competition platform.
- **GitClaw** (Nelson PROIA): voice AI companion for GitHub.
- **Benchmarking SLMs with Polars** (Yassine Hadi): deep dive into performance tuning and comparison.
- **Metaphorex: Multi-Agent Knowledge Graph** (Frank Shotwell): multi-agent coordination for knowledge graphs.
