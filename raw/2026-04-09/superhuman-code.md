# Superhuman Code — Raw — 2026-04-09

**Message ID:** 19d728c309fe53af
**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Subject:** 👀 Anthropic simplifies building Agents

Welcome back. Anthropic has shipped over 75 updates in 60 days. They just dropped Claude Managed Agents, and it changes how you'll build agents from here.

Also: How to learn LLMs the way engineers need to, build iOS apps with Codex, and why Postman's founder wants you to rethink your engineering team.

Today's Insights:
* Powerful new updates and hacks for devs
* Open-source becomes the primary choice for agents
* How to fix Claude Code's thinking regression
* Trending social posts, top repos, and more

---

## TODAY IN PROGRAMMING

### Anthropic ships a faster way to build production agents

The AI lab unveiled Claude Managed Agents (https://claude.com/blog/claude-managed-agents), a suite of APIs designed to cut months of infrastructure work down to days. Developers define their agents' tasks and tools while Anthropic handles sandboxing, orchestration, and permissions on its cloud. Early adopters like Notion and Asana are already using it to ship coding agents, AI teammates, and enterprise workflows.
Watch how Notion uses it: https://www.youtube.com/watch?v=45hPRdfDEsI&t=9s

### Meta launches its first model from Superintelligence Labs

Meta dropped Muse Spark (https://ai.meta.com/blog/introducing-muse-spark-msl), a multimodal AI model that excels at vision, reasoning, and agent workflows. Key feature: Contemplating mode, which runs multiple agents in parallel to solve complex problems without increasing latency. Meta claims their updated training stack matches the performance of Llama 4 Maverick while using 10x less compute.
Try it: https://meta.ai/

### Cursor teaches Bugbot to improve itself

Cursor upgraded (https://cursor.com/blog/bugbot-learning) its code reviewer with the ability to learn on the job. Bugbot now tracks how developers interact with its suggestions — analyzing reactions, replies, and reviewer comments to refine its future rules. With over 110K repos already using the feature, Bugbot has generated more than 44K rules, pushing its resolution rate to nearly 80%.

---

## SPONSOR: MongoDB AI Learning Hub

Technical training pathways for AI app-building — practical guides, tutorials, and quick starts for all skill levels, covering RAG, MongoDB Vector Search, and LLM optimization.
https://fandf.co/41l1KsP

---

## INSIGHT: How open-source became the primary choice for agents

**Apps are no longer the most valuable part of software.** Mitchell Hashimoto (founder of HashiCorp) spent 18 months building Ghostty, a terminal emulator that hit ~1 million daily users on macOS. Then he open-sourced its core as a library called libghostty, and that library reached millions of daily users in two months. The library outran the app because AI agents could plug it directly into new projects.

**Agents prioritize open-source by default.** Independent research labs have found that AI coding agents consistently reach for open-source, free components over commercial alternatives. Agents are very good at snapping together well-documented building blocks. Individual components you ship are starting to matter more than the finished product.

**More assembly, more risk.** Agent-assembled software comes with trade-offs: new security vulnerabilities, instability, and developers who don't fully understand the systems they've stitched together. Hashimoto built a trust-gating tool specifically to filter out unreliable dependencies: https://github.com/mitchellh/vouch

**What's next?** The "building block" layer of the ecosystem is now handling R&D and niche use cases on autopilot. If you're deciding where to put engineering resources, the leverage has shifted downstream toward foundational tools. Ship primitives, not just products.

---

## WHAT'S TRENDING

* **Project Glasswing:** Anthropic is using an unreleased Claude model to hunt vulnerabilities in critical open-source software before attackers do.
  https://x.com/AnthropicAI/status/2041578392852517128

* **iOS Shortcut:** Building iOS apps with Codex has been painful because agents don't know Xcode. This skill fixes that.
  https://x.com/PaulSolt/status/2041643862913949929

* **LLM Guide:** Skip the academic papers. This guide teaches LLMs the way engineers need to learn them: build, optimize, deploy.
  https://x.com/kmeanskaran/status/2040651169744535722

* **Agent Ready:** Your coding agents are only as good as the environment they run in. A Cursor engineer shares the playbook for getting out of the loop.
  https://x.com/ericzakariasson/status/2041897427431563613

* **Org Overhaul:** Postman's founder dropped his blueprint for engineering teams in the AI era.
  https://x.com/ivanburazin/status/2041199368296931595

* **Exit Interview:** Conversation between a CEO and manager explaining why best engineers quit (1.5M views).
  https://x.com/javarevisited/status/2040802388462928308

* **YC's Youngest:** Y Combinator named its youngest General Partner ever — a 25-year-old who dropped out at 15 and built a $700M company.
  https://x.com/gjarrosson/status/2041888014574743577

---

## AI CODING HACK: How to fix Claude Code's thinking regression

Claude Code is under-allocating reasoning for complex tasks — skipping ahead and trying to edit code before fully processing it. After analyzing over 17,000 thinking blocks, an AMD engineer surfaced this issue. Three fixes from AI PM Paweł Huryn:

1. Run **/effort high** in Claude Code (fastest fix).
2. Use **/effort max** on Opus for hard debugging. Add this to `~/.claude/settings.json` to see Claude's reasoning in real time:
   ```
   "showThinkingSummaries": true
   ```
3. Add this to your CLAUDE.md: "Research the codebase before editing. Never change code you haven't read."

Nuclear option to bypass adaptive thinking entirely:
```
CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1
```

Source: https://github.com/anthropics/claude-code/issues/42796
Paweł's post: https://x.com/PawelHuryn/status/2041418614557802747

---

## TOP & TRENDING RESOURCES

### Top Tutorial
**How to build self-evolving agent memory:** Tutorial showing devs how to create a self-evolving memory system for Claude Code, built after Andrej Karpathy's knowledge base architecture. Uses hooks to automatically capture and summarize coding sessions into an Obsidian vault, giving your AI agent long-term memory that evolves alongside your codebase.
https://www.youtube.com/watch?v=7huCP6RkcY4

### Top Repo
**Andrej-karpathy-skills:** CLAUDE.md file designed to optimize Claude Code performance by incorporating Andrej Karpathy's observations on LLM coding pitfalls.
https://github.com/forrestchang/andrej-karpathy-skills

### Trending Paper
**How LLMs follow instructions:** Research investigating whether AI models rely on a single, universal process to follow instructions. Rather than one process, models dynamically coordinate diverse, specialized language skills to satisfy specific rules.
https://arxiv.org/abs/2604.06015

---

Until next time — The Code team
Online version: https://codenewsletter.ai/p/anthropic-introduces-claude-managed-agents-meta-drops-muse-spark
