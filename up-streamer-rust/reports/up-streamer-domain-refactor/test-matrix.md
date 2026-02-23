# Test Matrix

Date: 2026-02-09
Executor: OpenCode (gpt-5.3-codex)

## Purpose

Map each domain layer/concept to robust tests and verification commands.

## Layer Coverage Matrix

| Layer | Concept | Test type | Test location(s) | Command(s) | Status |
|---|---|---|---|---|---|
| API Facade | add/delete rule contract, same-authority rejection, duplicate/missing semantics | API contract | `up-streamer/tests/api_contract_forwarding_rules.rs`, `up-streamer/src/ustreamer.rs` | `cargo test -p up-streamer -- --nocapture` | pass |
| Control Plane | route lifecycle insert/remove idempotency + transport identity keying + rollback | unit/component | `up-streamer/src/control_plane/route_lifecycle.rs`, `up-streamer/src/control_plane/route_table.rs`, `up-streamer/src/ustreamer.rs` | `cargo test -p up-streamer -- --nocapture` | pass |
| Routing | publish source derivation, wildcard authority handling, dedupe, tuple strictness | unit | `up-streamer/src/routing/publish_resolution.rs`, `up-streamer/src/ustreamer.rs` | `cargo test -p up-streamer -- --nocapture` | pass |
| Data Plane | ingress register/unregister symmetry + egress pool refcount lifecycle | unit/component | `up-streamer/src/data_plane/ingress_registry.rs`, `up-streamer/src/data_plane/egress_pool.rs`, `up-streamer/src/ustreamer.rs` | `cargo test -p up-streamer -- --nocapture` | pass |
| Runtime | worker runtime + subscription runtime behavior exercised through crate and workspace tests | component/integration | `up-streamer/src/runtime/*.rs`, `up-streamer/tests/*.rs` | `cargo test -p up-streamer -- --nocapture`, `cargo test --workspace` | pass |
| Integration | end-to-end forwarding scenarios and failure-path behavior | integration | `up-streamer/tests/single_local_*.rs`, `up-streamer/tests/usubscription.rs` | `cargo test -p up-streamer -- --nocapture`, `cargo test --workspace` | pass |

## Existing Test Relocation Map

| Existing test path/name | New path/name | Reason | Behavior preserved |
|---|---|---|---|
| `ustreamer::tests::publish_filter_*` | `routing::publish_resolution::tests::*` (retained original + new focused unit tests) | add deterministic routing-policy ownership at routing module boundary without dropping baseline tests | yes |
| `ustreamer::tests::add_forwarding_rule_*`/`delete_forwarding_rule` scenarios | `up-streamer/tests/api_contract_forwarding_rules.rs` (additional dedicated API contract tests) | isolate outward API contract checks from broader internal behavior tests | yes |
| `integration_test_utils::UPClientFoo` listener wrapping calls | `utils/integration-test-utils/src/up_client_foo.rs` helper `comparable_listener` | reduce duplication in mock listener wrapping while preserving behavior | yes |

## Robustness Checklist

- [x] Deterministic tests for key policies/invariants.
- [x] Component tests for module interactions.
- [x] API contract tests for outward surface.
- [x] Integration tests for end-to-end behavior.
- [x] Doctests for public conceptual examples.

## Hardening Follow-Up Status

- [x] Phase 4 objective validator passes (test readability/refactor checks).
- [x] In-file tests in `up-streamer/src/ustreamer.rs` are sufficiently reduced after extraction.
- [x] No placeholder relocation rows remain in test mapping artifacts.

## Command Summary

```text
cargo test -p up-streamer -- --nocapture -> PASS (11 unit + 6 integration + 2 API-contract integration tests; 1 existing ignored integration)
cargo test -p up-streamer --doc -> PASS (8 doctests total: 3 passed, 5 ignored layer fences)
cargo test -p subscription-cache -- --nocapture -> PASS (3 tests)
cargo test -p integration-test-utils -- --nocapture -> PASS (0 tests, crate/build/doc clean)
cargo test --workspace -> PASS
python3 "$OPENCODE_CONFIG_DIR/scripts/up_streamer_refactor_autopilot.py" --project-dir /home/pete.levasseur/eclipse/uprotocol/up-streamer-rust --start-phase 4 --end-phase 4 --validate-only -> PASS (0 blockers)
```
