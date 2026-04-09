# Superhuman — The Code — 2026-04-07

**Source:** thecode@mail.joinsuperhuman.ai
**Date:** 2026-04-07
**Original items:** 10

## Key Announcements
- **OpenAI + Anthropic + Google vs. Adversarial Distillation** — The three labs are collaborating via the Frontier Model Forum to combat unauthorized model copying; Anthropic has already cut off Chinese-controlled firms after catching three labs harvesting responses.
- **Anthropic Compute Expansion** — Multi-gigawatt deal with Google and Broadcom for next-gen TPU capacity (live 2027); run-rate revenue tripled to $30B since late 2025, enterprise customers spending $1M+ doubled to 1,000+ in two months.
- **Meta Open-Source Plans** — Avocado (LLM) and Mango (image/video gen) open-source versions of Meta's next frontier models in development, lighter with fewer parameters.
- **Claude Code Source Leak** — Anthropic accidentally leaked ~500K lines of TypeScript via npm; reveals the harness engineering (file history tracking, navigation tools, parallel agents) is the performance differentiator, not the model alone.
- **Milla Jovovich's Agentic Memory Tool** — Scored 100% on LongMemEval benchmark.

## Tools & Products
- **Graphify** — Turns any folder of code, docs, papers, or images into a queryable knowledge graph | Effort: weekend
- **Mastra** — TypeScript framework for building AI agents with Slack, Exa AI, Cal.com integration | Effort: weekend

## Techniques & Methods
- **`!` Backtick Syntax in SKILL.md** — Embed live shell commands in Claude Code skill files; Claude Code executes and injects output before processing (e.g., `!`gh pr diff`` for live PR diffs). Shared by Lydia Hallie (Claude Code team).
- **32x More Memory-Efficient RAG** — Technique used by Perplexity, Azure, and HubSpot; explained with code. Details behind paywall/link.
- **Compounding LLM Knowledge Base** — Build a self-improving external brain that compounds over time, inspired by Andrej Karpathy.
- **Harness > Parameters** — Claude Code's performance traced to engineering (file history, tools, parallel agents) not model quality; LangChain reached top-5 benchmarks via harness improvements alone.
- **Warp Decode on Blackwell GPUs** — Cursor achieves 1.8x faster inference; trending paper.
- **Stateless-to-Production Agent** — When agents fail, the problem is rarely the model; framework for turning stateless LLMs into production agents.

## Research Papers
- **Cursor Warp Decode on Blackwell GPUs** — 1.8x faster inference via warp decode technique | Effort: major (GPU-level)

## Industry Trends
- Adversarial distillation draining billions annually from US AI labs — regulatory and technical countermeasures forming.
- Harnesses/wrappers are now the primary competitive differentiator over model quality.
- OpenAI announced Safety Fellowship hours after New Yorker investigation revealed dissolved safety teams — optics problem.
- Anthropic revenue at $30B run-rate; enterprise growth accelerating.

## Actionable Items
- [ ] Use `!` backtick syntax in SKILL.md files to inject live shell output into Claude Code skills — *quick-win* — immediate productivity boost for any Claude Code workflow | action-2026-04-07-001
- [ ] Apply the 32x memory-efficient RAG technique to any existing RAG pipeline — *weekend* — used in production by Perplexity/Azure/HubSpot | action-2026-04-07-002
- [ ] Build a compounding LLM knowledge base (Karpathy-style) — *weekend* — turns ongoing AI interactions into a searchable personal knowledge graph | action-2026-04-07-003
- [ ] Read leaked Claude Code source code system prompt analysis to understand production agent prompt construction — *quick-win* — directly applicable to building better agents | action-2026-04-07-004

## Notable Links
- Graphify repo — code/docs/images to queryable knowledge graph
- Mastra TypeScript agent framework tutorial — Slack + Exa AI + Cal.com
- Leaked Claude Code system prompt breakdown (trending post)
