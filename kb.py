"""Knowledge base parser for processed newsletter markdown files."""

import re
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


def _parse_tool_item(line: str, category: str, date: str, index: int) -> dict:
    """Parse: - **Name** — Description | url | Effort: level"""
    m = re.match(
        r"^- \*\*(.+?)\*\*\s*[—–-]\s*(.+?)\s*\|\s*(https?://[^\s|]+)\s*\|\s*Effort:\s*(\S+)",
        line,
    )
    if m:
        title, summary, url, effort = m.group(1), m.group(2), m.group(3), m.group(4)
        return {
            "id": f"{category}-{date}-{index:03d}",
            "category": category,
            "title": title,
            "summary": summary.strip(),
            "url": url.strip(),
            "effort": effort.strip(),
        }
    return None


def _parse_paper_item(line: str, category: str, date: str, index: int) -> dict:
    """Parse: - **Title** (Authors) — Summary | url"""
    m = re.match(
        r"^- \*\*(.+?)\*\*\s*\([^)]+\)\s*[—–-]\s*(.+?)\s*\|\s*(https?://[^\s|]+)",
        line,
    )
    if m:
        title, summary, url = m.group(1), m.group(2), m.group(3)
        return {
            "id": f"{category}-{date}-{index:03d}",
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


def _parse_link_item(line: str, category: str, date: str, index: int) -> dict:
    """Parse: - url — Description"""
    m = re.match(r"^- (https?://[^\s|]+)\s*[—–-]\s*(.+)", line)
    if m:
        url, description = m.group(1), m.group(2)
        return {
            "id": f"{category}-{date}-{index:03d}",
            "category": category,
            "title": description.strip(),
            "summary": description.strip(),
            "url": url.strip(),
            "effort": None,
        }
    return None


def _parse_bold_item(line: str, category: str, date: str, index: int) -> dict:
    """Parse: - **Title** — Description"""
    m = re.match(r"^- \*\*(.+?)\*\*\s*[—–-]\s*(.+)", line)
    if m:
        title, summary = m.group(1), m.group(2)
        return {
            "id": f"{category}-{date}-{index:03d}",
            "category": category,
            "title": title.strip(),
            "summary": summary.strip(),
            "url": None,
            "effort": None,
        }
    return None


def _parse_plain_item(line: str, category: str, date: str, index: int) -> dict:
    """Parse: - plain text description"""
    m = re.match(r"^- (.+)", line)
    if m:
        text = m.group(1).strip()
        return {
            "id": f"{category}-{date}-{index:03d}",
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
            item = _parse_tool_item(line, current_category, date, idx)
        elif current_category == "paper":
            item = _parse_paper_item(line, current_category, date, idx)
        elif current_category == "link":
            item = _parse_link_item(line, current_category, date, idx)
        elif current_category in ("announcement", "technique"):
            item = _parse_bold_item(line, current_category, date, idx)
        elif current_category == "trend":
            # Try bold first, fall back to plain
            item = _parse_bold_item(line, current_category, date, idx)
            if item is None:
                item = _parse_plain_item(line, current_category, date, idx)

        if item is None:
            # Fallback: plain item
            item = _parse_plain_item(line, current_category, date, idx)

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
