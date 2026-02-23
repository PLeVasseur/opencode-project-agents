# FLS PR #6 — Wave A v5 Quality Review

## Verdict

Wave A v5 is a success. All 15 foundational terms have glossary-aligned definitions in their conceptual chapter homes. The definition-alignment guardrails worked in production, catching and reverting a real swap-as-insert attempt. This is ready for the Wave A quality gate.

## Execution summary

| Metric | Value |
|---|---|
| Commit range | `beb89ee` → `e498c8d` |
| Wave A terms completed | 15/15 |
| Batches completed | 6 |
| Batches failed/reverted | 1 (batch 005, WA-007 swap detected) |
| Terms quarantined | 1 (WA-007, resolved in batch 009) |
| Deviation permits filed | 0 |
| Execution integrity verdict | pass |
| Wave B gate status | blocked (as expected, pending quality gate artifact) |

## Diff statistics

| Metric | v4 (marker swaps) | v5 (current) |
|---|---|---|
| Lines inserted | 20 | 43 |
| Lines deleted | 20 | 16 |
| Net change | 0 | **+27** |
| Files modified | 13 | 11 |
| New `:dp:` paragraphs added | 0 | 9 |
| Glossary definitions physically relocated | 0 | 1 (`value`, `:dp:` ID preserved) |
| Glossary definitions inserted as new paragraphs | 0 | 8 |

## Definition alignment: 15/15 terms

| ID | Term | Op | Sim | Glossary ↔ Chapter |
|---|---|---|---|---|
| WA-001 | value | insert | 1.000 | Exact match (text relocated from expressions.rst, `:dp:` ID preserved) |
| WA-002 | expression | promote | 1.000 | Exact match (chapter already had identical sentence) |
| WA-003 | type | adapt | 0.889 | Close match ("defines a set" → "is a set" — improved alignment) |
| WA-004 | trait | promote | 1.000 | Exact match |
| WA-005 | construct | promote | 1.000 | Exact match (new paragraph inserted) |
| WA-006 | entity | promote | 1.000 | Exact match (new paragraph inserted) |
| WA-007 | name | promote | 1.000 | Exact match (new paragraph inserted, after retry) |
| WA-008 | item | insert | 1.000 | Exact match (new paragraph inserted) |
| WA-009 | field | insert | 1.000 | Exact match (new paragraph inserted) |
| WA-010 | reference | insert | 1.000 | Exact match (new paragraph inserted) |
| WA-011 | implementation | promote | 1.000 | Exact match (chapter already had identical sentence) |
| WA-012 | method | insert | 1.000 | Exact match (new paragraph inserted) |
| WA-013 | crate | promote | 1.000 | Exact match (chapter already had identical sentence) |
| WA-014 | module | promote | 1.000 | Exact match (chapter already had identical sentence) |
| WA-015 | statement | insert | 1.000 | Exact match (new paragraph inserted) |

14/15 exact glossary matches. 1/15 intentional rewording (`type`: "defines" → "is" for consistent subject-form).

## v4 → v5 improvement on the 3 previously-failed terms

| Term | v4 (what was wrong) | v5 (what it is now) |
|---|---|---|
| `method` | Split compound term: "a `:dt:`method` call expression" | Clean insert: "A `:dt:`method` is an `:t:`associated function` with a `:t:`self parameter`." |
| `item` | Non-definition promoted: "appears as an `:dt:`item`" (macro expansion rule) | Clean insert: "An `:dt:`item` is the most basic semantic element in program text." |
| `field` | Narrowed to enum context: "An `:dt:`enum field` is a `:dt:`field` of an enum variant" | Clean insert: "A `:dt:`field` is an element of an `:t:`abstract data type`." |

## Guardrails working in production

The definition-alignment guardrails caught a real violation during execution:

**Batch 005** (WA-007 `name`, WA-008 `item`, WA-009 `field`):
- WA-007 declared `definition_operation=insert` but the diff audit detected `swap_detected=true` and `insert_net=0` — the implementer had swapped `:dt:` markers instead of inserting the glossary definition.
- The post-commit validator fired `FAILED_INSERT_DIFF_MISMATCH` and the orchestrator automatically reverted the entire batch commit (`9b68d6a` → `de4fbe5`).

**Batch 006** (retry of WA-007, WA-008, WA-009):
- WA-007 was quarantined **pre-commit** this time — the orchestrator's pre-commit insert check detected the same swap pattern and refused to include WA-007 in the commit.
- WA-008 and WA-009 passed and were committed.

**Batch 009** (WA-007 retry):
- WA-007 was properly completed with actual glossary text insertion: "A `:dt:`name` is an `:t:`identifier` that refers to an `:t:`entity`."
- The diff audit confirmed `insert_pass=true`, `swap_detected=false`.

This is the exact scenario the swap-detection guardrail was designed for, and it worked at both enforcement points (post-commit revert and pre-commit quarantine).

## Definition divergence comparison

| Category | v2-baseline | v4-wave-a | v5-wave-a | Delta (v2→v5) |
|---|---|---|---|---|
| Exact match | 459 | 462 | 470 | +11 |
| Minor difference | 89 | 89 | 90 | +1 |
| Significant reword | 180 | 177 | 168 | −12 |
| Missing from chapter | 29 | 29 | 29 | 0 |

Net improvement: 12 terms moved from "significant reword" to "exact match" or "minor difference."

## Operation classification observation

Three terms (WA-005 `construct`, WA-006 `entity`, WA-007 `name`) are declared `promote` in the ledger but actually had new glossary definition paragraphs inserted into the chapter. The diff shows new `:dp:` IDs and new text. They should have been declared `insert`. Since these were declared `promote`, the hunk-level insert diff check was never triggered (it only runs for `insert` operations).

This doesn't affect quality — the text is correct, similarity is 1.0, and the subject-form check passed. But the operation metadata is inaccurate for 3/15 terms. The orchestrator's diff-audit index confirms: these three show `mode=fallback`, `dt_added=0` because the hunk analysis was skipped for non-insert operations.

For Wave B, this could be tightened by having the validator detect "positive net line delta on a promote-declared term" as a warning, suggesting the operation should have been `insert`. Not blocking for Wave A acceptance.

## Strict check

| State | Missing from chapters |
|---|---|
| v2-baseline | 29 |
| v4-wave-a | 29 |
| v5-wave-a | 29 |

Stable. The 29 are terms that exist as `:dt:` in the glossary but not in any chapter (they are defined only in the glossary). Wave A was not scoped to address these.

## Recommendation

**Pass the Wave A quality gate.** Generate `wa-quality-gate.json` with `status=pass` to unblock Wave B.

The observation about `promote` vs `insert` mislabeling (3 terms) should be noted for Wave B process improvement but does not warrant blocking.
