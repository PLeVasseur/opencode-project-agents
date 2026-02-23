# Phase 3 Ergonomics Slice A Report

Date: 2026-02-10
Candidate baseline name: `ergonomics_candidate_slice_a`

## Evidence

1) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && git rev-parse --abbrev-ref HEAD && git status --short --branch`
- Exit status: 0 (pass)
- Key output:
  - `refactor/up-streamer-domain-architecture`
  - `## refactor/up-streamer-domain-architecture...origin/refactor/up-streamer-domain-architecture [ahead 1]`
- Conclusion: Slice A executed from pinned branch and clean pre-change status.

2) Command: `cargo test -p up-streamer --test api_contract_forwarding_rules`
- Exit status: 0 (pass)
- Key output:
  - `test add_delete_route_contract_duplicate_and_missing_rules ... ok`
  - `test add_delete_route_contract_rejects_same_authority ... ok`
- Conclusion: Route API contract behavior remains correct.

3) Command: `cargo test -p up-streamer --test usubscription`
- Exit status: 0 (pass)
- Key output:
  - `test usubscription_bad_data ... ok`
- Conclusion: Subscription-related behavior remains stable.

4) Command: `cargo test -p up-streamer --test single_local_single_remote`
- Exit status: 0 (pass)
- Key output:
  - `test single_local_single_remote ... ok`
- Conclusion: Single-route forwarding scenario still passes end-to-end.

5) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && export BENCH_PIN_PREFIX="taskset -c 2" && export CRITERION_ARGS="--sample-size 60 --warm-up-time 3 --measurement-time 12 --noise-threshold 0.02" && $BENCH_PIN_PREFIX cargo bench -p up-streamer --bench streamer_criterion -- $CRITERION_ARGS --save-baseline ergonomics_candidate_slice_a`
- Exit status: 0 (pass)
- Key output:
  - `Benchmarking routing_lookup/exact_authority`
  - `Benchmarking ingress_registry/register_route`
  - `Benchmarking egress_forwarding/single_route_dispatch`
- Conclusion: Slice A candidate benchmark snapshot generated with canonical benchmark command.

6) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && cargo run -p criterion-guardrail -- --criterion-root target/criterion --baseline ergonomics_baseline --candidate ergonomics_candidate_slice_a --throughput-threshold-pct 3 --latency-threshold-pct 5 --alloc-proxy-threshold-pct 5 --report "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/03-slice-a-guardrail.json"`
- Exit status: 0 (pass)
- Key output:
  - `ingress_registry/register_route ... -1.397% ... PASS`
  - `ingress_registry/unregister_route ... 1.191% ... PASS`
  - `criterion-guardrail: PASS`
- Conclusion: Slice A is within configured throughput/latency/allocation proxy thresholds.

7) Command: `git status --short --branch`
- Exit status: 0 (pass)
- Key output:
  - `M configurable-streamer/src/main.rs`
  - `M up-streamer/src/ustreamer.rs`
- Conclusion: Slice A scope is contained to required API and call-site touch points.

8) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && git rev-parse --abbrev-ref HEAD && git status --short --branch`
- Exit status: 0 (pass)
- Key output:
  - `refactor/up-streamer-domain-architecture`
  - `M configurable-streamer/src/main.rs`
  - `M up-streamer/src/ustreamer.rs`
- Conclusion: Pre-commit branch pin and change scope verified for Commit B.

9) Command: `git add configurable-streamer/src/main.rs up-streamer/src/ustreamer.rs && git diff --name-only --cached && git diff --stat --cached`
- Exit status: 0 (pass)
- Key output:
  - `configurable-streamer/src/main.rs`
  - `up-streamer/src/ustreamer.rs`
  - `2 files changed, 28 insertions(+), 10 deletions(-)`
- Conclusion: Commit B staging is limited to Slice A touch points.

10) Command: `git diff --name-only --cached | rg -n '^(plans|prompts|reports)/' || true`
- Exit status: 0 (pass)
- Key output:
  - no matches
- Conclusion: No repo-local OPENCODE artifact paths staged for Commit B.

11) Command: `git commit -m "refactor: add borrowed route APIs for ergonomic call sites"`
- Exit status: 0 (pass)
- Key output:
  - `[refactor/up-streamer-domain-architecture cae6282] refactor: add borrowed route APIs for ergonomic call sites`
- Conclusion: Commit B created with compatibility-preserving API ergonomics scope.

12) Command: `git status --short --branch`
- Exit status: 0 (pass)
- Key output:
  - `## refactor/up-streamer-domain-architecture...origin/refactor/up-streamer-domain-architecture [ahead 2]`
- Conclusion: Post-commit worktree is clean and branch pin remains valid.

## Ergonomics outcomes

- Added compatibility-preserving borrowed APIs: `add_route_ref` and `delete_route_ref`.
- Kept existing owned APIs (`add_route`, `delete_route`) and delegated them to borrowed variants.
- Updated `configurable-streamer` forwarding setup to call borrowed APIs directly and avoid endpoint cloning.

## Phase 3 result

PASS - Slice A API ergonomics landed with compatibility preserved and no guardrail threshold breach.
