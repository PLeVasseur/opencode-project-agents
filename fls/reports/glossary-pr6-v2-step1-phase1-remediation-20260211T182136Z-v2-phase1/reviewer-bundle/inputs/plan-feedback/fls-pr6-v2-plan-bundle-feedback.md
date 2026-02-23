# Feedback on PR6 V2 Plan Artifact Bundle

**Bundle:** `glossary-pr6-v2-plan-artifact-bundle-20260211T145136Z`
**Review Date:** 2026-02-11

## Integrity Check

All 12 files present. All SHA256 checksums in `REVIEWER_INDEX.md` verified — pass.

## Overall Assessment

The **plan document** (`glossary-pr6-v2-step1-phase1-remediation-plan.md`) is solid. It correctly incorporates all prior feedback: conceptual-home-first policy, Wave A scoped to 15 foundational terms, Gate B+ as a hard stop for v3 re-analysis, per-wave pattern documents, action_type/decision_detail separation with semantic_change_flag, streamlined reporting, and partial-batch failure handling with quarantine.

The **tooling** (`validate-ledger-and-checklist.py` and `glossary-batch-orchestrator.py`) is from the prior v1 remediation run and has not been updated. The tooling will not work with the v2 artifacts. This is the central issue with this bundle.

## Critical: Tooling Is From v1 — Incompatible With v2 Plan

### 1. Checklist ID Scheme Mismatch

The v2 checklist template uses wave-prefixed IDs: `WA-001`, `WB-001`, `WC-001`, `WD-001`, `QQ-001`.

Both the validator and orchestrator hardcode the v1 pattern:

```python
# validate-ledger-and-checklist.py
PARENT_RE = re.compile(r"^- \[(?P<mark>[ xX])\] (?P<id>PQ-\d{3}) term=")
SUB_RE = re.compile(r"^  - \[(?P<mark>[ xX])\] (?P<id>PQ-\d{3})\.(?P<idx>\d+)\b")

# glossary-batch-orchestrator.py
PARENT_RE = re.compile(r'^- \[(?P<mark>[ xX])\] (?P<id>PQ-\d{3}) (?P<rest>.+)$')
SUB_RE = re.compile(r'^  - \[(?P<mark>[ xX])\] (?P<id>PQ-\d{3})\.(?P<idx>[1-5])\b')
```

**Impact:** No checklist line will ever be parsed. The validator will report 0 parent items found and immediately fail with "missing parent checklist IDs." The orchestrator's `choose_batch()` will return an empty list and exit with "No unchecked parent checklist IDs remain" on the very first iteration.

**Fix:** Both regexes need to accept the wave-prefixed format. Something like `(?P<id>W[A-D]-\d{3}|QQ-\d{3})` or a configurable pattern.

### 2. Sub-Item Count Mismatch

The v2 checklist template defines **6 sub-items** per parent (.1 through .6):

```
- [ ] WA-001.1 before snapshot locked
- [ ] WA-001.2 action recorded
- [ ] WA-001.3 rationale quality pass
- [ ] WA-001.4 semantic review fields complete
- [ ] WA-001.5 after snapshot captured
- [ ] WA-001.6 status finalized
```

The validator defaults to `--subitems-per-parent=5`. The orchestrator hardcodes `range(1, 6)` (i.e. indices 1–5). The validator's rubric check function `check_rubric_subitems` only handles indices 1–5, mapping them to: (1) before snapshot, (2) decision/reason, (3) reason quality, (4) after snapshot, (5) statuses/final quality.

**Impact:** Sub-item .6 ("status finalized") will never be validated. The validator will report sub-item .6 as "unexpected" for every parent. The orchestrator will never check sub-item .6 completion.

**Fix:** Update both to expect 6 sub-items. Add `.4 = semantic review fields` to the rubric check (currently .4 maps to "after snapshot" which is now .5 in v2). The v2 mapping should be:

| Sub-item | v1 meaning | v2 meaning |
|----------|------------|------------|
| .1 | before snapshot | before snapshot locked |
| .2 | decision/reason | action recorded |
| .3 | reason quality | rationale quality pass |
| .4 | after snapshot | **semantic review fields complete** |
| .5 | statuses/final quality | after snapshot captured |
| .6 | *(doesn't exist)* | **status finalized** |

### 3. Ledger Column Name Mismatches

The v2 plan and template introduced new columns and renamed others. The validator expects v1 column names.

**Columns the validator expects that don't exist in the v2 template:**

| Validator expects | v2 template equivalent |
|-------------------|----------------------|
| `decision` | `decision_detail` |
| `baseline_rating` | `placement_fitness_rating` |
| `relocation_priority` | `placement_priority` |
| `conceptual_home` | *(not present)* |
| `phase2_status` | *(not present)* |

**Columns in the v2 template that the validator doesn't know about:**

- `action_type` — the core move/rewrite taxonomy from the plan
- `semantic_change_flag` — the `none`/`clarification-only`/`normative-risk` field
- `review_attention` — the `required` flag for rewrites
- `divergence_match_category`, `divergence_reliability`, `divergence_similarity`
- `wave`, `source_set`, `batch_id`
- `quarantine_status`, `quarantine_reason`
- `before_evidence_ref`, `after_evidence_ref`

**Impact:** The validator will fail on column-missing checks before it gets to any data validation. Even if forced past that, it will look for `decision` (doesn't exist), skip `action_type` entirely, and never enforce the plan's core rewrite-attention rule.

### 4. Orchestrator Default Paths Reference v1 Artifacts

The orchestrator's `build_defaults()` function hardcodes:

```python
"checklist": reports_dir / "glossary-poor-questionable-202-checklist.md",
"seed_ledger": reports_dir / "glossary-poor-questionable-202-ledger-seed.csv",
"baseline_reference": reports_dir / "glossary-poor-questionable-202-baseline-reference.csv",
"reason_rubric": reports_dir / "glossary-poor-questionable-reason-rubric.md",
"manual_plan": plans_dir / "glossary-poor-questionable-manual-remediation-plan.md",
```

The remediation directory naming uses:
```python
f"glossary-poor-questionable-manual-remediation-{run_id}"
```

**Impact:** Running the orchestrator without overriding every single path argument will look for files that don't exist in the v2 layout. Even the argparser description says "Run glossary poor/questionable remediation in 20-item OpenCode batches" — it's the v1 orchestrator, unmodified.

### 5. Batch Failure Protocol Divergence

The plan specifies partial-batch commit with quarantine:

> "classify term outcomes into passed and quarantined sets... if at least one term passed, preserve passing term edits, commit passing term subset once, rollback only quarantined term checklist/ledger rows"

The orchestrator implements full-batch rollback only:

```python
except Exception as exc:
    shutil.copy2(checklist_snapshot, checklist_path)
    shutil.copy2(ledger_snapshot, ledger_path)
    # ... full rollback, no partial commit
```

There is no quarantine queue, no partial commit logic, and no `quarantine-queue.json` management.

### 6. No Wave Awareness in Orchestrator

The orchestrator has no concept of waves. It processes all unchecked items sequentially regardless of wave assignment. It doesn't know about:

- Wave boundaries (stop after Wave A, stop after Wave B)
- Gate B+ (hard stop for v3 artifacts)
- Different batch sizes per wave (20 for A/B, 40-50 for C/D)
- Per-wave pattern document generation
- Rescope checkpoint

The `--max-batches` flag can approximate wave boundaries, but the operator would need to manually calculate how many batches each wave requires and set it correctly each run. There's no enforcement of the Gate B+ hard stop.

### 7. Validator `expected-parent-count` Default

Defaults to 202 (the v1 scope). The v2 scope starts at 15 (Wave A), grows to ~98 after Wave B, and is dynamically determined after Gate B+. Every validator invocation will need `--expected-parent-count` overridden, but the orchestrator doesn't pass this through — it calls `run_validator()` without it.

## Non-Critical Observations

### Checklist Template Has Correct Structure

Despite the tooling mismatch, the checklist template itself is well-designed. The wave-prefixed IDs, 6-point sub-item rubric, Gate B+ section, and quarantine queue section all align with the plan. The template is ready to use — it's the tooling that needs to catch up.

### Ledger Template Is Comprehensive

The 37-column CSV template captures everything the plan requires: the action_type taxonomy, semantic_change_flag, review_attention, divergence metadata, quarantine fields, and evidence references. It's a superset of what's needed. This is fine — better to have unused columns than missing ones.

### Reason Codes Are Consistent

The validator and orchestrator share identical `ALLOWED_REASON_CODES` sets, and these align with the plan's intent. No changes needed here.

### Execution Prompt Is Clean

The prompt correctly scopes execution to Waves A/B + Gate B+ boundary, includes the reviewer handoff package requirement, and specifies the blocked-on-v3 stop condition.

## Recommendations

1. **Update the validator and orchestrator before execution begins.** This is a hard blocker. The tooling cannot process the v2 artifacts in its current state. Either update the scripts to match the v2 plan, or write new ones. The validator needs: new ID regex, 6-sub-item rubric, v2 column names, action_type/semantic_change_flag awareness. The orchestrator needs: new ID regex, wave awareness, Gate B+ enforcement, partial-batch commit with quarantine, v2 default paths, configurable batch sizes per wave.

2. **Test the tooling against the v2 templates before starting Wave A.** Run the validator in `init` mode against the populated checklist and ledger. If it doesn't pass cleanly on a fresh initialized state, the tooling isn't ready.

3. **Add the tooling update as an explicit Gate G0 prerequisite.** The plan's G0 section checks that `uv run python tools/glossary-migration-check.py --help` works and `./make.py --help` works, but doesn't verify that the validator and orchestrator are compatible with the v2 artifacts. Add a step: "Run validator in init mode against v2 checklist/ledger templates; must pass with zero errors."

## Summary

The plan is good. The checklist and ledger templates are good. The execution prompt is good. The tooling is from the wrong run and will fail immediately if used. Fix the tooling, then this bundle is ready to execute.
