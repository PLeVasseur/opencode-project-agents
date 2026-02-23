# Domain-First Modularization and Naming Plan

## Objective

- [x] Re-center modularization around domain ownership and readability.
  - [x] Keep the `~500` LoC threshold as a rule of thumb, not a hard partition target.
  - [x] Remove naming artifacts created by line-cap-driven splitting (`part1`, `part2`, mixed `*_and_*` files).
  - [x] Preserve behavior while improving navigability and maintainability.

## Current Audit Snapshot

- [x] Inventory problematic naming and split patterns.
  - [x] Confirmed `*_partN.rs` naming appears across ingest and validate modules.
  - [x] Confirmed many mixed-concern `*_and_*` files across ingest, query, and validate.
  - [x] Confirmed composition is heavily `include!`-driven, obscuring module boundaries.
  - [x] Confirmed multiple files sit at or near the 500-line budget, indicating cap-driven splits.

- [x] Identify concrete cross-file cohesion issues.
  - [x] `coverage_freshness_part1.rs` depends on helpers located in `coverage_freshness_part2.rs`.
  - [x] `ListSemanticsMetrics` type and its computation are split awkwardly across fidelity part files.
  - [x] `tail_and_tests.rs` mixes production helper code and test code.

## Guiding Decisions

- [x] Adopt explicit module ownership by topic.
  - [x] Prefer module names that describe one responsibility (`metrics`, `checks`, `citation`, `io`, `parsing`, `output`).
  - [x] Avoid sequence-based names (`part1`, `part2`) except for temporary migration branches.
  - [x] Avoid combined names that hide boundary decisions (`*_and_*`).
  - [x] `include!()` is temporary scaffolding only and must be fully removed from the codebase.

- [x] Soften budget enforcement posture.
  - [x] Keep `scripts/check_file_size_budget.sh` default behavior in warning mode.
  - [x] Treat line budget breaches as prompts for review, not mandatory immediate splits.
  - [x] Require a short rationale only when a file stays large and cohesive by design.

- [x] Preserve runtime behavior and external contracts.
  - [x] No CLI argument or command behavior changes during modularization.
  - [x] No report schema changes during modularization.
  - [x] No SQL schema/contract changes during modularization.

- [x] Apply practical visibility policy during include removal.
  - [x] Prefer plain `pub` for shared items across files within a command module.
  - [x] Keep child modules private by default (`mod foo;`) so helpers are not exported via module paths unintentionally.
  - [x] Expose cross-module entry points via `mod.rs`/`lib.rs` facade re-exports.
  - [x] Use `pub(super)`/`pub(crate)` only when a narrower boundary is clearly useful.

## Size-Budget Handling for This Plan

- [x] Keep file-size budget checks explicitly non-gating for this refactor plan.
  - [x] Treat `scripts/check_file_size_budget.sh` output as informational only while domain regrouping is active.
  - [x] Do not split files solely to satisfy 500-line thresholds.
  - [x] Prefer cohesive domain modules even when files exceed legacy budget defaults.
  - [x] If the size script is run during this plan, run it in warn mode and record results without blocking phase progress.

## Scope

- [x] In scope
  - [x] Rename and regroup source files by domain/topic.
  - [x] Replace `include!`-centric flattening with explicit `mod` boundaries.
  - [x] Update docs/tooling language to reflect soft-size guidance.
  - [x] Drive `include!()` usage to zero across `src/**`.

- [x] Out of scope
  - [x] New functional features.
  - [x] Semantic quality threshold tuning.
  - [x] Data model changes unrelated to module organization.

## Work Plan

- [x] Phase 0: Baseline and Safety Net
  - [x] Capture current behavior baseline (`cargo check`, `cargo test`, existing smoke commands).
  - [x] Record deterministic query/report artifacts used for parity checks.
  - [x] Ensure the working tree is clean for only planned move/rename changes per phase.

- [x] Phase 1: Architecture Cleanup (replace `include!` layering)
  - [x] Convert command modules to explicit `mod` trees (no behavior changes).
  - [x] Keep command entrypoints thin (`run` orchestration only).
  - [x] Prefer migration-friendly visibility (`pub` for shared sibling symbols) and keep structure controlled through `mod.rs` facades.
  - [x] Establish include-removal migration pattern and apply it consistently per command subtree.
  - [x] Run post-refactor verification sequence and attach artifacts.

- [x] Phase 2: Query Domain Regrouping
  - [x] Replace `src/commands/query/semantic_and_fusion.rs` with topic modules.
    - [x] Create semantic retrieval module.
    - [x] Create fusion/ranking module (if distinct from output concerns).
  - [x] Split `src/commands/query/ranking_and_output.rs` by responsibility.
    - [x] Keep candidate ranking/dedup logic in ranking module.
    - [x] Keep JSON/text rendering in output module.
  - [x] Split `src/commands/query/hierarchy_and_citation.rs` by responsibility.
    - [x] Keep hierarchy traversal in hierarchy module.
    - [x] Keep citation formatting helpers in citation module.
  - [x] Keep `src/commands/query/pinpoint.rs` cohesive; split only if domain boundaries are clear.
  - [x] Run post-refactor verification sequence and attach artifacts.

- [x] Phase 3: Embed Domain Regrouping
  - [x] Rename `src/commands/embed/prelude.rs` to a domain-meaningful module (`types`, `model`, or `context`).
  - [x] Keep payload/store/run separation, but align naming with responsibility.
  - [x] Remove residual naming that implies ordering rather than ownership.
  - [x] Run post-refactor verification sequence and attach artifacts.

- [x] Phase 4: Ingest Domain Regrouping
  - [x] Replace sequence splits.
    - [x] Merge or regroup `table_parse_quality_part1.rs` and `table_parse_quality_part2.rs` into table parsing domain module(s).
  - [x] Replace mixed-concern names with topic names.
    - [x] `types_and_structured.rs` -> separate types and structured parsing modules.
    - [x] `ids_and_outline.rs` -> separate id/citation helpers and outline extraction (or regroup under extract).
    - [x] `page_extract_and_normalize.rs` -> extract/page pipeline modules as needed.
    - [x] `ocr_tools_and_manifest.rs` -> tooling/version/manifest helpers grouped by concern.
    - [x] `node_and_table_insert.rs` -> split node insertion from table child insertion if boundaries are strong.
    - [x] `paragraphs_and_list_parse.rs` -> separate paragraph parsing and list parsing if that improves cohesion.
    - [x] `list_note_requirement_insert.rs` -> split list/note insertion from requirement atom insertion if needed.
  - [x] Keep SQL parameter ordering and persisted string values unchanged.
  - [x] Run post-refactor verification sequence and attach artifacts.

- [x] Phase 5: Validate Domain Regrouping (highest impact)
  - [x] Replace sequence splits.
    - [x] `prelude_types_part1.rs` and `prelude_types_part2.rs` -> constants/models modules.
    - [x] `coverage_freshness_part1.rs` and `coverage_freshness_part2.rs` -> freshness/reference-eval/io modules.
    - [x] `fidelity_metrics_part1.rs` and `fidelity_metrics_part2.rs` -> metrics modules.
  - [x] Replace mixed-concern names.
    - [x] `stage_and_wp2_core.rs` -> wp2 gate/policy module.
    - [x] `checks_and_summary.rs` -> checks builder plus summary module(s).
    - [x] `invariants_and_hierarchy.rs` -> structural invariants module and hierarchy metrics module if needed.
    - [x] `tail_and_tests.rs` -> test-only module plus any production helper moved to a proper topic module.
  - [x] Keep check IDs, stage behavior, and report schema identical.
  - [x] Run post-refactor verification sequence and attach artifacts.

- [x] Phase 6: Semantic Quality Subtree Naming Cleanup
  - [x] Keep semantic quality feature grouping, but normalize names for readability.
    - [x] Remove residual utility-only naming where it leaks implementation details (`semantic_quality_shared.rs`, `semantic_quality_pinpoint_utils.rs`) if better domain names are available.
    - [x] Keep nested pinpoint modules cohesive and explicit.
  - [x] Avoid further splits solely to satisfy file length if cohesion is good.
  - [x] Run post-refactor verification sequence and attach artifacts.

- [x] Phase 7: Policy and Documentation Update
  - [x] Update maintainability docs to describe soft budget guidance.
    - [x] Update `scripts/README.md` wording from cap-centric to cohesion-centric guidance.
    - [x] Clarify when exceptions are expected and acceptable.
  - [x] Update `scripts/check_file_size_budget.sh` help/output language to reinforce advisory-first behavior.
  - [x] Add a brief naming convention section for module/file naming.

- [x] Phase 8: Verification and Closeout
  - [x] Run final verification matrix.
    - [x] `cargo check`
    - [x] `cargo test`
    - [x] relevant smoke and determinism checks
  - [x] Compare normalized parity artifacts to baseline.
  - [x] Confirm no `*_partN.rs` and no avoidable `*_and_*` names remain in command modules.
  - [x] Record final decisions and any intentional large-file rationale.

## Phase-to-Commit Plan (Conventional Commits)

- [x] Phase 0 commits (baseline only)
  - [x] `chore(plan): capture domain-first modularization baseline`.
    - [x] Record baseline commands run and artifact paths.
    - [x] Record known pre-existing dirty files excluded from this effort.

- [x] Phase 1 commits (architecture cleanup)
  - [x] `refactor(commands): replace include-based composition with explicit modules`.
    - [x] Convert one command tree at a time (query, embed, ingest, validate).
    - [x] Keep behavior-preserving moves only in this commit.
  - [x] `refactor(commands): establish module facade re-exports after extraction`.
    - [x] Use `mod.rs`/`lib.rs` to expose curated shared symbols.
    - [x] Avoid visibility-scope churn unless it enforces a meaningful boundary.

- [x] Phase 2 commits (query)
  - [x] `refactor(query): split semantic, fusion, ranking, output modules by domain`.
    - [x] Isolate retrieval/fusion/ranking/output concerns.
  - [x] `refactor(query): separate hierarchy traversal from citation formatting`.
    - [x] Move hierarchy helpers and citation helpers into dedicated modules.
  - [x] `refactor(query): normalize query module filenames to domain names`.
    - [x] Remove `*_and_*` naming artifacts in `src/commands/query`.

- [x] Phase 3 commits (embed)
  - [x] `refactor(embed): rename prelude module to domain-specific naming`.
    - [x] Keep functionality and wire-up unchanged.
  - [x] `refactor(embed): align module boundaries with payload/store/run responsibilities`.
    - [x] Ensure naming reflects ownership, not ordering.

- [x] Phase 4 commits (ingest)
  - [x] `refactor(ingest): replace part-suffixed table parsing modules`.
    - [x] Remove `table_parse_quality_part1.rs` / `table_parse_quality_part2.rs` naming.
  - [x] `refactor(ingest): split mixed-concern ingest modules by topic`.
    - [x] Address `types_and_structured`, `ids_and_outline`, `page_extract_and_normalize`, `ocr_tools_and_manifest`.
  - [x] `refactor(ingest): normalize insertion and parser module naming`.
    - [x] Address `node_and_table_insert`, `paragraphs_and_list_parse`, `list_note_requirement_insert`.

- [x] Phase 5 commits (validate)
  - [x] `refactor(validate): replace prelude/part module names with constants and models`.
    - [x] Remove `prelude_types_part1.rs` / `prelude_types_part2.rs`.
  - [x] `refactor(validate): regroup freshness and reference evaluation modules`.
    - [x] Remove `coverage_freshness_part1.rs` / `coverage_freshness_part2.rs`.
  - [x] `refactor(validate): regroup fidelity metrics into topic modules`.
    - [x] Remove `fidelity_metrics_part1.rs` / `fidelity_metrics_part2.rs`.
  - [x] `refactor(validate): separate wp2 checks, summary, and test-only modules`.
    - [x] Replace `stage_and_wp2_core`, `checks_and_summary`, `tail_and_tests` naming.

- [x] Phase 6 commits (semantic quality subtree)
  - [x] `refactor(validate): normalize semantic quality helper module names`.
    - [x] Replace residual utility-style names where domain names are clearer.
  - [x] `refactor(validate): preserve semantic quality boundaries while reducing naming noise`.
    - [x] Keep pinpoint subtree explicit and cohesive.

- [x] Phase 7 commits (policy + docs)
  - [x] `docs(maintainability): document size limits as heuristics`.
    - [x] Update `scripts/README.md` wording to cohesion-first guidance.
  - [x] `chore(scripts): adjust size-budget messaging to advisory-first language`.
    - [x] Keep enforcement mode opt-in.
  - [x] `docs(naming): add module naming conventions`.
    - [x] Add concise do/don't examples.

- [x] Phase 8 commits (verification + closeout)
  - [x] `test(modularization): run full parity verification matrix after regrouping`.
    - [x] Record command outputs and artifact paths.
  - [x] `docs(plan): record closeout status and residual rationale`.
    - [x] Mark completed checklist items and link evidence.

## Dual-Pass Acceptance Model

- [x] Pass A: Refactor Safety Pass (RSP) [required for each refactor commit/phase]
  - [x] `cargo check` passes.
  - [x] Targeted tests pass (or `cargo test` when no focused target exists).
  - [x] `scripts/smoke_part6.sh` passes.
  - [x] `SMOKE_DETERMINISM=1 scripts/smoke_part6.sh` passes.
  - [x] If query retrieval/ranking/fusion/citation code changed, `BENCH_PROFILE=quick scripts/benchmark_query_modes.sh` is valid (`.overall.valid == true`) and report path is captured.
  - [x] No schema or CLI contract diffs appear in move/rename-only commits.
  - [x] No new failing check IDs appear versus the phase baseline.

- [x] Pass B: Quality Hard-Gate Pass (QGP) [run every phase; must be green at final closeout]
  - [x] `PART=6 MAX_PAGES=60 WP2_GATE_STAGE=A scripts/refresh_quality_artifacts.sh` is executed and artifact paths are captured.
  - [x] `WP2_GATE_STAGE=B cargo run -- validate --cache-root .cache/iso26262` is executed and report status is captured.
  - [x] Stage B `non_passing_checks` list is recorded explicitly for each phase.
  - [x] Full-target hard-gate run is executed at phase boundary for truth data:
    - [x] `FULL_TARGET_SET=1 TARGET_PARTS="2 6 8 9" WP2_GATE_STAGE=A scripts/refresh_quality_artifacts.sh`
    - [x] `WP2_GATE_STAGE=B cargo run -- validate --cache-root .cache/iso26262`
  - [x] QGP is green only when report status is `passed` and `summary.failed == 0`.

- [x] Phase progression policy (RSP and QGP are separate pass types)
  - [x] RSP must pass before accepting a refactor commit.
  - [x] QGP must be executed and recorded at least once per phase.
  - [x] If QGP remains red due to pre-existing conditions, continue only with explicit no-worsening evidence versus baseline.
  - [x] Final modularization closeout requires QGP green.

## Regression Gate Integration (Large Refactors)

- [x] Use regression gate artifacts as primary no-regression evidence for large modularization phases.
  - [x] Phases 2-6 (`query`, `embed`, `ingest`, `validate`, semantic-quality cleanup) require regression mode `full`.
  - [x] `lite` mode is allowed only for local intermediate checkpoints and never for phase closeout.
  - [x] Phase closeout requires `scripts/regression_compare.sh --run-id <run_id> --mode full` with gate status `PASS`.
  - [x] Record compare artifacts (`drift_report.json`, `drift_report.md`, `gate_status.txt`) in phase notes.
  - [x] Keep quick/full Stage B report summaries from compare output for traceability.

## Include Macro Sunset Policy

- [x] Treat `include!()` elimination as a first-class modularization objective.
  - [x] New modularization work must not introduce additional `include!()` calls.
  - [x] Touched command subtrees must end each phase with zero `include!()` usage.
  - [x] Final closeout requires zero `include!()` usage anywhere under `src/`.

- [x] Track include burn-down as explicit evidence.
  - [x] Record baseline include count before phase work.
  - [x] Record post-phase include count after verification.
  - [x] Include count deltas are captured in phase notes.

## Baseline and Drift Controls

- [x] Capture phase baseline before first refactor commit in the phase
  - [x] Record baseline report path, run ID, and stage policy from `extraction_quality_report.json`.
  - [x] Record baseline `non_passing_checks` (expected known failures tracked separately).
  - [x] Record baseline freshness summary (`stale_parts`, `full_target_cycle_run_id`).
  - [x] Record baseline citation parity metrics (`top1_parity`, `top3_containment`, `page_range_parity`).
  - [x] Record baseline semantic quality metrics (nDCG/recall/MRR/determinism) and benchmark report path when query code is touched.

- [x] Enforce no-worsening policy after each phase
  - [x] No new failed check IDs are introduced.
  - [x] Existing failed checks do not worsen without explicit, written rationale.
  - [x] Citation parity and semantic quality metrics stay within defined drift budgets.
  - [x] Determinism outputs remain stable under repeated runs.

- [x] Define and apply drift budgets consistently
  - [x] Require exact equality for deterministic identity fields (check IDs, anchor IDs, stable citation fields).
  - [x] Use small bounded tolerances for aggregate metrics (for example p95 latency and nDCG deltas).
  - [x] Any delta outside budget blocks progression until resolved or explicitly approved with rationale.

## Post-Refactor Verification Sequence

- [x] Run this sequence after each refactor phase (Phase 1 through Phase 6), executing both pass types
  - [x] Step 0: baseline snapshot
    - [x] Create or confirm `<run_id>` for the phase.
    - [x] `scripts/regression_capture.sh --run-id <run_id> --phase before --mode full`
  - [x] Step 1: refactor implementation
    - [x] Apply only phase-scoped domain refactor changes.
    - [x] Keep unrelated feature work and threshold changes out of this phase.
  - [x] Step 2: post-change snapshot
    - [x] `scripts/regression_capture.sh --run-id <run_id> --phase after --mode full`
  - [x] Step 3: deterministic compare and gate decision
    - [x] `scripts/regression_compare.sh --run-id <run_id> --mode full --expect-status PASS`
    - [x] Confirm compare gate output is `PASS`.
  - [x] Step 4: explicit quality gate recording
    - [x] Record quick Stage B before/after status and `non_passing_checks`.
    - [x] Record full-target Stage B before/after status and `non_passing_checks`.
    - [x] Capture benchmark p95/p99 drift summary from compare report.
  - [x] Step 5: include-removal gate
    - [x] Record `rg "include!\(" src -n | wc -l` baseline and post-phase counts.
    - [x] Confirm touched command subtree contains zero `include!()` usage.
    - [x] Block phase closeout if touched subtree still relies on `include!()` without approved exception.
  - [x] Step 6: artifact recording and go/no-go decision
    - [x] Record all command outcomes and artifact paths in phase notes.
    - [x] Confirm RSP status and QGP status separately (both required; different meaning).
    - [x] Stop progression if compare is `WARN`/`FAIL` unless an approved override is documented.

## New Session Bootstrap Checklist

- [x] Session setup
  - [x] `printenv OPENCODE_CONFIG_DIR` and confirm plan path.
  - [x] Confirm working branch policy (`main` unless explicitly overridden).
  - [x] Capture `git status --short` for both implementation repo and config repo.
  - [x] Generate and record a unique `<run_id>` for the active refactor phase.
  - [x] Confirm regression capture mode is `full` for large refactor phases.
  - [x] Record expected artifact location under `.cache/iso26262/regression/<run_id>/`.

- [x] Workspace hygiene
  - [x] Identify pre-existing unrelated changes and exclude them from staged commits.
  - [x] Confirm only intended files are staged for each commit.
  - [x] Avoid broad `git add .` in multi-project worktrees.

- [x] Execution control
  - [x] Start at the next unchecked phase item only.
  - [x] Keep one active phase at a time.
  - [x] Stop immediately on parity regression; fix before continuing.

- [x] Evidence and handoff
  - [x] Record completed commands and artifact paths in phase notes.
  - [x] Update checklist statuses after each commit/phase.
  - [x] Leave explicit next action and next commit target at session end.

## Proposed Naming Targets

- [x] Query module naming targets
  - [x] `semantic_and_fusion.rs` -> `semantic_retrieval.rs` + `fusion.rs` (or equivalent domain names).
  - [x] `ranking_and_output.rs` -> `ranking.rs` + `output.rs`.
  - [x] `hierarchy_and_citation.rs` -> `hierarchy.rs` + `citation.rs`.

- [x] Ingest module naming targets
  - [x] `table_parse_quality_part1.rs`/`table_parse_quality_part2.rs` -> `table_parsing.rs` (or `table/*`).
  - [x] `types_and_structured.rs` -> `types.rs` + `structured_parser.rs`.
  - [x] `ids_and_outline.rs` -> `ids.rs` + `outline_extract.rs`.
  - [x] `page_extract_and_normalize.rs` -> `page_extract.rs` + `page_normalize.rs`.
  - [x] `ocr_tools_and_manifest.rs` -> `ocr.rs` + `tool_versions.rs` + `manifest_helpers.rs` (as needed).

- [x] Validate module naming targets
  - [x] `prelude_types_part1.rs`/`prelude_types_part2.rs` -> `constants.rs` + `models.rs`.
  - [x] `coverage_freshness_part1.rs`/`coverage_freshness_part2.rs` -> `freshness.rs` + `reference_eval.rs` + `io.rs`.
  - [x] `fidelity_metrics_part1.rs`/`fidelity_metrics_part2.rs` -> `metrics/extraction.rs`, `metrics/semantics.rs`, etc.
  - [x] `stage_and_wp2_core.rs` -> `wp2_gate.rs`.
  - [x] `checks_and_summary.rs` -> `checks.rs` + `summary.rs`.
  - [x] `tail_and_tests.rs` -> `tests.rs` + production helper relocation.

- [x] Embed module naming targets
  - [x] `prelude.rs` -> topic-specific module (`types.rs`/`context.rs`) based on final ownership.

## Acceptance Criteria

- [x] Module/file names reflect domain ownership rather than split order.
  - [x] No command module files named `*_partN.rs`.
  - [x] No avoidable mixed-concern `*_and_*` names in active command paths.

- [x] Size guidance is explicitly soft and policy-aligned.
  - [x] Documentation describes line limits as heuristics.
  - [x] Tooling language defaults to advisory behavior.

- [x] Behavior parity is maintained.
  - [x] Command behavior unchanged for ingest/embed/query/validate workflows.
  - [x] Quality report schema and check semantics unchanged.
  - [x] Determinism and smoke baselines remain stable.
  - [x] Pass A (RSP) and Pass B (QGP) evidence exists for every refactor phase.
  - [x] For Phases 2-6, full regression artifacts exist under `.cache/iso26262/regression/<run_id>/`.
  - [x] For Phases 2-6, `compare/gate_status.txt` is `PASS` at phase closeout.
  - [x] Final closeout occurs only when QGP is green (`status == passed`, `summary.failed == 0`).

- [x] Include elimination is complete.
  - [x] `rg "include!\(" src -n` returns no matches.
  - [x] Command module boundaries are expressed via explicit `mod` trees and imports.

## Closeout Evidence

- [x] Phase commit sequence captured on `main`:
  - [x] Phase 1 include-removal commits: `7cf8860`, `870e86e`, `cf049bc`, `0304028`.
  - [x] Phase 2-6 naming/domain commits: `5d9f16b`, `5a46150`, `6a595fd`, `79f4b19`.
  - [x] Phase 7 policy/docs commits: `1372914`, `6ce323e`.
- [x] Phase regression compare gates are `PASS`:
  - [x] `.cache/iso26262/regression/mod-phase2-query/compare/gate_status.txt`
  - [x] `.cache/iso26262/regression/mod-phase3-embed/compare/gate_status.txt`
  - [x] `.cache/iso26262/regression/mod-phase4-ingest/compare/gate_status.txt`
  - [x] `.cache/iso26262/regression/mod-phase4-ingest-naming/compare/gate_status.txt`
  - [x] `.cache/iso26262/regression/mod-phase5-validate/compare/gate_status.txt`
  - [x] `.cache/iso26262/regression/mod-phase5-validate-naming/compare/gate_status.txt`
  - [x] `.cache/iso26262/regression/mod-phase6-semantic-naming/compare/gate_status.txt`
  - [x] `.cache/iso26262/regression/mod-phase8-closeout/compare/gate_status.txt`
- [x] Final hard-gate validation is green:
  - [x] `.cache/iso26262/manifests/extraction_quality_report.json` reports `status: passed` and `summary.failed: 0`.
- [x] Naming/include cleanup checks at closeout:
  - [x] No `include!()` usage under `src/**`.
  - [x] No `*_partN.rs` files under `src/commands/**`.
  - [x] No avoidable `*_and_*.rs` files under `src/commands/**`.

## Execution Order

- [x] Recommended sequence
  - [x] Query cleanup (lowest migration risk).
  - [x] Embed cleanup.
  - [x] Ingest cleanup.
  - [x] Validate cleanup (largest/highest coupling).
  - [x] Docs and policy language updates.
  - [x] Final verification and closeout.
