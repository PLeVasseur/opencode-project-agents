# Placement disposition

## Scope

- Source: `fls-pr6-placement-fitness.json` high/medium relocation candidates.
- Candidate count: `38` (`high=14`, `medium=24`).
- Conceptual-home filter outcome: all high/medium candidates had `conceptual_home.is_conceptual_home=false`; relocation recommendations were therefore reviewed for chapter-ownership semantics rather than accepted by reference-count alone.

## Decision totals

- `relocate-now`: `0`
- `keep-conceptual-home`: `5`
- `forward-reference-only`: `33`

## High-priority candidates

| term | current location | recommended location | decision | rationale | follow-up phase/PR |
|---|---|---|---|---|---|
| unit value | types-and-traits.rst:705 | expressions.rst / Block Expressions | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| pointer | types-and-traits.rst:1175 | expressions.rst / Type Cast Expressions | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| renaming | program-structure-and-compilation.rst:181 | entities-and-resolution.rst / Use Imports | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| field | types-and-traits.rst:733 | patterns.rst / Record Struct Patterns | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| size operand | types-and-traits.rst:581 | expressions.rst / Array Expressions | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| size | types-and-traits.rst:1694 | expressions.rst / Type Cast Expressions | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| type parameter | generics.rst:105 | expressions.rst / Arithmetic Expressions | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| arity | types-and-traits.rst:708 | patterns.rst / Tuple Struct Patterns | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| lifetime parameter | generics.rst:98 | types-and-traits.rst / Trait and Lifetime Bounds | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| alignment | types-and-traits.rst:1688 | types-and-traits.rst / Type Layout | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| initialization | values.rst:27 | ownership-and-deconstruction.rst / Initialization | keep-conceptual-home | Definition already precedes first observed use; relocation signal is reference-concentration only. | No move in PR7; keep current chapter ownership. |
| field index | types-and-traits.rst:977 | expressions.rst / Struct Expressions | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| c | ffi.rst:65 | types-and-traits.rst / Function Pointer Types | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| code point | lexical-elements.rst:34 | expressions.rst / Type Cast Expressions | keep-conceptual-home | Definition already precedes first observed use; relocation signal is reference-concentration only. | No move in PR7; keep current chapter ownership. |

## Medium-priority candidates

| term | current location | recommended location | decision | rationale | follow-up phase/PR |
|---|---|---|---|---|---|
| separator | lexical-elements.rst:189 | macros.rst / Token Matching | keep-conceptual-home | Definition already precedes first observed use; relocation signal is reference-concentration only. | No move in PR7; keep current chapter ownership. |
| discriminant initializer | types-and-traits.rst:810 | expressions.rst / Constant Expressions | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| destructor | ownership-and-deconstruction.rst:385 | values.rst / Constant Promotion | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| label | expressions.rst:3943 | expressions.rst / Named Blocks | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| constant parameter | generics.rst:84 | generics.rst / Generic Conformance | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| constant parameter initializer | generics.rst:87 | generics.rst / Generic Conformance | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| declaration | entities-and-resolution.rst:46 | entities-and-resolution.rst / Scope Hierarchy | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| discriminant | types-and-traits.rst:807 | expressions.rst / Type Cast Expressions | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| unicode | lexical-elements.rst:29 | lexical-elements.rst / Character Set | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| elaboration | items.rst:53 | values.rst / Constants | keep-conceptual-home | Definition already precedes first observed use; relocation signal is reference-concentration only. | No move in PR7; keep current chapter ownership. |
| direction modifier | inline-assembly.rst:687 | inline-assembly.rst / Registers | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| evaluation | expressions.rst:122 | expressions.rst / Comparison Expressions | keep-conceptual-home | Definition already precedes first observed use; relocation signal is reference-concentration only. | No move in PR7; keep current chapter ownership. |
| constant argument | generics.rst:388 | generics.rst / Generic Parameters | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| unhygienic | macros.rst:1106 | macros.rst / Hygiene | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| binding argument | generics.rst:374 | generics.rst / Generic Conformance | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| field list | types-and-traits.rst:922 | types-and-traits.rst / Enum Types | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| hygienic | macros.rst:1103 | macros.rst / Hygiene | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| qualified type | entities-and-resolution.rst:383 | entities-and-resolution.rst / Paths | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| associativity | expressions.rst:5083 | expressions.rst / Expression Precedence | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| fundamental | implementations.rst:167 | implementations.rst / Implementation Coherence | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| main function signature | program-structure-and-compilation.rst:266 | program-structure-and-compilation.rst / Crates | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| refutable type | patterns.rst:120 | patterns.rst / Refutability | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| structurally equal | types-and-traits.rst:2466 | patterns.rst / Path Patterns | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |
| base initializer | expressions.rst:3248 | - / - | forward-reference-only | Definition appears after first important use; keep ownership and rely on explicit term links at use sites. | PR7 keeps location; monitor for additional local link opportunities in later phases. |

## Forward-reference mitigations

- Existing first-use sites for reviewed terms already use term roles (`:t:`) in normative text; those links provide forward discoverability without relocating canonical definitions.
- No additional relocation edits were applied in PR7 for placement fitness during this remediation run.
- Follow-up path: if reviewer requests stronger local discoverability for a specific term, add targeted nearby cross-links in that owning chapter in a dedicated follow-up commit.
