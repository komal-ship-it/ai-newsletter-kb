# AI Collective — 2026-04-14

**Source:** aicollectivenewsletter@mail.beehiiv.com
**Date:** 2026-04-14
**Original items:** 11

## Key Announcements
- **Anthropic Project Glasswing / Mythos** — Restricted cybersecurity initiative; ~12 orgs given Mythos Preview access. Found thousands of zero-days: 27-year-old OpenBSD RCE, 17-year-old FreeBSD root access (CVE-2026-4747), 16-year-old FFmpeg codec flaws. Benchmarks: CyberGym 83.1% (vs Opus 4.6: 66.6%), SWE-bench Pro 77.8% (vs Opus 4.6: 53.4%). Priced $25/$125 per M input/output tokens. NOT releasing publicly; in red team testing generated 181 working Firefox exploits (vs Opus 4.6: 2), chained exploits into kernel privilege escalation for under $2,000/run.
- **Meta Muse Spark** — First model from Alexandr Wang's Superintelligence Labs (Meta invested $14.3B for 49% of Scale AI). Proprietary multimodal model; three modes: quick, advanced, Contemplating (parallel agent reasoning). Gaps: trails on long-horizon agentic and coding tasks. Meta stock +6.5%. 2026 AI capex: $115B–$135B.
- **Claude Managed Agents (public beta)** — Define autonomous agents via natural language or YAML; priced at $0.08/session-hour + token costs.
- **Perplexity ARR $450M** — "Computer" agent drove 50% revenue jump in a single month; 100M+ MAUs.
- **Google merges NotebookLM into Gemini app** — All users now get NotebookLM directly inside Gemini.
- **NVIDIA Isaac GR00T open models + Newton 1.0** — Open models for natural-language robot instruction; Newton 1.0 physics engine released for robotics week.
- **Neuro-symbolic AI energy reduction** — Researchers cut AI energy consumption up to 100x via neuro-symbolic approach.
- **OpenAI Safety Fellowship** — External researchers: $3,850/week + ~$15K/month in compute.
- **19 new AI bills signed into law** — Signed in late March; AI governance acceleration.
- **NVIDIA locks TSMC CoWoS packaging capacity** — Reserved majority of TSMC's advanced packaging; supply chain concentration risk.

## Tools & Products
- **Mythos model** — Frontier cybersecurity/coding model; restricted access via Claude API / Bedrock / Vertex AI / Microsoft Foundry | $25/$125 per M tokens | Effort: major
- **Claude Managed Agents** — Enterprise agent definition via NL or YAML | https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/ | $0.08/session-hour | Effort: weekend
- **Meta Muse Spark** — Multimodal AI with Contemplating mode (parallel agents for hard problems) | meta.ai | Effort: quick-win
- **NVIDIA Isaac GR00T** — Open models for natural-language robot instruction | https://blogs.nvidia.com/blog/national-robotics-week-2026/ | Effort: weekend

## Techniques & Methods
- **Parallel agent reasoning (Contemplating mode)** — Meta's Muse Spark spins up multiple AI agents in parallel for complex problems; productized multi-agent pattern
- **Deployment as safety test** — Anthropic's philosophy: deploy Mythos despite alignment risk, using real-world deployment as the definitive safety evaluation

## Research Papers
- **Neuro-symbolic AI energy reduction** — Up to 100x energy cut by combining neural and symbolic approaches | https://www.sciencedaily.com/releases/2026/04/260405003952.htm

## Industry Trends
- AI capability and alignment risk growing in lockstep — Mythos is simultaneously "best-aligned" and "greatest alignment risk"
- Meta abandoning open-source Llama strategy with Muse Spark; going proprietary for enterprise distribution and API revenue
- AI agent products driving step-change revenue growth: Perplexity +50% in one month from a single agent product
- Frontier model cybersecurity capabilities collapsing the exploit discovery cycle from months to minutes
- AI governance pace accelerating: 19 new state laws in late March
- NVIDIA supply chain concentration: CoWoS packaging lock-in creates hardware bottleneck risk

## Actionable Items
- [ ] Explore Claude Managed Agents beta for enterprise agent workflows — *weekend* — https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/ | action-2026-04-14-008
- [ ] Test Meta Muse Spark's Contemplating mode for complex multi-step reasoning tasks — *quick-win* — https://meta.ai | action-2026-04-14-009
- [ ] Read NVIDIA Isaac GR00T open robotics model release — *quick-win* — https://blogs.nvidia.com/blog/national-robotics-week-2026/ | action-2026-04-14-010
- [ ] Apply for OpenAI Safety Fellowship if doing AI safety research ($3,850/week + compute) — *major* — https://openai.com/index/introducing-openai-safety-fellowship/ | action-2026-04-14-011

## Notable Links
- https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/ — Claude Managed Agents beta
- https://www.pymnts.com/artificial-intelligence-2/2026/perplexitys-shift-to-ai-agents-boosts-revenue-50/ — Perplexity 50% revenue jump from Computer agent
- https://www.sciencedaily.com/releases/2026/04/260405003952.htm — Neuro-symbolic AI cuts energy 100x
- https://openai.com/index/introducing-openai-safety-fellowship/ — OpenAI Safety Fellowship
- https://blogs.nvidia.com/blog/national-robotics-week-2026/ — NVIDIA Isaac GR00T + Newton 1.0
- https://pluralpolicy.com/blog/the-ai-governance-watch-april-2026-nineteen-new-ai-bills-passed-into-law/ — 19 new AI laws signed
- https://newsletter.aicollective.com/p/what-anthropic-s-mythos-actually-tells-us-meta-bets-135b-on-muse — Full newsletter
