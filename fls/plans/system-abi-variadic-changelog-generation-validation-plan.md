# Plan: Validate Changelog Generation on `system-abi-variadic`

## Goal
- [ ] Demonstrate, with reproducible evidence, that `tools/changelog_assistant.py` can generate changelog content for the `system-abi-variadic` branch and pass follow-up coverage checks.

## Non-goals
- [ ] Do **not** enable `--require-tags` in this validation pass.
- [ ] Do **not** wire automatic changelog updates into CI.

## Required outputs
- [ ] A markdown report in `$OPENCODE_CONFIG_DIR/reports/` with command results and evidence.
- [ ] JSON/MD assistant reports for pre-check, update, and post-check runs.
- [ ] A captured changelog diff snippet showing the generated entry.
- [ ] Final output includes the exact worktree path used for validation so reviewers can inspect `src/changelog.rst` directly.

## Report destination
- [ ] Define a unique report root for this run:
  - [ ] `REPORT_ROOT="$OPENCODE_CONFIG_DIR/reports/system-abi-variadic-changelog-generation-<timestamp>"`
  - [ ] Example timestamp format: `2026-02-07T083000Z`.

## Session bootstrap checklist
- [ ] `printenv OPENCODE_CONFIG_DIR` resolves successfully.
- [ ] `git fetch origin`.
- [ ] `git switch system-abi-variadic`.
- [ ] `git pull --ff-only origin system-abi-variadic`.
- [ ] `uv sync` has run.
- [ ] Capture current commit SHA for traceability.

## Metadata checklist
- [ ] Determine base ref explicitly (do not rely on implicit defaults):
  - [ ] `BASE_REF="$(git merge-base HEAD origin/main)"`
- [ ] Determine release version from `version.rst` (assistant also records this).
- [ ] Choose validation metadata for generated entry:
  - [ ] `ENTRY_TITLE` (clear, branch-specific title).
  - [ ] `UPSTREAM_PR_URL` (real URL if known; placeholder acceptable for local validation).

## Execution checklist

### 1) Prepare report folder
- [ ] `mkdir -p "$REPORT_ROOT"`.
- [ ] Record environment context in report header (branch, HEAD, BASE_REF, date/time).

### 2) Baseline check (before update)
- [ ] Run:

```bash
uv run python tools/changelog_assistant.py \
  --check \
  --base "$BASE_REF" \
  --emit-report "$REPORT_ROOT/pre-check"
```

- [ ] Capture exit code and note expectation:
  - [ ] Exit `1` is acceptable if coverage is currently missing.
  - [ ] Exit `0` is acceptable if branch is already fully covered.
- [ ] Verify files exist:
  - [ ] `$REPORT_ROOT/pre-check.json`
  - [ ] `$REPORT_ROOT/pre-check.md`

### 3) Generate changelog entry
- [ ] Run:

```bash
uv run python tools/changelog_assistant.py \
  --update \
  --base "$BASE_REF" \
  --title "$ENTRY_TITLE" \
  --upstream-pr "$UPSTREAM_PR_URL" \
  --emit-report "$REPORT_ROOT/update"
```

- [ ] Verify files exist:
  - [ ] `$REPORT_ROOT/update.json`
  - [ ] `$REPORT_ROOT/update.md`

### 4) Post-update validation check
- [ ] Run:

```bash
uv run python tools/changelog_assistant.py \
  --check \
  --base "$BASE_REF" \
  --emit-report "$REPORT_ROOT/post-check"
```

- [ ] Verify files exist:
  - [ ] `$REPORT_ROOT/post-check.json`
  - [ ] `$REPORT_ROOT/post-check.md`
- [ ] Record exit code (target: `0`).

### 5) Inspect generated `src/changelog.rst`
- [ ] Capture diff to report artifact:

```bash
git diff -- src/changelog.rst > "$REPORT_ROOT/changelog.diff"
```

- [ ] Confirm generated entry appears under the correct release section.
- [ ] Confirm generated entry includes a `Change tags:` line.
- [ ] Confirm generated entry references changed IDs correctly:
  - [ ] paragraph IDs as `:p:` roles,
  - [ ] section IDs as `:ref:` roles.

### 6) Tags-to-entry mapping evidence
- [ ] Compare detected tags/changes from `$REPORT_ROOT/update.json` against inserted changelog lines.
- [ ] Record a concise mapping table in the final report:
  - [ ] `tag` -> `change types` -> `generated bullet content`.

## Optional helper check (recommended)
- [ ] Run a small validation script and capture output to `$REPORT_ROOT/mapping-check.txt`:

```bash
uv run python - <<'PY' > "$REPORT_ROOT/mapping-check.txt"
import json
import os
from pathlib import Path

report_root = Path(os.environ["REPORT_ROOT"])
report = json.loads((report_root / "update.json").read_text(encoding="utf-8"))
changelog = Path("src/changelog.rst").read_text(encoding="utf-8")

paragraph_ids = sorted({c["paragraph_id"] for c in report["changes"] if "paragraph_id" in c})
section_ids = sorted({c["section_id"] for c in report["changes"] if "section_id" in c})

missing_p = [pid for pid in paragraph_ids if f":p:`{pid}`" not in changelog]
missing_s = [sid for sid in section_ids if f":ref:`{sid}`" not in changelog]

print("tags:", ", ".join(report["tags"]) if report["tags"] else "<none>")
print("paragraph ids:", ", ".join(paragraph_ids) if paragraph_ids else "<none>")
print("section ids:", ", ".join(section_ids) if section_ids else "<none>")
print("missing :p: refs:", ", ".join(missing_p) if missing_p else "<none>")
print("missing :ref: refs:", ", ".join(missing_s) if missing_s else "<none>")
PY
```

## Final report checklist (`$REPORT_ROOT/summary.md`)
- [ ] Include command list with exit codes.
- [ ] Include pre-check result summary.
- [ ] Include generated entry snippet from `src/changelog.rst`.
- [ ] Include post-check result summary.
- [ ] Include tags detected vs generated content mapping.
- [ ] Include explicit pass/fail conclusion.
- [ ] If failed, include exact remediation suggestions (file + line targets when possible).

## Operator handoff checklist (session response)
- [ ] Return the exact worktree path used during execution.
- [ ] Return the active branch name for that worktree.
- [ ] Return a short inspect command list:
  - [ ] `git -C <worktree> status --short`
  - [ ] `git -C <worktree> diff -- src/changelog.rst`
  - [ ] `sed -n '<line-start>,<line-end>p' <worktree>/src/changelog.rst` (optional snippet view)

## Acceptance criteria
- [ ] Validation run artifacts are present under `$REPORT_ROOT`.
- [ ] `src/changelog.rst` contains a generated entry for branch changes.
- [ ] Post-update check succeeds (`--check` exit code `0`).
- [ ] Final summary report provides enough evidence for peer review in a new session.
