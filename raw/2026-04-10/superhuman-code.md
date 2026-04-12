# Superhuman Code — Raw — 2026-04-10

**Message ID:** 19d77b31925d8e5f
**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Subject:** 👀 Anthropic gives your code a security cam

Welcome back. Software engineering best practices were built for humans. Now that agents write most of the code, we're rebuilding those practices from scratch. Anthropic's new Monitor tool for Claude Code is a perfect example.

Also: How to build an agent harness, 50+ guides to ship with Claude, and what Karpathy thinks separates AI hype from reality.

Today's Insights:
- Powerful new updates and hacks for devs
- What is agentic thinking and why it matters
- How to auto-load project context in Claude Code
- Trending social posts, top repos, and more

---

## TODAY IN PROGRAMMING

**Claude Code gets a Monitor tool (security camera for your code):** Anthropic dropped the Monitor tool — an update that lets its coding agent run background scripts to track real-time events. It is basically a security camera for your code that only alerts you when it spots movement. You can set Claude to watch for dev server errors, track failing tests, or monitor a production launch for hours. This approach saves tokens because it only fires up when something actually goes wrong.
Source: https://x.com/noahzweben/status/2042332268450963774

**Cursor brings screenshots and video to agent-generated PRs:** Cursor shipped a feature that automatically attaches demo videos and screenshots to the GitHub PRs created by its cloud agents. In one demo, an agent built a color picker, refined the UI, added tests, and dropped a 20-second clip of the finished feature directly into the PR.
Source: https://x.com/cursor_ai/status/2042287192895267212

**OpenAI adds $100/mo Pro plan for heavier Codex use:** New Pro tier for developers who have outgrown the standard $20 Plus plan. Offers 5x Codex usage, an exclusive Pro model, and unlimited Instant and Thinking models. Launch promo: up to 10x the standard Plus usage through May 31st.
Source: https://x.com/OpenAI/status/2042295688323875316

---

## INSIGHT: What is agentic thinking, and why does it matter now

**The reasoning era is over.** Junyang Lin, former tech lead behind Alibaba's Qwen models, published an essay arguing the reasoning wave sparked by OpenAI's o1 and DeepSeek's R1 is already winding down, replaced by agentic thinking.

**Interaction over monologue.** While reasoning models just think longer before they speak, agentic models think in order to act. They use tools, read environment feedback, and pivot mid-task. The key question is no longer "how long can it think?" but "can it execute effectively over multiple turns?"

**More thinking doesn't mean more intelligence.** Recent research shows that simply increasing test-time compute doesn't always yield better results. Giving agents tool access makes training riskier — they can exploit logs or search for answers rather than actually solving problems.

**Environments are the new moat.** Building better environments is becoming its own startup category. Training agents now involves browsers, terminals, and API layers instead of just models. Competitive edge is shifting from RL algorithms to harness engineering and the ability to close the loop between what a model decides and what actually happens next.

Source: https://justinlin610.github.io/blog/from-reasoning-to-agentic-thinking/

---

## IN THE KNOW: What's trending on socials and headlines

- **Claude Cookbook:** Anthropic published 50+ ready-to-use guides for building with Claude, covering managed agents, context compaction, and multi-modal workflows. https://platform.claude.com/cookbook/
- **Better Agents:** LangChain open-sourced a system that runs evals on your agent, finds what's broken, and fixes the prompts automatically — no manual tuning. https://x.com/Vtrivedy10/status/2041927488918413589
- **Faster File Search:** The creator of Claude Code broke down how they made file search 3x faster on massive codebases. Enterprise users confirmed the speed boost. https://x.com/bcherny/status/2042352720489955539
- **Reality Gap:** Andrej Karpathy says there's a growing gap in how people understand AI — it comes down to who's paying $200/month and who isn't. (2M views) https://x.com/karpathy/status/2042334451611693415
- **Session Extender:** Guide to bridge Claude Code with NotebookLM to offload research and stretch your tokens. https://x.com/hooeem/status/2042293751805329445
- **AGI Timeline:** OpenAI's Chief Scientist shared when they expect AI to go from intern-level to fully autonomous researcher. https://x.com/jacobeffron/status/2042234897134162077
- **Advisor Mode:** Anthropic shipped a way to use Opus for complex planning but leaves grunt work to Sonnet in a single API call. Costs 11.9% less per task. (2.9M views) https://x.com/claudeai/status/2042308622181339453

---

## AI CODING HACK: How to auto-load project context in Claude Code

Claude Code loads your CLAUDE.md at session start, but it doesn't know what branch you're on, what files changed, or what broke since your last session. A hook pattern from Claude Code's hooks system fixes this.

Add this to your `.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [{
      "hooks": [{
        "type": "command",
        "command": "git status > /tmp/claude-git-context.txt && echo 'Development context loaded'"
      }]
    }]
  }
}
```

Now, whenever you start a session or clear your history, Claude automatically pulls in your current branch and any changes.

Reference: https://dev.to/holasoymalva/the-ultimate-claude-code-guide-every-hidden-trick-hack-and-power-feature-you-need-to-know-2l45

---

## TOP & TRENDING RESOURCES

**Top Tutorial — How a senior software engineer uses coding agents:**
Turn Claude Code into a powerful autonomous assistant. Learn how to set up project context files, build automated validation loops to catch bugs, run parallel sub-agents, and master a "plan, execute, and review" workflow.
https://www.youtube.com/watch?v=MzhIr7BfpI0

**Top Repo — Archon:**
A harness builder for AI coding agents. Define your entire development process from planning and implementation to code reviews and PRs as YAML workflows that run reliably across all your projects.
https://github.com/coleam00/Archon

**Trending Paper — ConvApparel (Google):**
Today's AI user simulators feel too perfect and unnaturally patient compared to real people. When you train these simulators on actual human data instead of just feeding them instructions, they become much more realistic and adaptable.
https://research.google/blog/convapparel-measuring-and-bridging-the-realism-gap-in-user-simulators/

---

Web version: https://codenewsletter.ai/p/anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan
