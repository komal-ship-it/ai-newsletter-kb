# Superhuman — The Code — 2026-04-14 (raw)

**Source:** thecode@mail.joinsuperhuman.ai
**Subject:** 👀 MiniMax drops open weight coding model
**Message-ID:** 19d8725ea71ea8b3
**Date:** 2026-04-13T14:01:09+00:00

---

Welcome back. Three weeks ago, China-based MiniMax claimed they built a coding model that trains itself. Now that it is making rounds on X, they just dropped M2.7 as an open-weight model on Hugging Face.

Also: How an ex-Oracle director tests code with agents, 18 Cursor tips from their engineer, and an Atlassian engineer explains how to crack a Staff Engineer interview.

Today's Insights:
- Powerful new updates and hacks for devs
- Why training your own LLM is still so hard
- How to pull live git data into Claude Code
- Trending social posts, top repos, and more

## TODAY IN PROGRAMMING

MiniMax opens up its coding agent model and ships a new CLI: MiniMax just released [M2.7 as an open-weight download](https://x.com/MiniMax_AI/status/2043132047397659000) on Hugging Face, allowing teams to run the 230-billion-parameter model locally on 128GB RAM setups. It holds its own against top closed models on engineering benchmarks like SWE-Pro (56.22%) and Terminal Bench 2 (57.0%). Along with the model, they launched [MMX-CLI](https://x.com/MiniMax_AI/status/2042641521653256234), a command-line tool that gives agents native access to image, video, voice, and search capabilities without needing any MCP setup. [Try it here.](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)

Developers highlight sharp decline in Claude Code quality: Anthropic is facing backlash after AMD's senior director of AI [published](https://github.com/anthropics/claude-code/issues/42796) metrics from nearly 7,000 coding sessions. The report shows Claude Code's reasoning length dropped by 67%, while API requests have spiked 80x since February. Anthropic [confirmed](https://x.com/bcherny/status/2043163965648515234) they lowered the default thinking effort from high to medium to cut down on token costs.

Apple tests four designs for its first smart glasses: The iPhone maker is [reportedly](https://techcrunch.com/2026/04/12/apple-reportedly-testing-four-designs-for-upcoming-smart-glasses/) testing four different frame styles for its upcoming smart glasses, slated for a 2027 release. According to Bloomberg, these glasses won't include a display. Instead, they'll focus on cameras for photos and video, phone calls, music, and an upgraded Siri.

## INSIGHT: Why training your own LLM is still so hard

The enterprise LLM market is on track to hit $5.9 billion this year. Paras Stefanopoulos, an AI engineer at Baseten, writes in a [deep dive](https://www.baseten.co/blog/open-source-llm-training-is-a-mess-here-is-how-it-all-works/) that teams finding a total mess.

Framework overlap: Stefanopoulos mapped the entire stack and found five major frameworks that overlap significantly. Teams waste days troubleshooting library combinations that crash before training even begins.

The obvious fix isn't ready: Even PyTorch's [native stack](https://github.com/pytorch/torchtitan) is struggling. Reports show gradient explosions after just 1,000 steps on newer architectures and frequent out-of-memory crashes.

The smart play: Baseten is currently relying on NVIDIA's [Megatron framework](https://arxiv.org/abs/2603.07685) for its reliability at scale.

## IN THE KNOW: What's trending on socials and headlines

- Under Wraps: A leaked Anthropic feature shows a Lovable-style [app builder](https://x.com/marmaduke091/status/2043382991901147158) living directly inside Claude (2.7M views).
- Swift Skills: These [5 skill packs](https://x.com/PaulSolt/status/2042716870512353294) for Claude Code iOS development.
- Prep Trap: A Principal Engineer at Atlassian posted a [Staff interview playbook](https://x.com/system_monarch/status/2042573963608674673).
- Inside The Lab: OpenAI [shared](https://x.com/gabrielchua/status/2043339151278506234) how their team uses Codex internally.
- 700 AI Coworkers: A billion-dollar company gave every employee a personal [AI coworker](https://x.com/sebgoddijn/status/2042285915435937816).
- Cursor Flow: A Cursor engineer just dropped [18 workflow tips](https://x.com/tibor_tee/status/2041233650881266170).
- Career Bet: Box CEO Aaron Levie thinks AI-generated code is about to trigger a [massive shift](https://x.com/levie/status/2043318118169354302) in who gets hired in security.
- Test-First Agents: Ex-Director of Engineering at Oracle [walks through](https://www.youtube.com/watch?v=Kx7bAwVH_1c) how he builds with TDD in Claude Code.

## TOP & TRENDING RESOURCES

Top Tutorial — [Meta staff engineer's guide to Codex](https://www.youtube.com/watch?v=nQFtsehu7h0): Teaches developers how to master OpenAI's Codex app. You'll learn to navigate its IDE, manage parallel tasks with git worktrees, write effective AI prompts, and build custom automated workflows using an agents.md file.

Top Repo — [Agent Reach](https://github.com/Panniantong/Agent-Reach/blob/main/docs/README_en.md): Gives your agents instant access to social platforms like Twitter and Reddit. Single command to start scraping.

Trending Paper — [Single-agent LLMs vs. Multi-agent systems](https://arxiv.org/abs/2604.02460): When you level the playing field on computing power, single agents often perform just as well, or even better than multi-agent systems on complex reasoning.

## AI CODING HACK: How to pull live git data into Claude Code commands

Most people think Claude Code slash commands are static, but there is a hidden way to make them dynamic. If you prefix a shell command with "!" in your command file, Claude runs it first and pulls the output as context.

T3 Chat founder Theo Browne [shared](https://x.com/theo/status/2043103001121034581) a PR summary command that automatically pulls diffs and comments by setting up a file at ".claude/commands/pr-summary.md":

```
---
name: pr-summary
description: Summarize changes in a pull request
---

## Pull request context
- PR diff: !`gh pr diff`
- PR comments: !`gh pr view --comments`
- Changed files: !`gh pr diff --name-only`

## Your task
Summarize this pull request...
```

Just run "/pr-summary" on any branch with an open PR to automatically pull in the live diff, comment thread, and file list.

https://codenewsletter.ai/p/minimax-drops-an-open-weight-model-apple-designs-its-first-smart-glasses
