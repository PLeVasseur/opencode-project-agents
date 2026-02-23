# Plan: Version compatibility alignment for streamer stack

## Context
- Current workspace uses:
  - `up-rust = 0.5.0` (`Cargo.toml:55`, `Cargo.lock:4808`)
  - `up-transport-zenoh = 0.6.0` (`Cargo.toml:56`, `Cargo.lock:4893`)
  - `up-transport-vsomeip` from git upstream (`Cargo.toml:57`, `Cargo.lock:4871`)
- Upstream ecosystem versions are not uniformly aligned; mixing latest crates.io versions with older git-based streamer dependencies is high risk.

## Problem statement
- Version skew across `up-rust`, transport crates, and git dependencies can cause compile/runtime incompatibilities that are hard to diagnose.
- Bug triage can be confounded by dependency mismatch instead of actual logic defects.

## Goal
- Establish a deterministic, explicitly documented compatibility baseline for Zenoh <-> UStreamer <-> SOME/IP validation.
- Prevent accidental drift during issue testing and fix verification.

## Baseline policy
- For current testing and bug validation, pin to streamer-compatible set:
  - `up-rust = 0.5.0`
  - `up-transport-zenoh = 0.6.0`
  - `up-transport-vsomeip` from git (temporary fork if Bug #1 workaround is needed)
- Do not mix with `0.9.x` line in the same dependency graph unless doing a deliberate full-stack upgrade.

## Implementation plan
1. Encode explicit dependency constraints
- Keep workspace dependency declarations aligned with the baseline.
- Ensure lockfile reflects intended sources/versions and is committed for reproducibility.

2. Add compatibility documentation
- Add a short matrix in project docs specifying known-good combinations and known-bad mixed combinations.
- Include warning that crates.io `up-transport-vsomeip` release may not contain required streamer fix.

3. Add CI/build guardrails
- Add a lightweight CI job or script that checks resolved versions/sources for key crates.
- Fail fast if incompatible versions are introduced.

4. Define upgrade track (separate from bug fixes)
- Create a dedicated upgrade plan to move all uProtocol crates together to a newer coherent set.
- Require full regression sweep across zenoh/mqtt/someip paths before accepting upgrade.

## Validation checklist
- `cargo tree`/lockfile show expected versions and sources.
- Build and key streamer scenarios pass under pinned baseline.
- Docs clearly state required versions for reproducing Bugs #1-#3.
- CI guard catches accidental drift.

## Risks and mitigations
- Risk: long-term pinning delays adoption of upstream fixes.
  - Mitigation: schedule periodic dependency review with explicit upgrade branch.
- Risk: hidden transitive drift through git updates.
  - Mitigation: pin git revisions where needed during active triage windows.

## Exit criteria
- A single, documented, reproducible dependency baseline exists for triage and testing.
- No accidental mixed-version states in normal development/CI flows.
- Upgrade path is defined as a controlled, separate effort.
