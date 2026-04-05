# Newsletter Configuration

## Sender Whitelist

Sender email addresses for AI newsletters. The remote agent checks these
if the `AI-Newsletters` Gmail label returns no results.

- noreply@skool.com (AI Enthusiasts community)
- notifications@mail.ideabrowser.com (Ideabrowser)
- pat@starterstory.com (Pat @ Starter Story)
- post-training@mail.aitinkerers.org (AI Tinkerers — Post-Training)

## Preferences

- **Effort levels:** quick-win, weekend, major
- **Action ID format:** action-YYYY-MM-DD-NNN
- **Source slug format:** lowercase-hyphenated
  - noreply@skool.com → `ai-enthusiasts-skool`
  - notifications@mail.ideabrowser.com → `ideabrowser`
  - pat@starterstory.com → `starter-story`
  - post-training@mail.aitinkerers.org → `ai-tinkerers-post-training`

## Notes

- `noreply@skool.com` may also send non-newsletter notifications (comments, replies).
  The agent should filter for newsletter/digest content and skip bare notifications.
