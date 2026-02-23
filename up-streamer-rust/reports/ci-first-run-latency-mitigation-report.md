# CI First-Run Latency Mitigation Report

## Scope

- Branch: `perf/ci-pr-latency-reduction`
- PR: https://github.com/eclipse-uprotocol/up-streamer-rust/pull/76
- Runtime/code behavior changes: none (CI/workflow only)

## Run URLs

### Baseline reference runs

- Bundled required checks: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21781569522
- Unbundled required checks: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21781569519
- Cargo timings profile baseline: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21781569523

### Phase B runs (OpenSSL no-vendor)

- Bundled required checks: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21782412142
- Unbundled required checks: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21782412137
- Cargo timings profile: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21782412143

### Phase C runs (bundled lint de-dup)

- Bundled required checks: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21782569999
- Unbundled required checks: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21782570005
- Cargo timings profile: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21782569995

### Phase D runs (vsomeip stability/cache hygiene)

- Bundled required checks: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21782749327
- Bundled rerun (stability gate, attempt 2): https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21782749327/attempts/2
- Unbundled required checks: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21782749323
- Cargo timings profile: https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21782749332

## Required Check Durations (Before vs After)

| Workflow | Job | Before (s) | After (s) | Delta (s) | Delta (%) | Run URL (After) |
|---|---:|---:|---:|---:|---:|---|
| Bundled | Lint | 8 | 2 | -6 | -75.0% | https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21782749327/attempts/2 |
| Bundled | Test | 270 | 233 | -37 | -13.7% | https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21782749327/attempts/2 |
| Unbundled | Lint | 75 | 104 | +29 | +38.7% | https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21782749323 |
| Unbundled | Test | 291 | 233 | -58 | -19.9% | https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21782749323 |

## Bundled Lint Shard Durations (Before vs After)

| Job | Before (s) | After (s) | Delta (s) |
|---|---:|---:|---:|
| Lint (base build+clippy) | 78 | 83 | +5 |
| Lint (feature build+clippy) | 328 | 173 | -155 |
| Lint (fmt) | 7 | 9 | +2 |
| Lint (aggregator) | 8 | 2 | -6 |

## Cache Behavior Summary

### Rust cache writer/restore policy

- Bundled workflow (`Lint and Test - Bundled`): single writer remains `lint_feature` (`save-if: github.job == 'lint_feature'`); `lint_base`, `test`, and `build-docs` restore-only.
- Unbundled workflow (`Lint and Test - Unbundled`): single writer remains `lint` (`save-if: github.job == 'lint'`); `test` and `build-docs` restore-only.

### vsomeip cache writer/restore policy

- `obtain_and_build_vsomeip` is the writer when cache miss occurs.
- Consumer jobs (`lint`, `test`, `build-docs`, and timings consumers) restore-only.

### Contention status

- `Unable to reserve cache`: not found in inspected logs for Phase B/C/D bundled, unbundled, or timings runs.

## Cargo Timings Bottleneck Summary

### Baseline (from run `21781569523`)

- Bundled base total `224.7s`; `openssl-sys build script (run)` was `101.9s` (~45.3%).
- Bundled feature total `229.5s`; `vsomeip-sys build script (run)` was `128.4s` (~55.9%).
- Unbundled feature total `254.1s`; `openssl-sys build script (run)` was `116.8s` (~46.0%).

### Final (from run `21782749332` artifacts)

- Bundled base total `148.5s`; top units:
  - `stabby-abi` `26.2s` (17.6%)
  - `zenoh` `17.6s` (11.9%)
  - `zenoh-config` `11.8s` (7.9%)
  - `zenoh-transport` `10.8s` (7.3%)
  - `bollard-stubs` `10.2s` (6.8%)
  - `openssl-sys build script (run)` `0.1s` (~0.0%)
- Bundled feature total `236.0s`; top units:
  - `vsomeip-sys build script (run)` `129.5s` (54.9%)
  - `zenoh` `29.8s` (12.6%)
  - `stabby-abi` `26.2s` (11.1%)
  - `up-transport-vsomeip` `14.2s` (6.0%)
  - `zenoh-config` `11.9s` (5.0%)
- Unbundled feature total `183.9s`; top units:
  - `zenoh` `29.4s` (16.0%)
  - `stabby-abi` `26.3s` (14.3%)
  - `up-transport-vsomeip` `20.0s` (10.9%)
  - `vsomeip-sys build script (run)` `14.2s` (7.7%)
  - `zenoh-config` `11.8s` (6.4%)
  - `openssl-sys build script (run)` `0.1s` (~0.0%)

## Follow-Up Opportunities (Not Included)

- Reduce bundled `vsomeip-sys` CMake compile dominance (still ~55% of bundled feature profile).
- Evaluate whether `Lint` required-check wall time can be represented without a thin aggregator if branch-protection constraints permit.
- Investigate unbundled `Lint` regression (`+29s`) driven by dependency install + cold compile variance while preserving strict signal.
