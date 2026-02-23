# Plan: Upgrade `up-rust` to Latest crates.io Release

## Goal

Upgrade this workspace from `up-rust` `0.5.0` to the current crates.io latest (`0.9.0`) with minimal, scoped compatibility fixes and a clean PR against `main`.

## Source of Truth

- Target crate: `up-rust`
- crates.io API endpoint: `https://crates.io/api/v1/crates/up-rust`
- Expected latest version: `0.9.0`
- Current workspace dependency location: `Cargo.toml` (`[workspace.dependencies].up-rust`)

## Risks / Change Areas to Watch

- `up-rust` releases between `0.6.0` and `0.9.0` include breaking behavior changes.
- Listener/filter URI validation in newer `up-rust` may reject previously tolerated wildcard patterns.
- Payload extraction behavior is stricter for protobuf payload formats in newer releases.
- Workspace `rust-version` declaration may need alignment if dependency MSRV expectations are higher.

## Branching Strategy

- Base: upstream `main`
- Suggested branch: `chore/upgrade-up-rust-0.9.0`
- Keep scope limited to dependency upgrade + required compatibility/test fixes only.

## Checklist

- [ ] Resolve config and confirm plan path
  - [ ] Run `printenv OPENCODE_CONFIG_DIR`
  - [ ] Confirm this file path: `$OPENCODE_CONFIG_DIR/plans/up-rust-0.9.0-upgrade-plan.md`

- [ ] Prepare clean working branch from updated `main`
  - [ ] Verify remotes (`git remote -v`)
  - [ ] Fetch upstream (`git fetch upstream`)
  - [ ] Fast-forward local `main` from `upstream/main`
  - [ ] Create/switch branch `chore/upgrade-up-rust-0.9.0`

- [ ] Capture baseline before edits
  - [ ] Confirm current dependency pin (`Cargo.toml` has `up-rust = { version = "0.5.0" }`)
  - [ ] Confirm lockfile currently resolves `up-rust 0.5.0`
  - [ ] Record scope baseline:
    - [ ] `git log --oneline main..HEAD`
    - [ ] `git diff --name-only main...HEAD`

- [ ] Reconfirm target version on crates.io
  - [ ] Query crates API for `up-rust` latest
  - [ ] Confirm target is non-yanked and stable enough for this repo
  - [ ] Note release notes for `0.6.0`..`0.9.0` (breaking/behavioral highlights)

- [ ] Apply dependency upgrade
  - [ ] Update workspace dependency in `Cargo.toml` to `up-rust = { version = "0.9.0" }`
  - [ ] Update lockfile resolution (`cargo update -p up-rust --precise 0.9.0`)
  - [ ] Verify lockfile now contains `up-rust 0.9.0`

- [ ] Run compile pass and triage breakages early
  - [ ] `source build/envsetup.sh highest`
  - [ ] `cargo check --all-targets`
  - [ ] Fix compile/API breakages with minimal changes

- [ ] Compatibility adaptation pass (only if needed)
  - [ ] Listener/filter URI validation
    - [ ] Check `register_listener` call sites for wildcard/resource-id validity
    - [ ] Ensure point-to-point wildcard filters still satisfy current `determine_message_type` semantics
    - [ ] Adjust tests if stricter URI checks invalidate legacy patterns
  - [ ] Payload format handling
    - [ ] Ensure protobuf extraction paths do not assume `UNSPECIFIED` payload format is accepted
    - [ ] Update tests/examples that extract protobuf from SOME/IP payloads as needed
  - [ ] Communication helper/API drift
    - [ ] Verify `up_rust::communication` usage in examples still compiles and behaves as expected

- [ ] Rust version declaration decision
  - [ ] Compare workspace `rust-version` (`Cargo.toml`) against upgraded dependency expectations
  - [ ] If required and acceptable for project policy, bump workspace `rust-version` with clear PR rationale
  - [ ] If not changed, document why current declaration remains and confirm CI/toolchain compatibility

- [ ] Run full validation (required)
  - [ ] `source build/envsetup.sh highest`
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `cargo test -- --test-threads 1`
  - [ ] If `publisher_subscriber` fails by one message once, rerun full serial test command once

- [ ] Validate scope before PR
  - [ ] `git log --oneline main..HEAD`
  - [ ] `git diff --name-only main...HEAD`
  - [ ] Ensure only dependency upgrade + necessary compatibility fixes are included

- [ ] Commit strategy
  - [ ] Commit dependency manifest/lock update
  - [ ] Commit compatibility/test adjustments separately (if any)
  - [ ] Keep commit messages explicit about "upgrade" vs "adaptation"

- [ ] Open PR to `main`
  - [ ] Push branch to origin
  - [ ] Create PR with explicit repo/base/head flags
  - [ ] Include in PR body:
    - [ ] crates.io target version confirmation (`0.9.0`)
    - [ ] concise list of required code adaptations
    - [ ] note on rust-version decision
    - [ ] exact validation commands run and outcomes

- [ ] Final handoff report
  - [ ] Files changed
  - [ ] Brief diff summary
  - [ ] Clippy/test results (include flaky rerun note if applicable)
  - [ ] Commit SHA(s)
  - [ ] PR URL

## Suggested Validation Commands (copy/paste)

```bash
source build/envsetup.sh highest
cargo check --all-targets
cargo clippy --all-targets -- -W warnings -D warnings
cargo test -- --test-threads 1
```

## Definition of Done

- [ ] Workspace depends on `up-rust 0.9.0` and lockfile is updated accordingly.
- [ ] Compatibility changes (if needed) are minimal and scoped.
- [ ] Local clippy and serial tests pass (with flaky retry policy applied if needed).
- [ ] PR is open against `main` with clear upgrade rationale and validation evidence.
