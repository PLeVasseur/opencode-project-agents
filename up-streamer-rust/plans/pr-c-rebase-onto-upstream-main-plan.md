# PR C Rebase Onto upstream/main Plan

- [ ] Outcome contract
  - [ ] PR C branch is rebased directly onto `upstream/main` after PR A and PR B merges.
  - [ ] Current branch is never assumed; PR C head branch is resolved from GitHub and explicitly checked out before any rewrite.
  - [ ] Commit intent is preserved (no accidental drops or extra commits).
  - [ ] Rebased branch is pushed with `--force-with-lease` and PR reflects the new tip.

- [ ] 1) PR targeting, branch guard, and preflight
  - [ ] Set PR C selector (number or URL): `pr_c="<PR_C_NUMBER_OR_URL>"`
  - [ ] Resolve expected PR C head branch from GitHub:
    - [ ] `expected_branch="$(gh pr view "$pr_c" --json headRefName -q .headRefName)"`
    - [ ] `expected_head_oid="$(gh pr view "$pr_c" --json headRefOid -q .headRefOid)"`
  - [ ] Check out the exact PR C head branch: `git checkout "$expected_branch"`
  - [ ] Confirm working branch and tip match PR metadata (fail fast if not):
    - [ ] `branch="$(git rev-parse --abbrev-ref HEAD)"`
    - [ ] `local_head_oid="$(git rev-parse HEAD)"`
    - [ ] `test "$branch" = "$expected_branch"`
    - [ ] `test "$local_head_oid" = "$expected_head_oid"`
  - [ ] Confirm clean working tree before rewriting history: `git status -sb`
  - [ ] Capture PR context for logs: `gh pr view "$pr_c" --json number,headRefName,baseRefName,url`
  - [ ] Fetch latest refs so merged PR A/PR B commits are present: `git fetch upstream main --prune && git fetch origin --prune`
  - [ ] Confirm divergence summary: `git rev-list --left-right --count upstream/main..."$branch"`

- [ ] 2) Create no-loss backup refs
  - [ ] Create timestamp anchor once: `ts="$(date -u +%Y%m%dT%H%M%SZ)"`
  - [ ] Create local backup branch and tag at current PR C tip:
    - [ ] `git branch "backup/prc-pre-rebase-${ts}" "$branch"`
    - [ ] `git tag "backup/prc-pre-rebase-${ts}" "$branch"`
  - [ ] (Recommended) Push backup refs for remote recovery:
    - [ ] `git push origin "backup/prc-pre-rebase-${ts}"`
    - [ ] `git push origin "refs/tags/backup/prc-pre-rebase-${ts}"`

- [ ] 3) Rebase PR C onto upstream/main
  - [ ] Detect whether PR C contains merge commits: `git rev-list --merges upstream/main.."$branch"`
  - [ ] Rebase strategy:
    - [ ] If no merge commits: `git rebase upstream/main`
    - [ ] If merge commits exist: `git rebase --rebase-merges upstream/main`
  - [ ] Conflict loop (if needed): resolve files, `git add <paths>`, then `git rebase --continue` until complete
  - [ ] Abort path (if needed): `git rebase --abort`

- [ ] 4) Verify rebased history and diff shape
  - [ ] Confirm PR C is now based on `upstream/main`: `git merge-base --is-ancestor upstream/main "$branch"`
  - [ ] Inspect final commit list for PR C: `git log --oneline upstream/main.."$branch"`
  - [ ] Compare pre/post-rebase commit intent with range-diff:
    - [ ] `git range-diff upstream/main..."backup/prc-pre-rebase-${ts}" upstream/main..."$branch"`
  - [ ] Validate file-level delta still matches PR C scope: `git diff --stat upstream/main..."$branch"`

- [ ] 5) Validation checks
  - [ ] Run at least targeted checks for changed crates/files.
  - [ ] If transport-affecting, run CI-parity preflight matrix from repo root:
    - [ ] `source build/envsetup.sh highest`
    - [ ] `cargo build`
    - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
    - [ ] `cargo fmt -- --check`
    - [ ] `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
    - [ ] `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
    - [ ] `cargo check --workspace --all-targets`
    - [ ] `cargo test --workspace`

- [ ] 6) Publish rebased branch and confirm PR health
  - [ ] Push rewritten branch safely: `git push --force-with-lease origin "$branch"`
  - [ ] Confirm PR now points to rebased tip:
    - [ ] `gh pr view --json number,url,headRefOid,baseRefName,mergeable,mergeStateStatus`
  - [ ] Confirm no unexpected commits remain in the PR stack: `git log --oneline upstream/main.."$branch"`

- [ ] 7) Rollback plan (only if needed)
  - [ ] Reset local branch to backup ref: `git reset --hard "backup/prc-pre-rebase-${ts}"`
  - [ ] Restore remote branch: `git push --force-with-lease origin "$branch"`
  - [ ] Keep backup refs until PR C merges and CI is green.
