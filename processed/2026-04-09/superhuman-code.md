# Superhuman Code — 2026-04-09

**Source:** thecode@mail.joinsuperhuman.ai
**Date:** 2026-04-09
**Original items:** 6 main sections

## Key Announcements
- **Claude Managed Agents** — Suite of APIs cutting months of infrastructure work to days. Anthropic handles sandboxing, orchestration, and permissions. Notion and Asana building coding agents, AI teammates, enterprise workflows on it.
- **Meta Muse Spark** — Contemplating mode runs multiple agents in parallel without increasing latency; updated training stack matches Llama 4 Maverick performance at 10x less compute.
- **Cursor Bugbot self-improvement** — Tracks developer reactions and reviewer comments to refine its own rules. 110K repos, 44K self-generated rules, ~80% resolution rate.
- **Project Glasswing** — Anthropic using unreleased Claude model to proactively hunt vulnerabilities in critical open-source software before attackers.

## Tools & Products
- **Andrej-karpathy-skills** — CLAUDE.md optimized for Claude Code incorporating Karpathy's observations on LLM coding pitfalls | GitHub | Effort: quick-win
- **LLM Guide for Engineers** — Teaches LLMs the way engineers need to learn: build → optimize → deploy (skips academic papers) | Effort: quick-win
- **Claude Code thinking regression fixes:**
  - `/effort high` in Claude Code (fastest fix)
  - `/effort max` on Opus + `"showThinkingSummaries": true` in `~/.claude/settings.json`
  - Add to CLAUDE.md: "Research the codebase before editing. Never change code you haven't read."
  - Bypass adaptive thinking: `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1`

## Techniques & Methods
- **Open-source-first agent component strategy** — Agents consistently choose open-source, free, well-documented building blocks. Mitchell Hashimoto's libghostty reached millions of daily users in 2 months (vs 1M for the app it came from). Ship primitives and libraries alongside finished products.
- **Self-evolving agent memory** — Use Claude Code hooks to capture and summarize coding sessions into Obsidian vault (Karpathy KB architecture). Gives agent long-term memory that evolves with codebase.
- **Claude Code thinking fix** — AMD engineer analysis of 17,000+ thinking blocks found under-allocation of reasoning for complex tasks; Claude skips deep analysis and attempts code edits prematurely.

## Research Papers
- **How LLMs follow instructions** — Models don't use a single universal process; they dynamically coordinate diverse specialized language skills to satisfy specific rules.

## Industry Trends
- libghostty (open-source library from Ghostty terminal emulator) outgrew the app within 2 months by being composable for AI agents
- "Building block" layer of the ecosystem now handles R&D and niche use cases automatically
- YC names youngest General Partner ever: 25-year-old who dropped out at 15, built a $700M company
- Postman's founder: blueprint for engineering teams in the AI era published

## Actionable Items
- [ ] Add to CLAUDE.md: "Research the codebase before editing. Never change code you haven't read." — immediate thinking regression fix — *quick-win* | action-2026-04-09-008
- [ ] Run `/effort high` in Claude Code for complex tasks; `/effort max` on Opus for hard debugging — *quick-win* | action-2026-04-09-009
- [ ] Add `"showThinkingSummaries": true` to `~/.claude/settings.json` — *quick-win* | action-2026-04-09-010
- [ ] Build self-evolving memory system for Claude Code using hooks to capture sessions into Obsidian vault — *weekend* | action-2026-04-09-011
- [ ] Download Andrej-karpathy-skills CLAUDE.md from GitHub and review for applicable optimizations — *quick-win* | action-2026-04-09-012

## Notable Links
- Self-evolving agent memory tutorial (hooks → Obsidian vault, Karpathy architecture)
- Andrej-karpathy-skills CLAUDE.md (GitHub)
- How LLMs follow instructions (paper)
- Building macOS Apps with Codex skill (iOS Shortcut trending item)
- Postman founder's engineering team blueprint for AI era
