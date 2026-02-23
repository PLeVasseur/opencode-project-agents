# Part 6 Table 1 Chunk-First Restart: Session Bootstrap Capsule

Use this capsule at the start of any new session to avoid re-discovery work.

## Canonical Working Context

- Repo root: `/home/pete.levasseur/personal/iso-26262-rust-mapping-coding-guidelines`
- Restart plan: `plans/part6-table1-chunk-first-retrieval-restart-plan.md`
- Implementation runbook: `plans/part6-table1-retrieval-restart-implementation-runbook.md`
- Feedback source of truth:
  - `feedback/rust-reference/retrieval-restart-plan-feedback.md`
- Extractor DB path (validated):
  - `/home/pete.levasseur/personal/iso-26262-coding-standard-extraction/.cache/iso26262/iso26262_index.sqlite`
- Canonical active DB path:
  - `.cache/sqlite_kb/current/rust_reference.sqlite`
- Canonical manifest + snapshot roots:
  - `data/sqlite_kb_manifest.yaml`
  - `.cache/sqlite_kb/snapshots/rust_reference`

## Execution Mode

- Rip-and-replace restart.
- No legacy dual-run requirement.
- No legacy control artifact freeze/copy/compare requirement.

## Locked Technical Invariants

- Pinned source revision is mandatory for production builds.
- Retrieval unit is chunk.
- IDs are content-addressed and deterministic.
- `raw_text` is for citation; `clean_text` is for indexing/rerank.
- Row mapping is post-retrieval and must support abstain.

## Known Restart Triggers

- Statement-era ID drift and sentence-level fragility are known root causes.
- Row metadata quality issues exist and require structured hygiene rebuild.

## Required New-Session Startup Sequence

1. Read this capsule.
2. Read `feedback/rust-reference/retrieval-restart-plan-feedback.md`.
3. Read `plans/part6-table1-chunk-first-retrieval-restart-plan.md`.
4. Read `plans/part6-table1-retrieval-restart-implementation-runbook.md`.
5. Continue from the earliest unchecked step in the restart plan.

## Session Handoff Expectations

Every session that changes restart status should update:

- active DB in place at `.cache/sqlite_kb/current/rust_reference.sqlite` (never under restart run dirs)
- if canonical DB is stale (`user_version < 6` or missing `chunks`), run build step to recreate before materialization/eval/review
- run artifact root under `.cache/sqlite_kb/reports/rust_reference/restart_phase0/<RUN_ID>/` (reports/bundles/status only)
- run status snapshot (`reports/run_status.json`)
- restart plan checkboxes for completed steps
- one commit per completed step (Conventional Commit with step number)
- this capsule if key facts/paths changed
