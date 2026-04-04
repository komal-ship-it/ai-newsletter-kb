"""Knowledge base parser for processed newsletter markdown files."""

import re
import sqlite3
from pathlib import Path


SECTION_CATEGORY_MAP = {
    "Key Announcements": "announcement",
    "Tools & Products": "tool",
    "Techniques & Methods": "technique",
    "Research Papers": "paper",
    "Industry Trends": "trend",
    "Actionable Items": "actionable",
    "Notable Links": "link",
}


def _parse_tool_item(line: str, category: str, slug: str, date: str, index: int) -> dict:
    """Parse: - **Name** — Description | url | Effort: level"""
    m = re.match(
        r"^- \*\*(.+?)\*\*\s*[—–-]\s*(.+?)\s*\|\s*(https?://[^\s|]+)\s*\|\s*Effort:\s*(\S+)",
        line,
    )
    if m:
        title, summary, url, effort = m.group(1), m.group(2), m.group(3), m.group(4)
        return {
            "id": f"{category}-{slug}-{date}-{index:03d}",
            "category": category,
            "title": title,
            "summary": summary.strip(),
            "url": url.strip(),
            "effort": effort.strip(),
        }
    return None


def _parse_paper_item(line: str, category: str, slug: str, date: str, index: int) -> dict:
    """Parse: - **Title** (Authors) — Summary | url"""
    m = re.match(
        r"^- \*\*(.+?)\*\*\s*\([^)]+\)\s*[—–-]\s*(.+?)\s*\|\s*(https?://[^\s|]+)",
        line,
    )
    if m:
        title, summary, url = m.group(1), m.group(2), m.group(3)
        return {
            "id": f"{category}-{slug}-{date}-{index:03d}",
            "category": category,
            "title": title,
            "summary": summary.strip(),
            "url": url.strip(),
            "effort": None,
        }
    return None


def _parse_actionable_item(line: str) -> dict:
    """Parse: - [ ] Description — *effort* — url | action-ID
              - [ ] Description — *effort* | action-ID"""
    # With URL
    m = re.match(
        r"^- \[ \]\s+(.+?)\s*[—–-]\s*\*(.+?)\*\s*[—–-]\s*(https?://[^\s|]+)\s*\|\s*(action-[\w-]+)",
        line,
    )
    if m:
        title, effort, url, action_id = m.group(1), m.group(2), m.group(3), m.group(4)
        return {
            "id": action_id,
            "category": "actionable",
            "title": title.strip(),
            "summary": title.strip(),
            "url": url.strip(),
            "effort": effort.strip(),
        }
    # Without URL
    m = re.match(
        r"^- \[ \]\s+(.+?)\s*[—–-]\s*\*(.+?)\*\s*\|\s*(action-[\w-]+)",
        line,
    )
    if m:
        title, effort, action_id = m.group(1), m.group(2), m.group(3)
        return {
            "id": action_id,
            "category": "actionable",
            "title": title.strip(),
            "summary": title.strip(),
            "url": None,
            "effort": effort.strip(),
        }
    return None


def _parse_link_item(line: str, category: str, slug: str, date: str, index: int) -> dict:
    """Parse: - url — Description"""
    m = re.match(r"^- (https?://[^\s|]+)\s*[—–-]\s*(.+)", line)
    if m:
        url, description = m.group(1), m.group(2)
        return {
            "id": f"{category}-{slug}-{date}-{index:03d}",
            "category": category,
            "title": description.strip(),
            "summary": description.strip(),
            "url": url.strip(),
            "effort": None,
        }
    return None


def _parse_bold_item(line: str, category: str, slug: str, date: str, index: int) -> dict:
    """Parse: - **Title** — Description"""
    m = re.match(r"^- \*\*(.+?)\*\*\s*[—–-]\s*(.+)", line)
    if m:
        title, summary = m.group(1), m.group(2)
        return {
            "id": f"{category}-{slug}-{date}-{index:03d}",
            "category": category,
            "title": title.strip(),
            "summary": summary.strip(),
            "url": None,
            "effort": None,
        }
    return None


def _parse_plain_item(line: str, category: str, slug: str, date: str, index: int) -> dict:
    """Parse: - plain text description"""
    m = re.match(r"^- (.+)", line)
    if m:
        text = m.group(1).strip()
        return {
            "id": f"{category}-{slug}-{date}-{index:03d}",
            "category": category,
            "title": text,
            "summary": text,
            "url": None,
            "effort": None,
        }
    return None


def parse_processed_markdown(text: str, processed_path: str) -> dict:
    """Parse a processed newsletter markdown file.

    Returns a dict with keys: id, source, date, source_email, processed_path, items.
    """
    lines = text.splitlines()

    # Parse H1: # Newsletter Name — YYYY-MM-DD
    h1_match = re.match(r"^# (.+?)\s*[—–-]\s*(\d{4}-\d{2}-\d{2})", lines[0])
    if not h1_match:
        raise ValueError(
            f"Expected H1 header matching '# Name — YYYY-MM-DD', got: {lines[0]!r}"
        )
    source = h1_match.group(1).strip()
    date = h1_match.group(2).strip()

    # Parse metadata block
    source_email = None
    for line in lines:
        m = re.match(r"^\*\*Source:\*\*\s*(.+)", line)
        if m:
            source_email = m.group(1).strip()
            break

    # Derive id from processed_path filename and date
    # e.g. "processed/2026-04-01/the-batch.md" -> "the-batch-2026-04-01"
    filename = Path(processed_path).stem  # "the-batch"
    newsletter_id = f"{filename}-{date}"

    items = []
    current_category = None
    category_counters = {}

    for line in lines:
        # Detect section headers: ## Section Name
        h2_match = re.match(r"^## (.+)", line)
        if h2_match:
            section_name = h2_match.group(1).strip()
            current_category = SECTION_CATEGORY_MAP.get(section_name)
            continue

        if current_category is None:
            continue

        # Skip empty lines and non-list lines
        if not line.startswith("- "):
            continue

        # Increment counter for this category
        category_counters[current_category] = category_counters.get(current_category, 0) + 1
        idx = category_counters[current_category]

        item = None

        if current_category == "actionable":
            item = _parse_actionable_item(line)
        elif current_category == "tool":
            item = _parse_tool_item(line, current_category, filename, date, idx)
        elif current_category == "paper":
            item = _parse_paper_item(line, current_category, filename, date, idx)
        elif current_category == "link":
            item = _parse_link_item(line, current_category, filename, date, idx)
        elif current_category in ("announcement", "technique"):
            item = _parse_bold_item(line, current_category, filename, date, idx)
        elif current_category == "trend":
            # Try bold first, fall back to plain
            item = _parse_bold_item(line, current_category, filename, date, idx)
            if item is None:
                item = _parse_plain_item(line, current_category, filename, date, idx)

        if item is None:
            # Fallback: plain item
            item = _parse_plain_item(line, current_category, filename, date, idx)

        if item:
            items.append(item)

    return {
        "id": newsletter_id,
        "source": source,
        "date": date,
        "source_email": source_email,
        "processed_path": processed_path,
        "items": items,
    }


def parse_digest_markdown(text: str, date: str) -> dict:
    """Parse a daily digest markdown file.

    Returns a dict with keys: date, one_line_summary.
    """
    one_line_summary = None
    lines = text.splitlines()
    in_summary_section = False

    for line in lines:
        if re.match(r"^## One-Line Summary", line):
            in_summary_section = True
            continue
        if in_summary_section:
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                one_line_summary = stripped
                break

    return {
        "date": date,
        "one_line_summary": one_line_summary,
    }


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
    title, summary
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
    """Rebuild the SQLite index from all processed markdown files.

    Preserves action item statuses (tried/skipped) across rebuilds.
    """
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

    if not processed_dir.exists():
        return conn

    # Walk all date directories
    for date_dir in sorted(processed_dir.iterdir()):
        if not date_dir.is_dir():
            continue
        date_str = date_dir.name

        for md_file in sorted(date_dir.glob("*.md")):
            if md_file.name == "daily-digest.md":
                text = md_file.read_text()
                digest = parse_digest_markdown(text, date_str)
                conn.execute(
                    "INSERT OR REPLACE INTO digests (date, path, one_line_summary) "
                    "VALUES (?, ?, ?)",
                    (digest["date"],
                     str(md_file.relative_to(processed_dir.parent)),
                     digest["one_line_summary"]),
                )
            else:
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
