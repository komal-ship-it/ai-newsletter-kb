import sys
import os
import sqlite3
import subprocess
import tempfile
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


PYTHON = str(Path(__file__).parent.parent / ".venv" / "bin" / "python")
KB_SCRIPT = str(Path(__file__).parent.parent / "kb.py")
TEST_DB = "/tmp/test_kb_cli.sqlite"


def _run_kb(*args: str) -> subprocess.CompletedProcess:
    """Run kb.py as a subprocess pointing at fixtures."""
    cmd = [PYTHON, KB_SCRIPT,
           "--db", TEST_DB,
           "--processed-dir", str(FIXTURES / "processed")]
    cmd.extend(args)
    return subprocess.run(cmd, capture_output=True, text=True,
                          cwd=str(Path(__file__).parent.parent))


def test_cli_rebuild():
    """kb.py rebuild should create the database."""
    result = _run_kb("rebuild")
    assert result.returncode == 0
    assert "rebuilt" in result.stdout.lower() or "Rebuilt" in result.stdout


def test_cli_search():
    """kb.py search should find items matching a query."""
    _run_kb("rebuild")
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
