# CI Strictness-Preserving Latency Follow-Up Report

## Scope

- Branch: `perf/ci-pr-latency-reduction`
- PR: https://github.com/eclipse-uprotocol/up-streamer-rust/pull/76
- Constraints honored: CI/workflow-only changes, required check names unchanged, strict clippy flags preserved, bundled `vsomeip` lint signal preserved.

## Commit List

1. `ec4af3b` - ci: trim unbundled lint apt deps
2. `5f7e6b6` - ci: simplify bundled lint aggregator checks

## Timing Comparison

Before baseline: latest pre-follow-up required-check runs at head `9578b4d`.
After baseline: first required-check runs after mitigation (`ec4af3b`).

| Workflow | Job | Before (s) | After (s) | Delta (s) | Delta (%) | Run URL (After) |
|---|---:|---:|---:|---:|---:|---|
| Bundled | Lint | 2 | 3 | +1 | +50.0% | https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21783227987 |
| Bundled | Test | 233 | 220 | -13 | -5.6% | https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21783227987 |
| Unbundled | Lint | 104 | 73 | -31 | -29.8% | https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21783227997 |
| Unbundled | Test | 233 | 223 | -10 | -4.3% | https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21783227997 |

Variance notes (additional samples):

- Pre-change rerun sample: unbundled `Lint=82s`, `Test=236s` (https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21782749323/attempts/2)
- Post-change additional samples: unbundled `Lint=91s` (attempt 1) and `Lint=87s` (attempt 2), `Test=215s/232s` (https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21783308178)
- Bundled stability rerun after Phase C: `Lint=3s`, `Test=221s` (https://github.com/eclipse-uprotocol/up-streamer-rust/actions/runs/21783308187/attempts/2)

## Required Check Name Confirmation

Required check names remained intact throughout:

- Bundled: `Lint`, `Test`, `Build documentation`
- Unbundled: `Lint`, `Test`, `Build documentation`, `obtain_and_build_vsomeip`

## Cache Behavior Summary

- Rust cache one-writer policy preserved:
  - Bundled workflow: `lint_feature` writes; other jobs restore-only via `save-if: ${{ github.job == 'lint_feature' }}`.
  - Unbundled workflow: `lint` writes; `test`/`build-docs` restore-only via `save-if: ${{ github.job == 'lint' }}`.
- vsomeip cache behavior preserved:
  - `obtain_and_build_vsomeip` manages writer path on cache miss.
  - downstream jobs restore-only using emitted `CACHE_KEY`.
- Contention status: no `Unable to reserve cache` occurrences across all validation runs and reruns in this follow-up.

## Bottlenecks and Follow-Up Opportunities (Not Included)

- Bundled bottleneck remains `Lint (feature build+clippy)` due intentional bundled `vsomeip` rebuild/compile signal.
- Unbundled `Lint` still shows environment-driven variance in `rust-cache` restore and compile step durations despite improved dependency step behavior.
- Not included (risk/ROI tradeoff):
  1. Narrower unbundled dependency package set beyond current minimal change.
  2. Runner/image-level optimization or self-hosted runner tuning.
  3. Transport-feature partitioning redesign (out of CI-only scope).
