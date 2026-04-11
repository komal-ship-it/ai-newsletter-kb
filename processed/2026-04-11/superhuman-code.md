# Superhuman — The Code — 2026-04-07

**Source:** thecode@mail.joinsuperhuman.ai
**Date:** 2026-04-07
**Original items:** ~10 (partial retrieval — beginning of newsletter body truncated)

## Key Announcements
- **OpenAI / Anthropic / Google model copying** — Main story (body truncated in retrieval) covers AI labs copying each other's model capabilities; subject line indicates Meta going open source as related thread.
- **Competition shifts to harness quality** — The "wrapper is the new winner": LangChain climbed to top 5 on benchmarks by improving its harness; Vercel improved results by simplifying agent tools. Real competition has moved from model quality to surrounding infrastructure.
- **OpenAI Safety Fellowship timing** — Announced hours after a New Yorker investigation revealed OpenAI had dissolved its safety teams.

## Tools & Products
- **Docs-as-filesystem tool** — Turns live documentation into a filesystem that agents can browse; prevents AI code from breaking when docs change | https://x.com/arlanr/status/2041215978957389908 | Effort: quick-win
- **Claude Code ! backtick syntax** — Embed shell commands directly in SKILL.md; Claude Code executes and substitutes live output before processing. Enables dynamic skill injection without copy-pasting. | https://x.com/lydiahallie/status/2034337963820327017 | Effort: quick-win

## Techniques & Methods
- **Agent harness quality as competitive moat** — Rather than switching models, focus on improving the surrounding infrastructure: tool selection, context structure, prompt architecture. LangChain and Vercel both demonstrated this outperforms model-swapping.
- **Claude Code ! backtick syntax in SKILL.md** — Create a skill file at `.claude/skills/<name>/SKILL.md`, prefix shell commands with `!` and backticks. Claude Code auto-runs the command and injects output before the skill runs. Pattern: `- PR diff: !` ` `gh pr diff` ` `. Use read-only commands (`cat`, `grep`, `gh pr view`) to avoid side effects.
- **RAG memory efficiency** — Perplexity, Azure, HubSpot use a technique making RAG 32x more memory efficient | https://x.com/_avichawla/status/2040326889928356122

## Research Papers
- None today.

## Industry Trends
- Agent harness / wrapper quality is the new model benchmark differentiator
- "Blueprints aren't buildings" — every competitor has the architecture map; execution at scale remains the real moat
- Karpathy-inspired LLM knowledge base pattern gaining broad adoption (third newsletter referencing this this week)
- OpenAI safety governance optics damaged by Safety Fellowship timing vs. NY investigative reporting

## Actionable Items
- [ ] Add `!` backtick shell commands to existing SKILL.md files for dynamic data injection — *quick-win* — https://x.com/lydiahallie/status/2034337963820327017 | action-2026-04-11-001
- [ ] Audit your current AI agent's harness/wrapper quality before switching models — improve tooling, context, prompts first — *weekend* — https://blog.langchain.com/the-anatomy-of-an-agent-harness/ | action-2026-04-11-002
- [ ] Read the Claude Code system prompt breakdown (leaked source code analysis) — *quick-win* — https://www.dbreunig.com/2026/04/04/how-claude-code-builds-a-system-prompt.html | action-2026-04-11-003
- [ ] Explore the docs-as-filesystem approach for keeping AI agents current with live docs — *quick-win* — https://x.com/arlanr/status/2041215978957389908 | action-2026-04-11-004
- [ ] Watch the Inside Codex video — OpenAI Head of DevRel + Codex PM on how the team ships — *quick-win* — https://www.youtube.com/watch?v=9qXc-THAvc0 | action-2026-04-11-005

## Notable Links
- https://blog.langchain.com/the-anatomy-of-an-agent-harness/ — LangChain agent harness anatomy (benchmark improvement story)
- https://www.dbreunig.com/2026/04/04/how-claude-code-builds-a-system-prompt.html — How Claude Code constructs system prompts (leaked source code breakdown)
- https://x.com/lydiahallie/status/2034337963820327017 — Lydia Hallie on Claude Code ! backtick syntax
- https://codenewsletter.ai/p/openai-anthropic-google-fight-model-copying-meta-goes-open-source — Full newsletter
