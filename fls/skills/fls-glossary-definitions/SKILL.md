---
name: fls-glossary-definitions
description: Write high-quality, standalone FLS glossary definitions.
compatibility: opencode
---

## What I do

- Provide rules for writing glossary definitions that are scoped, discriminating, and standalone.
- Highlight common failure modes from the glossary audit (missing "See ..." lines, list lead-ins without lists, truncated text, missing scope/discriminators).
- Offer concrete do/don't examples from recent audit findings.

## When to use me

- Defining a new glossary term with :dt:.
- Revising existing glossary definitions for clarity or scope.

## Do

- State what the term is and include at least one discriminator (scope, constraints, domain).
- Make the definition stand alone without requiring a second glossary hop.
- Use one or two clear sentences; add a list only if the list is present.
- Preserve explicit legacy "See ..." cross-references when a term is intentionally alias-only/link-only.
- Keep :dt: for definitions and :t: for references; don't swap roles when defining a term.
- Keep casing and hyphenation consistent with :t: references and term headings.
- Prefer concrete, testable wording over taxonomy-only phrasing.

## Don't

- Do not drop a legacy "See ..." line when a term is intentionally alias-only/link-only.
- Do not replace an explicit cross-reference with a tautology ("ABI is an ABI") or a synonym-only rewrite.
- Do not leave dangling example/list lead-ins (e.g., "for example:" without the example).
- Do not rely solely on "X is a Y" without scope or discriminators.
- Do not leave truncated or fragmentary sentences.
- Do not change term casing or hyphenation inconsistently across references.

## Examples

Good (standalone, scoped):
- alignment: "The alignment of a value specifies which addresses are valid for storing the value... power of two..."
- data race: "A data race is a scenario where two or more threads access a shared memory location concurrently..."

Good (alias-only preserved with explicit See line):
- ABI: "For :dt:`ABI`, see :t:`Application Binary Interface`."

Bad (missing legacy See line):
- ABI clobber: missing "See :s:`AbiClobber`." cross-reference.

Bad (dangling example lead-in):
- syntactic category: "A syntactic category is a grammar symbol denoted in PascalCase, for example:" (missing the example)

## Quick checklist

- Is the definition usable without following another term?
- Does it include at least one discriminator (scope, constraint, domain, or operational property)?
- Are lists/examples complete (no dangling lead-ins)?
- If legacy included a "See ..." line, is it preserved?
- Are :dt: and :t: roles used correctly (definition vs reference)?
- Is casing/hyphenation consistent with glossary term references?
