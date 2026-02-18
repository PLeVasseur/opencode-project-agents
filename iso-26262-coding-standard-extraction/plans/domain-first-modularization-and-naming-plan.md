# Domain-First Modularization and Naming Plan

## Objective

- [ ] Re-center modularization around domain ownership and readability.
  - [ ] Keep the `~500` LoC threshold as a rule of thumb, not a hard partition target.
  - [ ] Remove naming artifacts created by line-cap-driven splitting (`part1`, `part2`, mixed `*_and_*` files).
  - [ ] Preserve behavior while improving navigability and maintainability.

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

- [ ] Adopt explicit module ownership by topic.
  - [ ] Prefer module names that describe one responsibility (`metrics`, `checks`, `citation`, `io`, `parsing`, `output`).
  - [ ] Avoid sequence-based names (`part1`, `part2`) except for temporary migration branches.
  - [ ] Avoid combined names that hide boundary decisions (`*_and_*`).

- [ ] Soften budget enforcement posture.
  - [ ] Keep `scripts/check_file_size_budget.sh` default behavior in warning mode.
  - [ ] Treat line budget breaches as prompts for review, not mandatory immediate splits.
  - [ ] Require a short rationale only when a file stays large and cohesive by design.

- [ ] Preserve runtime behavior and external contracts.
  - [ ] No CLI argument or command behavior changes during modularization.
  - [ ] No report schema changes during modularization.
  - [ ] No SQL schema/contract changes during modularization.

## Scope

- [ ] In scope
  - [ ] Rename and regroup source files by domain/topic.
  - [ ] Replace `include!`-centric flattening with explicit `mod` boundaries.
  - [ ] Update docs/tooling language to reflect soft-size guidance.

- [ ] Out of scope
  - [ ] New functional features.
  - [ ] Semantic quality threshold tuning.
  - [ ] Data model changes unrelated to module organization.

## Work Plan

- [ ] Phase 0: Baseline and Safety Net
  - [ ] Capture current behavior baseline (`cargo check`, `cargo test`, existing smoke commands).
  - [ ] Record deterministic query/report artifacts used for parity checks.
  - [ ] Ensure the working tree is clean for only planned move/rename changes per phase.

- [ ] Phase 1: Architecture Cleanup (replace `include!` layering)
  - [ ] Convert command modules to explicit `mod` trees (no behavior changes).
  - [ ] Keep command entrypoints thin (`run` orchestration only).
  - [ ] Restrict visibility (`pub(crate)`/`pub(super)`) to prevent accidental API sprawl.

- [ ] Phase 2: Query Domain Regrouping
  - [ ] Replace `src/commands/query/semantic_and_fusion.rs` with topic modules.
    - [ ] Create semantic retrieval module.
    - [ ] Create fusion/ranking module (if distinct from output concerns).
  - [ ] Split `src/commands/query/ranking_and_output.rs` by responsibility.
    - [ ] Keep candidate ranking/dedup logic in ranking module.
    - [ ] Keep JSON/text rendering in output module.
  - [ ] Split `src/commands/query/hierarchy_and_citation.rs` by responsibility.
    - [ ] Keep hierarchy traversal in hierarchy module.
    - [ ] Keep citation formatting helpers in citation module.
  - [ ] Keep `src/commands/query/pinpoint.rs` cohesive; split only if domain boundaries are clear.

- [ ] Phase 3: Embed Domain Regrouping
  - [ ] Rename `src/commands/embed/prelude.rs` to a domain-meaningful module (`types`, `model`, or `context`).
  - [ ] Keep payload/store/run separation, but align naming with responsibility.
  - [ ] Remove residual naming that implies ordering rather than ownership.

- [ ] Phase 4: Ingest Domain Regrouping
  - [ ] Replace sequence splits.
    - [ ] Merge or regroup `table_parse_quality_part1.rs` and `table_parse_quality_part2.rs` into table parsing domain module(s).
  - [ ] Replace mixed-concern names with topic names.
    - [ ] `types_and_structured.rs` -> separate types and structured parsing modules.
    - [ ] `ids_and_outline.rs` -> separate id/citation helpers and outline extraction (or regroup under extract).
    - [ ] `page_extract_and_normalize.rs` -> extract/page pipeline modules as needed.
    - [ ] `ocr_tools_and_manifest.rs` -> tooling/version/manifest helpers grouped by concern.
    - [ ] `node_and_table_insert.rs` -> split node insertion from table child insertion if boundaries are strong.
    - [ ] `paragraphs_and_list_parse.rs` -> separate paragraph parsing and list parsing if that improves cohesion.
    - [ ] `list_note_requirement_insert.rs` -> split list/note insertion from requirement atom insertion if needed.
  - [ ] Keep SQL parameter ordering and persisted string values unchanged.

- [ ] Phase 5: Validate Domain Regrouping (highest impact)
  - [ ] Replace sequence splits.
    - [ ] `prelude_types_part1.rs` and `prelude_types_part2.rs` -> constants/models modules.
    - [ ] `coverage_freshness_part1.rs` and `coverage_freshness_part2.rs` -> freshness/reference-eval/io modules.
    - [ ] `fidelity_metrics_part1.rs` and `fidelity_metrics_part2.rs` -> metrics modules.
  - [ ] Replace mixed-concern names.
    - [ ] `stage_and_wp2_core.rs` -> wp2 gate/policy module.
    - [ ] `checks_and_summary.rs` -> checks builder plus summary module(s).
    - [ ] `invariants_and_hierarchy.rs` -> structural invariants module and hierarchy metrics module if needed.
    - [ ] `tail_and_tests.rs` -> test-only module plus any production helper moved to a proper topic module.
  - [ ] Keep check IDs, stage behavior, and report schema identical.

- [ ] Phase 6: Semantic Quality Subtree Naming Cleanup
  - [ ] Keep semantic quality feature grouping, but normalize names for readability.
    - [ ] Remove residual utility-only naming where it leaks implementation details (`semantic_quality_shared.rs`, `semantic_quality_pinpoint_utils.rs`) if better domain names are available.
    - [ ] Keep nested pinpoint modules cohesive and explicit.
  - [ ] Avoid further splits solely to satisfy file length if cohesion is good.

- [ ] Phase 7: Policy and Documentation Update
  - [ ] Update maintainability docs to describe soft budget guidance.
    - [ ] Update `scripts/README.md` wording from cap-centric to cohesion-centric guidance.
    - [ ] Clarify when exceptions are expected and acceptable.
  - [ ] Update `scripts/check_file_size_budget.sh` help/output language to reinforce advisory-first behavior.
  - [ ] Add a brief naming convention section for module/file naming.

- [ ] Phase 8: Verification and Closeout
  - [ ] Run final verification matrix.
    - [ ] `cargo check`
    - [ ] `cargo test`
    - [ ] relevant smoke and determinism checks
  - [ ] Compare normalized parity artifacts to baseline.
  - [ ] Confirm no `*_partN.rs` and no avoidable `*_and_*` names remain in command modules.
  - [ ] Record final decisions and any intentional large-file rationale.

## Phase-to-Commit Plan (Conventional Commits)

- [ ] Phase 0 commits (baseline only)
  - [ ] `chore(plan): capture domain-first modularization baseline`.
    - [ ] Record baseline commands run and artifact paths.
    - [ ] Record known pre-existing dirty files excluded from this effort.

- [ ] Phase 1 commits (architecture cleanup)
  - [ ] `refactor(commands): replace include-based composition with explicit modules`.
    - [ ] Convert one command tree at a time (query, embed, ingest, validate).
    - [ ] Keep behavior-preserving moves only in this commit.
  - [ ] `refactor(commands): tighten internal visibility after module extraction`.
    - [ ] Apply `pub(crate)`/`pub(super)` where appropriate.
    - [ ] Avoid introducing new public APIs.

- [ ] Phase 2 commits (query)
  - [ ] `refactor(query): split semantic, fusion, ranking, output modules by domain`.
    - [ ] Isolate retrieval/fusion/ranking/output concerns.
  - [ ] `refactor(query): separate hierarchy traversal from citation formatting`.
    - [ ] Move hierarchy helpers and citation helpers into dedicated modules.
  - [ ] `refactor(query): normalize query module filenames to domain names`.
    - [ ] Remove `*_and_*` naming artifacts in `src/commands/query`.

- [ ] Phase 3 commits (embed)
  - [ ] `refactor(embed): rename prelude module to domain-specific naming`.
    - [ ] Keep functionality and wire-up unchanged.
  - [ ] `refactor(embed): align module boundaries with payload/store/run responsibilities`.
    - [ ] Ensure naming reflects ownership, not ordering.

- [ ] Phase 4 commits (ingest)
  - [ ] `refactor(ingest): replace part-suffixed table parsing modules`.
    - [ ] Remove `table_parse_quality_part1.rs` / `table_parse_quality_part2.rs` naming.
  - [ ] `refactor(ingest): split mixed-concern ingest modules by topic`.
    - [ ] Address `types_and_structured`, `ids_and_outline`, `page_extract_and_normalize`, `ocr_tools_and_manifest`.
  - [ ] `refactor(ingest): normalize insertion and parser module naming`.
    - [ ] Address `node_and_table_insert`, `paragraphs_and_list_parse`, `list_note_requirement_insert`.

- [ ] Phase 5 commits (validate)
  - [ ] `refactor(validate): replace prelude/part module names with constants and models`.
    - [ ] Remove `prelude_types_part1.rs` / `prelude_types_part2.rs`.
  - [ ] `refactor(validate): regroup freshness and reference evaluation modules`.
    - [ ] Remove `coverage_freshness_part1.rs` / `coverage_freshness_part2.rs`.
  - [ ] `refactor(validate): regroup fidelity metrics into topic modules`.
    - [ ] Remove `fidelity_metrics_part1.rs` / `fidelity_metrics_part2.rs`.
  - [ ] `refactor(validate): separate wp2 checks, summary, and test-only modules`.
    - [ ] Replace `stage_and_wp2_core`, `checks_and_summary`, `tail_and_tests` naming.

- [ ] Phase 6 commits (semantic quality subtree)
  - [ ] `refactor(validate): normalize semantic quality helper module names`.
    - [ ] Replace residual utility-style names where domain names are clearer.
  - [ ] `refactor(validate): preserve semantic quality boundaries while reducing naming noise`.
    - [ ] Keep pinpoint subtree explicit and cohesive.

- [ ] Phase 7 commits (policy + docs)
  - [ ] `docs(maintainability): document size limits as heuristics`.
    - [ ] Update `scripts/README.md` wording to cohesion-first guidance.
  - [ ] `chore(scripts): adjust size-budget messaging to advisory-first language`.
    - [ ] Keep enforcement mode opt-in.
  - [ ] `docs(naming): add module naming conventions`.
    - [ ] Add concise do/don't examples.

- [ ] Phase 8 commits (verification + closeout)
  - [ ] `test(modularization): run full parity verification matrix after regrouping`.
    - [ ] Record command outputs and artifact paths.
  - [ ] `docs(plan): record closeout status and residual rationale`.
    - [ ] Mark completed checklist items and link evidence.

## Per-Phase Parity Gates

- [ ] Gate for each commit slice
  - [ ] `cargo check` passes before proceeding.
  - [ ] Targeted tests for touched area pass.
  - [ ] No schema or CLI contract diffs in move/rename commits.

- [ ] Gate for each phase boundary
  - [ ] `cargo test` passes.
  - [ ] Relevant smoke commands pass.
  - [ ] Determinism/parity probe outputs are unchanged after normalization.
  - [ ] Any deviation is documented with explicit rationale and follow-up action.

## New Session Bootstrap Checklist

- [ ] Session setup
  - [ ] `printenv OPENCODE_CONFIG_DIR` and confirm plan path.
  - [ ] Confirm working branch policy (`main` unless explicitly overridden).
  - [ ] Capture `git status --short` for both implementation repo and config repo.

- [ ] Workspace hygiene
  - [ ] Identify pre-existing unrelated changes and exclude them from staged commits.
  - [ ] Confirm only intended files are staged for each commit.
  - [ ] Avoid broad `git add .` in multi-project worktrees.

- [ ] Execution control
  - [ ] Start at the next unchecked phase item only.
  - [ ] Keep one active phase at a time.
  - [ ] Stop immediately on parity regression; fix before continuing.

- [ ] Evidence and handoff
  - [ ] Record completed commands and artifact paths in phase notes.
  - [ ] Update checklist statuses after each commit/phase.
  - [ ] Leave explicit next action and next commit target at session end.

## Proposed Naming Targets

- [ ] Query module naming targets
  - [ ] `semantic_and_fusion.rs` -> `semantic_retrieval.rs` + `fusion.rs` (or equivalent domain names).
  - [ ] `ranking_and_output.rs` -> `ranking.rs` + `output.rs`.
  - [ ] `hierarchy_and_citation.rs` -> `hierarchy.rs` + `citation.rs`.

- [ ] Ingest module naming targets
  - [ ] `table_parse_quality_part1.rs`/`table_parse_quality_part2.rs` -> `table_parsing.rs` (or `table/*`).
  - [ ] `types_and_structured.rs` -> `types.rs` + `structured_parser.rs`.
  - [ ] `ids_and_outline.rs` -> `ids.rs` + `outline_extract.rs`.
  - [ ] `page_extract_and_normalize.rs` -> `page_extract.rs` + `page_normalize.rs`.
  - [ ] `ocr_tools_and_manifest.rs` -> `ocr.rs` + `tool_versions.rs` + `manifest_helpers.rs` (as needed).

- [ ] Validate module naming targets
  - [ ] `prelude_types_part1.rs`/`prelude_types_part2.rs` -> `constants.rs` + `models.rs`.
  - [ ] `coverage_freshness_part1.rs`/`coverage_freshness_part2.rs` -> `freshness.rs` + `reference_eval.rs` + `io.rs`.
  - [ ] `fidelity_metrics_part1.rs`/`fidelity_metrics_part2.rs` -> `metrics/extraction.rs`, `metrics/semantics.rs`, etc.
  - [ ] `stage_and_wp2_core.rs` -> `wp2_gate.rs`.
  - [ ] `checks_and_summary.rs` -> `checks.rs` + `summary.rs`.
  - [ ] `tail_and_tests.rs` -> `tests.rs` + production helper relocation.

- [ ] Embed module naming targets
  - [ ] `prelude.rs` -> topic-specific module (`types.rs`/`context.rs`) based on final ownership.

## Acceptance Criteria

- [ ] Module/file names reflect domain ownership rather than split order.
  - [ ] No command module files named `*_partN.rs`.
  - [ ] No avoidable mixed-concern `*_and_*` names in active command paths.

- [ ] Size guidance is explicitly soft and policy-aligned.
  - [ ] Documentation describes line limits as heuristics.
  - [ ] Tooling language defaults to advisory behavior.

- [ ] Behavior parity is maintained.
  - [ ] Command behavior unchanged for ingest/embed/query/validate workflows.
  - [ ] Quality report schema and check semantics unchanged.
  - [ ] Determinism and smoke baselines remain stable.

## Execution Order

- [ ] Recommended sequence
  - [ ] Query cleanup (lowest migration risk).
  - [ ] Embed cleanup.
  - [ ] Ingest cleanup.
  - [ ] Validate cleanup (largest/highest coupling).
  - [ ] Docs and policy language updates.
  - [ ] Final verification and closeout.
