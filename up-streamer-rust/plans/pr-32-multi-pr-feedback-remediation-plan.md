# PR-32 Feedback Remediation Plan (Stacked Multi-PR, Recovery-Safe)

Date: 2026-02-14
Source feedback: `$OPENCODE_CONFIG_DIR/reports/pr-32-review.md`
Execution repo: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
Current source branch: `cleanup/refactor-upstream-main`

## Locked strategy (good-faith, to-the-letter response)

- [x] Use **three stacked PRs** (Architecture, Benchmark, Smoke) rather than one monolithic PR.
- [x] Rebuild commits so each file reaches its final state in exactly one commit (`Cargo.lock` exception only).
- [x] Split concerns exactly as requested: `observability/` isolated; `benchmark_support.rs` lands with benchmark harness.
- [x] Remove the need for a copyright-fixup commit by adding headers at file creation.
- [x] Ensure every commit has a meaningful body (what changed, why, key review files).
- [x] Make fixture-heavy smoke diffs reviewer-friendly via `.gitattributes` (`linguist-generated=true`).

## Reviewer requirement traceability

- [ ] R1 (overlap in commits 1-3): zero multi-commit file overlap after rewrite.
- [ ] R2 (mixed concerns in commit 3): observability/benchmark/perf concerns separated into dedicated commits.
- [ ] R3 (copyright fixup commit): no standalone header-only remediation commit exists.
- [ ] R4 (`benchmark_support.rs` blank-line boundary leak): eliminated by creating it once in benchmark commit.
- [ ] R5 (fixtures bury logic): `.gitattributes` collapse rules added for smoke fixtures.
- [ ] R6 (no commit bodies): every commit has rationale-focused body and reviewer guidance.

## Checkbox integrity policy (always on)

- [ ] Parent checkbox is marked `[x]` only when every child checkbox under it is `[x]`.
- [ ] If evidence is missing, leave unchecked and capture required proof in report artifacts.
- [ ] At restart, resume from first unchecked item in the active phase.

## Phase 0 - Fresh-session bootstrap and run-state creation

- [ ] Confirm environment and repo state:
  - [ ] `printenv OPENCODE_CONFIG_DIR`
  - [ ] `test -n "$OPENCODE_CONFIG_DIR"`
  - [ ] `git -C /home/pete.levasseur/eclipse/uprotocol/up-streamer-rust status --short --branch`
  - [ ] `test ! -d /home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/.git/rebase-merge`
  - [ ] `test ! -d /home/pete.levasseur/eclipse/uprotocol/up-streamer-rust/.git/rebase-apply`
- [ ] Initialize durable run metadata under `$OPENCODE_CONFIG_DIR/reports/`:
  - [ ] `RUN_ID="pr-32-multi-pr-remediation-$(date -u +%Y%m%dT%H%M%SZ)"`
  - [ ] `REPORT_DIR="$OPENCODE_CONFIG_DIR/reports/$RUN_ID"`
  - [ ] `mkdir -p "$REPORT_DIR"`
  - [ ] `RUN_POINTER="$OPENCODE_CONFIG_DIR/reports/pr-32-multi-pr-remediation.current"`
  - [ ] `ln -sfn "$REPORT_DIR" "$RUN_POINTER"`
  - [ ] `STATE_FILE="$REPORT_DIR/session-state.env"`
  - [ ] `PHASE_FILE="$REPORT_DIR/phase-markers.log"`
  - [ ] `TRANSCRIPT_FILE="$REPORT_DIR/command-transcript.log"`
  - [ ] `: > "$PHASE_FILE"`
  - [ ] write initial state values to `STATE_FILE`
- [ ] Start command transcript capture (append mode for resumes):
  - [ ] `exec > >(tee -a "$TRANSCRIPT_FILE") 2>&1`
- [ ] Phase marker:
  - [ ] append `PHASE_0_COMPLETE` timestamp to `PHASE_FILE`

## Phase 0R - Resume protocol (if session crashes/restarts)

- [ ] Detect existing unfinished run:
  - [ ] `test -L "$OPENCODE_CONFIG_DIR/reports/pr-32-multi-pr-remediation.current"`
  - [ ] `ACTIVE_REPORT_DIR="$(readlink -f "$OPENCODE_CONFIG_DIR/reports/pr-32-multi-pr-remediation.current")"`
  - [ ] `test -f "$ACTIVE_REPORT_DIR/session-state.env"`
- [ ] Rehydrate state and validate:
  - [ ] `source "$ACTIVE_REPORT_DIR/session-state.env"`
  - [ ] verify `PHASE_FILE` and `TRANSCRIPT_FILE` exist
  - [ ] `git -C /home/pete.levasseur/eclipse/uprotocol/up-streamer-rust fetch --all --prune`
  - [ ] if rebase is active, resolve `git rebase --continue`/`--abort` before new operations
- [ ] Resume execution:
  - [ ] locate first unchecked checkbox in this plan
  - [ ] continue from that point only (no duplicate phase re-runs unless evidence is invalid)

## Phase 1 - Safety baseline before rewrite

- [ ] Confirm clean, synchronized starting point:
  - [ ] `git status --short --branch`
  - [ ] `test -z "$(git status --porcelain)"`
  - [ ] `git fetch --all --prune`
  - [ ] `BASE_SHA="$(git rev-parse upstream/main)"`
  - [ ] `SOURCE_SHA="$(git rev-parse cleanup/refactor-upstream-main)"`
  - [ ] `REMOTE_SOURCE_SHA="$(git rev-parse origin/cleanup/refactor-upstream-main)"`
  - [ ] `test "$SOURCE_SHA" = "$REMOTE_SOURCE_SHA"`
- [ ] Create durable rollback refs before history rewrite:
  - [ ] `BACKUP_BRANCH="backup/pr-32-before-multi-pr-$(date -u +%Y%m%dT%H%M%SZ)"`
  - [ ] `BACKUP_TAG="backup-pr-32-before-multi-pr-$(date -u +%Y%m%dT%H%M%SZ)"`
  - [ ] `git branch "$BACKUP_BRANCH" "$SOURCE_SHA"`
  - [ ] `git tag "$BACKUP_TAG" "$SOURCE_SHA"`
  - [ ] `git push origin "$BACKUP_BRANCH"`
  - [ ] `git push origin "$BACKUP_TAG"`
  - [ ] `git ls-remote --heads origin "$BACKUP_BRANCH"`
  - [ ] `git ls-remote --tags origin "$BACKUP_TAG"`
- [ ] Persist rollback metadata to `STATE_FILE`.
- [ ] Phase marker:
  - [ ] append `PHASE_1_COMPLETE` timestamp to `PHASE_FILE`

## Phase 2 - Deterministic rewrite workspace

- [ ] Create isolated rewrite branch:
  - [ ] `git switch -c pr-32-restack-work "$SOURCE_SHA"`
- [ ] Materialize full diff as unstaged changes against `upstream/main`:
  - [ ] `git reset --soft "$BASE_SHA"`
  - [ ] `git reset HEAD .`
- [ ] Save baseline inventories for proof and recovery:
  - [ ] `git diff --name-status > "$REPORT_DIR/pre-rewrite-name-status.txt"`
  - [ ] `git diff --stat > "$REPORT_DIR/pre-rewrite-stat.txt"`
  - [ ] `git log --reverse --oneline "$BASE_SHA".."$SOURCE_SHA" > "$REPORT_DIR/original-commit-order.txt"`
- [ ] Confirm expected large diff is present and unstaged.
- [ ] Phase marker:
  - [ ] append `PHASE_2_COMPLETE` timestamp to `PHASE_FILE`

## Phase 3 - Rebuild the 7 commit stack with strict boundaries

### Commit 1 - observability leaf

- [ ] Stage only `up-streamer/src/observability/` (final state with headers).
- [ ] Commit subject/body:
  - [ ] `refactor: add observability event and field vocabulary`
  - [ ] body explains leaf nature + review focus files.
- [ ] Gate:
  - [ ] `git diff --name-only --cached`
  - [ ] `git diff --stat --cached`
  - [ ] `cargo check --workspace --all-targets`

### Commit 2 - routing extraction + subscription-cache fold-in

- [ ] Stage only routing final-state files and `subscription-cache` removal/fold-in paths.
- [ ] Commit subject/body:
  - [ ] `refactor: extract routing module and fold in subscription-cache crate`
  - [ ] body includes explicit rationale for fold-in location.
- [ ] Gate:
  - [ ] staged file scope checks
  - [ ] `cargo check --workspace --all-targets`

### Commit 3 - data_plane + control_plane + runtime extraction

- [ ] Stage only `up-streamer/src/data_plane/`, `up-streamer/src/control_plane/`, `up-streamer/src/runtime/` final-state files.
- [ ] Commit subject/body with dependency explanation and key review files.
- [ ] Gate:
  - [ ] staged file scope checks
  - [ ] `cargo check --workspace --all-targets`

### Commit 4 - top-level rewire

- [ ] Stage only top-level wiring/API/entrypoint/plugin/Cargo files.
- [ ] Include `up-streamer/src/ustreamer.rs`, `up-streamer/src/lib.rs`, entrypoints, plugin wiring.
- [ ] Commit subject/body:
  - [ ] `refactor: rewire top-level API, plugin, and entrypoints`
  - [ ] body names important design deltas vs mechanical moves.
- [ ] Gate:
  - [ ] staged file scope checks
  - [ ] `cargo check --workspace --all-targets`

### Commit 5 - tests only

- [ ] Stage only test/integration utility updates.
- [ ] Commit subject/body:
  - [ ] `test: update integration and unit tests for refactored module layout`
  - [ ] body labels mechanical path updates vs behavior changes.
- [ ] Gate:
  - [ ] staged file scope checks
  - [ ] `cargo check --workspace --all-targets`

### Commit 6 - benchmark harness (must include benchmark_support)

- [ ] Stage benchmark/guardrail files **including** `up-streamer/src/benchmark_support.rs` creation.
- [ ] Ensure no separate commit later edits `benchmark_support.rs` for trivial whitespace.
- [ ] Commit subject/body:
  - [ ] `feat(ci): add criterion benchmark harness and guardrail workflow`
  - [ ] body explains deterministic fixtures and CI advisory intent.
- [ ] Gate:
  - [ ] staged file scope checks
  - [ ] `cargo check -p criterion-guardrail --all-targets`
  - [ ] `cargo test -p criterion-guardrail --all-targets`

### Commit 7 - smoke suite (fixture-collapsed)

- [ ] Stage smoke-suite code/workflow/fixtures and `.gitattributes` rules.
- [ ] Add and verify:
  - [ ] `utils/transport-smoke-suite/tests/fixtures/** linguist-generated=true`
  - [ ] `utils/transport-smoke-suite/claims/** linguist-generated=true`
- [ ] Commit subject/body:
  - [ ] `feat(smoke): add deterministic cross-transport smoke suite`
  - [ ] body explains claims engine, matrix execution, fixture-collapsing rationale.
- [ ] Gate:
  - [ ] staged file scope checks
  - [ ] `cargo check -p transport-smoke-suite --all-targets`
  - [ ] `cargo test -p transport-smoke-suite --tests`

### Post-stack proof gates (mandatory)

- [ ] Final-tree identity vs source branch:
  - [ ] `git diff --stat "$SOURCE_SHA"..HEAD` shows 0 changes.
- [ ] Per-commit compile proof:
  - [ ] `git rebase --exec 'cargo check --workspace --all-targets' "$BASE_SHA"` (or equivalent scripted traversal) passes.
- [ ] File overlap proof (`Cargo.lock` exception only):
  - [ ] generate commit-to-file matrix report at `"$REPORT_DIR/commit-file-overlap.txt"`
  - [ ] report shows no duplicates across commits 1-7 except `Cargo.lock`.
- [ ] Header-at-creation audit:
  - [ ] confirm no commit exists whose sole purpose is adding headers.

- [ ] Phase marker:
  - [ ] append `PHASE_3_COMPLETE` timestamp to `PHASE_FILE`

## Phase 4 - Split into three stacked PR branches

- [ ] Capture rewritten commit SHAs (`C1..C7`) into `STATE_FILE`.
- [ ] Create PR A branch at `C5`:
  - [ ] `git branch cleanup/refactor-upstream-main-prA-architecture "$C5"`
- [ ] Create PR B branch from `C5` with benchmark commit only:
  - [ ] `git switch -c cleanup/refactor-upstream-main-prB-benchmark "$C5"`
  - [ ] `git cherry-pick -x "$C6"`
- [ ] Create PR C branch from `C5` with smoke commit only:
  - [ ] `git switch -c cleanup/refactor-upstream-main-prC-smoke "$C5"`
  - [ ] `git cherry-pick -x "$C7"`
- [ ] Verify branch intent:
  - [ ] PR A (`upstream/main...prA`) contains commits C1-C5 only
  - [ ] PR B (`prA...prB`) contains commit C6 only
  - [ ] PR C (`prA...prC`) contains commit C7 only

- [ ] Phase marker:
  - [ ] append `PHASE_4_COMPLETE` timestamp to `PHASE_FILE`

## Phase 5 - Validation gates before publish

- [ ] PR A validation:
  - [ ] `source build/envsetup.sh highest`
  - [ ] `cargo build`
  - [ ] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [ ] `cargo fmt -- --check`
  - [ ] `cargo check --workspace --all-targets`
  - [ ] `cargo test --workspace`
- [ ] PR B validation:
  - [ ] `cargo check -p criterion-guardrail --all-targets`
  - [ ] `cargo test -p criterion-guardrail --all-targets`
  - [ ] `cargo check -p up-streamer --benches`
- [ ] PR C validation:
  - [ ] `cargo check -p transport-smoke-suite --all-targets`
  - [ ] `cargo test -p transport-smoke-suite --tests`
  - [ ] smoke CI workflow YAML lint/check (syntax and path integrity)

- [ ] Phase marker:
  - [ ] append `PHASE_5_COMPLETE` timestamp to `PHASE_FILE`

## Phase 6 - Push branches and create stacked PRs

- [ ] Push branches:
  - [ ] `git push -u origin cleanup/refactor-upstream-main-prA-architecture`
  - [ ] `git push -u origin cleanup/refactor-upstream-main-prB-benchmark`
  - [ ] `git push -u origin cleanup/refactor-upstream-main-prC-smoke`
- [ ] Create PR A (base `upstream/main`) with explicit commit-by-commit map and reviewer focus.
- [ ] Create PR B (base `cleanup/refactor-upstream-main-prA-architecture`) and note dependency on PR A.
- [ ] Create PR C (base `cleanup/refactor-upstream-main-prA-architecture`) and note dependency on PR A.
- [ ] In each PR body, include “Feedback closure” bullets for R1-R6.
- [ ] Record PR URLs in `"$REPORT_DIR/pr-urls.md"`.

- [ ] Phase marker:
  - [ ] append `PHASE_6_COMPLETE` timestamp to `PHASE_FILE`

## Phase 7 - Failure handling and rollback procedures

- [ ] If rewrite is wrong before pushes:
  - [ ] `git switch cleanup/refactor-upstream-main`
  - [ ] `git branch -D pr-32-restack-work` (only if safe and not needed)
  - [ ] restart from Phase 2 using backup refs.
- [ ] If pushed branches need full rollback:
  - [ ] recreate from backup ref: `git switch -c recovery/pr-32 "$BACKUP_BRANCH"`
  - [ ] force-update affected remote branch only with explicit `--force-with-lease` and exact old SHA.
- [ ] If session dies mid-phase:
  - [ ] resume via Phase 0R using `RUN_POINTER`
  - [ ] continue from first unchecked checkbox
  - [ ] do not create a second parallel run for same rewrite effort.

## Completion criteria (must all be true)

- [ ] All R1-R6 traceability items are checked with command-evidence in `REPORT_DIR`.
- [ ] Three PRs exist with correct stacking and scopes (A architecture, B benchmark, C smoke).
- [ ] Final code content is identical to original source branch tip (`SOURCE_SHA`) apart from commit/PR structure.
- [ ] No copyright-fixup-only commit exists.
- [ ] Every commit includes a body and reviewer guidance.
- [ ] Resume artifacts (`RUN_POINTER`, `STATE_FILE`, `PHASE_FILE`, transcript) are complete for future sessions.
