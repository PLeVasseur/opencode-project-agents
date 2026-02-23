# Glossary migration plan (Phase 2, revised)

## Goals
- Migrate glossary terms into chapter files using `.. glossary-entry::`.
- Keep generated glossary output identical to the static glossary.
- Work in repeatable batches of 20 terms.

## Scope rules
- Only migrate terms present in `src/glossary.static.rst.inc`.
- Do not use `:propagate:` in this phase.
- When a chapter definition exists, use dual blocks:
  - `:glossary:` is copied verbatim from the glossary (including glossary `:dp:` IDs and any "See ..." lines).
  - `:chapter:` is copied verbatim from the chapter (including chapter `:dp:` IDs and existing `:t:` usage).
- When no chapter definition exists yet, migrate the term with a glossary-only block:
  - Add only `:glossary:` copied verbatim from the glossary entry.
  - Place the directive near the most relevant chapter section for the term.

## Artifacts and required helpers
- Checklist file: `$OPENCODE_CONFIG_DIR/plans/glossary-migration-checklist.md`
- Metadata map: `$OPENCODE_CONFIG_DIR/reports/glossary-migration-phase2/term-map.jsonl`
- Generated glossary output: `build/generated.glossary.rst`
- HTML verification report: `build/html-diff/html-diff.txt`
- Required term-map helper: `$OPENCODE_CONFIG_DIR/glossary-term-map.py`
  - Example (next 20 terms): `python3 $OPENCODE_CONFIG_DIR/glossary-term-map.py --checklist --count 20`
  - Example (explicit term): `python3 $OPENCODE_CONFIG_DIR/glossary-term-map.py --terms "binary literal"`
- Required directive helper: `generate-glossary-entry.py` (repo root)
  - Dual example (chapter): `python3 generate-glossary-entry.py --term "binary literal" --chapter-file src/lexical-elements.rst --chapter-dp fls_nxqncu5yq4eu`
  - Glossary-only example: `python3 generate-glossary-entry.py --term "atomic"`

## Git hygiene (OPENCODE_CONFIG_DIR)
- Files under `$OPENCODE_CONFIG_DIR/` (plans, reports, scripts) are outside the repo.
- Never `git add` or commit any `$OPENCODE_CONFIG_DIR` files.
- Commits must include only repository paths (e.g., `src/...`).

## Term-map hashing
- `glossary_text_hash` is SHA-256 of the glossary body lines for the term
  (the lines under the glossary heading, including `:dp:` and "See ..." lines),
  joined with `\n` and no trailing newline.

## Batch size and selection
- Each batch migrates 20 terms (use the next 20 unchecked items in the checklist).
- Skip any term not present in `src/glossary.static.rst.inc`.
- If a term has no chapter definition yet, migrate it with a glossary-only block and still count it toward the batch of 20.

## Directive usage guidance
- Use dual blocks (`:glossary:` + `:chapter:`) when a chapter definition exists.
- Use glossary-only blocks (`:glossary:` only) when no chapter definition exists.
- Preserve existing `:dp:` IDs in both blocks; do not change chapter IDs.
- Do not introduce new glossary text or rewrap lines; copy verbatim.
- Always use `generate-glossary-entry.py` to emit directives (it preserves required indentation, including indented blank lines).

## Matching examples (before/after)

### ABI clobber (glossary has `:dt:` + See, chapter uses `:t:`)
Before (glossary)
```rst
:dp:`fls_OVX4RFcWKfP9`
An :dt:`ABI clobber` is an argument to :t:`macro` :std:`core::arch::asm` which
indicates that the :t:`[value]s` of selected :t:`[register]s` might be
overwritten during the :t:`execution` of an :t:`assembly code block`.

:dp:`fls_pMNTKjDMCHia`
See :s:`AbiClobber`.
```

Before (chapter)
```rst
:dp:`fls_xa11ggykg0sh`
An :t:`ABI clobber` is an argument to :t:`macro` :std:`core::arch::asm` which
indicates that the :t:`[value]s` of selected :t:`[register]s` might be
overwritten during the :t:`execution` of an :t:`assembly code block`.
```

After (directive)
```rst
.. glossary-entry:: ABI clobber

   :glossary:
     :dp:`fls_OVX4RFcWKfP9`
     An :dt:`ABI clobber` is an argument to :t:`macro` :std:`core::arch::asm` which
     indicates that the :t:`[value]s` of selected :t:`[register]s` might be
     overwritten during the :t:`execution` of an :t:`assembly code block`.

     :dp:`fls_pMNTKjDMCHia`
     See :s:`AbiClobber`.
   :chapter:
     :dp:`fls_xa11ggykg0sh`
     An :t:`ABI clobber` is an argument to :t:`macro` :std:`core::arch::asm` which
     indicates that the :t:`[value]s` of selected :t:`[register]s` might be
     overwritten during the :t:`execution` of an :t:`assembly code block`.
```

### argument operand (glossary `:dt:` vs chapter `:t:`, text identical)
Before (glossary)
```rst
:dp:`fls_ljuwr88k92vp`
An :dt:`argument operand` is an :t:`operand` which is used as an argument in a
:t:`call expression` or a :t:`method call expression`.
```

Before (chapter)
```rst
:dp:`fls_jvz5z3eqxb39`
An :t:`argument operand` is an :t:`operand` which is used as an argument in a
:t:`call expression` or a :t:`method call expression`.
```

After (directive)
```rst
.. glossary-entry:: argument operand

   :glossary:
     :dp:`fls_ljuwr88k92vp`
     An :dt:`argument operand` is an :t:`operand` which is used as an argument in a
     :t:`call expression` or a :t:`method call expression`.
   :chapter:
     :dp:`fls_jvz5z3eqxb39`
     An :t:`argument operand` is an :t:`operand` which is used as an argument in a
     :t:`call expression` or a :t:`method call expression`.
```

### alignment (glossary is shorter; chapter is expanded)
Before (glossary)
```rst
:dp:`fls_c0hbatn5o8x3`
The :dt:`alignment` of a :t:`value` specifies which addresses are valid for
storing the value.
```

Before (chapter)
```rst
:dp:`fls_muxfn9soi47l`
The :t:`alignment` of a :t:`value` specifies which addresses are valid for
storing the :t:`value`. :t:`Alignment` is measured in bytes, is at least one,
and always a power of two. A :t:`value` of :t:`alignment` ``N`` is stored at an
address that is a multiple of ``N``.
```

After (directive)
```rst
.. glossary-entry:: alignment

   :glossary:
     :dp:`fls_c0hbatn5o8x3`
     The :dt:`alignment` of a :t:`value` specifies which addresses are valid for
     storing the value.
   :chapter:
     :dp:`fls_muxfn9soi47l`
     The :t:`alignment` of a :t:`value` specifies which addresses are valid for
     storing the :t:`value`. :t:`Alignment` is measured in bytes, is at least one,
     and always a power of two. A :t:`value` of :t:`alignment` ``N`` is stored at an
     address that is a multiple of ``N``.
```

### Application Binary Interface (chapter includes "or ABI")
Before (glossary)
```rst
:dp:`fls_ew4babc9467c`
:dt:`Application Binary Interface` is a set of conventions that dictate how
data and computation cross language boundaries.

:dp:`fls_8dgmmsp34lgc`
See :s:`AbiSpecification`.
```

Before (chapter)
```rst
:dp:`fls_xangrq3tfze0`
:t:`Application Binary Interface` or :t:`ABI` is a set of conventions that
dictate how data and computation cross language boundaries.
```

After (directive)
```rst
.. glossary-entry:: Application Binary Interface

   :glossary:
     :dp:`fls_ew4babc9467c`
     :dt:`Application Binary Interface` is a set of conventions that dictate how
     data and computation cross language boundaries.

     :dp:`fls_8dgmmsp34lgc`
     See :s:`AbiSpecification`.
   :chapter:
     :dp:`fls_xangrq3tfze0`
     :t:`Application Binary Interface` or :t:`ABI` is a set of conventions that
     dictate how data and computation cross language boundaries.
```

### Pattern matching (rare reverse case: glossary `:t:`, chapter `:dt:`)
Before (glossary)
```rst
:dp:`fls_y3oputy9e0sz`
:t:`Pattern matching` is the process of matching a :t:`pattern` against a :t:`value`.
```

Before (chapter)
```rst
:dp:`fls_zv73CR8rplIa`
:dt:`Pattern matching` is the process of matching a :t:`pattern` against a :t:`value`.
```

After (directive)
```rst
.. glossary-entry:: pattern matching

   :glossary:
     :dp:`fls_y3oputy9e0sz`
     :t:`Pattern matching` is the process of matching a :t:`pattern` against a :t:`value`.
   :chapter:
     :dp:`fls_zv73CR8rplIa`
     :dt:`Pattern matching` is the process of matching a :t:`pattern` against a :t:`value`.
```

### abstract data type (glossary-only; no chapter definition)
Before (glossary)
```rst
:dp:`fls_64drmro2fcfo`
An :dt:`abstract data type` is a collection of other :t:`[type]s`.
```

Before (chapter)
```rst
.. _fls_wdec78luqh5b:

Abstract Data Types
-------------------

.. _fls_szibmtfv117b:

Enum Types
~~~~~~~~~~
```

After (directive)
```rst
.. _fls_wdec78luqh5b:

Abstract Data Types
-------------------

.. glossary-entry:: abstract data type

   :glossary:
     :dp:`fls_64drmro2fcfo`
     An :dt:`abstract data type` is a collection of other :t:`[type]s`.

.. _fls_szibmtfv117b:

Enum Types
~~~~~~~~~~
```

### adjusted call operand (glossary-only; no chapter definition)
Before (glossary)
```rst
:dp:`fls_mchqbc64iu0u`
An :dt:`adjusted call operand` is a :t:`call operand` adjusted with inserted :t:`[borrow expression]s` and :t:`[dereference expression]s`.
```

Before (chapter)
```rst
:dp:`fls_7ql1c71eidg8`
A :t:`call operand` is the :t:`function` being invoked or the
:t:`tuple enum variant value` or the :t:`tuple struct value` being constructed
by a :t:`call expression`.

:dp:`fls_QpBu34U6hXn9`
A :t:`tuple struct call expression` is a :t:`call expression` where the
:t:`call operand` resolves to a :t:`tuple struct`.
```

After (directive)
```rst
:dp:`fls_7ql1c71eidg8`
A :t:`call operand` is the :t:`function` being invoked or the
:t:`tuple enum variant value` or the :t:`tuple struct value` being constructed
by a :t:`call expression`.

.. glossary-entry:: adjusted call operand

   :glossary:
     :dp:`fls_mchqbc64iu0u`
     An :dt:`adjusted call operand` is a :t:`call operand` adjusted with inserted :t:`[borrow expression]s` and :t:`[dereference expression]s`.

:dp:`fls_QpBu34U6hXn9`
A :t:`tuple struct call expression` is a :t:`call expression` where the
:t:`call operand` resolves to a :t:`tuple struct`.
```

### arithmetic operator (glossary-only; no chapter definition)
Before (glossary)
```rst
:dp:`fls_Qf7DckakqvRq`
An :dt:`arithmetic operator` is the operator of an :t:`arithmetic expression`.
```

Before (chapter)
```rst
.. rubric:: Legality Rules

.. glossary-entry:: arithmetic expression

   :glossary:
     :dp:`fls_u3z2r1fw89xo`
     An :dt:`arithmetic expression` is an :t:`expression` that computes a :t:`value`
     from two :t:`[operand]s` using arithmetic.

     :dp:`fls_in59ccg4g3we`
     See :s:`ArithmeticExpression`.
   :chapter:
     :dp:`fls_asibqpe3z95h`
     An :t:`arithmetic expression` is an :t:`expression` that computes a :t:`value`
     from two :t:`[operand]s` using arithmetic.
```

After (directive)
```rst
.. rubric:: Legality Rules

.. glossary-entry:: arithmetic operator

   :glossary:
     :dp:`fls_Qf7DckakqvRq`
     An :dt:`arithmetic operator` is the operator of an :t:`arithmetic expression`.

.. glossary-entry:: arithmetic expression

   :glossary:
     :dp:`fls_u3z2r1fw89xo`
     An :dt:`arithmetic expression` is an :t:`expression` that computes a :t:`value`
     from two :t:`[operand]s` using arithmetic.

     :dp:`fls_in59ccg4g3we`
     See :s:`ArithmeticExpression`.
   :chapter:
     :dp:`fls_asibqpe3z95h`
     An :t:`arithmetic expression` is an :t:`expression` that computes a :t:`value`
     from two :t:`[operand]s` using arithmetic.
```

### arity (glossary-only; no chapter definition)
Before (glossary)
```rst
:dp:`fls_dl2gkip00bua`
An :dt:`arity` is the number of :t:`[tuple field]s` in a :t:`tuple type`.
```

Before (chapter)
```rst
:dp:`fls_bn7wmf681ngt`
A :t:`tuple type` is a :t:`sequence type` that represents a heterogeneous list
of other :t:`[type]s`.

:dp:`fls_s9a36zsrfqew`
If the :t:`type` of a :t:`tuple field` is a :t:`dynamically-sized type`, then
the :t:`tuple field` shall be the last :t:`tuple field` in the
:s:`TupleFieldList`.
```

After (directive)
```rst
:dp:`fls_bn7wmf681ngt`
A :t:`tuple type` is a :t:`sequence type` that represents a heterogeneous list
of other :t:`[type]s`.

.. glossary-entry:: arity

   :glossary:
     :dp:`fls_dl2gkip00bua`
     An :dt:`arity` is the number of :t:`[tuple field]s` in a :t:`tuple type`.

:dp:`fls_s9a36zsrfqew`
If the :t:`type` of a :t:`tuple field` is a :t:`dynamically-sized type`, then
the :t:`tuple field` shall be the last :t:`tuple field` in the
:s:`TupleFieldList`.
```

## Per-batch workflow (repeat)
1) Select the next 20 unchecked terms that exist in `src/glossary.static.rst.inc`.
2) Insert `.. glossary-entry::` blocks using `generate-glossary-entry.py`.
3) Verify adjacent `.. syntax::` blocks (especially indentation) were not altered by the insertions.
4) Append metadata entries with `$OPENCODE_CONFIG_DIR/glossary-term-map.py` after the directives are in place.
5) Generate glossary output: `./generate-glossary.py` (writes `build/generated.glossary.rst`).
6) Compare with static baseline (must be empty):
   - `diff -u build/generated.glossary.rst src/glossary.static.rst.inc`
   - Any diff is a failure; fix the dual blocks until empty.
7) Build and verify between each batch:
- `./tools/verify-html-diff.py` (full HTML diff; expects no differences)
8) Update the checklist: mark the 20 migrated terms as complete.
9) Commit the batch (Conventional Commit message) before starting the next batch.

## Stop conditions
- If HTML diff is non-empty, resolve before proceeding to the next batch.
- If generated glossary diff is non-empty, resolve before proceeding to the next batch.
