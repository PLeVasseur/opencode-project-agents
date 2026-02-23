# Plan: PR CI Latency Reduction (Coverage to Nightly)

## Goal

Reduce pull-request CI turnaround time while preserving confidence in transport compatibility and lint quality.

## Baseline (from latest successful PR runs)

- Bundled workflow (`Lint and Test - Bundled`):
  - `Lint`: ~12m21s
  - `Test`: ~9m18s
- Unbundled workflow (`Lint and Test - Unbundled`):
  - `Lint`: ~9m01s
  - `Test`: ~9m05s

Primary hotspots:

- Duplicate no-feature build/clippy work across bundled + unbundled lint jobs
- `cargo install cargo-tarpaulin` in PR test jobs
- Tarpaulin coverage run on every PR

## Scope

In scope:

1. Move coverage from PR-required jobs to nightly/main coverage workflow.
2. Remove duplicated no-feature lint work from unbundled lint job.
3. Add Rust dependency/target caching across workflows.
4. Keep branch-protection-compatible job names for existing required checks.

Out of scope:

- Any production code changes
- Transport behavior changes
- Reducing canonical smoke test coverage expectations

## Execution Rules

- [ ] Execute phases in order.
- [ ] Tick each checkbox immediately after completing that task.
- [ ] Keep all work in one feature branch and one upstream PR.
- [ ] Prefer stacked base `chore/up-rust-0.9-transport-upgrade` when available in target repo; otherwise open PR to `main` from the same feature branch and accept inherited stacked commits.
- [ ] Use logical commits aligned to commit chunks below.

## Phase 0 - Preflight and Safety

- [x] Set up stacked branch from the current branch head.
  - [x] Confirm current branch is `chore/up-rust-0.9-transport-upgrade` (or explicitly chosen replacement base branch).
  - [x] Confirm working tree is clean before branching.
  - [x] Create stacked feature branch from current HEAD (suggested: `perf/ci-pr-latency-reduction`).
  - [x] Push branch with upstream (`git push -u origin <branch>`).
- [ ] Confirm current required check names and avoid renaming required jobs.
  - [x] Verify current PR check names via `gh pr checks <pr-number>`.
  - [ ] Preserve `Lint`, `Test`, and `Build documentation` job names in both workflows.
- [x] Reconfirm baseline timing from latest green run(s) and capture in PR notes.
  - [x] Record bundled `Lint`/`Test` durations.
  - [x] Record unbundled `Lint`/`Test` durations.

## Phase 1 - Move Coverage to Nightly/Main

- [x] Update PR test jobs to run fast functional tests only.
  - [x] In `.github/workflows/bundled-lint-and-test.yaml`, replace tarpaulin path with normal test path.
  - [x] In `.github/workflows/unbundled-lint-and-test.yaml`, replace tarpaulin path with normal test path.
  - [x] Remove PR-time `cargo install cargo-tarpaulin` steps.
- [x] Add dedicated coverage workflow (nightly + manual + main push).
  - [x] Add `.github/workflows/nightly-coverage.yaml`.
  - [x] Trigger on `schedule`, `workflow_dispatch`, and `push` to `main`.
  - [x] Run tarpaulin coverage once (single matrix path) and upload artifacts.
  - [x] Keep coverage command aligned with current expected behavior (`--doc --tests`, thread constraints as needed).
- [x] Ensure coverage workflow does not block PR-required checks.

## Phase 2 - De-duplicate Lint Matrix Work

- [x] Keep no-feature lint/fmt in one workflow only (bundled).
  - [x] Bundled lint retains:
    - [x] `cargo build`
    - [x] `cargo clippy --all-targets -- -W warnings -D warnings`
    - [x] `cargo fmt -- --check`
    - [x] bundled feature build/clippy
- [x] Unbundled lint runs only unbundled feature validation.
  - [x] Remove no-feature build/clippy duplication from unbundled lint.
  - [x] Keep unbundled feature build/clippy steps.
  - [x] Keep fmt check only once overall (bundled).

## Phase 3 - Add Build/Dependency Caching

- [x] Add Rust cache step to CI jobs that compile Rust code.
  - [x] Bundled workflow: `lint`, `test`, `build-docs`.
  - [x] Unbundled workflow: `lint`, `test`, `build-docs`.
- [x] Keep existing vsomeip cache logic in unbundled workflow.
- [x] Ensure cache usage does not change correctness (no skipped validation logic).

## Phase 4 - Validation and Timing Comparison

- [ ] Validate workflow YAML changes are syntactically correct.
  - [ ] Open stacked PR and ensure workflows trigger without YAML errors.
  - [ ] Create PR in upstream repo with base branch set according to availability (use `main` when stacked base branch is absent in upstream).
  - [ ] Verify PR routing with `gh pr view <pr-number> --json baseRefName,headRefName,url`.
- [ ] Confirm required checks still appear and pass on PR.
  - [ ] Bundled: `Lint`, `Test`, `Build documentation`
  - [ ] Unbundled: `Lint`, `Test`, `Build documentation`, `obtain_and_build_vsomeip`
- [ ] Confirm coverage workflow runs on nightly/manual/main push.
  - [ ] Trigger once via `workflow_dispatch` for verification.
- [ ] Capture after-change timing and compare against baseline.
  - [ ] Record new bundled `Lint`/`Test` durations.
  - [ ] Record new unbundled `Lint`/`Test` durations.
  - [ ] Include before/after delta table in PR description.

## Phase 5 - Documentation and Handoff

- [ ] Update CI notes/docs as needed to reflect coverage relocation.
  - [ ] Mention that PR checks validate correctness; coverage is generated nightly/main.
- [ ] Add follow-up notes for any optional future optimization (paths filter, matrix split, test sharding).

## Commit Chunks

- [x] Commit 1: PR test path optimization
  - [x] Move tarpaulin out of PR `Test` jobs
  - [x] Keep PR `Test` jobs as standard test execution
- [x] Commit 2: Coverage workflow introduction
  - [x] Add nightly/main/manual coverage workflow with tarpaulin
- [x] Commit 3: Lint de-duplication
  - [x] Remove duplicated no-feature lint/fmt from unbundled workflow
- [x] Commit 4: Rust cache optimization
  - [x] Add Rust cache to compile-heavy jobs
- [ ] Commit 5 (if needed): Docs/notes update

## Success Criteria

- [ ] Upstream PR is open from `perf/ci-pr-latency-reduction` with base branch chosen per branch availability policy.
- [ ] PR required checks remain green with no loss of lint/test signal quality.
- [ ] Coverage artifacts are produced by dedicated nightly/main workflow.
- [ ] PR critical-path time is materially reduced (target: >=25% reduction for `Lint`+`Test` bottleneck jobs).
- [ ] No repo-code behavior changes (CI/workflow-only scope).

## Rollback Strategy

- [ ] If required checks regress, revert workflow changes in reverse order:
  1. Cache additions
  2. Lint de-duplication
  3. Coverage relocation
- [ ] Re-run checks and re-open with smaller scoped changes.
