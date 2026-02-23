Execute the plan at `$OPENCODE_CONFIG_DIR/plans/pr42-author-credit-landing-plan.md` end-to-end.

Process checklist:
- [ ] Run `printenv OPENCODE_CONFIG_DIR` first and confirm the resolved path.
- [ ] Read the plan from `$OPENCODE_CONFIG_DIR/plans` (do not use repo globbing to locate plans).
- [ ] If available, load skills: `main-ci-fix-pr`, `rust-ffi-lint-triage`, and `gh-safe-pr-commenting`.
- [ ] Branch from updated `main` as `fix/streamer-usecase-pr42`.
- [ ] Create firewall ref `pr42-firewall` from PR #42 and verify source commit metadata.
- [ ] Carry forward commit `3e277e835916b9428d8492ea1ae1383c5131bca6` using `git cherry-pick -x`, preserving original author attribution.
- [ ] Keep scope strict to the PR #42 change; if drift adaptation is required, put it in a separate maintainer-authored commit.
- [ ] Validate scope before PR with:
  - [ ] `git log --oneline main..HEAD`
  - [ ] `git diff --name-only main...HEAD`
- [ ] Run local validation:
  - [ ] `source build/envsetup.sh highest`
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `cargo test -- --test-threads 1`
  - [ ] If `publisher_subscriber` fails by one message once, rerun the full serial test command once before classifying as hard failure.
- [ ] Push branch and open a PR targeting `main`.
- [ ] In the PR body, explicitly include:
  - [ ] source PR #42 URL
  - [ ] source commit SHA
  - [ ] original author name/email
  - [ ] note that cherry-pick preserved authorship
  - [ ] validation commands run
- [ ] Comment on PR #42 with the new PR link using a single-quoted heredoc-safe body.
- [ ] Verify posted comment text via `gh api`; if malformed, add a correction comment.

Final report checklist:
- [ ] files changed
- [ ] brief diff summary
- [ ] clippy/test results
- [ ] commit SHA(s)
- [ ] PR URL
- [ ] PR #42 comment URL
