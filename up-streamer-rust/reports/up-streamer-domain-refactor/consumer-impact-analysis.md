# Consumer Impact Analysis

Date: 2026-02-09
Executor: OpenCode (gpt-5.3-codex)

## Purpose

Track impact on workspace crates that consume `up-streamer` and ensure compatibility.

## Consumer Inventory

| Consumer crate | Usage summary (`Endpoint`/`UStreamer`) | Impact expectation | Required change? | Notes |
|---|---|---|---|---|
| `configurable-streamer` | Constructs one `UStreamer`, builds endpoint map, applies forwarding rules from config | minimal | no (expected) | Depends on stable `Endpoint::new` and `UStreamer::{new,add_forwarding_rule}` signatures. |
| `example-streamer-implementations` | Constructs one `UStreamer`, creates host/someip endpoints, installs two directional rules | minimal | no (expected) | Typical two-endpoint bridge usage; sensitive mainly to API signature drift. |
| `up-linux-streamer-plugin` | Constructs `UStreamer` in plugin run task, creates host/mechatronics endpoints, installs bidirectional rules | minimal | no (expected) | Highest sensitivity to logging/subscriber-init boundary changes, not API shape. |
| `utils/integration-test-utils` | No direct `Endpoint`/`UStreamer` usage in crate source; provides transport/listener test harnesses | none | no | Indirect compatibility surface via `up-streamer` integration tests. |

## Compilation Validation

- [x] `cargo check -p configurable-streamer`
- [x] `cargo check -p example-streamer-implementations`
- [x] `cargo check -p up-linux-streamer-plugin`
- [x] `cargo check -p integration-test-utils`

### Results

```text
PASS: cargo check -p configurable-streamer
PASS: cargo check -p up-linux-streamer-plugin
PASS: cargo check -p integration-test-utils
PASS (command adaptation): cargo check --manifest-path example-streamer-implementations/Cargo.toml

Adaptation rationale: workspace package id for `example-streamer-implementations` is `up-linux-streamer`
(declared in `example-streamer-implementations/Cargo.toml`), so `cargo check -p example-streamer-implementations`
does not resolve. Manifest-path check validates the intended consumer crate without code changes.

Optional non-gating probe (feature-heavy): `cargo check -p up-linux-streamer --features zenoh-transport,vsomeip-transport,bundled-vsomeip`
did not complete due local `vsomeip-sys` build-env requirement (`generic C++ stdlib path` not provided). This does not affect Gate 6,
which requires the listed consumer compile checks and minimal adaptation only.
```

## Revalidation (Attempt 1/3)

```text
PASS: cargo check -p configurable-streamer
PASS: cargo check -p up-linux-streamer-plugin
PASS: cargo check -p integration-test-utils
FAIL (expected package-id mismatch): cargo check -p example-streamer-implementations
PASS (minimal command adaptation): cargo check --manifest-path example-streamer-implementations/Cargo.toml
PASS: objective validator (Phase 6 validate-only, 0 blockers)
```

Adaptation reaffirmed: package id `example-streamer-implementations` is not present; validating via
`example-streamer-implementations/Cargo.toml` checks the intended consumer crate (`up-linux-streamer`) without code changes.

## Consumer Changes (if any)

| Crate | File(s) | Why needed | Scope | Risk |
|---|---|---|---|---|
| none | none | no consumer code updates required | N/A | low |

## Sign-Off

- [x] Consumer compatibility preserved.
- [x] Any consumer changes are minimal and justified.
