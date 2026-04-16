# AI Tinkerers Post-Training — 2026-04-14

**Source:** post-training@mail.aitinkerers.org
**Subject:** ⚡ Autonomous Software Factories + Agentic Security
**Date:** 2026-04-14 (published Apr 15, covers Apr 13 builds)

---

⚡ Autonomous Software Factories + Agentic Security
April 13, 2026 — Joe Heitzeberg, Founder at AI Tinkerers

This week, builders shipped concrete systems — from autonomous software factories to LLM training pipelines.

---

## Top 5 Picks (April 13)

### 1. TOP PICK — Sundai Claw: Autonomous Software Factories
Nate Aune (CEO at Jazkarta) — AI Tinkerers Boston, Mar 30

Nate shared his "Dark Software Factory" journey while building Sundai Claw, an OpenClaw Telegram agent that takes a natural-language request and autonomously generates a Sundai project card, GitHub repo, spec doc, and deploys the app. He used OpenSpec to refine requirements, then Fabro.sh to orchestrate task graphs with branching, looping, quality gates, and human-in-the-loop checkpoints.

Tech Stack: OpenClaw, OpenSpec, Fabro, Google Cloud Run, Telegram
[Read more](https://sundai.club)

### 2. RUNNER UP — Agentic Trust and Security Verification
Will Sergeant (Cybersecurity Analyst at Harvard Medical School) — AI Tinkerers Boston, Mar 30

Will presented Agentic Highway's demo on agentic trust when tools started skipping permissions. The project maps AI execution artifacts through discovery and verification. KelvinClaw powers a modular, security-focused Rust agent framework.

Tech Stack: Python, NextJS
[agentichighway.ai](https://agentichighway.ai)

### 3. COMMUNITY FAVORITE — ATX: Automated Code Review Loop
Rohan Hasabe (Software Engineer at Esper.io) — AI Tinkerers Boston, Mar 30

Rohan demoed ATX (Agent Nexus), a CLI that hooks into Claude Code and creates a closed loop for continuous correction. ATX generates targeted "code review agents" based on your repo's key patterns, then iterates by feeding back specific fixes.

Tech Stack: Golang, Claude Code, AI agents, code review, local deployment
[iteration.sh](https://iteration.sh)

### 4. STANDOUT — DroneQRF: Predictive Drone Security Platform
Michael Lever (CTO at 24/7 Drone Force) — AI Tinkerers Johannesburg, Mar 31

Michael presented DroneQRF, a drone operations platform that lets pilots focus on flying while the system continuously fuses telemetry into predictive and prescriptive security intelligence. Demo normalized disparate streams (flight plans, alarm signals, LPR) into a unified threat scoring model.

Tech Stack: Node, Express, React, PostgreSQL, AWS EC2

### 5. NOTABLE — Nanochat: Train LLMs from Scratch
Sofie Van Landeghem (Open-source maintainer at OxyKodit) — AI Tinkerers Brussels, Apr 01

Sofie showed how nanochat trains your own LLM chat bot from scratch using Andrej Karpathy's minimal PyTorch harness. The repo implements the full loop: tokenization, pretraining, finetuning, evaluation, inference, plus a lightweight chat UI — designed to run on a single GPU or even CPU.

Tech Stack: Python, Torch, Transformers, Weights & Biases, LLM

---

## More Great Builds

- **TriCoach** (Wafaa Arbash): Triathlon training app with an AI coach that adapts to progress. Built with Claude Code, shipped on Vercel. [adaptive-race-coach.vercel.app](https://adaptive-race-coach.vercel.app)
- **CoChef** (Jayesh Gupta, InterSystems): AI kitchen copilot using Raspberry Pi + thermal and RGB cameras. Provides actionable spoken and on-screen guidance. [cochef.tech](https://cochef.tech)
- **Building Effective Agents** (Quinten Rosseel, ML6): Shared how to build effective agents with the Claude Agents SDK — turning chatty prompts into task-driven workflows.

---

## 🏆 Hackathon Spotlight — SundAI x Spring Epic Sprint 1.1.1 (Paris, Apr 5, 2026)

**Winner: Radar** — Automates the entire job search lifecycle by deploying autonomous agents that continuously monitor major platforms for real-time push notifications featuring instant ATS-optimized CV tailoring and browser-based form auto-filling.

**Winner: AlphaFounder by ajones.studio** — Automates the operational burden of early-stage startups by deploying isolated, per-founder OpenClaw agents on Fly.io that transform 2-minute voice recaps and financial data into polished investor updates and CRM pipelines.

---

## 💼 Top Job Match

[GTM AI Engineer](https://aitinkerers.org) — AZX, PBC | Remote | $70,000–$110,000
