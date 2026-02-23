# Phase 2 Baseline Report

Date: 2026-02-10
Baseline name: `ergonomics_baseline`

## Evidence

1) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && git rev-parse --abbrev-ref HEAD && git status --short --branch`
- Exit status: 0 (pass)
- Key output:
  - `refactor/up-streamer-domain-architecture`
  - `## refactor/up-streamer-domain-architecture...origin/refactor/up-streamer-domain-architecture [ahead 1]`
- Conclusion: Phase 2 started on pinned branch with no unstaged repository drift.

2) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && export BENCH_PIN_PREFIX="taskset -c 2" && export CRITERION_ARGS="--sample-size 60 --warm-up-time 3 --measurement-time 12 --noise-threshold 0.02" && $BENCH_PIN_PREFIX cargo bench -p up-streamer --bench streamer_criterion -- $CRITERION_ARGS --save-baseline ergonomics_baseline`
- Exit status: 0 (pass)
- Key output:
  - `Benchmarking routing_lookup/exact_authority`
  - `Benchmarking ingress_registry/register_route`
  - `Benchmarking egress_forwarding/single_route_dispatch`
- Conclusion: Canonical baseline snapshot run completed with pinned arguments and CPU pinning.

3) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && export BENCH_PIN_PREFIX="taskset -c 2" && export CRITERION_ARGS="--sample-size 60 --warm-up-time 3 --measurement-time 12 --noise-threshold 0.02" && $BENCH_PIN_PREFIX cargo bench -p up-streamer --bench streamer_criterion -- $CRITERION_ARGS --output-format bencher | tee "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/criterion-baseline-bencher.txt"`
- Exit status: 0 (pass)
- Key output:
  - `test routing_lookup/exact_authority ... bench:       62104 ns/iter (+/- 1357)`
  - `test ingress_registry/register_route ... bench:     1107409 ns/iter (+/- 62911)`
  - `test egress_forwarding/single_route_dispatch ... bench:         234 ns/iter (+/- 2)`
- Conclusion: Optional human-readable bencher export captured under bench-data for quick diff readability.

4) Command: `export BASELINE_ROOT="$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/baseline" && mkdir -p "$BASELINE_ROOT/routing_lookup/exact_authority" "$BASELINE_ROOT/routing_lookup/wildcard_authority" "$BASELINE_ROOT/publish_resolution/source_filter_derivation" "$BASELINE_ROOT/ingress_registry/register_route" "$BASELINE_ROOT/ingress_registry/unregister_route" "$BASELINE_ROOT/egress_forwarding/single_route_dispatch" && cp -a "target/criterion/routing_lookup/exact_authority/ergonomics_baseline" "$BASELINE_ROOT/routing_lookup/exact_authority/" && cp -a "target/criterion/routing_lookup/wildcard_authority/ergonomics_baseline" "$BASELINE_ROOT/routing_lookup/wildcard_authority/" && cp -a "target/criterion/publish_resolution/source_filter_derivation/ergonomics_baseline" "$BASELINE_ROOT/publish_resolution/source_filter_derivation/" && cp -a "target/criterion/ingress_registry/register_route/ergonomics_baseline" "$BASELINE_ROOT/ingress_registry/register_route/" && cp -a "target/criterion/ingress_registry/unregister_route/ergonomics_baseline" "$BASELINE_ROOT/ingress_registry/unregister_route/" && cp -a "target/criterion/egress_forwarding/single_route_dispatch/ergonomics_baseline" "$BASELINE_ROOT/egress_forwarding/single_route_dispatch/"`
- Exit status: 0 (pass)
- Key output:
  - command completed without copy errors
- Conclusion: Baseline artifact copy exists under `$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/baseline/` for offline review and reproducibility.

5) Command: `rustc -Vv && cargo -V && lscpu && date -Is`
- Exit status: 0 (pass)
- Key output:
  - `rustc 1.92.0 (ded5c06cf 2025-12-08)`
  - `cargo 1.92.0 (344c4567c 2025-10-21)`
  - `Model name: VirtualApple @ 2.50GHz`
  - `2026-02-10T20:17:59+09:00`
- Conclusion: Environment snapshot recorded for baseline cycle reproducibility.

6) Command: `cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor`
- Exit status: 0 (pass)
- Key output:
  - `performance`
- Conclusion: CPU governor already set to `performance`; no constrained-run notation required for this baseline cycle.

## Phase 2 result

PASS - Baseline artifacts are locked under `ergonomics_baseline` and copied into OPENCODE report storage for all required benchmark IDs.
