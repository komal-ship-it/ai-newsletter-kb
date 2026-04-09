# Superhuman — The Code (raw) — 2026-04-07

**Source:** thecode@mail.joinsuperhuman.ai
**Subject:** 👀 Strange things happening in AI
**Message ID:** 19d6840035018ea4

---

Welcome back. The number of strange things happening in AI is ridiculous. Yesterday, someone built an actual Indiana Jones-style whip for Claude Code. And today, Milla Jovovich announced that she has built an agentic memory tool that scored 100% on LongMemEval.

Also: How to make RAG 32x more memory efficient, building self-improving LLM knowledge bases, and a look at how OpenAI's Codex team actually ships.

TODAY'S INSIGHTS
- Powerful new updates and hacks for devs
- Why Claude Code's real edge was never the model
- How to feed Claude Code skills real-time data
- Trending social posts, top repos, and more

TODAY IN PROGRAMMING

OpenAI, Anthropic, and Google team up to fight model copying:
These three AI rivals are teaming up through the Frontier Model Forum to combat "adversarial distillation" — a process where unauthorized users harvest responses from US models to build cheaper knockoffs. OpenAI has accused DeepSeek of piggybacking on its tech, while Anthropic has already cut off access for Chinese-controlled firms after catching three labs doing just that. US officials estimate this practice drains billions of dollars from Silicon Valley labs every year.

Anthropic secures massive compute expansion with Google and Broadcom:
The AI lab recently landed a multi-gigawatt deal for next-gen TPU capacity, set to go live in 2027. This marks the company's largest compute commitment to date, fueled by explosive growth: run-rate revenue has tripled since late 2025 to $30B, while the number of enterprise customers spending over $1M annually has doubled to more than 1,000 in just two months.

Meta plans open-source versions of its next frontier models:
Meta is working on open-source versions of its next two proprietary models, codenamed Avocado (an LLM) and Mango (an image and video generator). These open-source editions will likely be lighter versions with fewer features or parameters, partly due to AI safety concerns.

INSIGHT: The Claude Code leak proves harnesses are the next big thing — not models

The $2.5B code dump: Last week, Anthropic accidentally leaked Claude Code's entire source code via an npm update, exposing half a million lines of TypeScript. But the leak revealed a bigger truth: the model isn't the secret sauce.

Plumbing beats parameters: ML researchers found that Claude Code's performance comes from its engineering, not just the underlying model. It relies on smart features like file history tracking to save context, specialized navigation tools, and parallel agents for background tasks. You'd likely get similar results using DeepSeek or Kimi with the same setup.

The wrapper is the new winner: LangChain climbed to the top five on benchmarks just by improving its harness, while Vercel saw better results by simplifying its agent's tools. The real competition has shifted from model quality to the quality of the surrounding infrastructure.

WHAT'S TRENDING
- Faster RAG: How Perplexity, Azure, and HubSpot use a simple technique to make RAG 32x more memory efficient (explained with code).
- External Brain: Building your own LLM knowledge base that compounds over time, inspired by Andrej Karpathy.
- Inside Codex: OpenAI's Head of DevRel and Codex product lead go behind the scenes on how the team actually ships products.
- Agent Anatomy: When your AI agent fails, the problem is rarely the model — how to turn a stateless LLM into a production agent.
- Leaked Playbook: A breakdown of how Claude Code constructs system prompts from its accidentally leaked source code.
- Perfect Timing: OpenAI announced a new Safety Fellowship, hours after a New Yorker investigation revealed it had dissolved its safety teams.

AI CODING HACK: How to feed Claude Code skills real-time data

Claude Code skills are normally static. Lydia Hallie, an engineer on the Claude Code team, shared a better way: use the `!` backtick syntax to embed shell commands directly into your SKILL.md. Claude Code will execute the commands and swap in the live output automatically before processing. Example for a PR summary skill:

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

This syntax works with any shell command, allowing you to pull in test results, grep for TODOs, or fetch API responses automatically.

TOP RESOURCES
- Top Tutorial: How to build your own AI agent from scratch using the Mastra TypeScript framework, integrating Slack, Exa AI, and Cal.com.
- Top Repo: Graphify — turns any folder of code, docs, papers, or images into a queryable knowledge graph.
- Trending Paper: Cursor doubles AI coding speed on Blackwell GPUs with warp decode, making inference 1.8x faster.
