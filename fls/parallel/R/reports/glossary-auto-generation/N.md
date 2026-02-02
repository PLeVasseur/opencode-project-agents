# Glossary audit N

## Per-letter checklist
- Letter: N
- [x] Reconcile N terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate N terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for N
- [x] Update `migration-checklist.md` for all N terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint N migration`
- [x] Letter complete

## Term checklist
- [x] name (name)
- [x] named block expression (named_block_expression)
- [x] named deconstructor (named_deconstructor)
- [x] named field selector (named_field_selector)
- [x] named initializer (named_initializer)
- [x] named loop expression (named_loop_expression)
- [x] named register argument (named_register_argument)
- [x] namespace (namespace)
- [x] NaN-boxing (nan_boxing)
- [x] negation expression (negation_expression)
- [x] nesting import (nesting_import)
- [x] never type (never_type)
- [x] non-reference pattern (non_reference_pattern)
- [x] not configuration predicate (not_configuration_predicate)
- [x] not-equals expression (not_equals_expression)
- [x] null (null)
- [x] numeric literal (numeric_literal)
- [x] numeric literal pattern (numeric_literal_pattern)
- [x] numeric type (numeric_type)

## name (name)
- placement: `src/entities-and-resolution.rst`
- action: upgraded definition to `:dt:` in Entities.
- rationale: Entities section defines names used by namespace and resolution rules.

## named block expression (named_block_expression)
- placement: `src/expressions.rst`
- action: upgraded definition to `:dt:` in Named Blocks legality rules.
- rationale: Named block semantics are defined in Expressions.

## named deconstructor (named_deconstructor)
- placement: `src/patterns.rst`
- action: upgraded definition to `:dt:` in Record Struct Patterns.
- rationale: Pattern deconstruction rules live in Patterns.

## named field selector (named_field_selector)
- placement: `src/entities-and-resolution.rst`
- action: added `:dt:` definition in Field Resolution.
- rationale: Field resolution already defines indexed selectors and needs the named form.

## named initializer (named_initializer)
- placement: `src/expressions.rst`
- action: upgraded definition to `:dt:` in Struct Expressions.
- rationale: Struct expression semantics define named initializers.

## named loop expression (named_loop_expression)
- placement: `src/expressions.rst`
- action: upgraded definition to `:dt:` in Loop Expressions.
- rationale: Loop semantics define named loops.

## named register argument (named_register_argument)
- placement: `src/inline-assembly.rst`
- action: upgraded definition to `:dt:` in Register Arguments.
- rationale: Inline assembly register argument rules define the construct.

## namespace (namespace)
- placement: `src/entities-and-resolution.rst`
- action: upgraded definition to `:dt:` in Namespaces.
- rationale: Namespace segregation rules are defined there.

## NaN-boxing (nan_boxing)
- placement: `src/inline-assembly.rst`
- action: added `:dt:` definition near register size rules.
- rationale: The term is only used for inline assembly register sizing.

## negation expression (negation_expression)
- placement: `src/expressions.rst`
- action: upgraded definition to `:dt:` in Negation Expression.
- rationale: Operator semantics are defined in Expressions.

## nesting import (nesting_import)
- placement: `src/entities-and-resolution.rst`
- action: upgraded definition to `:dt:` in Use Imports.
- rationale: Import resolution rules define nesting imports.

## never type (never_type)
- placement: `src/types-and-traits.rst`
- action: upgraded definition to `:dt:` in Never Type.
- rationale: Type semantics for `!` belong in Types.

## non-reference pattern (non_reference_pattern)
- placement: `src/patterns.rst`
- action: upgraded definition to `:dt:` in Binding Modes.
- rationale: Pattern classification is defined in Patterns.

## not configuration predicate (not_configuration_predicate)
- placement: `src/attributes.rst`
- action: upgraded definition to `:dt:` in `cfg` predicate rules.
- rationale: Configuration predicate semantics live in Attributes.

## not-equals expression (not_equals_expression)
- placement: `src/expressions.rst`
- action: upgraded definition to `:dt:` in Comparison Expressions.
- rationale: Comparison expression semantics are defined there.

## null (null)
- placement: `src/values.rst`
- action: added `:dc:` definition in Values legality rules.
- rationale: Null is referenced by indirection and dangling semantics.

## numeric literal (numeric_literal)
- placement: `src/lexical-elements.rst`
- action: upgraded definition to `:dt:` in Numeric Literals.
- rationale: Literal syntax and meaning are defined in Lexical Elements.

## numeric literal pattern (numeric_literal_pattern)
- placement: `src/patterns.rst`
- action: upgraded definition to `:dt:` in Literal Patterns.
- rationale: Pattern matching rules are defined in Patterns.

## numeric type (numeric_type)
- placement: `src/types-and-traits.rst`
- action: added `:dt:` definition in Numeric Types.
- rationale: Numeric type grouping belongs in Types.
