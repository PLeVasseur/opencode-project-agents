# Phase 5 Ergonomics Slice C Report

Date: 2026-02-10
Candidate baseline name: `ergonomics_candidate_slice_c`

## Evidence

1) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && git rev-parse --abbrev-ref HEAD && git status --short --branch`
- Exit status: 0 (pass)
- Key output:
  - `refactor/up-streamer-domain-architecture`
  - `## refactor/up-streamer-domain-architecture...origin/refactor/up-streamer-domain-architecture [ahead 3]`
- Conclusion: Slice C started on pinned branch and clean pre-change state.

2) Command: `cargo test -p up-streamer ingress_registry`
- Exit status: 0 (pass)
- Key output:
  - `test data_plane::ingress_registry::tests::duplicate_register_route_keeps_single_listener_registration ... ok`
  - `test data_plane::ingress_registry::tests::register_and_unregister_route_registers_and_unregisters_request_and_publish_filters ... ok`
- Conclusion: Ingress registry behavior remained correct after lock-scope refactor.

3) Command: `cargo test -p up-streamer --test single_local_two_remote_add_remove_rules`
- Exit status: 0 (pass)
- Key output:
  - `test single_local_two_remote_add_remove_rules ... ok`
- Conclusion: Route add/remove correctness remained intact.

4) Command: `cargo test -p configurable-streamer`
- Exit status: 0 (pass)
- Key output:
  - `Running unittests src/main.rs`
  - `test result: ok. 0 passed; 0 failed`
- Conclusion: Configurable streamer binary crate compiles/tests successfully with explicit error-path handling changes.

5) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && export BENCH_PIN_PREFIX="taskset -c 2" && export CRITERION_ARGS="--sample-size 60 --warm-up-time 3 --measurement-time 12 --noise-threshold 0.02" && $BENCH_PIN_PREFIX cargo bench -p up-streamer --bench streamer_criterion -- $CRITERION_ARGS --save-baseline ergonomics_candidate_slice_c`
- Exit status: 0 (pass)
- Key output:
  - `Benchmarking ingress_registry/register_route`
  - `Benchmarking ingress_registry/unregister_route`
- Conclusion: Slice C candidate snapshot generated for threshold evaluation.

6) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && cargo run -p criterion-guardrail -- --criterion-root target/criterion --baseline ergonomics_baseline --candidate ergonomics_candidate_slice_c --throughput-threshold-pct 3 --latency-threshold-pct 5 --alloc-proxy-threshold-pct 5 --report "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/05-slice-c-guardrail.json"`
- Exit status: non-zero (first attempt)
- Key output:
  - `ingress_registry/unregister_route ... 5.263% ... FAIL`
  - `criterion-guardrail: FAIL (threshold breach)`
- Conclusion: Initial Slice C guardrail breached throughput threshold on `ingress_registry/unregister_route`; rerun policy invoked.

7) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && export BENCH_PIN_PREFIX="taskset -c 2" && export CRITERION_ARGS="--sample-size 60 --warm-up-time 3 --measurement-time 12 --noise-threshold 0.02" && $BENCH_PIN_PREFIX cargo bench -p up-streamer --bench streamer_criterion -- $CRITERION_ARGS --save-baseline ergonomics_candidate_slice_c_rerun`
- Exit status: 0 (pass)
- Key output:
  - `Benchmarking ingress_registry/register_route`
  - `Benchmarking ingress_registry/unregister_route`
- Conclusion: Required one-time rerun baseline generated per flakiness policy.

8) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && cargo run -p criterion-guardrail -- --criterion-root target/criterion --baseline ergonomics_baseline --candidate ergonomics_candidate_slice_c_rerun --throughput-threshold-pct 3 --latency-threshold-pct 5 --alloc-proxy-threshold-pct 5 --report "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/ergonomics_candidate_slice_c-guardrail-rerun.json"`
- Exit status: 0 (pass)
- Key output:
  - `ingress_registry/unregister_route ... 2.123% ... PASS`
  - `criterion-guardrail: PASS`
- Conclusion: Slice C passes thresholds after mandated rerun; progression gate remains open.

9) Command: `git status --short --branch`
- Exit status: 0 (pass)
- Key output:
  - `M configurable-streamer/src/main.rs`
  - `M up-streamer/src/data_plane/ingress_registry.rs`
- Conclusion: Slice C scope is constrained to required async/error ergonomics touch points.

10) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && git rev-parse --abbrev-ref HEAD && git status --short --branch`
- Exit status: 0 (pass)
- Key output:
  - `refactor/up-streamer-domain-architecture`
  - `M configurable-streamer/src/main.rs`
  - `M up-streamer/src/data_plane/ingress_registry.rs`
- Conclusion: Pre-commit branch pin and slice scope verified for Commit D.

11) Command: `git add configurable-streamer/src/main.rs up-streamer/src/data_plane/ingress_registry.rs && git diff --name-only --cached && git diff --stat --cached`
- Exit status: 0 (pass)
- Key output:
  - `configurable-streamer/src/main.rs`
  - `up-streamer/src/data_plane/ingress_registry.rs`
  - `2 files changed, 124 insertions(+), 79 deletions(-)`
- Conclusion: Commit D staging is constrained to Slice C required files.

12) Command: `git diff --name-only --cached | rg -n '^(plans|prompts|reports)/' || true`
- Exit status: 0 (pass)
- Key output:
  - no matches
- Conclusion: No repo-local OPENCODE artifact paths staged for Commit D.

13) Command: `git commit -m "refactor: narrow ingress registry locks and explicit config errors"`
- Exit status: 0 (pass)
- Key output:
  - `[refactor/up-streamer-domain-architecture 2440388] refactor: narrow ingress registry locks and explicit config errors`
- Conclusion: Commit D created with async/ownership and runtime error-path ergonomics scope.

14) Command: `git status --short --branch`
- Exit status: 0 (pass)
- Key output:
  - `## refactor/up-streamer-domain-architecture...origin/refactor/up-streamer-domain-architecture [ahead 4]`
- Conclusion: Post-commit state is clean and branch remains pinned.

## Ergonomics outcomes

- Removed lock-held-across-`.await` in ingress registry register/unregister flows via two-phase lock/update and post-lock transport operations.
- Preserved listener rollback behavior while handling race-on-insert safely without holding mutex guards over I/O-like transport calls.
- Replaced runtime `unwrap/expect` usage in configurable-streamer startup/forwarding paths with explicit `UStatus` error propagation and validation.

## Phase 5 result

PASS (after required rerun) - Async/ownership and runtime error-path ergonomics improved with guardrail thresholds satisfied.
