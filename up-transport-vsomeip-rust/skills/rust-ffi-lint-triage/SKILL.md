---
name: rust-ffi-lint-triage
description: Resolve clippy and warning failures in Rust FFI-heavy code using source fixes first and narrow lint allowances only when required.
license: Apache-2.0
compatibility: opencode
metadata:
  project: up-transport-vsomeip-rust
  workflow: lint-triage
---

## When to use

Use this skill when CI fails in `cargo clippy --all-targets -- -W warnings -D warnings`, especially in `vsomeip-sys` or other binding-heavy code.

## Triage order

1. Fix warnings at source when practical:
   - replace deprecated/older patterns (for example `std::io::Error::new(...Other...)` -> `std::io::Error::other(...)`)
   - use preferred iterator forms (for example `next_back()` where clippy suggests it)
   - clean doc formatting and genuinely unused code/variables
2. For FFI/generated-binding constraints, use narrow allowances:
   - prefer method-level `#[allow(...)]` over module/crate-level suppression
   - document why the allowance is required by wrapper semantics
3. Avoid broad suppression unless unavoidable for generated interop behavior.

## Generated-binding policy

- Prefer fixes in handwritten wrapper/glue layers first; keep allowances narrow and local.
- Avoid editing generated binding files directly unless regeneration is explicitly in scope.
- If regeneration is in scope, keep generated changes isolated and document the regeneration command in the PR notes.

## Validation loop

1. `source build/envsetup.sh highest`
2. `cargo clippy --all-targets -- -W warnings -D warnings`
3. If clippy passes, run `cargo test -- --test-threads 1` to ensure behavior remains intact.

## Decision notes to include in PR

- Which warnings were fixed at source
- Which lint allowances were added and why they are narrowly scoped
- Any known tradeoffs or follow-up cleanups
