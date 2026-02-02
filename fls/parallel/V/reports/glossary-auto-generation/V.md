# Glossary audit V

## Per-letter checklist
- Letter: V
- [x] Reconcile V terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate V terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for V
- [x] Update `migration-checklist.md` for all V terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint V migration`
- [x] Letter complete

## Term checklist
- [x] validity invariant (validity_invariant)
- [x] value (value)
- [x] value expression (value_expression)
- [x] value expression context (value_expression_context)
- [x] value operand (value_operand)
- [x] variable (variable)
- [x] variadic part (variadic_part)
- [x] variance (variance)
- [x] visibility (visibility)
- [x] visibility modifier (visibility_modifier)
- [x] visible emptiness (visible_emptiness)
- [x] visible empty enum variant (visible_empty_enum_variant)
- [x] visible empty type (visible_empty_type)

## validity invariant (validity_invariant)
- placement: src/unsafety.rst
- action: added :dt: definition near safety invariant
- rationale: unsafety defines invariants tied to undefined behavior

## value (value)
- placement: src/values.rst
- action: upgraded definition to :dt:
- rationale: Values section defines what a value is

## value expression (value_expression)
- placement: src/expressions.rst
- action: upgraded definition to :dt:
- rationale: Value Expressions section defines the term

## value expression context (value_expression_context)
- placement: src/expressions.rst
- action: upgraded definition to :dt:
- rationale: Expression context rules are defined in Expressions

## value operand (value_operand)
- placement: src/expressions.rst
- action: upgraded definition to :dt:
- rationale: Assignment Expressions define operands

## variable (variable)
- placement: src/values.rst
- action: upgraded definition to :dt:
- rationale: Variables are defined in Values

## variadic part (variadic_part)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Function pointer type syntax and rules live in Types and Traits

## variance (variance)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Subtyping and Variance defines the concept

## visibility (visibility)
- placement: src/entities-and-resolution.rst
- action: upgraded definition to :dt:
- rationale: Visibility rules live in Entities and Resolution

## visibility modifier (visibility_modifier)
- placement: src/entities-and-resolution.rst
- action: upgraded definition to :dt:
- rationale: Visibility modifiers are defined in Visibility

## visible emptiness (visible_emptiness)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Visible Emptiness section defines the property

## visible empty enum variant (visible_empty_enum_variant)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Defined alongside visible emptiness rules

## visible empty type (visible_empty_type)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Defined alongside visible emptiness rules
