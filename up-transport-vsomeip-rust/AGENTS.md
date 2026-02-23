# Project Instructions

When asked to confirm AGENTS, run `printenv OPENCODE_CONFIG_DIR` and reply `AGENTS loaded from <value>`. Do not search for AGENTS.md or use Python for this check.

When asked to execute or follow a plan, first run `printenv OPENCODE_CONFIG_DIR`, then read plan files from `$OPENCODE_CONFIG_DIR/plans`. Do not use repository globbing to locate plans.

## Overview

- Rust workspace implementing uProtocol uTransport over SOME/IP (vsomeip).
- Workspace members: `up-transport-vsomeip` (transport implementation), `vsomeip-sys` (C++ vsomeip FFI bindings/wrappers), `vsomeip-proc-macro` (proc-macro helpers).
- Integration tests rely on shared vsomeip resources/configurations and are sensitive to runtime ordering.

## Workflow

- Branch and scope management:
  - For independent CI fixes, branch from `main` and keep changes narrowly scoped.
  - If borrowing changes from another PR for temporary validation, isolate them as a firewall commit/branch and recreate the final PR branch with only intended commits.
  - Before opening a PR, verify scope with `git log --oneline main..HEAD` and `git diff --name-only main...HEAD`.
- Preferred local validation commands (run from repo root):
  - `source build/envsetup.sh highest`
  - `cargo clippy --all-targets -- -W warnings -D warnings`
  - `cargo test -- --test-threads 1`
- Flaky test guidance:
  - `publisher_subscriber` may intermittently fail by one message; rerun the full serial test command once before classifying as a hard failure.
- GitHub CLI safety:
  - For `gh pr create`/`gh pr comment`, use single-quoted heredocs for bodies to prevent shell interpolation issues.
  - Avoid backticks in double-quoted shell strings; they can trigger command substitution.
  - If a malformed PR comment is posted, add a correction comment rather than rewriting history.

## Code Standards

- Rust edition 2021, workspace `rust-version = 1.76`.
- Prefer fixing warnings at the source (`std::io::Error::other`, iterator updates, doc formatting, dead code cleanup) over lint suppression.
- For unavoidable FFI/generated-binding patterns, use narrow/local lint allowances (for example method-level `#[allow(clippy::mut_from_ref)]`) instead of broad crate-wide suppression.
- Keep point-to-point listener/filter behavior aligned with `determine_message_type` semantics; add compatibility fallbacks only when needed to preserve current behavior.

## Files to Know

- `Cargo.toml` (workspace structure, versions, rust toolchain).
- `build/envsetup.sh` (required build/test env setup).
- `up-transport-vsomeip/src/lib.rs` and `up-transport-vsomeip/src/transport_engine.rs` (core transport behavior).
- `up-transport-vsomeip/src/determine_message_type.rs` (message type classification semantics).
- `up-transport-vsomeip/tests/point_to_point.rs` and `up-transport-vsomeip/tests/publisher_subscriber.rs` (CI-sensitive integration tests).
- `example-utils/hello-world-protos/build.rs` (clippy-sensitive build script patterns).
- `vsomeip-sys/src/glue_additions.rs` and `vsomeip-sys/src/lib.rs` (FFI wrapper and lint-prone areas).

## Skills

- `main-ci-fix-pr` - execute independent CI-fix plans from config-plan lookup through PR + cross-linking.
- `rust-ffi-lint-triage` - resolve clippy/warning failures in FFI-heavy code with minimal safe lint allowances.
- `gh-safe-pr-commenting` - create/verify PR bodies and comments safely using `gh`.
