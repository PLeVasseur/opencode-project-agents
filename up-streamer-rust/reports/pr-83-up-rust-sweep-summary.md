# PR-83 up-rust idiomatic usage sweep summary

Date: 2026-02-17
Repository: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
Branch: `cleanup/refactor-upstream-main-prA-architecture`
PR: https://github.com/eclipse-uprotocol/up-streamer-rust/pull/83

## Completed remediation scope

- Replaced manual nested protobuf field access with canonical up-rust accessors where available.
- Replaced wildcard authority string comparisons with semantic URI helper usage.
- Replaced local doctest transport stubs with hidden setup built on `up_rust::MockTransport` (`test-util`, dev-only).
- Ran a residual whole-codebase idiom closure pass to convert remaining easy accessor sites.
- Documented approved residual direct-field usages where helper/setter equivalents are not available or would introduce avoidable clone overhead.

## Review feedback to remediation mapping

- Feedback: prefer `up-rust` message/attribute helpers over raw `attributes.as_ref()` chains.
  - Remediated in:
    - `up-streamer/src/observability/fields.rs`
    - `utils/integration-test-utils/src/integration_test_utils.rs`
    - `utils/integration-test-utils/src/up_client_foo.rs`
    - `example-streamer-uses/src/bin/common/mod.rs`
- Feedback: prefer semantic URI helpers over direct authority string checks.
  - Remediated in:
    - `up-streamer/src/routing/publish_resolution.rs`
    - `utils/integration-test-utils/src/up_client_foo.rs`
- Feedback: prefer shared `up-rust` mock transport in doctests.
  - Remediated in:
    - `up-streamer/src/lib.rs`
    - `up-streamer/src/control_plane/mod.rs`
    - `up-streamer/src/data_plane/mod.rs`
    - `up-streamer/src/routing/mod.rs`
    - `up-streamer/Cargo.toml` (dev-dependency feature wiring)
    - `Cargo.lock` (dependency resolution updates)

## Commit state

- Local phased confidence commits were created and validated, then squashed into:
  - `87e0b7e` - `refactor: align streamer code with up-rust idioms`
- Pre-squash rollback anchor:
  - Tag `pr-83-pre-squash-20260217T161524Z` -> `a6dcccc`
- Squashed commit body includes detailed rationale for intentionally retained direct-field usages.

## Validation results

- Base parity gate (`build`, `clippy -D warnings`, `fmt --check`): pass.
- Bundled transport matrix (`vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport` + clippy): pass.
- Workspace `check` and `test`: pass.
- `up-streamer` doctests: pass.
- Repository-wide anti-pattern grep re-sweep: no remaining matches for targeted classes.
- Residual-closure grep matrix: only approved exemptions remain.

## Remaining work before publish

- Do not add more code changes without preserving branch lock and validation policy.
- Keep exemptions synchronized with any additional residual direct-field edits.
- Perform the planned final squash of local remediation commits into one commit (not done yet).
- Run pre-push remote drift checks and squash integrity checks.
- Push only after explicit user go-ahead.
