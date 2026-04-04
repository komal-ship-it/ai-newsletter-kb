# AI Newsletter Knowledge Base

Automated AI newsletter processing powered by Claude Code remote triggers.

## How It Works

A scheduled Claude Code agent runs daily at 7 AM ET:
1. Reads your Gmail via MCP for new AI newsletters
2. Extracts and processes content into structured markdown
3. Generates a daily synthesis/digest
4. Commits everything to this repo

## Local Usage

```bash
git pull                                    # get latest newsletters
python kb.py rebuild                        # rebuild search index
python kb.py digest                         # today's digest
python kb.py search "prompting" --days 14   # search items
python kb.py actions                        # pending action items
python kb.py actions mark <id> tried        # track progress
```

## Setup

1. Connect Gmail MCP at https://claude.ai/settings/connectors
2. Create the `AI-Newsletters` label in Gmail and apply it to your subscriptions
3. The remote trigger handles the rest automatically

## Requirements

- Python 3.8+
- No pip dependencies (stdlib only)
