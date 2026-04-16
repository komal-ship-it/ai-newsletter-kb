# Superhuman — The Code — 2026-04-14

**Source:** thecode@mail.joinsuperhuman.ai
**Subject:** 👀 Cursor changes how you code with agents
**Date:** 2026-04-14

---

Welcome back. AI agents keep getting smarter, but running multiple tasks at once still feels clunky. Cursor just dropped an update that changes how you manage them.

Also: How a senior engineer built a coding harness in 60 lines, a DeepMind engineer's 8 tips for better agent skills, and what Google expects from Product Managers in 2026.

We've grown to over 230K CTOs, engineering leaders, and developers.

---

## TODAY IN PROGRAMMING

**Cursor now lets you manage a fleet of coding agents at once:** [Cursor 3.1](https://cursor.com/changelog/3-1) adds a tiled Agents Window for running multiple AI agents in draggable panes, compare outputs side by side without tab switching. Also brings batch speech-to-text, branch selection for cloud agents, and improved file search filters.

**Vercel open-sources a platform for cloud coding agents:** [Open Agents](https://x.com/rauchg/status/2043869656931529034) — a template for deploying coding agents that run indefinitely in the cloud. Built with Vercel's AI SDK and Sandbox tools, allows teams to run hundreds of agents at once with zero timeouts. [Try it here](https://vercel.com/templates/template/open-agents)

**Meta is reportedly working on an AI clone of its CEO:** Developing an AI version of [Mark Zuckerberg](https://sg.news.yahoo.com/meta-reportedly-building-ai-clone-130242070.html), trained on his mannerisms, tone, and public statements.

---

## INSIGHT: Why Long-Running AI Agents Keep Failing

**The 45-minute cliff.** AI agents start strong but lose steam halfway through, declaring projects "finished" at 60% completion. Anthropic engineer Prithvi Rajasekaran [identified](https://www.anthropic.com/engineering/harness-design-long-running-apps) two culprits: models lose focus as context windows fill, and they can't honestly critique their own work.

**Agents are terrible at grading themselves.** They routinely praise mediocre or broken code as high-quality.

**The fix.** Rajasekaran solved this with a planner, a generator, and a skeptical evaluator. The evaluator uses [Playwright](https://playwright.dev/) to test the app like a real user. A solo agent built a broken game for $9 in 20 minutes; this multi-agent harness produced a working game for $200 over 6 hours.

**The catch is maintenance.** Agent harnesses are built on assumptions about model limitations that quickly become obsolete. When upgrading from Opus 4.5 to 4.6, Anthropic found they could strip away entire structures the newer model no longer needed.

---

## IN THE KNOW

- [8 tips for better agent skills from Google DeepMind engineer](https://x.com/_philschmid/status/2043705157850951699)
- [Build an agent memory that actually learns](https://x.com/akshay_pachaar/status/2043745099792953508)
- [AI coding harness in 60 lines of Python](https://x.com/theo/status/2043611205856837680)
- [Google DeepMind's newest hire is a Cambridge philosopher](https://x.com/dioscuri/status/2043661976534950323)
- [Pre-launch checklist for vibe-coded apps](https://x.com/Hartdrawss/status/2043351026053386727) — covers API key exposure blind spots
- [OpenAI memo calls Claude "a religion" internally](https://www.theverge.com/ai-artificial-intelligence/911118/openai-memo-cro-ai-competition-anthropic) — five-point plan to win enterprise AI war

---

## TOP & TRENDING RESOURCES

**Top Tutorial:** [How to build and deploy an app with Codex](https://www.youtube.com/watch?v=hoCWD1aI60Y) — build and launch a complete web app, configure Codex plugins, generate code with plain English prompts.

**Top Repo:** [MarkItDown](https://github.com/microsoft/markitdown) — converts any messy file into clean Markdown for AI agents. Handles PDFs, slides, documents, audio, and more.

**Trending Paper:** [Scaling coding agents via atomic skills](https://arxiv.org/abs/2604.05013) — By training on basic "atomic skills" like editing, agents significantly improve ability to generalize and solve unseen coding challenges.

---

## AI CODING HACK: How to Fix Claude Code's Unstable Behavior

Claude Code users noticed a dip in quality — bloated context, override settings, stale auto-memory. Kun Chen (former L8 at Meta and Microsoft) [shared a fix](https://x.com/kunchenguid/status/2043511416448307378): add this config to `~/.claude/settings.json`:

```json
{
  "effortLevel": "high",
  "env": {
    "CLAUDE_CODE_DISABLE_1M_CONTEXT": "1",
    "CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING": "1",
    "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1",
    "CLAUDE_CODE_SUBAGENT_MODEL": "sonnet"
  }
}
```

These flags keep setup lean, lock effort level, and give manual control over CLAUDE.md. Switching subagent to Sonnet boosts reliability.
