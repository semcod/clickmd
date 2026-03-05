# clickmd

[![PyPI version](https://badge.fury.io/py/clickmd.svg)](https://badge.fury.io/py/clickmd)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Tests](https://github.com/wronai/clickmd/actions/workflows/tests.yml/badge.svg)](https://github.com/wronai/clickmd/actions)
[![codecov](https://codecov.io/gh/wronai/clickmd/branch/main/graph/badge.svg)](https://codecov.io/gh/wronai/clickmd)

**Markdown rendering for CLI applications with syntax highlighting.**

`clickmd` provides beautiful terminal output with:
- 🎨 **Syntax highlighting** for code blocks (Python, TypeScript, JSON, YAML, Bash, etc.)
- 📝 **Markdown rendering** with headers, bold, links, and more
- 🔧 **Zero dependencies** for core functionality
- 🖱️ **Optional Click integration** for CLI decorators

## Installation

```bash
# Core package (no dependencies)
pip install clickmd

# With Click support
pip install clickmd[click]
```

## Quick Start

### Basic Usage (No Dependencies)

```python
from clickmd import md, echo

# Render markdown with syntax highlighting
md("""
# Hello World

This is **bold** and this is a [link](https://example.com).

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```
""")

# Smart echo - auto-detects markdown
echo("## Status Update")
echo("Regular text without markdown")
```

### With Click Integration

```python
import clickmd as click

@click.group()
def cli():
    """My awesome CLI tool"""
    pass

@cli.command()
@click.option("--name", "-n", default="World")
def hello(name: str):
    """Say hello"""
    click.md(f"""
## 👋 Hello, {name}!

Welcome to **clickmd** - making CLIs beautiful.
    """)

if __name__ == "__main__":
    cli()
```

## Features

### Syntax Highlighting

`clickmd` provides syntax highlighting for multiple languages:

| Language | Extensions | Highlight Features |
|----------|------------|-------------------|
| Python | `.py` | Keywords, strings, comments, decorators |
| TypeScript/JavaScript | `.ts`, `.js` | Keywords, strings, template literals |
| JSON | `.json` | Keys, strings, numbers, booleans |
| YAML | `.yaml`, `.yml` | Keys, values, comments |
| Bash/Shell | `.sh`, `.bash` | Commands, comments |
| Markdown | `.md` | Headers, bold, links |
| Log | `.log` | Errors (red), warnings (yellow), success (green) |

### Markdown Elements

```python
from clickmd import md

md("""
# Heading 1
## Heading 2
### Heading 3

**Bold text** and regular text.

[Links](https://example.com) are supported.

```python
# Code blocks with syntax highlighting
print("Hello, World!")
```

- List items
- Are rendered
- Correctly
""")
```

### MarkdownRenderer Class

For more control, use the `MarkdownRenderer` class directly:

```python
from clickmd import MarkdownRenderer
import sys

renderer = MarkdownRenderer(use_colors=True, stream=sys.stdout)
renderer.heading(1, "My Title")
renderer.codeblock("python", 'print("Hello!")')
```

### Progress and Status Output

```python
from clickmd import md

# Log-style output with automatic coloring
md("""
```log
🚀 Starting process...
📦 Installing dependencies...
✅ Build successful!
⚠️ Warning: deprecated API
🛑 Error: connection failed
```
""")
```

## API Reference

### Core Functions

#### `md(text: str) -> None`
Render markdown text with syntax highlighting.

#### `echo(message, file=None, nl=True, err=False, color=None) -> None`
Smart echo that auto-detects markdown and renders it.

#### `render_markdown(text, text_lang="markdown", stream=None, use_colors=True) -> None`
Low-level markdown rendering function.

#### `get_renderer(stream=None, use_colors=True) -> MarkdownRenderer`
Get a `MarkdownRenderer` instance.

### Click Decorators (requires `click` package)

When `click` is installed, these decorators are available:

- `@clickmd.group()` - Create a command group
- `@clickmd.command()` - Create a command
- `@clickmd.option()` - Add an option
- `@clickmd.argument()` - Add an argument
- `@clickmd.pass_context` - Pass Click context
- `clickmd.Choice` - Choice type
- `clickmd.Path` - Path type

### Constants

- `CLICK_AVAILABLE: bool` - Whether Click is installed

## Examples

See the [examples/](examples/) directory for more usage examples:

- `examples/basic.py` - Basic markdown rendering
- `examples/cli_app.py` - Full CLI application with Click
- `examples/custom_renderer.py` - Custom renderer configuration
- `examples/logging.py` - Log-style colored output

## Project Structure

```
clickmd/
├── src/clickmd/          # Package source
│   ├── __init__.py       # Public API & re-exports
│   ├── renderer.py       # Core markdown renderer & syntax highlighting
│   ├── decorators.py     # Click decorator re-exports
│   ├── help.py           # Markdown help formatter for Click
│   ├── logger.py         # Markdown-aware structured logger
│   ├── progress.py       # Progress bars, spinners, live updates
│   ├── themes.py         # Color themes & NO_COLOR support
│   ├── devtools.py       # Debug, inspect, diff, tree tools
│   ├── rich_backend.py   # Optional Rich integration
│   └── py.typed          # PEP 561 type marker
├── tests/                # Test suite (69 tests)
├── examples/             # Demo scripts
├── scripts/              # Build & version tools
├── tools/                # Markdown-to-HTML converter
├── pyproject.toml        # Project config (hatchling)
└── Makefile              # Dev commands
```

## Development

```bash
# Clone the repository
git clone https://github.com/wronai/clickmd.git
cd clickmd

# Install development dependencies
pip install -e ".[dev,click]"

# Run tests
make test

# Run linter & format
make lint
make format

# Build & publish
make build
make publish
```

## License

Apache License 2.0 - see [LICENSE](LICENSE) for details.

## Author

Created by **Tom Sapletta** - [tom@sapletta.com](mailto:tom@sapletta.com)

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) first.

## Related Projects

- [Click](https://click.palletsprojects.com/) - Python CLI framework
- [Rich](https://github.com/Textualize/rich) - Rich text and beautiful formatting
