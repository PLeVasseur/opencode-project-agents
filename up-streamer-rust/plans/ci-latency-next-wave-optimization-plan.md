# Plan: CI Latency Next Wave (Cache Topology, Compiler Caching, and Graph Restructure)

## Goal

Reduce PR critical-path latency further (especially `Lint`) while preserving required check names and CI signal quality.

## Current State Snapshot (from latest successful run on PR #76)

- Bundled workflow (`Lint and Test - Bundled`)
  - `Lint`: ~12m50s
  - `Test`: ~4m54s
  - `Build documentation`: ~45s
- Unbundled workflow (`Lint and Test - Unbundled`)
  - `Lint`: ~6m45s
  - `Test`: ~4m48s
  - `Build documentation`: ~46s
  - `obtain_and_build_vsomeip`: ~15s (cache hit path)
- Known cache contention symptom in logs:
  - `Failed to save: Unable to reserve cache with key ... another job may be creating this cache.`

## Scope

In scope:

1. Fix Rust cache key topology to avoid cross-workflow/job contention.
2. Set one Rust cache writer per workflow; keep other jobs restore-only.
3. Evaluate and (if beneficial) enable `sccache` for Rust compile steps.
4. Evaluate `cache-workspace-crates: true` with measured outcomes.
5. Add `cargo --timings` profiling for crate-level bottleneck analysis.
6. If needed, restructure bundled lint into parallel internals while preserving required check name `Lint`.
7. Improve graph-level sharing opportunities across CI pipelines where feasible.

Out of scope:

- Runtime behavior changes
- Product code changes
- Renaming required PR checks

## Guardrails

- [x] Preserve required PR check names:
  - [x] Bundled: `Lint`, `Test`, `Build documentation` (trial emits `Lint` via aggregator)
  - [x] Unbundled: `Lint`, `Test`, `Build documentation`, `obtain_and_build_vsomeip`
- [x] Keep changes CI/workflow-only unless explicitly approved.
- [ ] Keep branch-protection compatibility intact (currently blocked by ECA identity drift on new SHAs and bundled lint feature-link regression).
- [ ] Capture before/after timing with run URLs for every optimization phase.

## Phase 0 - Baseline and Graph Mapping

- [x] Capture baseline run metadata and timings for current graph.
  - [x] Export per-job durations for bundled and unbundled workflows.
  - [x] Capture queue/start/finish times for critical jobs.
- [x] Build an explicit CI graph map.
  - [x] Enumerate jobs and `needs` edges in bundled and unbundled workflows.
  - [x] Mark compile-heavy steps, duplicated steps, and cache restore/save points.
  - [x] Identify opportunities to reuse outputs/caches and avoid duplicate work.
- [x] Confirm branch-protection-required checks currently configured in target repo.
  - Baseline bundled run: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21774091310 (`Lint` 12m50s, `Test` 4m54s, `Build documentation` 45s)
  - Baseline unbundled run: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21774091311 (`Lint` 6m45s, `Test` 4m48s, `Build documentation` 46s, `obtain_and_build_vsomeip` 15s)
  - Critical-path timestamps captured from job metadata (`startedAt`/`completedAt`) for bundled/unbundled `Lint` and `Test`
  - Graph map (bundled): `set-env -> {lint, test, build-docs}`; all three jobs run Rust cache restore/save today
  - Graph map (unbundled): `set-env -> obtain_and_build_vsomeip -> {lint, test, build-docs}` with `set-env` also needed by `{lint, test, build-docs}`
  - Compile-heavy steps: bundled `cargo build`/`cargo clippy` (base + feature), unbundled feature `cargo build`/`cargo clippy`, both `cargo test` jobs
  - Duplicate/setup-heavy steps: repeated apt installs and repeated Rust cache post-save attempts across parallel jobs
  - Opportunity selected for highest ROI first: workflow-specific rust-cache topology + single writer job per workflow
  - Branch protection/ruleset check query (`repos/.../rules/branches/main`) shows required status context `eclipsefdn/eca`; PR status rollup still includes expected CI checks (`Lint`, `Test`, `Build documentation`, `obtain_and_build_vsomeip`)

## Phase 1 - Rust Cache Topology Fix (Highest ROI)

- [x] Remove cache key collisions across workflows/jobs.
  - [x] Ensure rust-cache keys include workflow identity (not only job id).
  - [x] Ensure bundled and unbundled `lint` jobs cannot share the same final key unless explicitly intended.
- [x] Adopt one-writer-per-workflow cache policy.
  - [x] Bundled workflow: keep `lint` as cache writer.
  - [x] Bundled `test` and `build-docs`: restore-only mode.
  - [x] Unbundled workflow: keep `lint` as cache writer.
  - [x] Unbundled `test` and `build-docs`: restore-only mode.
- [x] Validate cache behavior from logs.
  - [x] No `Unable to reserve cache` errors in post-job cache steps.
  - [x] Confirm successful cache save in designated writer jobs.
  - [x] Confirm restores happen in non-writer jobs.
  - Validation runs:
    - Bundled: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21774567403
    - Unbundled: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21774567422
  - Writer jobs (`Lint`) now use workflow-scoped keys (`v0-rust-Lint and Test - Bundled-...`, `v0-rust-Lint and Test - Unbundled-...`) and complete post-job save without reservation collisions
  - Restore-only jobs show `save-if: false` and still restore cache state for compile/test/doc steps

## Phase 2 - Compiler Output Caching via sccache (Attempted, then skipped)

- [x] Add `sccache` wiring in compile-heavy jobs (trialed in commits `4da3b2b` and `0e63b9d`).
  - [x] Install/configure `sccache` in bundled `lint`/`test`/`build-docs`.
  - [x] Install/configure `sccache` in unbundled `lint`/`test`/`build-docs`.
  - [x] Set `RUSTC_WRAPPER=sccache` and `SCCACHE_GHA_ENABLED=true` where applicable.
- [x] Add diagnostics during trial.
  - [x] Print `sccache --show-stats` at end of compile-heavy jobs.
  - [x] Capture hit/miss rates in workflow logs.
- [x] Validate correctness and rollback on regression.
  - [x] Detect regressions in CI (`openssl-sys`/OpenSSL assembler failures with `sccache`) on runs `21774812598` and `21774812605`.
  - [x] Roll back Phase 2 trial to stable commit `71fc302` and re-push.
  - [x] Confirm rollback health on runs `21774567403` and `21774567422`.
- [x] Skip further Phase 2 work in this wave to keep focus on first-run latency and stability.

## Phase 3 - Evaluate Workspace-Crate Caching (Skipped for now)

- [x] Defer `cache-workspace-crates: true` trial for this cycle.
  - [x] Rationale captured: mainly warm-run optimization with limited first-run ROI.
  - [x] Follow-up captured: revisit after Phase 4/5 first-run changes are stable.
- [ ] (Future) Trial `cache-workspace-crates: true` in rust-cache.
  - [ ] Enable in writer jobs first.
  - [ ] Keep restore-only semantics for non-writer jobs.
- [ ] (Future) Measure impact over at least two consecutive runs.
  - [ ] Cold run timing.
  - [ ] Warm run timing.
  - [ ] Compare against Phase 1/2 baseline.
- [ ] (Future) Decision gate.
  - [ ] Keep setting only if net latency improvement is consistent.
  - [ ] Revert if cache churn/size or instability offsets gains.

## Phase 4 - Cargo Timings Profiling

- [x] Add cargo timings profiling workflow scaffolding.
  - [x] Create `.github/workflows/cargo-timings-profile.yaml` in commit `b204894`.
  - [x] Define bundled base/feature and unbundled feature timings jobs with artifact upload steps.
- [ ] Make profiling workflow executable from PR development flow.
  - [ ] Enable an execution path available before default-branch adoption (current `workflow_dispatch` on non-default-branch file is not dispatchable).
  - [ ] Choose trigger strategy (`pull_request` filter vs temporary in existing workflow) and implement.
- [ ] Produce compile timing artifacts to identify crate bottlenecks.
  - [ ] Run `cargo build --timings` for bundled base path.
  - [ ] Run `cargo build --timings` for bundled feature path.
  - [ ] Run `cargo build --timings` for unbundled feature path.
- [ ] Upload `target/cargo-timings` artifacts from profiling runs.
- [ ] Analyze timing outputs.
  - [ ] Identify top N slow crates and serial bottlenecks.
  - [ ] Identify duplicate rebuild patterns across workflow jobs.
  - [ ] Identify low-value repeated checks that can be safely reorganized.

## Phase 5 - Graph Restructure for Critical-Path Reduction

- [x] Rework bundled lint internals trial.
  - [x] Split bundled lint into parallel internal jobs (base/feature/fmt) in commit `4b6738c`.
  - [x] Add final aggregator job named exactly `Lint`.
- [ ] Stabilize bundled lint trial behavior.
  - [ ] Ensure aggregator `Lint` reports deterministic pass/fail (not `skipped`) when internal jobs fail.
  - [ ] Fix bundled feature lint linker regression (`rust-lld: unable to find library -lvsomeip3`) from run `21781185475` (`Lint (feature build+clippy)`).
  - [ ] Re-run bundled workflow to green with required check names intact.
- [ ] Optimize graph-level sharing.
  - [ ] Move shared setup work to prerequisite jobs only where payoff is clear.
  - [ ] Preserve existing vsomeip cache flow in unbundled workflow.
  - [ ] Avoid introducing fragile artifact coupling unless measured gain is clear.
- [ ] Keep required check names unchanged and green.

## Phase 6 - Validation and Comparison

- [x] Validate workflow syntax and execution (partial).
  - [x] Open/update PR and confirm workflows trigger without YAML errors (`21781185475`, `21781185484`).
  - [x] Confirm required checks appear with expected names.
- [ ] Confirm functional quality signal unchanged.
  - [ ] Both workflows green with same logical coverage intent (currently blocked by bundled feature-link regression).
  - [ ] Nightly/manual coverage workflow remains healthy.
- [ ] Publish timing comparison.
  - [ ] Before/after table for bundled and unbundled `Lint`/`Test`.
  - [ ] Include run URLs and notable cache/sccache stats.
- [ ] Add first-run critical-path comparison after Phase 5 stabilization rerun.

## Phase 7 - Rollback Strategy

- [x] Execute rollback for observed regressions in this cycle.
  - [x] Roll back step 3 (`sccache` integration) after regressions and restore stable head `71fc302`.
  - [x] Re-run CI after rollback to isolate fault source.
- [ ] If new regressions occur, revert in this order:
  1. Graph restructure changes
  2. Workspace-crate caching toggle
  3. sccache integration
  4. Cache topology changes

## Commit Chunks (Planned)

- [x] Commit 1: Rust cache topology and writer/restore policy
- [x] Commit 2: sccache integration and stats (attempted, then rolled back)
- [x] Commit 3: workspace crate caching trial (if retained) (skipped this cycle)
- [x] Commit 4: cargo timings profiling support/artifacts workflow changes
- [x] Commit 5: bundled lint graph parallelization + `Lint` aggregator (if needed)
- [ ] Commit 6: documentation/timing report updates
- [ ] Commit 7: stabilize bundled lint trial (`-lvsomeip3` fix + non-skipped `Lint` aggregator)

## Success Criteria

- [ ] Required check names unchanged and green.
- [x] Cache reservation collisions eliminated from logs.
- [ ] Measurable critical-path reduction vs current baseline.
- [ ] Clear crate-level bottleneck visibility via timings artifacts.
- [x] CI/workflow-only scope maintained.
- [ ] Bundled lint parallelization stable on PR checks (`Lint` not skipped; no `-lvsomeip3` linker failures).
