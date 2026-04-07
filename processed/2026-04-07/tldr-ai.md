# TLDR AI — 2026-04-07

**Source:** dan@tldrnewsletter.com
**Date:** 2026-04-07
**Original items:** 12

## Key Announcements
- **Anthropic revenue run-rate hits $30B** — Up from ~$9B at end of 2025; surpasses OpenAI's ~$24B run-rate. Partnership expansion with Google and Broadcom, including 3.5 GW of TPU compute starting 2027.
- **OpenAI CFO conflict** — CFO Sarah Friar excluded from financial planning conversations after raising doubts about readiness for 2026 IPO and concerns over server spending.
- **Artemis II returns** — First crewed lunar flyby in 50+ years; reached 252,756 miles from Earth, surpassing Apollo 13 record. Splashdown Friday April 10.
- **Generalist GEN-1 robotics at 99% reliability** — Physical AI system reaches production-level success on broad range of manipulation tasks, including improvising around disruptions.

## Tools & Products
- **Google AI Edge Gallery** — Official Google app for running Gemma 4 models directly on-device (iPhone). | Effort: quick-win
- **Vercel autonomous PR review agent** — Reviews and auto-merges 58% of PRs in their largest Next.js monorepo with no human reviewer; cut average merge time 62%. | Effort: weekend

## Techniques & Methods
- **Meta tribal knowledge pre-compute engine** — Swarm of 50+ specialized AI agents systematically read every file in a large-scale data pipeline to produce context files encoding tribal knowledge. Results in structured navigation guides for 100% of code modules. Model-agnostic knowledge layer.
- **Agentic coding → monolithic architecture** — AI enables developers to work more monolithically by reducing the overhead of managing distributed complexity.

## Research Papers
- None today.

## Industry Trends
- Anthropic revenue accelerating faster than OpenAI ($30B vs $24B run-rate)
- Compute crunch expected to define next 18–24 months
- Quantum computing risk: cryptography engineers say act now even if timelines uncertain
- Robotics crossing into production-reliability territory (99% on GEN-1)

## Actionable Items
- [ ] Evaluate Meta's tribal knowledge pre-compute pattern for your own agentic pipelines — *weekend* — Build per-module context files using a swarm of reader agents before deploying coding agents | action-2026-04-07-001
- [ ] Try Google AI Edge Gallery — run Gemma 4 locally on iPhone for offline AI workflows — *quick-win* | action-2026-04-07-002
- [ ] Read Vercel's autonomous PR merge writeup — extract the agent review criteria for your own CI/merge automation — *quick-win* | action-2026-04-07-003

## Notable Links
- Vercel: 58% of PRs merge without human review — (TLDR article, search "58% of PRs in our largest monorepo")
- Meta tribal knowledge AI pipeline — (TLDR article, search "How Meta used AI to map tribal knowledge")
- Google AI Edge Gallery — run Gemma 4 on iPhone
- Quantum computing timeline perspective — cryptography engineer's take
