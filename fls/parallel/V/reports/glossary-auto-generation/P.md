# Glossary audit P

## Per-letter checklist
- Letter: P
- [x] Reconcile P terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate P terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for P
- [x] Update `migration-checklist.md` for all P terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint P migration`
- [x] Letter complete

## Term checklist
- [x] panic (panic)
- [x] parenthesized expression (parenthesized_expression)
- [x] parenthesized pattern (parenthesized_pattern)
- [x] parenthesized type (parenthesized_type)
- [x] partially hygienic (partially_hygienic)
- [x] passing convention (passing_convention)
- [x] path (path)
- [x] path expression (path_expression)
- [x] path expression resolution (path_expression_resolution)
- [x] path pattern (path_pattern)
- [x] path resolution (path_resolution)
- [x] path segment (path_segment)
- [x] pattern (pattern)
- [x] pattern-without-alternation (pattern_without_alternation)
- [x] pattern-without-range (pattern_without_range)
- [x] place (place)
- [x] place expression (place_expression)
- [x] place expression context (place_expression_context)
- [x] plane (plane)
- [x] pointer (pointer)
- [x] pointer type (pointer_type)
- [x] positional register argument (positional_register_argument)
- [x] precedence (precedence)
- [x] prelude (prelude)
- [x] prelude entity (prelude_entity)
- [x] prelude name (prelude_name)
- [x] primitive representation (primitive_representation)
- [x] principal trait (principal_trait)
- [x] private visibility (private_visibility)
- [x] proc-macro crate (proc_macro_crate)
- [x] procedural macro (procedural_macro)
- [x] program entry point (program_entry_point)
- [x] public visibility (public_visibility)
- [x] punctuator (punctuator)
- [x] pure identifier (pure_identifier)

## panic (panic)
- Placement: src/exceptions-and-errors.rst
- Action: Upgraded the Panic legality rules definition to :dt:.
- Rationale: Panic semantics are defined in Exceptions and Errors.

## parenthesized expression (parenthesized_expression)
- Placement: src/expressions.rst
- Action: Upgraded the Parenthesized Expressions definition to :dt:.
- Rationale: Expression grouping semantics are defined in Expressions.

## parenthesized pattern (parenthesized_pattern)
- Placement: src/patterns.rst
- Action: Upgraded the Parenthesized Patterns definition to :dt:.
- Rationale: Pattern precedence rules live in Patterns.

## parenthesized type (parenthesized_type)
- Placement: src/types-and-traits.rst
- Action: Upgraded the Parenthesized Types definition to :dt:.
- Rationale: Type disambiguation is specified in Types and Traits.

## partially hygienic (partially_hygienic)
- Placement: src/macros.rst
- Action: Kept the existing :dt: definition in the Hygiene rules.
- Rationale: Hygiene classifications are defined in Macros.

## passing convention (passing_convention)
- Placement: src/ownership-and-deconstruction.rst
- Action: Upgraded the Passing Conventions definition to :dt:.
- Rationale: Value transfer semantics are defined in Ownership and Deconstruction.

## path (path)
- Placement: src/entities-and-resolution.rst
- Action: Upgraded the Paths definition to :dt:.
- Rationale: Path structure and resolution are defined in Entities and Resolution.

## path expression (path_expression)
- Placement: src/expressions.rst
- Action: Upgraded the Path Expressions definition to :dt:.
- Rationale: Path expressions are specified in Expressions.

## path expression resolution (path_expression_resolution)
- Placement: src/entities-and-resolution.rst
- Action: Upgraded the Path Expression Resolution definition to :dt:.
- Rationale: Resolution rules are defined in Entities and Resolution.

## path pattern (path_pattern)
- Placement: src/patterns.rst
- Action: Upgraded the Path Patterns definition to :dt:.
- Rationale: Path patterns are defined in Patterns.

## path resolution (path_resolution)
- Placement: src/entities-and-resolution.rst
- Action: Upgraded the Path Resolution definition to :dt:.
- Rationale: Resolution rules are defined in Entities and Resolution.

## path segment (path_segment)
- Placement: src/entities-and-resolution.rst
- Action: Upgraded the Path Segment definition to :dt:.
- Rationale: Path structure is defined in Entities and Resolution.

## pattern (pattern)
- Placement: src/patterns.rst
- Action: Upgraded the Patterns definition to :dt:.
- Rationale: Pattern semantics are defined in Patterns.

## pattern-without-alternation (pattern_without_alternation)
- Placement: src/patterns.rst
- Action: Upgraded the definition to :dt:.
- Rationale: Pattern grammar rules are defined in Patterns.

## pattern-without-range (pattern_without_range)
- Placement: src/patterns.rst
- Action: Upgraded the definition to :dt:.
- Rationale: Pattern grammar rules are defined in Patterns.

## place (place)
- Placement: src/expressions.rst
- Action: Added a :dt: definition before Place Expressions.
- Rationale: Place semantics are specified in Expressions.

## place expression (place_expression)
- Placement: src/expressions.rst
- Action: Upgraded the Place Expressions definition to :dt:.
- Rationale: Place expression rules are defined in Expressions.

## place expression context (place_expression_context)
- Placement: src/expressions.rst
- Action: Upgraded the Place Expression Context definition to :dt:.
- Rationale: Expression context rules are defined in Expressions.

## plane (plane)
- Placement: src/lexical-elements.rst
- Action: Kept the :dt: definition in the Character Set rules.
- Rationale: Unicode terminology is defined in Lexical Elements.

## pointer (pointer)
- Placement: src/types-and-traits.rst
- Action: Added a :dt: definition near Indirection Types.
- Rationale: Pointer values are part of the type system definitions.

## pointer type (pointer_type)
- Placement: src/types-and-traits.rst
- Action: Added a :dt: definition near Indirection Types.
- Rationale: Pointer type semantics live in Types and Traits.

## positional register argument (positional_register_argument)
- Placement: src/inline-assembly.rst
- Action: Upgraded the Register Arguments definition to :dt:.
- Rationale: Inline assembly register rules are defined in Inline Assembly.

## precedence (precedence)
- Placement: src/expressions.rst
- Action: Upgraded the Expression Precedence definition to :dt:.
- Rationale: Precedence rules are defined in Expressions.

## prelude (prelude)
- Placement: src/entities-and-resolution.rst
- Action: Upgraded the Preludes definition to :dt:.
- Rationale: Prelude semantics are defined in Entities and Resolution.

## prelude entity (prelude_entity)
- Placement: src/entities-and-resolution.rst
- Action: Added a standalone :dt: definition.
- Rationale: Prelude membership is defined in the Preludes section.

## prelude name (prelude_name)
- Placement: src/entities-and-resolution.rst
- Action: Added a standalone :dt: definition.
- Rationale: Prelude naming rules are defined in the Preludes section.

## primitive representation (primitive_representation)
- Placement: src/types-and-traits.rst
- Action: Upgraded the Primitive Representation definition to :dt:.
- Rationale: Representation rules are defined in Types and Traits.

## principal trait (principal_trait)
- Placement: src/types-and-traits.rst
- Action: Upgraded the Principal Trait definition to :dt:.
- Rationale: Trait object rules define the principal trait.

## private visibility (private_visibility)
- Placement: src/entities-and-resolution.rst
- Action: Upgraded the Private Visibility definition to :dt:.
- Rationale: Visibility rules are defined in Entities and Resolution.

## proc-macro crate (proc_macro_crate)
- Placement: src/program-structure-and-compilation.rst
- Action: Upgraded the proc-macro crate definition to :dt:.
- Rationale: Crate type semantics are defined in Program Structure and Compilation.

## procedural macro (procedural_macro)
- Placement: src/macros.rst
- Action: Upgraded the Procedural Macro definition to :dt:.
- Rationale: Macro semantics are defined in Macros.

## program entry point (program_entry_point)
- Placement: src/program-structure-and-compilation.rst
- Action: Upgraded the Program Entry Point definition to :dt:.
- Rationale: Entry point rules are defined in Program Structure and Compilation.

## public visibility (public_visibility)
- Placement: src/entities-and-resolution.rst
- Action: Upgraded the Public Visibility definition to :dt:.
- Rationale: Visibility rules are defined in Entities and Resolution.

## punctuator (punctuator)
- Placement: src/lexical-elements.rst
- Action: Added a :dt: definition before simple punctuators.
- Rationale: Punctuation is defined in Lexical Elements.

## pure identifier (pure_identifier)
- Placement: src/lexical-elements.rst
- Action: Upgraded the Pure Identifier definition to :dt:.
- Rationale: Identifier rules are defined in Lexical Elements.
