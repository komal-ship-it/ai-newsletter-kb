# Skool — Claude Code Pirates — 2026-04-07

**Source:** noreply@skool.com (Claude Code Pirates community)
**Date:** 2026-04-07
**Original items:** 1

## Key Announcements
- **Claude Code OAuth login bug (v2.1.92)** — Users hitting OAuth timeout (15000ms exceeded), 401 authentication_error / expired token after browser login completes. Confirmed across multiple GitHub reports.

## Tools & Products
- None today.

## Techniques & Methods
- **Claude Code auth recovery (no destructive steps):**
  1. Quit Claude Code entirely
  2. Open your system terminal (NOT VS Code integrated terminal)
  3. Run: `claude auth logout`
  4. Run: `claude auth login`
  - Root cause: VS Code terminal interferes with OAuth redirect flow. System terminal resolves the timeout.
- **Multi-LLM debugging** — When one AI tool is the broken thing, use a second AI to troubleshoot it. Jay Tarzwell used ChatGPT to diagnose the Claude Code auth issue and cross-reference GitHub bug reports.

## Research Papers
- None today.

## Industry Trends
- Claude Code v2.1.92 auth regression affecting VS Code users
- Multi-LLM workflows as a resilience pattern gaining mindshare in practitioner communities

## Actionable Items
- [ ] If experiencing Claude Code auth issues in VS Code: quit, open system terminal, run `claude auth logout` then `claude auth login` — *quick-win* | action-2026-04-07-024

## Notable Links
- GitHub issue reports for Claude Code OAuth timeout (search: Claude Code OAuth timeout 15000ms expired token)
