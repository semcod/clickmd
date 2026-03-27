<!-- code2docs:start --># clickmd

![version](https://img.shields.io/badge/version-0.1.0-blue) ![python](https://img.shields.io/badge/python-%3E%3D3.10-blue) ![coverage](https://img.shields.io/badge/coverage-unknown-lightgrey) ![functions](https://img.shields.io/badge/functions-233-green)
> **233** functions | **11** classes | **28** files | CC̄ = 2.9

> Auto-generated project documentation from source code analysis.

**Author:** Tom Sapletta  
**License:** Apache-2.0[(LICENSE)](./LICENSE)  
**Repository:** [https://github.com/wronai/clickmd](https://github.com/wronai/clickmd)

## Installation

### From PyPI

```bash
pip install clickmd
```

### From Source

```bash
git clone https://github.com/wronai/clickmd
cd clickmd
pip install -e .
```

### Optional Extras

```bash
pip install clickmd[click]    # click features
pip install clickmd[rich]    # rich features
pip install clickmd[dev]    # development tools
pip install clickmd[all]    # all optional features
```

## Quick Start

### CLI Usage

```bash
# Generate full documentation for your project
clickmd ./my-project

# Only regenerate README
clickmd ./my-project --readme-only

# Preview what would be generated (no file writes)
clickmd ./my-project --dry-run

# Check documentation health
clickmd check ./my-project

# Sync — regenerate only changed modules
clickmd sync ./my-project
```

### Python API

```python
from clickmd import generate_readme, generate_docs, Code2DocsConfig

# Quick: generate README
generate_readme("./my-project")

# Full: generate all documentation
config = Code2DocsConfig(project_name="mylib", verbose=True)
docs = generate_docs("./my-project", config=config)
```

## Generated Output

When you run `clickmd`, the following files are produced:

```
<project>/
├── README.md                 # Main project README (auto-generated sections)
├── docs/
│   ├── api.md               # Consolidated API reference
│   ├── modules.md           # Module documentation with metrics
│   ├── architecture.md      # Architecture overview with diagrams
│   ├── dependency-graph.md  # Module dependency graphs
│   ├── coverage.md          # Docstring coverage report
│   ├── getting-started.md   # Getting started guide
│   ├── configuration.md    # Configuration reference
│   └── api-changelog.md    # API change tracking
├── examples/
│   ├── quickstart.py       # Basic usage examples
│   └── advanced_usage.py   # Advanced usage examples
├── CONTRIBUTING.md         # Contribution guidelines
└── mkdocs.yml             # MkDocs site configuration
```

## Configuration

Create `clickmd.yaml` in your project root (or run `clickmd init`):

```yaml
project:
  name: my-project
  source: ./
  output: ./docs/

readme:
  sections:
    - overview
    - install
    - quickstart
    - api
    - structure
  badges:
    - version
    - python
    - coverage
  sync_markers: true

docs:
  api_reference: true
  module_docs: true
  architecture: true
  changelog: true

examples:
  auto_generate: true
  from_entry_points: true

sync:
  strategy: markers    # markers | full | git-diff
  watch: false
  ignore:
    - "tests/"
    - "__pycache__"
```

## Sync Markers

clickmd can update only specific sections of an existing README using HTML comment markers:

```markdown
<!-- clickmd:start -->
# Project Title
... auto-generated content ...
<!-- clickmd:end -->
```

Content outside the markers is preserved when regenerating. Enable this with `sync_markers: true` in your configuration.

## Architecture

```
clickmd/
    ├── config_viewer    ├── basic    ├── logger_usage    ├── colored_logging    ├── one_liners    ├── cli_colors    ├── cli_app    ├── custom_renderer    ├── markdown_help    ├── phase3_progress    ├── phase1_features    ├── phase4_themes    ├── simple_cli    ├── md_to_html    ├── bump_version    ├── quickstart        ├── progress    ├── clickmd/        ├── rich_backend    ├── api_response        ├── renderer        ├── decorators    ├── phase5_devtools        ├── logger├── project        ├── help        ├── themes        ├── devtools```

## API Overview

### Classes

- **`ProgressBar`** — A customizable progress bar.
- **`Spinner`** — An animated spinner for indeterminate progress.
- **`LiveUpdate`** — Live-updating display that refreshes in place.
- **`StatusIndicator`** — A status indicator that shows step-by-step progress.
- **`MarkdownRenderer`** — —
- **`User`** — Sample user class for debugging.
- **`Logger`** — Markdown-aware logger that wraps output in codeblocks.
- **`Theme`** — Color theme definition.
- **`PrettyExceptionFormatter`** — Format exceptions with syntax highlighting and context.
- **`ClickmdHandler`** — Logging handler that formats logs with clickmd styling.

### Functions

- `show_yaml_config()` — Wyświetl przykładową konfigurację YAML.
- `show_json_config()` — Wyświetl przykładową konfigurację JSON.
- `show_toml_config()` — Wyświetl przykładową konfigurację TOML.
- `show_env_config()` — Wyświetl zmienne środowiskowe.
- `show_config_diff()` — Pokaż różnicę między konfiguracjami.
- `show_config_tree()` — Pokaż strukturę konfiguracji jako drzewo.
- `basic_usage()` — Basic Logger usage
- `action_logging()` — Action-based logging with emojis
- `progress_and_steps()` — Progress and step logging
- `exception_handling()` — Exception logging
- `grouped_output()` — Grouped output using sections
- `llm_logging()` — LLM-specific logging
- `mixed_output()` — Mixed markdown and log output
- `real_world_example()` — Real-world evolution pipeline example
- `main()` — —
- `cli()` — Example CLI application with clickmd.
- `hello(name, formal)` — Say hello with style.
- `status()` — Show application status.
- `example(language)` — Show code example for a language.
- `main()` — —
- `cli()` — # 🚀 My Awesome CLI
- `process(input, output, format, verbose)` — # Process Data
- `config(action, key, value)` — # Configuration Management
- `version()` — # Version Information
- `demo_progress_bar()` — Demonstrate progress bar.
- `demo_spinners()` — Demonstrate spinners.
- `demo_status_indicator()` — Demonstrate status indicator.
- `demo_live_update()` — Demonstrate live updates.
- `demo_countdown()` — Demonstrate countdown.
- `demo_combined()` — Demonstrate combined usage.
- `demo_tables()` — Demonstrate table rendering.
- `demo_panels()` — Demonstrate panel/box rendering.
- `demo_blockquotes()` — Demonstrate blockquote rendering.
- `demo_horizontal_rules()` — Demonstrate horizontal rule rendering.
- `demo_checklists()` — Demonstrate checklist rendering.
- `demo_nested_lists()` — Demonstrate nested list rendering.
- `demo_combined()` — Demonstrate combined usage.
- `demo_available_themes()` — Show available themes.
- `demo_theme_switching()` — Demonstrate theme switching.
- `demo_theme_colors()` — Show theme color palette.
- `demo_color_support()` — Show terminal color support detection.
- `demo_custom_theme()` — Demonstrate custom theme creation.
- `demo_no_color()` — Demonstrate NO_COLOR behavior.
- `demo_styled_output()` — Show styled output with current theme.
- `greet(name, loud)` — # 👋 Powitanie
- `cli()` — # 🛠️ Simple CLI Tool
- `hello(name)` — Przywitaj użytkownika.
- `info()` — # Informacje o systemie
- `status(format)` — Pokaż status aplikacji.
- `markdown_to_html(markdown_text, title)` — —
- `convert_directory(md_dir)` — —
- `main()` — —
- `bump_version(version_type)` — Bump version in pyproject.toml
- `progress(iterable, label, total)` — Wrap an iterable with a progress bar.
- `spinner(message, style)` — Context manager for a spinner.
- `live(initial)` — Context manager for live-updating display.
- `countdown(seconds, message, on_complete)` — Display a countdown timer.
- `menu(title, items, default, prompt_text)` — Display a numbered markdown menu and prompt for selection.
- `select(prompt_text, items, default)` — Inline numbered selection without a title heading.
- `echo(message, file, nl, err)` — Smart echo that auto-detects markdown and renders it with colors.
- `md(text)` — —
- `is_rich_available()` — Check if Rich is installed and available.
- `get_console(stream, force_terminal, no_color)` — Get or create a Rich Console instance.
- `render_md(text, stream, use_rich)` — Render markdown text to the terminal.
- `render_panel(content, title, style, stream)` — Render content in a styled panel/box.
- `render_syntax(code, language, theme, line_numbers)` — Render syntax-highlighted code.
- `render_table(headers, rows, title, stream)` — Render a formatted table.
- `print_md(text)` — Print markdown (alias for render_md).
- `print_panel(content)` — Print a panel (alias for render_panel).
- `print_syntax(code, language)` — Print syntax-highlighted code (alias for render_syntax).
- `print_table(headers, rows)` — Print a table (alias for render_table).
- `handle_api_error(response)` — Przykład obsługi błędu API z clickmd.
- `strip_ansi(text)` — —
- `get_renderer(stream, use_colors)` — —
- `render_markdown(text, text_lang, stream, use_colors)` — —
- `table(headers, rows)` — Render a table.
- `panel(content)` — Render a panel.
- `blockquote(content)` — Render a blockquote.
- `hr(char, width)` — Render a horizontal rule.
- `checklist(items)` — Render a checklist.
- `demo_debug()` — Demonstrate debug output.
- `demo_inspect()` — Demonstrate object inspection.
- `demo_tree()` — Demonstrate tree view.
- `demo_diff()` — Demonstrate diff visualization.
- `demo_logging()` — Demonstrate logging handler.
- `demo_pretty_exceptions()` — Demonstrate pretty exceptions.
- `demo_combined()` — Demonstrate combined usage.
- `get_logger(verbose)` — Get or create the default logger
- `set_logger(logger)` — Set the default logger
- `log_info(message)` — —
- `log_success(message)` — —
- `log_warning(message)` — —
- `log_error(message)` — —
- `log_action(action, message)` — —
- `success(message)` — Display a success message in a green panel.
- `warning(message)` — Display a warning message in a yellow panel.
- `error(message)` — Display an error message in a red panel.
- `info(message)` — Display an info message in a blue panel.
- `echo_md(text, err)` — Echo markdown-formatted text to the terminal.
- `get_theme()` — Get the current theme.
- `set_theme(name)` — Set the current theme by name.
- `register_theme(theme)` — Register a custom theme.
- `list_themes()` — Get list of available theme names.
- `is_no_color()` — Check if colors are disabled (NO_COLOR standard).
- `get_color_support()` — Get detected terminal color support level.
- `color(name, text, bold, dim)` — Apply color to text using current theme.
- `init_theme_from_env()` — Initialize theme from environment variables.
- `install_excepthook(show_locals, context_lines)` — Install pretty exception hook.
- `uninstall_excepthook()` — Restore original exception hook.
- `debug(obj, name, max_depth, max_items)` — Pretty-print an object for debugging.
- `inspect_obj(obj, markdown_safe)` — Inspect an object showing its type, methods, and attributes.
- `diff(old, new, old_name, new_name)` — Display a colored diff between two texts.
- `tree(data, prefix, is_last, name)` — Display data in a tree structure.


## Project Structure

📄 `examples.api_response` (1 functions)
📄 `examples.basic`
📄 `examples.cli_app` (4 functions)
📄 `examples.cli_colors`
📄 `examples.colored_logging` (1 functions)
📄 `examples.config_viewer` (6 functions)
📄 `examples.custom_renderer` (1 functions)
📄 `examples.logger_usage` (8 functions)
📄 `examples.markdown_help` (4 functions)
📄 `examples.one_liners`
📄 `examples.phase1_features` (7 functions)
📄 `examples.phase3_progress` (6 functions)
📄 `examples.phase4_themes` (7 functions)
📄 `examples.phase5_devtools` (7 functions, 1 classes)
📄 `examples.quickstart`
📄 `examples.simple_cli` (5 functions)
📄 `project`
📄 `scripts.bump_version` (1 functions)
📦 `src.clickmd` (4 functions)
📄 `src.clickmd.decorators`
📄 `src.clickmd.devtools` (20 functions, 2 classes)
📄 `src.clickmd.help` (9 functions)
📄 `src.clickmd.logger` (30 functions, 1 classes)
📄 `src.clickmd.progress` (30 functions, 4 classes)
📄 `src.clickmd.renderer` (50 functions, 1 classes)
📄 `src.clickmd.rich_backend` (13 functions, 1 classes)
📄 `src.clickmd.themes` (14 functions, 1 classes)
📄 `tools.md_to_html` (5 functions)

## Requirements

- Python >= >=3.10


## Contributing

**Contributors:**
- Tom Softreck <tom@sapletta.com>
- Tom Sapletta <tom-sapletta-com@users.noreply.github.com>

We welcome contributions! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
# Clone the repository
git clone https://github.com/wronai/clickmd
cd clickmd

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest
```

## Documentation

- 📖 [Full Documentation](https://github.com/wronai/clickmd/tree/main/docs) — API reference, module docs, architecture
- 🚀 [Getting Started](https://github.com/wronai/clickmd/blob/main/docs/getting-started.md) — Quick start guide
- 📚 [API Reference](https://github.com/wronai/clickmd/blob/main/docs/api.md) — Complete API documentation
- 🔧 [Configuration](https://github.com/wronai/clickmd/blob/main/docs/configuration.md) — Configuration options
- 💡 [Examples](./examples) — Usage examples and code samples

### Generated Files

| Output | Description | Link |
|--------|-------------|------|
| `README.md` | Project overview (this file) | — |
| `docs/api.md` | Consolidated API reference | [View](./docs/api.md) |
| `docs/modules.md` | Module reference with metrics | [View](./docs/modules.md) |
| `docs/architecture.md` | Architecture with diagrams | [View](./docs/architecture.md) |
| `docs/dependency-graph.md` | Dependency graphs | [View](./docs/dependency-graph.md) |
| `docs/coverage.md` | Docstring coverage report | [View](./docs/coverage.md) |
| `docs/getting-started.md` | Getting started guide | [View](./docs/getting-started.md) |
| `docs/configuration.md` | Configuration reference | [View](./docs/configuration.md) |
| `docs/api-changelog.md` | API change tracking | [View](./docs/api-changelog.md) |
| `CONTRIBUTING.md` | Contribution guidelines | [View](./CONTRIBUTING.md) |
| `examples/` | Usage examples | [Browse](./examples) |
| `mkdocs.yml` | MkDocs configuration | — |

<!-- code2docs:end -->