# Step1/Phase1 V2 Remediation Plan Proposal

## Why this plan

- `fls-pr6-updated-analysis-v2.md` shows forward references improved, but conceptual placement worsened in key areas (`high` relocation priority rose to 49).
- The same analysis shows `significant_reword` increased to 160, largely due to inline/contextual chapter definitions replacing standalone-style definitions.
- `fls-pr6-placement-fitness-v2.json` confirms: `poor=61`, `questionable=111`, `high=49`, `medium=49`, `forward_reference_count=248`.
- `fls-pr6-definition-divergence-v2.json` confirms: `significant_reword=160`, `low reliability=160`, `missing=2`.
- Combined actionable universe is large; covering all placement poor/questionable + divergence low yields ~233 unique terms after overlap.

## V2 Remediation Plan (Step1 / Phase1)

### Stage 0 - baseline lock and scope freeze

- [ ] Freeze source inputs to this copied bundle (`feedback-v2-20260211T133654Z`).
- [ ] Record baseline branch head (`glossary-step-1-main-text-coverage`) and current commit ancestry.
- [ ] Run baseline validation: `uv run python tools/glossary-migration-check.py --phase 1 --strict`, `./make.py --clear`, `./make.py --check-links`.
- [ ] Write baseline artifact pack under `$OPENCODE_CONFIG_DIR/reports/<new-v2-remediation-run>/baseline/`.

### Stage 1 - policy gate (critical)

- [ ] Adopt explicit policy: conceptual-home-first for foundational terms; first-use placement is secondary.
- [ ] Treat recommender targets in placement JSON as signals, not authoritative destinations.
- [ ] Define when to keep local definitions: only for truly local/specialized concepts.
- [ ] Define fallback for first-use discoverability: keep `:t:` usage plus explicit `For :dt:\`term\`, see :p:\`...\`` where needed.
- [ ] Document policy in `policy-decisions-v2.md` before term edits begin.

### Stage 2 - build unified v2 backlog with mandatory traceability

- [ ] Create one master checklist + ledger for v2 terms (new files; do not reuse old 202-term checklist).
- [ ] Scope checklist to 233 unique terms (172 placement poor/questionable + 160 divergence low, overlap accounted for).
- [ ] For each term require: `before_file/line/dp`, `after_file/line/dp`, `action`, `why`, `commit`, `quality`.
- [ ] Add per-term subchecks (`before locked`, `decision`, `reason quality`, `after captured`, `status finalized`).
- [ ] Hard gate: no term closes without concrete before/after anchors and rationale.

### Stage 3 - execution waves (manual term-by-term)

- [ ] **Wave A (highest risk):** foundational/high-risk terms first (e.g., `value`, `expression`, `reference`, `trait`, `field`, `implementation`, `crate`, `static`, `statement`).
- [ ] **Wave B:** remaining `high` + `medium` placement terms (98 total target for conceptual coherence correction).
- [ ] **Wave C:** low-reliability divergence terms not already fixed by Waves A/B (rewrite to standalone definitional sentences).
- [ ] **Wave D:** residual placement poor/questionable with `low_forward_ref`/`none` priorities; resolve by either rehome or justified keep+forward-reference.
- [ ] Commit cadence: 20 terms per batch, one commit per batch, with checkpoint validation per batch.

### Stage 4 - quality controls (strict)

- [ ] Enforce one canonical `:dt:` definition per term (no duplicate canonical definitions).
- [ ] When relocating a term, convert old definitional occurrence to `:t:` or explicit forward-reference text.
- [ ] For low-reliability terms, rewrite chapter definitions so they stand alone (not buried in incidental logic sentences).
- [ ] Resolve the 2 missing-singular findings (`crate import`, `declaration`) with an explicit decision (retain plural only with justification, or reintroduce singular aliases).
- [ ] Maintain paragraph ID integrity and lint requirements.

### Stage 5 - validation gates

- [ ] Batch gate (every 20): checklist/ledger validator pass + repo diff present + no out-of-scope checklist drift.
- [ ] Wave gate: `uv run ... --phase 1 --strict` pass.
- [ ] Milestone gate (every 2-3 waves): `./make.py --clear` + `./make.py --check-links`.
- [ ] Final gate: all checklist items closed; all reason-quality checks pass; strict/build/link all green.

### Stage 6 - before/after/why reporting

- [ ] Produce `phase1-v2-before-after-why.md` with per-term evidence (or per-batch annex tables).
- [ ] Produce `placement-v2-resolution-summary.md` (counts by action and unresolved=0 target).
- [ ] Produce `divergence-v2-resolution-summary.md` (low-reliability before/after counts and notable rewrites).
- [ ] Produce `core-term-disposition.md` for foundational term decisions and rationale.
- [ ] Produce `open-issues.md` only if anything remains deferred (with explicit reason and owner).

### Stage 7 - re-analysis loop

- [ ] Request/produce refreshed v3 analysis bundle after remediation.
- [ ] Reconcile v2 vs v3 deltas and close only when high-priority placement and low-reliability divergence are demonstrably reduced to acceptable thresholds.

## Recommended closure thresholds

- `high` placement priority: 49 -> 0
- `medium` placement priority: 49 -> 0 (or explicitly justified exceptions list)
- `low reliability`: 160 -> near 0 with explicit exceptions only
- `poor + questionable`: 172 -> minimized with no unresolved foundational misplacements

## Policy decision required before execution

1. **Conceptual-home-first (recommended):** allow some forward references to return if that restores coherent canonical definitions.
2. First-use-first: keep aggressive first-use placement and optimize around it.
