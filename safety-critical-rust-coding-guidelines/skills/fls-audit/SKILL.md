---
name: fls-audit
description: Run the FLS spec lock audit and summarize changes.
compatibility: opencode
---

# Skill: FLS Spec Lock Audit

## Purpose

Run the FLS audit tool and summarize changes and guideline impact. The skill must invoke the audit tool and must not reimplement diff logic.

## Steps

1. Run the audit tool:

   ```shell
   uv run python scripts/fls_audit.py
   ```

   If before/after diffs are needed:

   ```shell
   uv run python scripts/fls_audit.py --write-text-snapshot build/fls_audit/snapshots
   uv run python scripts/fls_audit.py --baseline-text-snapshot build/fls_audit/snapshots/<snapshot>.json
   ```

2. Read the report at `build/fls_audit/report.md` and summarize:

   - Added/removed/changed/renumbered/header counts
   - Whether any guidelines are affected
   - Any new paragraphs that are near existing guidelines
   - Heuristic top-3 guideline matches per paragraph
   - Any meaningful impacts that require rationalization

3. If no guidelines are affected, state that explicitly.

## Notes

- Use `--summary-only` if the user wants a quick console summary.
- Use `--snapshot path/to/paragraph-ids.json` for offline audits.
- Use `--baseline-text-snapshot` to show before/after diffs.
- Use `--write-text-snapshot` to capture current text for future audits.
- Use `--baseline-deployment-offset N` when the baseline deployment is not the most recent.
- Deployment offsets require GitHub API access; set `GITHUB_TOKEN` or use explicit commits.
- Use `--baseline-fls-commit` / `--current-fls-commit` for manual commit selection.
- Use `--include-legacy-report` to append the legacy diff section.
- Use `--include-heuristic-details` to show top-match details.
- Use `--print-diffs` to emit ANSI-colored diffs to stdout when available.
- Use `--delta-path path/to/delta` to point to a specific delta binary.
- Use `--no-delta` to disable delta rendering.
- Do not update `src/spec.lock` unless the user explicitly requests it.

## ANSI report

- The audit writes `build/fls_audit/report.ansi.md` alongside `report.md`.
- View it in a terminal with `less -R build/fls_audit/report.ansi.md`.
