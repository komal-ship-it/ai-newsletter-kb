# TLDR — 2026-04-22

**Source:** dan@tldrnewsletter.com
**Date:** 2026-04-22
**Original items:** 12

## Key Announcements
- **SpaceX acquires rights to buy Cursor for $60B** — Or pay $10B for "our work together." SpaceXAI + Cursor working on AI for coding and knowledge work. Cursor separately in talks to raise $2B (a16z, Nvidia, Thrive Capital).
- **ChatGPT Images 2.0** — Thinking capabilities, web search, multi-image generation, 2K resolution; available via gpt-image-2 API.
- **TypeScript 7.0 Beta** — Go-based foundation, ~10x faster than TS 6.0; type-checking logic ported (not rewritten), structurally identical.
- **Anthropic Mythos found 271 Firefox 150 security vulnerabilities** — Mozilla says this sped up the process by months vs automated fuzzing.
- **Claude Code $100/month pricing test** — Anthropic testing on ~2% of new prosumer signups; not yet rolled out broadly.
- **Meta employee tracking for AI training** — Model Capability Initiative tracks mouse, clicks, keystrokes to generate training data for AI agents; US employees only.

## Tools & Products
- **TypeScript 7.0 Beta** — 10x faster type checking via Go port; drop-in replacement for TS 6.0 | https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/ | Effort: weekend
- **ChatGPT Images 2.0 (gpt-image-2)** — Thinking + web search + multi-image + 2K resolution | https://techcrunch.com/2026/04/21/chatgpts-new-images-2-0-model-is-surprisingly-good-at-generating-text/ | Effort: quick-win
- **AWS Lambda S3 file system mounting** — Lambda functions can now mount S3 buckets as file systems | https://aws.amazon.com/about-aws/whats-new/2026/04/aws-lambda-amazon-s3/ | Effort: quick-win

## Techniques & Methods
- **Agents with Taste** — Create a skill file per interface aspect describing rules for what "great" looks and feels like; hand this to coding agents to ground visual quality judgments. Addresses the core problem: agents don't know what tasteful looks like without explicit criteria.

## Research Papers
- None today.

## Industry Trends
- SpaceX/Cursor valuation signals ($60B purchase option) show coding AI is now a strategic asset, not software.
- TypeScript Go port follows Python's similar direction; language toolchain performance becoming a first-class compiler concern.
- Anthropic Mythos used for offensive security research (Firefox vulnerabilities) — AI as a force multiplier for security auditing.
- Claude Code pricing uncertainty: $100/month test on 2% of new users; most existing users unaffected.

## Actionable Items
- [ ] Read "Agents with Taste" and create a taste/style skill file for your UI agent workflows — *quick-win* — https://emilkowal.ski/ui/agents-with-taste | action-2026-04-22-001
- [ ] Try TypeScript 7.0 Beta on a non-critical project to benchmark type-checking speed gain — *weekend* — https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/ | action-2026-04-22-002
- [ ] Enable AWS Lambda S3 file system mounting if running Lambda with large asset reads — *quick-win* — https://aws.amazon.com/about-aws/whats-new/2026/04/aws-lambda-amazon-s3/ | action-2026-04-22-003

## Notable Links
- https://emilkowal.ski/ui/agents-with-taste — Agents with Taste: skill files for visual aesthetics
- https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/ — TypeScript 7.0 Beta announcement
- https://simonwillison.net/2026/Apr/22/claude-code-confusion/ — Claude Code $100/month pricing test analysis
- https://arstechnica.com/ai/2026/04/mozilla-anthropics-mythos-found-271-zero-day-vulnerabilities-in-firefox-150/ — Anthropic Mythos finds 271 Firefox vulnerabilities
- https://aws.amazon.com/about-aws/whats-new/2026/04/aws-lambda-amazon-s3/ — AWS Lambda S3 file system mounting
