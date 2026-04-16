# AI Tinkerers Post-Training — 2026-04-14

**Source:** post-training@mail.aitinkerers.org
**Date:** 2026-04-14
**Original items:** 8 (5 picks + 3 more builds + 2 hackathon winners)

## Key Announcements
- **ATX (Agent Nexus) CLI** — Hooks into Claude Code; generates code-review agents from repo patterns, creates a closed loop for continuous correction.
- **Sundai Claw** — OpenClaw Telegram agent that takes a natural-language request and autonomously generates GitHub repo, spec doc, and deploys app via Fabro.sh task graphs.
- **Hackathon winner: Radar** — Automates job search lifecycle with agents: real-time job monitoring + ATS-optimized CV tailoring + auto form-filling.

## Tools & Products
- **ATX (Agent Nexus)** — CLI for automated code review loop with Claude Code; uses repo-pattern-derived review agents | https://iteration.sh | Effort: weekend
- **Sundai Claw** — NL-to-deployed-app agent via OpenClaw + Fabro.sh orchestration | https://sundai.club | Effort: major
- **Fabro.sh** — Task graph orchestrator with branching, looping, quality gates, human-in-the-loop checkpoints | https://fabro.sh | Effort: weekend
- **Nanochat** — Train your own LLM from scratch (Karpathy harness): tokenization, pretraining, finetuning, eval, inference, chat UI; single GPU or CPU | https://github.com | Effort: major
- **Agentic Highway** — Modular security-focused Rust agent framework (KelvinClaw); maps AI execution artifacts for trust verification | https://agentichighway.ai | Effort: major
- **TriCoach** — AI triathlon coach adapting to athlete progress; built with Claude Code on Vercel | https://adaptive-race-coach.vercel.app | Effort: weekend
- **CoChef** — AI kitchen copilot with Raspberry Pi + thermal/RGB cameras; spoken + on-screen guidance | https://cochef.tech | Effort: major

## Techniques & Methods
- **Dark Software Factory pattern** — Natural-language → OpenSpec (spec refinement) → Fabro.sh (task graph with quality gates + HITL) → deployed app. Key: explicit quality gates and human-in-the-loop checkpoints prevent silent failures.
- **Closed-Loop Code Review via Agents** — ATX pattern: generate review agents from your repo's key patterns → apply fix suggestions → re-run review → iterate. Continuous quality loop without human review per cycle.
- **Agentic Trust Verification** — Map AI execution artifacts through discovery + verification stages. KelvinClaw Rust framework: intercept and audit agent tool calls at the framework level.
- **Minimal LLM Training (Karpathy harness)** — Full training loop (tokenization → pretraining → finetuning → eval → inference) runnable on single GPU or CPU. Nanochat implementation.

## Research Papers
- **Scaling coding agents via atomic skills** — By training on basic "atomic skills" (editing, navigation), agents significantly improve generalization to unseen coding tasks. (arxiv.org/abs/2604.05013 — covered in Superhuman Code same day)

## Industry Trends
- "Autonomous software factory" pattern maturing: NL spec → deployed app without human coding steps
- Agentic security emerging as a distinct discipline: trust verification, permission auditing, execution artifact mapping
- Community hackathons producing production-quality agentic tools (Radar, AlphaFounder)

## Actionable Items
- [ ] Try ATX CLI to add a continuous code-review loop to a Claude Code project — *weekend* — https://iteration.sh | action-2026-04-14-010
- [ ] Explore Fabro.sh for orchestrating multi-step agent task graphs with quality gates — *weekend* — https://fabro.sh | action-2026-04-14-011

## Notable Links
- https://sundai.club — Sundai Claw: autonomous software factory
- https://agentichighway.ai — Agentic Highway: trust and security verification framework
- https://iteration.sh — ATX: automated code review loop for Claude Code
- https://cochef.tech — CoChef: AI kitchen copilot with computer vision
- https://adaptive-race-coach.vercel.app — TriCoach: AI triathlon training (Claude Code built)
