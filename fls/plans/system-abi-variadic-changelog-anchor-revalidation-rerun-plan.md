# Plan: Re-run System ABI Variadic Anchor Replacement Validation

## Goal
- [x] Re-run the canonical upstream URL replacement validation on `system-abi-variadic` after porting anchor-aware update logic into the local `tools/changelog_assistant.py` used by that worktree.

## Scope and constraints
- [x] Worktree under test: `/home/pete.levasseur/project/fls-system-abi-variadic-validation`
- [x] Branch under test: `system-abi-variadic`
- [x] Canonical anchor URL: `https://github.com/rust-lang/rust/pull/145954`
- [x] Keep artifacts under `$OPENCODE_CONFIG_DIR/reports/`
- [x] Do not push.

## Execution checklist

### 1) Session/bootstrap
- [x] Confirm `OPENCODE_CONFIG_DIR` and record it.
- [x] Ensure branch/worktree metadata is captured (path, branch, HEAD, UTC timestamp).
- [x] Create new timestamped `REPORT_ROOT` for this rerun.

### 2) Port replacement logic into test worktree
- [x] Compare `tools/changelog_assistant.py` in source worktree (`/home/pete.levasseur/project/fls`) and test worktree.
- [x] Port anchor-aware update logic (`replace`/`append`, `--require-anchor`, metadata fields) into `/home/pete.levasseur/project/fls-system-abi-variadic-validation/tools/changelog_assistant.py`.
- [x] Verify help output includes `--require-anchor`.
- [x] Verify script contains `update_action`, `anchored_pr_url`, `anchored_entry_line`, `anchored_entry_index` fields in report output.

### 3) Prepare verification baseline for rerun
- [x] Save a backup copy of current `src/changelog.rst` into `REPORT_ROOT`.
- [x] Restore `src/changelog.rst` in worktree to the pre-validation baseline (single canonical URL entry) for this rerun.
- [x] Confirm canonical URL top-level entry count before update is `1` and record line number(s).

### 4) Execute validation sequence (same behavior checks)
- [x] Compute explicit `BASE_REF="$(git merge-base HEAD origin/main)"` and use it for all assistant invocations.
- [x] Run pre-check (`--check`) and capture stdout/stderr + exit code + report files.
- [x] Run first update (`--update` with canonical URL) and capture stdout/stderr + exit code + report files.
- [x] Verify first update metadata indicates `update_action=replace` with anchor fields present.
- [x] Capture `git diff -- src/changelog.rst` after first update.
- [x] Run second identical update for idempotence and capture stdout/stderr + exit code + report files.
- [x] Capture `git diff -- src/changelog.rst` after second update.
- [x] Run post-check (`--check`) and capture stdout/stderr + exit code + report files.

### 5) Evidence and quality checks
- [x] Record canonical URL top-level entry count/line before first update.
- [x] Record canonical URL top-level entry count/line after first update.
- [x] Record canonical URL top-level entry count/line after second update.
- [x] Verify count remains exactly `1` throughout (`replace`, no duplication).
- [x] Verify updated entry is in the correct release section and includes `Change tags:`.
- [x] Verify role usage for generated references remains consistent (`:p:` for paragraphs, `:ref:` for sections).
- [x] Build tags-to-generated-content mapping artifact.

### 6) Reporting and handoff
- [x] Maintain `command-exit-codes.tsv` in `REPORT_ROOT`.
- [x] Write final rerun summary to `$REPORT_ROOT/summary.md` with pass/fail acceptance outcomes.
- [x] Include exact artifact paths, readiness outcome, pre/post-check results, and anchor verdict.
- [x] Include remediation steps if anything fails.

## Acceptance criteria
- [x] `tools/changelog_assistant.py --help` in the test worktree includes `--require-anchor`.
- [x] Update report JSON includes anchor metadata fields.
- [x] Canonical URL behavior is `replace` (not append).
- [x] Canonical URL count remains `1` before, after first update, and after second update.
- [ ] Post-check exits `0`.

## Outcome note
- [x] Anchor replacement/idempotence behavior validated; outstanding blocker is check-mode coverage failure for `fls_I9JaKZelMiby` and `fls_t4yeovFm83Wo` (see rerun `summary.md`).
