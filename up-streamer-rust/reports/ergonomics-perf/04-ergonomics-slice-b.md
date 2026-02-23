# Phase 4 Ergonomics Slice B Report

Date: 2026-02-10
Candidate baseline name: `ergonomics_candidate_slice_b`

## Evidence

1) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && git rev-parse --abbrev-ref HEAD && git status --short --branch`
- Exit status: 0 (pass)
- Key output:
  - `refactor/up-streamer-domain-architecture`
  - `## refactor/up-streamer-domain-architecture...origin/refactor/up-streamer-domain-architecture [ahead 2]`
- Conclusion: Slice B started on pinned branch with clean pre-change status.

2) Command: `cargo test -p up-streamer route_lifecycle`
- Exit status: 0 (pass)
- Key output:
  - `test control_plane::route_lifecycle::tests::add_route_error_exposes_display_and_source_for_ingress_failure ... ok`
  - `test control_plane::route_lifecycle::tests::remove_route_error_display_is_stable_for_not_found ... ok`
- Conclusion: Route lifecycle control-plane behavior remained correct after composition/lifetime changes.

3) Command: `cargo test -p up-streamer publish_resolution`
- Exit status: 0 (pass)
- Key output:
  - `test routing::publish_resolution::tests::resolver_allows_wildcard_topic_authority ... ok`
  - `test routing::publish_resolution::tests::resolver_dedupes_sources_across_subscribers ... ok`
- Conclusion: Publish resolution logic remained correct after resolver refactor.

4) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && export BENCH_PIN_PREFIX="taskset -c 2" && export CRITERION_ARGS="--sample-size 60 --warm-up-time 3 --measurement-time 12 --noise-threshold 0.02" && $BENCH_PIN_PREFIX cargo bench -p up-streamer --bench streamer_criterion -- $CRITERION_ARGS --save-baseline ergonomics_candidate_slice_b`
- Exit status: 0 (pass)
- Key output:
  - `Benchmarking routing_lookup/wildcard_authority`
  - `Benchmarking ingress_registry/register_route`
  - `Benchmarking egress_forwarding/single_route_dispatch`
- Conclusion: Slice B candidate snapshot generated with canonical benchmark command/arguments.

5) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && cargo run -p criterion-guardrail -- --criterion-root target/criterion --baseline ergonomics_baseline --candidate ergonomics_candidate_slice_b --throughput-threshold-pct 3 --latency-threshold-pct 5 --alloc-proxy-threshold-pct 5 --report "$OPENCODE_CONFIG_DIR/reports/ergonomics-perf/bench-data/04-slice-b-guardrail.json"`
- Exit status: 0 (pass)
- Key output:
  - `ingress_registry/register_route ... 0.944% ... PASS`
  - `ingress_registry/unregister_route ... 1.978% ... PASS`
  - `criterion-guardrail: PASS`
- Conclusion: Slice B stayed within all guardrail thresholds.

6) Command: `git status --short --branch`
- Exit status: 0 (pass)
- Key output:
  - `M up-streamer/src/control_plane/route_lifecycle.rs`
  - `M up-streamer/src/routing/publish_resolution.rs`
  - `M up-streamer/src/data_plane/ingress_registry.rs`
- Conclusion: Slice B scope aligns with required modules and directly related internal call paths.

7) Command: `export EXEC_BRANCH="refactor/up-streamer-domain-architecture" && test "$(git rev-parse --abbrev-ref HEAD)" = "$EXEC_BRANCH" && git rev-parse --abbrev-ref HEAD && git status --short --branch`
- Exit status: 0 (pass)
- Key output:
  - `refactor/up-streamer-domain-architecture`
  - `M up-streamer/src/control_plane/route_lifecycle.rs`
  - `M up-streamer/src/routing/publish_resolution.rs`
- Conclusion: Pre-commit branch pin and scope validated for Commit C.

8) Command: `git add up-streamer/src/control_plane/route_lifecycle.rs up-streamer/src/routing/publish_resolution.rs up-streamer/src/data_plane/ingress_registry.rs up-streamer/src/ustreamer.rs up-streamer/src/benchmark_support.rs && git diff --name-only --cached && git diff --stat --cached`
- Exit status: 0 (pass)
- Key output:
  - staged files limited to Slice B touched internals and call-site adapters
  - `5 files changed, 80 insertions(+), 77 deletions(-)`
- Conclusion: Commit C contains only composition/lifetime simplification scope.

9) Command: `git diff --name-only --cached | rg -n '^(plans|prompts|reports)/' || true`
- Exit status: 0 (pass)
- Key output:
  - no matches
- Conclusion: No OPENCODE repo-local artifact paths staged in Commit C.

10) Command: `git commit -m "refactor: simplify route lifecycle and publish resolver composition"`
- Exit status: 0 (pass)
- Key output:
  - `[refactor/up-streamer-domain-architecture e8e5fb5] refactor: simplify route lifecycle and publish resolver composition`
- Conclusion: Commit C created with slice-specific composition/lifetime scope.

11) Command: `git status --short --branch`
- Exit status: 0 (pass)
- Key output:
  - `## refactor/up-streamer-domain-architecture...origin/refactor/up-streamer-domain-architecture [ahead 3]`
- Conclusion: Post-commit worktree remains clean and branch pin unchanged.

## Ergonomics outcomes

- `RouteLifecycle` now narrows mutable `EgressRoutePool` borrowing to per-call method arguments instead of struct-wide state.
- `PublishRouteResolver` now uses stateless associated functions, removing resolver lifetime-carrying state and simplifying composition.
- Ingress registry and benchmark support call paths now consume the stateless resolver API, reducing transient coordinator object wiring.

## Phase 4 result

PASS - Composition/lifetime simplification landed with behavior parity and no guardrail threshold breach.
