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
