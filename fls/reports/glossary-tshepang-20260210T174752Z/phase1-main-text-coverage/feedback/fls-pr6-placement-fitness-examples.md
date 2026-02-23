# FLS PR #6 — Placement Fitness Examples by Priority

## High Priority — Strong Relocation Candidates

**`unit value`** (fitness: 0.114)
Currently defined in `types-and-traits.rst::Tuple Types` at paragraph `fls_y6c2p9k4m1ra`, sandwiched between the definition of "unit tuple" and "arity." The problem: all 9 references to `unit value` are in `expressions.rst` — block expressions, if expressions, loop expressions — and zero are in `types-and-traits.rst`. A reader encountering `:t:`unit value`` in the expressions chapter would have to jump to a completely different chapter's section on tuple types to find the definition. The recommendation is to move it into the Block Expressions section (`fls_nf65p0l0v0gr` .. `fls_elcl73psruxw`), where it first appears.

**`renaming`** (fitness: 0.178)
Defined in `program-structure-and-compilation.rst::Crate Imports` at `fls_2v7k7p4v0xra`. But 5 of its 9 references are in `entities-and-resolution.rst::Use Imports`, and its first use is in `entities-and-resolution.rst::Preludes`. It's a resolution/import concept defined in the compilation chapter — the recommendation targets Use Imports (`fls_lyw4t098sxrj` .. `fls_s86dgrdpl1w4`).

**`field`** (fitness: 0.223)
Defined in `types-and-traits.rst::Abstract Data Types` as "an element of an abstract data type." But it's referenced 93 times across the spec, with the heaviest concentration in `patterns.rst::Record Struct Patterns` (19 refs) and `expressions.rst` (38 refs). Only 27 of 93 references are even in the same file. The definition is also after the first use. This is a fundamental term whose placement in Abstract Data Types is defensible conceptually, but the reference pattern suggests patterns or expressions would serve readers better.

## Medium Priority — Questionable Fit

**`separator`** (fitness: 0.333)
Defined in `lexical-elements.rst::Lexical Elements, Separators, and Punctuation` — which sounds right from the section title, but 5 of its 6 references are in `macros.rst`, specifically Token Matching. Only 1 reference is in its own file. The section title gives a false sense of fit here; the term is a lexical concept but it's operationally a macros concept in the FLS.

**`discriminant initializer`** (fitness: 0.336)
Defined in `types-and-traits.rst::Enum Types`, but its first reference is at `expressions.rst:319` in Constant Expressions — well before the definition. The recommendation points to Constant Expressions (`fls_1ji7368ieg0b` .. `fls_tg0kya5125jt`).

**`integer type`** (fitness: 0.305)
Defined in `types-and-traits.rst::Integer Types` — which is clearly its conceptual home. But 20 of its 40 references are in `expressions.rst::Type Cast Expressions`. This is a case where the recommendation (move to expressions) is technically what the reference pattern suggests, but would be wrong — you don't define "integer type" inside "Type Cast Expressions." That's why the conceptual home analysis catches this and downgrades the recommendation.

## Low Priority (Forward Reference) — Right Place, Wrong Order

**`method`** (fitness: 0.058, adjusted to `acceptable_at_home`)
This scored the *worst* raw fitness of any term — zero references in `associated-items.rst`, first use in `expressions.rst::Method Call Expressions`, with 7 of 13 references in expressions. But `method` is definitionally an associated item; it's *"an associated function with a self parameter."* The conceptual home assessment correctly identifies that `associated-items.rst` is where this belongs. The caveat on the recommendation notes this tension: the reference pattern says "move to expressions" but the concept says "keep it here." The real issue is that the definition comes after the first use — a forward reference problem inherent to specification structure.

**`value`** (fitness: 0.075, adjusted to `acceptable_at_home`)
The most foundational term in the spec, referenced 385 times across every chapter. It's defined in `values.rst::Values`, which is exactly right. But `values.rst` comes after `expressions.rst` in chapter order, so the term is used 25 times in Type Cast Expressions alone before the reader ever reaches the definition. You can't move `value` into expressions — it'd be absurd. This is the quintessential forward-reference problem.

**`construct`** (fitness: 0.085, adjusted to `acceptable_at_home`)
Referenced 75 times, first used in `general.rst::Structure` at line 158, but defined much later in `entities-and-resolution.rst::Entities`. The spec's meta-vocabulary ("construct," "entity," "name") is inherently forward-referenced because it's used to describe everything that comes before the chapter that formally defines it.

## No Action — Good Fit

**`abi clobber`** (fitness: 0.825)
Defined in `inline-assembly.rst::ABI Clobbers` at `fls_1anqm6p7g0wd`. Section title relevance: 0.5. All references are in the same file and section. Defined before first use. High sibling coherence with other assembly terms. This is exactly where it belongs.

**`tuple pattern`** (fitness: 0.813)
Defined in `patterns.rst::Tuple Patterns`. All 10 references are in the same file. Defined before first use. Siblings include `tuple struct pattern` and other pattern types. Perfect placement.

## The Pattern

The overall pattern that emerges: terms that describe **specific constructs** (tuple patterns, ABI clobbers, specific expression types) tend to be well-placed because they naturally live in the section that describes them. Terms that describe **foundational concepts** (value, construct, method, name, field) score poorly because they're used everywhere before they're defined — but they're still in the right place conceptually. The genuine misplacements are the middle ground: terms like `unit value`, `renaming`, and `separator` that aren't foundational enough to justify forward-referencing but are placed in sections that don't use them.
