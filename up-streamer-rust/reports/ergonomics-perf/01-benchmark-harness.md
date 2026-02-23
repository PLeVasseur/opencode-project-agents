# Phase 1 Benchmark Harness Report

Date: 2026-02-10
Criterion pin: `0.5.1` with `csv_output` feature enabled for `raw.csv` generation.

## Evidence

1) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && git rev-parse --abbrev-ref HEAD && git status --short --branch`
- Exit status: 0 (pass)
- Key output:
  - `refactor/up-streamer-domain-architecture`
  - `## refactor/up-streamer-domain-architecture...origin/refactor/up-streamer-domain-architecture`
- Conclusion: Phase 1 started on the pinned execution branch with no pre-existing worktree drift.

2) Command: `cargo test -p criterion-guardrail`
- Exit status: 0 (pass)
- Key output:
  - `running 5 tests`
  - `test result: ok. 5 passed; 0 failed`
  - `test checked_in_fixture_tree_supports_direct_and_fallback_layouts ... ok`
- Conclusion: Guardrail CLI unit + fixture coverage is green (parse success, missing input, threshold breach, pass case, schema checks, fixture-tree parser).

3) Command: `cargo check -p up-streamer --bench streamer_criterion`
- Exit status: 0 (pass)
- Key output:
  - `Checking up-streamer v0.1.0 (.../up-streamer)`
  - `Finished 'dev' profile ...`
- Conclusion: Criterion benchmark target compiles successfully.

4) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && cargo run -p criterion-guardrail -- --criterion-root target/criterion --baseline ergonomics_smoke_base --candidate ergonomics_smoke_candidate --throughput-threshold-pct 3 --latency-threshold-pct 5 --alloc-proxy-threshold-pct 5 --report "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/01-guardrail-smoke.json"`
- Exit status: non-zero (expected failure during first attempt)
- Key output:
  - `missing required benchmark IDs ... missing baseline CSV ... missing candidate CSV`
- Conclusion: Initial smoke guardrail failed because Criterion `raw.csv` artifacts were not generated; remediation required enabling Criterion `csv_output`.

5) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && export BENCH_PIN_PREFIX="taskset -c 2" && export CRITERION_ARGS="--sample-size 60 --warm-up-time 3 --measurement-time 12 --noise-threshold 0.02" && $BENCH_PIN_PREFIX cargo bench -p up-streamer --bench streamer_criterion -- $CRITERION_ARGS --save-baseline ergonomics_smoke_base`
- Exit status: 0 (pass)
- Key output:
  - `Benchmarking routing_lookup/exact_authority`
  - `Benchmarking ingress_registry/register_route`
  - `Benchmarking egress_forwarding/single_route_dispatch`
- Conclusion: Smoke baseline benchmark run completed with canonical command/arguments.

6) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && export BENCH_PIN_PREFIX="taskset -c 2" && export CRITERION_ARGS="--sample-size 60 --warm-up-time 3 --measurement-time 12 --noise-threshold 0.02" && $BENCH_PIN_PREFIX cargo bench -p up-streamer --bench streamer_criterion -- $CRITERION_ARGS --save-baseline ergonomics_smoke_candidate`
- Exit status: 0 (pass)
- Key output:
  - `Benchmarking routing_lookup/wildcard_authority`
  - `Benchmarking publish_resolution/source_filter_derivation`
  - `Benchmarking ingress_registry/unregister_route`
- Conclusion: Smoke candidate benchmark run completed with canonical command/arguments.

7) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && cargo run -p criterion-guardrail -- --help`
- Exit status: 0 (pass)
- Key output:
  - `Usage: criterion-guardrail --criterion-root ... --report ...`
- Conclusion: Guardrail CLI contract is available and callable.

8) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && cargo run -p criterion-guardrail -- --criterion-root target/criterion --baseline ergonomics_smoke_base --candidate ergonomics_smoke_candidate --throughput-threshold-pct 3 --latency-threshold-pct 5 --alloc-proxy-threshold-pct 5 --report "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/01-guardrail-smoke.json"`
- Exit status: 0 (pass)
- Key output:
  - `ingress_registry/register_route ... result PASS`
  - `ingress_registry/unregister_route ... result PASS`
  - `criterion-guardrail: PASS`
- Conclusion: Smoke comparison passes all configured thresholds and writes JSON report artifact.

9) Command: `ls "target/criterion/routing_lookup/exact_authority/ergonomics_smoke_base/raw.csv" "target/criterion/routing_lookup/exact_authority/ergonomics_smoke_candidate/raw.csv"`
- Exit status: 0 (pass)
- Key output:
  - `target/criterion/routing_lookup/exact_authority/ergonomics_smoke_base/raw.csv`
  - `target/criterion/routing_lookup/exact_authority/ergonomics_smoke_candidate/raw.csv`
- Conclusion: Criterion raw exports are present under `target/criterion` and parseable by the guardrail CLI.

10) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && git rev-parse --abbrev-ref HEAD && git status --short --branch`
- Exit status: 0 (pass)
- Key output:
  - `refactor/up-streamer-domain-architecture`
  - `M Cargo.lock` ... `?? utils/criterion-guardrail/`
- Conclusion: Pre-commit branch pin and staged-scope preparation snapshot recorded.

11) Command: `git add Cargo.toml Cargo.lock "scripts/bench_streamer_criterion.sh" up-streamer/Cargo.toml up-streamer/README.md up-streamer/benches/streamer_criterion.rs up-streamer/src/lib.rs up-streamer/src/benchmark_support.rs utils/criterion-guardrail && git diff --name-only --cached && git diff --stat --cached`
- Exit status: 0 (pass)
- Key output:
  - staged files limited to harness/script/docs/guardrail crate paths
  - `24 files changed, 1524 insertions(+)`
- Conclusion: Commit A staging scope includes only benchmark-harness and guardrail foundation changes.

12) Command: `git diff --name-only --cached | rg -n '^(plans|prompts|reports)/' || true`
- Exit status: 0 (pass)
- Key output:
  - no matches
- Conclusion: No repo-local OPENCODE artifact paths were staged.

13) Command: `git commit -m "feat: add Criterion harness and guardrail CLI foundation"`
- Exit status: 0 (pass)
- Key output:
  - `[refactor/up-streamer-domain-architecture 2043298] feat: add Criterion harness and guardrail CLI foundation`
- Conclusion: Commit A created with the required harness-only scope.

14) Command: `git status --short --branch`
- Exit status: 0 (pass)
- Key output:
  - `## refactor/up-streamer-domain-architecture...origin/refactor/up-streamer-domain-architecture [ahead 1]`
- Conclusion: Post-commit state is clean and branch remains pinned.

## Phase 1 result

PASS - Benchmark harness, canonical script, guardrail CLI, parser fixtures/tests, and smoke validation flow are operational.
