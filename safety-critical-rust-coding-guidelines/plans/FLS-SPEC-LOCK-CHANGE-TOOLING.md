# FLS Spec Lock Audit Tooling Plan

## Purpose

Establish repeatable, non-ad-hoc tooling to detect upstream FLS changes, map them to guideline references, and produce a deterministic audit report. The tool will be the single source of truth for change analysis, and the skill must use the tool rather than reimplementing logic.

## Scope

- Create a new audit tool in the repo: `scripts/fls_audit.py`.
- Extract shared, Sphinx-free diff logic into `exts/coding_guidelines/fls_diff.py` and reuse it in both the audit tool and `exts/coding_guidelines/fls_checks.py`.
- Update the repo `README.md` to document how to run the audit tool.
- Configure the repo to use the uv build backend so the shared module is importable without `sys.path` hacks.
- Add a skill wrapper and runbook outside the repo (in `~/opencode-project-agents/safety-critical-rust-coding-guidelines/`).
- Update the helper script to set `OPENCODE_CONFIG_DIR` so the skill is discoverable.

## Constraints

- Repo changes are expected to include:
  - `scripts/fls_audit.py`
  - `exts/coding_guidelines/fls_diff.py`
  - `exts/coding_guidelines/fls_checks.py` (refactor to use shared diff logic)
  - `pyproject.toml` (uv build backend configuration)
  - `README.md`
- All plans, skills, runbooks, and helper-script changes live in `~/opencode-project-agents/...`.
- Use `uv run python ...` for script execution; do not invoke `python`/`python3` directly.

## Tooling Design

### Inputs

- Baseline: `src/spec.lock`
- Current: live `https://rust-lang.github.io/fls/paragraph-ids.json`
- Guideline references: `src/**/*.rst` and `src/**/*.rst.inc` (line-based parse of `:id:` and `:fls:`)

### Outputs

- Markdown report: `build/fls_audit/report.md`
- JSON report: `build/fls_audit/report.json`

### Diff Categories

- Added IDs
- Removed IDs
- Content checksum changed
- Section renumbered

### Mapping

Map changed FLS IDs to guideline `:fls:` references and list affected guideline IDs and files. If no overlap, report "no guideline impact".

### CLI Options

- `--output-dir <path>`
- `--summary-only`
- `--fail-on-impact`
- `--snapshot <path>` (optional: compare against a saved `paragraph-ids.json`)

### Packaging (uv build backend)

- Configure `pyproject.toml` to use `uv_build` as the build backend.
- Set `module-root = "exts"` and `module-name = "coding_guidelines"` so `uv run` installs the module and scripts can `import coding_guidelines.*` without `PYTHONPATH` or `sys.path` hacks.

## Documentation

- Update repo `README.md` with a concise "FLS audit tool" section, including:
  - `uv run python scripts/fls_audit.py`
  - Output location
  - Interpretation guidance
  - Reminder: updating `src/spec.lock` is a separate, manual step

## Skill Wrapper (Outside Repo)

- Place skill at `~/opencode-project-agents/safety-critical-rust-coding-guidelines/skills/<skill-name>/SKILL.md`.
- The skill must invoke the audit tool and summarize its output.
- Do not reimplement logic in the skill prompt.

## Environment Integration

- Update `~/opencode-project-agents/shell/opencode-env.sh` to set:
  - `OPENCODE_CONFIG_DIR="$HOME/opencode-project-agents/$repo"`
- Keep `OPENCODE_CONFIG` behavior unchanged so `AGENTS.md` continues to load.

## Acceptance Criteria

- Running the tool produces deterministic Markdown and JSON reports.
- Report correctly identifies added/removed/modified/renumbered IDs.
- Report accurately maps any changed IDs to guideline references.
- `README.md` documents the tool with `uv run` usage.
- Skill loads from project-agents and runs the tool.

## Progress Tracking

- [x] Update project `AGENTS.md` with uv usage instructions.
- [x] Configure `pyproject.toml` to use `uv_build` with `module-root = "exts"`.
- [x] Add `exts/coding_guidelines/fls_diff.py` (Sphinx-free diff logic).
- [x] Refactor `exts/coding_guidelines/fls_checks.py` to use the shared diff logic.
- [x] Implement `scripts/fls_audit.py` in repo.
- [x] Update repo `README.md` with audit tool usage.
- [x] Add runbook outside repo for tool usage.
- [x] Create skill wrapper outside repo that calls the tool.
- [x] Update helper script to set `OPENCODE_CONFIG_DIR`.
- [x] Validate tool output against `./make.py -c` `fls_diff_*` output.

## Notes

- Keep the project-agents directory focused on plans/skills/runbooks to avoid unexpected config overrides.
- Prefer stdlib in the audit script; add dependencies only if they materially reduce risk or complexity.
