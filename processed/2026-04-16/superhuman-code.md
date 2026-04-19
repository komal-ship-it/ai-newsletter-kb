# Superhuman (The Code) — 2026-04-16

**Source:** thecode@mail.joinsuperhuman.ai
**Date:** 2026-04-16
**Original items:** 8

## Key Announcements
- **Gemini 3.1 Flash TTS** — Google's new text-to-speech model; natural language control over tone, pace, and delivery; 70+ languages; native multi-speaker dialogue; consistent character voices across scenes
- **Claude Code rebuilt with split-pane interface** — New sidebar organizes multiple sessions by project or status; built-in file editing, diff reviews, terminal; Theo Browne (T3 Chat CEO) reported 40 bugs in first hour of the new build
- **Cloudflare rebuilding Wrangler CLI for agents** — AI agents are now Cloudflare's primary API users; single schema auto-generates every command with strict naming rules; CLI approach is 10-32x more token-efficient than MCP-based setups; 6 major open-source projects launched Q1 2026 with this focus

## Tools & Products
- **Gemini 3.1 Flash TTS** — Text-to-speech with natural language tone/pace control; 70+ languages; multi-speaker | Google AI Studio | Effort: quick-win
- **Claude Code (new split-pane build)** — Multi-session sidebar, file editing, diff reviews, terminal | claude.ai/code | Effort: quick-win
- **Gemini Scribe** — Obsidian plugin integrating Gemini to search, edit, and organize vault files | GitHub | Effort: quick-win

## Techniques & Methods
- **/loop command for deploy monitoring** — Use `/loop 5m check if the deploy succeeded and report back` in Claude Code to monitor deploys without tab-switching; supports s/m/h/d intervals; defaults to 10m; session-scoped, expires after 3 days; works with any slash command e.g. `/loop 20m /review-pr 1234`
- **Spec-driven development with coding agents** — Write clear markdown specs and project guides first; agents build from the spec; reduces iteration waste (DeepLearning.AI tutorial)
- **Agents-first CLI design** — Enforce consistent naming via single schema generation rather than manual code reviews; eliminates the "get vs info" ambiguity that breaks agents

## Research Papers
- **Trusted access for the next era of cyber defense** (OpenAI) — GPT-5.4-Cyber being offered to verified defenders with less-restricted access to find and fix vulnerabilities; hackers using advanced AI offensively

## Industry Trends
- AI agents outrank humans as primary API users — Cloudflare's Wrangler rebuild driven by agents being the dominant caller
- CLI-for-agents approach gaining momentum: 6 major OSS projects in Q1 2026; 10-32x more token-efficient than MCP but no single standard winning
- Prompt injection attacks on websites growing — websites embedding content to trick AI agents into unintended actions
- AllBirds pivoting to GPU compute; stock surged 5x — signals how "AI pivot" label moves markets regardless of substance

## Actionable Items
- [ ] Use `/loop 5m` in Claude Code to monitor deploys in background while staying focused — *quick-win* — built into Claude Code, no setup | action-2026-04-16-004
- [ ] Try Gemini 3.1 Flash TTS for voice/audio generation — 70+ languages, natural language tone control — *quick-win* | action-2026-04-16-005
- [ ] Read Cursor VP of Developer Education's 30-min agent course for planning features and squashing bugs — *quick-win* | action-2026-04-16-006
- [ ] Find and test the "8 subagents to fix vibecoded codebase" viral prompt for cleaning messy code — *quick-win* | action-2026-04-16-007

## Notable Links
- Cloudflare Wrangler CLI rebuild post — agents-first CLI design rationale; single-schema command generation
- DeepLearning.AI spec-driven development with coding agents tutorial
- "8 subagents to fix everything wrong with a vibecoded codebase" viral prompt
- GPT-5.4-Cyber (OpenAI) — less-restricted access for verified cyber defenders
