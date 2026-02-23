# Plan: Restack tooling changes onto assistant branch, then consume in ABI integration

## Goal
- [ ] Move `tools/changelog_assistant.py` renderer changes off the ABI integration worktree and onto a proper tooling branch.
- [ ] Validate and commit tooling changes on the tooling branch first.
- [ ] Re-apply tooling commit into integration via cherry-pick (no ad-hoc local tool edits in integration).
- [ ] Regenerate the ABI PR `145954` changelog entry using a dedupe-boundary base so dedupe deltas are excluded.

## Branch/worktree model
- [ ] Source assistant tooling base branch: `changelog-assistant-upstream-pr-anchor-title-preserve-on-dedupe`
- [ ] ABI branch (docs source): `system-abi-variadic-on-dedupe`
- [ ] Integration branch (consumes both): `system-abi-variadic-anchor-title-preserve-integration-on-dedupe-<timestamp>`
- [ ] New tooling branch to create:
  - [ ] `TOOLING_BRANCH="changelog-assistant-paragraph-buckets-inline-tags-on-dedupe-<timestamp>"`
  - [ ] `TOOLING_WT="/home/pete.levasseur/project/fls-changelog-assistant-paragraph-buckets-<timestamp>"`

## Scope
- [ ] Tooling file: `tools/changelog_assistant.py`
- [ ] ABI entry target: `https://github.com/rust-lang/rust/pull/145954`
- [ ] Missing-anchor probe: `https://github.com/rust-lang/rust/pull/999999`
- [ ] No push unless explicitly requested.

## Safety / hygiene
- [ ] Do not rewrite published history.
- [ ] Do not force-push.
- [ ] Preserve unrelated local edits in other worktrees.
- [ ] Keep report artifacts under `$OPENCODE_CONFIG_DIR/reports/`.

## Required artifacts
- [ ] Timestamped report root with command ledger and per-command stdout/stderr/exitcode.
- [ ] Patch evidence showing tooling diff moved from integration WT to tooling WT.
- [ ] Tooling commit SHA and message.
- [ ] Cherry-pick mapping into integration (`old -> new`).
- [ ] Final ABI entry evidence generated with dedupe-boundary base.
- [ ] Final summary report with pass/fail checklist.

## Step 0: Bootstrap
- [ ] `printenv OPENCODE_CONFIG_DIR`
- [ ] `git fetch origin`
- [ ] `uv sync`
- [ ] Create `REPORT_ROOT="$OPENCODE_CONFIG_DIR/reports/system-abi-variadic-tooling-restack-<timestamp>"`
- [ ] Initialize command ledger and capture bootstrap metadata (branch/HEAD/base SHAs/worktree paths).

## Step 1: Capture current integration dirty state (before restack)
- [ ] In integration WT, capture:
  - [ ] `git status --short --branch`
  - [ ] `git diff -- tools/changelog_assistant.py`
  - [ ] `git diff -- src/changelog.rst`
- [ ] Save a reversible copy of current changelog and tooling files under `REPORT_ROOT`.
- [ ] Save a transport patch for tooling edits (choose one):
  - [ ] `git diff -- tools/changelog_assistant.py > "$REPORT_ROOT/tooling.patch"`
  - [ ] or equivalent safe patch capture.

## Step 2: Create dedicated tooling branch/worktree
- [ ] Create new worktree from `changelog-assistant-upstream-pr-anchor-title-preserve-on-dedupe`:
  - [ ] `git worktree add -b "$TOOLING_BRANCH" "$TOOLING_WT" changelog-assistant-upstream-pr-anchor-title-preserve-on-dedupe`
- [ ] Verify clean status in tooling WT.

## Step 3: Apply tooling change in tooling WT
- [ ] Apply captured tooling patch into `TOOLING_WT`.
- [ ] Confirm only expected tooling files changed (`tools/changelog_assistant.py`, plus any intentional test/docs updates).
- [ ] Confirm paragraph-bucket rendering behavior present:
  - [ ] sections are `Added paragraphs` / `Removed paragraphs` / `Changed paragraphs`
  - [ ] changed paragraph lines include inline tags
  - [ ] legacy detail sections are not emitted

## Step 4: Tooling branch validation
- [ ] `uv run python -m py_compile tools/changelog_assistant.py`
- [ ] `uv run python tools/changelog_assistant.py --help`
- [ ] `uv run python tools/changelog_tag_verifier.py --mode compare --report-dir <repo-relative-report-dir>`
- [ ] `uv run python tools/changelog_tag_verifier.py --mode extract --report-dir <repo-relative-report-dir>`
- [ ] Behavior checks on tooling WT:
  - [ ] canonical default anchor-hit preserves title
  - [ ] canonical `--replace-title` replaces title
  - [ ] strict missing anchor is non-zero
  - [ ] default missing anchor appends and exits zero
- [ ] Structure assertions for generated `145954` entry:
  - [ ] only paragraph bucket section headers present
  - [ ] changed lines have inline tags
  - [ ] added/removed lines have no inline tags
  - [ ] no duplicate paragraph IDs per category

## Step 5: Commit tooling changes on tooling branch
- [ ] Stage intended files only.
- [ ] Commit using Conventional Commit, e.g.:
  - [ ] `refactor(changelog-assistant): render paragraph lifecycle buckets with inline changed tags`
- [ ] Record tooling commit SHA (`TOOLING_COMMIT_SHA`).

## Step 6: Clean integration WT of ad-hoc tooling edits
- [ ] In integration WT, remove local tool edits by restoring tooling file from HEAD:
  - [ ] `git restore tools/changelog_assistant.py`
- [ ] Keep/churn `src/changelog.rst` as needed for regeneration (do not lose intentional entry state evidence).
- [ ] Verify integration WT status after cleanup.

## Step 7: Cherry-pick tooling commit into integration branch
- [ ] Cherry-pick `TOOLING_COMMIT_SHA` onto integration branch.
- [ ] If conflicts occur, resolve and capture conflict notes.
- [ ] Record mapping in report:
  - [ ] `TOOLING_COMMIT_SHA -> INTEGRATION_TOOLING_SHA`

## Step 8: Regenerate ABI entry using dedupe-boundary base
- [ ] Compute base at dedupe boundary:
  - [ ] `ABI_BASE_REF="$(git merge-base HEAD dedupe-paragraph-ids-mainline)"`
- [ ] Regenerate `145954` entry with:
  - [ ] `--base "$ABI_BASE_REF"`
  - [ ] canonical upstream URL
  - [ ] title preserved default path
- [ ] Validate result excludes dedupe-only spillover:
  - [ ] compare old vs new report JSON counts
  - [ ] verify removed dedupe-linked IDs no longer appear in ABI entry

## Step 9: Post-restack verification in integration WT
- [ ] `git status --short --branch`
- [ ] Confirm integration branch now contains tooling change via commit history (not local-only edit).
- [ ] Confirm ABI entry at `src/changelog.rst` has:
  - [ ] preserved canonical title (default path)
  - [ ] paragraph buckets + inline changed tags
  - [ ] change set computed from dedupe boundary base

## Step 10: Reporting / handoff
- [ ] Write `summary.md` under `REPORT_ROOT` including:
  - [ ] bootstrap results
  - [ ] tooling branch/worktree details
  - [ ] tooling commit SHA + message
  - [ ] cherry-pick mapping
  - [ ] dedupe-boundary base SHA used for ABI generation
  - [ ] before/after change counts for `145954`
  - [ ] final integration WT status and branch
  - [ ] explicit note that no push was performed

## Acceptance criteria
- [ ] Tooling refactor is committed on dedicated tooling branch (not only local in integration WT).
- [ ] Integration consumes tooling via cherry-pick commit.
- [ ] ABI `145954` entry is generated using dedupe-boundary base.
- [ ] Dedupe-only changes are excluded from ABI changelog item.
- [ ] Entry format uses paragraph lifecycle buckets and inline tags for changed paragraphs only.
- [ ] Validation and report artifacts are complete for fresh-session review.
