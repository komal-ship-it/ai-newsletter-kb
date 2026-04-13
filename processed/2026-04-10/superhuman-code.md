# Superhuman Code — 2026-04-10

**Source:** thecode@mail.joinsuperhuman.ai
**Date:** 2026-04-10
**Original items:** 10

## Key Announcements
- **Anthropic drops Claude Code Monitor tool** — Background script runner that acts as a "security camera" for your code. Watch for dev server errors, failing tests, or production launches for hours. Only fires up when something goes wrong — saves tokens. https://x.com/noahzweben/status/2042332268450963774
- **Cursor auto-attaches demo videos/screenshots to agent-generated PRs** — Cloud agents now automatically include visual proof of their changes. https://x.com/cursor_ai/status/2042287192895267212
- **OpenAI launches $100/mo Codex Pro plan** — 5x Codex usage, exclusive Pro model, unlimited Instant and Thinking models. Launch promo: up to 10x standard Plus usage through May 31. https://x.com/OpenAI/status/2042295688323875316
- **Anthropic publishes 50+ Claude cookbook guides** — Ready-to-use guides covering managed agents, context compaction, multi-modal workflows. https://platform.claude.com/cookbook/
- **Anthropic ships Advisor Mode** — Use Opus for planning + Sonnet for grunt work in a single API call. 11.9% cost reduction per task. (2.9M views) https://x.com/claudeai/status/2042308622181339453

## Tools & Products
- **Claude Code Monitor** — Background script runner that tracks real-time dev events (server errors, failing tests, production launches); token-efficient because it only activates on events | https://x.com/noahzweben/status/2042332268450963774 | Effort: quick-win
- **Cursor Cloud Agents with PR screenshots/video** — AI-generated PRs automatically include demo videos and screenshots for visual review | https://x.com/cursor_ai/status/2042287192895267212 | Effort: quick-win
- **Archon (open-source)** — Harness builder for AI coding agents; define dev process (planning, implementation, code review, PRs) as YAML workflows | https://github.com/coleam00/Archon | Effort: weekend
- **LangChain auto-eval system (open-source)** — Runs evals on your agent, finds what's broken, fixes prompts automatically — no manual tuning | https://x.com/Vtrivedy10/status/2041927488918413589 | Effort: weekend
- **Claude Cookbook** — 50+ ready-to-use guides for building with Claude | https://platform.claude.com/cookbook/ | Effort: quick-win
- **NotebookLM + Claude Code bridge** — Offload research to NotebookLM to stretch Claude Code token limits | https://x.com/hooeem/status/2042293751805329445 | Effort: quick-win

## Techniques & Methods
- **Claude Code SessionStart hook** — Auto-load git status into Claude's context at session start by adding a hook to `.claude/settings.json`. Eliminates the need to manually run `git status` before every session. Code snippet in newsletter.
- **Plan → Execute → Review workflow** — Strict agentic coding workflow used by senior engineers with Claude Code: set up project context files, build automated validation loops, run parallel sub-agents. Tutorial: https://www.youtube.com/watch?v=MzhIr7BfpI0
- **Agentic Thinking vs. Reasoning** — Shift from "how long can it think?" to "can it execute effectively over multiple turns?" Agents use tools, read environment feedback, and pivot mid-task. Environments (browsers, terminals, API layers) are the new moat — not RL algorithms.
- **Advisor Mode pattern** — Use Opus for complex planning + Sonnet for execution in a single API call for 11.9% cost savings without quality loss.

## Research Papers
- **ConvApparel (Google)** — AI user simulators trained on actual human data (rather than instructions alone) become significantly more realistic and adaptable. Addresses the "unnaturally patient" flaw in today's simulators. | https://research.google/blog/convapparel-measuring-and-bridging-the-realism-gap-in-user-simulators/

## Industry Trends
- The "reasoning era" (o1, DeepSeek R1) is winding down; "agentic thinking" is the next wave — acting over multiple turns vs. monologue before speaking.
- Environments (browsers, terminals, API harnesses) are becoming their own startup category for training agents.
- Simply increasing test-time compute doesn't always yield better results — quality of environment and harness matters more.
- Claude Code file search is now 3x faster on massive codebases — enterprise-confirmed.
- Karpathy: a growing "AI capability understanding gap" between those paying $200/month professionally and casual users. (2M views)
- OpenAI's Chief Scientist: gap between intern-level AI and fully autonomous researcher is shorter than expected.

## Actionable Items
- [ ] Set up Claude Code Monitor for your dev server/test watcher using background scripts — *quick-win* — https://x.com/noahzweben/status/2042332268450963774 | action-2026-04-10-008
- [ ] Add SessionStart hook to `.claude/settings.json` to auto-load git context — *quick-win* — https://dev.to/holasoymalva/the-ultimate-claude-code-guide-every-hidden-trick-hack-and-power-feature-you-need-to-know-2l45 | action-2026-04-10-009
- [ ] Browse the Anthropic Claude Cookbook for ready-made agent patterns — *quick-win* — https://platform.claude.com/cookbook/ | action-2026-04-10-010
- [ ] Watch the senior SDE coding agent workflow tutorial — *quick-win* — https://www.youtube.com/watch?v=MzhIr7BfpI0 | action-2026-04-10-011
- [ ] Explore Archon for defining agent dev workflows as YAML — *weekend* — https://github.com/coleam00/Archon | action-2026-04-10-012
- [ ] Try LangChain's auto-eval agent optimizer on your current agent — *weekend* — https://x.com/Vtrivedy10/status/2041927488918413589 | action-2026-04-10-013

## Notable Links
- https://platform.claude.com/cookbook/ — Anthropic Claude Cookbook: 50+ agent building guides
- https://github.com/coleam00/Archon — Archon: YAML-based AI agent harness builder
- https://x.com/noahzweben/status/2042332268450963774 — Claude Code Monitor tool demo
- https://www.youtube.com/watch?v=MzhIr7BfpI0 — Senior SDE coding agent workflow tutorial
- https://justinlin610.github.io/blog/from-reasoning-to-agentic-thinking/ — Junyang Lin: From reasoning to agentic thinking
- https://research.google/blog/convapparel-measuring-and-bridging-the-realism-gap-in-user-simulators/ — Google ConvApparel paper
- https://codenewsletter.ai/p/anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan — Full newsletter web version
