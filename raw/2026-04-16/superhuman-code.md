# Superhuman (The Code) — Raw — 2026-04-16

**Source:** thecode@mail.joinsuperhuman.ai
**Message-ID:** 19d969926e6574a4
**Date:** 2026-04-16

---

Welcome back. Things in AI are getting pretty crazy. Allbirds (yes, the sneaker company) is selling off its shoe business and is pivoting into buying GPUs and renting them out to AI companies. The company's stock price surged more than 5x on the move.

Today: Gemini's new TTS model, 7 concepts behind senior backend interviews, a viral prompt that uses 8 subagents to fix messy code, and why Nvidia's CEO says chip restrictions are backfiring.

TODAY IN PROGRAMMING

Google unveils a speech model that acts on your cues: The search giant just released Gemini 3.1 Flash TTS, a text-to-speech model that lets you use natural language prompts to control tone, pace, and delivery on the fly. It supports over 70 languages, native multi-speaker dialogue, and consistent character voices across scenes. Additionally, Google launched a native Gemini app for macOS. This Swift build was prototyped in just days using their Antigravity coding platform.

OpenAI's SDK gets serious about agent safety: The ChatGPT maker just shipped major updates to its Agents SDK, giving enterprises a safer way to deploy automated helpers. A fresh sandbox integration isolates agents within controlled workspaces, limiting their access to only the files and code they need. The SDK also gains an in-distribution harness for frontier models, which should help tackle those complex, multi-step jobs that have proven notoriously tricky to automate.

Anthropic rebuilds its coding app for parallel agents: The AI lab just rebuilt Claude Code from the ground up, centering it on a new split-pane interface. Developers can now handle several sessions at once using a sidebar that keeps tasks organized by project or current status. With built-in file editing, diff reviews, and a terminal, you'll rarely need to jump between different apps. That said, the rollout hasn't been perfectly smooth — senior engineer and T3 Chat CEO, Theo Browne, reported 40 bugs within just his first hour of use.

INSIGHT: Why is Cloudflare rebuilding its CLI for agents

Agents outrank humans. This week, Cloudflare announced they are rebuilding its Wrangler CLI from scratch, and the reason behind it is pretty significant. The company says AI agents are now the main users of its APIs, yet most of its 100+ products don't even have CLI commands.

Where agents stumble. Cloudflare's main issue was that inconsistent CLI commands were breaking AI agents. While humans can navigate different terms like "get" or "info" for the same action, agents can't. To fix this, Cloudflare built a single schema to automatically generate every command, enforcing strict naming rules at the system level instead of relying on manual code reviews.

They're not alone in this bet. In early 2026, six major open-source projects launched with a focus on providing structured CLIs for AI agents. This approach is 10 to 32 times more cost-effective on tokens than MCP-based setups and significantly more reliable.

No single winner. Cloudflare still ships MCP servers, meaning even the company pushing hardest for CLIs isn't settling on just one method. The platforms that can adapt the fastest across all these standards will likely set the new bar.

IN THE KNOW: What's trending on socials and headlines

- Prompt Prank: The internet is increasingly being written for agents. Here's one hilarious example of a user prompt injecting a website to trick an agent.
- Agent Academy: Cursor's VP of Developer Education just dropped a 30-minute course on using coding agents to plan features, squash bugs, and ship.
- Huang's Warning: On a recent podcast, Nvidia's CEO argued U.S. chip restrictions are doing the exact opposite of what they were designed for.
- Mac Mode: An OpenAI Codex engineer shipped a plugin that finally teaches the agent how native Mac apps should feel, not just compile.
- Cleanup Crew: This viral prompt spins up 8 subagents to fix everything wrong with a vibecoded codebase in one sweep.
- The Seven: One engineer claims 93.5% of senior backend interviews boil down to just 7 core concepts.

AI CODING HACK: How to monitor deploys without leaving Claude Code

You just kicked off a deploy, and now you're constantly switching tabs to see if it passed. Instead, use the /loop command to run a recurring prompt in the background while you stay focused on your work. Just set a check to fire every five minutes:

/loop 5m check if the deploy succeeded and report back

The interval supports seconds, minutes, hours, and days. If you skip the interval, it defaults to 10 minutes. You can also loop other commands:

/loop 20m /review-pr 1234

Tasks are session-scoped and expire after three days, so you don't have to worry about a forgotten loop running indefinitely.

TOP & TRENDING RESOURCES

Top Tutorial: Spec-driven development with coding agents (by DeepLearning.AI) — This tutorial teaches developers how to build better software using AI coding agents. You'll learn to write clear markdown specs and project guides.

Top Repo: Gemini Scribe — An Obsidian plugin that integrates Google's Gemini models to search, edit, and organize your vault files.

Trending Paper: Trusted access for the next era of cyber defense (by OpenAI) — Hackers are using advanced AI to attack vulnerable digital systems. To fight back, OpenAI is giving verified defenders a less-restricted model called GPT-5.4-Cyber to help them quickly find and fix weaknesses.
