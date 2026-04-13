# Superhuman Code — 2026-04-09

**Source:** thecode@mail.joinsuperhuman.ai
**Date:** 2026-04-09
**Original items:** 12

## Key Announcements
- **Claude Managed Agents launched** — Anthropic released a suite of composable APIs that cuts months of agent infrastructure work down to days; sandboxing, orchestration, and permissions handled by Anthropic's cloud. Early adopters: Notion and Asana.
- **Meta Muse Spark released** — Meta's Superintelligence Labs' first public model; multimodal, excels at vision and reasoning, features Contemplating mode (parallel agents without latency increase); matches Llama 4 Maverick performance at 10x less compute.
- **Cursor Bugbot self-improvement** — Bugbot now learns from developer interactions (reactions, replies, reviewer comments) to refine its rules; 44K+ rules generated across 110K repos; ~80% resolution rate.
- **Project Glasswing** — Anthropic using an unreleased Claude model to proactively hunt vulnerabilities in critical open-source software; a senior engineer's reaction went viral (27M views).
- **YC names youngest General Partner** — A 25-year-old who dropped out at 15 and built a $700M company.

## Tools & Products
- **Claude Managed Agents** — Suite of composable APIs for production-grade cloud-hosted AI agents; sandboxing, orchestration, scoped permissions, persistent sessions | https://claude.com/blog/claude-managed-agents | Effort: weekend
- **Meta Muse Spark** — Multimodal AI model with Contemplating mode (parallel agents); available in Meta AI app, website, and API for selected partners | https://meta.ai/ | Effort: quick-win
- **Cursor Bugbot (upgraded)** — AI code reviewer that learns from dev interactions to self-improve rules; 80% resolution rate across 110K repos | https://cursor.com/blog/bugbot-learning | Effort: quick-win
- **Vouch (Mitchell Hashimoto)** — Trust-gating tool to filter out unreliable open-source dependencies in agent-assembled software | https://github.com/mitchellh/vouch | Effort: quick-win
- **Andrej-karpathy-skills (GitHub repo)** — CLAUDE.md optimized for Claude Code, incorporating Karpathy's LLM coding pitfall observations | https://github.com/forrestchang/andrej-karpathy-skills | Effort: quick-win
- **Vera** — Programming language designed for LLMs that makes everything explicit and verifiable | https://veralang.dev/ | Effort: weekend
- **MongoDB AI Learning Hub** — RAG, Vector Search, LLM optimization tutorials for all skill levels | https://fandf.co/41l1KsP | Effort: quick-win

## Techniques & Methods
- **Fix Claude Code's thinking regression** — Run `/effort high` for faster results; `/effort max` on Opus for hard debugging; add `"showThinkingSummaries": true` to `~/.claude/settings.json`; add "Research the codebase before editing. Never change code you haven't read." to CLAUDE.md. Nuclear option: `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1`.
- **Self-evolving agent memory architecture** — Use hooks to automatically capture and summarize coding sessions into an Obsidian vault, giving AI agents long-term memory that evolves with the codebase; based on Karpathy's knowledge base architecture | https://www.youtube.com/watch?v=7huCP6RkcY4
- **Ship primitives, not just products** — AI agents prioritize well-documented open-source building blocks; the leverage in the software ecosystem has shifted downstream toward foundational tools. Open-source libraries now outpace polished apps in adoption.
- **iOS Codex shortcut** — Skill to build iOS apps with Codex despite agents not knowing Xcode | https://x.com/PaulSolt/status/2041643862913949929
- **Engineering team redesign for the AI era** — Postman founder's blueprint for restructuring engineering teams | https://x.com/ivanburazin/status/2041199368296931595

## Research Papers
- **How LLMs Follow Instructions** — Investigates whether AI models rely on a single universal instruction-following process; finding: models dynamically coordinate diverse, specialized language skills rather than a single process | https://arxiv.org/abs/2604.06015

## Industry Trends
- Anthropic shipped 75+ updates in 60 days — extraordinary release velocity.
- Open-source libraries and primitives are now adopted faster than full applications; AI agents preferentially pull from open-source, free components.
- Agent-assembled software is creating new security and stability risks; trust-gating and dependency vetting tools are emerging as a response.
- Mitchell Hashimoto's libghostty (open-sourced terminal library) reached millions of daily users in 2 months vs. 18 months for the parent app — a signal of where adoption is accelerating.
- Big tech (Meta) entering the proprietary/open-source hybrid model space; Muse Spark proprietary, other Muse models open source.

## Actionable Items
- [ ] Add `"showThinkingSummaries": true` to `~/.claude/settings.json` and run `/effort high` in Claude Code to immediately improve reasoning quality — *quick-win* — https://x.com/PawelHuryn/status/2041418614557802747 | action-2026-04-09-007
- [ ] Add "Research the codebase before editing. Never change code you haven't read." to CLAUDE.md — *quick-win* — https://github.com/anthropics/claude-code/issues/42796 | action-2026-04-09-008
- [ ] Clone and review the andrej-karpathy-skills CLAUDE.md template to improve Claude Code performance — *quick-win* — https://github.com/forrestchang/andrej-karpathy-skills | action-2026-04-09-009
- [ ] Watch the self-evolving agent memory tutorial and implement hooks for Obsidian-based session capture — *weekend* — https://www.youtube.com/watch?v=7huCP6RkcY4 | action-2026-04-09-010
- [ ] Evaluate Vouch for filtering unreliable dependencies in any agent-assembled project — *quick-win* — https://github.com/mitchellh/vouch | action-2026-04-09-011
- [ ] Read the "How LLMs Follow Instructions" paper to understand instruction-following mechanics in deployed models — *weekend* — https://arxiv.org/abs/2604.06015 | action-2026-04-09-012
- [ ] Test Meta Muse Spark's Contemplating mode against Claude for parallel agent workflows — *quick-win* — https://meta.ai/ | action-2026-04-09-013

## Notable Links
- https://claude.com/blog/claude-managed-agents — Official Anthropic announcement: Claude Managed Agents
- https://codenewsletter.ai/p/anthropic-introduces-claude-managed-agents-meta-drops-muse-spark — Full newsletter online
- https://x.com/mitchellh/status/2041566958681014418 — Mitchell Hashimoto on open-source library vs. app adoption
- https://github.com/anthropics/claude-code/issues/42796 — Claude Code thinking regression issue thread (17K+ thinking blocks analyzed)
- https://ai.meta.com/blog/introducing-muse-spark-msl — Meta Muse Spark official announcement
- https://cursor.com/blog/bugbot-learning — Cursor Bugbot self-improvement write-up
