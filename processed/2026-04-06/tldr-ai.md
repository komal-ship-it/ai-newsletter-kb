# TLDR — 2026-04-06

**Source:** dan@tldrnewsletter.com
**Date:** 2026-04-06
**Original items:** 13

## Key Announcements
- **OpenAI & Anthropic Pre-IPO Finances Revealed** — Confidential financial documents show OpenAI expects to burn $85B in 2028; Anthropic forecasts similar mounting compute costs; both companies accelerating model release cadence with no slowdown in sight.
- **Apple Signs Nvidia/AMD eGPU Drivers for Mac** — Macs can now use Nvidia eGPUs for AI LLM processing without disabling System Integrity Protection; Mac delivery times stretch to 6 weeks due to AI agent (e.g., OpenClaw) demand.
- **Claude Code System Prompt Leaked & Analyzed** — Accidental source code leak reveals how Claude Code assembles context from always-included, conditional, and variable components; highlights complexity of "context engineering" and the role of harnesses.
- **OpenAI COO Brad Lightcap Shifts Role** — Lightcap moves to lead special projects, reporting directly to Sam Altman.

## Tools & Products
- **Clerk Billing** — Seat-limited plans for B2B SaaS orgs; auto-enforces org member limits and surfaces upgrade prompts; integrates with existing Clerk auth/org setup | clerk.com/billing | Effort: quick-win
- **syntaqlite** — High-fidelity devtools for SQLite built by one developer using an AI coding agent over ~250 hours across 3 months; detailed post-mortem on where AI helped and hurt | Effort: weekend
- **Gauntlet AI Fellowship** — Intensive 10-week fully funded AI engineering fellowship targeting $200K–$950K roles | Effort: major

## Techniques & Methods
- **Claude Code Context Engineering** — System prompts assembled from layers: always-included components, conditional components (based on environment/state), and variable alternatives. Harnesses coordinate this assembly. Leaked source reveals the full table of components.

## Research Papers
- None today.

## Industry Trends
- GitHub commits on pace for 14 billion/year — AI-assisted development is measurably accelerating commit velocity.
- Economists now taking AI job displacement seriously; policy discussions needed within 2–5 year window.
- China tech giants recruiting high schoolers for creative and PM roles; universities questioned as talent pipeline.
- Domain-specific LLMs argued unlikely to succeed: large providers would have built them if feasible.
- Non-determinism in AI products reframed as a product management challenge, not a bug.
- AI arms race intensifying: no signs of slowdown in compute investment or model release cadence.

## Actionable Items
- [ ] Read the Claude Code system prompt breakdown for context engineering patterns — *quick-win* — Search "How Claude Code Builds a System Prompt" | action-2026-04-06-001
- [ ] Read "Eight Years of Wanting, Three Months of Building with AI" (syntaqlite) for AI coding workflow lessons — *quick-win* — Search "syntaqlite eight years wanting" | action-2026-04-06-002
- [ ] Evaluate Clerk Billing seat-limited plans for any B2B SaaS products — *quick-win* — clerk.com/billing | action-2026-04-06-003

## Notable Links
- "How Claude Code Builds a System Prompt" — context engineering deep-dive from leaked source code
- "Eight Years of Wanting, Three Months of Building with AI" — 23-min AI coding agent case study (syntaqlite/SQLite devtools)
- "An Inside Look at OpenAI and Anthropic's Finances" — IPO financial documents analysis with charts
- "Why Domain-Specific LLMs Won't Exist: An Intuition" — 3-min argument against vertical AI models
- "Non-Determinism Isn't a Bug. It's Tuesday." — 14-min piece on AI product management
