# Plan: Preserve Anchored Changelog Title by Default + ABI-on-Dedupe Integration

## Goal
- [ ] Update `tools/changelog_assistant.py` so anchor-hit updates preserve the existing changelog entry title by default.
- [ ] Add an explicit `--replace-title` override that allows intentional title replacement on anchor-hit updates.
- [ ] Validate behavior on the assistant branch first.
- [ ] Re-run dedupe-based ABI integration with cherry-picked assistant commits.
- [ ] Verify canonical and missing-anchor behavior end-to-end with full report artifacts.

## Target branch shape
- [ ] `main`
  - [ ] `dedupe-paragraph-ids-mainline`
    - [ ] `changelog-assistant-upstream-pr-anchor-title-preserve-on-dedupe`
    - [ ] `system-abi-variadic-on-dedupe`
      - [ ] `system-abi-variadic-anchor-title-preserve-integration-on-dedupe-<timestamp>`

## Scope
- [ ] Repo: `/home/pete.levasseur/project/fls`
- [ ] Dedupe base branch: `dedupe-paragraph-ids-mainline`
- [ ] Assistant source branch: `changelog-assistant-upstream-pr-anchor`
- [ ] ABI source branch: `system-abi-variadic`
- [ ] Canonical upstream URL under test:
  - [ ] `CANONICAL_UPSTREAM_PR="https://github.com/rust-lang/rust/pull/145954"`
- [ ] Missing upstream URL under test:
  - [ ] `MISSING_UPSTREAM_PR="https://github.com/rust-lang/rust/pull/999999"`
- [ ] Do not push unless explicitly requested.

## Non-goals
- [ ] Do not rewrite published history in place.
- [ ] Do not modify ABI spec content outside integration/changelog validation needs.
- [ ] Do not write reports in the repo.

## Safety model
- [ ] Keep source branches untouched; use derived `*-on-dedupe` branches for rebases.
- [ ] Preserve dirty worktrees; create fresh worktrees when needed.
- [ ] Use timestamped report roots under `$OPENCODE_CONFIG_DIR/reports/`.

## Required outputs
- [ ] Timestamped report root with command ledger and per-command stdout/stderr/exitcode files.
- [ ] Assistant implementation evidence (`--replace-title` support + default preserve behavior).
- [ ] Rebase evidence for assistant and ABI derived branches (pre/post SHA, merge-base, divergence).
- [ ] Cherry-pick mapping (`old SHA -> new SHA`) for integration branch.
- [ ] Validation artifacts for:
  - [ ] pre-check,
  - [ ] canonical preserve-default update,
  - [ ] canonical replace-title update,
  - [ ] canonical replace-title idempotence rerun,
  - [ ] missing strict miss,
  - [ ] missing default append,
  - [ ] post-check.
- [ ] Final summary report with acceptance criteria and remediation.

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
- [ ] `REPORT_ROOT="$OPENCODE_CONFIG_DIR/reports/system-abi-variadic-anchor-title-preserve-and-integration-<timestamp>"`
- [ ] `mkdir -p "$REPORT_ROOT"`
- [ ] Print/report exact `REPORT_ROOT` path.

## Command capture rules
- [ ] Save each key command stdout/stderr to `$REPORT_ROOT/<label>.stdout.txt` and `$REPORT_ROOT/<label>.stderr.txt`.
- [ ] Save each exit code to `$REPORT_ROOT/<label>.exitcode`.
- [ ] Maintain `$REPORT_ROOT/command-exit-codes.tsv` with `label<TAB>exit_code<TAB>command`.

## Step 1: Implement preserve-by-default title semantics on assistant branch

### 1a) Assistant branch prep
- [ ] Confirm working branch (expected: `changelog-assistant-upstream-pr-anchor`) and record SHA.
- [ ] Record current behavior evidence (anchor-hit update replaces first line title).

### 1b) Code changes in `tools/changelog_assistant.py`
- [ ] Add CLI flag:
  - [ ] `--replace-title` (`store_true`) with help text clarifying it only applies on anchor-hit replacement.
- [ ] Refactor entry rendering helpers so first-line generation can be controlled:
  - [ ] Keep current generated first-line behavior for append.
  - [ ] For anchor-hit + default mode, preserve existing first line from anchored entry.
  - [ ] For anchor-hit + `--replace-title`, generate first line from provided/inferred title + PR URL.
- [ ] Keep anchor selection and `--require-anchor` semantics unchanged.
- [ ] Ensure report metadata still includes:
  - [ ] `update_action`,
  - [ ] `anchored_pr_url`,
  - [ ] `anchored_entry_line`,
  - [ ] `anchored_entry_index`.
- [ ] Ensure TODO warning behavior remains correct (warn only when TODO headline is inserted).

### 1c) Assistant branch readiness and local validation
- [ ] `uv run python -m py_compile tools/changelog_assistant.py`
- [ ] Confirm `--help` includes both `--require-anchor` and `--replace-title`.
- [ ] Run changelog tag verifier compare mode:
  - [ ] `uv run python tools/changelog_tag_verifier.py --mode compare --report-dir "$REPORT_ROOT/assistant-compare"`
- [ ] Run changelog tag verifier extract mode:
  - [ ] `uv run python tools/changelog_tag_verifier.py --mode extract --report-dir "$REPORT_ROOT/assistant-extract"`
- [ ] Run targeted anchor behavior checks on assistant branch:
  - [ ] canonical URL + mismatched `--title` without `--replace-title` => `replace` + first line preserved,
  - [ ] canonical URL + mismatched `--title` with `--replace-title` => `replace` + first line changed.
- [ ] Record diffs/artifacts for both scenarios.

### 1d) Commit on assistant branch
- [ ] Stage relevant assistant script/test/workflow updates.
- [ ] Commit with Conventional Commit message, e.g.:
  - [ ] `fix(changelog-assistant): preserve anchored entry title by default`
- [ ] Record new assistant commit SHA for integration cherry-pick manifest.

## Step 2: Verify base branch prerequisites for dedupe integration
- [ ] Confirm local and remote dedupe branches exist:
  - [ ] `dedupe-paragraph-ids-mainline`
  - [ ] `origin/dedupe-paragraph-ids-mainline`
- [ ] Confirm expected dedupe commit message is reachable:
  - [ ] `fix(paragraph-ids): deduplicate reused glossary IDs`
- [ ] Record base SHAs in `$REPORT_ROOT/base-branch-shas.txt`.

## Step 3: Create assistant dedupe-based derived branch

### 3a) Worktree/branch setup
- [ ] Define:
  - [ ] `ANCHOR_REBASED_BRANCH="changelog-assistant-upstream-pr-anchor-title-preserve-on-dedupe"`
  - [ ] `ANCHOR_REBASED_WT="/home/pete.levasseur/project/fls-anchor-title-preserve-on-dedupe-<timestamp>"`
- [ ] Create derived branch/worktree from assistant source branch (reuse only if existing worktree is clean).

### 3b) Rebase onto dedupe
- [ ] Record pre-rebase values:
  - [ ] `ANCHOR_PRE_SHA`
  - [ ] `ANCHOR_PRE_BASE_MAIN="$(git merge-base HEAD origin/main)"`
  - [ ] `git rev-list --left-right --count origin/main...HEAD`
- [ ] Rebase with:
  - [ ] `git rebase --onto dedupe-paragraph-ids-mainline "$ANCHOR_PRE_BASE_MAIN"`
- [ ] Record post-rebase values:
  - [ ] `ANCHOR_POST_SHA`
  - [ ] `ANCHOR_POST_BASE_DEDUPE="$(git merge-base HEAD dedupe-paragraph-ids-mainline)"`
  - [ ] `git rev-list --left-right --count dedupe-paragraph-ids-mainline...HEAD`
- [ ] Verify dedupe is ancestor of rebased assistant branch.

## Step 4: Create ABI dedupe-based derived branch

### 4a) Worktree/branch setup
- [ ] Define:
  - [ ] `ABI_REBASED_BRANCH="system-abi-variadic-on-dedupe"`
  - [ ] `ABI_REBASED_WT="/home/pete.levasseur/project/fls-system-abi-on-dedupe-<timestamp>"`
- [ ] Create derived branch/worktree from ABI source branch (reuse only if existing worktree is clean).

### 4b) Rebase onto dedupe
- [ ] Record pre-rebase values:
  - [ ] `ABI_PRE_SHA`
  - [ ] `ABI_PRE_BASE_MAIN="$(git merge-base HEAD origin/main)"`
  - [ ] `git rev-list --left-right --count origin/main...HEAD`
- [ ] Rebase with:
  - [ ] `git rebase --onto dedupe-paragraph-ids-mainline "$ABI_PRE_BASE_MAIN"`
- [ ] Record post-rebase values:
  - [ ] `ABI_POST_SHA`
  - [ ] `ABI_POST_BASE_DEDUPE="$(git merge-base HEAD dedupe-paragraph-ids-mainline)"`
  - [ ] `git rev-list --left-right --count dedupe-paragraph-ids-mainline...HEAD`
- [ ] Verify dedupe is ancestor of rebased ABI branch.

## Step 5: Create integration branch from ABI-on-dedupe and cherry-pick assistant stack

### 5a) Integration branch/worktree
- [ ] Define:
  - [ ] `INTEGRATION_BRANCH="system-abi-variadic-anchor-title-preserve-integration-on-dedupe-<timestamp>"`
  - [ ] `INTEGRATION_WT="/home/pete.levasseur/project/fls-system-abi-anchor-title-preserve-integration-<timestamp>"`
- [ ] Create integration branch from `ABI_REBASED_BRANCH`.
- [ ] Record integration base SHA.

### 5b) Resolve assistant commits
- [ ] Build full ordered assistant commit manifest on top of dedupe.
- [ ] Build selected manifest with required commits in order:
  - [ ] assistant introduction commit (`tools/changelog_assistant.py` added),
  - [ ] `fix(changelog-assistant): anchor updates to existing upstream PR entries`,
  - [ ] `ci(changelog-assistant): run coverage checks in pull requests`,
  - [ ] new preserve-title commit from Step 1d,
  - [ ] any prerequisites needed for clean cherry-pick (document rationale).

### 5c) Cherry-pick onto integration branch
- [ ] Cherry-pick selected commits in order in `INTEGRATION_WT`.
- [ ] If conflicts occur, resolve and document in `$REPORT_ROOT/cherry-pick-conflicts.txt`.
- [ ] Record old SHA -> new SHA mapping in `$REPORT_ROOT/integration-stack-manifest.txt`.

## Step 6: Readiness checks in integration branch
- [ ] Confirm `tools/changelog_assistant.py` exists.
- [ ] Confirm help includes:
  - [ ] `--require-anchor`
  - [ ] `--replace-title`
- [ ] Confirm metadata fields are present in code:
  - [ ] `update_action`
  - [ ] `anchored_pr_url`
  - [ ] `anchored_entry_line`
  - [ ] `anchored_entry_index`
- [ ] Confirm compilation:
  - [ ] `uv run python -m py_compile tools/changelog_assistant.py`
- [ ] Write readiness summary to `$REPORT_ROOT/readiness.txt`.

## Step 7: Validation setup in integration worktree
- [ ] Compute and freeze:
  - [ ] `BASE_REF="$(git merge-base HEAD origin/main)"`
- [ ] Use exact `BASE_REF` for all assistant invocations.
- [ ] Resolve release from `version.rst`.
- [ ] Define titles for explicit behavior testing:
  - [ ] `ORIGINAL_TITLE_EXPECTED="Stabilize declaration of C-style variadic functions for the system ABI"`
  - [ ] `ALT_TITLE="Anchor replace validation title override probe"`

## Step 8: Execute verification sequence

### 8a) Baseline evidence
- [ ] Record canonical entry count and line numbers before updates.
- [ ] Record canonical first-line text before updates.
- [ ] Expected baseline count: `1`.

### 8b) Pre-check
- [ ] Run `--check` with `--base "$BASE_REF"` and emit report.
- [ ] Capture exit code and artifacts (`pre-check.json`, `pre-check.md`).

### 8c) Canonical update, preserve-default behavior
- [ ] Run `--update --upstream-pr "$CANONICAL_UPSTREAM_PR" --title "$ALT_TITLE"` (without `--replace-title`).
- [ ] Expect:
  - [ ] exit `0`,
  - [ ] `update_action="replace"`,
  - [ ] canonical first-line title remains unchanged (`ORIGINAL_TITLE_EXPECTED`),
  - [ ] canonical count remains `1`.
- [ ] Save diff and line-count evidence.

### 8d) Restore baseline changelog state
- [ ] Restore `src/changelog.rst` to pre-step-8c state for isolated follow-up checks.

### 8e) Canonical update, explicit replace-title behavior
- [ ] Run `--update --upstream-pr "$CANONICAL_UPSTREAM_PR" --title "$ALT_TITLE" --replace-title`.
- [ ] Expect:
  - [ ] exit `0`,
  - [ ] `update_action="replace"`,
  - [ ] canonical first-line title changes to `ALT_TITLE`,
  - [ ] canonical count remains `1`.
- [ ] Save diff and line-count evidence.

### 8f) Idempotence with `--replace-title`
- [ ] Re-run exact step 8e command.
- [ ] Expect exit `0` and canonical count still `1`.
- [ ] Save second-run diff and compare for stability.

### 8g) Missing-anchor behavior (strict first, then default)
- [ ] Strict miss first:
  - [ ] run update with `--upstream-pr "$MISSING_UPSTREAM_PR" --require-anchor`
  - [ ] expect non-zero exit and explicit anchor-miss error
- [ ] Default miss second:
  - [ ] run update with `--upstream-pr "$MISSING_UPSTREAM_PR"` (no strict)
  - [ ] expect exit `0`
  - [ ] expect `update_action="append"`

### 8h) Post-check
- [ ] Run `--check --base "$BASE_REF"` and emit report.
- [ ] Capture exit code and artifacts (`post-check.json`, `post-check.md`).

## Step 9: Final summary report
- [ ] Write `$REPORT_ROOT/summary.md` with:
  - [ ] bootstrap pass/fail,
  - [ ] branch topology and SHAs,
  - [ ] assistant and ABI rebase evidence,
  - [ ] cherry-pick manifest results,
  - [ ] command exit table,
  - [ ] preserve-default vs replace-title outcomes,
  - [ ] canonical/missing-anchor verdicts,
  - [ ] pre-check vs post-check outcomes,
  - [ ] acceptance criteria verdicts,
  - [ ] remediation notes for any failures.

## Session response checklist
- [ ] Return checklist completion status by section.
- [ ] Return exact branch names and SHAs for:
  - [ ] `ANCHOR_REBASED_BRANCH`
  - [ ] `ABI_REBASED_BRANCH`
  - [ ] `INTEGRATION_BRANCH`
- [ ] Return integration worktree path and active branch.
- [ ] Return cherry-pick mapping (`old SHA -> new SHA`).
- [ ] Return command summary with exit codes.
- [ ] Return exact artifact paths under `REPORT_ROOT`.
- [ ] Return title behavior verdicts:
  - [ ] anchor-hit default preserves title,
  - [ ] anchor-hit + `--replace-title` replaces title.
- [ ] Return anchor behavior verdicts:
  - [ ] canonical URL => `replace`,
  - [ ] missing URL default => `append`,
  - [ ] missing URL strict => non-zero.
- [ ] Return post-check pass/fail and blockers.

## Acceptance criteria
- [ ] On anchor-hit update without `--replace-title`, existing top-level entry title is preserved.
- [ ] On anchor-hit update with `--replace-title`, top-level entry title is replaced with provided title.
- [ ] Canonical URL update continues to report `update_action="replace"`.
- [ ] Canonical URL top-level entry count remains exactly `1` across baseline and reruns.
- [ ] Missing URL behavior is validated (`append` default, strict non-zero).
- [ ] Both derived `*-on-dedupe` branches have dedupe as ancestor.
- [ ] Integration branch is based on ABI-on-dedupe and contains selected assistant commits in order.
- [ ] Final artifacts are sufficient for review in a fresh session.
