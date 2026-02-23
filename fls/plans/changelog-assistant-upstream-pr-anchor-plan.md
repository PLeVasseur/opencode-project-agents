# Plan: Anchor Changelog Assistant Updates to Existing Upstream PR Entries

## Goal
- [ ] Update `tools/changelog_assistant.py` so `--update` can anchor to an existing changelog bullet in the current release section when the upstream Rust PR URL is already present, replacing that entry instead of appending a duplicate.

## Problem statement
- [ ] Current behavior appends a new changelog entry at the end of the release section even when an entry for the same upstream Rust PR already exists.
- [ ] This causes duplicated changelog content and can inject placeholder URLs (for example `.../pull/999999`) during validation runs.

## Terminology / scope clarification
- [ ] Treat `--upstream-pr` as the **upstream language PR URL** (typically `https://github.com/rust-lang/rust/pull/<n>`), not an FLS PR URL.
- [ ] Anchor matching must be performed inside `Language changes in Rust <release>` only.

## Non-goals
- [ ] Do not redesign diff/tag detection logic in this change.
- [ ] Do not add CI wiring in this change.
- [ ] Do not modify historical changelog sections outside the target release section.

## Deliverables
- [ ] Tooling update in `tools/changelog_assistant.py` implementing anchor-or-append behavior.
- [ ] Optional strict mode flag to require anchor hit when desired.
- [ ] Update/check output clearly indicates whether update mode was `replace` or `append`.
- [ ] Validation artifacts under `$OPENCODE_CONFIG_DIR/reports/` showing behavior with both matching and non-matching upstream PR URLs.

## Session bootstrap checklist
- [ ] `printenv OPENCODE_CONFIG_DIR` resolves.
- [ ] `git fetch origin`.
- [ ] `git switch main`.
- [ ] `git pull --ff-only origin main`.
- [ ] Create/switch to a working branch (plain descriptive name), for example:
  - [ ] `git switch -c changelog-assistant-upstream-pr-anchor`
- [ ] `uv sync`.
- [ ] Record HEAD SHA and timestamp in the validation report.

## Report destination
- [ ] Define a unique report root for this run:
  - [ ] `REPORT_ROOT="$OPENCODE_CONFIG_DIR/reports/changelog-assistant-upstream-pr-anchor-<timestamp>"`
- [ ] `mkdir -p "$REPORT_ROOT"`.

## Design checklist

### 1) URL normalization strategy
- [ ] Add a helper that normalizes URLs before comparison.
- [ ] Normalize at least:
  - [ ] Trim whitespace.
  - [ ] Lowercase scheme/host.
  - [ ] Remove trailing slash from path.
  - [ ] Ignore query/fragment for matching.
- [ ] Keep original URL text when emitting changelog output.

### 2) Entry block parsing strategy
- [ ] Add helper(s) to identify top-level entry blocks in a release section:
  - [ ] Entry start is a line beginning with `- ` at column 0.
  - [ ] Entry end is next top-level `- ` line or section end.
- [ ] Add helper to extract URL from entry first line when it contains `` `<...>`_ ``.
- [ ] Ensure nested bullets (`  - ...`, `    - ...`) are not treated as top-level entries.

### 3) Anchor selection rules
- [ ] If `pr_url` is available (explicit or inferred), search the target release section for matching entry URL.
- [ ] If exactly one match exists, mark it as anchor target.
- [ ] If more than one match exists, fail with clear diagnostic (ambiguous anchor).
- [ ] If no match exists:
  - [ ] default behavior: append as today.
  - [ ] strict behavior (if enabled): fail with non-zero status.

## Implementation checklist

### 1) CLI behavior
- [ ] Add optional strict flag, e.g. `--require-anchor`.
- [ ] Document flag in argparse help string.
- [ ] Keep backward compatibility for existing command invocations.

### 2) Core update logic changes
- [ ] Refactor update path so it can either:
  - [ ] replace an existing entry block (`anchor hit`), or
  - [ ] append a new entry block (`anchor miss`).
- [ ] Avoid duplicating line-construction logic (`entry_lines(...)` remains single source).

### 3) Reporting improvements
- [ ] Extend emitted JSON report with update metadata:
  - [ ] `update_action`: `replace` or `append`.
  - [ ] `anchored_pr_url` (if any).
  - [ ] `anchored_entry_line` and/or `anchored_entry_index` (if any).
- [ ] Mirror concise anchor result in markdown report.

### 4) Error handling
- [ ] On `--require-anchor` + no match, exit non-zero with explicit error.
- [ ] On multiple matching entries, exit non-zero with explicit error and matching line hints.

## Validation checklist

### Metadata setup
- [ ] `BASE_REF="$(git merge-base HEAD origin/main)"`
- [ ] `RELEASE` resolved from `version.rst` (script default is acceptable).
- [ ] Define canonical existing upstream URL for validation:
  - [ ] `CANONICAL_UPSTREAM_PR="https://github.com/rust-lang/rust/pull/145954"`
- [ ] Define a non-existing URL for negative test:
  - [ ] `MISSING_UPSTREAM_PR="https://github.com/rust-lang/rust/pull/999999"`

### Pre-change baseline capture
- [ ] Save current tool help output:
  - [ ] `uv run python tools/changelog_assistant.py --help > "$REPORT_ROOT/help-before.txt"`
- [ ] Capture current changelog match count for canonical URL:
  - [ ] record in `$REPORT_ROOT/pre-anchor-count.txt` via a small script.

### Quality gate before behavior tests
- [ ] `uv run python -m py_compile tools/changelog_assistant.py`

### Behavior test A: anchor replace on existing URL
- [ ] Run update with canonical upstream URL and deterministic title:

```bash
uv run python tools/changelog_assistant.py \
  --update \
  --base "$BASE_REF" \
  --title "Anchor replace validation" \
  --upstream-pr "$CANONICAL_UPSTREAM_PR" \
  --emit-report "$REPORT_ROOT/update-anchor-hit"
```

- [ ] Verify exit code `0`.
- [ ] Verify report files exist:
  - [ ] `$REPORT_ROOT/update-anchor-hit.json`
  - [ ] `$REPORT_ROOT/update-anchor-hit.md`
- [ ] Verify `update_action` is `replace`.
- [ ] Capture changelog diff to `$REPORT_ROOT/diff-anchor-hit.patch`.
- [ ] Verify there is still a single top-level entry for `$CANONICAL_UPSTREAM_PR`.

### Behavior test B: idempotence on second anchored update
- [ ] Re-run the same update command and capture diff to `$REPORT_ROOT/diff-anchor-hit-second.patch`.
- [ ] Verify no duplicate entry is introduced.
- [ ] Preferably verify second run is no-op or minimal deterministic rewrite only.

### Behavior test C: append on anchor miss (default)
- [ ] Restore changelog to pre-test state if needed for clean comparison.
- [ ] Run update with `MISSING_UPSTREAM_PR` (without strict mode) and capture report:
  - [ ] Expect exit code `0`.
  - [ ] Expect `update_action` = `append`.

### Behavior test D: strict failure on anchor miss
- [ ] Run update with `MISSING_UPSTREAM_PR` and strict flag (`--require-anchor`).
- [ ] Verify non-zero exit.
- [ ] Verify error explains anchor miss.

### Post-check
- [ ] Run check mode after anchored update and record exit code:

```bash
uv run python tools/changelog_assistant.py \
  --check \
  --base "$BASE_REF" \
  --emit-report "$REPORT_ROOT/post-check"
```

- [ ] Save `git diff -- src/changelog.rst` to `$REPORT_ROOT/changelog.diff`.

## Final report checklist (`$REPORT_ROOT/summary.md`)
- [ ] Include all commands with exit codes.
- [ ] Include anchor-hit, anchor-miss, and strict-miss results.
- [ ] Include snippets proving canonical URL entry was replaced, not duplicated.
- [ ] Include the exact line/location evidence for the targeted entry before and after.
- [ ] Include any edge cases encountered and follow-up recommendations.

## Session response checklist
- [ ] Return exact worktree path and branch used.
- [ ] Return exact artifact paths under `$REPORT_ROOT`.
- [ ] Return clear statement of whether anchoring works for canonical upstream PR URL.
- [ ] Return whether strict mode behaved as expected.

## Acceptance criteria
- [ ] Running `--update` with canonical upstream PR URL updates/replaces the existing release entry instead of appending a duplicate.
- [ ] Re-running anchored update does not create additional duplicate entries.
- [ ] Missing URL behavior is explicit and test-covered for both default and strict modes.
- [ ] Report artifacts are sufficient for review in a fresh session.
