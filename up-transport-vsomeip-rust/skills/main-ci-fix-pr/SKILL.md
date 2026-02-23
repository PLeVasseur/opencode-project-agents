---
name: main-ci-fix-pr
description: Execute independent main-branch CI fix plans with strict scope, local validation, PR creation, and cross-linking.
license: Apache-2.0
compatibility: opencode
metadata:
  project: up-transport-vsomeip-rust
  workflow: ci-fix
---

## When to use

Use this skill when asked to execute a CI-fix plan as a standalone PR targeting `main`, especially when another feature PR already exists.

## Workflow

1. Resolve config-plan location first:
   - Run `printenv OPENCODE_CONFIG_DIR`.
   - Read the requested plan from `$OPENCODE_CONFIG_DIR/plans`.
2. Prepare clean scope:
   - Branch from `main` (for example `fix/main-ci-failures`).
   - If borrowing changes from another PR for temporary validation, isolate them in a firewall branch/commit.
   - Recreate the final PR branch with only intended commits.
3. Apply only scoped fixes from the plan.
4. Validate locally from repo root:
   - `source build/envsetup.sh highest`
   - `cargo clippy --all-targets -- -W warnings -D warnings`
   - `cargo test -- --test-threads 1`
5. Flake handling:
   - If `publisher_subscriber` misses by one message once, rerun the same serial test command once before declaring failure.
6. PR target safety preflight:
   - Confirm branch/repo context before PR creation (`git branch --show-current`, `git remote -v`).
   - Create PR with explicit target/source flags:
     - `gh pr create --repo <owner>/<repo> --base main --head <fork-owner>:<branch> ...`
   - Verify PR routing immediately after creation:
     - `gh pr view <pr-number-or-url> --repo <owner>/<repo> --json url,baseRefName,headRefName`
7. Open PR and cross-link:
   - Push branch and open PR to `main`.
   - Comment on related PRs with the new PR URL.
   - Capture the cross-link comment URL for reporting.

## Scope guardrails

- Keep this PR limited to CI fixes (plus feasible warning cleanup explicitly requested during validation).
- Before opening PR, run:
  - `git log --oneline main..HEAD`
  - `git diff --name-only main...HEAD`
- If output includes unrelated work, rebuild the branch with cherry-picks.

## Reporting template

Always report:

1. Files changed
2. Brief diff summary
3. Clippy/test results (include rerun note for flaky tests)
4. Commit SHA(s)
5. PR URL
6. Cross-link comment URL(s)
7. Whether history rewrite occurred (yes/no) and final commit SHA(s)
