# FLS PR #6 — Wave B Quality Review

## Verdict

Wave B successfully placed definitions for all 89 terms with strong glossary alignment (74/89 exact match, 14/89 close, 1 marginal). The definition-alignment guardrails operated throughout, quarantining 52 term attempts across 12 batches and catching 2 strict check regressions. However, a systematic execution gap left 20 stale `:dt:` markers at old locations, creating cross-file duplicates that need mechanical cleanup before merge.

## Execution summary

| Metric | Value |
|---|---|
| Commit range | `e498c8d` → `0db68fc` |
| Wave B terms completed | 89/89 |
| Batches completed (successful) | 8 (of 12 total) |
| Batches failed/reverted | 5 |
| Failure reasons | 3× full-batch quarantine, 2× strict check regression |
| Total term-level quarantines | 52 (all resolved) |
| Insert operations | 22 (all passed hunk check, 0 swaps) |
| Promote operations | 59 |
| Adapt operations | 8 |
| Deviation permits | 0 |
| Execution integrity verdict | pass |
| Files modified | 20 (including glossary.rst) |
| Lines: inserted / deleted / net | 309 / 138 / +171 |

## Definition alignment: 89 WB terms

### Operation breakdown

| Operation | Count | Similarity range | Description |
|---|---|---|---|
| promote | 59 | 0.750–1.000 | Chapter already had glossary-equivalent text; `:t:` promoted to `:dt:` |
| insert | 22 | 1.000 | Glossary definition text inserted as new paragraph |
| adapt | 8 | 0.625–1.000 | Chapter text reworded to align with glossary while fitting context |

### Alignment quality

| Category | Count | Percentage |
|---|---|---|
| Exact match (glossary = chapter) | 74 | 83% |
| Close match (≥0.85 Jaccard) | 4 | 4% |
| Adapted (0.50–0.84) | 11 | 12% |
| Missing from chapter | 0 | 0% |

### Adapted terms requiring attention

Six terms have Jaccard similarity below 0.75 — all are intentional rewrites, but two have quality concerns:

| ID | Term | Sim | Glossary says | Chapter says | Assessment |
|---|---|---|---|---|---|
| WB-047 | mutable | 0.538 | "A value is mutable when it can be modified." | "mutable is the property of a value that can be modified." | **Missing article** — "mutable" as bare adjective without "A" violates subject-form pattern |
| WB-042 | [unifiable type]s | 0.417 | "Two types that unify are said to be unifiable types." | "unifiable types are two types that unify." | Acceptable restructure for subject-form |
| WB-026 | immutable | 0.636 | "A value is immutable when it cannot be modified." | "An immutable value is a value that cannot be modified." | Good subject-form conversion |
| WB-027 | signed integer type | 0.688 | "...denote negative whole numbers, zero, and positive whole numbers." | "...denote signed whole numbers." | **Semantic loss** — chapter definition drops the explicit enumeration. Original is more precise. |
| WB-002 | type specification | 0.727 | "describes the structure of a type" | "is a construct that describes the structure of a type" | Acceptable — adds construct framing |
| WB-041 | discriminant initializer | 0.727 | "provides the value of a discriminant" | "is a construct that provides the value of a discriminant" | Acceptable — adds construct framing |

**WB-047** (`mutable`): The chapter definition reads `:dt:\`mutable\` is the property of a :t:\`value\` that can be modified.` Missing the article "A" before the term — inconsistent with the subject-form pattern used by all other definitions. Minor fix needed.

**WB-027** (`signed integer type`): The glossary explicitly enumerates "negative whole numbers, zero, and positive whole numbers." The chapter simplifies to "signed whole numbers." This loses specificity — the glossary wording is more precise for a specification document. Consider restoring the full enumeration.

## Guardrail behavior in production

### Batch failure timeline

| Batch | Outcome | Terms | Cause |
|---|---|---|---|
| 010 | ✅ Success (2 quarantined) | WB-001–WB-020 | WB-017, WB-020 quarantined pre-commit |
| 011 | ❌ Full quarantine | WB-021–WB-040 | All 20 terms failed pre-commit validation |
| 012 | ❌ Full quarantine | WB-041–WB-060 | All 20 terms failed pre-commit validation |
| 013 | ❌ Full quarantine | WB-017–WB-038 (retry) | All 20 terms failed pre-commit validation |
| 014 | ✅ Success (2 quarantined) | WB-017–WB-038 | WB-024, WB-028 quarantined |
| 015 | ✅ Success (3 quarantined) | WB-024–WB-056 | WB-043, WB-045, WB-053 quarantined |
| 016 | ❌ Strict check regression | WB-043–WB-073 | Post-commit strict check: 1 newly-missing term |
| 017 | ❌ Strict check regression | WB-061–WB-080 | Post-commit strict check: 1 newly-missing term |
| 018 | ✅ Success (6 quarantined) | WB-061–WB-080 | 6 quarantined, 14 passed |
| 019 | ✅ Success (3 quarantined) | WB-081–WB-089 | WB-082, WB-084, WB-089 quarantined |
| 020 | ✅ Success (1 quarantined) | Retry batch | WB-082 quarantined |
| 021 | ✅ Success | WB-082 (final retry) | Completed |

The system self-corrected through retries. 52 individual term quarantines across 12 batches, all eventually resolved. Batches 016–017 demonstrate the strict check catching a commit that removed a `:dt:` marker without replacement — the orchestrator rolled back the worktree and ledger, then succeeded on retry.

### Insert guardrail results

All 22 insert operations passed the hunk-level diff check with `insert_pass=True` and `swap_detected=False`. Zero swap-as-insert attempts reached a committed state. The Wave A guardrail fix (swap detection via `analyze_dt_insert_patch`) prevented any marker-swap shortcuts in Wave B.

## Critical issue: 20 stale `:dt:` markers

**Severity: High — blocks merge-readiness**

Wave B introduced 20 new cross-file `:dt:` duplicates. Each term correctly has `:dt:` at its new target location, but the old location's `:dt:` was not demoted to `:t:`.

| Source of stale markers | Count |
|---|---|
| expressions.rst | 12 |
| types-and-traits.rst | 3 |
| patterns.rst | 2 |
| Other (macros, statements, inline-assembly) | 3 |
| **Total** | **20** |

Combined with 6 pre-existing duplicates from Wave A, there are now 26 terms with `:dt:` in multiple chapter files.

**Root cause:** The `promote` operation correctly swaps `:t:` → `:dt:` at the target, but the complementary demotion (`:dt:` → `:t:` at the source) is not enforced by the tooling. The validator checks that `:dt:` exists at the target; it does not check that `:dt:` does NOT exist elsewhere for the same term.

**Remediation:** 20 mechanical `:dt:` → `:t:` demotions at the stale locations. No text changes needed — the definitions at the target locations are correct. A single commit could fix all 20.

## Definition divergence: cross-version comparison

| Category | v2-baseline | v5-wave-a | v5-wave-b | Delta (baseline→B) |
|---|---|---|---|---|
| Exact match | 459 | 470 | 528 | **+69** |
| Minor difference | 89 | 90 | 99 | +10 |
| Significant reword | 180 | 168 | 104 | **−76** |
| Missing from chapter | 29 | 29 | 26 | −3 |

Wave A+B moved 76 terms from "significant reword" toward exact or close alignment. 69 terms achieved exact glossary-chapter alignment that didn't exist at baseline. The 3 newly-covered terms (Elaboration, Evaluation, Execution) came from glossary case normalization.

## Glossary modifications

Wave B modified `src/glossary.rst` to lowercase 5 term names:

| Old | New | Coverage impact |
|---|---|---|
| `C` | `c` | None (already covered) |
| `Elaboration` | `elaboration` | Now matches chapter `:dt:` |
| `Evaluation` | `evaluation` | Now matches chapter `:dt:` |
| `Execution` | `execution` | Now matches chapter `:dt:` |
| `Undefined behavior` | `undefined behavior` | None (already covered) |

This is appropriate — the FLS uses lowercase for these terms in chapter text, so the glossary should match.

## Recommendations

1. **Block merge until stale `:dt:` markers are cleaned up.** The 20 cross-file duplicates are a spec-quality issue: a term should have exactly one `:dt:` definition site in the chapters. Fix is mechanical — a single commit with 20 `:dt:` → `:t:` swaps at the stale locations listed in the placement fitness report.

2. **Fix WB-047 (`mutable`) subject-form article.** Add "A" before `:dt:\`mutable\`` to match the pattern: "A `:dt:\`mutable\`` value is..."

3. **Consider restoring WB-027 (`signed integer type`) full enumeration.** The glossary's "negative whole numbers, zero, and positive whole numbers" is more precise than the chapter's "signed whole numbers."

4. **Add cross-file `:dt:` uniqueness check to the validator.** The tooling should verify that each term has `:dt:` in exactly one chapter file. This would have caught the stale-marker issue during execution rather than in review.

5. **Wave A pre-existing duplicates (6 terms) should also be cleaned.** Terms: field, implementation, implemented trait, item, method, reference.
