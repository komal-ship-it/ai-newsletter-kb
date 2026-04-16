# Daily Digest — 2026-04-14

## Consensus Signals
- **Multi-agent parallel execution is the new default** — Covered by Superhuman Code (Cursor 3.1 tiled Agents Window), AI Tinkerers (Sundai Claw, ATX closed-loop review). Running a single agent is giving way to fleets of specialized agents working in parallel. Both IDE tooling and CLI tooling shipped this week.
- **Long-running agents need structured harnesses** — Covered by Superhuman Code, AI Tinkerers. Anthropic documented the "45-minute cliff" problem (agents declare "finished" at 60%). Fix: planner + generator + skeptical evaluator with real user testing (Playwright). ATX implements a similar loop for code review.
- **OpenAI-Microsoft relationship fractured** — Covered by TLDR. Leaked memo explicitly says Microsoft partnership "limited our ability" to reach enterprise clients. Amazon alliance is the new growth engine. Enterprise = 40% of OpenAI revenue.
- **AI democratizing company formation** — Covered by AI Collective (The Default State essay). 1-in-3 US adults planning business in 2026 (+94% YoY). 65% plan to use AI. This is structural, not a trend.

## Contrarian Takes
- **Agent harness maintenance cost is real** — Superhuman Code: patterns built for Opus 4.5 had to be stripped for 4.6. Harnesses are built on model-specific limitations that become obsolete each generation. The "fix" has a maintenance tax.
- **Fake GitHub stars undermine AI repo signal** — TLDR (covered Apr 15): 6M fake stars across 18K+ repos; AI/LLM repos are the biggest non-malicious category. GitHub stars as a quality signal are unreliable for the exact repos most builders rely on.

## Top 3 Actionable Items
1. Add Claude Code stability settings.json config — *quick-win* — Immediately improves context management and reliability: disable 1M context, adaptive thinking, auto-memory; set subagent to Sonnet. https://x.com/kunchenguid/status/2043511416448307378
2. Install MarkItDown for AI-ready document pipelines — *quick-win* — Convert PDFs, slides, audio, docs to clean Markdown; drops directly into any AI workflow. https://github.com/microsoft/markitdown
3. Implement planner+generator+evaluator harness for the next long-running task — *weekend* — Playwright-based evaluator tests like a real user; prevents 45-minute cliff failure mode. https://www.anthropic.com/engineering/harness-design-long-running-apps

## Urgent / Time-Sensitive
- None today.

## One-Line Summary
Multi-agent parallel execution went from experimental to shipping across every major dev tool while Anthropic published the harness design that prevents agents from quitting at 60% completion.
