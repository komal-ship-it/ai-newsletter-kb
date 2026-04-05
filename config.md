# Newsletter Configuration

## Sender Whitelist

Sender email addresses for AI newsletters. The remote agent checks these
if the `AI-Newsletters` Gmail label returns no results.

### Core AI newsletters
- batch@deeplearning.ai (The Batch — DeepLearning.AI)
- dan@tldrnewsletter.com (TLDR AI)
- post-training@mail.aitinkerers.org (AI Tinkerers — Post-Training)
- aicollectivenewsletter@mail.beehiiv.com (AI Collective)
- thecode@mail.joinsuperhuman.ai (Superhuman — The Code)

### Founder / SaaS / startup ideas
- notifications@mail.ideabrowser.com (Ideabrowser)
- pat@starterstory.com (Pat @ Starter Story)
- hello@saasopportunities.com (SaaS Opportunities)
- ideas@mail.gethalfbaked.com (Half Baked)
- newsletter@indieradar.app (IndieRadar)

### Community / curation
- noreply@skool.com (Skool communities)
- gostroverhovb@gmail.com (personal curated newsletter)

## Preferences

- **Effort levels:** quick-win, weekend, major
- **Action ID format:** action-YYYY-MM-DD-NNN
- **Source slug format:** lowercase-hyphenated

### Slug map
- batch@deeplearning.ai → `the-batch`
- dan@tldrnewsletter.com → `tldr-ai`
- post-training@mail.aitinkerers.org → `ai-tinkerers-post-training`
- aicollectivenewsletter@mail.beehiiv.com → `ai-collective`
- thecode@mail.joinsuperhuman.ai → `superhuman-code`
- notifications@mail.ideabrowser.com → `ideabrowser`
- pat@starterstory.com → `starter-story`
- hello@saasopportunities.com → `saas-opportunities`
- ideas@mail.gethalfbaked.com → `half-baked`
- newsletter@indieradar.app → `indie-radar`
- noreply@skool.com → `skool-{community-name}` (derive from subject line)
- gostroverhovb@gmail.com → `curated-personal`

## Notes

- `noreply@skool.com` sends digests from multiple Skool communities. Use the
  community name from the email subject to derive the slug (e.g.,
  `skool-ai-enthusiasts`, `skool-born-idea`). Skip bare community notifications
  that contain only post/comment counts with no substantive content.
- `gostroverhovb@gmail.com` is a personal curated newsletter. Process if content
  is substantive; skip if it's a personal message rather than a newsletter.
