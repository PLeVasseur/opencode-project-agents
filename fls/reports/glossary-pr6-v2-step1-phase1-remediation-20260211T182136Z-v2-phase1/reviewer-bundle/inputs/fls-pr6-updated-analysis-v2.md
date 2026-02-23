# FLS PR #6 — Updated Analysis (v2)

**PR:** https://github.com/PLeVasseur/fls/pull/6
**New Commit:** `19e75856eac5694e5d613c7c59b429848d333992`
**Previous Commit:** `1c2c2b73313fb48987ed02ac044ff68cec69968e`
**Branch:** `glossary-step-1-main-text-coverage`
**Analysis Date:** 2026-02-11

## What Changed Between PR Versions

The PR was substantially reworked since the initial review. Key changes:

- **137 definitions moved** between chapter files (e.g., `value` from `values.rst` to `expressions.rst`, `method` from `associated-items.rst` to `expressions.rst`)
- **3 missing terms added:** `casting` (now in `expressions.rst`), `namespace qualifier` and `shadowed` (both in `entities-and-resolution.rst`)
- **2 definitions removed:** `crate import` and `declaration` were replaced with plural forms `[crate import]s` and `[declaration]s`
- **5 new definitions added** (the 3 missing terms plus the 2 plural replacements)
- **Branch renamed** from `phase-1-main-text-coverage` to `glossary-step-1-main-text-coverage`

## Placement Fitness — Comparison

| Metric | Old PR | New PR | Change |
|--------|--------|--------|--------|
| Good fit | 331 | 302 | -29 |
| Acceptable | 240 | 302 | +62 |
| Questionable | 129 | 111 | -18 |
| Poor | 73 | 61 | -12 |
| Forward references | 332 | 248 | **-84** |

### Adjusted Ratings (with conceptual home assessment)

| Rating | Old PR | New PR | Change |
|--------|--------|--------|--------|
| Good | 331 | 302 | -29 |
| Acceptable | 240 | 302 | +62 |
| Acceptable at home | 164 | 65 | -99 |
| Questionable | 24 | 58 | +34 |
| Poor | 14 | 49 | +35 |

### Relocation Priorities

| Priority | Old PR | New PR | Change |
|----------|--------|--------|--------|
| High | 14 | 49 | +35 |
| Medium | 24 | 49 | +25 |
| Low (forward ref) | 146 | 48 | -98 |
| None | 589 | 630 | +41 |

### Interpretation

Forward references dropped significantly (332 → 248) — many terms were moved closer to their first use, which was one of the goals. However, the relocation also created a new tension: **high-priority relocations rose from 14 to 49**. Many foundational terms were moved to their first-use site, which puts them in contextually narrow sections rather than their conceptual home.

Notable examples of this tension:

- **`value`** moved from `values.rst::Values` to `expressions.rst::Type Cast Expressions` — no longer a forward reference, but "value" is now defined inside a section about type casts
- **`expression`** moved from `expressions.rst::Expressions` to `types-and-traits.rst::Type Inference` — the most fundamental expression concept is now defined in a type inference section
- **`reference`** moved from `ownership-and-deconstruction.rst::References` to `expressions.rst::Borrow Expression` — narrower context than the concept deserves
- **`trait`** moved from `types-and-traits.rst` to `entities-and-resolution.rst::Path Expression Resolution`
- **`field`** moved from `types-and-traits.rst::Abstract Data Types` to `patterns.rst::Record Struct Patterns`
- **`implementation`** moved from `implementations.rst` to `generics.rst::Generic Parameters`

These moves resolve forward references but sacrifice conceptual coherence. The terms are now defined in the first place they happen to be *used*, which isn't necessarily where a reader would *look* for them.

## Definition Divergence — Comparison

| Category | Old PR | New PR | Change |
|----------|--------|--------|--------|
| Exact match | 499 | 461 | -38 |
| Cosmetic | 127 | 50 | -77 |
| Extended | 24 | 27 | +3 |
| Moderate divergence | 49 | 44 | -5 |
| Significant reword | 68 | 160 | **+92** |
| Inline definition | — | 7 | +7 |
| Glossary cross-ref | 24 | 24 | 0 |
| Chapter redirect | 6 | 1 | -5 |
| Missing from chapter | 3 | 2 | -1 |
| Chapter only | 183 | 185 | +2 |

### Reliability Summary

| Rating | Old PR | New PR | Change |
|--------|--------|--------|--------|
| High | 626 | 535 | -91 |
| Medium | 79 | 79 | 0 |
| Low | 68 | 160 | **+92** |
| Missing | 3 | 2 | -1 |
| New term | 183 | 185 | +2 |

### Interpretation

The jump in significant rewords (68 → 160) is largely because moved terms now appear inline within other paragraphs rather than as standalone definitions. When `crate` is defined in a sentence that starts "Procedural macros shall be defined in a :dt:`crate` subject to attribute crate_type...", the surrounding context is completely different from the glossary's standalone "A crate is a unit of compilation and linking that contains a tree of nested modules." The definition isn't wrong — the `:dt:` correctly marks the first defining use — but the paragraph serves a different purpose than the glossary entry.

Examples of this pattern:

- **`arity`** (sim: 0.073) — Glossary: "the number of tuple fields in a tuple type." Chapter: appears inline in a sentence about record struct pattern matching position calculation. The glossary definition is a clean standalone; the chapter mention is incidental.
- **`crate root module`** (sim: 0.059) — Glossary: "the root of the nested module tree of a crate." Chapter: embedded in a long sentence about the external prelude bringing entities in scope.
- **`associated item`** (sim: 0.212) — Glossary: "an item that appears within an implementation or a trait." Chapter: appears in a paragraph about macro invocation context.
- **`attribute`** (sim: 0.344) — Glossary: "a general, free-form metadatum interpreted based on its name..." Chapter: "Attribute cfg enables conditional compilation."

The 29 terms that improved from low reliability include many glossary cross-references that were previously mismatched (e.g., `abi`, `addition assignment`, `while loop` — these now correctly show as `glossary_xref` in the glossary and the chapter `:dt:` was moved elsewhere or removed).

### Still Missing (2 terms)

- **`crate import`** — replaced with plural form `[crate import]s`
- **`declaration`** — replaced with plural form `[declaration]s`

These are likely intentional; the plural `:dt:` forms serve the same purpose.

## Recommendations

1. **Review the 49 high-priority relocation candidates.** Many are foundational terms (`value`, `expression`, `reference`, `trait`, `field`, `implementation`) that were moved to first-use sites but lost conceptual coherence. Consider whether these terms should return to their conceptual home chapters, even at the cost of forward references.

2. **Address the 160 low-reliability divergences.** Most are caused by terms being defined inline within paragraphs that serve a different purpose than the glossary definition. Before Phase 2 (deriving the glossary from chapter text), decide: should the glossary adopt these contextual definitions, or should the chapter definitions be made standalone?

3. **The forward-reference vs. conceptual-home tradeoff** is the core design question this PR surfaces. A specification is not a tutorial — readers don't necessarily read linearly. Having `value` defined in `values.rst` may be more useful than having it defined at its first `:t:` reference in `expressions.rst::Type Cast Expressions`, even though the latter eliminates a forward reference.
