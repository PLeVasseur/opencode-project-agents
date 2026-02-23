# Plan: Migrate verify-html-diff.py into the repo

## Goals
- Move `verify-html-diff.py` into the repo root and make it usable without `OPENCODE_CONFIG_DIR`.
- Keep outputs under `build/` by default, with an explicit flag to override the output location.
- Make the script deterministic (no stale artifacts), run from any working directory, and fail on differences.
- Run the script once after migration to validate and inspect the report.
- Update the migration plan reference to point at the new in-repo script.

## Steps
1. Add `verify-html-diff.py` to the repo root.
   - Preserve the `uv run` shebang and SPDX header.
   - Replace `OPENCODE_CONFIG_DIR` usage with a CLI flag such as `--output-dir` (default `build/html-diff`).
   - Resolve relative `--output-dir` paths against the repo root.
   - Layout under `build/html-diff/`:
     - `baseline/`
     - `generated/`
     - `html-diff.txt`
   - Allow `--output-dir` to point to `$OPENCODE_CONFIG_DIR/reports/html-diff` when needed.
   - Ensure the output root is created (`mkdir(parents=True, exist_ok=True)`).

2. Make output generation deterministic.
   - Remove `baseline/` and `generated/` directories before copying (avoid stale files from prior runs).
   - Keep the report file under the output root.

3. Allow running from any working directory.
   - Derive repo root from `Path(__file__).resolve().parent`.
   - Keep the `make.py` existence check and emit a clear error if missing.

4. Fix exit status behavior.
   - Return non-zero when differences are found, after writing the report.

5. Optional cleanup.
   - Remove the explicit `generate-glossary.py` call in the script since `make.py` already runs it.

6. Update the migration plan reference.
   - In `/home/pete.levasseur/opencode-project-agents/fls/plans/glossary-migration-phase2.md`, replace the config-dir path with the new in-repo script invocation.

7. Run the script once after migration.
   - Execute `./tools/verify-html-diff.py` (or `python3 tools/verify-html-diff.py`) from the repo root.
   - If you need outputs under `$OPENCODE_CONFIG_DIR`, pass `--output-dir $OPENCODE_CONFIG_DIR/reports/html-diff`.
   - Inspect `build/html-diff/html-diff.txt` for differences; keep the run result in the session notes.

8. Make the script executable.
   - `chmod +x tools/verify-html-diff.py` so `./tools/verify-html-diff.py` works.

9. Commit.
   - Use a Conventional Commit message, e.g., `chore(tooling): add html diff verifier`.
