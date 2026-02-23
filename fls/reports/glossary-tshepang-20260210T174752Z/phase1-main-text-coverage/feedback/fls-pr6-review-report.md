# PR #6 Review: Phase 1 Main Text Coverage — Glossary Migration

**PR:** https://github.com/PLeVasseur/fls/pull/6
**Branch:** `phase-1-main-text-coverage`
**Commit:** `1c2c2b73313fb48987ed02ac044ff68cec69968e`
**Review Date:** 2026-02-10

## Executive Summary

This PR implements Phase 1 of the FLS glossary migration strategy, which adds `:dt:` (definition-term) markup to chapter text so that every glossary term has a canonical definition in the chapter where it is first introduced. The goal is to make the glossary a rendered output from body text rather than a standalone source of truth.

**Overall assessment:** The PR substantially achieves its Phase 1 goals. Coverage is near-complete (773 of 776 glossary terms now have chapter definitions), no banned directives were introduced, and tooling guardrails are in place. The primary concern is **68 terms with significantly divergent definitions** between glossary and chapter text, plus **3 terms missing from chapters entirely**.

## Scope of Changes

The PR touches 22 chapter files plus configuration and tooling:

| File | `:dt:` | `:dc:` | `:dp:` | Notes |
|------|--------|--------|--------|-------|
| expressions.rst | 216 | 0 | 924 | Largest change |
| types-and-traits.rst | 181 | 14 | 760 | Heavy use of `:dc:` for numeric types |
| entities-and-resolution.rst | 98 | 0 | 368 | Many resolution-specific new terms |
| patterns.rst | 63 | 0 | 268 | Pattern matching vocabulary |
| lexical-elements.rst | 55 | 0 | 200 | |
| macros.rst | 36 | 0 | 189 | |
| attributes.rst | 34 | 43 | 291 | Most `:dc:` for attribute names |
| ownership-and-deconstruction.rst | 33 | 0 | 161 | |
| inline-assembly.rst | 30 | 2 | 324 | |
| generics.rst | 29 | 0 | 84 | |
| values.rst | 24 | 1 | 69 | |
| Other 11 files | 98 | 0 | 608 | |
| **TOTAL** | **897** | **60** | **4046** | |

New tooling added:

- `tools/glossary-migration-check.py` (608 lines): Standalone validation script for term coverage, definition alignment, and banned directive detection.
- `exts/ferrocene_spec_lints/glossary_migration.py` (67 lines): Sphinx build-time lint extension enforcing phase guardrails.
- `src/conf.py`: Three new config values (`lint_glossary_migration_phase`, `lint_glossary_migration_strict`, `lint_glossary_migration_report`).

## What Passes

### No Banned Directives

Zero instances of `.. glossary-entry::` or `.. glossary-include::` were found across all `.rst` files. This is the hard Phase 1 constraint and it is satisfied.

### No Cross-File Duplicate Definitions

Every `:dt:` term is defined in exactly one chapter file. There are zero cases where two different chapter files both define the same term with `:dt:`. This is critical for the single-source-of-truth model.

### Glossary Source Unchanged

The glossary file (`src/glossary.rst`) retains all 757 `:dt:` and 19 `:dc:` definitions from main. No glossary definitions were removed, added, or modified. This is correct for Phase 1, which adds chapter coverage without touching the glossary.

### High Coverage

Of 776 unique glossary terms, 773 (99.6%) now have a corresponding `:dt:` or `:dc:` definition in chapter text.

### Numeric Types Correctly Use `:dc:`

Types like `u8`, `i32`, `f64`, `usize`, etc. appropriately use `:dc:` (definition-code) rather than `:dt:` (definition-term), as these are code identifiers rather than prose terms.

### Redirect Definitions Are Reasonable

The PR introduces 6 redirect-style chapter definitions of the form `:dt:`X`, see :t:`Y``. These are all legitimate aliases pointing to the canonical term:

- `atomic` → `atomic type`
- `evaluated` → `evaluation`
- `assignment` → `assignment expression`
- `loop` → `loop expression`
- `for loop` → `for loop expression`
- `range-full expression` → `full range expression`

Separately, `executed` → `execution`, `representation` → `type representation`, `elided` → `elided lifetime`, `infinite loop` → `infinite loop expression`, and `unsafe Rust` → `[unsafe operation]s` follow the same pattern.

## Issues

### Issue 1: Three Terms Missing from Chapters

Three glossary terms have no `:dt:` definition in any chapter:

**`casting`** — The glossary defines both `Cast` and `casting` in a single sentence: `:dt:`Cast` or :dt:`casting` is the process of...`. The chapter (`expressions.rst`) only defines `:dt:`cast``. The co-definition of `casting` was dropped.

**`namespace qualifier`** — Used inline in the definition of `path` in `entities-and-resolution.rst` as a `:t:` reference but never promoted to `:dt:`. The glossary defines it as `:dt:`namespace qualifier` ``::`` that resolves to an :t:`entity``.`

**`shadowed`** — The chapter defines `:dt:`shadowing`` but not `:dt:`shadowed``. The glossary defines both. In the chapter, `shadowed` appears only as `:t:`shadowed <shadowing>``, a reference back to the `shadowing` definition.

**Recommendation:** Add `:dt:`casting`` alongside `cast` in `expressions.rst`. For `namespace qualifier` and `shadowed`, decide whether these warrant standalone definitions or whether the existing cross-references are sufficient.

### Issue 2: 68 Terms with Significant Definition Divergence

68 terms have chapter definitions that differ substantially from their glossary definitions (similarity ratio below 0.70). These represent potential **semantic drift** where the chapter may be saying something materially different from the glossary.

The most concerning examples, ordered by divergence severity:

| Term | File | Similarity | Nature of Divergence |
|------|------|-----------|---------------------|
| `simple c string literal` | lexical-elements.rst | 0.258 | Glossary defines character exclusions; chapter defines it as "where the characters are [simple string literal] characters" |
| `ffi` | ffi.rst | 0.273 | Glossary: "set of language features"; chapter: "mechanism for calling functions in non-Rust ABIs" |
| `primitive representation` | types-and-traits.rst | 0.295 | Chapter adds details about applicability to enum types and combination with C representation |
| `char` | types-and-traits.rst | 0.320 | Glossary says "denote Unicode characters"; chapter specifies 32-bit ranges 0x000-0xD7FF and 0xE000-0x10FFFF |
| `syntactic category` | general.rst | 0.339 | Glossary: "nonterminal in the BNF grammar"; chapter: "grammar symbol denoted in PascalCase" |
| `unnamed lifetime` | types-and-traits.rst | 0.338 | Glossary: "declared with character 0x5F"; chapter: "the `'_` lifetime" |
| `binding mode` | patterns.rst | 0.352 | Glossary: "mechanism by which a matched value is bound"; chapter: "describes whether a binding captures by value, by reference, or by mutable reference" |
| `recursive type` | types-and-traits.rst | 0.355 | Glossary: "may define other types within its type specification"; chapter: "contained types refer back to the containing type" |
| `async closure type` | expressions.rst | 0.375 | Glossary: "unique anonymous function type that encapsulates all capture targets"; chapter: "closure type defined by an async closure expression" |
| `implementation conformance` | implementations.rst | 0.400 | Glossary: "measures compatibility between implementation and trait"; chapter: "exhibits conformance when it satisfies the constraints of its trait" |
| `control flow boundary` | expressions.rst | 0.417 | Glossary: "limits control flow from returning beyond the construct"; chapter: "provides the target of a [return/break] and bounds its control flow transfer" |
| `call conformance` | expressions.rst | 0.426 | Glossary: "measures compatibility between argument operands and function parameters"; chapter: "requirement that a call expression uses the ABI of the invoked function" — these describe different aspects |
| `borrowed` | ownership-and-deconstruction.rst | 0.434 | Glossary: "memory location is borrowed when reference pointing to it is active"; chapter: "value is borrowed when associated with an active borrow" — different subjects (memory location vs value) |
| `construct` | entities-and-resolution.rst | 0.500 | Glossary: "piece of program text that is an instance of a syntactic category"; chapter: "syntactic element of a Rust program defined by this specification" |
| `concrete type` | types-and-traits.rst | 0.511 | Glossary: "type described by a type specification"; chapter: "type where all type/constant parameters have been substituted with generic arguments" — fundamentally different definitions |
| `sized type` | types-and-traits.rst | 0.557 | Glossary: "type with statically known size"; chapter: "type that implements the Sized trait" — equivalent but stated differently |
| `unsized type` | types-and-traits.rst | 0.549 | Mirror of `sized type` divergence |
| `statement` | statements.rst | 0.451 | Glossary: "component of a block expression"; chapter: "construct described by Statement" — different framing |

**Analysis:** Some divergences are benign (the chapter provides a more precise or contextually appropriate definition), but others represent genuine semantic differences. `call conformance` and `concrete type` are particularly notable because the glossary and chapter definitions describe different concepts under the same name.

**Recommendation:** Each of the 68 terms should be reviewed to determine whether the chapter definition is an intentional improvement (in which case the glossary should eventually be updated to match) or an unintentional deviation (in which case the chapter should be aligned with the glossary). This is critical to resolve before Phase 2, which would start removing glossary-side definitions.

### Issue 3: 49 Terms with Moderate Divergence

An additional 49 terms have similarity ratios between 0.70 and 0.90. These are less concerning — typically the chapter extends the definition with additional context or uses slightly different phrasing — but should be reviewed for consistency.

### Issue 4: 183 Chapter-Only Terms

183 terms are defined with `:dt:` or `:dc:` in chapter text but have no corresponding glossary entry. These fall into several categories:

**Attribute names (63 terms in `attributes.rst`):** Individual attribute identifiers like `cfg`, `derive`, `repr`, `test`, `inline`, `no_mangle`, etc. These use `:dc:` and are reasonably defined only in context rather than the glossary.

**Resolution and method lookup terms (36 terms in `entities-and-resolution.rst`):** Specialized terms like `candidate callee type`, `candidate receiver type chain`, `method resolution inherent implementation candidate lookup`. These are implementation-detail concepts that may not warrant glossary entries.

**Expression subtypes (24 terms in `expressions.rst`):** Cast subtypes (`address-to-pointer cast`, `enum cast`, `numeric cast`), capture modes (`by immutable reference capture`, `by value capture`), and other expression-related terms.

**Pattern matching mechanics (20 terms in `patterns.rst`):** `pattern matching`, `identifier pattern matching`, `literal pattern matching`, etc.

**Other chapters (40 terms):** Scattered across ownership, types/traits, concurrency, FFI, etc.

**Recommendation:** This is likely acceptable for Phase 1 — these are terms that naturally emerge in chapter text. The question of whether they should be back-propagated to the glossary is a Phase 2+ concern.

### Issue 5: Paragraph ID Format Inconsistency

The PR introduces 846 new `:dp:` paragraph IDs with a **mixed-case alphanumeric format** (e.g., `fls_nNisRZ6p4T6u`, `fls_FJEqMV7Qt6ZJ`), while the existing 3,039 IDs use a **lowercase hex-like format** (e.g., `fls_klcltwcwrw6i`, `fls_7kb6ltajgiou`). An additional 168 IDs have shorter lowercase formats that don't match either pattern.

This is cosmetically inconsistent but functionally harmless — the IDs serve as stable paragraph anchors and their format doesn't affect correctness. The mixed-case IDs were likely generated by a different version of the ID generation tool.

**Recommendation:** Not a blocker, but consider standardizing on one format for future additions.

### Issue 6: `call site hygiene` Defined Inside a List Item

The `:dt:` for `call site hygiene` appears inside a bullet-list item in `macros.rst`:

```rst
* :dp:`fls_puqhytfzfsg6`
  :dt:`call site hygiene`, which resolves to a :s:`MacroInvocation` site.
```

While this is semantically correct (the definition is contextually appropriate as part of a hygiene-type enumeration), it may cause issues for automated extraction tools that expect `:dt:` definitions in standalone paragraphs. The similarity score (0.65) also reflects that the glossary has a standalone definition while the chapter embeds it in list context.

## Tooling Assessment

### `tools/glossary-migration-check.py`

The 608-line validation script is well-structured. It:

- Extracts `:dt:` and `:dc:` definitions from both glossary and chapters
- Compares definitions using text normalization (stripping roles)
- Classifies mismatches by severity
- Checks for banned directives (`glossary-entry`, `glossary-include`)
- Supports `--phase` and `--strict` flags for progressive enforcement
- Generates JSON reports via `--report`

### `exts/ferrocene_spec_lints/glossary_migration.py`

The 67-line Sphinx extension enforces two guardrails at build time:

1. No disallowed directives in any `.rst` file
2. At Phase 3+, no `:dt:` roles remaining in `glossary.rst`

The extension is cleanly gated behind `lint_glossary_migration_phase` and `lint_glossary_migration_strict` configuration flags, defaulting to disabled (phase 0).

### `src/conf.py` Changes

Configuration is environment-variable-driven, which is appropriate for CI integration:

- `FLS_GLOSSARY_MIGRATION_PHASE` (default 0: disabled)
- `FLS_GLOSSARY_MIGRATION_STRICT` (default false)
- `FLS_GLOSSARY_MIGRATION_REPORT` (output path for JSON report)

## Reliability Summary

| Rating | Count | Description |
|--------|-------|-------------|
| **High** | 626 | Exact match or cosmetic differences only |
| **Medium** | 79 | Extended definitions, moderate divergence, or redirect-style |
| **Low** | 68 | Significantly different definitions requiring review |
| **Missing** | 3 | Glossary term has no chapter definition |
| **New Term** | 183 | Chapter-only term, not in glossary |
| **Total** | **959** | |

## Recommendations

1. **Before merge:** Review the 68 low-reliability terms and establish a policy: should chapter definitions match the glossary verbatim, or is contextual adaptation acceptable? The answer determines whether Phase 2 can safely remove glossary definitions in favor of chapter definitions.

2. **Before merge:** Add the 3 missing terms (`casting`, `namespace qualifier`, `shadowed`) or document why they are intentionally excluded.

3. **Post-merge:** Run `./tools/glossary-migration-check.py --phase 1 --strict` in CI to prevent regression.

4. **Phase 2 planning:** The 68 semantically divergent definitions must be reconciled before the glossary can be derived from chapter text. Otherwise, the migration will silently change the specification's terminology.

5. **Post-merge:** Consider whether any of the 183 chapter-only terms should be added to the glossary for completeness.
