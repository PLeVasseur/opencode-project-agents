# FLS PR #6 — Placement Fitness Analysis (v5 Wave A)

## Commit state

| Label | Commit | Description |
|---|---|---|
| v2-baseline | `d8c5bc6` | Before any Wave A attempt |
| v4-wave-a | `d74a460` | First Wave A (marker swaps only) |
| v5-wave-a | `e498c8d` | Current Wave A (with definition-alignment guardrails) |

## Cross-version comparison

| Metric | v2-baseline | v4-wave-a | v5-wave-a |
|---|---|---|---|
| Total chapter `:dt:` terms | 900 | 900 | 899 |
| Good fitness | 658 | 656 | 656 |
| Questionable fitness | 34 | 35 | 35 |
| Poor fitness | 67 | 68 | 67 |
| Neutral (no refs) | 141 | 141 | 141 |
| Files modified | — | 13 | 11 |
| Net line change | — | +0 (20 ins, 20 del) | **+27 (43 ins, 16 del)** |

The v4 run had exactly zero net lines — every change was a marker swap. The v5 run has +27 net lines, confirming actual text insertion.

## Wave A term fitness ratings

| ID | Term | File | Section | Fitness | Operation |
|---|---|---|---|---|---|
| WA-001 | value | values.rst | Values | poor | insert |
| WA-002 | expression | expressions.rst | Expressions | good | promote |
| WA-003 | type | types-and-traits.rst | Type Coercion | good | adapt |
| WA-004 | trait | types-and-traits.rst | Traits | good | promote |
| WA-005 | construct | entities-and-resolution.rst | Generic Parameter Scope | questionable | promote |
| WA-006 | entity | entities-and-resolution.rst | Path Resolution | good | promote |
| WA-007 | name | entities-and-resolution.rst | Visibility | good | promote |
| WA-008 | item | items.rst | Items | good | insert |
| WA-009 | field | types-and-traits.rst | Struct Types | good | insert |
| WA-010 | reference | ownership-and-deconstruction.rst | References | good | insert |
| WA-011 | implementation | implementations.rst | Implementations | questionable | promote |
| WA-012 | method | functions.rst | Functions | poor | insert |
| WA-013 | crate | program-structure-and-compilation.rst | Crates | good | promote |
| WA-014 | module | program-structure-and-compilation.rst | Modules | questionable | promote |
| WA-015 | statement | statements.rst | Statements | questionable | insert |

**Summary**: 9 good, 4 questionable, 2 poor.

## Analyzer fitness paradox (unchanged from v4)

The "poor" ratings for `value` and `method` are expected and correct. The fitness metric optimizes for reference concentration — it asks "what fraction of `:t:` references to this term are in the same file as the `:dt:`?" Foundational terms like `value` and `method` are referenced across nearly all 28 chapter files, so no single file achieves high concentration. The analyzer would recommend moving them back to their old locations because those had the highest raw reference counts — but the old locations were semantically wrong (e.g., `value` was defined inside "Type Cast Expressions," `method` was inside "Method Call Expressions").

The correct evaluation for foundational terms is: (1) is the term in its conceptual home? (2) does the `:dt:` sentence match the glossary definition? Both are yes for all 15 terms.

## Placement changes from v4

The `field` term moved from `types-and-traits.rst:Enum Types` (v4) to `types-and-traits.rst:Struct Types` (v5). This is an improvement — fields are a property of struct types broadly, not just enum types. The v4 placement landed on "An `:dt:`enum field` is a `:dt:`field` of an `:t:`enum variant`" which narrowed the concept. The v5 placement inserts the general glossary definition "A `:dt:`field` is an element of an `:t:`abstract data type`" in the Struct Types section, which is the first place struct fields are discussed.
