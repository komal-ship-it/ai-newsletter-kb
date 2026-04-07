# AI Collective — 2026-04-07

**Source:** aicollectivenewsletter@mail.beehiiv.com
**Date:** 2026-04-07
**Original items:** 14

## Key Announcements
- **Anthropic ends flat-rate Claude access for third-party harnesses** — Effective April 4, 2026. OpenClaw was first blocked; all third-party harnesses to follow in coming weeks. One-time credit (matching monthly sub cost) redeemable by **April 17**. Up to 30% discount on pre-purchased usage bundles.
- **Karpathy's self-improving knowledge base** — Viral tweet kicked off broad discussion of AI systems that manage their own knowledge (read → structure → index → self-check). Best-performing system uses plain markdown + keyword search, not complex retrieval.
- **Q1 2026 VC record: $300B** — Up 150% YoY. AI took $242B (80%). Mega-rounds: OpenAI $122B, Anthropic $30B, xAI $20B, Waymo $16B. Early-stage funding +41% YoY to $41.3B across 1,800 deals.
- **Anthropic Conway agent** — Internally testing a persistent background agent that uses browsers and memory to complete multi-step workflows autonomously without waiting for user prompts.
- **OpenAI acquires TBPN** — First media company purchase. TBPN (John Coogan + Jordi Hays) on track for $30M ARR.
- **Mercor supply-chain breach** — 4TB stolen via LiteLLM attack. 500,000 machines affected. Mercor used by OpenAI, Anthropic, Meta.
- **Oracle: 30,000 layoffs** — 18% of workforce cut to fund $156B AI data center buildout.
- **MIT task study** — AI handles 65% of text-based work at acceptable quality today; projected 95% by 2029.
- **SpaceX confidential S-1** — Targeting $1.75T valuation; potential $75B raise (largest US IPO on record).
- **OpenAI Codex repriced** — Business seat: $20/month (down from $25). 2M+ weekly builders, up 6x since January.

## Tools & Products
- **Conway (Anthropic internal)** — Persistent background agent with browser + memory for autonomous multi-step workflows | Effort: watch/upcoming
- **OpenAI Codex** — Business seat now $20/month | Effort: quick-win to evaluate

## Techniques & Methods
- **Five-layer self-improving AI stack** — (1) Knowledge bases, (2) Agent memory, (3) Context engineering, (4) Agent systems, (5) Self-improvement. Converges into a loop: retrieve → act → write improvements back into KB. Key insight: plain markdown + keyword search outperforms complex retrieval pipelines on standard memory benchmarks.
- **Pre-compute context layer (Meta pattern)** — Separate from Karpathy's pattern but related: generate structured context files before deploying agents to act, rather than having agents discover structure at runtime.

## Research Papers
- None today.

## Industry Trends
- AI handling 65% of text tasks today, 95% projected by 2029 (MIT, 11,500 tasks analyzed)
- "It remains genuinely difficult to tell whether any given job was eliminated by AI, eliminated to fund AI, or simply eliminated under the cover of an AI narrative" — AI Collective on Oracle layoffs
- Supply-chain attacks on AI tooling rising (LiteLLM breach affecting 500K machines)
- Forward-deployed engineer (FDE) roles surging 10x in job postings but only 10% engineer interest

## Actionable Items
- [ ] **URGENT:** Redeem Anthropic one-time credit before April 17 deadline — matches your monthly subscription cost — *quick-win* | action-2026-04-07-011
- [ ] Build a Karpathy-style self-improving markdown knowledge base: AI reads raw sources → writes structured articles → maintains index → self-checks. Start with 121 curated sources as template — *weekend* | action-2026-04-07-012
- [ ] Evaluate OpenAI Codex Business at $20/month — repriced from $25, 2M+ weekly builders — *quick-win* | action-2026-04-07-013
- [ ] Monitor LiteLLM supply-chain breach details — if you use LiteLLM, check for compromise indicators — *quick-win* | action-2026-04-07-014

## Notable Links
- HumanX 2026 — April 6–9, San Francisco (Moscone Center), Fei-Fei Li + Ray Kurzweil
- AIM-2026 — April 27–29, San Francisco
- AI DevSummit 2026 — May 27–28, South San Francisco
