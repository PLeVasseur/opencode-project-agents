# Glossary audit E

## Per-letter checklist
- Letter: E
- [x] Reconcile E terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate E terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for E
- [x] Update `migration-checklist.md` for all E terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint E migration`
- [x] Letter complete

## Term checklist
- [x] elaboration (elaboration)
- [x] element type (element_type)
- [x] elided (elided)
- [x] elided lifetime (elided_lifetime)
- [x] else expression (else_expression)
- [x] empty statement (empty_statement)
- [x] entity (entity)
- [x] enum (enum)
- [x] enum field (enum_field)
- [x] enum type (enum_type)
- [x] enum value (enum_value)
- [x] enum variant (enum_variant)
- [x] enum variant value (enum_variant_value)
- [x] equals expression (equals_expression)
- [x] error propagation expression (error_propagation_expression)
- [x] escaped character (escaped_character)
- [x] evaluation (evaluation)
- [x] evaluated (evaluated)
- [x] exclusive range pattern (exclusive_range_pattern)
- [x] execution (execution)
- [x] executed (executed)
- [x] explicit register argument (explicit_register_argument)
- [x] explicit register name (explicit_register_name)
- [x] explicitly declared entity (explicitly_declared_entity)
- [x] exported function (exported_function)
- [x] exported static (exported_static)
- [x] expression (expression)
- [x] expression statement (expression_statement)
- [x] expression-with-block (expression_with_block)
- [x] expression-without-block (expression_without_block)
- [x] external block (external_block)
- [x] external function (external_function)
- [x] external function item type (external_function_item_type)
- [x] external static (external_static)

## elaboration (elaboration)
- Placement: `src/items.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Items define declaration elaboration semantics.

## element type (element_type)
- Placement: `src/types-and-traits.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Array and slice element types are defined in Types.

## elided (elided)
- Placement: `src/types-and-traits.rst`
- Action: Added an alias entry that redirects to elided lifetime.
- Rationale: Lifetime elision rules define the elided lifetime term.

## elided lifetime (elided_lifetime)
- Placement: `src/types-and-traits.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Lifetimes section defines elided lifetimes.

## else expression (else_expression)
- Placement: `src/expressions.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: If expressions define else expression semantics.

## empty statement (empty_statement)
- Placement: `src/statements.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Statements chapter defines the empty statement form.

## entity (entity)
- Placement: `src/entities-and-resolution.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Entities and Resolution defines entity semantics.

## enum (enum)
- Placement: `src/types-and-traits.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Enum types are defined in the Types chapter.

## enum field (enum_field)
- Placement: `src/types-and-traits.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Enum fields are defined with enum variants.

## enum type (enum_type)
- Placement: `src/types-and-traits.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Enum type semantics are defined in Types.

## enum value (enum_value)
- Placement: `src/types-and-traits.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Enum values are defined in the enum section.

## enum variant (enum_variant)
- Placement: `src/types-and-traits.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Enum variants are defined in Types.

## enum variant value (enum_variant_value)
- Placement: `src/types-and-traits.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Enum variant values are defined in Types.

## equals expression (equals_expression)
- Placement: `src/expressions.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Comparison expressions define equals semantics.

## error propagation expression (error_propagation_expression)
- Placement: `src/expressions.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Error propagation rules define the `?` expression semantics.

## escaped character (escaped_character)
- Placement: `src/lexical-elements.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Lexical elements define escape sequences.

## evaluation (evaluation)
- Placement: `src/expressions.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Expressions dynamic semantics define evaluation.

## evaluated (evaluated)
- Placement: `src/expressions.rst`
- Action: Added an alias entry that redirects to evaluation.
- Rationale: Evaluation defines the canonical term.

## exclusive range pattern (exclusive_range_pattern)
- Placement: `src/patterns.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Range patterns define exclusive range patterns.

## execution (execution)
- Placement: `src/statements.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Statements dynamic semantics define execution.

## executed (executed)
- Placement: `src/statements.rst`
- Action: Added an alias entry that redirects to execution.
- Rationale: Execution defines the canonical term.

## explicit register argument (explicit_register_argument)
- Placement: `src/inline-assembly.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Inline assembly register arguments define explicit register arguments.

## explicit register name (explicit_register_name)
- Placement: `src/inline-assembly.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Inline assembly registers define explicit register names.

## explicitly declared entity (explicitly_declared_entity)
- Placement: `src/entities-and-resolution.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Entities chapter defines declared entities.

## exported function (exported_function)
- Placement: `src/attributes.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Attribute rules define exported functions.

## exported static (exported_static)
- Placement: `src/attributes.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Attribute rules define exported statics.

## expression (expression)
- Placement: `src/expressions.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Expressions chapter defines expression semantics.

## expression statement (expression_statement)
- Placement: `src/statements.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Statements chapter defines expression statements.

## expression-with-block (expression_with_block)
- Placement: `src/expressions.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Expression classification defines expressions with blocks.

## expression-without-block (expression_without_block)
- Placement: `src/expressions.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Expression classification defines expressions without blocks.

## external block (external_block)
- Placement: `src/ffi.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: FFI chapter defines external blocks.

## external function (external_function)
- Placement: `src/ffi.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: FFI chapter defines external functions.

## external function item type (external_function_item_type)
- Placement: `src/types-and-traits.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Types chapter defines function item types.

## external static (external_static)
- Placement: `src/ffi.rst`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: FFI chapter defines external statics.
