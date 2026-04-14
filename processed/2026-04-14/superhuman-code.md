# Superhuman — The Code — 2026-04-14

**Source:** thecode@mail.joinsuperhuman.ai
**Date:** 2026-04-14
**Original items:** 10

## Key Announcements
- **MiniMax M2.7 open-weight release** — 230B-parameter model on Hugging Face; runs locally on 128GB RAM. Benchmarks: SWE-Pro 56.22%, Terminal Bench 2 57.0% (competitive with top closed models).
- **MMX-CLI** — MiniMax CLI giving agents native image/video/voice/search access; no MCP configuration needed.
- **Claude Code quality decline (AMD report)** — AMD's senior director published metrics from ~7,000 sessions: reasoning length dropped 67%, API requests up 80x since February. Anthropic confirmed they reduced default thinking effort from high to medium to cut token costs.
- **Apple smart glasses** — Testing 4 frame styles for 2027 launch; no display, camera/calls/music/Siri focus.
- **OpenAI Codex internal usage** — OpenAI shared how their team uses Codex internally; Meta staff engineer tutorial on Codex workflows.

## Tools & Products
- **MiniMax M2.7** — Open-weight 230B coding model for local deployment | https://huggingface.co/MiniMaxAI/MiniMax-M2.7 | 128GB RAM required | Effort: major
- **MMX-CLI** — MiniMax CLI with native multimodal + search, no MCP needed | https://x.com/MiniMax_AI/status/2042641521653256234 | Effort: quick-win
- **Agent Reach** — Single-command scraping from Twitter/Reddit for agents | https://github.com/Panniantong/Agent-Reach/blob/main/docs/README_en.md | Effort: weekend
- **Claude Code `!` dynamic commands** — Prefix shell command with `!` in .claude/commands/*.md to inject live output as context at command execution time | Effort: quick-win
- **5 Claude Code iOS skill packs** — Skill packs for iOS development | https://x.com/PaulSolt/status/2042716870512353294 | Effort: quick-win

## Techniques & Methods
- **Dynamic Claude Code slash commands** — Add `!` before a shell command in a .claude/commands/*.md file; Claude executes the shell command first and injects the output as live context. Example `!gh pr diff` in a pr-summary command pulls the current PR diff automatically. Full example shared by Theo Browne | https://x.com/theo/status/2043103001121034581
- **TDD with AI agents (Oracle approach)** — Ex-Oracle Director of Engineering demonstrates test-first methodology in Claude Code; write tests before implementation for better agent-generated code | https://www.youtube.com/watch?v=Kx7bAwVH_1c
- **Git worktrees for parallel agent tasks** — Meta staff engineer's Codex guide covers managing parallel tasks with git worktrees in AI coding workflows | https://www.youtube.com/watch?v=nQFtsehu7h0
- **Megatron for reliable LLM training at scale** — Despite five overlapping frameworks, NVIDIA's Megatron is currently most reliable for large-scale LLM training; PyTorch native stack has gradient explosion issues at 1K steps | https://www.baseten.co/blog/open-source-llm-training-is-a-mess-here-is-how-it-all-works/

## Research Papers
- **Single-agent LLMs vs. Multi-agent systems** — When compute is equalized, single agents often match or outperform multi-agent systems on complex reasoning tasks | https://arxiv.org/abs/2604.02460

## Industry Trends
- Open-weight models reaching near-closed-model performance (MiniMax M2.7 competitive on SWE-bench)
- Claude Code quality degradation as Anthropic optimizes for cost: community backlash documented with 7K-session data
- LLM training ecosystem fragmented (5 overlapping frameworks); NVIDIA Megatron most reliable at scale
- Enterprise LLM market projected at $5.9B in 2026
- AI-generated code reshaping security hiring criteria (Box CEO: shift in who gets hired)
- Open-weight models with no-MCP CLI tooling reducing deployment friction significantly

## Actionable Items
- [ ] Implement dynamic Claude Code slash commands using `!` shell prefix — *quick-win* — Follow Theo's pr-summary example: https://x.com/theo/status/2043103001121034581 | action-2026-04-14-012
- [ ] Try MMX-CLI for multimodal agent workflows without MCP setup — *quick-win* — https://x.com/MiniMax_AI/status/2042641521653256234 | action-2026-04-14-013
- [ ] Read single-agent vs multi-agent research paper — *quick-win* — https://arxiv.org/abs/2604.02460 | action-2026-04-14-014
- [ ] Watch Meta staff engineer's Codex guide (git worktrees + agents.md) — *quick-win* — https://www.youtube.com/watch?v=nQFtsehu7h0 | action-2026-04-14-015
- [ ] Explore 5 Claude Code iOS skill packs — *quick-win* — https://x.com/PaulSolt/status/2042716870512353294 | action-2026-04-14-016

## Notable Links
- https://github.com/anthropics/claude-code/issues/42796 — AMD director's Claude Code quality metrics (7K sessions; 67% shorter reasoning)
- https://www.baseten.co/blog/open-source-llm-training-is-a-mess-here-is-how-it-all-works/ — LLM training framework landscape deep dive
- https://arxiv.org/abs/2604.02460 — Single vs multi-agent LLMs research paper
- https://www.youtube.com/watch?v=Kx7bAwVH_1c — TDD with Claude Code (Oracle director)
- https://github.com/Panniantong/Agent-Reach/blob/main/docs/README_en.md — Agent Reach social scraping repo
- https://x.com/marmaduke091/status/2043382991901147158 — Leaked Claude app builder feature (2.7M views)
