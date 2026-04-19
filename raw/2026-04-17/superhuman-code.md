# Superhuman (The Code) — Raw — 2026-04-17

**Source:** thecode@mail.joinsuperhuman.ai
**Message-ID:** 19d9bbfce208753e
**Date:** 2026-04-17

---

Welcome back. There's a new ceiling for agentic performance. Anthropic just dropped Opus 4.7 and it's also the stepping stone to Mythos, the more powerful model they're still keeping behind closed doors for safety reasons.

Also: How to build the right AI stack in 2026, six Claude Code team tips for mastering Opus 4.7 and find out why data from dead startups is now a goldmine for AI labs.

TODAY IN PROGRAMMING

Anthropic unveils Claude Opus 4.7 with powerful new tools for devs: The AI lab just dropped its latest flagship model, designed to tackle complex engineering tasks with minimal oversight. Opus 4.7 is more rigorous with long-running workflows, follows instructions with more accuracy, and self-verifies its work before finishing. Vision capabilities also got a major upgrade, now supporting images at over three times the previous resolution.

OpenAI arms devs with its most capable Codex upgrade: The team behind ChatGPT just gave its coding agent the ability to see, click, and type across your Mac, allowing multiple agents to run in parallel. A new in-app browser lets you leave comments directly on pages to streamline frontend development. This update also introduces image generation via gpt-image-1.5, persistent memory that remembers your preferences, and over 90 new plugins.

Alibaba drops a lean open model for coding agents: The Chinese tech giant released Qwen3.6-35B-A3B, a mixture-of-experts model that packs 35B total parameters but only uses 3B for inference. Even with its small footprint, it outperforms the dense Qwen3.5-27B in coding and rivals Claude Sonnet 4.5 in multimodal tasks.

INSIGHT: How to pick agent patterns that actually scale

The coordination gap. As AI agents handle more complex tasks, the question has shifted from whether you should use them to how you should orchestrate them. Anthropic recently published a guide breaking down five coordination patterns, and the pick depends on one thing: how much your agents need each other.

Sophistication backfires. Many teams over-engineer their setups by choosing patterns based on complexity rather than fit. Anthropic's advice is to start with the simplest option that could work and only add complexity when it breaks.

Proof is in the kernel. Cursor and NVIDIA recently showed what the right pattern choice looks like in practice. They pointed a multi-agent system at CUDA kernel optimizations for Blackwell GPUs, the kind of assembly-level tuning that normally takes specialized engineers months. A planner agent distributed and rebalanced work across autonomous workers, coordinated by a single markdown file. Three weeks later, the system delivered a 38% speedup.

Before you build. Ask whether your agents need each other's work while it's still in progress. If so, shared state. Otherwise, keep them independent.

IN THE KNOW: What's trending on socials and headlines

- Opus Workflow: The creator of Claude Code just dropped 6 strategies to help you get the most out of Opus 4.7 in Claude Code (1.1M views).
- Builder's Guide: A dev's 2026 blueprint makes the case that the winners won't build their own models, just the right stack around them.
- Risk Flipped: Shopify's CEO posted data on first-time founders that flips which career path is the safer bet right now.
- Talent War: Meta has snatched yet another founding engineer from Mira Murati's Thinking Machines Lab.
- Context Mastery: One of Anthropic's Claude Code engineers broke down why our long Claude sessions are rotting our outputs.
- Data Gold Rush: AI labs are quietly paying hundreds of thousands for the Slack archives, Jira tickets, and emails of dead startups.

AI CODING HACK: How to cut your Gemini API bill in half

API costs can really spiral when you're dealing with high-volume tasks. Google DevRel engineer Patrick Loeber recently shared a simple, one-line fix that cuts Gemini pricing in half for any jobs that don't need an immediate response.

Just add service_tier: "flex" to the config of any "generate_content" call:

```python
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    contents="Analyze this dataset for trends...",
    config={"service_tier": "flex"},
)

print(response.text)
```

Flex cuts your Gemini costs by 50% by using Google's spare capacity. You'll trade a 1 to 15 minute delay for massive savings, like Flash-Lite at just $0.125 per million input tokens. It's ideal for background tasks, batch jobs, or nightly data processing.

TOP & TRENDING RESOURCES

Top Tutorial: How to use Hooks effectively in coding agents — This tutorial covers how to use hooks in AI coding agents like Copilot or Claude Code. You'll learn how to intercept the agent's lifecycle, inject custom context, and use pre-tool hooks to ensure the AI writes clean, linted code before any changes are saved.

Top Repo: HyperFrames (by HeyGen) — A new framework for generating AI videos straight from code. It allows AI agents to whip up high-quality MP4s using standard HTML, CSS, and JavaScript.

Trending Paper: Designing synthetic datasets for the real world (by Google) — Specialized AI struggles because real-world training data is often scarce, private, and expensive. Simula solves this by using reasoning models to systematically design entire synthetic datasets, proving that structured, high-quality data generation heavily outperforms simpler baselines.
