# Superhuman — The Code — 2026-04-07

**Source:** thecode@mail.joinsuperhuman.ai
**Date:** 2026-04-07
**Original items:** 10

## Key Announcements
- **OpenAI + Anthropic + Google vs. model copying** — Frontier Model Forum coordinating against "adversarial distillation" (harvesting US model responses to train knockoffs); Anthropic already cut off 3 Chinese-controlled labs; US officials estimate billions drained/year
- **Anthropic × Google × Broadcom compute deal** — Multi-gigawatt TPU capacity deal, live 2027; run-rate revenue tripled to $30B since late 2025; 1,000+ enterprise customers spending $1M+/year (doubled in 2 months)
- **Meta open-source Avocado + Mango** — Open-source versions of next frontier LLM (Avocado) and image/video model (Mango) in development; lighter than proprietary versions due to safety concerns
- **Claude Code source code leak** — 500K lines TypeScript accidentally leaked via npm update; reveals harness engineering (not the model) is the core competitive advantage

## Tools & Products
- **Graphify** — Turns any folder of code, docs, papers, or images into a queryable knowledge graph; gives AI agents full system context for complex architecture questions | https://github.com/safishamsi/graphify | Effort: weekend
- **Cursor warp decode** — 1.8x faster inference on Blackwell GPUs by assigning computing directly to outputs instead of managing MoE expert routing | https://cursor.com/blog/warp-decode | Effort: quick-win
- **Mastra TypeScript framework** — Build AI meeting assistants integrating Slack, Exa AI, Cal.com (tutorial available) | https://www.youtube.com/watch?v=pbAqx8B6NVc&t=876s | Effort: weekend
- **Live docs as filesystem** — Tool turns live documentation into an accessible filesystem that agents can browse; prevents code failing when docs change | https://x.com/arlanr/status/2041215978957389908 | Effort: weekend

## Techniques & Methods
- **Claude Code `!` backtick syntax in SKILL.md** — Embed shell commands directly in skill files; Claude Code executes and swaps in live output before processing. Example: `!`gh pr diff`` in pr-summary skill; use read-only commands only (cat, grep, gh pr view). Source: Lydia Hallie (Claude Code team)
- **Harness-first agent development** — Claude Code leak proves performance comes from engineering infrastructure (file history, navigation tools, parallel background agents), not just underlying model; DeepSeek or Kimi with same harness would achieve similar results
- **RAG 32x memory efficiency** — Technique used by Perplexity, Azure, HubSpot; explained with code: https://x.com/_avichawla/status/2040326889928356122
- **Compounding LLM knowledge base** — Build a self-improving knowledge base inspired by Karpathy's approach: https://x.com/hooeem/status/2041196025906418094
- **Production agent anatomy** — When AI agent fails, the problem is rarely the model; stateless LLM → production agent framework: https://x.com/akshay_pachaar/status/2041146899319971922

## Research Papers
- **Cursor Warp Decode** (Cursor team) — MoE inference optimization: assign computing to outputs, skip expert routing overhead; 1.8x faster on Blackwell GPUs | https://cursor.com/blog/warp-decode

## Industry Trends
- Agent harness quality is becoming the key differentiator over model quality — Claude Code leak crystallizes this shift
- Frontier labs forming defensive coalitions against adversarial distillation by state-linked actors
- Anthropic's revenue trajectory ($30B run-rate) suggests enterprise AI spending is accelerating rapidly
- Meta reverting to open-source strategy despite prior pivot to closed-source — competitive pressure from Anthropic/OpenAI
- OpenAI safety governance credibility deteriorating (Safety Fellowship announced hours after safety teams dissolved per New Yorker investigation)

## Actionable Items
- [ ] Implement `!` backtick syntax in Claude Code SKILL.md files to inject live data (PR diffs, test results) — *quick-win* — https://x.com/lydiahallie/status/2034337963820327017 | action-2026-04-08-011
- [ ] Read dbreunig's breakdown of Claude Code system prompt construction — immediate applicability to own agent work — *quick-win* — https://www.dbreunig.com/2026/04/04/how-claude-code-builds-a-system-prompt.html | action-2026-04-08-012
- [ ] Try Graphify to build queryable knowledge graph from existing codebase or docs — *weekend* — https://github.com/safishamsi/graphify | action-2026-04-08-013
- [ ] Apply RAG memory efficiency technique to current RAG workflows — *weekend* — https://x.com/_avichawla/status/2040326889928356122 | action-2026-04-08-014

## Notable Links
- https://www.dbreunig.com/2026/04/04/how-claude-code-builds-a-system-prompt.html — How Claude Code builds system prompts (post-leak breakdown)
- https://www.anthropic.com/news/google-broadcom-partnership-compute — Anthropic × Google × Broadcom TPU deal
- https://siliconangle.com/2026/04/06/report-meta-developing-open-source-versions-upcoming-ai-models/ — Meta open-source Avocado + Mango
- https://x.com/RonanFarrow/status/2041224604878864514 — OpenAI safety team dissolution (Ronan Farrow)
- https://github.com/safishamsi/graphify — Graphify knowledge graph repo
- https://cursor.com/blog/warp-decode — Cursor warp decode paper
