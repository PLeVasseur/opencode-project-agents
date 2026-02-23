# FLS PR #6 — Placement Fitness Analysis (Wave B)

## Commit state

| Label | Commit | Description |
|---|---|---|
| v2-baseline | `d8c5bc6` | Before any Wave A attempt |
| v5-wave-a | `e498c8d` | Wave A complete (15 terms) |
| v5-wave-b | `0db68fc` | Wave A+B complete (104 terms) |

## Cross-version comparison — global fitness

| Metric | v2-baseline | v5-wave-a | v5-wave-b | Delta (A→B) |
|---|---|---|---|---|
| Total chapter `:dt:` terms | 900 | 899 | 900 | +1 |
| Good fitness | 658 | 656 | 670 | +14 |
| Questionable fitness | 34 | 35 | 37 | +2 |
| Poor fitness | 67 | 67 | 49 | −18 |
| Neutral (no refs) | 141 | 141 | 143 | +2 |
| Files modified | — | 11 | 20 | — |
| Net line change | — | +27 | +171 | — |

Wave B improved global fitness: 18 terms moved out of "poor" and 14 into "good." The net improvement is driven by terms that were poorly placed in the original document and are now in their conceptual chapter homes.

## Wave B term fitness summary (89 terms)

| Rating | Count | Percentage |
|---|---|---|
| Good | 57 | 64% |
| Questionable | 16 | 18% |
| Poor | 12 | 13% |
| OK (no refs) | 4 | 4% |

### Poor fitness terms (12)

These terms have less than 10% of their `:t:` references in the same file as their `:dt:` definition:

| ID | Term | File | Total refs | Same-file | Notes |
|---|---|---|---|---|---|
| WB-003 | concrete type | types-and-traits.rst | 1 | 0 | Only 1 ref total; fitness metric unreliable |
| WB-004 | generic function | generics.rst | 1 | 0 | Only 1 ref total; fitness metric unreliable |
| WB-005 | variable | macros.rst | 34 | 2 | Placed in Metavariables section; refs scattered across many files |
| WB-010 | associated constant | expressions.rst | 23 | 2 | Placed in Constant Expressions; most refs in associated-items.rst |
| WB-014 | floating-point type | lexical-elements.rst | 24 | 2 | Placed near numeric literals; most refs in types-and-traits.rst |
| WB-029 | function body | functions.rst | 19 | 1 | Fitness metric picked up stale `:dt:` in types-and-traits.rst (see cross-file dup issue) |
| WB-032 | irrefutable pattern | patterns.rst | 21 | 0 | Has stale `:dt:` in statements.rst; correct target is patterns.rst |
| WB-040 | mutable variable | values.rst | 1 | 0 | Only 1 ref total |
| WB-043 | elaboration | items.rst | 2 | 0 | Low ref count |
| WB-046 | external function item type | types-and-traits.rst | 1 | 0 | Only 1 ref total |
| WB-047 | mutable | values.rst | 1 | 0 | Only 1 ref total |
| WB-057 | generic substitution | generics.rst | 6 | 0 | Refs in types-and-traits.rst and expressions.rst |

Of these 12, 5 have only 0–1 total references, making the fitness metric meaningless. The remaining 7 are genuinely scattered terms where no single file concentrates references. Note that WB-029 and WB-032 have their fitness underreported due to the cross-file duplicate issue (the analysis picked up the stale `:dt:` location rather than the correct target).

## Critical issue: 20 new cross-file `:dt:` duplicates

Wave A had 6 terms with `:dt:` in multiple chapter files. Wave B introduced 20 more, bringing the total to 26.

**Root cause:** When a term is "moved" (action_type=move), the operation should promote `:t:` → `:dt:` at the target AND demote `:dt:` → `:t:` at the source. Wave B consistently performed the first half but not the second. The old `:dt:` markers remain at their original locations.

**Impact by stale-location file:**

| File | Stale `:dt:` count |
|---|---|
| expressions.rst | 12 |
| types-and-traits.rst | 3 |
| patterns.rst | 2 |
| macros.rst | 1 |
| statements.rst | 1 |
| inline-assembly.rst | 1 |

**Affected terms (20):**

| Term | Target file | Stale `:dt:` in |
|---|---|---|
| associated type | associated-items.rst | expressions.rst |
| attribute content | attributes.rst | macros.rst |
| borrowed | ownership-and-deconstruction.rst | expressions.rst |
| dangling | values.rst | expressions.rst |
| discriminant | types-and-traits.rst | expressions.rst |
| enum variant value | types-and-traits.rst | patterns.rst |
| field index | types-and-traits.rst | expressions.rst |
| function body | functions.rst | types-and-traits.rst |
| immutable | ffi.rst | expressions.rst |
| irrefutable pattern | patterns.rst | statements.rst |
| mutable static | values.rst | expressions.rst |
| pointer | patterns.rst | expressions.rst |
| record enum variant | patterns.rst | expressions.rst |
| self parameter | functions.rst | types-and-traits.rst |
| signed integer type | types-and-traits.rst | expressions.rst |
| static | values.rst | expressions.rst |
| structurally equal | types-and-traits.rst | patterns.rst |
| type parameter | generics.rst | expressions.rst |
| type specification | macros.rst | types-and-traits.rst |
| underscore expression | macros.rst | inline-assembly.rst |

**Remediation required:** Each stale location needs `:dt:` → `:t:` demotion. This is a mechanical fix (20 marker swaps at the stale locations). No text needs to move — the definitions at the target locations are correct.

## Strict check

| State | Missing from chapters |
|---|---|
| v2-baseline | 29 |
| v5-wave-a | 29 |
| v5-wave-b | 26 |

The 3-term improvement is from glossary case normalization: `Elaboration`, `Evaluation`, `Execution` were lowercased to match their existing chapter `:dt:` markers. The remaining 26 are out-of-scope terms not assigned to Wave A or B.
