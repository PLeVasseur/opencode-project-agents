# Plan: Land PR #42 Change with Original Author Credit

## Goal

Land the functional change from PR #42 as a new, clean PR to `main`, while preserving and clearly documenting credit to the original author.

## Source of Truth

- Upstream repo: `eclipse-uprotocol/up-transport-vsomeip-rust`
- Source PR: `https://github.com/eclipse-uprotocol/up-transport-vsomeip-rust/pull/42`
- Source commit to carry forward:
  - SHA: `3e277e835916b9428d8492ea1ae1383c5131bca6`
  - Author: `ValMobBIllich <benedikt.illich@valtech.com>`
  - Message: `fixed streamer usecase check, enforce source authority non-wildcard`
  - File touched: `up-transport-vsomeip/src/determine_message_type.rs`

## Scope

Include only the PR #42 functional change in `determine_message_type`.

If compatibility tweaks are required due to drift from current `main`, keep them in a second, explicit maintainer-authored commit.

## Branching Strategy

- Working branch: `fix/streamer-usecase-pr42`
- Temporary firewall reference: `pr42-firewall`
- Base branch: current upstream `main`

## Checklist

- [ ] Resolve config path and ensure plan source is correct
  - [ ] Run `printenv OPENCODE_CONFIG_DIR`
  - [ ] Confirm this plan is being read from `$OPENCODE_CONFIG_DIR/plans/pr42-author-credit-landing-plan.md`

- [ ] Verify remotes and fetch latest refs
  - [ ] Ensure `upstream` points to `https://github.com/eclipse-uprotocol/up-transport-vsomeip-rust.git`
  - [ ] Run `git fetch upstream`

- [ ] Create firewall ref from PR #42
  - [ ] Run `git fetch upstream pull/42/head:pr42-firewall`
  - [ ] Verify expected commit metadata from firewall ref:
    - `git log -1 --format='%H%n%an <%ae>%n%s' pr42-firewall`
  - [ ] Confirm SHA is `3e277e835916b9428d8492ea1ae1383c5131bca6`

- [ ] Create clean working branch from upstream `main`
  - [ ] If local `main` is not current, fast-forward it:
    - `git switch main`
    - `git merge --ff-only upstream/main`
  - [ ] Create/reset working branch from updated `main`:
    - `git switch -C fix/streamer-usecase-pr42 main`

- [ ] Carry forward PR #42 commit with attribution preserved
  - [ ] Run `git cherry-pick -x 3e277e835916b9428d8492ea1ae1383c5131bca6`
  - [ ] Verify author is preserved:
    - `git log -1 --format='%H%n%an <%ae>%n%s'`
  - [ ] Verify patch scope:
    - `git show --name-only --format='' HEAD`

- [ ] Conflict or drift handling (only if cherry-pick does not apply cleanly)
  - [ ] Resolve conflicts while preserving PR #42 behavior in `determine_message_type`
  - [ ] Complete cherry-pick so the original-author commit remains in history
  - [ ] If any extra adaptation is required, create a second commit by maintainer with concise rationale
  - [ ] Keep adaptation minimal and scoped

- [ ] Validate scope before running full checks
  - [ ] `git log --oneline main..HEAD`
  - [ ] `git diff --name-only main...HEAD`
  - [ ] Confirm no unrelated files/commits are present

- [ ] Run required local validation
  - [ ] `source build/envsetup.sh highest`
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `cargo test -- --test-threads 1`
  - [ ] If `publisher_subscriber` fails by one message once, rerun the same serial test command once before treating as hard failure

- [ ] Push branch and open PR
  - [ ] Push branch:
    - `git push -u origin fix/streamer-usecase-pr42`
  - [ ] Create PR to upstream `main` with explicit attribution in body, using safe heredoc:
    - include source PR #42 URL
    - include source commit SHA
    - state original author name/email
    - include local validation commands/results

- [ ] Cross-link PR #42
  - [ ] Comment on PR #42 with new PR link
  - [ ] State this new PR carries the same functional change with preserved author credit and clean branch scope
  - [ ] Use single-quoted heredoc for comment body to avoid shell interpolation
  - [ ] Verify latest comment text with `gh api` after posting

- [ ] Final verification and handoff report
  - [ ] Collect changed files list
  - [ ] Capture brief diff summary
  - [ ] Capture clippy/test outcomes (include flaky rerun note if applicable)
  - [ ] Capture commit SHA(s)
  - [ ] Capture PR URL

## PR Body Template (Recommended)

Use this structure in the new PR:

- Summary of functional change
- Attribution section:
  - "This change carries forward PR #42"
  - original commit SHA
  - original author
  - note that cherry-pick preserved commit authorship
- Validation section with exact commands run

## Definition of Done

- [ ] New PR targeting `main` is open from `fix/streamer-usecase-pr42`
- [ ] PR contains only intended PR #42 change (plus minimal documented adaptation if needed)
- [ ] Original author credit is preserved in commit history and called out in PR text
- [ ] Local clippy and serial tests pass (with flaky retry policy applied if needed)
- [ ] PR #42 contains a cross-link comment to the new PR
