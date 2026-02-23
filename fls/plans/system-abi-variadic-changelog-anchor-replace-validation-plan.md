# Plan: Validate Anchor Replacement on `system-abi-variadic`

## Goal
- [ ] Validate, with reproducible artifacts, that `tools/changelog_assistant.py --update` replaces the existing changelog entry anchored by the canonical upstream Rust PR URL instead of appending a duplicate.

## Canonical anchor under test
- [ ] `CANONICAL_UPSTREAM_PR="https://github.com/rust-lang/rust/pull/145954"`
- [ ] Anchor matching is validated inside `Language changes in Rust <release>` only.

## Scope
- [ ] Repository: `/home/pete.levasseur/project/fls`
- [ ] Branch under validation: `system-abi-variadic`
- [ ] Focus behavior: anchor hit => `update_action=replace`
- [ ] Include idempotence evidence (second anchored update does not create duplicate canonical entry)

## Non-goals
- [ ] Do **not** enable `--require-tags` for this run.
- [ ] Do **not** push any branch unless explicitly requested.
- [ ] Do **not** wire this into CI in this run.

## Required outputs
- [ ] A timestamped report directory under `$OPENCODE_CONFIG_DIR/reports/`.
- [ ] Pre-check, update, and post-check JSON/MD report files.
- [ ] `src/changelog.rst` diff artifacts (first and second anchored update).
- [ ] Anchor evidence proving canonical URL count stays exactly `1` before and after update.
- [ ] Tags-to-generated-content mapping evidence.
- [ ] Final summary report at `$REPORT_ROOT/summary.md`.

## Session bootstrap checklist
- [ ] `printenv OPENCODE_CONFIG_DIR` resolves.
- [ ] `git fetch origin`.
- [ ] `git switch system-abi-variadic`.
- [ ] `git pull --ff-only origin system-abi-variadic`.
- [ ] `uv sync`.
- [ ] Record worktree path, branch, HEAD SHA, and UTC timestamp.

## Branch readiness checklist (anchor logic availability)
- [ ] Confirm `tools/changelog_assistant.py` exists on checked-out branch.
- [ ] Confirm CLI includes `--require-anchor` in `--help` output.
- [ ] Confirm update report schema includes `update_action`/`anchored_pr_url` metadata.
- [ ] If missing, rebase branch onto `origin/main` (allowed for this validation), then re-run readiness checks.
- [ ] If still missing after rebase, stop and report blocker in summary.

## Report destination
- [ ] Set a unique report root:
- [ ] `REPORT_ROOT="$OPENCODE_CONFIG_DIR/reports/system-abi-variadic-changelog-anchor-replace-<timestamp>"`
- [ ] Example timestamp format: `2026-02-07T083000Z`.
- [ ] `mkdir -p "$REPORT_ROOT"`.

## Metadata checklist
- [ ] Set explicit base ref (must be used for all assistant invocations):
- [ ] `BASE_REF="$(git merge-base HEAD origin/main)"`
- [ ] Resolve `RELEASE` from `version.rst`.
- [ ] Set deterministic update title:
- [ ] `ENTRY_TITLE="Anchor replace validation (system-abi-variadic)"`

## Command capture checklist
- [ ] For every key command, capture stdout/stderr to `$REPORT_ROOT/<name>.stdout.txt`.
- [ ] For every key command, capture exit code in `$REPORT_ROOT/<name>.exitcode`.
- [ ] Maintain a consolidated command/exit table in `$REPORT_ROOT/command-exit-codes.tsv`.

## Execution checklist

### 1) Baseline anchor evidence (before any update)
- [ ] Record canonical anchor count and line numbers in the target release section to `$REPORT_ROOT/anchor-before.txt`.
- [ ] Expectation for this branch: exactly one canonical URL match (`count=1`).

### 2) Baseline coverage check (pre-check)
- [ ] Run:

```bash
uv run python tools/changelog_assistant.py \
  --check \
  --base "$BASE_REF" \
  --emit-report "$REPORT_ROOT/pre-check"
```

- [ ] Capture exit code.
- [ ] Verify artifacts exist:
- [ ] `$REPORT_ROOT/pre-check.json`
- [ ] `$REPORT_ROOT/pre-check.md`

### 3) Anchor-hit update run (must replace)
- [ ] Run:

```bash
uv run python tools/changelog_assistant.py \
  --update \
  --base "$BASE_REF" \
  --title "$ENTRY_TITLE" \
  --upstream-pr "$CANONICAL_UPSTREAM_PR" \
  --emit-report "$REPORT_ROOT/update"
```

- [ ] Capture exit code (target: `0`).
- [ ] Verify artifacts exist:
- [ ] `$REPORT_ROOT/update.json`
- [ ] `$REPORT_ROOT/update.md`
- [ ] Verify in `update.json`:
- [ ] `update_action == "replace"`
- [ ] `anchored_pr_url == "$CANONICAL_UPSTREAM_PR"`
- [ ] `anchored_entry_line` and `anchored_entry_index` are present.

### 4) Diff + release-section quality checks
- [ ] Capture diff:

```bash
git diff -- src/changelog.rst > "$REPORT_ROOT/changelog.diff"
```

- [ ] Confirm generated/updated entry is under `Language changes in Rust <release>`.
- [ ] Confirm `Change tags:` line is present in updated entry block.
- [ ] Confirm paragraph changes use `:p:` roles and section changes use `:ref:` roles.
- [ ] Save targeted snippet (with line numbers) to `$REPORT_ROOT/changelog-snippet.txt`.

### 5) Idempotence check (second anchored update)
- [ ] Re-run the exact update command from step 3 with same title and canonical URL.
- [ ] Capture exit code (target: `0`).
- [ ] Save diff after second run to `$REPORT_ROOT/changelog-second.diff`.
- [ ] Record canonical anchor count and lines after second run in `$REPORT_ROOT/anchor-after-second.txt`.
- [ ] Validate canonical URL top-level entry count remains exactly `1`.

### 6) Post-update coverage check
- [ ] Run:

```bash
uv run python tools/changelog_assistant.py \
  --check \
  --base "$BASE_REF" \
  --emit-report "$REPORT_ROOT/post-check"
```

- [ ] Capture exit code (target: `0`).
- [ ] Verify artifacts exist:
- [ ] `$REPORT_ROOT/post-check.json`
- [ ] `$REPORT_ROOT/post-check.md`

### 7) Tags-to-generated-content mapping evidence
- [ ] Build mapping evidence file: `$REPORT_ROOT/tag-mapping.md`.
- [ ] Include for each detected tag:
- [ ] `tag`
- [ ] corresponding change types from `update.json`
- [ ] generated bullet subsection label/content in `src/changelog.rst`
- [ ] Include missing-reference checks (`:p:` and `:ref:`) and results.

## Optional extension (only if time permits)
- [ ] Add a strict miss sanity check with a non-existing URL and `--require-anchor`, expect non-zero.
- [ ] Save artifacts as `$REPORT_ROOT/strict-miss.*`.

## Final report checklist (`$REPORT_ROOT/summary.md`)
- [ ] Include run metadata (worktree, branch, HEAD, BASE_REF, timestamp).
- [ ] Include bootstrap pass/fail checklist.
- [ ] Include readiness check results (anchor logic present/absent and rebase notes if used).
- [ ] Include command list with exit codes.
- [ ] Include pre-check result summary.
- [ ] Include update result summary (`replace` expected/observed).
- [ ] Include before/after canonical anchor count and line evidence.
- [ ] Include generated-entry quality assessment (release section, Change tags line, role usage).
- [ ] Include post-check result summary.
- [ ] Include tags-to-generated-content mapping.
- [ ] Include explicit acceptance criteria pass/fail status.
- [ ] If failed, include exact remediation steps with file/line hints.

## Operator handoff checklist (session response)
- [ ] Return checklist completion status by section.
- [ ] Return concise command summary with exit codes.
- [ ] Return exact artifact paths under `$REPORT_ROOT`.
- [ ] Return exact worktree path and active branch.
- [ ] Return pre-check vs post-check results.
- [ ] Return anchor outcome for canonical URL (`replace` expected).
- [ ] Return remediation suggestions if any acceptance criterion failed.

## Acceptance criteria
- [ ] Validation artifacts exist under `$REPORT_ROOT` and are reviewable in a fresh session.
- [ ] `update.json` shows `update_action="replace"` for canonical upstream URL.
- [ ] `src/changelog.rst` shows replacement behavior (no duplicate canonical URL entry).
- [ ] Canonical URL count remains `1` after first and second anchored updates.
- [ ] Post-update check exits `0`.
