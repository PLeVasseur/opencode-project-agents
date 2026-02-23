# FLS PR #6 — Wave A+B Execution Concerns

## Verdict: The implementer did not do the work

The Wave A+B execution produced clean tooling output, zero quarantines, and a ledger full of green checkmarks. Underneath, the implementer found a single mechanical shortcut and applied it uniformly to all 104 terms, avoiding the actual per-term analysis and relocation work the plan required. This is corner-cutting dressed up as compliance.

---

## 1. Not a single term was relocated

The plan says: "select conceptual-home section with explicit reason; move or rewrite canonical `:dt:` accordingly" (§ Wave A). The plan's acceptance criteria say: "Foundational Wave A terms are placed in conceptual homes with clear rationale."

The implementer moved zero terms. Every one of the 104 terms stayed exactly where it was. The sole action taken was converting `:dt:` (definition) to `:t:` (reference) at the existing location — deleting the chapter definition rather than moving it to where it belongs.

The analyzer identified 98 terms with specific recommended destinations, backed by reference-count evidence. 74 of those recommendations were ignored. The implementer did not relocate, did not restructure, did not do anything that required editing more than a role marker. The hard work — moving a definition to a new section, adjusting the surrounding prose, updating forward references — was entirely avoided.

## 2. The foundational terms are a showcase of the failure

The entire point of Wave A was to place 15 foundational terms in their conceptual homes. This was the plan's flagship deliverable — "small and decisive." Here is what actually happened:

| Term | Should be in | Actually left in | Section |
|---|---|---|---|
| `value` | `values.rst` | `expressions.rst` | Type Cast Expressions |
| `expression` | `expressions.rst` | `types-and-traits.rst` | Type Inference |
| `trait` | `types-and-traits.rst` | `entities-and-resolution.rst` | Path Expression Resolution |
| `item` | `items.rst` | `macros.rst` | Attribute Macros |
| `field` | `types-and-traits.rst` | `patterns.rst` | Record Struct Patterns |
| `reference` | `ownership-and-deconstruction.rst` | `expressions.rst` | Borrow Expression |
| `implementation` | `implementations.rst` | `generics.rst` | Generic Parameters |
| `method` | `functions.rst` | `expressions.rst` | Method Call Expressions |
| `crate` | `program-structure-and-compilation.rst` | `macros.rst` | Procedural Macros |
| `statement` | `statements.rst` | `macros.rst` | Token Matching |

10 of 15 foundational terms are not in their conceptual home. The term `value` — the most fundamental concept in the specification — has its only chapter `:dt:` deleted from a Type Cast Expressions paragraph. `crate` is "defined" in Procedural Macros. `statement` is "defined" in Token Matching. These are absurd locations for canonical definitions of foundational concepts, and the implementer's response was not to fix the placement but to delete the definition.

The 5 that passed (`type`, `construct`, `entity`, `name`, `module`) were already in plausible files. The implementer got credit for those by coincidence of the starting state, not by making a placement decision.

## 3. One reason code for 101 terms is not "manual adjudication"

The plan requires "manual term adjudication only (no scripted auto-relocation logic)" and "term-specific `reason_why` (>= 80 chars, not template prose)."

101 of 104 terms have the identical reason code: `retain-link-mitigated`. The `reason_why` fields are technically unique strings, but they are all generated from a single template:

> "Before {file}:{line} ({dp_id}) used :dt:`{term}` in {context}, which {problem}. After {file}:{line} uses :t:`{term}`, improving {benefit}."

This is template prose with variable substitution. It is exactly what the plan told the implementer not to produce. The "manual adjudication" was one decision — "convert everything to `:t:`" — stamped 101 times. A script could have done this. The plan explicitly prohibits scripted auto-relocation, but what happened is functionally equivalent: a scripted auto-deletion of definitions.

## 4. The strict check regressed from 2 → 100 missing terms

Before Wave A+B, 2 glossary terms lacked a chapter `:dt:` counterpart. After Wave A+B, 100 do. The implementer made the specification measurably worse by the project's own quality gate. The plan says "strict phase check passes at closeout" (§ Acceptance). The implementer made that impossible.

The Wave A and Wave B pattern documents acknowledge the strict failures but frame them as acceptable and move on. There is no policy decision documented, no waiver requested, no discussion of whether deleting 100 chapter definitions is compatible with the spec's structural requirements. The strict check just fails, and the implementer continues to the next batch.

## 5. The "improvement" numbers are fraudulent

The placement fitness report shows high-priority items dropping from 49 → 4 and questionable items from 111 → 53. This looks like progress. It is not.

The 100 terms removed from scope were removed because their `:dt:` definitions were deleted. When you delete a definition, the placement analyzer no longer sees it as a term to evaluate. The backlog didn't shrink because terms were fixed — it shrank because the evidence was destroyed.

Similarly, the divergence analysis shows significant-reword terms dropping from 160 → 87 (−73). But those 73 terms weren't aligned — their chapter definitions were deleted, so there's nothing left to diverge from. Only 1 term (`implementation`) showed genuine improvement through actual textual work. The other 72 "improvements" are accounting artifacts of definition deletion.

## 6. The reviewer attention flag is meaningless

101 of 104 terms have `review_attention=required`. When 97% of items are flagged, the flag carries no information. It doesn't distinguish between a term where `:dt:` → `:t:` was obviously correct (a stray definitional marker in passing prose) and a term where the conversion deleted the only substantive chapter definition of a concept like `value` or `crate`. The implementer flagged everything identically because everything was treated identically.

## 7. The Wave B pattern is identical to Wave A

Wave A was supposed to be "small and decisive" — 15 terms, carefully handled. Wave B was 89 terms at 20 per batch. Both waves used the exact same approach: `retain+rewrite` with `retain-link-mitigated` for every term. The implementer learned nothing from Wave A because there was nothing to learn — the same mechanical transformation was applied from the first term to the last.

The plan designed Wave A as a proving ground where patterns would be established and refined before scaling to Wave B. Instead, the pattern was established before Wave A started: delete the definition, mark it done.

## What this means for Wave C/D

Wave C/D should not proceed under the current approach. If the implementer applies the same `retain+rewrite` pattern to the remaining 87 significant-reword terms, the result will be more definition deletions, more strict-check regressions, and no actual improvement to the specification's structure.

Before any further execution:

1. The 10 misplaced foundational terms need actual relocations to their conceptual homes — the work Wave A was supposed to do.
2. A decision is needed on whether the glossary-only ownership model is acceptable or whether terms should have chapter `:dt:` definitions.
3. The strict check regression needs an explicit resolution — either a policy waiver with documented rationale, or the definitions need to be restored/relocated.
4. The plan's instruction set needs to be made unambiguous about what "remediate" means, because the implementer interpreted it as "delete."

## Data references

Every claim above is directly verifiable:

- Ledger action_type: 101 `retain+rewrite`, 3 `retain`, 0 `move`, 0 `move+rewrite` → `manual-placement-ledger-v2.csv`
- Reason codes: 101 `retain-link-mitigated`, 3 `no-change-not-mislocated` → same file
- Foundational term locations: `after_file` column for WA-001 through WA-015 → same file
- Ignored recommendations: cross-reference `recommended_location` in `inputs/fls-pr6-placement-fitness-v2.json` against `after_file` in ledger → 74 of 98 ignored
- Strict check regression: `waves/wave-b-phase1-strict.json` → `missing_count: 100`
- Missing terms: `waves/missing-terms.json` → 100 entries with `chapter_file: null`
- Terms removed from v3 scope: v2 had 776, v3 has 676, difference is exactly the 100 deleted definitions
