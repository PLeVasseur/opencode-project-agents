# Plan: Upgrade to up-rust 0.9 + latest transports (single PR, logical commits)

## How to use this plan

- [x] Read this file fully before making changes.
- [x] Execute tasks in order, phase by phase.
- [x] As each task is completed, change its checkbox from `[ ]` to `[x]` in this same file.
- [x] Do not batch-complete checkboxes; tick them immediately when done.
- [x] Keep all work in a single branch and single PR, with the commit boundaries defined below.

## Outcome target

- [x] Repository updated to use `up-rust` `0.9.x`.
- [x] Transport dependencies updated to latest versions supporting `up-rust 0.9`.
- [x] Workspace MSRV set to `1.88`.
- [x] Canonical cross-transport validations executed and reported.
- [x] One PR opened with logical commits (no squashing).

## Dependency target matrix

- [x] `up-rust = 0.9.x`
- [x] `up-transport-zenoh = 0.9.0`
- [x] `up-transport-mqtt5 = 0.4.0`
- [x] `up-transport-vsomeip` pinned to git `rev = 278ab26415559d6cb61f40facd21de822032cc83` (temporary until crates.io release)

## Constraints and notes

- [x] Use Rust MSRV `1.88` because latest `up-transport-mqtt5` requires it.
- [x] Keep work as one PR, but split into the commit chunks below.
- [x] Keep vsomeip as exact git `rev` pin for now; document follow-up to move back to crates.io when available.
- [x] Adapt code to `up-transport-zenoh 0.9` builder API (old `UPTransportZenoh::new(...)` pattern no longer valid).

---

## Phase 0 - Baseline and branch setup

- [x] Create branch for this migration.
- [x] Capture current status (`git status`, baseline compile expectations).
- [x] Confirm toolchain can run Rust `1.88`.

Commit in this phase: none.

---

## Phase 1 - Commit 1: MSRV baseline

**Commit message**: `chore: raise workspace MSRV to 1.88`

Tasks:
- [x] Update workspace rust version in root `Cargo.toml` to `1.88`.
- [x] Update any project docs/config references to old MSRV (if present).
- [x] Run a quick sanity compile for at least one crate (`cargo check -p up-streamer`).
- [x] Commit only MSRV-related changes.

---

## Phase 2 - Commit 2: Dependency matrix migration

**Commit message**: `chore: upgrade up-rust and transport dependency matrix`

Tasks:
- [x] Update root workspace dependency versions in `Cargo.toml`:
  - [x] `up-rust` to `0.9` (keep existing feature posture unless required to change).
  - [x] `up-transport-zenoh` to `0.9.0`.
  - [x] `up-transport-mqtt5` to crates.io `0.4.0` (replace git dep).
  - [x] `up-transport-vsomeip` to git pin with exact `rev` above.
- [x] Remove obsolete dependency feature flags that no longer exist (for example `zenoh-unstable` on zenoh transport).
- [x] Regenerate `Cargo.lock`.
- [x] Run workspace check and capture expected API-break errors for zenoh call sites.
- [x] Commit only dependency/lockfile/manifest updates.

---

## Phase 3 - Commit 3: Zenoh API refactor

**Commit message**: `refactor: migrate zenoh transport usage to 0.9 builder API`

Tasks:
- [x] Update all zenoh transport construction call sites from old constructor usage to builder-based API.
- [x] Prefer using zenoh config types re-exported by `up_transport_zenoh` to avoid cross-version type mismatch.
- [x] Refactor likely touch points:
  - [x] `configurable-streamer/src/main.rs`
  - [x] `example-streamer-implementations/src/bin/zenoh_someip.rs`
  - [x] `example-streamer-uses/src/bin/zenoh_client.rs`
  - [x] `example-streamer-uses/src/bin/zenoh_service.rs`
  - [x] `example-streamer-uses/src/bin/zenoh_publisher.rs`
  - [x] `example-streamer-uses/src/bin/zenoh_subscriber.rs`
  - [x] `up-linux-streamer-plugin/src/lib.rs` (as needed to compile with selected features)
- [x] Run `cargo check --workspace` and fix all zenoh-related compile errors.
- [x] Commit only zenoh API adaptation changes.

---

## Phase 4 - Commit 4: Integration and feature cleanup

**Commit message**: `fix: align feature wiring and compile after transport upgrades`

Tasks:
- [x] Resolve remaining compile issues from dependency upgrades.
- [x] Ensure feature definitions still map to valid dependency features.
- [x] Verify key packages compile with expected feature combinations:
  - [x] `up-linux-streamer` with `zenoh-transport,vsomeip-transport`
  - [x] `configurable-streamer`
  - [x] `example-streamer-uses` with each transport feature
- [x] Run `cargo check --workspace --all-targets`.
- [x] Commit integration/cleanup changes only.

---

## Phase 5 - Commit 5: Validation and documentation

**Commit message**: `docs: update migration notes and validation results`

Tasks:
- [x] Execute canonical validation scenario A (Zenoh <-> SOME/IP request/response):
  - [x] Streamer: `up-linux-streamer` bin `zenoh_someip`
  - [x] Entities: `someip_client` + `zenoh_service`
  - [x] Confirm pass criteria from project AGENTS guidance.
- [x] Execute canonical validation scenario B (Zenoh <-> MQTT5 request/response):
  - [x] Streamer: `configurable-streamer` with `CONFIG.json5`
  - [x] Entities: `mqtt_client` + `zenoh_service` (or inverse)
  - [x] Confirm stable request/response and no transport-level failures.
- [x] Run relevant tests (`cargo test --workspace` or scoped tests if environment-constrained).
- [x] Update docs impacted by these upgrades (READMEs and transport usage notes).
- [x] Include explicit note that vsomeip remains temporarily git-pinned.
- [x] Commit docs/validation evidence updates.

---

## PR assembly checklist (single PR)

- [x] Verify commit order is logical and matches this plan.
- [x] Ensure no unrelated changes are included.
- [x] Push branch and open one PR.
- [x] PR description includes:
  - [x] Why MSRV moved to `1.88`
  - [x] Dependency target matrix
  - [x] Temporary vsomeip git pin rationale and follow-up
  - [x] Validation commands and outcomes
  - [x] Commit-by-commit summary

Suggested PR title:

`Upgrade transports to up-rust 0.9 compatibility (MSRV 1.88)`

---

## Follow-up item (not part of this PR unless available during execution)

- [ ] Replace `up-transport-vsomeip` git pin with official crates.io release once a release containing `up-rust 0.9` support is published.
