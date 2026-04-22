# Superhuman — The Code — 2026-04-20 (raw)

**Source:** thecode@mail.joinsuperhuman.ai
**Message ID:** 19dab31c59c14523
**Date:** 2026-04-20
**Subject:** 🚨 Vercel suffers MAJOR security breach

---

The AI race is quietly opening side doors for supply chain attacks. Vercel just became the latest platform caught in the crosshairs after a major breach through a third-party AI tool.

TODAY IN PROGRAMMING

Hackers breach Vercel through a compromised third-party AI tool (Context.ai): Attackers compromised an employee, escalated from his Google Workspace into Vercel's internal environments, and accessed environment variables not flagged as sensitive. Attacker is advertising stolen tokens and source code. Next.js and Turbopack unaffected — rotate secrets immediately.
https://vercel.com/kb/bulletin/vercel-april-2026-security-incident

Open-source project recreates Claude Mythos architecture: Kye Gomez released OpenMythos — a PyTorch project rebuilding Anthropic's flagship model. Theory: Mythos runs the same weights through a loop multiple times, doing all thinking silently within a single forward pass.

Anthropic drops Claude Design: Turns prompts, uploads, or codebases into prototypes, wireframes, and slide decks. Scans your codebase during onboarding to build a design system.
https://www.anthropic.com/news/claude-design-anthropic-labs

INSIGHT: Jensen Huang vs Dwarkesh Patel on selling AI chips to China
Huang called conceding the Chinese market a 'loser premise' — bans don't slow China's AI, they just drive business to Huawei. Patel argued US leads because of more compute. If US sells chips, China may reach AI frontier faster; if not, US risks losing global hardware standards to Huawei.

IN THE KNOW
- Anthropic restricted its top model to ~40 orgs for security; the NSA is using it despite being blacklisted by the Department of War.
- Three senior OpenAI leaders walked out in a single day, including ex-CPO Kevin Weil, as the company kills 'side quests' like Sora.
- A founder hit with a $100k Claude Code bill shipped a plugin cutting costs 25-55%.

AI CODING HACK: How to catch errors before Claude Code commits
LSP plugins give Claude automatic diagnostics after every edit:
/plugin install typescript-lsp@claude-plugins-official
/plugin install pyright-lsp@claude-plugins-official
/plugin install rust-analyzer-lsp@claude-plugins-official
/plugin install gopls-lsp@claude-plugins-official

TOP RESOURCES
- Top Tutorial: Deploy LLMs on Cloud Run GPUs. https://www.youtube.com/watch?v=njWyDHKYeVA
- Top Repo: Token Optimizer — 95%+ reduction in Claude Code token usage. https://github.com/ooples/token-optimizer-mcp
- Trending Paper: Prefill-as-a-Service (Moonshot AI) — standard internet cables can handle splitting AI tasks across data centers.

https://codenewsletter.ai/p/vercel-breached-via-compromised-ai-tool-anthropic-drops-claude-design
