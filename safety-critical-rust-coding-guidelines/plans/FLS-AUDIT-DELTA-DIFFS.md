# FLS Audit Delta Diffs Plan

## Purpose

Add colored inline diffs to the FLS audit output using `delta`, with a seamless default setup for new contributors and consistent behavior in CI.

## Goals

- Provide ANSI-colored inline diffs for content changes.
- Auto-download a pinned `delta` release when missing, with checksum verification.
- Support `linux-x86_64`, `linux-aarch64`, `macos-aarch64`, and `windows-x86_64`.
- Add CLI controls: `--print-diffs`, `--delta-path`, `--no-delta`.
- Generate `build/fls_audit/report.ansi.md` alongside the existing reports.
- Mirror the delta style from the local git configuration (side-by-side, line numbers, file style, no decorations).

## Non-Goals

- Do not change the diff algorithm or JSON report schema.
- Do not require a manual delta install for normal usage.
- Do not embed ANSI escape codes in `report.md`.

## Design Overview

### Delta acquisition

- Add a small helper module (e.g., `scripts/common/delta_diff.py`) that:
  - Maps OS/arch to the `delta` release asset name.
  - Downloads a pinned `delta` version from GitHub Releases into
    `.cache/fls-audit/tools/delta/<version>/<target>/`.
    - Source URL pattern:
      `https://github.com/dandavison/delta/releases/download/v<version>/delta-<version>-<target>.<ext>`.
    - Store a hard-coded SHA256 map keyed by `<target>` and verify after download.
  - Verifies SHA256 checksums for all supported assets.
  - Extracts safely (tar.gz on Linux/macOS, zip on Windows) and sets executable bits.
  - Returns the resolved binary path.
- CLI behavior:
  - `--delta-path` uses a user-provided binary and skips download.
  - `--no-delta` disables all delta usage and skips download.
  - If download fails and no override is provided, fall back to a system `delta` if available, otherwise plain diffs with a warning.
  - Resolution order: `--no-delta` -> `--delta-path` -> cached pinned binary -> system `delta` -> plain diffs.
  - Cache ensures CI/local runs are fast after first download.

### Platform detection

- Use `sys.platform` + `platform.machine()` mapping:
  - `linux` + `x86_64` -> `x86_64-unknown-linux-gnu`
  - `linux` + `aarch64`/`arm64` -> `aarch64-unknown-linux-gnu`
  - `darwin` + `arm64` -> `aarch64-apple-darwin`
  - `win32` + `AMD64` -> `x86_64-pc-windows-msvc`
- If unsupported, warn and fall back to `--delta-path` or system `delta`.

### Diff rendering

- Keep current unified diff generation with `difflib.unified_diff`.
- Pipe the unified diff through `delta` to obtain ANSI output for:
  - CLI printing (`--print-diffs`).
  - Markdown report (`report.ansi.md`).
- Use explicit delta args to mirror the local git settings:
  - `--color-only`, `--paging=never`, `--side-by-side`, `--line-numbers`,
    `--file-style "bold yellow ul"`, `--file-decoration-style none`,
    `--hunk-header-decoration-style none`, `--max-line-length 0`,
    `--wrap-max-lines 0`, `--whitespace-error-style "red reverse"`.

### Report outputs

- Keep `build/fls_audit/report.md` unchanged for GitHub-friendly output.
- Add `build/fls_audit/report.ansi.md` with ANSI-colored diff blocks.
- Only produce ANSI report when not `--summary-only`.
- Viewing ANSI report:
  - `less -R build/fls_audit/report.ansi.md`
  - `bat --style=plain --paging=always build/fls_audit/report.ansi.md`
  - VS Code with an ANSI color extension.

## Implementation Steps

1) Add delta helper module
- Create `scripts/common/delta_diff.py` with:
  - Version constant and per-target checksum map.
  - Download and extraction helpers.
  - `resolve_delta_path()` returning an executable path or `None`.

2) Wire into `scripts/fls_audit.py`
- Add CLI flags: `--print-diffs`, `--delta-path`, `--no-delta`.
- Add a small formatter that runs `delta` with explicit args over unified diff text.
- Store ANSI diff output in memory for report generation.
- Print diffs to stdout only when `--print-diffs` is set.

3) Add ANSI report output
- Extend `build_markdown_report` or add a new helper to emit ANSI diff blocks.
- Write `build/fls_audit/report.ansi.md` next to the existing reports.

4) Documentation updates
- Update `docs/fls-audit.md` with:
  - `--print-diffs`, `--delta-path`, `--no-delta` usage.
  - Cache path for the delta binary.
  - How to view ANSI report (e.g., `less -R`).
- Update project-agent runbook and skill:
  - `runbooks/fls-spec-lock-audit.md`
  - `skills/fls-audit/SKILL.md`

5) Performance follow-up (fast-path)

- Avoid `git fetch --prune --tags` on every audit run.
- Only fetch from origin when the requested commit is missing.
- Benchmark `--print-diffs` before/after to confirm reduced wall time.

6) Performance follow-up (selective parsing)

- Reduce docutils work by parsing only files relevant to the change set.
- Compute changed `.rst` files via `git diff --name-only <baseline>..<current> -- src/**/*.rst`.
- Scan all `.rst` files (no docutils) for `.. toctree::` and `.. appendices::` directives.
- If an ordering file changed, parse that file and expand referenced entries.
  - Support `:glob:` and expand patterns relative to the directive file.
  - Include referenced files in the parse set even if unchanged.
- Parse the union of changed files and referenced ordering files for baseline/current.
- Benchmark `--print-diffs` before/after and compare reports for parity.

## Verification

- `uv run python scripts/fls_audit.py --summary-only`
- `uv run python scripts/fls_audit.py --print-diffs --baseline-text-snapshot <path> --write-text-snapshot <path>`
- Confirm:
  - `build/fls_audit/report.md` exists (plain).
  - `build/fls_audit/report.ansi.md` exists and renders with ANSI in terminal.
  - `--no-delta` produces plain diffs without download.

## Performance verification

- Profile `uv run python scripts/fls_audit.py --print-diffs` before/after.
- Expect reduced time in git fetch/ensure_repo path.
- Expect reduced time spent in docutils parsing when few files change.

## Progress Tracking

- [ ] Add delta helper module with download + checksum verification.
- [ ] Add CLI flags and wire delta rendering in `scripts/fls_audit.py`.
- [ ] Generate `report.ansi.md` with ANSI diff blocks.
- [ ] Update docs/runbook/skill references.
- [ ] Run verification commands.
