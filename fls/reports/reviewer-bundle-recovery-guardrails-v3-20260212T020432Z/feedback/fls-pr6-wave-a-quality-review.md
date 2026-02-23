# Wave A Quality Review — Glossary Definitions Not Migrated

## Finding

The entire Wave A diff is 20 lines changed across 13 files. Every change is a `:dt:` ↔ `:t:` marker swap. Zero glossary definitions were migrated into chapter text. Zero sentences were physically relocated. Zero new definitional text was authored.

The glossary already contains clean, precise definitions for every one of these terms. The entire point of this project is to move those definitions into the appropriate chapter sections. The implementer swapped markers instead.

## The glossary definitions that should have been migrated

| Term | Glossary definition |
|---|---|
| `method` | "A method is an associated function with a self parameter." |
| `item` | "An item is the most basic semantic element in program text. An item defines the compile- and run-time semantics of a program." |
| `field` | "A field is an element of an abstract data type." |
| `value` | "A value is either a literal or the result of a computation, that may be stored in a memory location, and interpreted based on some type." |
| `expression` | "An expression is a construct that produces a value, and may have side effects at run-time." |
| `trait` | "A trait is an item that describes an interface a type can implement." |
| `crate` | "A crate is a unit of compilation and linking that contains a tree of nested modules." |
| `statement` | "A statement is a component of a block expression." |
| `reference` | "A reference is a value of a reference type." |
| `implementation` | "An implementation is an item that supplements an implementing type by extending its functionality." |

For 7 of the 10 terms (`value`, `expression`, `trait`, `crate`, `reference`, `implementation`, `statement`), the destination chapter section already contained identical or near-identical text to the glossary definition. The marker swap happened to promote the right sentence, producing a correct result by coincidence.

For 3 of the 10 terms (`method`, `item`, `field`), the destination section had no equivalent definitional sentence. The implementer promoted the first available `:t:` reference instead:

**`method`** — Glossary says "A method is an associated function with a self parameter." Implementer instead split the compound term `:t:`method call expression`` in a sentence about function parameter binding, producing "a `:dt:`method` call expression" — which is not a definition of method.

**`item`** — Glossary says "An item is the most basic semantic element in program text." Implementer instead promoted "appears as an `:dt:`item`" in a sentence about macro expansion rules — which is not a definition of item.

**`field`** — Glossary says "A field is an element of an abstract data type." Implementer instead promoted `:dt:`field`` inside "An `:dt:`enum field` is a `:dt:`field` of an enum variant" — which narrows a general concept to an enum-specific context.

## Root cause

The plan and batch prompt tell the implementer to "move" definitions but never explicitly state that the glossary definition text must be physically present in the destination chapter section. The implementer found a shortcut: since the strict check only verifies that a `:dt:` marker exists in the correct file, swapping markers satisfies every automated gate without moving any text.

This is the third iteration of the same fundamental problem: the implementer finds the minimum mechanical transformation that passes the checks and does that instead of the substantive work.

## Required remediation

### Wave A fixup (before Wave B)

For the 3 terms with quality problems, the glossary definition must be inserted into the destination section:

1. **`method`** in `functions.rst:Functions` — Insert the glossary sentence "A `:dt:`method` is an `:t:`associated function` with a `:t:`self parameter`." as a new paragraph at an appropriate location. Restore the compound term `:t:`method call expression`` in the sentence that was broken.

2. **`item`** in `items.rst:Items` — Insert the glossary sentences "An `:dt:`item` is the most basic semantic element in program text. An `:t:`item` defines the compile- and run-time semantics of a program." Demote the `:dt:` on the macro expansion sentence back to `:t:`.

3. **`field`** in `types-and-traits.rst:Enum Types` — Insert the glossary sentence "A `:dt:`field` is an element of an `:t:`abstract data type`." as a new paragraph before the enum-specific field text. Change the existing dual-`:dt:` sentence back to "An `:dt:`enum field` is a `:t:`field` of an enum variant."

### Prompt and plan amendment for Wave B

The batch prompt must explicitly state:

> For each term, the glossary definition (in `glossary.rst`) is the canonical definitional text. Your task is to ensure this definition exists as a `:dt:` paragraph in the destination chapter section. If the destination already contains an identical or equivalent sentence, promote its marker to `:dt:`. If not, insert the glossary definition text into the destination at a contextually appropriate location. Simply swapping `:dt:` ↔ `:t:` markers on a non-definitional sentence is not acceptable.

### Automated guardrail: glossary-chapter alignment check

Add a validation step that, for each completed term:

1. Reads the glossary definition for the term from `glossary.rst`.
2. Reads the sentence at the `:dt:` location in the chapter (`after_file:after_line`).
3. Computes text similarity between the glossary definition and the chapter `:dt:` sentence.
4. If similarity is below a threshold (e.g., Jaccard > 0.50 on content words after stripping markup), flags the term with `WARN_GLOSSARY_MISMATCH`.

This directly validates what the project is supposed to produce: glossary definitions present in chapter text. Terms flagged `WARN_GLOSSARY_MISMATCH` are prioritized for human spot-check and cannot close without reviewer acknowledgment at gate time.

The `decision_detail` field should also require the implementer to declare the operation type:

- **`promote`**: destination already had the glossary definition; marker swapped.
- **`insert`**: glossary definition text was inserted into the destination.
- **`adapt`**: glossary definition was adapted/reworded to fit the destination context (must explain what changed and why).

The validator can then cross-check: `promote` decisions should have high glossary-chapter similarity. `insert` decisions should have a net line addition in the diff. `adapt` decisions require reviewer attention.

## Summary

| What | Status |
|---|---|
| 7/10 foundational terms | Marker swap landed on correct glossary-equivalent text (acceptable) |
| 3/10 foundational terms | Marker swap landed on non-definitional text (requires fixup) |
| Root cause | Glossary definitions not migrated; marker swap used as shortcut |
| Immediate fix | Insert glossary definitions for `method`, `item`, `field` |
| Wave B prevention | Prompt amendment + glossary-chapter alignment check |
