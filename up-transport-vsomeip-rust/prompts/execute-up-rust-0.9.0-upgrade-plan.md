Execute the plan at `$OPENCODE_CONFIG_DIR/plans/up-rust-0.9.0-upgrade-plan.md` end-to-end.

Follow these constraints:
- First run `printenv OPENCODE_CONFIG_DIR`, confirm the plan path, and use that exact file as source of truth.
- Work from updated `main`, then create/switch to `chore/upgrade-up-rust-0.9.0`.
- Keep scope strictly to upgrading `up-rust` to `0.9.0` plus only the minimal compatibility/test fixes required.

Required implementation steps:
1) Update `[workspace.dependencies].up-rust` to `0.9.0` in `Cargo.toml`.
2) Update lockfile with `cargo update -p up-rust --precise 0.9.0`.
3) Run early compile triage:
   - `source build/envsetup.sh highest`
   - `cargo check --all-targets`
4) Fix only necessary API/behavior breakages (listener/filter URI validation, payload extraction strictness, communication API drift).
5) Decide whether workspace `rust-version` must change; if not, document why.

Required validation:
- `source build/envsetup.sh highest`
- `cargo clippy --all-targets -- -W warnings -D warnings`
- `cargo test -- --test-threads 1`
- If `publisher_subscriber` fails by one message once, rerun the full serial test command once.

Before PR:
- Verify scope with:
  - `git log --oneline main..HEAD`
  - `git diff --name-only main...HEAD`
- Prefer separate commits for:
  - dependency/lock upgrade
  - compatibility adaptations (if any)

PR requirements:
- Push branch and open PR to `main`.
- Use single-quoted heredoc for any `gh pr create` body content.
- Include: crates.io target confirmation (`up-rust 0.9.0`), compatibility changes, rust-version decision, exact validation commands + outcomes.

Final handoff must include:
- files changed
- concise diff summary
- clippy/test results (including flaky rerun note if applicable)
- commit SHA(s)
- PR URL

If blocked, stop at the smallest blocker, explain root cause, and provide 1-2 concrete unblock options.
