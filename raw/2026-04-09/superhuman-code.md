# Superhuman — The Code — Raw — 2026-04-09

**Message ID:** 19d728c309fe53af
**Subject:** 👀 Anthropic simplifies building Agents
**From:** thecode@mail.joinsuperhuman.ai
**Date:** 2026-04-09T14:01:21+00:00

---

Welcome back. Anthropic has shipped over 75 updates in 60 days. And they're at it again. They just dropped Claude Managed Agents, and it changes how you'll build agents from here.

Also: How to learn LLMs the way engineers need to, build iOS apps with Codex, and why Postman's founder wants you to rethink your engineering team.

Today's Insights:
- Powerful new updates and hacks for devs
- Open-source becomes the primary choice for agents
- How to fix Claude Code's thinking regression
- Trending social posts, top repos, and more

---

### TODAY IN PROGRAMMING

Anthropic ships a faster way to build production agents: The AI lab just unveiled Claude Managed Agents, a suite of APIs designed to cut months of infrastructure work down to days. Developers define their agents' tasks and tools while Anthropic handles sandboxing, orchestration, and permissions on its cloud. Early adopters like Notion and Asana are already using it to ship coding agents, AI teammates, and enterprise workflows.

Meta launches its first model from Superintelligence Labs: The social media giant just dropped Muse Spark, a multimodal AI model that excels at vision, reasoning, and agent workflows. Its key feature is Contemplating mode, which runs multiple agents in parallel to solve complex problems without increasing latency. Meta claims their updated training stack matches the performance of Llama 4 Maverick while using 10x less compute.

Cursor teaches Bugbot to improve itself: The AI coding startup just upgraded its code reviewer with the ability to learn on the job. Bugbot now tracks how developers interact with its suggestions by analyzing reactions, replies, and reviewer comments to refine its future rules. With over 110K repos already using the feature, Bugbot has generated more than 44K rules, pushing its resolution rate to nearly 80%, well ahead of competitors.

---

### INSIGHT: How open-source became the primary choice for agents

Apps are no longer the most valuable part of software. Mitchell Hashimoto, the founder of HashiCorp, spent 18 months building Ghostty, a terminal emulator that hit roughly one million daily users on macOS. Then he open-sourced its core as a library called libghostty, and that library reached millions of daily users in two months. The library outran the app because AI agents could plug it directly into new projects.

Agents prioritize open-source by default. Independent research labs have found that AI coding agents consistently reach for open-source, free components over commercial alternatives. Agents aren't great at building things from scratch, but they're very good at snapping together well-documented building blocks. Which means the individual components you ship are starting to matter more than the finished product built on top of them.

More assembly, more risk. All that agent-assembled software comes with trade-offs: new security vulnerabilities, instability, and developers who don't fully understand the systems they've stitched together.

What's next? Big, full-featured apps aren't going away, but they're getting more specialized. The "building block" layer of the ecosystem is now handling R&D and niche use cases on autopilot. If you're deciding where to put engineering resources, the leverage has shifted downstream toward foundational tools. Ship primitives, not just products.

---

### WHAT'S TRENDING

- Project Glasswing: Anthropic is using an unreleased Claude model to hunt vulnerabilities in critical open-source software before attackers do.
- iOS Shortcut: Building iOS apps with Codex has been painful because agents don't know Xcode. This skill fixes that.
- LLM Guide: Skip the academic papers. This guide teaches LLMs the way engineers actually need to learn them: build, optimize, deploy.
- Agent Ready: Your coding agents are only as good as the environment they run in. A Cursor engineer shares the playbook for getting out of the loop.
- Org Overhaul: Postman's founder just dropped his blueprint for engineering teams in the AI era.
- YC's Youngest: Y Combinator just named its youngest General Partner ever — a 25-year-old who dropped out at 15 and built a $700M company along the way.

---

### AI CODING HACK: How to fix Claude Code's thinking regression

If Claude Code feels like it is losing its edge, you are not imagining it. After analyzing over 17,000 thinking blocks, an AMD engineer found that the tool is under-allocating reasoning for complex tasks. Instead of performing a deep analysis, Claude is skipping ahead and trying to edit code before fully processing it. Three fixes:

1. The fastest: run "/effort high" in Claude Code.
2. Use "/effort max" on Opus for hard debugging. Then drop this snippet into your "~/.claude/settings.json" file: "showThinkingSummaries": true
3. Add this to your CLAUDE.md: "Research the codebase before editing. Never change code you haven't read."

If you want to bypass adaptive thinking entirely: CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1

---

### TOP & TRENDING RESOURCES

Top Tutorial: How to build self-evolving agent memory - This tutorial shows devs how to create a self-evolving memory system for Claude Code, built after Andrej Karpathy's knowledge base architecture. You'll learn to use hooks to automatically capture and summarize coding sessions into an Obsidian vault, giving your AI agent long-term memory that evolves alongside your codebase.

Top Repo: Andrej-karpathy-skills - CLAUDE.md file designed to optimize Claude Code performance by incorporating Andrej Karpathy's observations on LLM coding pitfalls.

Trending Paper: How LLMs follow instructions - The research investigates whether AI models rely on a single, universal process to follow instructions. Rather than relying on a single process, models dynamically coordinate diverse, specialized language skills to satisfy specific rules.
