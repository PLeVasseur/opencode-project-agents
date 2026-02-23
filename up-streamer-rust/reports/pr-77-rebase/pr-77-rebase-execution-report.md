# PR 77 Rebase Recovery Execution Report (Tail Replay)

Date: 2026-02-11

## Outcome

- Recovered from in-progress conflicted rebase state on `bugfix/issue-74-left-topic-authority`.
- Rewrote PR #77 by resetting to `upstream/main` and replaying only the derived keep-tail commits.
- Force-updated fork branch with `--force-with-lease`.
- Verified compare stats after push: `ahead_by=10`, `behind_by=0`, `total_commits=10`.

## Exact Commands Run (In Order)

1. `printenv OPENCODE_CONFIG_DIR`
2. `test -n "$OPENCODE_CONFIG_DIR"`
3. `ls "$OPENCODE_CONFIG_DIR"`
4. `mkdir -p "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase"`
5. `export PR_NUMBER=77`
6. `export BASE_REPO="eclipse-uprotocol/up-streamer-rust"`
7. `export PR_BRANCH="bugfix/issue-74-left-topic-authority"`
8. `export ABSORBED_PRS="75 76"`
9. `export PR_HEAD_OID="$(gh pr view "$PR_NUMBER" --repo "$BASE_REPO" --json headRefOid --jq .headRefOid)"` (failed because shell-local exports did not persist across calls)
10. `printenv PR_NUMBER`
11. `set -euo pipefail && export PR_NUMBER=77 && export BASE_REPO="eclipse-uprotocol/up-streamer-rust" && export PR_BRANCH="bugfix/issue-74-left-topic-authority" && export ABSORBED_PRS="75 76" && export PR_HEAD_OID="$(gh pr view "$PR_NUMBER" --repo "$BASE_REPO" --json headRefOid --jq .headRefOid)" && export PR_HEAD_OWNER="$(gh pr view "$PR_NUMBER" --repo "$BASE_REPO" --json headRepositoryOwner --jq .headRepositoryOwner.login)" && printf '%s\n' "$PR_HEAD_OID" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/pr-head-oid.txt" && printf '%s\n' "$PR_HEAD_OWNER" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/pr-head-owner.txt" && git status --branch --short | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/pre-recovery-status.txt" && git rev-parse --abbrev-ref HEAD | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/pre-recovery-head-name.txt" && git rev-parse HEAD | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/pre-recovery-head-sha.txt" && if [ -d .git/rebase-apply ] || [ -d .git/rebase-merge ]; then git rebase --abort; fi && test ! -d .git/rebase-apply && test ! -d .git/rebase-merge && gh pr checkout "$PR_NUMBER" --repo "$BASE_REPO" && test "$(git rev-parse --abbrev-ref HEAD)" = "$PR_BRANCH" && export UPSTREAM_REMOTE="upstream" && export FORK_REMOTE="origin" && printf '%s\n' "$UPSTREAM_REMOTE" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/upstream-remote.txt" && printf '%s\n' "$FORK_REMOTE" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/fork-remote.txt" && git remote get-url "$UPSTREAM_REMOTE" | rg 'eclipse-uprotocol/up-streamer-rust(\.git)?$' && git remote get-url "$FORK_REMOTE" | rg "$PR_HEAD_OWNER/up-streamer-rust(\.git)?$" && git fetch "$UPSTREAM_REMOTE" --prune && git fetch "$FORK_REMOTE" --prune && test -z "$(git status --porcelain)" && test "$(git rev-parse HEAD)" = "$PR_HEAD_OID"`
12. `set -euo pipefail && export PR_NUMBER=77 && export BASE_REPO="eclipse-uprotocol/up-streamer-rust" && export PR_BRANCH="bugfix/issue-74-left-topic-authority" && export ABSORBED_PRS="75 76" && export UPSTREAM_REMOTE="upstream" && export BACKUP_BRANCH="backup/pr77-pre-tail-replay-$(date +%Y%m%d-%H%M%S)" && git branch "$BACKUP_BRANCH" && printf '%s\n' "$BACKUP_BRANCH" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/backup-branch-name.txt" && git rev-parse "$BACKUP_BRANCH" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/backup-branch-sha.txt" && git log --reverse --pretty='%H%x09%s' "$UPSTREAM_REMOTE/main..$PR_BRANCH" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/branch-stack.txt" && for pr in $ABSORBED_PRS; do gh pr view "$pr" --repo "$BASE_REPO" --json commits --jq '.commits[].messageHeadline'; done | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/absorbed-subjects.txt" && python3 - <<'PY' | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/prefix-match-summary.txt"
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
export KEEP_START_SHA="$(rg '^keep_start_sha=(.+)$' "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/prefix-match-summary.txt" -or '$1')" && test -n "$KEEP_START_SHA" && printf '%s\n' "$KEEP_START_SHA" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/keep-start-sha.txt" && mapfile -t KEEP_COMMITS < <(git rev-list --reverse "${KEEP_START_SHA}^..$PR_BRANCH") && printf '%s\n' "${KEEP_COMMITS[@]}" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/keep-commits.txt" && git log --reverse --oneline "${KEEP_START_SHA}^..$PR_BRANCH" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/keep-commits-oneline.txt" && test "${#KEEP_COMMITS[@]}" -gt 0 && export BRANCH_AHEAD_COUNT="$(git rev-list --count "$UPSTREAM_REMOTE/main..$PR_BRANCH")" && printf '%s\n' "$BRANCH_AHEAD_COUNT" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/branch-ahead-count.txt" && printf '%s\n' "${#KEEP_COMMITS[@]}" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/keep-commit-count.txt" && test "${#KEEP_COMMITS[@]}" -lt "$BRANCH_AHEAD_COUNT"`
13. `set -euo pipefail && export PR_BRANCH="bugfix/issue-74-left-topic-authority" && export UPSTREAM_REMOTE="upstream" && mapfile -t KEEP_COMMITS < "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/keep-commits.txt" && git checkout -B "$PR_BRANCH" "$UPSTREAM_REMOTE/main" && git cherry-pick "${KEEP_COMMITS[@]}"`
14. `set -euo pipefail && export UPSTREAM_REMOTE="upstream" && read -r BACKUP_BRANCH < "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/backup-branch-name.txt" && git rev-parse --abbrev-ref HEAD && git status --short --branch && git cherry -v "$UPSTREAM_REMOTE/main" HEAD | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/cherry-post-rewrite.txt" && ! rg '^-' "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/cherry-post-rewrite.txt" && git range-diff "$UPSTREAM_REMOTE/main...$BACKUP_BRANCH" "$UPSTREAM_REMOTE/main...HEAD" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/range-diff.txt"`
15. `set +e && export UPSTREAM_REMOTE="upstream" && git status --short --branch ; s1=$? ; git log --oneline --decorate -25 ; s2=$? ; git diff --stat "$UPSTREAM_REMOTE/main...HEAD" ; s3=$? ; source build/envsetup.sh highest ; s4=$? ; cargo fmt -- --check ; s5=$? ; cargo clippy -p up-streamer --all-targets -- -W warnings -D warnings ; s6=$? ; cargo test -p up-streamer routing ; s7=$? ; cargo test -p up-streamer ingress_registry ; s8=$? ; printf 'git_status=%s\ngit_log=%s\ngit_diff_stat=%s\nsource_envsetup=%s\ncargo_fmt=%s\ncargo_clippy=%s\ncargo_test_routing=%s\ncargo_test_ingress_registry=%s\n' "$s1" "$s2" "$s3" "$s4" "$s5" "$s6" "$s7" "$s8" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/phase4-statuses.txt" ; test "$s1" -eq 0 -a "$s2" -eq 0 -a "$s3" -eq 0 -a "$s4" -eq 0 -a "$s5" -eq 0 -a "$s6" -eq 0 -a "$s7" -eq 0 -a "$s8" -eq 0`
16. `set -euo pipefail && export PR_NUMBER=77 && export BASE_REPO="eclipse-uprotocol/up-streamer-rust" && export PR_BRANCH="bugfix/issue-74-left-topic-authority" && export FORK_REMOTE="origin" && read -r PR_HEAD_OWNER < "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/pr-head-owner.txt" && test "$(git rev-parse --abbrev-ref HEAD)" = "$PR_BRANCH" && test -z "$(git status --porcelain)" && git push --force-with-lease "$FORK_REMOTE" "HEAD:$PR_BRANCH" && git ls-remote --heads "$FORK_REMOTE" "$PR_BRANCH" | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/post-push-ls-remote.txt" && gh pr view "$PR_NUMBER" --repo "$BASE_REPO" --json mergeStateStatus,headRefOid,commits,updatedAt,url | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/post-push-pr-view.json" && gh api "repos/eclipse-uprotocol/up-streamer-rust/compare/main...${PR_HEAD_OWNER}:${PR_BRANCH}" --jq '{status: .status, ahead_by: .ahead_by, behind_by: .behind_by, total_commits: .total_commits}' | tee "$OPENCODE_CONFIG_DIR/reports/pr-77-rebase/post-push-compare-stats.json"`

## Invariants and Resolved Values

- `UPSTREAM_REMOTE=upstream`
- `FORK_REMOTE=origin`
- `PR_HEAD_OID=42d5a26136fd4f71ea873b7e414f8f6fdd9f17a8`
- `BACKUP_BRANCH=backup/pr77-pre-tail-replay-20260211-104410`
- Upstream URL matched expected: `git@github.com:eclipse-uprotocol/up-streamer-rust.git`
- Fork URL matched expected owner: `git@github.com:PLeVasseur/up-streamer-rust.git`
- Clean-tree invariant before rewrite: pass (`test -z "$(git status --porcelain)"`)
- HEAD/PR SHA invariant before rewrite: pass (`HEAD == PR_HEAD_OID`)

## Absorbed-Prefix Derivation and Keep Set

From `prefix-match-summary.txt`:

- `matched_prefix=24`
- `branch_ahead_count=34`
- `keep_start_sha=0d441dc48eba8fb84a71560a02138a5f22d9efb3`
- `keep_start_subject=add shared CLI parsing helpers for example binaries`

Keep-set materialization:

- Keep commit count: `10`
- Strict-tail subset check: pass (`10 < 34`)
- Non-empty keep-set check: pass (`10 > 0`)
- Ordered keep commits used:
  - `0d441dc add shared CLI parsing helpers for example binaries`
  - `b134d5a parameterize MQTT and Zenoh pubsub binaries`
  - `08b3c0e parameterize remaining example binaries for CLI overrides`
  - `c026489 fix publish forwarding authority matching in streamer`
  - `c51bfc8 document issue74 runbook and CLI override usage`
  - `a553a37 fix integration harness listener unregister symmetry`
  - `f470b22 chore: remove issue-74 mentions from docs and tests`
  - `8ca9785 update listener registration to merge wildcard subscribers and dedupe publish keys`
  - `e8fa62a fix add_forwarding_rule rollback on listener setup failure`
  - `42d5a26 add regression tests for wildcard routing, dedupe safety, rollback, and Path A cache identity`

## Conflict Summary and Resolutions

- Pre-recovery state had an in-progress rebase (`HEAD (no branch)` and `UU .github/workflows/bundled-lint-and-test.yaml`).
- Rebase state was aborted successfully (`git rebase --abort`).
- Tail replay cherry-pick completed without conflicts and without empty commits.
- No conflict resolutions were required during replay.

## Post-Rewrite Duplicate-Proof and Mapping

- `git cherry -v upstream/main HEAD` output contained only `+` lines (no `-` lines).
- Duplicate-proof check passed via `! rg '^-'` on `cherry-post-rewrite.txt`.
- `git range-diff upstream/main...$BACKUP_BRANCH upstream/main...HEAD` showed absorbed-prefix commits dropped and keep-tail commits retained as equivalent patches.

## Phase 4 Validation Outcomes

All listed commands ran and exited `0`:

- `git status --short --branch`
- `git log --oneline --decorate -25`
- `git diff --stat "$UPSTREAM_REMOTE/main...HEAD"`
- `source build/envsetup.sh highest`
- `cargo fmt -- --check`
- `cargo clippy -p up-streamer --all-targets -- -W warnings -D warnings`
- `cargo test -p up-streamer routing`
- `cargo test -p up-streamer ingress_registry`

See `phase4-statuses.txt` for recorded exit codes.

## Final Branch/PR State

- Final local branch: `bugfix/issue-74-left-topic-authority`
- Final local HEAD: `2d42d167c83321ac351d7d3aa4a77b27393402b0`
- Backup branch: `backup/pr77-pre-tail-replay-20260211-104410` at `42d5a26136fd4f71ea873b7e414f8f6fdd9f17a8`
- PR URL: `https://github.com/eclipse-uprotocol/up-streamer-rust/pull/77`
- PR headRefOid after push: `2d42d167c83321ac351d7d3aa4a77b27393402b0`
- PR merge state status (post-push command): `UNKNOWN`
- PR merge state status (final re-check): `BLOCKED` (`mergeable=MERGEABLE`)
- Compare stats: `status=ahead`, `ahead_by=10`, `behind_by=0`, `total_commits=10`
