# Plan: Independent CI Fix PR for Main

## Goal

Create a standalone PR (base: `main`) in `eclipse-uprotocol/up-transport-vsomeip-rust` to fix CI issues that are currently broken on `main`.

## Scope

Include these CI-related fixes:

1. `up-transport-vsomeip/tests/point_to_point.rs`
   - Update point-to-point listener registration source filter to align with current streamer-use-case detection semantics.
2. `example-utils/hello-world-protos/build.rs`
   - Replace `std::io::Error::new(std::io::ErrorKind::Other, ...)` with `std::io::Error::other(...)`.
3. `example-utils/hello-world-protos/build.rs`
   - Replace `url.split('/').last()` with `url.split('/').next_back()`.
4. Feasible warning cleanup discovered during local validation
   - Address warnings that are practical to fix without broad API churn.
   - For generated/binding warnings that are not directly fixable at source, apply scoped lint allowances where justified.

## Branching Strategy

- Branch from upstream `main`.
- Suggested branch name: `fix/main-ci-failures`.

## Checklist

- [ ] Sync branch from upstream `main`
  - [ ] Fetch latest upstream refs
  - [ ] Create `fix/main-ci-failures` from `main`

- [ ] Apply the 3 scoped code fixes
  - [ ] `point_to_point.rs` source filter update
  - [ ] `build.rs` `std::io::Error::other(...)` update
  - [ ] `build.rs` `next_back()` update

- [ ] Address feasible warning fixes from validation runs
  - [ ] Remove/fix practical warning-producing code paths
  - [ ] Add narrow lint allowances only where direct code fixes are not feasible

- [ ] Validate locally
  - [ ] `source build/envsetup.sh highest`
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `cargo test -- --test-threads 1`

- [ ] Commit and open PR to `main`
  - [ ] Keep changes scoped to CI fixes only
  - [ ] Use a concise CI-fix commit message
  - [ ] Open PR with summary of the three fixes

- [ ] Link context
  - [ ] Comment on PR #42 with link to this independent PR
  - [ ] Note that these failures are reproducible on `main`

## Definition of Done

- [ ] Independent PR is open against `main` with only the 3 scoped fixes.
- [ ] Local clippy and test commands pass.
- [ ] Feasible warnings observed during validation are resolved or intentionally scoped with justification.
- [ ] CI checks on the independent PR are green.
- [ ] PR #42 is cross-linked to the independent CI fix PR.
