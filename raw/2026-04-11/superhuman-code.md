# Superhuman — The Code (raw) — 2026-04-07

**Source:** thecode@mail.joinsuperhuman.ai
**Subject:** OpenAI, Anthropic & Google Fight Over Model Copying — Meta Goes Open Source
**Date:** 2026-04-07
**Message-ID:** (truncated in retrieval — beginning of body was cut off)
**URL:** https://codenewsletter.ai/p/openai-anthropic-google-fight-model-copying-meta-goes-open-source
**Note:** The first portion of this newsletter body was not captured. Content below begins mid-article.

---

using DeepSeek or Kimi with the same setup.

**The wrapper is the new winner.** Others have already proven this. LangChain [**climbed**](https://blog.langchain.com/the-anatomy-of-an-agent-harness/) to the top five on benchmarks just by improving its harness, while Vercel saw better results by simplifying its agent's tools. The real competition has shifted from model quality to the quality of the surrounding infrastructure.

**Blueprints aren't buildings.** While every competitor now has the map to a multi-billion dollar product, execution remains the hurdle. Knowing how the architecture works and actually scaling it for production are two completely different challenges.

## **What's trending on socials and headlines**

* **Faster RAG:** How Perplexity, Azure, and HubSpot use a **[simple technique](https://x.com/_avichawla/status/2040326889928356122)** to make RAG 32x more memory efficient (explained with code).

* **External Brain:** Inspired by Andrej Karpathy, this thread **[walks you](https://x.com/hooeem/status/2041196025906418094)** through building your own LLM knowledge base that compounds over time.

* **Inside Codex:** OpenAI's Head of DevRel and Codex product lead go [**behind the scenes**](https://www.youtube.com/watch?v=9qXc-THAvc0) on how the team actually ships products.

* **Agent Anatomy:** When your AI agent fails, the problem is rarely the model. This [deep dive](https://x.com/akshay_pachaar/status/2041146899319971922) shows how to turn a stateless LLM into a production agent.

* **Leaked Playbook:** Claude Code's source code was accidentally leaked, and here's a [**breakdown**](https://www.dbreunig.com/2026/04/04/how-claude-code-builds-a-system-prompt.html) of how it constructs system prompts.

* **Docs as Files:** Most AI code fails when docs change. This tool turns live documentation into an accessible [filesystem](https://x.com/arlanr/status/2041215978957389908) that agents can browse.

* **Perfect Timing:** OpenAI announced a new Safety Fellowship, hours after a New Yorker investigation revealed it had [**dissolved**](https://x.com/RonanFarrow/status/2041224604878864514) its safety teams.

## **How to feed Claude Code skills real-time data**

Claude Code skills are normally static, which usually means tedious manual copy-pasting for PR diffs or logs. Lydia Hallie, an engineer on the Claude Code team, recently [shared](https://x.com/lydiahallie/status/2034337963820327017) a much better way: use the `!` backtick syntax to embed shell commands directly into your `SKILL.md`.

Claude Code will execute the commands and swap in the live output automatically before processing. To get started, create this file at `.claude/skills/pr-summary/SKILL.md`:

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

This syntax works with any shell command, allowing you to pull in test results, grep for TODOs, or fetch API responses automatically. To prevent accidental state changes, stick to read-only commands like `cat`, `grep`, and `gh pr view`.

https://codenewsletter.ai/p/openai-anthropic-google-fight-model-copying-meta-goes-open-source
