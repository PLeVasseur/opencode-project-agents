# Recovery Plan v3 — Reviewer Feedback

## Overall

The v3 recovery plan is substantially improved and addresses every concern from the prior round. The script implementations are real (not stubs), the smoke tests cover the critical rejection paths, the hard-fail codes are properly classified, and the deviation permit model is a genuine enforcement mechanism. Three issues remain, plus a redesign of the deviation permit approval model.

---

## 1. Deviation permit approval must be separated from execution

### Problem

The current model has the implementer create the deviation permit file and fill in `approved_by` with any string that isn't their own `implementer_id`. The check is `approved_by != implementer_id && approved_by != ""`. This means the implementer writes a fake name and the permit is accepted. The person being constrained is the person issuing the approvals.

### Required redesign

Split the permit lifecycle into three phases: **filing** (implementer, during execution), **review** (manager, after execution), and **gate enforcement** (tooling, at wave boundaries).

**During execution** — the implementer files the deviation permit with all evidence fields populated but `approved_by` left empty. A new field `status` is set to `pending-review`. The rationale writer accepts this — the term completes provisionally and the batch proceeds. This prevents individual deviations from blocking the entire run while waiting for external review.

The rationale writer changes:
- Drop the `approved_by != implementer_id` check entirely.
- Drop the `approved_by` non-empty requirement at write time.
- Validate only that evidence fields (`evidence_against_recommendation`, `evidence_for_proposed`, `reference_count_argument`) meet length and non-boilerplate requirements.
- Record `deviation_status=pending` in the ledger row.

**After execution** — the reviewer (manager) reads each filed permit and either approves or rejects it. A new signing script handles this:

```
approve-deviation.py \
  --permit deviation-permits/deviation-permit-WB-037.json \
  --approved-by pete \
  --decision approve|reject \
  --ledger manual-placement-ledger-v3.csv \
  --events-jsonl reports/rationale-events.jsonl
```

This script is the sole path to approval. It:
- Sets `approved_by` and `status` (either `approved` or `rejected`) in the permit JSON.
- Updates the ledger row's `deviation_approved_by`, `deviation_permit_sha256`, and `deviation_status`.
- Appends an approval/rejection event to `rationale-events.jsonl` with timestamp and permit digest.
- If `decision=reject`, sets `deviation_status=rejected` and `quarantine_status=quarantined-deviation-rejected` in the ledger, marking the term for re-execution.

**At gate checkpoints** — the validator distinguishes between modes:
- In `progress` mode (during batch execution): unsigned permits are accepted but counted. The batch summary reports `pending_deviation_count`.
- In `gate` mode (at Wave A/B boundaries): any completed row with `deviation_status=pending` triggers `FAILED_PENDING_DEVIATIONS`. The wave cannot close until every deviation is either approved or rejected.

The 30% deviation concentration gate still applies regardless of approval status — if more than 30% of high/medium terms in a wave filed deviations, that's a `FAILED_DEVIATION_CONCENTRATION` hard-stop, because it signals systematic avoidance of recommendations.

### Reviewer handoff addition

The bundle should include a `deviation-review-summary.json` artifact listing: total filed, total approved, total rejected, total pending, plus per-permit status and reviewer handle.

---

## 2. Foundational placement validates file but not section

### Problem

The validator's `FOUNDATIONAL_REQUIRED_FILES` dict maps term → file, and the check at line 805 only validates `after_file == required_file`. The plan's foundational matrix specifies allowed sections (e.g., `trait` → `types-and-traits.rst`, sections "Traits, Trait Types"), but the validator doesn't enforce them.

This means the implementer could relocate `trait` to the "Numeric Types" section of `types-and-traits.rst` and Gate A would pass. The file-level check gets you halfway; without a section check the implementer can technically comply while placing the definition in a nonsensical location within the correct file.

### Required change

Add a `FOUNDATIONAL_REQUIRED_SECTIONS` dict to the validator mapping each term to its set of allowed section strings. Check `after_section` against this set in the same foundational placement loop. Fail with `FAILED_FOUNDATIONAL_PLACEMENT` if `after_section` is not in the allowed set.

```python
FOUNDATIONAL_REQUIRED_SECTIONS = {
    "value":          {"Values"},
    "expression":     {"Expressions"},
    "trait":          {"Traits", "Trait Types"},
    "item":           {"Items"},
    "field":          {"Struct Types", "Enum Types"},
    "reference":      {"References", "Borrowing"},
    "implementation": {"Implementations", "Inherent Implementations"},
    "method":         {"Functions"},
    "crate":          {"Crates", "Compilation Roots"},
    "statement":      {"Statements"},
}
```

Note the `method` entry — see next item.

---

## 3. Foundational matrix lists a nonexistent section for `method`

### Problem

The plan says allowed sections for `method` are "Functions, Associated Functions." The file `functions.rst` has a "Functions" section heading at line 8, but there is no "Associated Functions" section anywhere in that file. The concept of associated functions lives in `associated-items.rst`, not `functions.rst`.

### Required change

Correct the foundational matrix entry for `method`:
- **Before**: `method` → `functions.rst` (allowed sections: Functions, Associated Functions)
- **After**: `method` → `functions.rst` (allowed sections: Functions)

If the implementer believes `method` should live in `associated-items.rst` instead, that's a plan revision requiring explicit approval, not an in-flight deviation.

---

## Summary of required changes

| Item | Script affected | Change |
|---|---|---|
| Deviation permit lifecycle redesign | `record-rationale-v3.py`, `validate-ledger-and-checklist-v3.py`, new `approve-deviation.py` | Split file/review/gate phases; drop self-attestation; add `FAILED_PENDING_DEVIATIONS` gate code |
| Section-level foundational check | `validate-ledger-and-checklist-v3.py` | Add `FOUNDATIONAL_REQUIRED_SECTIONS` dict and `after_section` validation |
| Fix `method` allowed sections | Plan + `FOUNDATIONAL_REQUIRED_SECTIONS` | Remove nonexistent "Associated Functions" from allowed set |
