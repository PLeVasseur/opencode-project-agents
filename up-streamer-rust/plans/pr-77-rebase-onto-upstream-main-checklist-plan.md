# PR 77 Rebase Onto `upstream/main` (Hardened Checklist Plan)

## Objective

Rebase PR branch `bugfix/issue-74-left-topic-authority` (PR #77) onto latest `upstream/main`, drop commits already represented on `main`, preserve only issue-74-relevant unique commits, and update the PR branch safely.

## New-session assumptions

- [ ] Treat this as a fresh session: do not assume exported variables, remote names, or local branch state.
- [ ] Run all checks in order; hard-fail on violated invariants before rewriting history.

## Current known context (already confirmed)

- [x] PR: `https://github.com/eclipse-uprotocol/up-streamer-rust/pull/77`
- [x] Current compare status is `diverged` (`ahead_by=34`, `behind_by=2`)
- [x] Many commits overlap with already merged PR #75 and PR #76 work
- [x] Issue-74-focused tail commits are expected to remain unique

## Guardrails

- [ ] Keep a recoverable backup ref before rewriting history.
- [ ] Use non-interactive git operations only (no `-i` workflows).
- [ ] Use `--force-with-lease` (never plain `--force`) when updating the remote PR branch.
- [ ] Hard-fail if working tree is not clean before rebase/cherry-pick.
- [ ] Verify local `HEAD` exactly matches PR `headRefOid` before rewriting.
- [ ] Derive keep-commit set dynamically from `git cherry -v` (do not rely on hardcoded SHA list).

## Phase 1: Session bootstrap and invariant checks

- [x] `printenv OPENCODE_CONFIG_DIR`
- [x] `test -n "$OPENCODE_CONFIG_DIR"`
- [x] `mkdir -p "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase"`
- [x] Export plan/session constants:
  - [x] `export PR_NUMBER=77`
  - [x] `export BASE_REPO="eclipse-uprotocol/up-streamer-rust"`
  - [x] `export PR_BRANCH="bugfix/issue-74-left-topic-authority"`
- [x] Pull PR metadata for later checks:
  - [x] `export PR_HEAD_OID="$(gh pr view "$PR_NUMBER" --repo "$BASE_REPO" --json headRefOid --jq .headRefOid)"`
  - [x] `export PR_HEAD_OWNER="$(gh pr view "$PR_NUMBER" --repo "$BASE_REPO" --json headRepositoryOwner --jq .headRepositoryOwner.login)"`
- [x] `gh pr checkout "$PR_NUMBER" --repo "$BASE_REPO"`
- [x] `test "$(git rev-parse --abbrev-ref HEAD)" = "$PR_BRANCH"`
- [x] Ensure no in-progress rebase state:
  - [x] `test ! -d .git/rebase-apply`
  - [x] `test ! -d .git/rebase-merge`
- [x] Hard-fail dirty tree check:
  - [x] `test -z "$(git status --porcelain)"`
- [x] `git status --short --branch`
- [x] `git remote -v`
- [x] Resolve and verify upstream remote:
  - [x] `export UPSTREAM_REMOTE="upstream"` (or discovered equivalent)
  - [x] `git remote get-url "$UPSTREAM_REMOTE" | rg 'eclipse-uprotocol/up-streamer-rust(\.git)?$'`
- [x] Resolve and verify fork remote:
  - [x] `export FORK_REMOTE="origin"` (or discovered equivalent)
  - [x] `git remote get-url "$FORK_REMOTE" | rg "$PR_HEAD_OWNER/up-streamer-rust(\.git)?$"`
- [x] `git fetch "$UPSTREAM_REMOTE" --prune`
- [x] `git fetch "$FORK_REMOTE" --prune`
- [x] Head SHA sanity check before rewrite:
  - [x] `test "$(git rev-parse HEAD)" = "$PR_HEAD_OID"`

## Phase 2: Safety snapshot and dynamic keep-set derivation

- [x] Create backup pointer before rewrite:
  - [x] `export BACKUP_BRANCH="backup/pr77-pre-rebase-$(date +%Y%m%d-%H%M%S)"`
  - [x] `git branch "$BACKUP_BRANCH"`
  - [x] `git rev-parse --short HEAD`
- [x] Confirm merge base and divergence:
  - [x] `git merge-base HEAD "$UPSTREAM_REMOTE/main"`
  - [x] `gh api "repos/eclipse-uprotocol/up-streamer-rust/compare/main...${PR_HEAD_OWNER}:${PR_BRANCH}" --jq '{status: .status, ahead_by: .ahead_by, behind_by: .behind_by, total_commits: .total_commits}'`
- [x] Confirm patch-equivalent overlap and persist evidence:
  - [x] `git cherry -v "$UPSTREAM_REMOTE/main" HEAD | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/cherry-pre.txt"`
- [x] Derive keep-commit list dynamically from `+` entries:
  - [x] `mapfile -t KEEP_COMMITS < <(git cherry -v "$UPSTREAM_REMOTE/main" HEAD | python3 -c 'import sys; [print(l.split()[1]) for l in sys.stdin if l.startswith("+ ")]')`
  - [x] `printf '%s\n' "${KEEP_COMMITS[@]}" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/keep-commits.txt"`
- [x] Keep-set sanity:
  - [x] `test "${#KEEP_COMMITS[@]}" -gt 0`
  - [ ] If this fails, stop and decide whether PR should be closed as fully absorbed.

## Phase 3: Rebase execution (preferred path)

- [ ] Start rebase:
  - [ ] `git rebase "$UPSTREAM_REMOTE/main"`
- [ ] During rebase stop points:
  - [ ] resolve conflicts minimally and behavior-preserving
  - [ ] `git add <resolved-files>`
  - [ ] `git rebase --continue`
- [ ] Empty/already-upstream commit handling:
  - [ ] `git rebase --skip`
- [ ] After rebase completion:
  - [ ] `git rev-parse --abbrev-ref HEAD`
  - [ ] `git status --short --branch`
  - [ ] `git cherry -v "$UPSTREAM_REMOTE/main" HEAD | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/cherry-post-rebase.txt"`
  - [ ] `! rg '^-' "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/cherry-post-rebase.txt"`
  - [ ] `git range-diff "$UPSTREAM_REMOTE/main...$BACKUP_BRANCH" "$UPSTREAM_REMOTE/main...HEAD" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/range-diff.txt"`

## Phase 3 fallback: Rebuild branch from keep-set (if preferred path is noisy/high-risk)

- [ ] Abort partial rebase safely (if active):
  - [ ] `git rebase --abort || true`
- [ ] Recreate target branch on latest base (backup already retained):
  - [ ] `git checkout -B "$PR_BRANCH" "$UPSTREAM_REMOTE/main"`
- [ ] Recompute keep-set from backup branch:
  - [ ] `mapfile -t KEEP_COMMITS < <(git cherry -v "$UPSTREAM_REMOTE/main" "$BACKUP_BRANCH" | python3 -c 'import sys; [print(l.split()[1]) for l in sys.stdin if l.startswith("+ ")]')`
  - [ ] `test "${#KEEP_COMMITS[@]}" -gt 0`
- [ ] Cherry-pick keep commits only:
  - [ ] `git cherry-pick "${KEEP_COMMITS[@]}"`
- [ ] Post-fallback duplicate proof:
  - [ ] `git cherry -v "$UPSTREAM_REMOTE/main" HEAD | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/cherry-post-fallback.txt"`
  - [ ] `! rg '^-' "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/cherry-post-fallback.txt"`

## Phase 4: Validation after rewrite

- [ ] `git status --short --branch`
- [ ] `git log --oneline --decorate -25`
- [ ] `git diff --stat "$UPSTREAM_REMOTE/main...HEAD"`
- [ ] `source build/envsetup.sh highest`
- [ ] `cargo fmt -- --check`
- [ ] `cargo clippy -p up-streamer --all-targets -- -W warnings -D warnings`
- [ ] `cargo test -p up-streamer routing`
- [ ] `cargo test -p up-streamer ingress_registry`

## Phase 5: Push and PR verification

- [ ] Pre-push invariants:
  - [ ] `test "$(git rev-parse --abbrev-ref HEAD)" = "$PR_BRANCH"`
  - [ ] `test -z "$(git status --porcelain)"`
- [ ] Push rewritten branch safely:
  - [ ] `git push --force-with-lease "$FORK_REMOTE" "HEAD:$PR_BRANCH"`
- [ ] Verify remote branch update:
  - [ ] `git ls-remote --heads "$FORK_REMOTE" "$PR_BRANCH"`
- [ ] Verify PR reflects rewritten history:
  - [ ] `gh pr view "$PR_NUMBER" --repo "$BASE_REPO" --json mergeStateStatus,headRefOid,commits,updatedAt,url`
  - [ ] `gh api "repos/eclipse-uprotocol/up-streamer-rust/compare/main...${PR_HEAD_OWNER}:${PR_BRANCH}" --jq '{status: .status, ahead_by: .ahead_by, behind_by: .behind_by, total_commits: .total_commits}'`
- [ ] Confirm expected outcome:
  - [ ] duplicate already-upstream stack is removed
  - [ ] issue-74 commit stack remains
  - [ ] `behind_by` is `0` (or explain if base advanced during execution)
  - [ ] PR mergeability improved (or blockers clearly captured)

## Deliverables

- [ ] Write execution report to:
  - [ ] `$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/pr-77-rebase-execution-report.md`
- [ ] Report must include:
  - [ ] exact commands run (ordered)
  - [ ] branch/remote invariants used (`UPSTREAM_REMOTE`, `FORK_REMOTE`, `PR_HEAD_OID`)
  - [ ] conflict list and exact resolutions
  - [ ] keep-set used for rewritten branch
  - [ ] validation outputs
  - [ ] final compare stats and PR URL
  - [ ] fallback usage note (if fallback path was used)
