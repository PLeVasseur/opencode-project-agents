Execute the plan at `$OPENCODE_CONFIG_DIR/plans/main-ci-fixes-independent-pr-plan.md`.

Process requirements:
- First run `printenv OPENCODE_CONFIG_DIR` and confirm the resolved path.
- Read the plan from `$OPENCODE_CONFIG_DIR/plans` (do not use repo globbing to locate plans).
- Execute the plan end-to-end with scope limited to the 3 CI fixes only.
- Branch from `main` as `fix/main-ci-failures`.
- Run local validation:
  - `source build/envsetup.sh highest`
  - `cargo clippy --all-targets -- -W warnings -D warnings`
  - `cargo test -- --test-threads 1`
- Commit with a concise CI-fix message, open a PR targeting `main`, and comment on PR #42 with the new PR link.

At the end, report:
1) files changed
2) brief diff summary
3) clippy/test results
4) commit SHA
5) PR URL
