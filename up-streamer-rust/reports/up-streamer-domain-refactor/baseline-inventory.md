# Baseline Inventory

Date: 2026-02-09
Executor: OpenCode (gpt-5.3-codex)
Branch: `refactor/up-streamer-domain-architecture`
Baseline anchor commit SHA: `42d5a26136fd4f71ea873b7e414f8f6fdd9f17a8`

## Purpose

Capture the exact starting state before refactor waves begin.

## Bootstrap Commands

- [x] `git status --short --branch`
- [x] `git log --oneline -15`
- [x] `git rev-parse HEAD`

### Outputs

```text
## refactor/up-streamer-domain-architecture

42d5a26 add regression tests for wildcard routing, dedupe safety, rollback, and Path A cache identity
e8fa62a fix add_forwarding_rule rollback on listener setup failure
8ca9785 update listener registration to merge wildcard subscribers and dedupe publish keys
f470b22 chore: remove issue-74 mentions from docs and tests
a553a37 fix integration harness listener unregister symmetry
c51bfc8 document issue74 runbook and CLI override usage
c026489 fix publish forwarding authority matching in streamer
08b3c0e parameterize remaining example binaries for CLI overrides
b134d5a parameterize MQTT and Zenoh pubsub binaries
0d441dc add shared CLI parsing helpers for example binaries
5f7e6b6 ci: simplify bundled lint aggregator checks
ec4af3b ci: trim unbundled lint apt deps
9578b4d ci: harden bundled lint cleanup for vsomeip artifacts
6bf09c3 ci: de-duplicate bundled feature lint compilation
4a5d3cd ci: avoid vendored OpenSSL in required CI paths

42d5a26136fd4f71ea873b7e414f8f6fdd9f17a8
```

## Workspace Inventory

### Workspace members (from root Cargo.toml)

- [x] `example-streamer-uses`
- [x] `utils/hello-world-protos`
- [x] `utils/integration-test-utils`
- [x] `example-streamer-implementations`
- [x] `configurable-streamer`
- [x] `up-linux-streamer-plugin`
- [x] `up-streamer`
- [x] `subscription-cache`
- [x] `utils/usubscription-static-file`

### Core file size snapshot

| File | Baseline LOC | Notes |
|---|---:|---|
| `up-streamer/src/ustreamer.rs` | 2060 | monolithic orchestration core |
| `up-streamer/src/endpoint.rs` | 112 | public endpoint facade |
| `subscription-cache/src/lib.rs` | 289 | subscription cache behavior core |
| `up-streamer/tests/*.rs` total | 1498 | 5 integration test files |
| `utils/integration-test-utils/src/*.rs` total | 1108 | harness/mocks and shared helpers |

## Environment and Prerequisites

- [x] `OPENCODE_CONFIG_DIR` set and writable
- [x] Rust toolchain/`rustc --version` captured
- [x] workspace root confirmed
- [x] notes for transport/CI parity environment captured

### Notes

```text
OPENCODE_CONFIG_DIR=/home/pete.levasseur/opencode-project-agents/up-streamer-rust (writable)
Workspace root=/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust
rustc 1.92.0 (ded5c06cf 2025-12-08)

Bootstrap branch operations executed:
- git fetch --all --prune
- git switch bugfix/issue-74-left-topic-authority
- git pull --ff-only
- git switch -c refactor/up-streamer-domain-architecture || git switch refactor/up-streamer-domain-architecture

Transport/CI parity notes:
- No transport feature matrix commands were executed in Phase 0 baseline capture.
- Phase 0 baseline test commands ran without requiring build/envsetup overrides.
```
