# Superhuman Code — 2026-04-07 (edition 2)

**Source:** thecode@mail.joinsuperhuman.ai
**Date:** 2026-04-07
**Original items:** 6 main sections

## Key Announcements
- **Claude Code source code leaked** — Anthropic accidentally leaked the entire Claude Code source via npm update (~500K lines TypeScript). Analysis reveals performance comes from engineering harness (file history tracking, parallel agents, nav tools), not the model. DeepSeek or Kimi with the same harness would likely produce similar results.
- **OpenAI/Anthropic/Google unite on adversarial distillation** — Frontier Model Forum formed to fight unauthorized harvesting of US model responses to build cheaper knockoffs. Anthropic already cut off three Chinese-controlled labs.
- **Anthropic compute expansion** — Multi-gigawatt TPU deal with Google and Broadcom going live 2027. Run-rate revenue tripled since late 2025 to $30B. Enterprise customers over $1M/year doubled to 1,000+ in two months.
- **Meta open-sourcing Avocado (LLM) and Mango (image/video generator)** — Reversal of closed-source pivot reported in December.

## Tools & Products
- **Claude Code `!` backtick syntax** — Embeds live shell commands in SKILL.md; Claude executes them and inserts live output before processing. Works with PR diffs, test results, grep, API calls. | Effort: quick-win
- **Graphify** — AI coding agent skill that turns code/docs/papers/images into a queryable knowledge graph for precise architecture Q&A | Effort: weekend
- **Docs-as-Files tool** — Converts live documentation into an accessible filesystem that agents can browse; prevents AI code failures when docs change | Effort: weekend

## Techniques & Methods
- **Harness-over-model approach** — Engineering quality (file history, navigation tools, parallel background agents) matters more than model choice. Blueprint publicly available; execution remains the barrier.
- **Real-time data in Claude Code SKILL.md** — Use `!` backtick syntax: `- PR diff: !`gh pr diff`` — Claude executes at skill invocation time, not authoring time.
- **Mastra TypeScript agent pattern** — Tools + memory + event triggers integrated with Slack, Exa AI, and Cal.com for custom AI meeting assistants.

## Research Papers
- **Warp decode for MoE inference on Blackwell GPUs** (Cursor research) — Assigns computing to outputs directly instead of routing through individual MoE experts; 1.8x faster inference, more accurate.

## Industry Trends
- The "wrapper/harness" is now the competitive moat, not model quality — confirmed by Claude Code leak
- AI labs fighting adversarial distillation worth billions/year in lost revenue
- Meta reversing closed-source pivot; open models alongside Avocado/Mango proprietary models
- Milla Jovovich's agentic memory tool scored 100% on LongMemEval (unusual high score)

## Actionable Items
- [ ] Add `!` backtick syntax to SKILL.md files for live PR diffs, test output, and log data — *quick-win* | action-2026-04-07-028
- [ ] Read Claude Code leaked source breakdown for system prompt construction insights — *quick-win* | action-2026-04-07-029
- [ ] Build Karpathy-style LLM knowledge base using Mastra TypeScript framework (hooks + memory + Obsidian vault) — *weekend* | action-2026-04-07-030

## Notable Links
- Claude Code leaked source analysis (npm leak, system prompt construction)
- How Perplexity/Azure/HubSpot make RAG 32x more memory efficient (explained with code)
- Inside Codex: OpenAI Head of DevRel on how team actually ships
- Graphify GitHub repo (code/docs → queryable knowledge graph)
- Stanford CS153 AI systems course (first lecture free and public)
