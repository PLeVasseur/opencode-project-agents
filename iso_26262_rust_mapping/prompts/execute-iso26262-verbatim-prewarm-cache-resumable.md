# Execute ISO 26262 Verbatim Prewarm Cache Integration Plan (Kickoff + Resume + Crash-Recovery)

Use this prompt to execute:

- `$OPENCODE_CONFIG_DIR/plans/2026-02-16-verbatim-prewarm-cache-integration-plan.md`

with resumable behavior aligned to:

- `$OPENCODE_CONFIG_DIR/skills/resumable-execution/SKILL.md`
- `$OPENCODE_CONFIG_DIR/reports/tooling/state_tool.py`

## Inputs

- Optional `RUN_ID`.
- Optional `MAX_PHASES` throttle (no default cap).
- Optional `MAX_PHASES=all` or `MAX_PHASES=0` to force explicit run-to-completion mode.
- Optional `START_PHASE` (default: earliest incomplete safe phase).
- Optional `BASE_BRANCH` (default `main`).
- Optional `PDF_ROOT` (default `$REPO_ROOT/.cache/iso26262`).
- Optional `MODE` (`fixture_ci` or `licensed_local`, default `licensed_local` for local runs).
- Optional `VERBATIM_PREWARM_ENABLED` (`1` default, must remain `1` for this plan).
- Optional `TS_GUIDELINES_PATH` (default `$REPO_ROOT/docs/traceability-ts-and-quotation-guidelines.md`).
- Optional `MAKEPY_VERIFY_COMMAND` (default `SPHINX_MIGRATION_RUN_ROOT="$CONTROL_RUN_ROOT" ./make.py verify`).
- Optional `RETAIN_PROBE_INSERTIONS` (`0` default; `1` only for explicit debug/promotion workflows).
- Optional `PROBESET_FREEZE_MANIFEST_PATH` (default `$CONTROL_RUN_ROOT/artifacts/probes/probeset-freeze-manifest.json`).
- Optional guardrail fields for documentation/reporting (`RESOURCE_GUARDRAILS_VERSION`, `QUERY_INDEX_MAX_SHARD_BYTES`, `QUERY_INDEX_MAX_POSTINGS_PER_TOKEN`, `QUERY_MAX_HITS`, `QUERY_MAX_QUOTE_BYTES`, `MAKEPY_VERIFY_TIMEOUT_SECONDS`) when explicitly needed.

## Operating modes

- `kickoff-new`: no `RUN_ID`, no incomplete run exists.
- `kickoff-explicit`: `RUN_ID` provided but control run root does not exist yet.
- `resume-auto`: no `RUN_ID`, newest incomplete run exists.
- `resume-explicit`: `RUN_ID` provided and control run root exists.

Mode must be auto-detected and reported in output.

## Required behavior

1. Determine `OPENCODE_CONFIG_DIR` and `REPO_ROOT`.
2. Resolve roots deterministically:
   - `CONTROL_RUN_ROOT="$OPENCODE_CONFIG_DIR/reports/iso26262-mining-verbatim-$RUN_ID"`
   - `DATA_RUN_ROOT="$REPO_ROOT/.cache/iso26262/mining/runs/$RUN_ID"`
   - `VERBATIM_CACHE_ROOT="$DATA_RUN_ROOT"`
   - `PDF_ROOT="${PDF_ROOT:-$REPO_ROOT/.cache/iso26262}"`
3. Auto-select run on `resume-auto`:
   - scan `$OPENCODE_CONFIG_DIR/reports/iso26262-mining-verbatim-*`,
   - treat run incomplete if any of: `S_FINALIZE_DONE!=1`, missing phase checkpoint(s), missing verify/finalize summaries, missing prewarm/rollout evidence,
   - pick newest incomplete by parsed run-id timestamp (fallback `mtime`).
4. Kickoff bootstrap for new runs:
   - run `uv sync` in repository root,
   - set `BASE_BRANCH="${BASE_BRANCH:-main}"`,
   - set `CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"`,
   - if `CURRENT_BRANCH==BASE_BRANCH`, create/switch `TARGET_BRANCH="feat/iso26262-verbatim-prewarm-$RUN_ID"`; else use current branch,
   - create `CONTROL_RUN_ROOT`, `DATA_RUN_ROOT`, and required prewarm/query/source-integration subdirectories,
   - initialize `state.env` and `checklist.state.env` using `state_tool.py` (atomic writes).
5. Resume bootstrap for existing runs:
   - ensure `state.env`, `checklist.state.env`, `run.log`, `artifacts/`, and `lock/` exist,
   - load `TARGET_BRANCH` from `state.env`,
   - if current branch differs, checkout `TARGET_BRANCH`.
6. Enforce lock discipline with `LOCK_FILE` from `state.env`:
   - stop on active valid lock,
   - lock payload includes `pid`, `host`, `user`, `run_id`, `acquired_at_utc`,
   - on stale lock, append stale payload to `run.log` before replacement,
   - release lock on all exits (success/failure/interruption).
7. Validate immutable contract before mutating work:
   - `RUN_ID`, `TASK_NAME`, `REPO_ROOT`, `PLAN_PATH`, `RUN_ROOT`, `PDF_ROOT`, `CONTROL_RUN_ROOT`, `ARTIFACT_ROOT`, `LOCK_FILE`,
   - `BASE_BRANCH`, `TARGET_BRANCH`, `BASE_PIN_SHA`,
   - `SOURCE_PDFSET_PATH`, `RELEVANT_POLICY_PATH`, `EXTRACTION_POLICY_PATH`,
   - `VERBATIM_PREWARM_ENABLED`, `VERBATIM_CACHE_ROOT`, `VERBATIM_SCHEMA_VERSION`, `PAGE_TEXT_SCHEMA_PATH`, `UNIT_SLICE_SCHEMA_PATH`, `ANCHOR_TEXT_LINK_SCHEMA_PATH`,
   - `QUERY_TOOL_PATH`, `QUERY_INDEX_SCHEMA_VERSION`, `QUERY_INDEX_MANIFEST_PATH`,
   - `TS_GUIDELINES_PATH`, `MAKEPY_VERIFY_COMMAND`, `SRC_INTEGRATION_MANIFEST_PATH`,
   - `PROBESET_FREEZE_MANIFEST_PATH`, `PROBESET_FREEZE_SIGNATURE`, `RETAIN_PROBE_INSERTIONS`,
   - optional guardrail fields when configured (`RESOURCE_GUARDRAILS_VERSION`, `QUERY_INDEX_MAX_SHARD_BYTES`, `QUERY_INDEX_MAX_POSTINGS_PER_TOKEN`, `QUERY_MAX_HITS`, `QUERY_MAX_QUOTE_BYTES`, `MAKEPY_VERIFY_TIMEOUT_SECONDS`),
   - required parts (`P06`, `P08`, `P09`) and selected mode.
8. Initialize and enforce canonical stage/checklist keys:
   - stage pointer: `CURRENT_STAGE` in (`ingest`, `extract`, `normalize`, `anchor`, `publish`, `verify`, `finalize`),
   - done flags: `S_INGEST_DONE`..`S_FINALIZE_DONE` explicit `0|1`,
   - checklist keys exactly per plan section `6` (missing required keys treated as `0`).
9. Enforce crash-recovery reconciliation windows before phase execution:
   - stage marked done but required prewarm/checkpoint artifact missing => reopen stage,
   - checklist incomplete => reopen stage,
   - commit marker/checkpoint mismatch => stop and reconcile,
   - unit-link/anchor-link counts mismatch => stop and reconcile,
   - query index manifests/signatures missing or mismatched for done phase => stop and reconcile,
   - `src-integration.begin` present without `src-integration.commit` => reconcile via source-integration manifest,
   - source-integration manifest checksum mismatch at resume boundary => stop and reconcile,
   - probe-freeze manifest/signature mismatch at resume boundary => stop and reconcile,
   - resume from earliest incomplete safe phase.
10. Enforce path/content policy strictly:
    - copyrighted/licensed/raw/OCR/verbatim/debug artifacts only under repo `.cache/...` data-plane,
    - control-plane under `$OPENCODE_CONFIG_DIR/reports/...` must remain metadata-only,
    - committed outputs only non-verbatim corpus/index under `traceability/iso26262/...`,
    - fail if `.cache` raw artifacts are staged/committed,
    - fail if control-plane artifacts contain disallowed verbatim keys (`raw_text`, `paragraph_text`, `cell_text`, `excerpt`, equivalent text payload keys).
11. Enforce implementation hygiene:
    - no hardcoded `OPENCODE` or `OPENCODE_CONFIG_DIR` references in mining implementation files,
    - runbook/docs may reference `$OPENCODE_CONFIG_DIR`.
12. Execute integrated phases (`C14 -> C15 -> ...`) with commit gates.
13. Default execution behavior: continue through all remaining phases until completion or a hard stop condition.
14. If `MAX_PHASES` is explicitly provided as a positive integer, treat it as a throttle and stop after that many completed phases with a clean resume pointer.
15. Enforce dedicated verification phases before CI/docs hardening and rollout batches:
    - cache-build quality phase verifies text normalization and parser-artifact hygiene,
    - query verification phase validates deterministic word/phrase behavior using probe sets sampled from existing tables/text and `src/` sources.
16. Enforce query output guardrails:
    - query output must present `{ts}` usage reminder and guideline pointer (`docs/traceability-ts-and-quotation-guidelines.md`) before locations/quotes,
    - quote mode must be explicitly requested, brief, and fair-use marked.
17. Enforce `{ts}` authoring bundle and end-to-end build validation:
    - from phase `C19` onward, query output must include parser-compatible `{ts}` authoring instructions with checked-in JSON lookup pointers,
    - during end-to-end phases (`C23` and later rollout batches), run query-driven insertions into representative paragraph/list/table cases in `src/` and run `SPHINX_MIGRATION_RUN_ROOT="$CONTROL_RUN_ROOT" ./make.py verify` as a hard validation gate.
18. Enforce post-validation source handling policy:
    - default `RETAIN_PROBE_INSERTIONS=0` => auto-revert probe fixture edits after evidence capture,
    - `RETAIN_PROBE_INSERTIONS=1` allowed only for explicit debug/promotion workflows and must be reported.
19. Canonical let-it-rip mode (default operator path):
    - when no throttles are provided, run-to-completion (`MAX_PHASES=all`) from earliest incomplete safe phase,
    - auto-resume newest incomplete run if present; otherwise kickoff a new run.

## Phase map and commit checkpoints

- `C14` / Phase 0: `feat(trace-miner): add data-plane verbatim page prewarm cache writers`
- `C15` / Phase 1: `feat(trace-miner): integrate normalize unit-slice verbatim cache links`
- `C16` / Phase 2: `feat(trace-miner): integrate anchor-to-verbatim linkage index`
- `C17` / Phase 3: `feat(trace-miner): add replay and checkpoint verification for verbatim caches`
- `C18` / Phase 4: `docs(trace-miner): specify prewarm cache query interface and lineage contracts`
  - required output includes baseline `docs/traceability-ts-and-quotation-guidelines.md`
- `C19` / Phase 5: `feat(trace-miner): add prewarm cache query CLI for words and phrases`
- `C20` / Phase 6: `test(trace-miner): verify prewarm cache normalization and artifact hygiene gates`
- `C21` / Phase 7: `test(trace-miner): verify prewarm cache query behavior with source probes` (includes probe-freeze manifest/signature)
- `C22` / Phase 8: `feat(trace-miner): add source insertion helpers for ts-guided query results`
- `C23` / Phase 9: `test(trace-miner): validate ts references end-to-end via src insertion and make.py` (auto-revert probe fixtures by default)
- `C24` / Phase 10: `chore(ci,docs): add prewarm cache query checks and operator runbook` (includes canonical let-it-rip operator mode)
- `C25+` / Phase 11+: repeatable `feat(trace-data): generate required-part verbatim prewarm cache batch <n>` until full required-part completion.

## Deterministic rules (must enforce)

- Required parts and PDF matching rules remain deterministic and unchanged (`P06`, `P08`, `P09` exact-name + regex fallback).
- Each required-part page must have exactly one extraction decision and one page-text prewarm record.
- `page-text.jsonl`, `unit-slices.jsonl`, and `anchor-text-links.jsonl` ordering is deterministic.
- Unit-to-anchor-to-text lineage must be deterministic and replay-signature stable.
- Query index shard generation and query result ordering are deterministic.
- Query probe-set generation from tables/text/`src/` is deterministic and signature-tracked.
- Query output preface and quote guardrails are deterministic and machine-verifiable.
- Query output includes deterministic `ts_authoring_bundle` fields and checked-in JSON lookup pointers.
- Query output includes deterministic `jsonl_row_hint` or `json_pointer_hint` for checked-in lookup paths.
- Markdown role and table YAML trace mappings are deterministic and parser-compatible.
- End-to-end query -> `src` insertion -> `$MAKEPY_VERIFY_COMMAND` validation is deterministic and replayable.
- Probe selection uses a frozen manifest/signature; implicit probe re-sampling is forbidden on resume.
- Resource guardrail fields are optional and may be reported when configured.
- Probe fixture source edits are auto-reverted by default after e2e validation.
- Required unit types for completion gates are `paragraph`, `list_bullet`, `table_cell`.

## Required checkpointing

- Stage checkpoints: `$CONTROL_RUN_ROOT/artifacts/checkpoints/<stage>.done.json`
- Phase checkpoints: `$CONTROL_RUN_ROOT/artifacts/checkpoints/phase-<n>.done.json`
- Checkpoint checksums are computed over canonical payload excluding volatile timestamp fields.

## Mandatory stop conditions

- Active non-stale lock by another process.
- Immutable contract drift on resume.
- `LAST_COMMITTED_SHA` mismatch with `git HEAD` at resume boundary.
- Stage marked done while required checklist keys are incomplete.
- Missing required stage/phase checkpoint artifacts.
- Missing required prewarm cache artifacts for a stage marked done.
- Required-part page or unit linkage coverage below 100%.
- Required query index artifacts missing/stale for current prewarm cache state.
- Query smoke checks fail for deterministic word/phrase fixtures.
- Prewarm cache build-quality verification fails (normalization/artifact hygiene).
- Query probe verification fails for deterministic probe suites (`tables`, `text`, `src`, `negative`).
- Probe-freeze manifest/signature is missing or mismatched for current run contract.
- Query output guardrails fail (`{ts}` reminder/guideline pointer missing, quote-limit violations, or missing fair-use marker).
- `{ts}` authoring bundle verification fails (invalid token/roles or unresolved checked-in JSON pointers).
- End-to-end paragraph/list/table `src` integration fails.
- `$MAKEPY_VERIFY_COMMAND` fails after query-driven `{ts}` insertion validation.
- Probe fixture edits remain in `src/` when `RETAIN_PROBE_INSERTIONS=0`.
- `TS_GUIDELINES_PATH` is missing/unreadable or does not match enforced guardrail limits when query guardrails are active (`C19+`).
- `MAKEPY_VERIFY_COMMAND` cannot be executed reproducibly at resume boundary when source integration/build phases are active (`C23+`).
- Source-integration manifest missing/inconsistent for a stage marked complete.
- Control-plane artifacts contain disallowed verbatim text payload fields.
- Any unresolved required-part QA item at publish/verify.
- Any attempt to include raw `.cache` artifacts in tracked commits.

## Required output format

- `MODE` (`kickoff-new`, `kickoff-explicit`, `resume-auto`, `resume-explicit`)
- `RUN_ID`
- `REPO_ROOT`
- `CONTROL_RUN_ROOT`
- `DATA_RUN_ROOT`
- `VERBATIM_CACHE_ROOT`
- `PDF_ROOT`
- `BASE_BRANCH` and `TARGET_BRANCH`
- `CURRENT_PHASE` before and after
- `CURRENT_STAGE` before and after
- phases/stages completed this invocation
- commits created this invocation (`sha`, `subject`, `phase`, `checkpoint`)
- required-part ingest resolution (`P06/P08/P09` resolved paths + hash status)
- prewarm cache summary (`page_text_records`, `page_block_records`, `unit_slice_records`, `anchor_text_link_records`)
- query tool status (`query_cli_path`, `query_index_shards`, `word_query_smoke`, `phrase_query_smoke`)
- build-quality verification status (`normalization_pass`, `artifact_hygiene_pass`, `anomaly_count`)
- query probe verification status (`tables_probe_pass`, `text_probe_pass`, `src_probe_pass`, `negative_probe_pass`, `probe_signature`)
- probe freeze status (`probeset_manifest_path`, `probeset_signature`, `freeze_pass`, `rotation_applied`)
- query output guardrail status (`ts_reminder_preface_pass`, `guideline_pointer_path`, `quote_limit_pass`, `fair_use_marker_pass`)
- `ts` authoring bundle status (`ts_token_enum_pass`, `ts_companion_roles_pass`, `json_lookup_pointer_pass`, `lookup_pointer_mode_pass`)
- end-to-end `src` build status (`paragraph_integration_pass`, `list_integration_pass`, `table_integration_pass`, `makepy_e2e_pass`)
- source integration transaction status (`src_integration_begin`, `src_integration_commit`, `manifest_checksum_pass`)
- source cleanup status (`retain_probe_insertions`, `auto_revert_applied`, `residual_src_diff_count`)
- resource guardrail status (if configured: `guardrails_version`, `index_limits_pass`, `query_limits_pass`, `build_timeout_pass`)
- linkage/coverage summary (`required parts completeness`, `required unit-type completeness`, `unresolved QA count`)
- deterministic replay signature status (`pass/fail`, mismatch counts)
- resilience drill status (`A/B/C/D/E/F/G`, lock contention/stale-lock)
- anti-leak/policy status (`control-plane metadata-only`, `.cache` untracked)
- artifacts created/updated (paths)
- `STOP_REASON` (`completed_all_phases`, `blocked_by_stop_condition`, `throttled_by_MAX_PHASES`)
- blockers/stop conditions (if any)
- exact next resume command or prompt invocation hint
