# Plan: Verify HTML diff script polish

## Goals
- Move the verifier into `tools/` and keep it executable.
- Add an opt-out flag for output cleanup while keeping clean-by-default behavior.
- Add guardrails for missing generated glossary output before the second build.
- Update references to the new script path.
- Run the script once to confirm output and exit status.

## Checklist usage
- Use the checkboxes below to track progress.
- Mark an item complete by replacing `[ ]` with `[x]`.

## Prereqs
- Ensure `OPENCODE_CONFIG_DIR` is set (per repo instructions).
- Ensure `uv` is available for the script shebang.

## Path note
- After moving the script, use `./tools/verify-html-diff.py` explicitly in docs, plans, and commands.

## Steps
- [x] Move the script into `tools/`.
  - Target path: `tools/verify-html-diff.py`.
  - Preserve the `uv run` shebang and SPDX header.
  - Keep the file executable (`chmod +x`).
  - Update repo-root detection to search parents for `make.py` (since the script is no longer in the repo root).

- [x] Add an optional cleanup bypass flag.
  - Proposed flag: `--keep-output`.
  - Default behavior remains to delete `baseline/` and `generated/` before copying.

- [x] Add guardrails for generated glossary availability.
  - If `build/generated.glossary.rst` is missing, run `./generate-glossary.py`.
  - If still missing, fail with a clear error message.

- [x] Update references to the script path.
  - Ensure references use `./tools/verify-html-diff.py` in plans and docs under `$OPENCODE_CONFIG_DIR`.

- [x] Run the verifier once after updates.
  - `./tools/verify-html-diff.py` (default output `build/html-diff`).
  - Inspect `build/html-diff/html-diff.txt` and confirm exit status.

- [x] Commit.
  - Use a descriptive Conventional Commit message that captures the relocation and behavior changes.
  - Example: `chore(tooling): move html diff verifier and add safeguards`.
