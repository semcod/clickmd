# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Split `renderer.py` into smaller modules (highlighters, table, panel)
- Reduce cyclomatic complexity in `devtools.py` (CC=24 → ≤14)
- Split high-CC functions: `_highlight_line`, `table`, `_format_debug_value`

## [1.1.0] - 2026-03-05

### Changed
- **BREAKING (internal)**: Moved package source to `src/clickmd/` layout
- Updated `pyproject.toml` to use `src` layout with hatchling
- Updated coverage config to target `src/clickmd`

### Fixed
- Fixed `pyproject.toml` authors field format (must be inline tables)
- Fixed `publish-env/` directory polluting builds and analysis
- Added `--skip-existing` flag to `make publish` to avoid duplicate upload errors
- Added `publish-env/` and `publish-test-env/` to `.gitignore`

### Added
- `scripts/bump_version.py` for automated version bumping (patch/minor/major)
- `make publish-new` target: bumps version + builds + publishes
- `make tets` alias for common typo
- VERSION file sync in bump script

### Removed
- Stale `publish-env/` and `venv/` directories from repo

## [1.0.3] - 2026-03-05

### Fixed
- Simplified Makefile publish targets (removed temporary venv creation)
- Installed `build` and `twine` as dev dependencies

## [1.0.2] - 2026-03-05

### Fixed
- Fixed `pyproject.toml` authors format for hatchling compatibility
- Added project analysis files

## [1.0.1] - 2026-03-05

### Added
- Phase 1: Tables, panels, blockquotes, horizontal rules, checklists
- Phase 3: Progress bars, spinners, live updates, countdown
- Phase 4: Theming system with multiple built-in themes
- Phase 5: Developer tools (debug, inspect, diff, tree, pretty exceptions)
- `menu()` and `select()` interactive prompts
- `Logger` class with markdown-aware structured logging
- Optional Rich backend integration
- Markdown help formatter for Click (`MarkdownCommand`, `MarkdownGroup`)
- Comprehensive test suite (69 tests)
- Examples directory with 17 demo scripts

### Features
- Works without Click installed (zero dependencies for core)
- Auto-detects TTY for color output
- Supports custom output streams
- Type hints (`py.typed` marker)

## [1.0.0] - 2024-01-07

### Added
- Initial release
- `md()` function for markdown rendering
- `echo()` smart function with auto-detection
- `MarkdownRenderer` class with syntax highlighting
- Supported languages: Python, TypeScript/JavaScript, JSON, YAML, Bash, Markdown, Log
- Click decorators re-export (optional dependency)
