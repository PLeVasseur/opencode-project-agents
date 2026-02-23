---
name: rust-test-quality-gate
description: Write deterministic, short, behavior-first Rust tests with explicit assertions and scoped validation.
license: Apache-2.0
compatibility: opencode
metadata:
  project: up-streamer-rust
  workflow: test-quality
---

## When to use

Use this skill for non-trivial test additions, test refactors, and behavior-sensitive bug fixes where reviewers need high-confidence, easy-to-read coverage.

## Foundations (synthesized)

- Rust Book (ch. 11): choose the right split between unit and integration tests; keep tests close to behavior under test.
- rustc-dev-guide testing guidance: keep test changes isolated and deterministic so failures are actionable and reproducible.
- Rust API Guidelines (dependability/debuggability): validate behavior with explicit checks and keep failures easy to diagnose.
- Ecosystem patterns from high-quality crates:
  - `serde`: compact regression fixtures plus compile-fail coverage where diagnostics matter.
  - `clap`: feature-aware test matrices, `trybuild` for compile diagnostics, and snapshot-like CLI behavior checks.
  - `tokio`: deterministic async/concurrency tests, strong `cfg` gating for platform/runtime differences.

## Workflow

1. Pick the smallest correct test type:
   - unit test for narrow logic
   - integration test for cross-module behavior
   - compile-fail (`trybuild`) when diagnostics are part of the contract
2. For bug fixes, add focused fail-before coverage first when practical.
3. Keep each test behavior-first and short:
   - one primary behavior per test
   - target compact bodies (roughly 15-35 lines before helper extraction)
   - use helpers/builders for setup repetition, not for hiding assertions
4. Make tests deterministic:
   - avoid sleep-based correctness checks
   - prefer explicit triggers, controlled channels, and deterministic fixtures
   - gate platform-specific behavior with `#[cfg(...)]`
5. Validate in increasing scope:
   - run focused tests first
   - then crate-level tests
   - then project-required lint/format checks

## Quality gate checklist

- Test names describe behavior, not issue IDs.
- Assertions are explicit (`assert_eq!`, `assert!`) with clear expected values.
- Failure output is informative without reading implementation internals.
- Fixtures are minimal and directly tied to the behavior being proven.
- No timing-sensitive flakiness is introduced without a documented reason.

## Anti-patterns to reject

- Multi-behavior "kitchen sink" tests.
- Assertions that only check `is_ok()` when concrete state can be asserted.
- Sleep-heavy async tests where deterministic signaling is available.
- Renaming tests to issue numbers or embedding issue tags in test IDs.

## Report template

Always report:

1. Tests added/updated and the single behavior each test proves
2. Determinism strategy used (why the test is stable)
3. Commands run (focused first, then broader)
4. Any intentionally untested edge cases and why
