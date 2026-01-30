# FLS Spec Lock Audit Runbook

## Purpose

Provide a repeatable process to audit differences between the live Ferrocene Language Specification (FLS) and `src/spec.lock`, and determine whether any guidelines are affected.

## Prerequisites

- Run from the repo root: `/home/pete.levasseur/scrc/safety-critical-rust-coding-guidelines`.
- `uv` is installed and available on PATH.
- Network access for live FLS data, or a local `paragraph-ids.json` snapshot.

## Procedure

1. Run the audit tool:

   ```shell
   uv run python scripts/fls_audit.py
   ```

   To print ANSI-colored diffs to the terminal:

   ```shell
   uv run python scripts/fls_audit.py --print-diffs
   ```

2. (Optional) Capture before/after text diffs by creating a baseline snapshot:

   ```shell
   uv run python scripts/fls_audit.py --write-text-snapshot build/fls_audit/snapshots
   uv run python scripts/fls_audit.py --baseline-text-snapshot build/fls_audit/snapshots/<snapshot>.json
   ```

3. Review the report:

   - `build/fls_audit/report.md`
   - `build/fls_audit/report.ansi.md`
   - `build/fls_audit/report.json`

   View the ANSI report with:

   ```shell
   less -R build/fls_audit/report.ansi.md
   ```

4. If guidelines are affected:

   - Review the old vs. new FLS paragraph text for each impacted FLS ID.
   - Determine whether each guideline needs rationalization or updates.

5. When the audit is complete and any guideline changes are ready, update the spec lock file:

   ```shell
   ./make.py --update-spec-lock-file
   ```

6. Open a PR with only the necessary guideline rationalization changes and the updated `src/spec.lock`.

## Options

- `--summary-only`: print a console summary and skip writing reports.
- `--snapshot path/to/paragraph-ids.json`: use a local FLS snapshot for offline comparisons.
- `--baseline-text-snapshot path/to/snapshot.json`: include before/after diffs.
- `--write-text-snapshot path/to/output.json`: capture the current text for future comparisons.
- `--baseline-deployment-offset N`: use the Nth prior Pages deployment as baseline.
- `--baseline-fls-commit <sha>` / `--current-fls-commit <sha>`: manual commit selection.
- `--include-legacy-report`: include legacy diff output in the report files.
- `--include-heuristic-details`: include top-match details in the heuristic section.
- `--fail-on-impact`: exit non-zero if any guidelines are affected (useful for CI).
- `--print-diffs`: print ANSI-colored diffs to stdout when available.
- `--delta-path path/to/delta`: use a specific delta binary.
- `--no-delta`: disable delta diff rendering.

## Notes

- The build process also writes `/tmp/fls_diff_<random>.txt` when spec lock mismatches are detected.
- The audit report groups changes by type, highlights new paragraphs near existing guidelines,
  and includes a heuristic section with top-3 guideline matches per paragraph.
- Listing deployment offsets requires GitHub API access (`GITHUB_TOKEN` recommended in CI).
- The audit tool caches the FLS repo and delta binaries under `./.cache/fls-audit/` and it is safe to delete.
- The audit tool is the source of truth for change analysis; the skill should only invoke the tool.
