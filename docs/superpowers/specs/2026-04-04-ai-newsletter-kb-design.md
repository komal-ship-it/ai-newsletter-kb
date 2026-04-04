# AI Newsletter Knowledge Base — Design Spec

**Date:** 2026-04-04
**Status:** Draft
**Author:** Komal + Claude

## Problem

Komal subscribes to 3-5 AI newsletters (The Batch, TLDR AI, Ben's Bites, Import AI, The Neuron, Superhuman, etc.). Insights get lost because there's no time to properly process them all. There's no way to search across newsletters, track actionable items, or see cross-source patterns.

## Solution

An automated system using a **Claude Code remote trigger** that runs daily, reads newsletters from Gmail via MCP, processes them into structured extractions, and commits results to a git repo. A lightweight local Python CLI enables searching and tracking.

## Architecture

### Two Components

1. **Claude Code Remote Trigger** — Daily scheduled agent that handles the entire pipeline: Gmail fetch, content extraction, structured processing, daily synthesis, git commit/push.
2. **Local Query CLI (`kb.py`)** — Python script for searching the SQLite index, managing actionable items, and viewing digests.

### Data Flow

```
Gmail ──MCP──> Remote Agent ──git push──> Repo ──git pull──> Local CLI
                    |                       |
                    +-- raw/*.md            +-- kb.sqlite (gitignored, rebuilt locally)
                    +-- processed/*.md      +-- kb.py (query tool)
                    +-- daily-digest.md
```

### Key Design Decision: No Separate API Calls

The remote agent IS Claude — it doesn't need to call the Anthropic API separately to process newsletters. This eliminates an entire layer (no API keys, no SDK, no token costs beyond the agent session).

## Newsletter Detection

Three-layer detection, checked in order:

1. **Gmail label** (primary) — User applies `AI-Newsletters` label or sets up Gmail auto-filter. Agent searches: `label:AI-Newsletters after:{last_run_date}`.
2. **Sender whitelist** (fallback) — `config.md` in the repo lists known sender addresses/domains. Agent checks `from:{sender}` for each.
3. **Auto-detect** (last resort) — Agent looks for `List-Unsubscribe` headers and bulk-sender patterns. Flags these as "possible newsletters" for user review rather than auto-processing.

## Content Extraction

For each newsletter email:

1. **Strip boilerplate** — Headers, footers, unsubscribe blocks, social links, ad sections, tracking pixels.
2. **Preserve substance** — Article text, links, embedded images (as URLs), code snippets.
3. **Convert to markdown** — Clean, readable markdown with preserved link URLs.
4. **Split multi-story newsletters** — Most AI newsletters contain 3-10 distinct items. The agent splits these into individual entries within the markdown.

## Structured Processing

### Per-Newsletter Extraction

Each newsletter produces a structured markdown file with these categories:

- **Key Announcements** — New model releases, product launches, company news
- **Tools & Products** — New tools, libraries, frameworks, APIs worth knowing about (with effort rating)
- **Techniques & Methods** — New approaches, architectures, prompting strategies, fine-tuning methods
- **Research Papers** — Notable papers with one-line summaries and links
- **Industry Trends** — Broader patterns or shifts being discussed
- **Actionable Items** — Things to try, ranked by effort: quick-win / weekend / major. Each gets a unique ID (`action-YYYY-MM-DD-NNN`).
- **Notable Links** — Bookmarkable URLs categorized by type

### Daily Synthesis (Cross-Newsletter)

After processing all newsletters, the agent generates `daily-digest.md`:

1. **Consensus signals** — Topics covered by 2+ newsletters (strongest signal)
2. **Contrarian takes** — Where sources disagree
3. **Top 3 actionable items** — Prioritized across all newsletters by effort/impact
4. **Urgent/time-sensitive** — Expiring betas, limited access, deadlines
5. **One-line summary** — Single sentence capturing the day in AI news

## Repository Structure

```
ai-newsletter-kb/
+-- raw/
|   +-- 2026-04-04/
|       +-- the-batch.md
|       +-- tldr-ai.md
+-- processed/
|   +-- 2026-04-04/
|       +-- the-batch.md
|       +-- tldr-ai.md
|       +-- daily-digest.md
+-- config.md                   # sender whitelist, preferences
+-- state.json                  # last run timestamp, processed IDs
+-- kb.sqlite                   # search index (gitignored, rebuilt locally)
+-- kb.py                       # local query CLI
+-- README.md
+-- .gitignore                  # ignores kb.sqlite, __pycache__, .env
```

### SQLite is Gitignored

SQLite is a binary file — bad for git diffs. The markdown files are the source of truth. SQLite is derived and rebuildable:

- `kb.py rebuild` parses all processed markdown and rebuilds the index
- The remote agent only writes markdown and commits — it never touches SQLite
- A git post-merge hook can auto-rebuild after `git pull`

### SQLite Schema

```sql
CREATE TABLE newsletters (
    id TEXT PRIMARY KEY,            -- 'the-batch-2026-04-04'
    source TEXT,                    -- 'The Batch'
    date TEXT,                      -- '2026-04-04'
    raw_path TEXT,
    processed_path TEXT
);

CREATE TABLE items (
    id TEXT PRIMARY KEY,            -- 'action-2026-04-04-001'
    newsletter_id TEXT,
    category TEXT,                  -- 'announcement', 'tool', 'technique', 'paper', 'trend', 'actionable', 'link'
    title TEXT,
    summary TEXT,
    url TEXT,
    effort TEXT,                    -- 'quick-win', 'weekend', 'major' (nullable)
    status TEXT DEFAULT 'pending',  -- 'pending', 'tried', 'skipped'
    date TEXT,
    FOREIGN KEY (newsletter_id) REFERENCES newsletters(id)
);

CREATE TABLE digests (
    date TEXT PRIMARY KEY,
    path TEXT,
    one_line_summary TEXT
);

CREATE VIRTUAL TABLE items_fts USING fts5(title, summary, content=items);
```

## Local Query CLI

### Commands

```bash
python kb.py search "prompting techniques" --days 14
python kb.py search "fine-tuning" --category technique
python kb.py tools --min-sources 2
python kb.py actions
python kb.py actions --effort quick-win
python kb.py actions mark <id> tried|skipped
python kb.py digest
python kb.py digest --date 2026-04-01
python kb.py digest --week
python kb.py stats
python kb.py rebuild
```

### Dependencies

Zero external dependencies — Python standard library only (`sqlite3`, `argparse`, `pathlib`, `json`, `re`).

### Typical Workflow

```bash
git pull
python kb.py rebuild
python kb.py digest
python kb.py actions
python kb.py actions mark action-2026-04-04-001 tried
git add . && git commit -m "mark action tried" && git push
```

## Remote Trigger Configuration

- **Schedule:** Daily at 7 AM ET (`0 11 * * *` UTC)
- **Model:** `claude-sonnet-4-6`
- **Environment:** Anthropic Cloud (default)
- **MCP:** Gmail connector
- **Repo:** GitHub repo `ai-newsletter-kb` (to be created)

### Agent Prompt Structure

The remote agent's prompt instructs it to:

1. Read `state.json` to find `last_run` timestamp
2. Read `config.md` for sender whitelist and preferences
3. Search Gmail for newsletters since `last_run` (label first, then whitelist fallback)
4. For each newsletter: extract, clean, write raw markdown, process into structured extraction
5. Generate daily synthesis/digest
6. Update `state.json` with new timestamp and processed message IDs
7. Commit all changes and push

### Error Handling

Errors are written to `state.json`:

```json
{
  "last_run": "2026-04-04T11:00:00Z",
  "last_run_status": "partial_success",
  "errors": ["Failed to process tldr-ai: email body was empty"]
}
```

### State Tracking

```json
{
  "last_run": "2026-04-04T11:00:00Z",
  "last_processed_ids": ["msg_abc123", "msg_def456"],
  "newsletters_seen": 847
}
```

## Implementation Plan

Build in this order:

1. **GitHub repo setup** — Create repo, initial structure, config.md, .gitignore
2. **Local CLI (`kb.py`)** — Build the query tool and SQLite rebuild logic first (testable without the remote agent)
3. **Remote trigger** — Create the scheduled agent with Gmail MCP, test with a manual run
4. **Iterate on the agent prompt** — Refine extraction quality based on real newsletter content

## Open Questions

- Gmail MCP connector tool surface: exact tool names and parameters need to be discovered during implementation
- Agent prompt will need iterative refinement based on actual extraction quality

## Stretch Goals (Future)

- Weekly synthesis in addition to daily
- Git post-merge hook for auto-rebuild
- Deduplication across newsletters (same story from multiple sources -> one entry)
- Simple local web UI to browse the knowledge base
- Integration with Notion or Obsidian
