# clickmd

[![PyPI version](https://badge.fury.io/py/clickmd.svg)](https://badge.fury.io/py/clickmd)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Tests](https://github.com/wronai/clickmd/actions/workflows/tests.yml/badge.svg)](https://github.com/wronai/clickmd/actions)
[![codecov](https://codecov.io/gh/wronai/clickmd/branch/main/graph/badge.svg)](https://codecov.io/gh/wronai/clickmd)


## AI Cost Tracking

![AI Cost](https://img.shields.io/badge/AI%20Cost-$2.25-green) ![AI Model](https://img.shields.io/badge/AI%20Model-openrouter%2Fqwen%2Fqwen3-coder-next-lightgrey)

This project uses AI-generated code. Total cost: **$2.2500** with **15** AI commits.

Generated on 2026-04-08 using [openrouter/qwen/qwen3-coder-next](https://openrouter.ai/models/openrouter/qwen/qwen3-coder-next)

---

**Markdown rendering for CLI applications with syntax highlighting.**

`clickmd` provides beautiful terminal output with:
- 🎨 **Syntax highlighting** for 25+ languages (Python, TypeScript, Go, Rust, SQL, etc.)
- 📝 **Markdown rendering** with headers, bold, links, tables, panels, blockquotes
- 📊 **Tables & panels** for structured data display
- 📈 **Progress bars, spinners, live updates** for async operations
- 🎭 **Theming system** with 5+ built-in themes (monokai, dracula, nord, etc.)
- 🐛 **Developer tools** (debug, inspect, diff, tree, pretty exceptions)
- 🔧 **Zero dependencies** for core functionality
- 🖱️ **Optional Click integration** for CLI decorators
- ✨ **Optional Rich backend** for enhanced rendering

## Installation

```bash
# Core package (no dependencies)
pip install clickmd

# With Click support
pip install clickmd[click]

# With Rich backend (enhanced rendering)
pip install clickmd[rich]

# All optional features
pip install clickmd[all]
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

`clickmd` provides syntax highlighting for 25+ languages:

| Category | Languages | Extensions |
|----------|-----------|------------|
| **Programming** | Python, TypeScript, JavaScript, Go, Rust, Java, Kotlin, C/C++, Ruby, PHP | `.py`, `.ts`, `.js`, `.go`, `.rs`, `.java`, `.kt`, `.c`, `.cpp`, `.rb`, `.php` |
| **Data Formats** | JSON, YAML, TOML, INI, Config | `.json`, `.yaml`, `.yml`, `.toml`, `.ini`, `.cfg`, `.conf` |
| **Web** | HTML, XML, CSS, SCSS, Sass, Less | `.html`, `.htm`, `.xml`, `.svg`, `.css`, `.scss`, `.sass`, `.less` |
| **Shell** | Bash, Shell, Zsh, Dockerfile | `.sh`, `.bash`, `.zsh`, `Dockerfile` |
| **Database** | SQL, MySQL, PostgreSQL, SQLite | `.sql` |
| **Other** | Markdown, Log, Diff | `.md`, `.log`, `.diff`, `.patch` |

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

### Core Functions (No Dependencies)

| Function | Description |
|----------|-------------|
| `md(text: str) -> None` | Render markdown text with syntax highlighting |
| `echo(message, file=None, nl=True, err=False, color=None) -> None` | Smart echo that auto-detects markdown and renders it |
| `render_markdown(text, text_lang="markdown", stream=None, use_colors=True) -> None` | Low-level markdown rendering function |
| `get_renderer(stream=None, use_colors=True) -> MarkdownRenderer` | Get a `MarkdownRenderer` instance |
| `strip_ansi(text: str) -> str` | Remove ANSI escape codes from text |

### Interactive Prompts

| Function | Description |
|----------|-------------|
| `menu(title, items, default=1, prompt_text="Select", exit_option="Exit") -> int` | Display a numbered markdown menu |
| `select(prompt_text, items, default=1) -> int` | Inline numbered selection without title |

### Phase 1: Tables, Panels, Blockquotes

| Function | Description |
|----------|-------------|
| `table(headers, rows, style="simple") -> None` | Render ASCII/Unicode tables |
| `panel(text, title=None, style="default") -> None` | Display text in a bordered box |
| `blockquote(text) -> None` | Render a markdown blockquote |
| `hr() -> None` | Render a horizontal rule |
| `checklist(items, checked=None) -> None` | Render a markdown checklist |

### Logger

| Function/Class | Description |
|----------------|-------------|
| `Logger` | Markdown-aware logger with automatic codeblock wrapping |
| `get_logger(name)` | Get a logger instance |
| `log_info(msg)`, `log_success(msg)`, `log_warning(msg)`, `log_error(msg)`, `log_action(msg)` | Shortcut functions |

### Phase 3: Progress, Spinners, Live Updates

| Function/Class | Description |
|----------------|-------------|
| `progress(items, label=None, show_eta=True)` | Iterator wrapper with progress bar |
| `ProgressBar` | Manual progress bar control |
| `spinner(text, style="dots")` | Context manager for animated spinners |
| `Spinner` | Manual spinner control |
| `live(text_fn, refresh_rate=0.5)` | Live updating display |
| `countdown(seconds, message=None)` | Countdown timer display |
| `SPINNERS` | Dictionary of spinner animation styles |

### Phase 4: Theming

| Function/Class | Description |
|----------------|-------------|
| `Theme` | Color theme definition |
| `set_theme(name)` | Activate a theme |
| `get_theme()` | Get current theme |
| `list_themes()` | Show available themes |
| `register_theme(name, theme)` | Register a custom theme |
| `color(name)` | Get color code from current theme |
| `is_no_color() -> bool` | Check if NO_COLOR is set |
| `get_color_support() -> int` | Detect terminal color support (0/8/256/true) |
| `THEMES` | Dictionary of built-in themes |

### Phase 5: Developer Tools

| Function/Class | Description |
|----------------|-------------|
| `debug(obj, name=None, depth=2)` | Pretty-print with type info |
| `inspect_obj(obj, show_methods=True)` | Show object attributes |
| `diff(a, b, context=3)` | Side-by-side diff visualization |
| `tree(path, max_depth=3)` | Directory tree display |
| `PrettyExceptionFormatter` | Format exceptions with syntax highlighting |
| `install_excepthook()` | Enable pretty exception display |
| `uninstall_excepthook()` | Restore default exception display |
| `ClickmdHandler` | Logging handler with markdown styling |

### Click Integration (requires `click` package)

When `click` is installed, the full Click API is available:

**Decorators:**
- `@clickmd.group()` - Create a command group
- `@clickmd.command()` - Create a command
- `@clickmd.option()` - Add an option
- `@clickmd.argument()` - Add an argument
- `@clickmd.pass_context`, `@clickmd.pass_obj` - Context passing
- `@clickmd.version_option()`, `@clickmd.help_option()`, etc.

**Parameter Types:**
- `clickmd.STRING`, `clickmd.INT`, `clickmd.FLOAT`, `clickmd.BOOL`, `clickmd.UUID`
- `clickmd.Choice`, `clickmd.Path`, `clickmd.File`, `clickmd.DateTime`
- `clickmd.IntRange`, `clickmd.FloatRange`, `clickmd.Tuple`, `clickmd.ParamType`

**Core Classes:**
- `clickmd.Context`, `clickmd.Command`, `clickmd.Group`
- `clickmd.Option`, `clickmd.Argument`, `clickmd.Parameter`

**Utility Functions:**
- `clickmd.click_echo()`, `clickmd.secho()`, `clickmd.style()`, `clickmd.unstyle()`
- `clickmd.prompt()`, `clickmd.confirm()`, `clickmd.getchar()`, `clickmd.clear()`
- `clickmd.progressbar()`, `clickmd.open_file()`, `clickmd.get_app_dir()`

**Exceptions:**
- `clickmd.ClickException`, `clickmd.UsageError`, `clickmd.BadParameter`
- `clickmd.Abort`, `clickmd.NoSuchOption`, `clickmd.MissingParameter`

### Markdown Help for Click

| Class/Decorator | Description |
|----------------|-------------|
| `MarkdownCommand` | Command class with markdown help rendering |
| `MarkdownGroup` | Group class with markdown help rendering |
| `MarkdownHelpFormatter` | Help formatter with markdown support |
| `@markdown_help` | Decorator to enable markdown help |
| `success(msg)`, `warning(msg)`, `error(msg)`, `info(msg)` | Styled output panels |
| `echo_md(msg)` | Echo with markdown rendering |

### Rich Backend (optional)

When `rich` is installed:

| Function | Description |
|----------|-------------|
| `is_rich_available() -> bool` | Check if Rich is installed |
| `get_console()` | Get Rich console instance |
| `render_md(text)` | Render markdown with Rich |
| `render_panel(text, **kwargs)` | Render panel with Rich |
| `render_syntax(code, lang)` | Render syntax-highlighted code |
| `render_table(data, **kwargs)` | Render table with Rich |

### Constants

| Constant | Description |
|----------|-------------|
| `CLICK_AVAILABLE: bool` | Whether Click is installed |
| `RICH_AVAILABLE: bool` | Whether Rich is installed |

## Usage Examples

### Interactive Menus

```python
import clickmd

choice = clickmd.menu("## Choose Provider", [
    ("groq", "Groq — fast & free tier"),
    ("openrouter", "OpenRouter — multi-model"),
    ("ollama", "Ollama — local, no API key"),
])
```

### Tables & Panels

```python
from clickmd import table, panel

table(
    headers=["Name", "Version", "Status"],
    rows=[
        ["clickmd", "1.1.0", "✅ OK"],
        ["click", "8.1.7", "✅ OK"],
    ],
)

panel("Deployment complete!", title="Success", style="green")
```

### Logger

```python
from clickmd import get_logger

log = get_logger("myapp")
log.info("Starting process...")
log.success("Build complete!")
log.warning("Deprecated API")
log.error("Connection failed")
```

### Themes

```python
from clickmd import set_theme, list_themes

list_themes()            # Show available themes
set_theme("monokai")     # Switch theme
```

### Developer Tools

```python
from clickmd import debug, inspect_obj, diff, tree

debug(my_variable)                    # Pretty-print with type info
inspect_obj(my_object)                # Show object attributes
diff("old text", "new text")          # Side-by-side diff
tree("/path/to/dir")                  # Directory tree
```

## Examples

See the [examples/](examples/) directory for 17 demo scripts:

- `basic.py` — Basic markdown rendering
- `cli_app.py` — Full CLI application with Click
- `custom_renderer.py` — Custom renderer configuration
- `colored_logging.py` — Log-style colored output
- `phase1_features.py` — Tables, panels, blockquotes, checklists
- `phase3_progress.py` — Progress bars, spinners, live updates
- `phase4_themes.py` — Theming system
- `phase5_devtools.py` — Debug, inspect, diff, tree tools
- `logger_usage.py` — Structured logging
- `markdown_help.py` — Markdown help formatter for Click

## Project Structure

```
clickmd/
├── src/clickmd/          # Package source (src layout)
│   ├── __init__.py       # Public API: md(), echo(), menu(), select()
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
├── examples/             # 17 demo scripts
├── docs/                 # API reference & contributing guide
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
pip install -e ".[dev,all]"

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

Licensed under Apache-2.0.
## Author

Tom Sapletta
## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) first.

## Related Projects

- [Click](https://click.palletsprojects.com/) - Python CLI framework
- [Rich](https://github.com/Textualize/rich) - Rich text and beautiful formatting
