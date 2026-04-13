# Superhuman — The Code — 2026-04-07

**Source:** thecode@mail.joinsuperhuman.ai
**Subject:** 👀 Strange things happening in AI
**Date:** 2026-04-07

## Raw Body

TODAY IN PROGRAMMING

OpenAI, Anthropic, and Google team up to fight model copying:
- Frontier Model Forum combats "adversarial distillation" — harvesting US model responses to build cheaper knockoffs
- OpenAI accused DeepSeek; Anthropic cut off access for Chinese-controlled firms after catching 3 labs
- US officials estimate this drains billions/year from Silicon Valley
Link: https://www.businesstimes.com.sg/international/global/openai-anthropic-google-unite-combat-model-copying-china

Anthropic secures massive compute expansion with Google and Broadcom:
- Multi-gigawatt deal for next-gen TPU capacity, go live 2027
- Run-rate revenue tripled since late 2025 to $30B
- Enterprise customers spending $1M+/year doubled to 1,000+ in just 2 months
Link: https://www.anthropic.com/news/google-broadcom-partnership-compute

Meta plans open-source versions of its next frontier models:
- Avocado (LLM) and Mango (image/video generator)
- Lighter versions with fewer features/parameters due to AI safety concerns
- Previous Bloomberg report said fully closed-source — plans changed
Link: https://siliconangle.com/2026/04/06/report-meta-developing-open-source-versions-upcoming-ai-models/

---

INSIGHT: The Claude Code leak proves harnesses are the next big thing — not models

$2.5B code dump: Anthropic accidentally leaked Claude Code's entire source code via npm update — 500K lines TypeScript.

Key finding: Claude Code's performance comes from engineering, not the underlying model.
- File history tracking to save context
- Specialized navigation tools
- Parallel agents for background tasks
- Sebastian Raschka: would get similar results using DeepSeek or Kimi with the same setup

The wrapper is the new winner:
- LangChain climbed to top 5 benchmarks by improving its harness
- Vercel saw better results by simplifying its agent's tools
- Competition has shifted from model quality to infrastructure quality

Blueprints aren't buildings: every competitor now has the map, but execution remains the hurdle.

dbreunig breakdown of how Claude Code builds system prompts: https://www.dbreunig.com/2026/04/04/how-claude-code-builds-a-system-prompt.html
Fortune article on leak: https://fortune.com/2026/03/31/anthropic-source-code-claude-code-data-leak-second-security-lapse-days-after-accidentally-revealing-mythos/

---

IN THE KNOW

- Faster RAG: Perplexity, Azure, HubSpot technique — 32x more memory efficient (with code): https://x.com/_avichawla/status/2040326889928356122
- External Brain: Build your own LLM knowledge base that compounds over time (Karpathy-inspired): https://x.com/hooeem/status/2041196025906418094
- Inside Codex: OpenAI's Head of DevRel goes behind the scenes on how Codex team ships: https://www.youtube.com/watch?v=9qXc-THAvc0
- Agent Anatomy: How to turn a stateless LLM into a production agent: https://x.com/akshay_pachaar/status/2041146899319971922
- Leaked Playbook: Claude Code system prompt construction breakdown: https://www.dbreunig.com/2026/04/04/how-claude-code-builds-a-system-prompt.html
- Docs as Files: Tool turns live docs into accessible filesystem for agents: https://x.com/arlanr/status/2041215978957389908
- OpenAI Safety Fellowship announced hours after New Yorker investigation revealed dissolved safety teams: https://x.com/RonanFarrow/status/2041224604878864514

Notable oddities:
- Someone built Indiana Jones-style whip for Claude Code: https://github.com/GitFrog1111/badclaude
- Milla Jovovich (actress) built agentic memory tool scoring 100% on LongMemEval: https://x.com/bensig/status/2041229266432733356

---

AI CODING HACK: Feed Claude Code skills real-time data using ! backtick syntax

Lydia Hallie (Claude Code team engineer) shared syntax to embed shell commands directly in SKILL.md files.

Example `.claude/skills/pr-summary/SKILL.md`:
```
---
name: pr-summary
description: Summarize changes in a pull request
---

- PR diff: !`gh pr diff`
- PR comments: !`gh pr view --comments`
- Changed files: !`gh pr diff --name-only`

Summarize this pull request...
```

Claude Code executes the commands and swaps in live output before processing.
Works with any shell command: test results, grep for TODOs, API responses.
Stick to read-only commands: cat, grep, gh pr view.
Source: https://x.com/lydiahallie/status/2034337963820327017

---

TOP & TRENDING RESOURCES

Top Tutorial: Build AI meeting assistant with Mastra TypeScript framework (Slack, Exa AI, Cal.com)
https://www.youtube.com/watch?v=pbAqx8B6NVc&t=876s

Top Repo: Graphify — turns folder of code/docs/papers/images into queryable knowledge graph
https://github.com/safishamsi/graphify

Trending Paper: Cursor warp decode — 1.8x faster inference on Blackwell GPUs
- Traditional MoE models waste processing around individual experts
- Warp decode assigns computing power directly to outputs, skips extra steps
https://cursor.com/blog/warp-decode

Newsletter URL: https://codenewsletter.ai/p/openai-anthropic-google-fight-model-copying-meta-goes-open-source
