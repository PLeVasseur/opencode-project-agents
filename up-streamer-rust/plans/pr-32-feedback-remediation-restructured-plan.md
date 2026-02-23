# PR-32 Feedback Remediation Plan (Restructured, Dependency-Aware)

Date: 2026-02-14
Primary source: `$OPENCODE_CONFIG_DIR/reports/pr-32-plan-and-concerns-review.md`
Supporting source: `$OPENCODE_CONFIG_DIR/reports/pr-32-review.md`
Execution repo: `/home/pete.levasseur/eclipse/uprotocol/up-streamer-rust`
Source branch: `cleanup/refactor-upstream-main`

## Canonical run artifacts

- [x] `SUMMARY_REPORT="$OPENCODE_CONFIG_DIR/reports/pr-32-remediation-run-summary.md"`
- [x] `PROGRESS_FILE="$OPENCODE_CONFIG_DIR/reports/pr-32-remediation-progress.env"`
- [x] `CHECKPOINT_TAG_PREFIX` is generated once and persisted in `PROGRESS_FILE`.
- [x] Restart rule: always read `SUMMARY_REPORT` and `PROGRESS_FILE` first in a new session.
- [x] Local-only resilience artifacts:
  - [x] checkpoint tags are local recovery markers only (do not push by default).
  - [x] recovery source of truth is `PROGRESS_FILE` + `SUMMARY_REPORT` + backup refs.

## Locked decisions

- [x] Use stacked PRs: PR A (migration+architecture+tests), PR B (benchmark), PR C (smoke).
- [x] Collapse prior commits 2-4 into one compile-safe architectural commit.
- [x] Treat `log`/`env_logger` -> `tracing` migration as an explicit, early, mechanical commit.
- [x] Keep recovery lean: backup branch/tag + clear rollback command, no heavy session orchestration.
- [x] Enforce fail-fast overlap checks after each reconstructed commit.
- [x] Allow controlled cross-commit overlap only for explicitly allowed files/categories.
- [x] Use lightweight crash resilience (progress file + checkpoint tags), not heavy session scaffolding.
- [x] Adopt Commit 0 Strategy A: include only fully-finalizable migration files; defer entangled files to owning commits.
- [x] Keep Commit 0 intentionally small; defer `example-streamer-uses` behavioral smoke infrastructure changes to Commit 5.

## Reviewer traceability targets

- [x] R1: remove cross-commit file overlap that made commits 1-3 non-reviewable.
- [x] R2: separate mixed concerns (observability, benchmark, perf/rewire) into clear boundaries.
- [x] R3: eliminate standalone copyright-fixup commit.
- [x] R4: ensure `benchmark_support.rs` is created in benchmark commit and not patched later.
- [ ] R5: collapse fixture-heavy smoke diff via `.gitattributes` linguist hints.
- [x] R6: require meaningful commit bodies with reviewer guidance.

## Single-touch policy with explicit exceptions

- [ ] Default rule: each file reaches final state in exactly one commit.
- [x] Allowed multi-touch exceptions (wiring files only):
  - [x] any workspace crate manifest `**/Cargo.toml` (including root `Cargo.toml`).
  - [x] `Cargo.lock`.
  - [x] `up-streamer/src/lib.rs` (only when needed for compile-safe module exposure).
- [x] Commit 0 strategy (Strategy A, narrow and finalizable):
  - [x] Commit 0 includes only files that are fully finalizable as mechanical logging/dependency migration.
  - [x] Commit 0 source-file scope is explicitly small by design (4 files):
    - [x] `example-streamer-uses/src/bin/common/mod.rs`
    - [x] `utils/integration-test-utils/src/integration_test_listeners.rs`
    - [x] `utils/integration-test-utils/src/up_client_failing_register.rs`
    - [x] `up-streamer/src/endpoint.rs`
  - [x] Commit 0 excludes files whose diffs mix logging migration with architectural/behavioral rewrites; those files land in their owning later commit.
  - [x] `example-streamer-uses/src/bin/*.rs` (except `common/mod.rs`) and `example-streamer-uses/README.md` are explicitly deferred to Commit 5 (smoke infrastructure scope).
  - [x] `subscription-cache/` is fully excluded from Commit 0.
  - [x] `up-streamer/src/endpoint.rs` is treated as Commit 0 finalizable (logging removal only).
  - [x] target overlap for source files (`*.rs`) between Commit 0 and later commits is zero.
  - [x] if any non-wiring overlap is unavoidable, pre-approve it in `$OPENCODE_CONFIG_DIR/reports/pr-32-approved-source-overlap.txt` with rationale before continuing.
- [x] Commit 0 inventories recorded before Commit 1:
  - [x] write included file list to `$OPENCODE_CONFIG_DIR/reports/pr-32-commit0-included-files.txt`.
  - [x] write deferred file list (with destination commit label) to `$OPENCODE_CONFIG_DIR/reports/pr-32-commit0-deferred-files.txt`.
- [x] Any new exception requires written rationale in report evidence before continuing.

## Phase 1 - Safety baseline (minimal, mandatory)

- [x] Verify clean/synced start:
  - [x] `git status --short --branch`
  - [x] `test -z "$(git status --porcelain)"`
  - [x] `git fetch --all --prune`
  - [x] `BASE_SHA="$(git rev-parse upstream/main)"`
  - [x] `SOURCE_SHA="$(git rev-parse cleanup/refactor-upstream-main)"`
  - [x] `REMOTE_SOURCE_SHA="$(git rev-parse origin/cleanup/refactor-upstream-main)"`
  - [x] `test "$SOURCE_SHA" = "$REMOTE_SOURCE_SHA"`
- [x] Initialize lightweight run evidence files:
  - [x] `SUMMARY_REPORT="$OPENCODE_CONFIG_DIR/reports/pr-32-remediation-run-summary.md"`
  - [x] `PROGRESS_FILE="$OPENCODE_CONFIG_DIR/reports/pr-32-remediation-progress.env"`
  - [x] if `PROGRESS_FILE` already exists, source it and reuse persisted values.
  - [x] if `PROGRESS_FILE` does not exist, initialize once:
    - [x] `CHECKPOINT_TAG_PREFIX="pr-32-restack-$(date -u +%Y%m%dT%H%M%SZ)"`
    - [x] `RESTACK_BRANCH_BASE="pr-32-restack-work"`
    - [x] `PRA_BRANCH_BASE="cleanup/refactor-upstream-main-prA-architecture"`
    - [x] `PRB_BRANCH_BASE="cleanup/refactor-upstream-main-prB-benchmark"`
    - [x] `PRC_BRANCH_BASE="cleanup/refactor-upstream-main-prC-smoke"`
    - [x] `FORK_REPO="PLeVasseur/up-streamer-rust"`
    - [x] `FORK_OWNER="PLeVasseur"`
    - [x] `FORK_BASE_BRANCH="main"`
    - [x] persist `CHECKPOINT_TAG_PREFIX`, `RESTACK_BRANCH_BASE`, `PR*_BRANCH_BASE`, and `FORK_*` values to `PROGRESS_FILE`.
  - [x] write initial summary header to `SUMMARY_REPORT` (date, repo, source branch, `BASE_SHA`, `SOURCE_SHA`).
  - [x] write/update progress seed in `PROGRESS_FILE` (`LAST_PHASE=phase1`, `LAST_COMMIT=none`, `LAST_SHA=$SOURCE_SHA`, `BASE_SHA`, `SOURCE_SHA`, `RESTACK_BRANCH`, `PRA_BRANCH`, `PRB_BRANCH`, `PRC_BRANCH`, `FORK_REPO`, `FORK_OWNER`, `FORK_BASE_BRANCH`).
  - [x] verify fork safety before publish path:
    - [x] `git remote get-url origin` matches `git@github.com:PLeVasseur/up-streamer-rust.git`.
    - [x] `git remote get-url upstream` matches `git@github.com:eclipse-uprotocol/up-streamer-rust.git`.
- [x] Create durable rollback refs before rewrite:
  - [x] `BACKUP_BRANCH="backup/pr-32-restack-$(date -u +%Y%m%dT%H%M%SZ)"`
  - [x] `BACKUP_TAG="backup-pr-32-restack-$(date -u +%Y%m%dT%H%M%SZ)"`
  - [x] `git branch "$BACKUP_BRANCH" "$SOURCE_SHA"`
  - [x] `git tag "$BACKUP_TAG" "$SOURCE_SHA"`
  - [x] `git push origin "$BACKUP_BRANCH"`
  - [x] `git push origin "$BACKUP_TAG"`
  - [x] `git ls-remote --heads origin "$BACKUP_BRANCH"`
  - [x] `git ls-remote --tags origin "$BACKUP_TAG"`
- [x] Persist rollback note in report:
  - [x] "If any step fails, `git switch cleanup/refactor-upstream-main && git reset --hard $BACKUP_BRANCH`, then restart Phase 2."
- [x] Update progress marker:
  - [x] set `LAST_PHASE=phase1_complete`, `BACKUP_BRANCH`, and `BACKUP_TAG` in `PROGRESS_FILE`.
  - [x] append checkpoint note with backup ref names to `SUMMARY_REPORT`.

## Phase 2 - Deterministic rewrite setup

- [x] Resolve rewrite branch name collision before create:
  - [x] default `RESTACK_BRANCH="$RESTACK_BRANCH_BASE"`
  - [x] if local branch exists, suffix with UTC timestamp (for example `pr-32-restack-work-20260214T123000Z`).
  - [x] if remote branch of same name exists, suffix with UTC timestamp.
- [x] Create rewrite branch from source tip:
  - [x] `git switch -c "$RESTACK_BRANCH" "$SOURCE_SHA"`
  - [x] persist resolved `RESTACK_BRANCH` to `PROGRESS_FILE`.
- [x] Materialize full branch delta as unstaged working changes:
  - [x] `git reset --soft "$BASE_SHA"`
  - [x] `git reset HEAD .`
- [x] Capture pre-rewrite inventories for proof:
  - [x] `git diff --name-status > "$OPENCODE_CONFIG_DIR/reports/pr-32-restack-pre-name-status.txt"`
  - [x] `git diff --stat > "$OPENCODE_CONFIG_DIR/reports/pr-32-restack-pre-stat.txt"`
  - [x] `git log --reverse --oneline "$BASE_SHA".."$SOURCE_SHA" > "$OPENCODE_CONFIG_DIR/reports/pr-32-restack-pre-commits.txt"`
- [x] Commit 0 scope derivation before any commit is created:
  - [x] build candidate list from files touching `log`/`env_logger` usage and related manifest swaps.
  - [x] classify each candidate as `finalizable_in_c0` or `defer_to_c2/c3/c5`.
  - [x] explicitly classify `example-streamer-uses/src/bin/*.rs` (except `common/mod.rs`) and `example-streamer-uses/README.md` as `defer_to_c5`.
  - [x] ensure `finalizable_in_c0` contains only files stageable by whole-file adds (no hunk surgery required).
  - [x] verify Commit 0 remains intentionally small (mechanical anchor commit, not broad migration sweep).
  - [x] if classification cannot avoid patch surgery for required files, stop and switch to forward-build fallback from `BASE_SHA` (construct commits incrementally rather than subtracting from final tree).
- [x] Update progress marker:
  - [x] set `LAST_PHASE=phase2_complete`, `LAST_COMMIT=none`, `LAST_SHA=$(git rev-parse HEAD)` in `PROGRESS_FILE`.

## Manifest mutation schedule (hard guardrail)

- [x] Root `Cargo.toml` mutation timing is enforced exactly:
  - [x] Commit 0: add `tracing` and `tracing-subscriber` workspace dependencies only.
  - [x] Commit 2: remove `subscription-cache` workspace member only.
  - [x] Commit 2: do **not** remove workspace `log`/`env_logger`/`async-std` yet.
  - [x] Commit 3: remove workspace `async-std` only after `utils/usubscription-static-file/Cargo.toml` no longer references it.
  - [x] Commit 4: add `utils/criterion-guardrail` workspace member.
  - [x] Commit 5: add `utils/transport-smoke-suite` workspace member.
  - [x] Commit 5: remove workspace `log` and `env_logger` only after final `example-streamer-uses` migration lands in this commit.
- [x] `up-streamer/Cargo.toml` mutation timing is enforced exactly:
  - [x] Commit 2: routing/rewire dependency changes only.
  - [x] Commit 2: do **not** add bench wiring (`criterion` dev-dependency or `[[bench]]`).
  - [x] Commit 4: add benchmark dependencies and `[[bench]]` wiring.
- [x] `example-streamer-uses/Cargo.toml` mutation timing is enforced exactly:
  - [x] Commit 0: add `tracing` dependency required for `common/mod.rs` migration.
  - [x] Commit 0: keep `log`/`env_logger` for deferred non-pure binaries.
  - [x] Commit 5: add `tracing-subscriber`, complete migration, and remove `log`/`env_logger`.
- [x] `utils/integration-test-utils/Cargo.toml` mutation timing is enforced exactly:
  - [x] Commit 0: add `tracing` dependency required for pure-file migration.
  - [x] Commit 0: keep `log`/`env_logger` for deferred files.
  - [x] Commit 3: add `tracing-subscriber`, complete migration, and remove `log`/`env_logger`.
- [x] `utils/usubscription-static-file/Cargo.toml` mutation timing is enforced exactly:
  - [x] Commit 2: remove `subscription-cache = { path = "../../subscription-cache" }` dependency only.
  - [x] Commit 3: remove `async-std`, migrate logging dependency to `tracing`, and add `[dev-dependencies] tokio`.
- [x] `configurable-streamer/Cargo.toml` mutation timing is enforced exactly:
  - [x] Commit 2: remove `log`/`env_logger`, add `tracing`/`tracing-subscriber`, and add `tokio` `signal` feature.
  - [x] No later commit re-touches this manifest unless required for compile fix and documented in `SUMMARY_REPORT`.
- [x] `example-streamer-implementations/Cargo.toml` mutation timing is enforced exactly:
  - [x] Commit 2: remove `log`/`env_logger`, add `tracing`/`tracing-subscriber`, and add `tokio` `signal` feature.
  - [x] No later commit re-touches this manifest unless required for compile fix and documented in `SUMMARY_REPORT`.
- [x] `up-linux-streamer-plugin/Cargo.toml` mutation timing is enforced exactly:
  - [x] Commit 2: remove `env_logger` and add `tracing-subscriber`.
  - [x] No later commit re-touches this manifest unless required for compile fix and documented in `SUMMARY_REPORT`.
- [x] If a manifest edit appears out of phase, stop and fix commit boundaries before continuing.

## Phase 3 - Reconstruct compile-safe commit stack (6 commits)

- [x] Common per-commit discipline (applies to Commit 0 through Commit 5):
  - [x] commit body must include: what changed, why this boundary exists, key review files, and mechanical-vs-behavioral note.
  - [x] after each commit, create a checkpoint tag `"$CHECKPOINT_TAG_PREFIX-cN"` (N = 0..5).
  - [x] after each commit, update `PROGRESS_FILE` with `LAST_PHASE=phase3`, `LAST_COMMIT=cN`, `LAST_SHA=$(git rev-parse HEAD)`.
  - [x] after each commit, append one-line status to `SUMMARY_REPORT` (commit label, SHA, pass/fail gates).
  - [x] set shared build cache once for worktree gates to avoid repeated cold builds:
    - [x] `export CARGO_TARGET_DIR="${CARGO_TARGET_DIR:-/tmp/pr32-shared-target}"`
    - [x] run gates sequentially (no parallel worktrees) to keep shared target usage safe.
  - [x] run all compile/test gates from an isolated detached worktree at `HEAD` snapshot (not from the dirty reconstruction worktree):
    - [x] `TMP_WT="$(mktemp -d /tmp/pr32-cN-XXXXXX)"`
    - [x] `git worktree add --detach "$TMP_WT" HEAD`
    - [x] run commit gate commands in `"$TMP_WT"`
    - [x] `git worktree remove "$TMP_WT" --force`
  - [x] initialize overlap artifacts before Commit 0 and run overlap subroutine immediately after each commit (see "Appendix A - Overlap check subroutine").
  - [x] if overlap subroutine finds disallowed overlap, stop immediately and rewrite boundary before next commit.

### Commit 0 - Mechanical log-to-tracing migration

- [x] Scope:
  - [x] stage only fully-finalizable migration files (Strategy A); defer entangled files to their owning later commits.
  - [x] stage exactly these source files:
    - [x] `example-streamer-uses/src/bin/common/mod.rs`
    - [x] `utils/integration-test-utils/src/integration_test_listeners.rs`
    - [x] `utils/integration-test-utils/src/up_client_failing_register.rs`
    - [x] `up-streamer/src/endpoint.rs`
  - [x] stage only supporting manifest changes needed for the above files:
    - [x] root `Cargo.toml`: add workspace `tracing` and `tracing-subscriber`
    - [x] `example-streamer-uses/Cargo.toml`: add `tracing` (retain `log`/`env_logger`)
    - [x] `utils/integration-test-utils/Cargo.toml`: add `tracing` (retain `log`/`env_logger`)
  - [x] add workspace `tracing` and `tracing-subscriber` if not already present.
  - [x] do **not** modify workspace member list in Commit 0.
  - [x] do **not** remove workspace `log`, `env_logger`, or `async-std` in Commit 0.
  - [x] explicitly exclude `subscription-cache/` from Commit 0 scope, including `subscription-cache/src/lib.rs`.
  - [x] explicitly treat `up-streamer/src/endpoint.rs` as finalized in Commit 0.
  - [x] explicitly exclude `example-streamer-uses/src/bin/*.rs` (except `common/mod.rs`) and `example-streamer-uses/README.md` from Commit 0.
  - [x] explicitly exclude known entangled migration files from Commit 0 (for example `up-streamer/src/ustreamer.rs`, `configurable-streamer/src/main.rs`, `example-streamer-implementations/src/bin/zenoh_someip.rs`, and mixed-hunk test files).
- [x] Guardrails:
  - [x] no architectural behavior changes in this commit.
  - [x] commit body marks this as mechanical and cross-cutting.
  - [x] commit body states this commit is intentionally small and establishes shared tracing dependencies for later commits.
  - [x] commit body notes that some sites remove logging instead of replacing it when final behavior no longer logs.
  - [x] stage by whole-file adds only (`git add <file>`); do not rely on interactive hunk surgery.
- [x] Gates:
  - [x] `git diff --name-only --cached`
  - [x] `git diff --stat --cached`
  - [x] `cargo check --workspace --all-targets`
  - [x] overlap check passes (exceptions only)
- [x] Crash/resume markers:
  - [x] save Commit 0 file list to `$OPENCODE_CONFIG_DIR/reports/pr-32-commit0-included-files.txt`.
  - [x] create tag `"$CHECKPOINT_TAG_PREFIX-c0"`.
  - [x] write `LAST_COMMIT=c0` marker to `PROGRESS_FILE`.

### Commit 1 - Observability vocabulary (leaf)

- [x] Scope:
  - [x] `up-streamer/src/observability/events.rs`
  - [x] `up-streamer/src/observability/fields.rs`
  - [x] `up-streamer/src/observability/mod.rs`
  - [x] minimal required `lib.rs` module exposure if needed
- [x] Guardrails:
  - [x] keep commit leaf-like and quickly reviewable.
  - [x] commit body names key files and expected reviewer focus.
- [x] Gates:
  - [x] staged scope checks
  - [x] `cargo check --workspace --all-targets`
  - [x] overlap check passes (exceptions only)
- [x] Crash/resume markers:
  - [x] create tag `"$CHECKPOINT_TAG_PREFIX-c1"`.
  - [x] write `LAST_COMMIT=c1` marker to `PROGRESS_FILE`.

### Commit 2 - Domain extraction + rewire + subscription-cache fold-in

- [x] Scope (collapsed by design):
  - [x] `up-streamer/src/routing/`
  - [x] `up-streamer/src/data_plane/`
  - [x] `up-streamer/src/control_plane/`
  - [x] `up-streamer/src/runtime/`
  - [x] `up-streamer/src/ustreamer.rs`
  - [x] required `up-streamer/src/lib.rs` wiring
  - [x] entrypoint/plugin wiring files impacted by module/API rewire
  - [x] manifest/workspace changes for module and crate ownership
  - [x] `subscription-cache` fold-in and crate removal as part of this same commit
  - [x] remove workspace-level `subscription-cache` member in this commit
  - [x] remove `subscription-cache` path dependency from `utils/usubscription-static-file/Cargo.toml` in this commit
  - [x] finalize manifest migrations in this commit for:
    - [x] `configurable-streamer/Cargo.toml`
    - [x] `example-streamer-implementations/Cargo.toml`
    - [x] `up-linux-streamer-plugin/Cargo.toml`
  - [x] keep workspace `log`, `env_logger`, and `async-std` in this commit (removed later per manifest schedule)
  - [x] do **not** add workspace members for `utils/criterion-guardrail` or `utils/transport-smoke-suite` in this commit
  - [x] do **not** add benchmark-only wiring in `up-streamer/Cargo.toml` in this commit
  - [x] do **not** include deferred smoke-infrastructure changes from `example-streamer-uses/` in this commit
  - [x] include minimal compile-safe API churn in legacy `up-streamer/tests/*.rs` files to keep `--all-targets` gate green; deterministic test refactors are deferred to Commit 3 with pre-approved overlap exceptions.
- [x] Guardrails:
  - [x] no later commit re-touches these files except explicit exception-list files.
  - [x] no later commit re-touches the three Commit-2-finalized manifests above unless a compile fix is required and documented.
  - [x] include copyright headers at file creation.
  - [x] commit body explains why this boundary is intentionally large.
- [x] Gates:
  - [x] staged scope checks
  - [x] verify no remaining `subscription-cache` path dependencies in workspace manifests:
    - [x] `rg -n 'subscription-cache\s*=\s*\{[^}]*path[^}]*subscription-cache[^}]*\}' --glob '**/Cargo.toml'` returns no matches.
  - [x] `cargo check --workspace --all-targets`
  - [x] overlap check passes (exceptions only)
- [x] Crash/resume markers:
  - [x] create tag `"$CHECKPOINT_TAG_PREFIX-c2"`.
  - [x] write `LAST_COMMIT=c2` marker to `PROGRESS_FILE`.

### Commit 3 - Test updates

- [x] Scope:
  - [x] `up-streamer/tests/`
  - [x] `utils/integration-test-utils/`
  - [x] `utils/usubscription-static-file/` test-related adjustments
  - [x] complete deferred logging migration for remaining `utils/integration-test-utils/src/*.rs` files.
  - [x] apply `utils/integration-test-utils/Cargo.toml` finalization (add `tracing-subscriber`; remove `log`/`env_logger` after source migration).
  - [x] apply `utils/usubscription-static-file/Cargo.toml` updates (remove `async-std`, migrate logging deps, add `[dev-dependencies] tokio`).
  - [x] remove workspace `async-std` from root `Cargo.toml` after crate-level removal lands.
- [x] Guardrails:
  - [x] body separates mechanical import/path churn from behavioral test changes.
  - [x] keep workspace `log`/`env_logger` in place for deferred `example-streamer-uses` migration in Commit 5.
- [x] Gates:
  - [x] staged scope checks
  - [x] `cargo check --workspace --all-targets`
  - [x] `cargo test --workspace`
  - [x] overlap check passes (exceptions only)
- [x] Crash/resume markers:
  - [x] create tag `"$CHECKPOINT_TAG_PREFIX-c3"`.
  - [x] write `LAST_COMMIT=c3` marker to `PROGRESS_FILE`.

### Commit 4 - Benchmark harness and CI guardrail

- [x] Scope:
  - [x] `up-streamer/src/benchmark_support.rs` (created here)
  - [x] `up-streamer/benches/`
  - [x] `utils/criterion-guardrail/`
  - [x] benchmark script/workflow files
  - [x] add `utils/criterion-guardrail` to workspace members in root `Cargo.toml`.
  - [x] add benchmark wiring in `up-streamer/Cargo.toml` (`criterion` dev-dependency and `[[bench]]`).
- [x] Guardrails:
  - [x] no subsequent commit modifies `benchmark_support.rs` for trivial fixups.
  - [x] body explains deterministic fixture strategy and CI intent.
- [x] Gates:
  - [x] staged scope checks
  - [x] `cargo check -p criterion-guardrail --all-targets`
  - [x] `cargo test -p criterion-guardrail --all-targets`
  - [x] `cargo check -p up-streamer --benches`
  - [x] overlap check passes (exceptions only)
- [x] Crash/resume markers:
  - [x] create tag `"$CHECKPOINT_TAG_PREFIX-c4"`.
  - [x] write `LAST_COMMIT=c4` marker to `PROGRESS_FILE`.

### Commit 5 - Smoke suite and fixture collapsing

- [ ] Scope:
  - [x] `utils/transport-smoke-suite/`
  - [x] smoke CI workflow files
  - [ ] `.gitattributes` entries for fixture collapsing
  - [x] deferred smoke-infrastructure updates in `example-streamer-uses/`:
    - [x] `example-streamer-uses/src/bin/*` readiness markers (`READY listener_registered`) and bounded sender CLI controls
    - [x] `example-streamer-uses/README.md` deterministic sender documentation
    - [x] `example-streamer-uses/Cargo.toml` finalization (add `tracing-subscriber`; remove `log`/`env_logger`)
  - [x] add `utils/transport-smoke-suite` to workspace members in root `Cargo.toml`.
  - [x] remove workspace `log` and `env_logger` from root `Cargo.toml` after deferred `example-streamer-uses` migration lands.
- [ ] Required `.gitattributes` rules:
  - [ ] `utils/transport-smoke-suite/tests/fixtures/** linguist-generated=true`
  - [ ] `utils/transport-smoke-suite/claims/** linguist-generated=true`
- [x] Guardrails:
  - [x] body calls out code-vs-fixture split for reviewers.
  - [x] body explicitly explains why `example-streamer-uses` updates land here (smoke determinism and readiness signaling).
- [x] Gates:
  - [x] staged scope checks
  - [x] `cargo check --workspace --all-targets`
  - [x] `cargo check -p transport-smoke-suite --all-targets`
  - [x] `cargo test -p transport-smoke-suite --tests`
  - [x] `cargo check -p example-streamer-uses --all-targets`
  - [x] overlap check passes (exceptions only)
- [x] Crash/resume markers:
  - [x] create tag `"$CHECKPOINT_TAG_PREFIX-c5"`.
  - [x] write `LAST_COMMIT=c5` marker to `PROGRESS_FILE`.

- [x] Phase completion marker:
  - [x] set `LAST_PHASE=phase3_complete`, `LAST_SHA=$(git rev-parse HEAD)` in `PROGRESS_FILE`.
  - [x] append phase-3 completion line to `SUMMARY_REPORT`.

## Appendix A - Overlap check subroutine (invoked from Phase 3, not sequential)

- [x] Initialize overlap audit artifacts (once per run):
  - [x] `OVERLAP_CUMULATIVE="$OPENCODE_CONFIG_DIR/reports/pr-32-overlap-cumulative.txt"`
  - [x] `OVERLAP_CURRENT="$OPENCODE_CONFIG_DIR/reports/pr-32-overlap-current.txt"`
  - [x] `OVERLAP_RAW="$OPENCODE_CONFIG_DIR/reports/pr-32-overlap-raw.txt"`
  - [x] `OVERLAP_DISALLOWED="$OPENCODE_CONFIG_DIR/reports/pr-32-overlap-disallowed.txt"`
  - [x] `OVERLAP_AUDIT="$OPENCODE_CONFIG_DIR/reports/pr-32-overlap-audit.md"`
  - [x] `APPROVED_SOURCE_OVERLAP="$OPENCODE_CONFIG_DIR/reports/pr-32-approved-source-overlap.txt"`
  - [x] `: > "$OVERLAP_CUMULATIVE"`
  - [x] create empty `APPROVED_SOURCE_OVERLAP` if it does not exist.
- [x] Repeated invocation checklist (run once after each commit):
  - [x] c0 overlap subroutine executed and logged
  - [x] c1 overlap subroutine executed and logged
  - [x] c2 overlap subroutine executed and logged
  - [x] c3 overlap subroutine executed and logged
  - [x] c4 overlap subroutine executed and logged
  - [x] c5 overlap subroutine executed and logged
- For each invocation `cN`, execute this command flow:
  - `git show --name-only --pretty='' HEAD | rg -v '^$' | sort -u > "$OVERLAP_CURRENT"`
  - `comm -12 "$OVERLAP_CUMULATIVE" "$OVERLAP_CURRENT" > "$OVERLAP_RAW" || true`
  - Build allowlist with:
    - wiring exceptions: any `Cargo.toml`, `Cargo.lock`, and optional `up-streamer/src/lib.rs`
    - optional source-file exceptions from `APPROVED_SOURCE_OVERLAP` (must be pre-approved with rationale)
  - filter `OVERLAP_RAW` into `OVERLAP_DISALLOWED` using active allowlist
  - `test ! -s "$OVERLAP_DISALLOWED"`
  - if disallowed overlap exists, stop immediately and fix boundary before next commit
  - `cat "$OVERLAP_CUMULATIVE" "$OVERLAP_CURRENT" | sort -u > "$OVERLAP_CUMULATIVE.tmp" && mv "$OVERLAP_CUMULATIVE.tmp" "$OVERLAP_CUMULATIVE"`
  - append overlap result line to `OVERLAP_AUDIT` (commit label, SHA, overlap count, disallowed count)
- [x] End-state confirmation report:
  - [x] write final commit-file matrix to `$OPENCODE_CONFIG_DIR/reports/pr-32-commit-file-overlap-final.txt`.
  - [x] append final overlap summary line to `SUMMARY_REPORT`.

## Phase 4 - Post-rewrite integrity and compilability proof

- [x] Final tree identity:
  - [x] `git diff --stat "$SOURCE_SHA"..HEAD` shows zero changes.
- [ ] Per-commit compilability proof:
  - [x] default rule: if every Phase 3 gate was executed in isolated detached worktree and logged, treat those logs as authoritative per-commit proof.
  - [ ] if any Phase 3 gate was skipped/interrupted, or logs are incomplete, run fallback detached recheck:
    - [ ] capture ordered commit list for c0..c5: `git rev-list --reverse "$BASE_SHA"..HEAD > "$OPENCODE_CONFIG_DIR/reports/pr-32-restack-commit-seq.txt"`.
    - [ ] run `cargo check --workspace --all-targets` at each listed SHA in detached HEAD mode, recording pass/fail in `SUMMARY_REPORT`.
    - [ ] restore branch context at end: `git switch "$RESTACK_BRANCH"`.
    - [ ] if any commit fails, stop and fix by rewriting from nearest checkpoint tag before continuing.
- [x] Commit quality proof:
  - [x] every commit has non-empty body with: what/why/key files/mechanical-vs-behavioral.
- [x] Copyright proof:
  - [x] no standalone header-fixup commit exists.
- [x] Progress markers:
  - [x] set `LAST_PHASE=phase4_complete`, `LAST_SHA=$(git rev-parse HEAD)` in `PROGRESS_FILE`.

## Phase 5 - Validation before publish

- [ ] PR A validation (full):
  - [x] `source build/envsetup.sh highest` (repo script for C++ stdlib include env setup)
  - [x] `cargo build`
  - [x] `cargo clippy --all-targets -- -W warnings -D warnings`
  - [x] `cargo fmt -- --check`
  - [x] `cargo test --workspace`
  - [x] bundled feature matrix checks:
    - [x] `cargo build --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport`
    - [x] `cargo clippy --features vsomeip-transport,bundled-vsomeip,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
  - [ ] unbundled feature matrix checks (when environment supports it):
    - [x] verify `VSOMEIP_INSTALL_PATH` points to valid install tree.
    - [ ] `cargo build --features vsomeip-transport,zenoh-transport,mqtt-transport`
    - [ ] `cargo clippy --features vsomeip-transport,zenoh-transport,mqtt-transport --all-targets -- -W warnings -D warnings`
    - [x] if unavailable, record explicit skip rationale in `SUMMARY_REPORT`.
- [x] PR B validation (targeted):
  - [x] `cargo check -p criterion-guardrail --all-targets`
  - [x] `cargo test -p criterion-guardrail --all-targets`
  - [x] `cargo check -p up-streamer --benches`
- [x] PR C validation (targeted):
  - [x] `cargo check --workspace --all-targets`
  - [x] `cargo check -p transport-smoke-suite --all-targets`
  - [x] `cargo test -p transport-smoke-suite --tests`
  - [x] `cargo check -p example-streamer-uses --all-targets`
- [x] Validation evidence:
  - [x] append command outcomes + key pass/fail lines to `SUMMARY_REPORT`.
  - [x] set `LAST_PHASE=phase5_complete` in `PROGRESS_FILE`.

## Phase 6 - Branch and PR topology (publish only after Phase 5 is green)

- [x] Resolve PR branch name collisions before creating branches:
  - [x] default names:
    - [x] `PRA_BRANCH="$PRA_BRANCH_BASE"`
    - [x] `PRB_BRANCH="$PRB_BRANCH_BASE"`
    - [x] `PRC_BRANCH="$PRC_BRANCH_BASE"`
  - [x] if local/remote name exists, suffix with UTC timestamp and record the resolved names in `SUMMARY_REPORT`.
  - [x] persist resolved `PRA_BRANCH`, `PRB_BRANCH`, and `PRC_BRANCH` to `PROGRESS_FILE`.
- [x] Verify fork base branch matches rewrite base before publishing:
  - [x] `git fetch origin "$FORK_BASE_BRANCH"`
  - [x] `FORK_BASE_SHA="$(git rev-parse origin/$FORK_BASE_BRANCH)"`
  - [x] `test "$FORK_BASE_SHA" = "$BASE_SHA"`
  - [x] if mismatch, stop with actionable message in `SUMMARY_REPORT` and sync fork base branch before continuing.
- [x] Create PR branches from reconstructed stack:
  - [x] `"$PRA_BRANCH"` includes commits 0-3
  - [x] `"$PRB_BRANCH"` includes commit 4 only (base PR A)
  - [x] `"$PRC_BRANCH"` includes commit 5 only (base PR A)
- [x] If cherry-pick is used for B/C:
  - [x] note SHA divergence explicitly in PR notes and report artifact.
- [x] Fork-only publish guardrail (no upstream PRs during remediation):
  - [x] push branches to `origin` only:
    - [x] `git push -u origin "$PRA_BRANCH"`
    - [x] `git push -u origin "$PRB_BRANCH"`
    - [x] `git push -u origin "$PRC_BRANCH"`
  - [x] do not push remediation branches to `upstream`.
  - [x] create PRs in fork repo only (`$FORK_REPO`).
- [x] Create PR A in fork repo (base `$FORK_BASE_BRANCH`) with explicit feedback-closure section:
  - [x] use `gh pr create --repo "$FORK_REPO" --base "$FORK_BASE_BRANCH" --head "$FORK_OWNER:$PRA_BRANCH" --title "..." --body "$(cat <<'EOF' ... EOF)"`.
  - [x] include commit-by-commit summary for commits 0-3 and closure notes for R1-R6.
- [x] Create PR B (base PR A branch):
  - [x] use `gh pr create --repo "$FORK_REPO" --base "$PRA_BRANCH" --head "$FORK_OWNER:$PRB_BRANCH" --title "..." --body "$(cat <<'EOF' ... EOF)"`.
  - [x] body states dependency on PR A and scope limited to benchmark commit.
- [x] Create PR C (base PR A branch):
  - [x] use `gh pr create --repo "$FORK_REPO" --base "$PRA_BRANCH" --head "$FORK_OWNER:$PRC_BRANCH" --title "..." --body "$(cat <<'EOF' ... EOF)"`.
  - [x] body states dependency on PR A and scope limited to smoke commit.
- [x] Record resulting PR URLs and branch names in `SUMMARY_REPORT`.
- [x] Progress markers:
  - [x] set `LAST_PHASE=phase6_complete`, `LAST_SHA=$(git rev-parse HEAD)` in `PROGRESS_FILE`.

## Appendix B - Stacked PR maintenance procedure (event-driven)

- [ ] If PR A receives changes:
  - [ ] update/rebase PR A and push to `origin` with `--force-with-lease`
  - [ ] rebase PR B onto updated PR A tip, then push to `origin` with `--force-with-lease`
  - [ ] rebase PR C onto updated PR A tip, then push to `origin` with `--force-with-lease`
  - [ ] keep PR updates in fork repo (`$FORK_REPO`), not `upstream`.
  - [ ] refresh PR bodies' feedback-closure notes (R1-R6) for all affected PRs
  - [ ] append refreshed SHAs/PR URLs to `SUMMARY_REPORT`

## Phase 7 - Crash/restart procedure (lightweight but explicit)

- [x] At start of any new session, recover state before running commands:
  - [x] read `PROGRESS_FILE` and `SUMMARY_REPORT`
  - [x] reuse persisted `CHECKPOINT_TAG_PREFIX`, `RESTACK_BRANCH`, `BACKUP_BRANCH`, `BASE_SHA`, `SOURCE_SHA`, resolved `PRA_BRANCH`/`PRB_BRANCH`/`PRC_BRANCH`, and `FORK_*` values from `PROGRESS_FILE`.
  - [x] verify current branch and `git rev-parse HEAD`
  - [x] compare current `HEAD` to `LAST_SHA` in `PROGRESS_FILE`
- [x] If `HEAD != LAST_SHA` and rewrite is incomplete:
  - [x] locate nearest checkpoint tag (`$CHECKPOINT_TAG_PREFIX-cN`) and inspect with `git show --no-patch`.
  - [x] either continue from checkpoint if consistent, or rollback to `$BACKUP_BRANCH` and restart at Phase 2.
- [ ] If rewrite is complete but PR creation incomplete:
  - [ ] resume at first unchecked item in Phase 6 using recorded branch names in `SUMMARY_REPORT`.
- [x] Record restart event in `SUMMARY_REPORT` (timestamp, prior `LAST_PHASE`, resumed phase).

## Completion criteria

- [ ] All reviewer traceability targets R1-R6 are checked with evidence artifacts.
- [x] Reconstructed stack has 6 commits (0-5) and each commit compiles at its own point.
- [x] Full validation (Phase 5) is green before any branch push/PR creation in Phase 6.
- [x] Final tree matches original source tip exactly (`SOURCE_SHA`) aside from commit history shape.
- [x] Unexpected cross-commit file overlap is zero outside the explicit exception list.
- [x] Commit 0 source-file overlap is zero by default; any approved source overlap is pre-declared with rationale in `$OPENCODE_CONFIG_DIR/reports/pr-32-approved-source-overlap.txt`.
- [x] Commit 0 remains a small mechanical anchor commit (4 source files plus required manifest additions).
- [x] `example-streamer-uses` behavioral smoke-infrastructure updates are deferred to Commit 5.
- [x] Commit 0 does not remove workspace `log`, `env_logger`, or `async-std`; removals occur in scheduled later commits (`async-std` in Commit 3, `log`/`env_logger` in Commit 5).
- [x] Commit 2 removes all dangling `subscription-cache` path dependencies from active workspace members.
- [x] Manifest schedule includes and enforces timing for all changed crate `Cargo.toml` files (including configurable-streamer, example-streamer-implementations, and up-linux-streamer-plugin).
- [ ] `.gitattributes` fixture-collapsing rules are present in smoke commit.
- [x] PR A/B/C are created with correct bases and dependency links.
- [x] PR A/B/C are created in fork repo (`$FORK_REPO`) and remediation branches are pushed to `origin` only (no upstream PRs/pushes).
- [x] Fork base branch SHA (`origin/$FORK_BASE_BRANCH`) matches `BASE_SHA` at PR creation time.
- [x] `SUMMARY_REPORT`, `PROGRESS_FILE`, and checkpoint tags are sufficient to resume in a fresh session.
