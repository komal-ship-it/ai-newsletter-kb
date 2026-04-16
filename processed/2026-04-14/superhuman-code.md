# Superhuman — The Code — 2026-04-14

**Source:** thecode@mail.joinsuperhuman.ai
**Date:** 2026-04-14
**Original items:** 9

## Key Announcements
- **Cursor 3.1** — Tiled Agents Window for parallel multi-agent management in draggable panes; batch speech-to-text; branch selection for cloud agents; improved file search filters.
- **Vercel Open Agents** — Open-source template for deploying indefinitely-running cloud coding agents; built on Vercel AI SDK + Sandbox; zero timeouts, run hundreds at once.
- **Anthropic engineer publishes long-running agent harness design** — Prithvi Rajasekaran (Anthropic) documented planner + generator + skeptical evaluator harness pattern that prevents the "45-minute cliff" problem.

## Tools & Products
- **Cursor 3.1** — Multi-agent tiled window, side-by-side output comparison, batch speech-to-text | https://cursor.com/changelog/3-1 | Effort: quick-win
- **Vercel Open Agents** — Template for always-on cloud coding agents (zero timeout) | https://vercel.com/templates/template/open-agents | Effort: weekend
- **MarkItDown (Microsoft)** — Any file → clean Markdown for AI agents (PDFs, slides, audio) | https://github.com/microsoft/markitdown | Effort: quick-win
- **Plain (Python framework)** — Python web framework designed for humans and agents | https://github.com/dropseed/plain | Effort: weekend

## Techniques & Methods
- **Planner + Generator + Skeptical Evaluator harness** — Three-agent pattern for long-running tasks: Planner sets goals, Generator implements, Evaluator uses Playwright to test like a real user. Prevents "finished at 60%" problem. Cost: $200 / 6 hours for working game vs $9 / 20 min for broken game solo.
- **Claude Code stability settings** — Add to `~/.claude/settings.json`: `effortLevel: "high"`, disable 1M context, adaptive thinking, auto-memory; set subagent to Sonnet. Keeps context lean, improves reliability. Source: Kun Chen (ex-L8 Meta/Microsoft).
- **Pre-launch API key audit** — Checklist specifically covering API key exposure blind spots in vibe-coded apps.
- **Agent memory that learns** — Pattern for building agent memory that improves over runs (link: @akshay_pachaar).
- **Atomic skills training for coding agents** — Training agents on basic "atomic skills" (edit, navigate) significantly improves generalization. Paper: arxiv.org/abs/2604.05013

## Research Papers
- **Scaling coding agents via atomic skills** (arxiv.org/abs/2604.05013) — Training on atomic editing/navigation skills improves agents' ability to generalize to unseen coding challenges | https://arxiv.org/abs/2604.05013

## Industry Trends
- Multi-agent parallel execution becoming standard in IDE tooling (Cursor 3.1 tiled agents window)
- "45-minute cliff" documented: long-running agents degrade as context fills; structured harness is the fix
- Agent harness maintenance cost: patterns built for Opus 4.5 needed stripping for 4.6 — harnesses tied to model generation
- OpenAI internally treating Claude as primary competitive threat ("a religion" memo)

## Actionable Items
- [ ] Implement planner+generator+evaluator harness for next long-running Claude Code task — *weekend* — https://www.anthropic.com/engineering/harness-design-long-running-apps | action-2026-04-14-012
- [ ] Add Claude Code stability settings.json config to fix unstable behavior — *quick-win* — https://x.com/kunchenguid/status/2043511416448307378 | action-2026-04-14-013
- [ ] Try Vercel Open Agents template for deploying a persistent cloud coding agent — *weekend* — https://vercel.com/templates/template/open-agents | action-2026-04-14-014

## Notable Links
- https://www.anthropic.com/engineering/harness-design-long-running-apps — Anthropic: harness design for long-running apps
- https://cursor.com/changelog/3-1 — Cursor 3.1 release notes
- https://arxiv.org/abs/2604.05013 — Scaling coding agents via atomic skills (paper)
- https://x.com/_philschmid/status/2043705157850951699 — 8 tips for better agent skills from DeepMind engineer
- https://x.com/theo/status/2043611205856837680 — AI coding harness in 60 lines of Python
