# Superhuman Code — 2026-04-07

**Source:** thecode@mail.joinsuperhuman.ai
**Date:** 2026-04-07
**Original items:** 10

## Key Announcements
- **OpenAI, Anthropic, Google anti-distillation coalition** — Three rivals joined the Frontier Model Forum to combat "adversarial distillation" — harvesting US model outputs to build cheaper knockoffs. Anthropic already cut off three Chinese labs caught doing this. US officials estimate billions drained annually.
- **Anthropic secures multi-gigawatt compute deal** — Partnership with Google and Broadcom for next-gen TPU capacity going live in 2027. Run-rate revenue tripled to $30B since late 2025; 1,000+ enterprise customers spending $1M+/year (doubled in two months).
- **Meta open-sourcing next frontier models** — Avocado (LLM) and Mango (image/video generator) to get open-source editions. Will be lighter versions due to AI safety concerns. No release date yet.
- **Claude Code source code leak** — Anthropic accidentally leaked ~500K lines of TypeScript via npm update. Key finding: performance comes from engineering harness, not the model itself.
- **Milla Jovovich builds agentic memory tool** — Actress scored 100% on LongMemEval with her agentic memory tool.

## Tools & Products
- **Graphify** — AI coding agent skill that turns any folder of code, docs, papers, or images into a queryable knowledge graph. Full system context for architecture questions. | https://github.com/safishamsi/graphify | Effort: weekend
- **Wispr Flow** — Voice input layer for AI-native dev workflows. Syntax-aware (camelCase, snake_case, acronyms, file names). Integrates with Cursor, VS Code, Slack, Linear. Auto-tags files in Cursor/Windsurf. Mac, Windows, iOS, Android. | https://ref.wisprflow.ai/thecode | Effort: quick-win
- **Claude Code SKILL.md with live shell commands** — Use `!` backtick syntax to embed shell commands in SKILL.md files; Claude Code executes and injects live output before processing. Pattern: `.claude/skills/pr-summary/SKILL.md` with `!` + `gh pr diff` etc. | Effort: quick-win
- **Mastra TypeScript framework** — For building custom AI agents with tools, memory, and event triggers. Used in tutorial for AI meeting assistant integrating Slack, Exa AI, Cal.com. | Effort: weekend

## Techniques & Methods
- **Claude Code SKILL.md live data injection** — Create `.claude/skills/{name}/SKILL.md`. Use `!` backtick syntax: `- PR diff: !` + `gh pr diff` ` `. Claude executes the command and substitutes live output. Stick to read-only commands (`cat`, `grep`, `gh pr view`) to prevent state changes.
- **Agent harness architecture** — Claude Code's leaked source shows: file history tracking to save context, specialized navigation tools, parallel agents for background tasks. Harness quality now more important than model choice — same setup with DeepSeek/Kimi yields similar results.
- **32x memory-efficient RAG** — Simple technique used by Perplexity, Azure, HubSpot (explained with code): https://x.com/_avichawla/status/2040326889928356122
- **Self-improving LLM knowledge base** — Karpathy-inspired pattern: LLM reads raw sources → writes structured articles → maintains its own index → self-checks. Tutorial: https://x.com/hooeem/status/2041196025906418094

## Research Papers
- **Warp Decode — Cursor on Blackwell GPUs** — Assigns compute directly to outputs instead of routing through expert management in MoE models, making single-token generation 1.8x faster and more accurate. | https://cursor.com/blog/warp-decode

## Industry Trends
- **Agent harness > model** — Claude Code leak confirms: engineering quality of the wrapper is now the competitive moat, not model choice. LangChain reached top-5 benchmarks via harness improvement; Vercel improved by simplifying tools.
- **OpenAI Safety Fellowship timing** — Announced hours after New Yorker investigation revealed dissolved safety teams. Credibility gap widening.
- **Live docs-as-filesystem pattern** — Tools that turn live documentation into agent-browsable filesystems solving the "docs go stale" problem in AI coding.

## Actionable Items
- [ ] Implement Claude Code SKILL.md live data injection for PR summaries — create `.claude/skills/pr-summary/SKILL.md` using `!` backtick syntax with `gh pr diff` — *quick-win* | action-2026-04-07-032
- [ ] Read the Claude Code system prompt breakdown from the leaked source — understand harness architecture — *quick-win* — https://www.dbreunig.com/2026/04/04/how-claude-code-builds-a-system-prompt.html | action-2026-04-07-033
- [ ] Implement 32x memory-efficient RAG technique — follow the Perplexity/Azure/HubSpot pattern with code — *weekend* — https://x.com/_avichawla/status/2040326889928356122 | action-2026-04-07-034
- [ ] Try Graphify to generate a queryable knowledge graph from this newsletter KB codebase — *weekend* — https://github.com/safishamsi/graphify | action-2026-04-07-035
- [ ] Watch the Mastra AI meeting assistant tutorial — build custom agent with tools/memory/event triggers — *weekend* — https://www.youtube.com/watch?v=pbAqx8B6NVc&t=876s | action-2026-04-07-036

## Notable Links
- https://www.dbreunig.com/2026/04/04/how-claude-code-builds-a-system-prompt.html — Claude Code system prompt breakdown
- https://cursor.com/blog/warp-decode — Warp Decode paper (1.8x inference speedup)
- https://github.com/safishamsi/graphify — Graphify repo
- https://x.com/_avichawla/status/2040326889928356122 — 32x memory-efficient RAG
- https://x.com/hooeem/status/2041196025906418094 — Self-improving LLM KB walkthrough
- https://codenewsletter.ai/p/openai-anthropic-google-fight-model-copying-meta-goes-open-source — Full issue
