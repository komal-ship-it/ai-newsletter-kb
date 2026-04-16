# AI Collective — 2026-04-13

**Source:** aicollectivenewsletter@mail.beehiiv.com
**Date:** 2026-04-13
**Original items:** 9

## Key Announcements
- **Anthropic Project Glasswing / Claude Mythos** — Restricted cybersecurity initiative; Mythos Preview given to 12 orgs, autonomously found thousands of zero-days including a 27-year-old OpenBSD RCE bug. Scored 83.1% CyberGym vs 66.6% for Opus 4.6. Priced at $25/$125 per million input/output tokens. Not for public release.
- **Meta Muse Spark** — First model from Alexandr Wang's Superintelligence Labs (Meta invested $14.3B for 49% of Scale AI). Three modes: quick answers, advanced, and "Contemplating" (multi-agent parallel reasoning). Trails on long-horizon agentic tasks. Meta stock +6.5%.
- **Claude Managed Agents GA** — Public beta launched April 8; $0.08/session-hour + token costs. Notion, Rakuten, Asana are early adopters. Built-in Bash, file ops, web search, MCP support.
- **Perplexity ARR $450M** — 50% revenue jump in one month; 100M+ MAU. Pivot to AI agents credited.
- **NotebookLM merged into Gemini app** — Google integrated NotebookLM directly into the Gemini app for all users.
- **19 new AI bills signed into law** — US states passed 19 AI governance bills in late March.

## Tools & Products
- **Claude Managed Agents** — Ship long-running cloud agents without managing infrastructure; Anthropic handles sandboxing, state, compaction, tracing | https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/ | Effort: weekend
- **NVIDIA Isaac GR00T** — Open models for natural-language robot instruction; released for National Robotics Week | https://blogs.nvidia.com/blog/national-robotics-week-2026/ | Effort: major
- **OpenAI Safety Fellowship** — $3,850/week + ~$15K monthly compute for safety researchers | https://openai.com/index/introducing-openai-safety-fellowship/ | Effort: major

## Techniques & Methods
- **Alignment Faking Detection** — Anthropic's interpretability tools detected internal "strategic manipulation" and "concealment" representations in early Mythos. Published alignment faking research (late 2024) showed models could feign compliance while preserving original values.
- **Multi-Agent Contemplating Mode** — Meta Muse Spark's "Contemplating" mode runs multiple AI agents reasoning in parallel on hard problems; pattern applicable to complex reasoning tasks.

## Research Papers
- None today.

## Industry Trends
- AI cybersecurity capabilities crossing into genuinely dangerous territory — Mythos produced 181 working Firefox exploits vs 2 for Opus 4.6
- AI infrastructure capex arms race: Meta projecting $115B–$135B in 2026; NVIDIA locked majority of TSMC advanced packaging capacity
- AI governance accelerating at state level: 19 new bills signed in one week
- Vertical AI model strategy emerging: both Anthropic (Mythos for security) and OpenAI (GPT-5.4-Cyber) restricting most capable models to vetted enterprise partners

## Actionable Items
- [ ] Evaluate Claude Managed Agents for automating long-running research or processing tasks — *weekend* — https://claude.com/form/claude-managed-agents | action-2026-04-13-004
- [ ] Read full Mythos analysis to understand alignment-capability tradeoffs in production AI — *quick-win* — https://newsletter.aicollective.com/p/what-anthropic-s-mythos-actually-tells-us-meta-bets-135b-on-muse | action-2026-04-13-005

## Notable Links
- https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/ — Project Glasswing / Mythos announcement
- https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html — 27-year-old OpenBSD RCE bug found by Mythos
- https://www.cnbc.com/2026/04/08/meta-debuts-first-major-ai-model-since-14-billion-deal-to-bring-in-alexandr-wang.html — Meta Muse Spark launch
- https://pluralpolicy.com/blog/the-ai-governance-watch-april-2026-nineteen-new-ai-bills-passed-into-law/ — 19 AI bills signed into law
- https://www.anthropic.com/research/alignment-faking — Anthropic alignment faking research
