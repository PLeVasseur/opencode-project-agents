# Sync `origin/main` to `upstream/main` (Fresh-Session Hardened Plan)

Goal: update your fork's `main` to exactly match `upstream/main` so fork PRs are based on the same base commit and do not include upstream-only commits.

## Phase 0: Fresh-Session Bootstrap and Hard Invariants

- [x] Confirm repository and clean execution state.
  - [x] `git rev-parse --is-inside-work-tree`
  - [x] `test ! -d .git/rebase-apply && test ! -d .git/rebase-merge`
  - [x] `test -z "$(git status --porcelain)"`
- [x] Capture starting context for safe return.
  - [x] `START_BRANCH="$(git rev-parse --abbrev-ref HEAD)"`
  - [x] `START_HEAD_SHA="$(git rev-parse HEAD)"`
- [x] Verify remotes are correct before any push.
  - [x] `git remote get-url origin` points to your fork (`PLeVasseur/up-streamer-rust`)
  - [x] `git remote get-url upstream` points to canonical repo (`eclipse-uprotocol/up-streamer-rust`)

## Phase 1: Fetch and Classify Relationship (No Changes Yet)

- [x] Refresh refs.
  - [x] `git fetch origin upstream --prune`
- [x] Capture baseline SHAs.
  - [x] `ORIGIN_MAIN_SHA="$(git rev-parse origin/main)"`
  - [x] `UPSTREAM_MAIN_SHA="$(git rev-parse upstream/main)"`
  - [x] `MERGE_BASE_SHA="$(git merge-base origin/main upstream/main)"`
  - [x] `AHEAD_COUNT="$(git rev-list --count origin/main..upstream/main)"`
- [x] Choose safe path based on ancestry.
  - [ ] If `ORIGIN_MAIN_SHA == UPSTREAM_MAIN_SHA`: stop (already synced; nothing to do).
  - [x] If `MERGE_BASE_SHA == ORIGIN_MAIN_SHA`: proceed (fast-forward expected).
  - [ ] If `MERGE_BASE_SHA == UPSTREAM_MAIN_SHA`: stop (`origin/main` ahead; do not rewrite accidentally).
  - [ ] Else: stop (diverged; resolve explicitly before touching `origin/main`).

## Phase 2: Create Durable Rollback Anchor on Fork

- [x] Create pre-sync backup tag from current `origin/main`.
  - [x] `PRE_SYNC_TAG="backup-origin-main-pre-sync-$(date -u +%Y%m%dT%H%M%SZ)"`
  - [x] `git tag "$PRE_SYNC_TAG" "$ORIGIN_MAIN_SHA"`
- [x] Push and verify rollback tag.
  - [x] `git push origin "$PRE_SYNC_TAG"`
  - [x] `git ls-remote --tags origin "$PRE_SYNC_TAG"`

## Phase 3: Race-Guarded Sync of Fork `main` (No Local Branch Rewrite Required)

- [x] Re-fetch immediately before push to detect races.
  - [x] `git fetch origin upstream --prune`
  - [x] `ORIGIN_MAIN_SHA_PRE_PUSH="$(git rev-parse origin/main)"`
  - [x] `UPSTREAM_MAIN_SHA_PRE_PUSH="$(git rev-parse upstream/main)"`
- [x] Re-validate invariants before push.
  - [x] `test "$ORIGIN_MAIN_SHA_PRE_PUSH" = "$ORIGIN_MAIN_SHA"`
  - [x] `test "$UPSTREAM_MAIN_SHA_PRE_PUSH" = "$UPSTREAM_MAIN_SHA"`
  - [x] `test "$(git merge-base origin/main upstream/main)" = "$ORIGIN_MAIN_SHA_PRE_PUSH"`
- [x] Push upstream main commit to fork main.
  - [x] `git push origin upstream/main:main`
  - [ ] If rejected due remote move/non-fast-forward: stop, return to Phase 1, and re-evaluate.

## Phase 4: Verify Sync and PR Shape

- [x] Verify fork `main` now matches upstream.
  - [x] `git fetch origin upstream --prune`
  - [x] `FINAL_ORIGIN_MAIN_SHA="$(git rev-parse origin/main)"`
  - [x] `FINAL_UPSTREAM_MAIN_SHA="$(git rev-parse upstream/main)"`
  - [x] `test "$FINAL_ORIGIN_MAIN_SHA" = "$FINAL_UPSTREAM_MAIN_SHA"`
- [x] Verify fork PR(s) from `cleanup/refactor-upstream-main` to fork `main`.
  - [x] `gh pr list --repo PLeVasseur/up-streamer-rust --head cleanup/refactor-upstream-main --base main --state open --json number,url`
  - [x] Capture PR number from list (if none, record and stop verification here).
  - [x] `gh pr view --repo PLeVasseur/up-streamer-rust <PR_NUMBER> --json commits,baseRefName,headRefName,url`
  - [x] Confirm commit count is exactly `6`.
  - [x] Confirm upstream-only commit (`b6bc245...`) is absent from PR commit list.

## Phase 5: Return Context and Report

- [x] Restore starting branch context.
  - [x] `git switch "$START_BRANCH"`
  - [x] `test "$(git rev-parse --abbrev-ref HEAD)" = "$START_BRANCH"`
- [x] Report final outcomes.
  - [x] Old `origin/main` SHA: `$ORIGIN_MAIN_SHA`
  - [x] New `origin/main` SHA: `$FINAL_ORIGIN_MAIN_SHA`
  - [x] `upstream/main` SHA: `$FINAL_UPSTREAM_MAIN_SHA`
  - [x] Rollback tag: `$PRE_SYNC_TAG` (and remote verification result)
  - [x] Fork PR URL and final commit count

## Phase 6: Recovery Contingency (Only If Needed)

- [ ] If sync result is unacceptable and rollback is required.
  - [ ] `git fetch origin --prune`
  - [ ] `CURRENT_ORIGIN_MAIN_SHA="$(git rev-parse origin/main)"`
  - [ ] `git push --force-with-lease=main:$CURRENT_ORIGIN_MAIN_SHA origin "$PRE_SYNC_TAG:main"`
  - [ ] Verify rollback: `test "$(git rev-parse origin/main)" = "$ORIGIN_MAIN_SHA"`
