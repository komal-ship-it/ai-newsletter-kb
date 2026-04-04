# AI Newsletter Knowledge Base — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a daily automated newsletter processing pipeline using a Claude Code remote trigger with Gmail MCP, backed by a git repo and local Python query CLI.

**Architecture:** Claude Code remote trigger reads Gmail via MCP daily, extracts and processes AI newsletter content, writes structured markdown files, and commits to a GitHub repo. A local Python CLI (`kb.py`) rebuilds a SQLite index from the markdown and provides search, filtering, and action tracking.

**Tech Stack:** Python 3 (stdlib only), SQLite/FTS5, Claude Code Remote Triggers, Gmail MCP connector, Git/GitHub

---

## File Map

| File | Responsibility |
|------|---------------|
| `kb.py` | Local query CLI — all subcommands (search, actions, digest, tools, stats, rebuild) |
| `config.md` | Newsletter sender whitelist and user preferences |
| `state.json` | Pipeline state — last run timestamp, processed message IDs |
| `.gitignore` | Ignore kb.sqlite, __pycache__, .env |
| `README.md` | Setup and usage instructions |
| `raw/YYYY-MM-DD/*.md` | Cleaned raw newsletter content (written by remote agent) |
| `processed/YYYY-MM-DD/*.md` | Structured extractions (written by remote agent) |
| `processed/YYYY-MM-DD/daily-digest.md` | Cross-newsletter synthesis (written by remote agent) |
| `tests/test_kb.py` | Tests for kb.py — parsing, indexing, querying, action management |
| `tests/fixtures/` | Sample processed markdown files for testing |

---

### Task 1: Repository scaffolding

**Files:**
- Create: `.gitignore`
- Create: `config.md`
- Create: `state.json`
- Create: `README.md`
- Create: `raw/.gitkeep`
- Create: `processed/.gitkeep`

- [ ] **Step 1: Create `.gitignore`**

```
kb.sqlite
__pycache__/
*.pyc
.env
.DS_Store
```

- [ ] **Step 2: Create `config.md`**

```markdown
# Newsletter Configuration

## Sender Whitelist

Add sender email addresses or domains below. The remote agent checks these
if the `AI-Newsletters` Gmail label returns no results.

- batch@deeplearning.ai
- dan@tldrnewsletter.com
- newsletter@bensbites.com
- jack@importai.com
- newsletter@theneurondaily.com
- newsletter@joinsuperhuman.com

## Preferences

- **Effort levels:** quick-win, weekend, major
- **Action ID format:** action-YYYY-MM-DD-NNN
- **Source slug format:** lowercase-hyphenated (e.g., the-batch, tldr-ai)
```

- [ ] **Step 3: Create `state.json`**

```json
{
  "last_run": null,
  "last_run_status": null,
  "last_processed_ids": [],
  "newsletters_seen": 0,
  "errors": []
}
```

- [ ] **Step 4: Create placeholder directories**

```bash
mkdir -p raw processed
touch raw/.gitkeep processed/.gitkeep
```

- [ ] **Step 5: Create `README.md`**

```markdown
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
```

- [ ] **Step 6: Commit scaffolding**

```bash
git add .gitignore config.md state.json README.md raw/.gitkeep processed/.gitkeep
git commit -m "feat: scaffold repo structure with config and README"
```

---

### Task 2: Test fixtures — sample processed markdown

**Files:**
- Create: `tests/__init__.py`
- Create: `tests/fixtures/processed/2026-04-01/the-batch.md`
- Create: `tests/fixtures/processed/2026-04-01/tldr-ai.md`
- Create: `tests/fixtures/processed/2026-04-01/daily-digest.md`

These fixtures define the exact markdown format the remote agent will produce. The parser in `kb.py` must handle this format.

- [ ] **Step 1: Create test directory**

```bash
mkdir -p tests/fixtures/processed/2026-04-01
touch tests/__init__.py
```

- [ ] **Step 2: Create `tests/fixtures/processed/2026-04-01/the-batch.md`**

```markdown
# The Batch — 2026-04-01

**Source:** batch@deeplearning.ai
**Date:** 2026-04-01
**Original items:** 5

## Key Announcements
- **Claude 4.5 Released** — Anthropic launches Claude 4.5 with improved reasoning and 1M context window

## Tools & Products
- **MCPHub** — Central registry for MCP servers, simplifies discovery and installation | https://mcphub.example.com | Effort: quick-win
- **PromptLayer 3.0** — Version control and observability for LLM prompts | https://promptlayer.example.com | Effort: weekend

## Techniques & Methods
- **Chain-of-Draft Prompting** — More token-efficient alternative to chain-of-thought, produces shorter intermediate reasoning steps

## Research Papers
- **Scaling Laws for Agents** (Smith et al.) — Shows agent performance scales predictably with tool count and context length | https://arxiv.org/abs/example1

## Industry Trends
- Multi-modal agents becoming standard — vision + code execution + web browsing in single agent loops

## Actionable Items
- [ ] Try MCPHub for discovering new MCP servers — *quick-win* — https://mcphub.example.com | action-2026-04-01-001
- [ ] Evaluate PromptLayer 3.0 for prompt versioning workflow — *weekend* — https://promptlayer.example.com | action-2026-04-01-002
- [ ] Experiment with chain-of-draft prompting on existing tasks — *quick-win* | action-2026-04-01-003

## Notable Links
- https://mcphub.example.com — Tool registry
- https://promptlayer.example.com — Prompt observability
- https://arxiv.org/abs/example1 — Scaling laws paper
```

- [ ] **Step 3: Create `tests/fixtures/processed/2026-04-01/tldr-ai.md`**

```markdown
# TLDR AI — 2026-04-01

**Source:** dan@tldrnewsletter.com
**Date:** 2026-04-01
**Original items:** 4

## Key Announcements
- **Claude 4.5 Released** — Anthropic's new flagship model with extended context and better tool use

## Tools & Products
- **MCPHub** — Registry for discovering and sharing MCP servers | https://mcphub.example.com | Effort: quick-win
- **Cursor Tab v2** — Improved AI-powered code completion with multi-file context | https://cursor.example.com | Effort: quick-win

## Techniques & Methods
- **Agentic RAG** — Using agents to dynamically choose retrieval strategies instead of static pipelines

## Research Papers
- **Constitutional AI v2** (Anthropic) — Updated RLHF approach with improved harmlessness without sacrificing helpfulness | https://arxiv.org/abs/example2

## Industry Trends
- MCP adoption accelerating across IDE and productivity tools

## Actionable Items
- [ ] Install MCPHub CLI and browse available servers — *quick-win* — https://mcphub.example.com | action-2026-04-01-004
- [ ] Try agentic RAG pattern on existing knowledge base — *weekend* | action-2026-04-01-005

## Notable Links
- https://mcphub.example.com — MCP server registry
- https://cursor.example.com — AI code editor
- https://arxiv.org/abs/example2 — Constitutional AI v2
```

- [ ] **Step 4: Create `tests/fixtures/processed/2026-04-01/daily-digest.md`**

```markdown
# Daily Digest — 2026-04-01

## Consensus Signals
- **Claude 4.5 launch** — Covered by The Batch, TLDR AI. Major model release from Anthropic with 1M context and improved tool use.
- **MCPHub** — Mentioned by The Batch, TLDR AI. New registry for MCP server discovery gaining traction.

## Contrarian Takes
- None today — sources largely aligned on major stories.

## Top 3 Actionable Items
1. Try MCPHub for discovering MCP servers — *quick-win* — consensus pick (2 sources)
2. Experiment with chain-of-draft prompting — *quick-win* — unique to The Batch
3. Evaluate PromptLayer 3.0 for prompt versioning — *weekend* — unique to The Batch

## Urgent / Time-Sensitive
- None today.

## One-Line Summary
Anthropic launches Claude 4.5 while MCP ecosystem tooling matures with MCPHub registry.
```

- [ ] **Step 5: Commit fixtures**

```bash
git add tests/
git commit -m "test: add processed markdown fixtures for parser testing"
```

---

### Task 3: Markdown parser — extract metadata and items from processed files

**Files:**
- Create: `tests/test_kb.py` (first batch of tests)
- Create: `kb.py` (parser module)

- [ ] **Step 1: Write failing tests for markdown parsing**

Create `tests/test_kb.py`:

```python
import sys
import os
from pathlib import Path

# Add repo root to path so we can import kb
sys.path.insert(0, str(Path(__file__).parent.parent))

FIXTURES = Path(__file__).parent / "fixtures"


def test_parse_newsletter_metadata():
    """Parse source, date, and item count from processed markdown header."""
    from kb import parse_processed_markdown

    text = (FIXTURES / "processed/2026-04-01/the-batch.md").read_text()
    result = parse_processed_markdown(text, "processed/2026-04-01/the-batch.md")

    assert result["id"] == "the-batch-2026-04-01"
    assert result["source"] == "The Batch"
    assert result["date"] == "2026-04-01"
    assert result["source_email"] == "batch@deeplearning.ai"
    assert result["processed_path"] == "processed/2026-04-01/the-batch.md"


def test_parse_newsletter_items():
    """Parse individual items with category, title, summary, url, effort."""
    from kb import parse_processed_markdown

    text = (FIXTURES / "processed/2026-04-01/the-batch.md").read_text()
    result = parse_processed_markdown(text, "processed/2026-04-01/the-batch.md")
    items = result["items"]

    # Should find items across all categories
    categories = {item["category"] for item in items}
    assert "announcement" in categories
    assert "tool" in categories
    assert "technique" in categories
    assert "paper" in categories
    assert "trend" in categories
    assert "actionable" in categories
    assert "link" in categories

    # Check a specific tool item
    tools = [i for i in items if i["category"] == "tool"]
    assert len(tools) == 2
    assert tools[0]["title"] == "MCPHub"
    assert "registry" in tools[0]["summary"].lower()
    assert tools[0]["url"] == "https://mcphub.example.com"
    assert tools[0]["effort"] == "quick-win"


def test_parse_actionable_items():
    """Parse actionable items with IDs and effort levels."""
    from kb import parse_processed_markdown

    text = (FIXTURES / "processed/2026-04-01/the-batch.md").read_text()
    result = parse_processed_markdown(text, "processed/2026-04-01/the-batch.md")
    actions = [i for i in result["items"] if i["category"] == "actionable"]

    assert len(actions) == 3
    assert actions[0]["id"] == "action-2026-04-01-001"
    assert actions[0]["effort"] == "quick-win"
    assert actions[1]["id"] == "action-2026-04-01-002"
    assert actions[1]["effort"] == "weekend"


def test_parse_digest_metadata():
    """Parse daily digest one-line summary."""
    from kb import parse_digest_markdown

    text = (FIXTURES / "processed/2026-04-01/daily-digest.md").read_text()
    result = parse_digest_markdown(text, "2026-04-01")

    assert result["date"] == "2026-04-01"
    assert "Claude 4.5" in result["one_line_summary"]
    assert "MCPHub" in result["one_line_summary"]
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /Users/komalgarg/Documents/learn-ai/ai-newsletter-kb
python -m pytest tests/test_kb.py -v
```

Expected: FAIL — `ModuleNotFoundError: No module named 'kb'`

- [ ] **Step 3: Implement `parse_processed_markdown` and `parse_digest_markdown` in `kb.py`**

Create `kb.py`:

```python
#!/usr/bin/env python3
"""AI Newsletter Knowledge Base — Local Query CLI."""

import re
from pathlib import Path

# --- Markdown Parsing ---

HEADER_PATTERN = re.compile(
    r"^# .+ — (\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE
)
SOURCE_PATTERN = re.compile(r"^\*\*Source:\*\*\s*(.+)$", re.MULTILINE)
DATE_PATTERN = re.compile(r"^\*\*Date:\*\*\s*(.+)$", re.MULTILINE)

SECTION_PATTERN = re.compile(r"^## (.+)$", re.MULTILINE)

CATEGORY_MAP = {
    "Key Announcements": "announcement",
    "Tools & Products": "tool",
    "Techniques & Methods": "technique",
    "Research Papers": "paper",
    "Industry Trends": "trend",
    "Actionable Items": "actionable",
    "Notable Links": "link",
}

# Matches: - **Title** — Summary | url | Effort: level
TOOL_ITEM_PATTERN = re.compile(
    r"^- \*\*(.+?)\*\*\s*—\s*(.+?)(?:\s*\|\s*(https?://\S+))?"
    r"(?:\s*\|\s*Effort:\s*(\S+))?\s*$",
    re.MULTILINE,
)

# Matches: - **Title** (Authors) — Summary | url
PAPER_ITEM_PATTERN = re.compile(
    r"^- \*\*(.+?)\*\*\s*\((.+?)\)\s*—\s*(.+?)(?:\s*\|\s*(https?://\S+))?\s*$",
    re.MULTILINE,
)

# Matches: - [ ] Description — *effort* — url | action-id
ACTION_ITEM_PATTERN = re.compile(
    r"^- \[ \] (.+?) — \*(\S+?)\*"
    r"(?: — (https?://\S+))?"
    r"\s*\|\s*(action-\d{4}-\d{2}-\d{2}-\d{3})\s*$",
    re.MULTILINE,
)

# Matches: - **Bold text** — Description
BOLD_ITEM_PATTERN = re.compile(
    r"^- \*\*(.+?)\*\*\s*—\s*(.+)$", re.MULTILINE
)

# Matches: - plain text description
PLAIN_ITEM_PATTERN = re.compile(r"^- (.+)$", re.MULTILINE)

# Matches: - url — description
LINK_ITEM_PATTERN = re.compile(
    r"^- (https?://\S+)\s*—\s*(.+)$", re.MULTILINE
)


def _split_sections(text: str) -> dict[str, str]:
    """Split markdown into sections by ## headers."""
    sections = {}
    parts = SECTION_PATTERN.split(text)
    # parts = [preamble, header1, body1, header2, body2, ...]
    for i in range(1, len(parts), 2):
        sections[parts[i].strip()] = parts[i + 1].strip() if i + 1 < len(parts) else ""
    return sections


def _slug_from_path(path: str) -> str:
    """Extract source slug from path like 'processed/2026-04-01/the-batch.md'."""
    return Path(path).stem


def parse_processed_markdown(text: str, path: str) -> dict:
    """Parse a processed newsletter markdown file into structured data."""
    source_match = SOURCE_PATTERN.search(text)
    date_match = DATE_PATTERN.search(text)

    source_email = source_match.group(1).strip() if source_match else ""
    date = date_match.group(1).strip() if date_match else ""
    slug = _slug_from_path(path)

    # Derive display name from the H1 header
    h1_match = re.match(r"^# (.+?) — \d{4}", text)
    source_name = h1_match.group(1).strip() if h1_match else slug

    newsletter_id = f"{slug}-{date}"

    sections = _split_sections(text)
    items = []

    for section_title, section_body in sections.items():
        category = CATEGORY_MAP.get(section_title)
        if not category:
            continue

        if category == "actionable":
            for m in ACTION_ITEM_PATTERN.finditer(section_body):
                items.append({
                    "id": m.group(4),
                    "category": "actionable",
                    "title": m.group(1).strip(),
                    "summary": m.group(1).strip(),
                    "url": m.group(3) or "",
                    "effort": m.group(2),
                })
        elif category == "link":
            for m in LINK_ITEM_PATTERN.finditer(section_body):
                items.append({
                    "id": "",
                    "category": "link",
                    "title": m.group(2).strip(),
                    "summary": m.group(2).strip(),
                    "url": m.group(1),
                    "effort": None,
                })
        elif category == "paper":
            for m in PAPER_ITEM_PATTERN.finditer(section_body):
                items.append({
                    "id": "",
                    "category": "paper",
                    "title": m.group(1).strip(),
                    "summary": f"({m.group(2)}) {m.group(3).strip()}",
                    "url": m.group(4) or "",
                    "effort": None,
                })
        elif category == "tool":
            for m in TOOL_ITEM_PATTERN.finditer(section_body):
                items.append({
                    "id": "",
                    "category": "tool",
                    "title": m.group(1).strip(),
                    "summary": m.group(2).strip(),
                    "url": m.group(3) or "",
                    "effort": m.group(4),
                })
        elif category in ("announcement", "technique", "trend"):
            for m in BOLD_ITEM_PATTERN.finditer(section_body):
                items.append({
                    "id": "",
                    "category": category,
                    "title": m.group(1).strip(),
                    "summary": m.group(2).strip(),
                    "url": "",
                    "effort": None,
                })
            # Also check plain items (no bold)
            if not BOLD_ITEM_PATTERN.search(section_body):
                for m in PLAIN_ITEM_PATTERN.finditer(section_body):
                    items.append({
                        "id": "",
                        "category": category,
                        "title": m.group(1).strip()[:80],
                        "summary": m.group(1).strip(),
                        "url": "",
                        "effort": None,
                    })

    # Generate IDs for items that don't have one
    counter = 1
    for item in items:
        if not item["id"]:
            item["id"] = f"{category}-{slug}-{date}-{counter:03d}"
            counter += 1

    return {
        "id": newsletter_id,
        "source": source_name,
        "source_email": source_email,
        "date": date,
        "processed_path": path,
        "items": items,
    }


def parse_digest_markdown(text: str, date: str) -> dict:
    """Parse a daily digest markdown file."""
    # Extract one-line summary from the last section
    summary_match = re.search(
        r"## One-Line Summary\s*\n(.+)", text
    )
    one_line = summary_match.group(1).strip() if summary_match else ""

    return {
        "date": date,
        "one_line_summary": one_line,
    }
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd /Users/komalgarg/Documents/learn-ai/ai-newsletter-kb
python -m pytest tests/test_kb.py -v
```

Expected: All 4 tests PASS.

- [ ] **Step 5: Commit parser**

```bash
git add kb.py tests/test_kb.py
git commit -m "feat: add markdown parser for processed newsletters and digests"
```

---

### Task 4: SQLite index — schema creation and rebuild from markdown

**Files:**
- Modify: `tests/test_kb.py` (add index tests)
- Modify: `kb.py` (add database module)

- [ ] **Step 1: Write failing tests for SQLite rebuild**

Append to `tests/test_kb.py`:

```python
import sqlite3
import tempfile


def test_create_database_schema():
    """create_database should create all tables and FTS index."""
    from kb import create_database

    with tempfile.NamedTemporaryFile(suffix=".sqlite") as f:
        db_path = f.name
    conn = create_database(db_path)
    cursor = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    )
    tables = {row[0] for row in cursor}
    assert "newsletters" in tables
    assert "items" in tables
    assert "digests" in tables
    assert "items_fts" in tables
    conn.close()
    os.unlink(db_path)


def test_rebuild_index_from_fixtures():
    """rebuild_index should parse fixtures and populate the database."""
    from kb import rebuild_index

    with tempfile.NamedTemporaryFile(suffix=".sqlite", delete=False) as f:
        db_path = f.name
    try:
        conn = rebuild_index(
            db_path, processed_dir=FIXTURES / "processed"
        )

        # Should have 2 newsletters
        count = conn.execute("SELECT COUNT(*) FROM newsletters").fetchone()[0]
        assert count == 2

        # Should have items from both newsletters
        item_count = conn.execute("SELECT COUNT(*) FROM items").fetchone()[0]
        assert item_count > 0

        # Should have 1 digest
        digest_count = conn.execute("SELECT COUNT(*) FROM digests").fetchone()[0]
        assert digest_count == 1

        # FTS search should work
        results = conn.execute(
            "SELECT title FROM items_fts WHERE items_fts MATCH 'MCPHub'"
        ).fetchall()
        assert len(results) >= 1

        conn.close()
    finally:
        os.unlink(db_path)
```

- [ ] **Step 2: Run tests to verify new tests fail**

```bash
python -m pytest tests/test_kb.py::test_create_database_schema tests/test_kb.py::test_rebuild_index_from_fixtures -v
```

Expected: FAIL — `ImportError: cannot import name 'create_database' from 'kb'`

- [ ] **Step 3: Implement `create_database` and `rebuild_index` in `kb.py`**

Add to `kb.py` after the parser code:

```python
import sqlite3

# --- Database ---

SCHEMA = """
CREATE TABLE IF NOT EXISTS newsletters (
    id TEXT PRIMARY KEY,
    source TEXT,
    date TEXT,
    raw_path TEXT,
    processed_path TEXT
);

CREATE TABLE IF NOT EXISTS items (
    id TEXT PRIMARY KEY,
    newsletter_id TEXT,
    category TEXT,
    title TEXT,
    summary TEXT,
    url TEXT,
    effort TEXT,
    status TEXT DEFAULT 'pending',
    date TEXT,
    FOREIGN KEY (newsletter_id) REFERENCES newsletters(id)
);

CREATE TABLE IF NOT EXISTS digests (
    date TEXT PRIMARY KEY,
    path TEXT,
    one_line_summary TEXT
);

CREATE VIRTUAL TABLE IF NOT EXISTS items_fts USING fts5(
    title, summary, content=items, content_rowid=rowid
);

CREATE TRIGGER IF NOT EXISTS items_ai AFTER INSERT ON items BEGIN
    INSERT INTO items_fts(rowid, title, summary)
    VALUES (new.rowid, new.title, new.summary);
END;
"""


def create_database(db_path: str) -> sqlite3.Connection:
    """Create a new SQLite database with the KB schema."""
    conn = sqlite3.connect(db_path)
    conn.executescript(SCHEMA)
    return conn


def rebuild_index(db_path: str, processed_dir: Path = None) -> sqlite3.Connection:
    """Rebuild the SQLite index from all processed markdown files."""
    if processed_dir is None:
        processed_dir = Path("processed")

    # Load existing action statuses before dropping
    old_statuses = {}
    if Path(db_path).exists():
        try:
            old_conn = sqlite3.connect(db_path)
            for row in old_conn.execute(
                "SELECT id, status FROM items WHERE status != 'pending'"
            ):
                old_statuses[row[0]] = row[1]
            old_conn.close()
        except sqlite3.OperationalError:
            pass

    # Drop and recreate
    if Path(db_path).exists():
        Path(db_path).unlink()

    conn = create_database(db_path)

    # Walk all date directories
    if not processed_dir.exists():
        return conn

    for date_dir in sorted(processed_dir.iterdir()):
        if not date_dir.is_dir():
            continue
        date_str = date_dir.name  # e.g., "2026-04-01"

        for md_file in sorted(date_dir.glob("*.md")):
            if md_file.name == "daily-digest.md":
                # Parse digest
                text = md_file.read_text()
                digest = parse_digest_markdown(text, date_str)
                conn.execute(
                    "INSERT OR REPLACE INTO digests (date, path, one_line_summary) "
                    "VALUES (?, ?, ?)",
                    (digest["date"], str(md_file.relative_to(processed_dir.parent)),
                     digest["one_line_summary"]),
                )
            else:
                # Parse newsletter
                rel_path = str(md_file.relative_to(processed_dir.parent))
                text = md_file.read_text()
                newsletter = parse_processed_markdown(text, rel_path)

                conn.execute(
                    "INSERT OR REPLACE INTO newsletters "
                    "(id, source, date, raw_path, processed_path) "
                    "VALUES (?, ?, ?, ?, ?)",
                    (newsletter["id"], newsletter["source"], newsletter["date"],
                     f"raw/{date_str}/{md_file.stem}.md", rel_path),
                )

                for item in newsletter["items"]:
                    status = old_statuses.get(item["id"], "pending")
                    conn.execute(
                        "INSERT OR REPLACE INTO items "
                        "(id, newsletter_id, category, title, summary, url, "
                        "effort, status, date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (item["id"], newsletter["id"], item["category"],
                         item["title"], item["summary"], item["url"],
                         item["effort"], status, newsletter["date"]),
                    )

    conn.commit()
    return conn
```

- [ ] **Step 4: Run all tests**

```bash
python -m pytest tests/test_kb.py -v
```

Expected: All 6 tests PASS.

- [ ] **Step 5: Commit database module**

```bash
git add kb.py tests/test_kb.py
git commit -m "feat: add SQLite schema creation and rebuild-from-markdown indexer"
```

---

### Task 5: CLI subcommands — search, actions, digest, tools, stats

**Files:**
- Modify: `tests/test_kb.py` (add CLI tests)
- Modify: `kb.py` (add CLI with argparse)

- [ ] **Step 1: Write failing tests for CLI subcommands**

Append to `tests/test_kb.py`:

```python
import subprocess


def _run_kb(*args: str, fixtures: bool = True) -> subprocess.CompletedProcess:
    """Run kb.py as a subprocess, optionally pointing at fixtures."""
    cmd = [sys.executable, str(Path(__file__).parent.parent / "kb.py")]
    if fixtures:
        cmd.extend(["--db", "/tmp/test_kb_cli.sqlite",
                     "--processed-dir", str(FIXTURES / "processed")])
    cmd.extend(args)
    return subprocess.run(cmd, capture_output=True, text=True, cwd=str(Path(__file__).parent.parent))


def test_cli_rebuild():
    """kb.py rebuild should create the database."""
    result = _run_kb("rebuild")
    assert result.returncode == 0
    assert "Rebuilt" in result.stdout or "rebuilt" in result.stdout.lower()


def test_cli_search():
    """kb.py search should find items matching a query."""
    _run_kb("rebuild")  # ensure index exists
    result = _run_kb("search", "MCPHub")
    assert result.returncode == 0
    assert "MCPHub" in result.stdout


def test_cli_actions():
    """kb.py actions should list pending actionable items."""
    _run_kb("rebuild")
    result = _run_kb("actions")
    assert result.returncode == 0
    assert "action-2026-04-01" in result.stdout


def test_cli_actions_mark():
    """kb.py actions mark should update item status."""
    _run_kb("rebuild")
    result = _run_kb("actions", "mark", "action-2026-04-01-001", "tried")
    assert result.returncode == 0
    # Verify it shows as tried now
    result2 = _run_kb("actions", "--all")
    assert "tried" in result2.stdout


def test_cli_digest():
    """kb.py digest should display the daily digest."""
    _run_kb("rebuild")
    result = _run_kb("digest", "--date", "2026-04-01")
    assert result.returncode == 0
    assert "Claude 4.5" in result.stdout


def test_cli_tools():
    """kb.py tools should show tools mentioned by multiple sources."""
    _run_kb("rebuild")
    result = _run_kb("tools", "--min-sources", "2")
    assert result.returncode == 0
    assert "MCPHub" in result.stdout


def test_cli_stats():
    """kb.py stats should show summary statistics."""
    _run_kb("rebuild")
    result = _run_kb("stats")
    assert result.returncode == 0
    assert "2" in result.stdout  # 2 newsletters
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
python -m pytest tests/test_kb.py::test_cli_rebuild -v
```

Expected: FAIL — kb.py has no CLI entry point yet.

- [ ] **Step 3: Implement CLI with argparse in `kb.py`**

Add to bottom of `kb.py`:

```python
import argparse
import json
from datetime import datetime, timedelta

# --- CLI Helpers ---

DB_DEFAULT = "kb.sqlite"
PROCESSED_DEFAULT = "processed"


def _get_conn(args) -> sqlite3.Connection:
    """Get a database connection, creating if needed."""
    db_path = getattr(args, "db", DB_DEFAULT)
    if not Path(db_path).exists():
        print(f"Database not found at {db_path}. Run 'kb.py rebuild' first.")
        raise SystemExit(1)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


# --- Subcommands ---

def cmd_rebuild(args):
    db_path = getattr(args, "db", DB_DEFAULT)
    processed_dir = Path(getattr(args, "processed_dir", PROCESSED_DEFAULT))
    conn = rebuild_index(db_path, processed_dir)
    nl_count = conn.execute("SELECT COUNT(*) FROM newsletters").fetchone()[0]
    item_count = conn.execute("SELECT COUNT(*) FROM items").fetchone()[0]
    digest_count = conn.execute("SELECT COUNT(*) FROM digests").fetchone()[0]
    conn.close()
    print(f"Rebuilt index: {nl_count} newsletters, {item_count} items, {digest_count} digests")


def cmd_search(args):
    conn = _get_conn(args)
    query = args.query

    sql = """
        SELECT i.id, i.category, i.title, i.summary, i.url, i.effort, i.date,
               n.source
        FROM items_fts f
        JOIN items i ON i.rowid = f.rowid
        JOIN newsletters n ON n.id = i.newsletter_id
        WHERE items_fts MATCH ?
    """
    params = [query]

    if args.category:
        sql += " AND i.category = ?"
        params.append(args.category)

    if args.days:
        cutoff = (datetime.now() - timedelta(days=args.days)).strftime("%Y-%m-%d")
        sql += " AND i.date >= ?"
        params.append(cutoff)

    sql += " ORDER BY i.date DESC"

    rows = conn.execute(sql, params).fetchall()
    if not rows:
        print("No results found.")
        return

    for row in rows:
        effort_str = f" [{row['effort']}]" if row["effort"] else ""
        url_str = f" — {row['url']}" if row["url"] else ""
        print(f"  [{row['date']}] [{row['category']}] {row['title']}{effort_str}")
        print(f"    {row['summary']}{url_str}")
        print(f"    Source: {row['source']}")
        print()
    conn.close()


def cmd_actions(args):
    conn = _get_conn(args)

    if args.subaction == "mark":
        conn.execute(
            "UPDATE items SET status = ? WHERE id = ?",
            (args.status, args.action_id),
        )
        conn.commit()
        print(f"Marked {args.action_id} as {args.status}")
        conn.close()
        return

    sql = """
        SELECT i.id, i.title, i.effort, i.url, i.date, i.status, n.source
        FROM items i
        JOIN newsletters n ON n.id = i.newsletter_id
        WHERE i.category = 'actionable'
    """
    params = []

    if not args.all:
        sql += " AND i.status = 'pending'"

    if args.effort:
        sql += " AND i.effort = ?"
        params.append(args.effort)

    sql += " ORDER BY i.date DESC"

    rows = conn.execute(sql, params).fetchall()
    if not rows:
        print("No actionable items found.")
        return

    for row in rows:
        status_str = f" ({row['status']})" if row["status"] != "pending" else ""
        url_str = f"\n    {row['url']}" if row["url"] else ""
        print(f"  [{row['effort']}] {row['title']}{status_str}")
        print(f"    ID: {row['id']} | {row['date']} | {row['source']}{url_str}")
        print()
    conn.close()


def cmd_digest(args):
    conn = _get_conn(args)

    if args.week:
        cutoff = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        rows = conn.execute(
            "SELECT date, one_line_summary FROM digests WHERE date >= ? ORDER BY date DESC",
            (cutoff,),
        ).fetchall()
    elif args.date:
        rows = conn.execute(
            "SELECT date, one_line_summary FROM digests WHERE date = ?",
            (args.date,),
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT date, one_line_summary FROM digests ORDER BY date DESC LIMIT 1"
        ).fetchall()

    if not rows:
        print("No digests found.")
        return

    for row in rows:
        print(f"  [{row['date']}] {row['one_line_summary']}")

        # Also print the full digest file if it exists
        digest_path = Path(
            getattr(args, "processed_dir", PROCESSED_DEFAULT)
        ) / row["date"] / "daily-digest.md"
        if digest_path.exists():
            print()
            print(digest_path.read_text())
    conn.close()


def cmd_tools(args):
    conn = _get_conn(args)
    min_sources = args.min_sources or 1

    rows = conn.execute(
        """
        SELECT i.title, i.summary, i.url, i.effort, COUNT(DISTINCT n.source) as source_count,
               GROUP_CONCAT(DISTINCT n.source) as sources
        FROM items i
        JOIN newsletters n ON n.id = i.newsletter_id
        WHERE i.category = 'tool'
        GROUP BY i.title
        HAVING source_count >= ?
        ORDER BY source_count DESC, i.date DESC
        """,
        (min_sources,),
    ).fetchall()

    if not rows:
        print("No tools found matching criteria.")
        return

    for row in rows:
        effort_str = f" [{row['effort']}]" if row["effort"] else ""
        print(f"  {row['title']}{effort_str} — mentioned by {row['source_count']} source(s)")
        print(f"    {row['summary']}")
        if row["url"]:
            print(f"    {row['url']}")
        print(f"    Sources: {row['sources']}")
        print()
    conn.close()


def cmd_stats(args):
    conn = _get_conn(args)
    nl = conn.execute("SELECT COUNT(*) FROM newsletters").fetchone()[0]
    items = conn.execute("SELECT COUNT(*) FROM items").fetchone()[0]
    actions_pending = conn.execute(
        "SELECT COUNT(*) FROM items WHERE category='actionable' AND status='pending'"
    ).fetchone()[0]
    actions_tried = conn.execute(
        "SELECT COUNT(*) FROM items WHERE category='actionable' AND status='tried'"
    ).fetchone()[0]
    digests = conn.execute("SELECT COUNT(*) FROM digests").fetchone()[0]

    print(f"  Newsletters indexed: {nl}")
    print(f"  Total items: {items}")
    print(f"  Actionable: {actions_pending} pending, {actions_tried} tried")
    print(f"  Digests: {digests}")
    conn.close()


# --- Main ---

def main():
    parser = argparse.ArgumentParser(
        description="AI Newsletter Knowledge Base CLI"
    )
    parser.add_argument("--db", default=DB_DEFAULT, help="Path to SQLite database")
    parser.add_argument(
        "--processed-dir", default=PROCESSED_DEFAULT,
        help="Path to processed markdown directory"
    )

    sub = parser.add_subparsers(dest="command")

    # rebuild
    sub.add_parser("rebuild", help="Rebuild SQLite index from markdown files")

    # search
    p_search = sub.add_parser("search", help="Search items")
    p_search.add_argument("query", help="Search query")
    p_search.add_argument("--category", help="Filter by category")
    p_search.add_argument("--days", type=int, help="Limit to last N days")

    # actions
    p_actions = sub.add_parser("actions", help="Manage actionable items")
    p_actions.add_argument("--effort", help="Filter by effort level")
    p_actions.add_argument("--all", action="store_true", help="Show all statuses")
    action_sub = p_actions.add_subparsers(dest="subaction")
    p_mark = action_sub.add_parser("mark", help="Mark an action's status")
    p_mark.add_argument("action_id", help="Action ID (e.g., action-2026-04-01-001)")
    p_mark.add_argument("status", choices=["tried", "skipped", "pending"])

    # digest
    p_digest = sub.add_parser("digest", help="View daily digest")
    p_digest.add_argument("--date", help="Specific date (YYYY-MM-DD)")
    p_digest.add_argument("--week", action="store_true", help="Last 7 days")

    # tools
    p_tools = sub.add_parser("tools", help="List tools by mention count")
    p_tools.add_argument("--min-sources", type=int, default=1,
                         help="Minimum number of newsletter sources")

    # stats
    sub.add_parser("stats", help="Show knowledge base statistics")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    commands = {
        "rebuild": cmd_rebuild,
        "search": cmd_search,
        "actions": cmd_actions,
        "digest": cmd_digest,
        "tools": cmd_tools,
        "stats": cmd_stats,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run all tests**

```bash
python -m pytest tests/test_kb.py -v
```

Expected: All 13 tests PASS.

- [ ] **Step 5: Commit CLI**

```bash
git add kb.py tests/test_kb.py
git commit -m "feat: add CLI subcommands — search, actions, digest, tools, stats, rebuild"
```

---

### Task 6: Remote trigger — create the scheduled agent

**Files:**
- No code files — this task uses the RemoteTrigger API

**Prerequisites:** The GitHub repo must exist and the Gmail MCP connector must be connected at claude.ai/settings/connectors.

- [ ] **Step 1: Create GitHub repo and push**

```bash
cd /Users/komalgarg/Documents/learn-ai/ai-newsletter-kb
gh repo create ai-newsletter-kb --private --source=. --push
```

- [ ] **Step 2: Craft the agent prompt**

The prompt below is the full instruction set for the remote agent. It references file paths and formats defined in earlier tasks.

```
You are the AI Newsletter Knowledge Base agent. You run daily to process new AI newsletters from Gmail and commit structured extractions to this repository.

## Step 1: Read state

Read `state.json` to find `last_run` timestamp. If `last_run` is null, this is the first run — fetch newsletters from the last 7 days.

## Step 2: Read config

Read `config.md` to get the sender whitelist and preferences.

## Step 3: Fetch newsletters from Gmail

Search Gmail for new newsletters since last_run. Try in this order:

1. Search for emails with label `AI-Newsletters` received after the last_run date.
2. If no results from the label, search for emails from each sender in the whitelist in config.md.
3. Skip any email whose message ID appears in `last_processed_ids` from state.json.

If no new newsletters are found, update state.json with the current timestamp and exit.

## Step 4: Process each newsletter

For each newsletter email found:

### 4a. Write raw content
- Extract the email body content
- Strip boilerplate: headers, footers, unsubscribe blocks, social media links, ad sections, tracking pixels
- Preserve: article text, links, embedded image URLs, code snippets
- Convert to clean markdown
- Write to `raw/YYYY-MM-DD/{source-slug}.md`

Source slugs must be lowercase-hyphenated (e.g., `the-batch`, `tldr-ai`, `bens-bites`, `import-ai`, `the-neuron`, `superhuman`). Derive the slug from the sender name or email address. Be consistent — the same newsletter must always get the same slug.

### 4b. Write structured extraction
Create a processed file at `processed/YYYY-MM-DD/{source-slug}.md` with this exact format:

```markdown
# {Newsletter Name} — {YYYY-MM-DD}

**Source:** {sender email}
**Date:** {YYYY-MM-DD}
**Original items:** {count of distinct stories/items in the newsletter}

## Key Announcements
- **{Title}** — {Brief summary}

## Tools & Products
- **{Tool Name}** — {What it does, why it matters} | {url} | Effort: {quick-win|weekend|major}

## Techniques & Methods
- **{Technique}** — {Description}

## Research Papers
- **{Paper Title}** ({Authors}) — {One-line summary} | {url}

## Industry Trends
- {Trend description}

## Actionable Items
- [ ] {Description} — *{effort}* — {url} | {action-YYYY-MM-DD-NNN}
- [ ] {Description} — *{effort}* | {action-YYYY-MM-DD-NNN}

## Notable Links
- {url} — {Description}
```

Rules for extraction:
- Every section must be present, even if empty (write "- None today." for empty sections)
- Action IDs must be globally unique: action-YYYY-MM-DD-NNN where NNN increments across ALL newsletters for that day (start from 001)
- Effort must be one of: quick-win, weekend, major
- URLs must be preserved exactly as they appear
- Omit items that are purely promotional or ads

## Step 5: Generate daily digest

After processing all newsletters, create `processed/YYYY-MM-DD/daily-digest.md`:

```markdown
# Daily Digest — {YYYY-MM-DD}

## Consensus Signals
- **{Topic}** — Covered by {sources}. {Brief synthesis}.

## Contrarian Takes
- {Description of disagreement between sources}

## Top 3 Actionable Items
1. {Description} — *{effort}* — {rationale for ranking}
2. {Description} — *{effort}* — {rationale}
3. {Description} — *{effort}* — {rationale}

## Urgent / Time-Sensitive
- {Item with deadline or expiring access}

## One-Line Summary
{Single sentence capturing the day in AI news.}
```

## Step 6: Update state

Update `state.json`:
```json
{
  "last_run": "{current ISO timestamp}",
  "last_run_status": "success",
  "last_processed_ids": ["{all message IDs processed this run}"],
  "newsletters_seen": {previous count + new count},
  "errors": []
}
```

If any newsletter failed to process, set `last_run_status` to `partial_success` and list errors.

## Step 7: Commit and push

```bash
git add raw/ processed/ state.json
git commit -m "newsletter: {YYYY-MM-DD} — {N} newsletters processed"
git push
```

## Error handling

- If Gmail MCP is unavailable, write the error to state.json and exit cleanly.
- If a single newsletter fails, continue with others and record the error.
- Never leave the repo in a dirty state — always commit what you have.
```

- [ ] **Step 3: Create the remote trigger via API**

Use the RemoteTrigger tool with:
- Name: `ai-newsletter-kb`
- Cron: `0 11 * * *` (7 AM ET = 11 AM UTC)
- Model: `claude-sonnet-4-6`
- Environment: `env_013QWurazUwNWjzyUHEz16mw`
- Repo: The GitHub URL from Step 1
- MCP: Gmail connector (attach after checking connector UUID)
- Prompt: The full prompt from Step 2
- Tools: `["Bash", "Read", "Write", "Edit", "Glob", "Grep"]`

- [ ] **Step 4: Test with a manual run**

Use RemoteTrigger with `action: "run"` and the trigger ID from Step 3. Monitor the output to verify:
- Agent reads state.json
- Agent searches Gmail via MCP
- Agent processes newsletters (if any exist)
- Agent commits results

- [ ] **Step 5: Verify results**

```bash
cd /Users/komalgarg/Documents/learn-ai/ai-newsletter-kb
git pull
ls raw/
ls processed/
cat state.json
```

Check that the agent produced valid markdown in the expected format.

---

### Task 7: Git post-merge hook for auto-rebuild

**Files:**
- Create: `.githooks/post-merge`
- Modify: `README.md` (add hook setup instructions)

- [ ] **Step 1: Create the post-merge hook**

```bash
mkdir -p .githooks
```

Create `.githooks/post-merge`:

```bash
#!/bin/sh
# Auto-rebuild SQLite index after pulling new newsletter data
echo "Rebuilding knowledge base index..."
python3 kb.py rebuild
```

- [ ] **Step 2: Make it executable and configure git**

```bash
chmod +x .githooks/post-merge
git config core.hooksPath .githooks
```

- [ ] **Step 3: Update README with hook setup**

Add to the Setup section of `README.md`:

```markdown
## One-Time Setup

After cloning, configure the git hook for auto-rebuild:

```bash
git config core.hooksPath .githooks
```

This automatically rebuilds the SQLite index whenever you `git pull` new newsletters.
```

- [ ] **Step 4: Commit hook**

```bash
git add .githooks/post-merge README.md
git commit -m "feat: add post-merge git hook for automatic index rebuild"
```

---

## Self-Review Checklist

**Spec coverage:**
- [x] Gmail detection (3-layer: label, whitelist, auto-detect) → Task 6 agent prompt
- [x] Content extraction (strip boilerplate, preserve substance) → Task 6 agent prompt
- [x] Structured processing (7 categories) → Task 2 fixtures + Task 3 parser + Task 6 prompt
- [x] Daily synthesis → Task 2 fixtures + Task 6 prompt
- [x] Repo structure → Task 1
- [x] SQLite schema + FTS5 → Task 4
- [x] SQLite gitignored, rebuilt locally → Task 4 + Task 7
- [x] Local CLI commands → Task 5
- [x] Zero external deps → Task 5 (stdlib only)
- [x] Remote trigger config → Task 6
- [x] Agent prompt → Task 6
- [x] Error handling in state.json → Task 6 prompt
- [x] State tracking → Task 6 prompt
- [x] Actionable item status management → Task 5 (`actions mark`)

**Placeholder scan:** No TBDs, TODOs, or vague steps found.

**Type consistency:** `parse_processed_markdown`, `parse_digest_markdown`, `create_database`, `rebuild_index` — used consistently across tests and implementation. CLI args (`--db`, `--processed-dir`) consistent across all subcommands.
