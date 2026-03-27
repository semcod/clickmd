#!/usr/bin/env python3

import argparse
import html
import re
from pathlib import Path


_BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
_ITALIC_RE = re.compile(r"\*([^*]+)\*")
_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_INLINE_CODE_RE = re.compile(r"`([^`]+)`")


def _inline_md_to_html(text: str) -> str:
    """Convert inline markdown to HTML."""
    # Process in order: code first (to protect content), then bold, italic, links
    
    # Inline code - protect content
    def _code(m: re.Match[str]) -> str:
        return f"<code>{html.escape(m.group(1))}</code>"
    
    result = _INLINE_CODE_RE.sub(_code, text)
    
    # Bold
    result = _BOLD_RE.sub(lambda m: f"<strong>{html.escape(m.group(1))}</strong>", result)
    
    # Italic (but not inside code)
    result = _ITALIC_RE.sub(lambda m: f"<em>{m.group(1)}</em>", result)
    
    # Links
    result = _LINK_RE.sub(lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>', result)
    
    return result


def _escape_text(text: str) -> str:
    """Escape HTML but preserve already processed tags."""
    # Only escape < > & that aren't part of our generated tags
    text = text.replace("&", "&amp;")
    # Don't escape < > if they're part of tags we generated
    return text


def markdown_to_html(markdown_text: str, title: str) -> str:
    """Convert markdown text to HTML with basic formatting support."""
    lines = (markdown_text or "").splitlines()
    
    # Initialize state
    state = {
        "out": [],
        "in_code": False,
        "code_lang": "",
        "code_buf": [],
        "paragraph": [],
        "in_list": False,
        "list_items": [],
    }
    
    # Add HTML header
    _add_html_header(state["out"], title)
    
    # Process each line
    i = 0
    while i < len(lines):
        i = _process_line(lines, i, state)
    
    # Flush remaining content
    _flush_paragraph(state)
    _flush_list(state)
    _flush_code(state)
    
    # Close HTML
    state["out"].append("</body>")
    state["out"].append("</html>")
    
    return "\n".join(state["out"])


def _add_html_header(out: list[str], title: str) -> None:
    """Add the HTML head section with styles."""
    out.append("<!doctype html>")
    out.append("<html lang=\"en\">")
    out.append("<head>")
    out.append("  <meta charset=\"utf-8\" />")
    out.append("  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />")
    out.append(f"  <title>{html.escape(title)}</title>")
    out.append(
        "  <style>\n"
        "    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; padding: 24px; max-width: 980px; margin: 0 auto; }\n"
        "    h1, h2, h3, h4, h5, h6 { margin: 24px 0 12px; }\n"
        "    p { line-height: 1.5; margin: 10px 0; }\n"
        "    pre { background: #0b1020; color: #e6edf3; padding: 14px; border-radius: 10px; overflow-x: auto; }\n"
        "    code { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 13px; }\n"
        "    a { color: #2563eb; text-decoration: none; }\n"
        "    a:hover { text-decoration: underline; }\n"
        "    table { border-collapse: collapse; width: 100%; margin: 12px 0; }\n"
        "    th, td { border: 1px solid #e5e7eb; padding: 8px; text-align: left; }\n"
        "    th { background: #f3f4f6; }\n"
        "  </style>"
    )
    out.append("</head>")
    out.append("<body>")


def _process_line(lines: list[str], i: int, state: dict) -> int:
    """Process a single line and return the next line index."""
    line = lines[i]
    stripped = line.rstrip("\n")
    
    # Code fences
    fence = re.match(r"^(`{3,})(.*)$", stripped.strip())
    if fence:
        _flush_paragraph(state)
        _flush_list(state)
        if not state["in_code"]:
            _start_code(state, fence.group(2))
        else:
            _flush_code(state)
        return i + 1
    
    # Inside code block
    if state["in_code"]:
        state["code_buf"].append(stripped)
        return i + 1
    
    # Headings
    m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
    if m:
        _flush_paragraph(state)
        _flush_list(state)
        level = len(m.group(1))
        state["out"].append(f"<h{level}>{_inline_md_to_html(m.group(2).strip())}</h{level}>")
        return i + 1
    
    # List items
    list_match = re.match(r"^[-*]\s+(.*)$", stripped.strip())
    if list_match:
        _flush_paragraph(state)
        state["in_list"] = True
        state["list_items"].append(list_match.group(1))
        return i + 1
    
    ordered_match = re.match(r"^\d+\.\s+(.*)$", stripped.strip())
    if ordered_match:
        _flush_paragraph(state)
        state["in_list"] = True
        state["list_items"].append(ordered_match.group(1))
        return i + 1
    
    # Tables
    if _is_table_row(stripped) and i + 1 < len(lines) and re.match(r"^\|\s*[:-]-+.*\|$", lines[i + 1].strip()):
        i = _process_table(lines, i, state)
        return i
    
    # Blank line
    if not stripped.strip():
        _flush_paragraph(state)
        _flush_list(state)
        return i + 1
    
    # Regular text
    if state["in_list"]:
        _flush_list(state)
    state["paragraph"].append(stripped)
    return i + 1


def _process_table(lines: list[str], i: int, state: dict) -> int:
    """Process a table and return the next line index after the table."""
    _flush_paragraph(state)
    _flush_list(state)
    
    header = [c.strip() for c in lines[i].strip()[1:-1].split("|")]
    i += 2  # Skip header and separator
    
    rows = []
    while i < len(lines) and _is_table_row(lines[i]):
        row = [c.strip() for c in lines[i].strip()[1:-1].split("|")]
        rows.append(row)
        i += 1
    
    state["out"].append("<table>")
    state["out"].append("<thead><tr>" + "".join([f"<th>{_inline_md_to_html(c)}</th>" for c in header]) + "</tr></thead>")
    state["out"].append("<tbody>")
    for row in rows:
        row_cells = "".join([f"<td>{_inline_md_to_html(c)}</td>" for c in row])
        state["out"].append(f"<tr>{row_cells}</tr>")
    state["out"].append("</tbody></table>")
    
    return i


def _is_table_row(s: str) -> bool:
    """Check if a line is a table row."""
    t = s.strip()
    return t.startswith("|") and t.endswith("|") and "|" in t[1:-1]


def _flush_code(state: dict) -> None:
    """Flush the code buffer to output."""
    if not state["in_code"]:
        return
    code = "\n".join(state["code_buf"])
    state["out"].append(
        f"<pre><code class=\"language-{html.escape(state['code_lang'])}\">{html.escape(code)}</code></pre>"
    )
    state["in_code"] = False
    state["code_lang"] = ""
    state["code_buf"] = []


def _start_code(state: dict, lang: str) -> None:
    """Start a code block."""
    state["in_code"] = True
    state["code_lang"] = (lang or "").strip() or "text"
    state["code_buf"] = []


def _flush_paragraph(state: dict) -> None:
    """Flush paragraph buffer to output."""
    if not state["paragraph"]:
        return
    for p in state["paragraph"]:
        text = p.strip()
        if text:
            state["out"].append(f"<p>{_inline_md_to_html(text)}</p>")
    state["paragraph"] = []


def _flush_list(state: dict) -> None:
    """Flush list buffer to output."""
    if not state["in_list"] or not state["list_items"]:
        state["in_list"] = False
        state["list_items"] = []
        return
    state["out"].append("<ul>")
    for item in state["list_items"]:
        state["out"].append(f"<li>{_inline_md_to_html(item)}</li>")
    state["out"].append("</ul>")
    state["in_list"] = False
    state["list_items"] = []


def convert_directory(md_dir: Path) -> None:
    for md_path in sorted(md_dir.glob("*.md")):
        title = md_path.stem
        html_path = md_path.with_suffix(".html")
        md_text = md_path.read_text(encoding="utf-8")
        html_text = markdown_to_html(md_text, title=title)
        html_path.write_text(html_text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("md_dir", help="Directory containing *.md files")
    args = parser.parse_args()

    md_dir = Path(args.md_dir)
    if not md_dir.exists() or not md_dir.is_dir():
        raise SystemExit(f"Not a directory: {md_dir}")

    convert_directory(md_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
