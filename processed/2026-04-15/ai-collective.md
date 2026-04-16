# AI Collective — 2026-04-15

**Source:** aicollectivenewsletter@mail.beehiiv.com
**Date:** 2026-04-15
**Original items:** 6

## Key Announcements
- **Shopify AI Toolkit open-sourced** — Free MIT-licensed MCP server connecting AI coding agents (Claude Code, Cursor, VS Code, Gemini CLI, OpenAI Codex) directly to Shopify stores. 16 skills covering API learning, live docs, code validation, store ops. Rate limit: 1,000 cost points/min.
- **Atlassian Confluence Remix open beta** — Highlight any Confluence section → generate chart, infographic, or scorecard layered on top. Three partner agents (Lovable, Replit, Gamma) convert content to prototypes, apps, presentations.
- **Claude Managed Agents public beta** — Available to all Claude API accounts. Built-in tools: Bash, file ops, web search, MCP. $0.08/session-hour + token costs. Early adopters: Notion, Rakuten, Asana.

## Tools & Products
- **Shopify AI Toolkit (MCP)** — Plain-English store management via AI agents; MIT-licensed; Claude Code/Cursor/VS Code compatible | https://shopify.dev/docs/apps/build/ai-toolkit | Effort: weekend
- **Atlassian Confluence Remix** — Highlight → visual (chart/infographic/scorecard); Lovable/Replit/Gamma partner agents | https://support.atlassian.com/confluence-cloud/docs/transform-content-with-remix/ | Effort: quick-win
- **Claude Managed Agents** — Long-running cloud agents without infrastructure management; Bash + file ops + web search + MCP built-in | https://claude.com/form/claude-managed-agents | Effort: weekend
- **Lovable (Confluence partner)** — Converts Confluence product spec to working interactive prototype | https://www.atlassian.com/software/confluence | Effort: weekend
- **Replit (Confluence partner)** — Converts technical doc to forkable starter app | Effort: weekend
- **Gamma (Confluence partner)** — Converts meeting notes to polished presentation | Effort: quick-win

## Techniques & Methods
- **MCP as store control plane** — Connect Claude Code to Shopify Dev MCP Server → manage inventory, products, SEO, pricing in plain English. Pattern extends to any platform with MCP server.
- **Doc-to-artifact pipeline** — Confluence Remix + partner agents: spec → prototype (Lovable), tech doc → starter app (Replit), meeting notes → deck (Gamma). No manual reformatting.
- **Managed agent architecture** — Define task, Anthropic handles: sandboxed execution, state management, context compaction, end-to-end tracing. Eliminates infra work for one-off or recurring long-running tasks.

## Research Papers
- None today.

## Industry Trends
- MCP becoming universal control plane: Shopify, Atlassian, Cloudflare all shipping MCP servers for their platforms
- "Define task, run forever" agent pattern becoming available as managed service (Claude Managed Agents, Vercel Open Agents)
- Enterprise doc/knowledge tools (Confluence) integrating AI transformation layer directly
- Anthropic enterprise pricing shift from flat fee to per-token (separate coverage in TLDR Apr 15)

## Actionable Items
- [ ] Connect Shopify AI Toolkit MCP server to Claude Code for store management — *weekend* — https://shopify.dev/docs/apps/build/ai-toolkit | action-2026-04-15-007
- [ ] Sign up for Claude Managed Agents beta and test with a recurring long-running task — *weekend* — https://claude.com/form/claude-managed-agents | action-2026-04-15-008
- [ ] Use Confluence Remix + Gamma to convert meeting notes to deck — *quick-win* — https://support.atlassian.com/confluence-cloud/docs/transform-content-with-remix/ | action-2026-04-15-009

## Notable Links
- https://shopify.dev/docs/apps/build/ai-toolkit — Shopify AI Toolkit documentation
- https://support.atlassian.com/confluence-cloud/docs/transform-content-with-remix/ — Atlassian Confluence Remix docs
- https://claude.com/form/claude-managed-agents — Claude Managed Agents beta signup
- https://modelcontextprotocol.io/introduction — MCP protocol introduction
- https://luma.com/17mpuzyj — MongoDB.local London May 7 (founders event)
