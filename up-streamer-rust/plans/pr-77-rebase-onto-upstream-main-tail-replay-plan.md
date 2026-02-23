# PR 77 Rewrite Recovery Onto `upstream/main` (Tail-Replay Plan)

## Objective

Recover from the currently stuck/noisy rebase attempt for PR branch `bugfix/issue-74-left-topic-authority` by rebuilding the branch from the first non-absorbed commit onward, based on merged PR #75/#76 commit-subject prefix matching, then validating and force-updating the PR branch safely.

## Why this plan replaces the prior checklist

- `git cherry -v` is unreliable here because PR #75/#76 were squash-merged into `upstream/main`.
- Direct replay of the full stack is already in a conflicted in-progress rebase state.
- Safer approach: detect absorbed prefix from merged PR commit subjects, then replay only the remaining issue-74 tail commits onto latest `upstream/main`.

## Execution rules

- [x] Manual execution only; no autopilot/orchestration.
- [x] Non-interactive git commands only (no `-i` flows).
- [x] Hard-fail immediately on invariant violations.
- [x] Use `--force-with-lease` only for remote rewrite push.
- [x] Keep artifacts under `$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/`.
- [x] Update this plan in-place as you execute (`[ ]` -> `[x]`).

## Hard-fail invariants

- [x] Working tree must be clean before rewrite starts.
- [x] Upstream/fork remotes must match expected repos.
- [x] Local `HEAD` must match PR `headRefOid` after rebase-abort recovery.
- [x] Derived keep-set must be non-empty.
- [x] Derived keep-set must be a strict tail subset (absorbed prefix length > 0).

## Phase 1: Session bootstrap and rebase-state recovery

- [x] `printenv OPENCODE_CONFIG_DIR`
- [x] `test -n "$OPENCODE_CONFIG_DIR"`
- [x] `mkdir -p "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase"`
- [x] Export session constants:
  - [x] `export PR_NUMBER=77`
  - [x] `export BASE_REPO="eclipse-uprotocol/up-streamer-rust"`
  - [x] `export PR_BRANCH="bugfix/issue-74-left-topic-authority"`
  - [x] `export ABSORBED_PRS="75 76"`
- [x] Pull PR metadata:
  - [x] `export PR_HEAD_OID="$(gh pr view "$PR_NUMBER" --repo "$BASE_REPO" --json headRefOid --jq .headRefOid)"`
  - [x] `export PR_HEAD_OWNER="$(gh pr view "$PR_NUMBER" --repo "$BASE_REPO" --json headRepositoryOwner --jq .headRepositoryOwner.login)"`
- [x] Capture pre-recovery state (for report evidence):
  - [x] `git status --branch --short | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/pre-recovery-status.txt"`
  - [x] `git rev-parse --abbrev-ref HEAD | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/pre-recovery-head-name.txt"`
  - [x] `git rev-parse HEAD | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/pre-recovery-head-sha.txt"`
- [x] If rebase state exists, abort it:
  - [x] `if [ -d .git/rebase-apply ] || [ -d .git/rebase-merge ]; then git rebase --abort; fi`
  - [x] `test ! -d .git/rebase-apply`
  - [x] `test ! -d .git/rebase-merge`
- [x] Checkout PR branch cleanly:
  - [x] `gh pr checkout "$PR_NUMBER" --repo "$BASE_REPO"`
  - [x] `test "$(git rev-parse --abbrev-ref HEAD)" = "$PR_BRANCH"`
- [x] Resolve and verify remotes:
  - [x] `export UPSTREAM_REMOTE="upstream"`
  - [x] `export FORK_REMOTE="origin"`
  - [x] `git remote get-url "$UPSTREAM_REMOTE" | rg 'eclipse-uprotocol/up-streamer-rust(\.git)?$'`
  - [x] `git remote get-url "$FORK_REMOTE" | rg "$PR_HEAD_OWNER/up-streamer-rust(\.git)?$"`
- [x] Refresh refs:
  - [x] `git fetch "$UPSTREAM_REMOTE" --prune`
  - [x] `git fetch "$FORK_REMOTE" --prune`
- [x] Hard-fail cleanliness + head SHA check before rewrite:
  - [x] `test -z "$(git status --porcelain)"`
  - [x] `test "$(git rev-parse HEAD)" = "$PR_HEAD_OID"`

## Phase 2: Safety snapshot and absorbed-prefix derivation

- [x] Create backup pointer before any rewrite:
  - [x] `export BACKUP_BRANCH="backup/pr77-pre-tail-replay-$(date +%Y%m%d-%H%M%S)"`
  - [x] `git branch "$BACKUP_BRANCH"`
  - [x] `git rev-parse "$BACKUP_BRANCH" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/backup-branch-sha.txt"`
- [x] Capture branch stack and absorbed PR commit subjects:
  - [x] `git log --reverse --pretty='%H%x09%s' "$UPSTREAM_REMOTE/main..$PR_BRANCH" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/branch-stack.txt"`
  - [x] `for pr in $ABSORBED_PRS; do gh pr view "$pr" --repo "$BASE_REPO" --json commits --jq '.commits[].messageHeadline'; done | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/absorbed-subjects.txt"`
- [x] Derive prefix-match boundary and persist evidence:
  - [x] Run:
    ```bash
    python3 - <<'PY' | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/prefix-match-summary.txt"
    import os
    import subprocess
    import sys

    upstream = os.environ["UPSTREAM_REMOTE"]
    branch = os.environ["PR_BRANCH"]
    repo = os.environ["BASE_REPO"]
    absorbed_prs = os.environ["ABSORBED_PRS"].split()

    branch_lines = subprocess.check_output(
        ["git", "log", "--reverse", "--pretty=%H\t%s", f"{upstream}/main..{branch}"],
        text=True,
    ).splitlines()
    branch_commits = [line.split("\t", 1) for line in branch_lines if "\t" in line]

    absorbed_subjects = []
    for pr in absorbed_prs:
        out = subprocess.check_output(
            ["gh", "pr", "view", pr, "--repo", repo, "--json", "commits", "--jq", ".commits[].messageHeadline"],
            text=True,
        ).splitlines()
        absorbed_subjects.extend(out)

    i = 0
    while i < len(branch_commits) and i < len(absorbed_subjects) and branch_commits[i][1] == absorbed_subjects[i]:
        i += 1

    if not branch_commits:
        sys.exit("Branch has no commits ahead of upstream/main")
    if i == 0:
        sys.exit("Absorbed prefix length is zero; boundary derivation failed")
    if i >= len(branch_commits):
        sys.exit("No remaining tail commits after absorbed-prefix matching")

    keep_start_sha, keep_start_subject = branch_commits[i]
    print(f"matched_prefix={i}")
    print(f"branch_ahead_count={len(branch_commits)}")
    print(f"keep_start_sha={keep_start_sha}")
    print(f"keep_start_subject={keep_start_subject}")
    PY
    ```
- [x] Export keep-start SHA from summary:
  - [x] `export KEEP_START_SHA="$(rg '^keep_start_sha=(.+)$' "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/prefix-match-summary.txt" -or '$1')"`
  - [x] `test -n "$KEEP_START_SHA"`
- [x] Materialize ordered keep-set (tail only):
  - [x] `mapfile -t KEEP_COMMITS < <(git rev-list --reverse "${KEEP_START_SHA}^..$PR_BRANCH")`
  - [x] `printf '%s\n' "${KEEP_COMMITS[@]}" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/keep-commits.txt"`
  - [x] `git log --reverse --oneline "${KEEP_START_SHA}^..$PR_BRANCH" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/keep-commits-oneline.txt"`
- [x] Keep-set sanity:
  - [x] `test "${#KEEP_COMMITS[@]}" -gt 0`
  - [x] `export BRANCH_AHEAD_COUNT="$(git rev-list --count "$UPSTREAM_REMOTE/main..$PR_BRANCH")"`
  - [x] `test "${#KEEP_COMMITS[@]}" -lt "$BRANCH_AHEAD_COUNT"`

## Phase 3: Rewrite branch by replaying tail onto latest base

- [x] Reset PR branch tip to latest `upstream/main` (backup retained):
  - [x] `git checkout -B "$PR_BRANCH" "$UPSTREAM_REMOTE/main"`
- [x] Replay keep commits in order:
  - [x] `git cherry-pick "${KEEP_COMMITS[@]}"`
- [x] If cherry-pick stops (not triggered; replay completed cleanly):
  - [x] resolve conflicts minimally and behavior-preserving (not needed)
  - [x] `git add <resolved-files>` (not needed)
  - [x] `git cherry-pick --continue` (not needed)
  - [x] if commit becomes empty: `git cherry-pick --skip` (not needed)
- [x] Post-rewrite duplicate-proof and mapping evidence:
  - [x] `git rev-parse --abbrev-ref HEAD`
  - [x] `git status --short --branch`
  - [x] `git cherry -v "$UPSTREAM_REMOTE/main" HEAD | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/cherry-post-rewrite.txt"`
  - [x] `! rg '^-' "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/cherry-post-rewrite.txt"`
  - [x] `git range-diff "$UPSTREAM_REMOTE/main...$BACKUP_BRANCH" "$UPSTREAM_REMOTE/main...HEAD" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/range-diff.txt"`

## Phase 4: Validation after rewrite (run exactly)

- [x] `git status --short --branch`
- [x] `git log --oneline --decorate -25`
- [x] `git diff --stat "$UPSTREAM_REMOTE/main...HEAD"`
- [x] `source build/envsetup.sh highest`
- [x] `cargo fmt -- --check`
- [x] `cargo clippy -p up-streamer --all-targets -- -W warnings -D warnings`
- [x] `cargo test -p up-streamer routing`
- [x] `cargo test -p up-streamer ingress_registry`

## Phase 5: Push and PR verification

- [x] Pre-push invariants:
  - [x] `test "$(git rev-parse --abbrev-ref HEAD)" = "$PR_BRANCH"`
  - [x] `test -z "$(git status --porcelain)"`
- [x] Push rewritten branch safely:
  - [x] `git push --force-with-lease "$FORK_REMOTE" "HEAD:$PR_BRANCH"`
- [x] Verify remote branch update:
  - [x] `git ls-remote --heads "$FORK_REMOTE" "$PR_BRANCH"`
- [x] Verify PR update and compare stats:
  - [x] `gh pr view "$PR_NUMBER" --repo "$BASE_REPO" --json mergeStateStatus,headRefOid,commits,updatedAt,url`
  - [x] `gh api "repos/eclipse-uprotocol/up-streamer-rust/compare/main...${PR_HEAD_OWNER}:${PR_BRANCH}" --jq '{status: .status, ahead_by: .ahead_by, behind_by: .behind_by, total_commits: .total_commits}'`
- [x] Confirm expected outcome:
  - [x] absorbed PR #75/#76 stack removed from PR #77 branch history
  - [x] issue-74 tail stack preserved
  - [x] `behind_by` is `0` (or explain if base advanced mid-run)
  - [x] mergeability improved (or blockers captured)

## Deliverables

- [x] Write execution report to:
  - [x] `$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/pr-77-rebase-execution-report.md`
- [x] Report must include:
  - [x] exact commands run in order
  - [x] invariants and resolved values (`UPSTREAM_REMOTE`, `FORK_REMOTE`, `PR_HEAD_OID`, `BACKUP_BRANCH`)
  - [x] absorbed-prefix derivation output and keep-set used
  - [x] conflict list and exact resolutions (if any)
  - [x] validation command outcomes
  - [x] final PR URL and compare stats (`ahead_by`, `behind_by`, `total_commits`)
