# Execute ISO 26262 PDF Mining Corpus Plan (Kickoff + Resume + Crash-Recovery)

Use this prompt to execute:

- `$OPENCODE_CONFIG_DIR/plans/2026-02-15-hierarchical-pdf-mining-corpus-plan.md`

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

## Operating modes

- `kickoff-new`: no `RUN_ID`, no incomplete run exists.
- `kickoff-explicit`: `RUN_ID` provided but control run root does not exist yet.
- `resume-auto`: no `RUN_ID`, newest incomplete run exists.
- `resume-explicit`: `RUN_ID` provided and control run root exists.

Mode must be auto-detected and reported in output.

## Required behavior

1. Determine `OPENCODE_CONFIG_DIR` and `REPO_ROOT`.
2. Resolve roots deterministically:
   - `CONTROL_RUN_ROOT="$OPENCODE_CONFIG_DIR/reports/iso26262-mining-$RUN_ID"`
   - `DATA_RUN_ROOT="$REPO_ROOT/.cache/iso26262/mining/runs/$RUN_ID"`
   - `PDF_ROOT="${PDF_ROOT:-$REPO_ROOT/.cache/iso26262}"`
3. Auto-select run on `resume-auto`:
   - scan `$OPENCODE_CONFIG_DIR/reports/iso26262-mining-*`,
   - treat run incomplete if any of: `S_FINALIZE_DONE!=1`, missing phase checkpoint(s), missing `verify-summary`, missing finalize markers,
   - pick newest incomplete by parsed run-id timestamp (fallback `mtime`).
4. Kickoff bootstrap for new runs:
   - run `uv sync` in repository root,
   - set `BASE_BRANCH="${BASE_BRANCH:-main}"`,
   - set `CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"`,
   - if `CURRENT_BRANCH==BASE_BRANCH`, create/switch `TARGET_BRANCH="feat/iso26262-pdf-mining-$RUN_ID"`; else use current branch,
   - create `CONTROL_RUN_ROOT`, `DATA_RUN_ROOT`, and required subdirectories,
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
   - required parts (`P06`, `P08`, `P09`) and selected mode.
8. Initialize and enforce canonical stage/checklist keys:
   - stage pointer: `CURRENT_STAGE` in (`ingest`, `extract`, `normalize`, `anchor`, `publish`, `verify`, `finalize`),
   - done flags: `S_INGEST_DONE`..`S_FINALIZE_DONE` explicit `0|1`,
   - checklist keys exactly per plan section `6C` (missing required keys treated as `0`).
9. Enforce crash-recovery reconciliation windows before phase execution:
   - stage marked done but artifact/checkpoint missing => reopen stage,
   - checklist incomplete => reopen stage,
   - commit marker/checkpoint mismatch => stop and reconcile,
   - resume from earliest incomplete safe phase.
10. Enforce path/content policy strictly:
    - copyrighted/licensed/raw/OCR/debug artifacts only under repo `.cache/...` data-plane,
    - control-plane under `$OPENCODE_CONFIG_DIR/reports/...` must remain metadata-only,
    - committed outputs only non-verbatim corpus under `traceability/iso26262/...`,
    - fail if `.cache` raw artifacts are staged/committed.
11. Enforce implementation hygiene:
    - no hardcoded `OPENCODE` or `OPENCODE_CONFIG_DIR` references in mining implementation files,
    - runbook/docs may reference `$OPENCODE_CONFIG_DIR`.
12. Execute integrated phases (`C0 -> C1 -> ...`) with commit gates.
13. Default execution behavior: continue through all remaining phases until completion or a hard stop condition.
14. If `MAX_PHASES` is explicitly provided as a positive integer, treat it as a throttle and stop after that many completed phases with a clean resume pointer.

## Phase map and commit checkpoints

- `C0` / Phase 0: `chore(trace-data): lock required-part source PDF hash baseline`
  - run ingest hash-lock mode (`--lock-source-hashes`), eliminate required-part `sha256: PENDING`.
- `C1`: `chore(trace-miner): scaffold standalone mining CLI and stage framework`
- `C2`: `feat(trace-miner): implement resumable control-plane state machine`
- `C3`: `feat(trace-miner): implement ingest stage and required-part PDF discovery`
- `C4`: `feat(trace-miner): implement deterministic extraction policy metrics and page decisions`
- `C5`: `feat(trace-miner): implement OCR fallback and quality banding`
- `C6`: `feat(trace-miner): implement normalize stage and locator model`
- `C7`: `feat(trace-miner): implement deterministic anchoring and sharded corpus writers`
- `C8`: `feat(trace-miner): implement publish stage and compatibility registry generation`
- `C9`: `feat(trace-miner): implement verify gates and compliance checks`
- `C10`: `chore(ci,docs): add CI jobs and operator runbook workflows`
- `C11`: `chore(trace-data): refresh required-part source hash evidence and lock provenance`
- `C12`: `feat(trace-data): publish pilot normalized corpus and evidence`
- `C13+`: repeatable `feat(trace-data): publish required-part corpus batch <n>` for full rollout.

## Deterministic ingest rules (must enforce)

- Default `--pdf-root` is `$REPO_ROOT/.cache/iso26262`.
- Required parts are read from `traceability/iso26262/index/relevant-pdf-policy.jsonc`.
- Preferred exact filenames:
  - `P06`: `ISO 26262-6;2018 ed.2 (en).pdf`
  - `P08`: `ISO 26262-8;2018 ed.2 (en).pdf`
  - `P09`: `ISO 26262-9;2018 ed.2 (en).pdf`
- Fallback regexes:
  - `P06`: `(?i)^ISO\s*26262[-; ]6.*2018.*ed\.?\s*2.*\.pdf$`
  - `P08`: `(?i)^ISO\s*26262[-; ]8.*2018.*ed\.?\s*2.*\.pdf$`
  - `P09`: `(?i)^ISO\s*26262[-; ]9.*2018.*ed\.?\s*2.*\.pdf$`
- Ambiguous matches are hard failures.

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
- Required part hash still `PENDING` outside Phase 0 hash-lock flow.
- Any attempt to include raw `.cache` artifacts in tracked commits.

## Required output format

- `MODE` (`kickoff-new`, `kickoff-explicit`, `resume-auto`, `resume-explicit`)
- `RUN_ID`
- `REPO_ROOT`
- `CONTROL_RUN_ROOT`
- `DATA_RUN_ROOT`
- `PDF_ROOT`
- `BASE_BRANCH` and `TARGET_BRANCH`
- `CURRENT_PHASE` before and after
- `CURRENT_STAGE` before and after
- phases/stages completed this invocation
- commits created this invocation (`sha`, `subject`, `phase`, `checkpoint`)
- required-part ingest resolution (`P06/P08/P09` resolved paths + hash status)
- coverage/QA status summary (`required parts completeness`, `unresolved QA count`)
- artifacts created/updated (paths)
- `STOP_REASON` (`completed_all_phases`, `blocked_by_stop_condition`, `throttled_by_MAX_PHASES`)
- blockers/stop conditions (if any)
- exact next resume command or prompt invocation hint
