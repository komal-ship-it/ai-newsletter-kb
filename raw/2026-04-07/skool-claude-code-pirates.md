# Skool — Claude Code Pirates — Raw — 2026-04-07

**Message ID:** 19d63b80e76f9b8a
**From:** noreply@skool.com
**Subject:** Jay Tarzwell posted "Pain-in-the-Ass Claude Code Login Issue Today"
**Date:** 2026-04-06T16:54:58Z

---

Claude Code Pirates

Jay Tarzwell (admin) posted:

Pain-in-the-Ass Claude Code Login Issue Today

What happened: Claude Code quit inside VS Code. When I tried to login, Claude Code kept sending me through Anthropic's browser login, which told me I was signed in. It may or may not be related to v2.1.92.

When I returned to VS Code there was still an OAuth error: timeout of 15000ms exceeded, and 401 authentication_error / expired token messages.

Results of online search with ChatGPT: There are current GitHub reports from other users seeing the same pattern: OAuth timeout, interrupted login, and fresh logins that still end up with expired-token style errors. Anthropic's CLI docs also show this is all part of the auth flow, not some random repo issue.

What fixed it for me without doing anything destructive:
- quit — log out fully
- open terminal
- run the auth commands from shell

Do this: Open your Terminal — do not use the VS Code terminal.

Then run these two terminal commands one after the other:
1. claude auth logout
2. claude auth login

If you are already stuck inside Claude Code, quit first.

Also: ChatGPT saved the day. This is a good reminder why having more than one LLM is useful. I used ChatGPT to help troubleshoot Claude Code, cross-check docs, look at current bug reports, and narrow it down without immediately going nuclear on config files.

Moral of the story: When one model/tool is the thing that's broken, having a second one around is handy.
