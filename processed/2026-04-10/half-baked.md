# Half Baked — 2026-04-10

**Source:** ideas@mail.gethalfbaked.com
**Date:** 2026-04-10
**Original items:** 7

## Key Announcements
- **PixelProof (Cross-Device Testing Tool)** — Half Baked's featured idea: an AI monitoring SaaS that continuously tests landing pages across 5,000+ virtual device/browser/OS combinations, ranks issues by device market share, and fires Slack alerts the moment something breaks — before a single customer notices.
- **AfterQuery raises $30M at $300M valuation** — Just crossed $100M ARR milestone.
- **Rork raises $15M seed** — Led by Left Lane Capital.
- **SpaceX posted ~$5B in losses in 2025** — Largely driven by xAI spending.

## Tools & Products
- **PixelProof** — AI-powered cross-device visual regression monitoring for landing pages; connects domain in 60s, scans 5,000+ device/browser combos, sends Slack alerts ranked by traffic impact | https://rendar-557521439876.us-west1.run.app/ | Effort: weekend
- **Ferndesk** — AI agent that writes help docs, takes annotated screenshots, and responds to customers; auto-updating help center | https://ferndesk.com/ | Effort: quick-win
- **Obsidian + Claude Code (LLM Wiki)** — AI-maintained personal knowledge base using Obsidian vault structure with /raw-sources/, /wiki/, and CLAUDE.md | https://obsidian.md/ | Effort: weekend

## Techniques & Methods
- **LLM Wiki Pattern (Andrej Karpathy)** — Use Claude Code pointed at an Obsidian vault to auto-process sources into structured wiki pages. Drop files into /raw-sources/, Claude updates 10-15 wiki pages per file. Weekly lint pass for contradictions and orphan pages. Full tutorial: https://x.com/defileo/status/2042241063612502162
- **Ramp's AI-pilled framework** — Getting an entire company onto AI tooling. Resource: https://x.com/geoffintech/status/2042002590758572377
- **7 Claude prompt skills** — Curated prompt techniques worth adding to a developer's repertoire. https://x.com/heynavtoor/status/2042291937483637219

## Research Papers
- None today.

## Industry Trends
- Over 24,000 distinct Android devices are in active use today; most dev teams test on roughly 10, creating a massive cross-device QA gap.
- Q1 2026 venture funding surpassed $300B, but ~66% captured by just four companies — concentration of capital continuing.
- AfterQuery crossing $100M ARR signals strong demand in AI data/analytics tooling.

## Actionable Items
- [ ] Try the PixelProof demo to validate cross-device testing concept — *quick-win* — https://rendar-557521439876.us-west1.run.app/ | action-2026-04-10-001
- [ ] Set up LLM Wiki using Obsidian + Claude Code following the 4-step tutorial — *weekend* — https://x.com/defileo/status/2042241063612502162 | action-2026-04-10-002
- [ ] Review the 7 Claude skills thread and add relevant prompts to your workflow — *quick-win* — https://x.com/heynavtoor/status/2042291937483637219 | action-2026-04-10-003
- [ ] Read Ramp's AI adoption framework for ideas on company-wide AI rollout — *quick-win* — https://x.com/geoffintech/status/2042002590758572377 | action-2026-04-10-004

## Notable Links
- https://rendar-557521439876.us-west1.run.app/ — PixelProof demo (cross-device testing tool)
- https://x.com/defileo/status/2042241063612502162 — LLM Wiki / Second Brain 5-minute setup tutorial
- https://www.notion.so/From-Weekend-Project-to-7-Billion-in-App-Revenue-33e8d2b9402b80a5a8ebdccb03d483d3 — Case study: side project to $7B in app revenue
- https://www.businesswire.com/news/home/20260409469482/en/AfterQuery-Raises-%2430-Million-Series-A-Round-at-%24300-Million-Valuation — AfterQuery $30M raise announcement
- https://www.gethalfbaked.com/p/half-baked-586-device-testing — Full newsletter web version
