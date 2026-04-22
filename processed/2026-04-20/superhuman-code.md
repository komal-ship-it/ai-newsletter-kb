# Superhuman — The Code — 2026-04-20

**Source:** thecode@mail.joinsuperhuman.ai
**Date:** 2026-04-20
**Original items:** 8

## Key Announcements
- **Vercel breach via Context.ai** — Attacker compromised an employee, escalated through Google Workspace into Vercel internal environments. Environment variables exposed. Stolen tokens and source code being sold. Next.js and Turbopack unaffected. **Rotate secrets now.**
- **Three senior OpenAI leaders walk out** — Ex-CPO Kevin Weil among three who left the same day as the company kills "side quests" including Sora.
- **OpenMythos** — Kye Gomez open-sourced a PyTorch reconstruction of Claude Mythos architecture; theory: same weights looped multiple times, all thinking silently in a single forward pass.
- **Founder $100k Claude Code bill** — Shipped a plugin cutting Claude Code costs 25-55%.

## Tools & Products
- **Token Optimizer MCP** — 95%+ reduction in Claude Code token usage | https://github.com/ooples/token-optimizer-mcp | Effort: quick-win
- **LSP Plugins for Claude Code** — Auto-diagnostics after every edit: typescript-lsp, pyright-lsp, rust-analyzer-lsp, gopls-lsp via /plugin install | Effort: quick-win
- **Claude Design** — Scans codebase during onboarding to build a design system; outputs prototypes and wireframes | https://www.anthropic.com/news/claude-design-anthropic-labs | Effort: quick-win
- **OpenMythos** — Open-source PyTorch reconstruction of Anthropic Mythos architecture | Effort: weekend

## Techniques & Methods
- **LSP-Driven Claude Code Diagnostics** — Install language server plugins so Claude sees type errors and linter warnings automatically after every edit, catching issues before commit.
- **Supply Chain AI Security** — Third-party AI tools (Context.ai in Vercel's case) are now an active attack surface; audit which AI tools have OAuth access to your critical environments.

## Research Papers
- **Prefill-as-a-Service (Moonshot AI)** — Standard internet cables can handle splitting AI inference tasks across data centers; enables distributed prefill without specialized networking.

## Industry Trends
- AI tool supply chain becoming primary attack vector: compromised third-party integrations bypass perimeter security.
- Talent exodus from OpenAI accelerating as company prioritizes commercial products over research initiatives.
- $100k/month Claude Code bills emerging for heavy users; cost optimization tooling now a market.

## Actionable Items
- [ ] Install LSP plugins for Claude Code to get automatic diagnostics (typescript-lsp, pyright-lsp) — *quick-win* | action-2026-04-20-006
- [ ] Evaluate Token Optimizer MCP to reduce Claude Code costs — *quick-win* — https://github.com/ooples/token-optimizer-mcp | action-2026-04-20-007

## Notable Links
- https://vercel.com/kb/bulletin/vercel-april-2026-security-incident — Vercel security incident bulletin
- https://github.com/ooples/token-optimizer-mcp — Token Optimizer MCP
- https://www.youtube.com/watch?v=njWyDHKYeVA — Deploy LLMs on Cloud Run GPUs tutorial
- https://codenewsletter.ai/p/vercel-breached-via-compromised-ai-tool-anthropic-drops-claude-design — Full issue
