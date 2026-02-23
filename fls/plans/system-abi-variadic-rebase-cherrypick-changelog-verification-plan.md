# Plan: Rebase Assistant + ABI, Integrate, Generate, and Verify Changelog

## Goal
- [ ] Starting from current local state, produce a reproducible validation run that:
  - [ ] rebases the changelog assistant branch onto current `origin/main`,
  - [ ] confirms/rebases the ABI branch state onto current `origin/main`,
  - [ ] creates a fresh integration branch on top of ABI,
  - [ ] cherry-picks assistant commits needed for changelog generation + anchor replacement,
  - [ ] runs changelog generation and verification,
  - [ ] proves canonical upstream URL behavior is `replace` (no duplicate entry).

## Scope
- [ ] Repo: `/home/pete.levasseur/project/fls`
- [ ] Assistant source branch: `changelog-assistant-upstream-pr-anchor`
- [ ] ABI base branch: `system-abi-variadic`
- [ ] Canonical upstream PR URL under test:
  - [ ] `CANONICAL_UPSTREAM_PR="https://github.com/rust-lang/rust/pull/145954"`
- [ ] Do not push unless explicitly requested.

## Non-goals
- [ ] Do not force-push or rewrite remote history.
- [ ] Do not modify unrelated branches/worktrees beyond what is needed for this integration test.
- [ ] Do not write artifacts into the repo; write only under `$OPENCODE_CONFIG_DIR/reports/`.

## Required outputs
- [ ] Timestamped `REPORT_ROOT` under `$OPENCODE_CONFIG_DIR/reports/`.
- [ ] Rebase status evidence for assistant + ABI branches.
- [ ] Cherry-pick manifest (resolved SHAs + order) for integration branch.
- [ ] `pre-check`, `update`, `update-second`, and `post-check` JSON/MD report artifacts.
- [ ] Diff artifacts and anchor count evidence before/after updates.
- [ ] Consolidated command + exit code table.
- [ ] Final summary report: `$REPORT_ROOT/summary.md`.

## Session bootstrap checklist
- [ ] `printenv OPENCODE_CONFIG_DIR` resolves.
- [ ] `git fetch origin`.
- [ ] `uv sync`.
- [ ] Record UTC timestamp and operator metadata in report:
  - [ ] worktree path used for each branch operation,
  - [ ] active branch,
  - [ ] HEAD SHA,
  - [ ] `origin/main` SHA.

## Report destination
- [ ] Set and print a unique report root:
- [ ] `REPORT_ROOT="$OPENCODE_CONFIG_DIR/reports/system-abi-variadic-rebase-cherrypick-changelog-verification-<timestamp>"`
- [ ] `mkdir -p "$REPORT_ROOT"`.

## Command capture checklist
- [ ] For each key command, save stdout/stderr to `$REPORT_ROOT/<label>.stdout.txt`.
- [ ] Save exit code to `$REPORT_ROOT/<label>.exitcode`.
- [ ] Maintain a consolidated table at `$REPORT_ROOT/command-exit-codes.tsv`.

## Worktree hygiene rules
- [ ] If an existing worktree is dirty for a target branch, do not destroy or reset it.
- [ ] Prefer creating fresh temporary integration/rebase worktrees instead of modifying dirty ones.
- [ ] Use plain descriptive branch names (no `feat/` prefix requirement).

## Branch topology checklist

### 1) Assistant branch rebase (`changelog-assistant-upstream-pr-anchor`)
- [ ] Identify where this branch is checked out (`git worktree list`).
- [ ] Ensure branch worktree is clean before rebasing; if dirty, stop and report blocker.
- [ ] Capture pre-rebase evidence:
  - [ ] `ASSISTANT_PRE_SHA`
  - [ ] divergence from `origin/main` (`git rev-list --left-right --count origin/main...<branch>`)
  - [ ] merge-base with `origin/main`
- [ ] Rebase assistant branch onto `origin/main`.
- [ ] Capture post-rebase evidence:
  - [ ] `ASSISTANT_POST_SHA`
  - [ ] merge-base now equals `origin/main`
  - [ ] updated divergence counts.

### 2) ABI branch rebase/verification (`system-abi-variadic`)
- [ ] Identify where ABI branch is checked out.
- [ ] If checked-out ABI worktree is dirty, do not reuse it; create a clean ABI rebase worktree from `origin/system-abi-variadic`.
- [ ] Capture pre-check evidence:
  - [ ] `ABI_PRE_SHA`
  - [ ] merge-base with `origin/main`
  - [ ] divergence counts.
- [ ] If ABI merge-base already equals `origin/main`, mark as rebase no-op.
- [ ] Else rebase ABI branch onto `origin/main` and capture `ABI_POST_SHA`.

## Integration branch checklist

### 3) Create clean integration worktree
- [ ] Create a fresh worktree for integration branch off rebased/validated ABI head:
  - [ ] recommended branch name: `system-abi-variadic-anchor-integration-<timestamp>`
  - [ ] recommended path: `/home/pete.levasseur/project/fls-system-abi-variadic-anchor-integration-<timestamp>`
- [ ] Record integration worktree path + branch + HEAD SHA.

### 4) Resolve cherry-pick commit set from assistant branch
- [ ] Resolve SHAs by commit subject on rebased assistant branch (do not assume old SHAs after rebase):
  - [ ] `feat(changelog): add Sphinx-aware changelog automation` (prerequisite introducing `tools/changelog_assistant.py`)
  - [ ] `fix(changelog-assistant): anchor updates to existing upstream PR entries`
  - [ ] `ci(changelog-assistant): run coverage checks in pull requests`
- [ ] Write resolved SHAs to `$REPORT_ROOT/cherry-pick-manifest.txt`.

### 5) Cherry-pick onto integration branch
- [ ] Cherry-pick in this order:
  1. [ ] changelog automation prerequisite commit
  2. [ ] anchor replacement fix commit
  3. [ ] CI coverage-check commit
- [ ] If conflicts occur:
  - [ ] record conflict files and resolution notes in `$REPORT_ROOT/cherry-pick-conflicts.txt`
  - [ ] continue and capture final commit SHAs in integration stack manifest.
- [ ] Save final stack manifest to `$REPORT_ROOT/integration-stack-manifest.txt`:
  - [ ] ABI base SHA
  - [ ] cherry-picked commit SHAs (old -> new)
  - [ ] integration HEAD SHA

## Readiness checks on integration branch
- [ ] Confirm `tools/changelog_assistant.py` exists.
- [ ] Confirm `--help` includes `--require-anchor`.
- [ ] Confirm report metadata fields exist in code:
  - [ ] `update_action`
  - [ ] `anchored_pr_url`
  - [ ] `anchored_entry_line`
  - [ ] `anchored_entry_index`
- [ ] Record readiness verdict in `$REPORT_ROOT/readiness.txt`.

## Metadata setup for validation run
- [ ] Compute and record explicit base ref:
  - [ ] `BASE_REF="$(git merge-base HEAD origin/main)"`
- [ ] Use this exact `BASE_REF` for all assistant invocations in this run.
- [ ] Resolve `RELEASE` from `version.rst`.
- [ ] Set deterministic title:
  - [ ] `ENTRY_TITLE="Anchor replace validation (system-abi integration)"`

## Validation execution checklist

### A) Baseline anchor evidence
- [ ] Record canonical URL top-level entry count + line numbers before update:
  - [ ] artifact: `$REPORT_ROOT/anchor-before.txt`
- [ ] Expected baseline count in target release section: `1`.

### B) Pre-check
- [ ] Run:

```bash
uv run python tools/changelog_assistant.py \
  --check \
  --base "$BASE_REF" \
  --emit-report "$REPORT_ROOT/pre-check"
```

- [ ] Capture exit code and artifact existence:
  - [ ] `$REPORT_ROOT/pre-check.json`
  - [ ] `$REPORT_ROOT/pre-check.md`

### C) First update (anchor hit => replace)
- [ ] Run:

```bash
uv run python tools/changelog_assistant.py \
  --update \
  --base "$BASE_REF" \
  --title "$ENTRY_TITLE" \
  --upstream-pr "$CANONICAL_UPSTREAM_PR" \
  --emit-report "$REPORT_ROOT/update"
```

- [ ] Capture exit code (target `0`).
- [ ] Verify report files:
  - [ ] `$REPORT_ROOT/update.json`
  - [ ] `$REPORT_ROOT/update.md`
- [ ] Verify metadata in `update.json`:
  - [ ] `update_action == "replace"`
  - [ ] `anchored_pr_url == "$CANONICAL_UPSTREAM_PR"`
  - [ ] `anchored_entry_line` and `anchored_entry_index` present.

### D) Diff and quality checks after first update
- [ ] Save diff:

```bash
git diff -- src/changelog.rst > "$REPORT_ROOT/changelog-after-first.diff"
```

- [ ] Record canonical URL count + line(s) after first update:
  - [ ] `$REPORT_ROOT/anchor-after-first.txt`
- [ ] Confirm canonical URL top-level count remains exactly `1`.
- [ ] Confirm updated entry is in `Language changes in Rust <release>`.
- [ ] Confirm `Change tags:` line appears in updated block.

### E) Second update (idempotence)
- [ ] Re-run the same update command from step C.
- [ ] Capture exit code (target `0`).
- [ ] Save diff:

```bash
git diff -- src/changelog.rst > "$REPORT_ROOT/changelog-after-second.diff"
```

- [ ] Record canonical URL count + line(s) after second update:
  - [ ] `$REPORT_ROOT/anchor-after-second.txt`
- [ ] Confirm canonical URL top-level count remains exactly `1`.

### F) Post-check
- [ ] Run:

```bash
uv run python tools/changelog_assistant.py \
  --check \
  --base "$BASE_REF" \
  --emit-report "$REPORT_ROOT/post-check"
```

- [ ] Capture exit code (target `0`).
- [ ] Verify report files:
  - [ ] `$REPORT_ROOT/post-check.json`
  - [ ] `$REPORT_ROOT/post-check.md`

### G) Optional strict miss sanity check (recommended)
- [ ] Run strict miss with non-existing URL and `--require-anchor`.
- [ ] Expect non-zero exit and explicit anchor-miss error.
- [ ] Save artifacts as `$REPORT_ROOT/strict-miss.*`.

## Final report checklist (`$REPORT_ROOT/summary.md`)
- [ ] Include run metadata (paths, branches, SHAs, timestamps).
- [ ] Include bootstrap status (pass/fail per item).
- [ ] Include assistant rebase result (pre/post SHAs, divergence).
- [ ] Include ABI rebase/no-op result (pre/post SHAs, divergence).
- [ ] Include integration stack manifest and cherry-pick outcome.
- [ ] Include command list with exit codes.
- [ ] Include pre-check and post-check outcomes.
- [ ] Include anchor evidence before/after/after-second with exact lines.
- [ ] Include `update_action` evidence (`replace`) from report JSON.
- [ ] Include idempotence verdict.
- [ ] Include strict miss result (if run).
- [ ] Include acceptance criteria pass/fail.
- [ ] If any criterion fails, include remediation with concrete next actions.

## Session response checklist
- [ ] Return section-by-section checklist completion status.
- [ ] Return assistant/ABI/integration branch SHAs and branch names.
- [ ] Return command summary with exit codes.
- [ ] Return exact `REPORT_ROOT` artifact paths.
- [ ] Return exact integration worktree path + active branch.
- [ ] Return anchor verdict for canonical URL (`replace` expected).
- [ ] Return whether post-check passed (`0`) and, if not, why.

## Acceptance criteria
- [ ] Assistant branch is rebased onto current `origin/main` (or blocker explicitly documented).
- [ ] ABI branch is verified rebased/no-op against current `origin/main`.
- [ ] Integration branch exists on ABI base with required assistant commits cherry-picked in order.
- [ ] Canonical URL update run reports `update_action="replace"`.
- [ ] Canonical URL top-level entry count remains `1` before first update, after first update, and after second update.
- [ ] Post-check exits `0` (or blocker is explicitly documented with remediation).
- [ ] Report artifacts are complete and reviewable in a fresh session.
