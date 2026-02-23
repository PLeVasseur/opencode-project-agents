# Plan: Dedupe-Based Rebase + ABI Integration + Changelog Verification

## Goal
- [ ] Use `dedupe-paragraph-ids-mainline` as the base for both:
  - [ ] changelog assistant branch work, and
  - [ ] system ABI branch work,
- [ ] then build an integration branch on top of ABI, cherry-pick assistant commits, generate changelog output, and verify replacement behavior for the canonical upstream PR URL.

## Target branch shape
- [ ] `main`
  - [ ] `dedupe-paragraph-ids-mainline`
    - [ ] `changelog-assistant-upstream-pr-anchor-on-dedupe`
    - [ ] `system-abi-variadic-on-dedupe`
      - [ ] `system-abi-variadic-anchor-integration-on-dedupe-<timestamp>`

## Scope
- [ ] Repo: `/home/pete.levasseur/project/fls`
- [ ] Dedupe base branch: `dedupe-paragraph-ids-mainline`
- [ ] Assistant source branch: `changelog-assistant-upstream-pr-anchor`
- [ ] ABI source branch: `system-abi-variadic`
- [ ] Canonical anchor URL:
  - [ ] `CANONICAL_UPSTREAM_PR="https://github.com/rust-lang/rust/pull/145954"`
- [ ] No push unless explicitly requested.

## Non-goals
- [ ] Do not rewrite published branch history unless explicitly requested.
- [ ] Do not destroy or reset dirty worktrees.
- [ ] Do not write run artifacts inside the repo.

## Safety model
- [ ] Create new `*-on-dedupe` branches instead of rebasing original branches in place.
- [ ] Use fresh worktrees for each rebased branch and integration branch.
- [ ] Preserve existing dirty worktrees untouched.

## Required outputs
- [ ] Timestamped report root under `$OPENCODE_CONFIG_DIR/reports/`.
- [ ] Rebase evidence for assistant and ABI derived branches (pre/post SHA + merge-base + divergence).
- [ ] Cherry-pick manifest and resulting integration stack manifest.
- [ ] Validation artifacts: `pre-check`, `update`, `update-second`, `post-check` JSON/MD files.
- [ ] Diff and anchor evidence before/after/after-second update.
- [ ] Consolidated command/exit ledger.
- [ ] Final summary: `$REPORT_ROOT/summary.md`.

## Session bootstrap checklist
- [ ] `printenv OPENCODE_CONFIG_DIR` resolves.
- [ ] `git fetch origin` succeeds.
- [ ] `uv sync` succeeds.
- [ ] Record metadata:
  - [ ] UTC timestamp,
  - [ ] repo path,
  - [ ] current branch,
  - [ ] `HEAD` SHA,
  - [ ] `origin/main` SHA,
  - [ ] `origin/dedupe-paragraph-ids-mainline` SHA.

## Report destination
- [ ] Set `REPORT_ROOT`:
- [ ] `REPORT_ROOT="$OPENCODE_CONFIG_DIR/reports/system-abi-variadic-dedupe-base-integration-<timestamp>"`
- [ ] `mkdir -p "$REPORT_ROOT"`
- [ ] Print/report exact `REPORT_ROOT` path.

## Command capture rules
- [ ] Save each key command stdout/stderr to `$REPORT_ROOT/<label>.stdout.txt`.
- [ ] Save each exit code to `$REPORT_ROOT/<label>.exitcode`.
- [ ] Maintain `$REPORT_ROOT/command-exit-codes.tsv` with `label<TAB>exit_code<TAB>command`.

## Step 1: Verify base branch prerequisites
- [ ] Confirm local/remote dedupe branch exists:
  - [ ] `dedupe-paragraph-ids-mainline`
  - [ ] `origin/dedupe-paragraph-ids-mainline`
- [ ] Confirm dedupe commit is reachable (expected commit message: `fix(paragraph-ids): deduplicate reused glossary IDs`).
- [ ] Record dedupe branch SHA in `$REPORT_ROOT/base-branch-shas.txt`.

## Step 2: Create assistant dedupe-based branch

### 2a) Create clean worktree
- [ ] Define:
  - [ ] `ANCHOR_REBASED_BRANCH="changelog-assistant-upstream-pr-anchor-on-dedupe"`
  - [ ] `ANCHOR_REBASED_WT="/home/pete.levasseur/project/fls-anchor-on-dedupe-<timestamp>"`
- [ ] If branch already exists, record and reuse only if clean; otherwise create fresh branch/worktree.
- [ ] Create worktree from source branch:
  - [ ] `git worktree add -b "$ANCHOR_REBASED_BRANCH" "$ANCHOR_REBASED_WT" changelog-assistant-upstream-pr-anchor`

### 2b) Rebase onto dedupe base
- [ ] In `ANCHOR_REBASED_WT`, record pre-rebase values:
  - [ ] `ANCHOR_PRE_SHA`
  - [ ] `ANCHOR_PRE_BASE_MAIN="$(git merge-base HEAD origin/main)"`
  - [ ] `git rev-list --left-right --count origin/main...HEAD`
- [ ] Rebase assistant-derived branch onto dedupe branch:
  - [ ] `git rebase --onto dedupe-paragraph-ids-mainline "$ANCHOR_PRE_BASE_MAIN"`
- [ ] Record post-rebase values:
  - [ ] `ANCHOR_POST_SHA`
  - [ ] `ANCHOR_POST_BASE_DEDUPE="$(git merge-base HEAD dedupe-paragraph-ids-mainline)"`
  - [ ] `git rev-list --left-right --count dedupe-paragraph-ids-mainline...HEAD`
- [ ] Verify dedupe branch is ancestor of rebased assistant branch.

## Step 3: Create ABI dedupe-based branch

### 3a) Create clean worktree
- [ ] Define:
  - [ ] `ABI_REBASED_BRANCH="system-abi-variadic-on-dedupe"`
  - [ ] `ABI_REBASED_WT="/home/pete.levasseur/project/fls-system-abi-on-dedupe-<timestamp>"`
- [ ] Create worktree from source branch:
  - [ ] `git worktree add -b "$ABI_REBASED_BRANCH" "$ABI_REBASED_WT" system-abi-variadic`

### 3b) Rebase onto dedupe base
- [ ] In `ABI_REBASED_WT`, record pre-rebase values:
  - [ ] `ABI_PRE_SHA`
  - [ ] `ABI_PRE_BASE_MAIN="$(git merge-base HEAD origin/main)"`
  - [ ] `git rev-list --left-right --count origin/main...HEAD`
- [ ] Rebase ABI-derived branch onto dedupe branch:
  - [ ] `git rebase --onto dedupe-paragraph-ids-mainline "$ABI_PRE_BASE_MAIN"`
- [ ] Record post-rebase values:
  - [ ] `ABI_POST_SHA`
  - [ ] `ABI_POST_BASE_DEDUPE="$(git merge-base HEAD dedupe-paragraph-ids-mainline)"`
  - [ ] `git rev-list --left-right --count dedupe-paragraph-ids-mainline...HEAD`
- [ ] Verify dedupe branch is ancestor of rebased ABI branch.

## Step 4: Create integration branch on ABI-on-dedupe

### 4a) Create integration worktree/branch
- [ ] Define:
  - [ ] `INTEGRATION_BRANCH="system-abi-variadic-anchor-integration-on-dedupe-<timestamp>"`
  - [ ] `INTEGRATION_WT="/home/pete.levasseur/project/fls-system-abi-anchor-integration-<timestamp>"`
- [ ] Create integration branch from `ABI_REBASED_BRANCH`:
  - [ ] `git worktree add -b "$INTEGRATION_BRANCH" "$INTEGRATION_WT" "$ABI_REBASED_BRANCH"`
- [ ] Record integration base SHA.

### 4b) Resolve assistant commits to cherry-pick
- [ ] In repo root, list assistant-derived commits on top of dedupe base:
  - [ ] `git log --reverse --format='%H %s' dedupe-paragraph-ids-mainline..$ANCHOR_REBASED_BRANCH`
- [ ] Build two manifest files:
  - [ ] `$REPORT_ROOT/assistant-commit-manifest-full.txt` (full ordered list)
  - [ ] `$REPORT_ROOT/assistant-commit-manifest-selected.txt` (selected picks)
- [ ] Required selected commits:
  - [ ] commit that introduces `tools/changelog_assistant.py` (changelog automation prerequisite)
  - [ ] commit `fix(changelog-assistant): anchor updates to existing upstream PR entries`
  - [ ] commit `ci(changelog-assistant): run coverage checks in pull requests`
- [ ] If additional prerequisite commits are needed for clean cherry-pick, include and document rationale.

### 4c) Cherry-pick selected commits into integration branch
- [ ] In `INTEGRATION_WT`, cherry-pick selected assistant commits in order.
- [ ] If conflict occurs:
  - [ ] resolve,
  - [ ] capture conflict details in `$REPORT_ROOT/cherry-pick-conflicts.txt`,
  - [ ] continue cherry-pick.
- [ ] Record resulting mapping old SHA -> new SHA in `$REPORT_ROOT/integration-stack-manifest.txt`.

## Step 5: Readiness checks in integration branch
- [ ] Confirm `tools/changelog_assistant.py` exists.
- [ ] Confirm help output includes `--require-anchor`.
- [ ] Confirm report metadata fields appear in code:
  - [ ] `update_action`
  - [ ] `anchored_pr_url`
  - [ ] `anchored_entry_line`
  - [ ] `anchored_entry_index`
- [ ] Confirm tool can compile:
  - [ ] `uv run python -m py_compile tools/changelog_assistant.py`
- [ ] Write readiness report to `$REPORT_ROOT/readiness.txt`.

## Step 6: Validation setup in integration worktree
- [ ] Determine explicit base ref:
  - [ ] `BASE_REF="$(git merge-base HEAD origin/main)"`
- [ ] Use this exact `BASE_REF` for all assistant invocations.
- [ ] Resolve release from `version.rst`.
- [ ] Define:
  - [ ] `ENTRY_TITLE="Anchor replace validation (abi-on-dedupe integration)"`
  - [ ] `CANONICAL_UPSTREAM_PR="https://github.com/rust-lang/rust/pull/145954"`
  - [ ] `MISSING_UPSTREAM_PR="https://github.com/rust-lang/rust/pull/999999"`

## Step 7: Execute verification sequence

### 7a) Baseline canonical anchor evidence
- [ ] Record canonical top-level entry count and line numbers before update:
  - [ ] `$REPORT_ROOT/anchor-before.txt`
- [ ] Expected baseline: count `1`.

### 7b) Pre-check
- [ ] Run:

```bash
uv run python tools/changelog_assistant.py \
  --check \
  --base "$BASE_REF" \
  --emit-report "$REPORT_ROOT/pre-check"
```

- [ ] Record exit code and artifact existence:
  - [ ] `$REPORT_ROOT/pre-check.json`
  - [ ] `$REPORT_ROOT/pre-check.md`

### 7c) First update (anchor hit)
- [ ] Run:

```bash
uv run python tools/changelog_assistant.py \
  --update \
  --base "$BASE_REF" \
  --title "$ENTRY_TITLE" \
  --upstream-pr "$CANONICAL_UPSTREAM_PR" \
  --emit-report "$REPORT_ROOT/update"
```

- [ ] Verify exit code `0`.
- [ ] Verify report files:
  - [ ] `$REPORT_ROOT/update.json`
  - [ ] `$REPORT_ROOT/update.md`
- [ ] Verify JSON metadata:
  - [ ] `update_action == "replace"`
  - [ ] `anchored_pr_url == "$CANONICAL_UPSTREAM_PR"`
  - [ ] `anchored_entry_line` present
  - [ ] `anchored_entry_index` present

### 7d) Post-first-update evidence
- [ ] Save diff:
  - [ ] `git diff -- src/changelog.rst > "$REPORT_ROOT/changelog-after-first.diff"`
- [ ] Record canonical count/lines after first update:
  - [ ] `$REPORT_ROOT/anchor-after-first.txt`
- [ ] Confirm canonical count remains `1`.

### 7e) Second update (idempotence)
- [ ] Re-run exact update command from step 7c.
- [ ] Verify exit code `0`.
- [ ] Save diff:
  - [ ] `git diff -- src/changelog.rst > "$REPORT_ROOT/changelog-after-second.diff"`
- [ ] Record canonical count/lines after second update:
  - [ ] `$REPORT_ROOT/anchor-after-second.txt`
- [ ] Confirm canonical count remains `1`.

### 7f) Anchor miss behavior checks
- [ ] Default miss (no strict flag):
  - [ ] run update with `$MISSING_UPSTREAM_PR`
  - [ ] expect exit `0`
  - [ ] expect `update_action="append"`
- [ ] Strict miss:
  - [ ] run update with `$MISSING_UPSTREAM_PR` + `--require-anchor`
  - [ ] expect non-zero exit
  - [ ] expect explicit anchor-miss error message

### 7g) Post-check
- [ ] Run:

```bash
uv run python tools/changelog_assistant.py \
  --check \
  --base "$BASE_REF" \
  --emit-report "$REPORT_ROOT/post-check"
```

- [ ] Capture exit code and artifacts:
  - [ ] `$REPORT_ROOT/post-check.json`
  - [ ] `$REPORT_ROOT/post-check.md`

## Step 8: Final summary report
- [ ] Write `$REPORT_ROOT/summary.md` with:
  - [ ] bootstrap pass/fail,
  - [ ] branch topology and SHAs,
  - [ ] assistant rebase evidence,
  - [ ] ABI rebase evidence,
  - [ ] cherry-pick manifest/results,
  - [ ] command exit table,
  - [ ] anchor behavior outcomes (`replace`, `append`, strict non-zero),
  - [ ] pre-check vs post-check outcomes,
  - [ ] acceptance criteria verdicts,
  - [ ] remediation suggestions for any failures.

## Session response checklist
- [ ] Return checklist completion status by section.
- [ ] Return exact derived branch names + SHAs:
  - [ ] `ANCHOR_REBASED_BRANCH`
  - [ ] `ABI_REBASED_BRANCH`
  - [ ] `INTEGRATION_BRANCH`
- [ ] Return concise command summary with exit codes.
- [ ] Return exact artifact paths under `REPORT_ROOT`.
- [ ] Return exact integration worktree path + active branch.
- [ ] Return anchor verdicts:
  - [ ] canonical URL => `replace`
  - [ ] missing URL default => `append`
  - [ ] missing URL strict => non-zero
- [ ] Return verification result (`post-check` pass/fail) with blockers if any.

## Acceptance criteria
- [ ] Both derived branches (`*-on-dedupe`) have `dedupe-paragraph-ids-mainline` as ancestor.
- [ ] Integration branch is based on ABI-on-dedupe and contains selected assistant commits in order.
- [ ] Canonical URL update run reports `update_action="replace"`.
- [ ] Canonical URL top-level count remains exactly `1` before, after first update, and after second update.
- [ ] Missing URL behavior validated for default append and strict non-zero.
- [ ] Final report artifacts are sufficient to review in a fresh session.
