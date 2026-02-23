# Commit Buckets for Consolidation (Target: 6 commits)

## Commit 1 (final subject)

`refactor: modernize up-streamer domain architecture boundaries`

Included original commits:

- `8437405` chore: checkpoint domain modernization baseline
- `9f29a28` refactor: consolidate streamer api facade ownership
- `78653e0` refactor: modernize control-plane route lifecycle boundaries
- `f8c2bd0` refactor: modernize routing resolution policies
- `536173f` refactor: modernize data-plane ingress and egress abstractions
- `83bfa41` refactor: isolate runtime adapters and remove leakage
- `fae8c1e` test: improve readability and ownership of streamer tests
- `5d95dea` refactor: align internal route semantics with domain modules
- `e9f0faf` docs: add layered rustdoc and doctest coverage
- `1db82a1` chore: checkpoint domain modernization baseline

## Commit 2 (final subject)

`refactor: complete USubscription and route identity contract migration`

Included original commits:

- `47dc4dc` chore: checkpoint usubscription decoupling prep state
- `2271665` refactor: migrate streamer refresh to USubscription contract
- `6bf5410` style: normalize USubscription wiring formatting
- `ac4d98c` refactor: use UUri keys for subscription identity dedupe
- `33adf32` refactor: make route lifecycle errors idiomatic and explicit
- `f8a1bde` refactor: remove forwarding-rule aliases and migrate callers
- `af23f8d` refactor: restore immutable URI projection keys in up-streamer routing
- `0be68a9` refactor: migrate static subscription dedupe to projection keys

## Commit 3 (final subject)

`perf+obs: optimize worker/runtime paths and structured tracing coverage`

Included original commits:

- `711897d` refactor: add borrowed route APIs for ergonomic call sites
- `4d5fd6f` refactor: simplify route lifecycle and publish resolver composition
- `002209e` refactor: narrow ingress registry locks and explicit config errors
- `edfe2cc` refactor: harden egress recv loop and thread traceability
- `b0f8c15` chore: add structured tracing event and field helpers
- `5d8115a` refactor: convert egress worker logs to structured tracing events
- `7d5d845` refactor: correlate route labels to pooled egress workers
- `b8767b8` refactor: migrate ingress and routing logs to structured tracing
- `584d221` feat: add structured lifecycle and runtime observability events
- `76f1e6c` fix: harden plugin lifecycle and ingress listener teardown
- `083fbb6` perf: cut routing and ingress overhead with snapshot caching
- `0878db8` perf: shift egress workers to shared runtime tasks
- `f917011` refactor: improve startup ergonomics and static-file reload options
- `1041aa7` test: stabilize integration scenarios with bounded wait controls

## Commit 4 (final subject)

`feat(ci): add benchmark guardrail harness and advisory workflow`

Included original commits:

- `46e5bf3` feat: add Criterion harness and guardrail CLI foundation
- `f48d98c` ci: add advisory benchmark guardrail integration

## Commit 5 (final subject)

`feat(smoke): add deterministic cross-transport smoke suite, claims, and matrix workflow`

Included original commits:

- `d01a4a6` Add transport-smoke-suite orchestration foundation
- `11da7e5` Add deterministic sender bounds and readiness markers
- `a0c830e` Add MQTT smoke scenario binaries and fixture audits
- `a282462` Add SOME/IP smoke scenario binaries and contracts
- `56fd4d8` Add matrix runner, docs, and capstone workflow
- `349d8a0` Align smoke claims with structured tracing output
- `184e986` Refactor smoke runtime for strict file-backed claims
- `51c6212` Add per-scenario smoke claims files and contracts

## Commit 6 (final subject)

`chore: align new-file copyright headers to 2026`

Included original commits:

- `cbe631a` chore: align new-file copyright headers to 2026

## Mixed Commits Requiring Split (`edit`)

- None identified; all original commits are fully bucketed without split.
