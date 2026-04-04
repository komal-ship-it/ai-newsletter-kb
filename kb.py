"""Knowledge base parser for processed newsletter markdown files."""

import argparse
import re
import sqlite3
import sys
from datetime import datetime, timedelta
from pathlib import Path


DB_DEFAULT = "kb.sqlite"
PROCESSED_DEFAULT = "processed"


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


# ---------------------------------------------------------------------------
# CLI helpers
# ---------------------------------------------------------------------------

def _get_conn(args) -> sqlite3.Connection:
    """Connect to the SQLite database; exit with an error if it doesn't exist."""
    db_path = Path(args.db)
    if not db_path.exists():
        print(f"Error: database not found at {db_path}. Run 'kb.py rebuild' first.",
              file=sys.stderr)
        sys.exit(1)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn


# ---------------------------------------------------------------------------
# Subcommand implementations
# ---------------------------------------------------------------------------

def cmd_rebuild(args) -> None:
    """Rebuild the SQLite index from processed markdown files."""
    processed_dir = Path(args.processed_dir)
    conn = rebuild_index(args.db, processed_dir=processed_dir)
    n_newsletters = conn.execute("SELECT COUNT(*) FROM newsletters").fetchone()[0]
    n_items = conn.execute("SELECT COUNT(*) FROM items").fetchone()[0]
    n_digests = conn.execute("SELECT COUNT(*) FROM digests").fetchone()[0]
    conn.close()
    print(f"Rebuilt {args.db}: {n_newsletters} newsletters, {n_items} items, "
          f"{n_digests} digests.")


def cmd_search(args) -> None:
    """Full-text search over items."""
    conn = _get_conn(args)

    query = args.query
    params: list = [query]

    sql = (
        "SELECT i.id, i.category, i.title, i.summary, i.url, i.date "
        "FROM items_fts f "
        "JOIN items i ON i.rowid = f.rowid "
        "WHERE items_fts MATCH ?"
    )

    if args.category:
        sql += " AND i.category = ?"
        params.append(args.category)

    if args.days:
        cutoff = (datetime.now() - timedelta(days=args.days)).strftime("%Y-%m-%d")
        sql += " AND i.date >= ?"
        params.append(cutoff)

    rows = conn.execute(sql, params).fetchall()
    conn.close()

    if not rows:
        print("No results found.")
        return

    for row in rows:
        print(f"[{row['date']}] [{row['category']}] {row['title']}")
        if row['summary'] and row['summary'] != row['title']:
            print(f"  {row['summary']}")
        if row['url']:
            print(f"  {row['url']}")
        print(f"  id: {row['id']}")
        print()


def cmd_actions(args) -> None:
    """List or mark actionable items."""
    # Handle mark sub-subcommand
    if getattr(args, 'actions_command', None) == 'mark':
        conn = _get_conn(args)
        conn.execute(
            "UPDATE items SET status = ? WHERE id = ?",
            (args.status, args.action_id),
        )
        conn.commit()
        rows_affected = conn.execute(
            "SELECT changes()"
        ).fetchone()[0]
        conn.close()
        if rows_affected:
            print(f"Marked {args.action_id} as '{args.status}'.")
        else:
            print(f"No action found with id '{args.action_id}'.", file=sys.stderr)
            sys.exit(1)
        return

    conn = _get_conn(args)

    params: list = []
    sql = (
        "SELECT id, title, effort, status, date "
        "FROM items WHERE category = 'actionable'"
    )

    if not getattr(args, 'all', False):
        sql += " AND status = 'pending'"

    if getattr(args, 'effort', None):
        sql += " AND effort = ?"
        params.append(args.effort)

    sql += " ORDER BY date DESC, id"

    rows = conn.execute(sql, params).fetchall()
    conn.close()

    if not rows:
        print("No actionable items found.")
        return

    for row in rows:
        status_tag = f"[{row['status']}]" if row['status'] != 'pending' else ""
        effort_tag = f"({row['effort']})" if row['effort'] else ""
        parts = [row['id'], effort_tag, status_tag, row['title']]
        print("  ".join(p for p in parts if p))


def cmd_digest(args) -> None:
    """Display daily digest content."""
    conn = _get_conn(args)
    processed_dir = Path(args.processed_dir)

    if getattr(args, 'date', None):
        dates = [args.date]
    elif getattr(args, 'week', False):
        cutoff = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        rows = conn.execute(
            "SELECT date FROM digests WHERE date >= ? ORDER BY date DESC", (cutoff,)
        ).fetchall()
        dates = [r['date'] for r in rows]
    else:
        row = conn.execute(
            "SELECT date FROM digests ORDER BY date DESC LIMIT 1"
        ).fetchone()
        dates = [row['date']] if row else []

    conn.close()

    if not dates:
        print("No digests found.")
        return

    for date in dates:
        digest_path = processed_dir / date / "daily-digest.md"
        if digest_path.exists():
            print(digest_path.read_text())
        else:
            print(f"Digest for {date}: (file not found at {digest_path})")
        print()


def cmd_tools(args) -> None:
    """Show tools mentioned across multiple newsletter sources."""
    conn = _get_conn(args)

    min_sources = getattr(args, 'min_sources', 1) or 1

    sql = (
        "SELECT i.title, COUNT(DISTINCT n.source) as source_count, "
        "GROUP_CONCAT(DISTINCT n.source) as sources, i.url "
        "FROM items i "
        "JOIN newsletters n ON n.id = i.newsletter_id "
        "WHERE i.category = 'tool' "
        "GROUP BY i.title "
        "HAVING source_count >= ? "
        "ORDER BY source_count DESC, i.title"
    )

    rows = conn.execute(sql, [min_sources]).fetchall()
    conn.close()

    if not rows:
        print(f"No tools found mentioned by {min_sources}+ sources.")
        return

    for row in rows:
        print(f"{row['title']}  ({row['source_count']} sources: {row['sources']})")
        if row['url']:
            print(f"  {row['url']}")


def cmd_stats(args) -> None:
    """Show summary statistics about the knowledge base."""
    conn = _get_conn(args)

    n_newsletters = conn.execute("SELECT COUNT(*) FROM newsletters").fetchone()[0]
    n_items = conn.execute("SELECT COUNT(*) FROM items").fetchone()[0]
    n_pending = conn.execute(
        "SELECT COUNT(*) FROM items WHERE category='actionable' AND status='pending'"
    ).fetchone()[0]
    n_tried = conn.execute(
        "SELECT COUNT(*) FROM items WHERE category='actionable' AND status='tried'"
    ).fetchone()[0]
    n_skipped = conn.execute(
        "SELECT COUNT(*) FROM items WHERE category='actionable' AND status='skipped'"
    ).fetchone()[0]
    n_digests = conn.execute("SELECT COUNT(*) FROM digests").fetchone()[0]

    conn.close()

    print(f"Newsletters : {n_newsletters}")
    print(f"Items       : {n_items}")
    print(f"Digests     : {n_digests}")
    print(f"Actions")
    print(f"  pending   : {n_pending}")
    print(f"  tried     : {n_tried}")
    print(f"  skipped   : {n_skipped}")


# ---------------------------------------------------------------------------
# argparse setup and main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="AI Newsletter Knowledge Base CLI",
        prog="kb.py",
    )
    parser.add_argument("--db", default=DB_DEFAULT,
                        help=f"Path to SQLite database (default: {DB_DEFAULT})")
    parser.add_argument("--processed-dir", default=PROCESSED_DEFAULT,
                        help=f"Path to processed newsletters directory "
                             f"(default: {PROCESSED_DEFAULT})")

    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND")
    subparsers.required = True

    # rebuild
    subparsers.add_parser("rebuild", help="Rebuild the database index")

    # search
    sp_search = subparsers.add_parser("search", help="Full-text search items")
    sp_search.add_argument("query", help="Search query")
    sp_search.add_argument("--category", help="Filter by category")
    sp_search.add_argument("--days", type=int,
                           help="Limit to items from the last N days")

    # actions
    sp_actions = subparsers.add_parser("actions", help="List or mark actions")
    sp_actions.add_argument("--effort", help="Filter by effort level")
    sp_actions.add_argument("--all", action="store_true",
                            help="Show all statuses (not just pending)")
    actions_sub = sp_actions.add_subparsers(dest="actions_command")
    sp_mark = actions_sub.add_parser("mark", help="Update action status")
    sp_mark.add_argument("action_id", help="Action ID to mark")
    sp_mark.add_argument("status", choices=["tried", "skipped", "pending"],
                         help="New status")

    # digest
    sp_digest = subparsers.add_parser("digest", help="Show daily digest")
    sp_digest.add_argument("--date", help="Date (YYYY-MM-DD)")
    sp_digest.add_argument("--week", action="store_true",
                           help="Show digests for the last 7 days")

    # tools
    sp_tools = subparsers.add_parser("tools", help="Show tools by source count")
    sp_tools.add_argument("--min-sources", type=int, default=1,
                          help="Minimum number of sources mentioning the tool")

    # stats
    subparsers.add_parser("stats", help="Show knowledge base statistics")

    args = parser.parse_args()

    dispatch = {
        "rebuild": cmd_rebuild,
        "search": cmd_search,
        "actions": cmd_actions,
        "digest": cmd_digest,
        "tools": cmd_tools,
        "stats": cmd_stats,
    }

    fn = dispatch[args.command]
    fn(args)


if __name__ == "__main__":
    main()
