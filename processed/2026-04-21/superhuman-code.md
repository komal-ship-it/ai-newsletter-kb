# Superhuman — The Code — 2026-04-21

**Source:** thecode@mail.joinsuperhuman.ai
**Date:** 2026-04-21
**Original items:** 9

## Key Announcements
- **Moonshot Kimi K2.6** — Open-source, trillion-parameter multimodal model; 300 sub-agents, 4,000 parallel steps, 13-hour autonomous coding runs; beats frontier models on Humanity's Last Exam.
- **Alibaba Qwen3.6-Max-Preview** — Top spot on six coding benchmarks; available on Qwen Studio now.
- **OpenAI Codex + Chronicle memory** — Uses screen context to fill in session context without re-explaining errors or open docs.
- **Token spend as vanity metric** — Meta's "Claudeonomics" leaderboard: 85,000 employees, 60 trillion tokens in 30 days. Employees leaving agents idle to climb rankings. Mirrors "lines of code" productivity theater.
- **Anthropic Opus 4.7 guide for Claude Code** — Official guide flagging settings most devs are missing.

## Tools & Products
- **Kimi K2.6** — Open-source, 1T-parameter multimodal; 300-agent orchestration, 4K parallel steps | https://www.kimi.com/blog/kimi-k2-6 | Effort: weekend
- **Qwen3.6-Max-Preview** — #1 on 6 coding benchmarks | https://qwen.ai/blog?id=qwen3.6-max-preview | Effort: quick-win
- **GenericAgent** — Lightweight AI agent framework, 3K lines of code, 5.3k stars | https://github.com/lsdefine/GenericAgent | Effort: weekend
- **/fewer-permission-prompts skill** — Boris Cherny (Claude Code creator): scans session history, finds safe bash/MCP commands, outputs allowlist to add to settings | Effort: quick-win

## Techniques & Methods
- **/fewer-permission-prompts** — Run this Claude Code skill to scan session history for permission-safe commands and add them to your allowlist, eliminating repetitive prompts.
- **Chronicle Context** — OpenAI Codex update: screen-based context injection so you stop re-explaining the codebase to the agent each session.

## Research Papers
- **Better AI models enable more ambitious work (Cursor)** — Better AI shifts developers from implementing known solutions to managing complex system-wide challenges. https://cursor.com/blog/better-models-ambitious-work

## Industry Trends
- Open-source model war heating up: Kimi K2.6 and Qwen3.6-Max both challenge closed frontier models on coding.
- Token spend gamification at Meta signals AI tooling adoption without ROI alignment — productivity theater 2.0.
- Google DeepMind strike team targeting Anthropic's coding lead; every major lab now treats coding as the frontier battleground.

## Actionable Items
- [ ] Run /fewer-permission-prompts to clean up Claude Code permission spam — *quick-win* — Built-in Claude Code skill, zero cost | action-2026-04-21-005
- [ ] Test Kimi K2.6 or Qwen3.6-Max-Preview on a complex multi-step coding task — *weekend* — Both open-source/free tier | action-2026-04-21-006
- [ ] Watch veteran engineer build from scratch with Claude — *quick-win* — https://www.youtube.com/live/K-mA3MZ_EzU | action-2026-04-21-007

## Notable Links
- https://www.kimi.com/blog/kimi-k2-6 — Kimi K2.6 launch post
- https://qwen.ai/blog?id=qwen3.6-max-preview — Qwen3.6-Max-Preview
- https://github.com/lsdefine/GenericAgent — GenericAgent framework
- https://cursor.com/blog/better-models-ambitious-work — Better models, more ambitious work (Cursor research)
- https://www.youtube.com/live/K-mA3MZ_EzU — Veteran engineer builds from scratch with Claude
- https://codenewsletter.ai/p/moonshot-drops-kimi-k2-6-openai-expands-codex-memory-with-chronicle — Full issue
