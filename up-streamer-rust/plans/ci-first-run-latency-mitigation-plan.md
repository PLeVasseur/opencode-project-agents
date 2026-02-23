# CI First-Run Latency Mitigation Plan (Session-Handoff Grade)

## 0) Purpose and Success Definition

This plan is written so a **fresh session** can execute it end-to-end without hidden context.

Success means all of the following are true on the PR branch:

- Required checks are unchanged and green:
  - Bundled: `Lint`, `Test`, `Build documentation`
  - Unbundled: `Lint`, `Test`, `Build documentation`, `obtain_and_build_vsomeip`
- No validation-signal loss (no dropped lint/test/doc intent)
- No cache contention regressions (`Unable to reserve cache` absent)
- First-run latency is improved for at least one critical required job, with before/after evidence
- Deliverables prepared: run URLs, timing table, bottleneck summary, rollback notes

## 1) Scope, Constraints, and Non-Goals

### Scope

- CI workflow and docs/reporting changes only
- No runtime behavior changes in Rust crates

### Constraints

- Keep one branch and one PR
- Keep required check names exactly as above
- Keep branch-protection signal intact
- Keep commits aligned to logical plan chunks (no squash/amend unless explicitly requested)

### Non-Goals

- Fixing ECA identity instability for new SHAs (tracked externally)
- Broad build-system redesign beyond measured first-run ROI

## 2) Current Evidence Snapshot (Use as Baseline)

Reference successful timing run and companion required-check runs:

- Timing profile run: `21781569523`
  - https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21781569523
- Bundled required checks run: `21781569522`
  - https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21781569522
- Unbundled required checks run: `21781569519`
  - https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21781569519

Top first-run bottlenecks from cargo timings artifacts:

- Bundled base (`224.7s total`)
  - `openssl-sys v0.9.111 build script (run)`: `101.9s` (~45.3%)
  - `stabby-abi`: `29.7s` (~13.2%)
  - `zenoh`: `25.5s` (~11.3%)
  - `ring build script`: `23.8s` (~10.6%)
- Bundled feature (`229.5s total`)
  - `vsomeip-sys build script (run)` (`bundled, cmake`): `128.4s` (~55.9%)
  - `zenoh`: `30.3s` (~13.2%)
  - `stabby-abi`: `29.3s` (~12.8%)
  - `up-transport-vsomeip`: `13.9s` (~6.1%)
- Unbundled feature (`254.1s total`)
  - `openssl-sys build script (run)`: `116.8s` (~46.0%)
  - `zenoh`: `31.6s` (~12.4%)
  - `stabby-abi`: `26.1s` (~10.3%)
  - `up-transport-vsomeip`: `22.0s` (~8.7%)

Implication:

- Highest cross-workflow ROI is OpenSSL vendored-build mitigation
- Highest bundled-only bottleneck is bundled vsomeip CMake build

## 3) Execution Order (Do In Order)

### Phase A - Preflight and Guardrails

- [x] Confirm branch and PR head state:
  - `git status --short --branch`
  - `gh pr view 76 --repo eclipse-uprotocol/up-streamer-rust --json headRefOid,statusCheckRollup,url`
- [x] Confirm required check names currently visible in status rollup
- [x] Freeze baseline durations from current reference runs:
  - Bundled: `Lint`, `Test`
  - Unbundled: `Lint`, `Test`
- [x] Confirm current cache policy still one-writer-per-workflow

Acceptance gate:

- Do not continue if required checks are already renamed/missing

---

### Phase B - OpenSSL First-Run Mitigation (Highest ROI)

Goal: avoid vendored OpenSSL compile in CI paths that currently spend ~102s to ~117s in `openssl-sys` build script.

Files to touch:

- `.github/workflows/bundled-lint-and-test.yaml`
- `.github/workflows/unbundled-lint-and-test.yaml`
- `.github/workflows/cargo-timings-profile.yaml`

Changes:

- [x] In compile-heavy jobs, set `OPENSSL_NO_VENDOR=1`
- [x] Ensure those jobs install `pkg-config` and `libssl-dev`
- [x] Keep all required job names unchanged
- [x] Keep rust-cache writer policy unchanged

Validation:

- [x] Push and run bundled + unbundled workflows
- [x] Run timings profile workflow for post-change evidence
- [x] Confirm no workflow regressions
- [x] Confirm `openssl-sys` timing drops materially in timing artifacts (or at least loses `vendored` feature)

Acceptance gate:

- Proceed only if required checks still green and names unchanged

Rollback trigger:

- Any OpenSSL linkage failure or deterministic breakage in lint/test/doc jobs

---

### Phase C - Bundled Lint Feature De-duplication

Goal: reduce duplicate compile work inside bundled lint feature shard.

Current behavior in shard:

- `cargo build --features ...`
- then `cargo clippy --features ... --all-targets -- -W warnings -D warnings`

Planned optimization:

- [x] Replace two-pass feature build+clippy with one strict `cargo clippy --all-targets` pass for same feature set
- [x] Keep base lint shard unchanged
- [x] Keep final `Lint` aggregator check and deterministic fail logic (`always()` + explicit result checks)

Validation:

- [x] Bundled workflow green
- [x] `Lint` required check green (not skipped)
- [x] Compare bundled critical path before/after

Acceptance gate:

- No reduction of lint strictness (`-W warnings -D warnings` preserved)

Rollback trigger:

- Missing validation signal or unstable results

---

### Phase D - Bundled vsomeip Stability and Cache Hygiene

Goal: keep feature shard stable while avoiding stale `-lvsomeip3` link failures.

- [x] Keep stale-artifact guard after rust-cache restore in bundled feature shard
- [x] Verify guard does not introduce unnecessary extra rebuild outside intended scope
- [x] Confirm no `-lvsomeip3` failures in bundled feature lint
- [x] Confirm no cache reservation collisions

Validation commands:

- `gh run view <bundled_run_id> --log | rg -n "unable to find library -lvsomeip3|Unable to reserve cache"`

Acceptance gate:

- Bundled `Lint (feature...)` stable across at least one additional rerun

---

### Phase E - Optional Optimization (Only If Needed)

Execute only if Phases B-D do not produce acceptable first-run gain.

- [ ] Trial one narrow graph optimization that keeps required checks unchanged
- [ ] Require measured improvement + no stability regression
- [ ] Revert immediately if mixed results

## 4) Reporting and Evidence Collection

### Required artifacts to collect per phase

- [x] Run URLs (bundled, unbundled, timings)
- [x] Job durations table (`Lint`, `Test`, plus internal bundled lint shards)
- [x] Cache behavior summary:
  - writer jobs
  - restore-only jobs
  - contention status
- [x] Timing artifact bottleneck summary (top crates + percentages)

### Before/After table template

- [x] Fill this table in final report:

| Workflow | Job | Before (s) | After (s) | Delta (s) | Delta (%) | Run URL (After) |
|---|---:|---:|---:|---:|---:|---|
| Bundled | Lint |  |  |  |  |  |
| Bundled | Test |  |  |  |  |  |
| Unbundled | Lint |  |  |  |  |  |
| Unbundled | Test |  |  |  |  |  |

## 5) Commit Chunk Plan

- [x] Commit A: OpenSSL no-vendor mitigation across workflows
- [x] Commit B: Bundled feature lint de-duplication
- [x] Commit C: Bundled vsomeip stability/cache hygiene hardening
- [ ] Commit D: Plan/report updates with measured before/after results

Commit hygiene checks before each commit:

- [x] `git diff --name-only --cached`
- [x] `git diff --stat --cached`

## 6) Explicit Rollback Order

If regression appears, revert in this order:

1. Optional Phase E changes
2. Phase D stability tweaks
3. Phase C de-duplication
4. Phase B OpenSSL mitigation

After each rollback step:

- [ ] Re-run bundled/unbundled required workflows
- [ ] Confirm required checks green and names unchanged

## 7) Session Handoff Checklist (for a New Agent/Session)

- [x] Read this plan file completely
- [x] Confirm current branch head SHA and latest run IDs
- [x] Execute Phase A preflight first (no code changes)
- [x] Execute one phase at a time with push + measurement
- [x] Update checkboxes immediately after each completed item
- [ ] Stop and report at first unexpected regression with run URL and log proof

## 8) Known External Blocker (Non-Execution)

- ECA status on new SHAs may fail due to external identity mapping behavior.
- This does not invalidate CI latency measurements, but may block mergeability.
