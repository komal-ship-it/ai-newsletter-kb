# Superhuman (The Code) — 2026-04-17

**Source:** thecode@mail.joinsuperhuman.ai
**Date:** 2026-04-17
**Original items:** 8

## Key Announcements
- **Claude Opus 4.7 released** — Designed for complex engineering with minimal oversight; more rigorous on long-running workflows; self-verifies before finishing; vision now supports 3x previous resolution; API pricing $5/$25 per million tokens; "Mythos" (more powerful model) still held back for safety reasons
- **OpenAI Codex major upgrade** — Can see, click, and type across Mac; multiple parallel agents; in-app browser for frontend comments; image generation via gpt-image-1.5; persistent memory; 90+ new plugins
- **Alibaba Qwen3.6-35B-A3B** — Mixture-of-experts: 35B total params, only 3B active at inference; outperforms dense Qwen3.5-27B in coding; rivals Claude Sonnet 4.5 in multimodal tasks

## Tools & Products
- **Claude Opus 4.7** — Long-running agentic tasks, minimal oversight, self-verification, 3x vision resolution | api.anthropic.com | Effort: quick-win
- **HyperFrames (HeyGen)** — Generate AI videos from HTML/CSS/JS; agent-first non-interactive CLI | GitHub | Effort: weekend
- **Qwen3.6-35B-A3B (Alibaba)** — Lightweight MoE coding agent model; only 3B active params | Hugging Face | Effort: weekend

## Techniques & Methods
- **Gemini Flex service tier** — Add `service_tier: "flex"` to Gemini `generate_content` config; 50% cost reduction by using spare capacity; 1-15 minute delay tradeoff; Flash-Lite at $0.125/M input tokens; ideal for batch jobs, background processing, nightly pipelines
- **5 agent coordination patterns** (Anthropic guide) — Start simplest; add complexity only when it breaks; key question: do agents need each other's work while in progress? Yes → shared state; No → keep independent; proven by Cursor + NVIDIA 38% CUDA speedup on Blackwell GPUs in 3 weeks using planner + workers via single markdown file
- **Claude Code hooks for code quality** — Intercept agent lifecycle; inject custom context; pre-tool hooks enforce linting and cleanup before any changes are saved

## Research Papers
- **Designing synthetic datasets for the real world** (Google/Simula) — Use reasoning models to systematically design entire synthetic datasets; structured high-quality generation heavily outperforms simpler baselines; addresses scarcity of real-world specialized training data

## Industry Trends
- AI labs paying hundreds of thousands for dead startups' Slack archives, Jira tickets, emails — data gold rush for proprietary workflow data
- Long Claude sessions degrade outputs — Anthropic engineer warns about context rot in extended sessions; use Continue, rewind, compact, clear, or subagent to manage
- Shopify CEO data shows first-time founders have the safer career path right now vs staying employed
- Meta acquiring founding engineers from Mira Murati's Thinking Machines Lab — talent war intensifying

## Actionable Items
- [ ] Use Gemini Flex tier for batch/background API jobs — add `service_tier: "flex"` for 50% cost reduction; 1-15 min delay — *quick-win* — one-line config change | action-2026-04-17-004
- [ ] Read Anthropic's 5 agent coordination patterns guide before designing next agent system — *quick-win* | action-2026-04-17-005
- [ ] Explore Claude Code hooks for pre-tool code quality enforcement — pre-tool hooks can lint before saving — *weekend* | action-2026-04-17-006
- [ ] Try HyperFrames for AI-generated video from HTML/CSS/JS — open source by HeyGen — *weekend* | action-2026-04-17-007
- [ ] Read the creator of Claude Code's 6 strategies for Opus 4.7 — 1.1M views — *quick-win* | action-2026-04-17-008

## Notable Links
- Anthropic guide: 5 agent coordination patterns
- Cursor + NVIDIA: 38% CUDA kernel speedup via multi-agent system in 3 weeks
- Anthropic engineer on context rot in long Claude sessions — "Continue, rewind, compact, clear, subagent" breakdown
