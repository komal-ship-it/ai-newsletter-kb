# Superhuman Code — 2026-04-07

**Source:** thecode@mail.joinsuperhuman.ai
**Date:** 2026-04-07
**Original items:** 10

## Key Announcements
- **Microsoft MAI model family** — Three new models on Microsoft Foundry: MAI-Transcribe-1 (speech-to-text, tops benchmarks in 25 languages, 2.5x faster than Azure batch transcription, beats Whisper + Gemini), MAI-Voice-1 (voice cloning from seconds of audio), MAI-Image-2 (top-3 on Arena AI, 2x faster generation).
- **Anthropic cuts third-party subscription access** — OpenClaw blocked April 4. One-time credit for existing subscribers. OpenAI immediately capitalized, promoting ChatGPT Plus compatibility with OpenClaw/OpenCode/Cline.
- **Karpathy personal knowledge engine** — LLM-generated interconnected Markdown knowledge bases stored locally, viewable in Obsidian. Own your data, format is universal, swap any AI provider.
- **Auto-apply job tool** — Scans career pages, rewrites CV, fills applications; one dev landed a job after 700+ submissions (1.8M views).
- **Axios npm supply chain attack** — Trojan slipped into Axios, the most popular HTTP client (1.5M views on maintainer post-mortem).

## Tools & Products
- **Microsoft MAI-Transcribe-1** — Speech-to-text, 25 languages, beats Whisper + Gemini, 2.5x Azure batch speed | Available: Microsoft Foundry | Effort: quick-win to test
- **Microsoft MAI-Voice-1** — Custom voice clone from seconds of audio | Available: Microsoft Foundry | Effort: quick-win
- **Microsoft MAI-Image-2** — Top-3 image gen on Arena AI, 2x faster | Available: Microsoft Foundry | Effort: quick-win
- **Agent Skills repo (Google Cloud AI Director)** — Production-grade packaged workflows and quality gates for AI coding agents | Effort: weekend
- **Codex Figma→code workflow** — Uses Figma MCP + Playwright to generate and validate UI code against Figma designs automatically | Effort: weekend

## Techniques & Methods
- **Spec-driven development with AI agents** — Write clear specs, set strict constraints, break complex features into manageable tasks before handing to agents. Covered in linked tutorial.
- **Codex Figma→code prompt pattern:**
  1. `get_design_context` for the exact node/frame
  2. `get_screenshot` of the exact variant before coding
  3. Reuse existing design system components and tokens
  4. Playwright validation loop until UI matches reference
- **Forward-deployed engineer (FDE) pattern** — Embedding engineers with enterprise customers to make AI work in production; postings up 10x but only 10% engineer interest due to "zero coding, too much client management" perception.

## Research Papers
- **AI Agent Traps** (Google) — Six types of hidden malicious web content designed to trick or exploit AI agents browsing the web. | Effort: quick-win to read

## Industry Trends
- Microsoft emerging as independent AI model competitor (MAI family beating OpenAI Whisper + Gemini on transcription)
- Enterprise AI still requires heavy human hand-holding — vibe-coded production apps failing at 15 common points
- iOS app shipping without Xcode now possible via Codex CLI workflow (under 7 minutes)
- Stanford CS153 AI systems course first lecture now public

## Actionable Items
- [ ] Test Microsoft MAI-Transcribe-1 on Microsoft Foundry — compare against current Whisper/Gemini usage — *quick-win* | action-2026-04-07-015
- [ ] Read the Google AI Agent Traps paper — understand the 6 attack types before deploying web-browsing agents — *quick-win* | action-2026-04-07-016
- [ ] Try spec-driven development workflow with AI agents using the linked tutorial — *quick-win* | action-2026-04-07-017
- [ ] Set up the Codex Figma→code workflow for your next frontend component — *weekend* | action-2026-04-07-018
- [ ] Watch Stanford CS153 AI systems first lecture (free, public) — *quick-win* | action-2026-04-07-019

## Notable Links
- Google AI Agent Traps paper
- Agent Skills repo (Google Cloud AI Director)
- Spec-driven development with AI agents tutorial
- Stanford CS153 first lecture (AI systems course)
- Codex App Server (open-source, from OpenAI)
