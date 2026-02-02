# Glossary audit R

## Per-letter checklist
- Letter: R
- [x] Reconcile R terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate R terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for R
- [x] Update `migration-checklist.md` for all R terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint R migration`
- [x] Letter complete

## Term checklist
- [x] range expression (range_expression)
- [x] range expression high bound (range_expression_high_bound)
- [x] range expression low bound (range_expression_low_bound)
- [x] range pattern (range_pattern)
- [x] range pattern bound (range_pattern_bound)
- [x] range pattern high bound (range_pattern_high_bound)
- [x] range pattern low bound (range_pattern_low_bound)
- [x] range-from expression (range_from_expression)
- [x] range-from-to expression (range_from_to_expression)
- [x] range-full expression (range_full_expression)
- [x] range-inclusive expression (range_inclusive_expression)
- [x] range-to expression (range_to_expression)
- [x] range-to-inclusive expression (range_to_inclusive_expression)
- [x] raw borrow expression (raw_borrow_expression)
- [x] raw byte string literal (raw_byte_string_literal)
- [x] raw c string literal (raw_c_string_literal)
- [x] raw pointer (raw_pointer)
- [x] raw pointer type (raw_pointer_type)
- [x] raw string literal (raw_string_literal)
- [x] reachable control flow path (reachable_control_flow_path)
- [x] receiver operand (receiver_operand)
- [x] receiver type (receiver_type)
- [x] record enum variant (record_enum_variant)
- [x] record struct (record_struct)
- [x] record struct field (record_struct_field)
- [x] record struct pattern (record_struct_pattern)
- [x] record struct type (record_struct_type)
- [x] record struct value (record_struct_value)
- [x] recursive type (recursive_type)
- [x] reference (reference)
- [x] reference identifier pattern (reference_identifier_pattern)
- [x] reference pattern (reference_pattern)
- [x] reference type (reference_type)
- [x] referent (referent)
- [x] refutability (refutability)
- [x] refutable constant (refutable_constant)
- [x] refutable pattern (refutable_pattern)
- [x] refutable type (refutable_type)
- [x] register (register)
- [x] register argument (register_argument)
- [x] register class (register_class)
- [x] register class argument (register_class_argument)
- [x] register class name (register_class_name)
- [x] register expression (register_expression)
- [x] register name (register_name)
- [x] register parameter (register_parameter)
- [x] register parameter modifier (register_parameter_modifier)
- [x] remainder assignment (remainder_assignment)
- [x] remainder assignment expression (remainder_assignment_expression)
- [x] remainder expression (remainder_expression)
- [x] renaming (renaming)
- [x] repeat operand (repeat_operand)
- [x] repetition operator (repetition_operator)
- [x] representation modifier (representation_modifier)
- [x] reserved keyword (reserved_keyword)
- [x] resolution (resolution)
- [x] rest pattern (rest_pattern)
- [x] return expression (return_expression)
- [x] return type (return_type)
- [x] right operand (right_operand)
- [x] rule matching (rule_matching)
- [x] rustc (rustc)

## range expression (range_expression)
- placement: `src/expressions.rst`
- action: Upgraded the definition to :dt: in Range Expressions.
- rationale: The range construction rules are defined in the Range Expressions section.

## range expression high bound (range_expression_high_bound)
- placement: `src/expressions.rst`
- action: Upgraded the definition to :dt: in Range Expressions.
- rationale: The operand role is defined alongside range expression syntax and rules.

## range expression low bound (range_expression_low_bound)
- placement: `src/expressions.rst`
- action: Upgraded the definition to :dt: in Range Expressions.
- rationale: The operand role is defined alongside range expression syntax and rules.

## range pattern (range_pattern)
- placement: `src/patterns.rst`
- action: Upgraded the definition to :dt: in Range Patterns.
- rationale: Range pattern semantics are defined in the Range Patterns section.

## range pattern bound (range_pattern_bound)
- placement: `src/patterns.rst`
- action: Upgraded the definition to :dt: in Range Patterns.
- rationale: Range pattern bounds are specified with the range pattern rules.

## range pattern high bound (range_pattern_high_bound)
- placement: `src/patterns.rst`
- action: Upgraded the definition to :dt: in Range Patterns.
- rationale: High bound semantics are defined in the range pattern legality rules.

## range pattern low bound (range_pattern_low_bound)
- placement: `src/patterns.rst`
- action: Upgraded the definition to :dt: in Range Patterns.
- rationale: Low bound semantics are defined in the range pattern legality rules.

## range-from expression (range_from_expression)
- placement: `src/expressions.rst`
- action: Upgraded the definition to :dt: in Range Expressions.
- rationale: Range-from expressions are defined in Range Expressions.

## range-from-to expression (range_from_to_expression)
- placement: `src/expressions.rst`
- action: Upgraded the definition to :dt: in Range Expressions.
- rationale: Range-from-to expressions are defined in Range Expressions.

## range-full expression (range_full_expression)
- placement: `src/expressions.rst`
- action: Verified existing :dt: definition in Range Expressions.
- rationale: Range-full expression semantics are defined in Range Expressions.

## range-inclusive expression (range_inclusive_expression)
- placement: `src/expressions.rst`
- action: Upgraded the definition to :dt: in Range Expressions.
- rationale: Range-inclusive expressions are defined in Range Expressions.

## range-to expression (range_to_expression)
- placement: `src/expressions.rst`
- action: Upgraded the definition to :dt: in Range Expressions.
- rationale: Range-to expressions are defined in Range Expressions.

## range-to-inclusive expression (range_to_inclusive_expression)
- placement: `src/expressions.rst`
- action: Upgraded the definition to :dt: in Range Expressions.
- rationale: Range-to-inclusive expressions are defined in Range Expressions.

## raw borrow expression (raw_borrow_expression)
- placement: `src/expressions.rst`
- action: Upgraded the definition to :dt: in Raw Borrow Expression.
- rationale: Raw borrow semantics are defined in the Raw Borrow Expression section.

## raw byte string literal (raw_byte_string_literal)
- placement: `src/lexical-elements.rst`
- action: Upgraded the definition to :dt: in Raw Byte String Literals.
- rationale: Raw byte string literal rules are defined in Lexical Elements.

## raw c string literal (raw_c_string_literal)
- placement: `src/lexical-elements.rst`
- action: Upgraded the definition to :dt: in Raw C String Literals.
- rationale: Raw C string literal rules are defined in Lexical Elements.

## raw pointer (raw_pointer)
- placement: `src/types-and-traits.rst`
- action: Added a :dt: definition in Raw Pointer Types.
- rationale: Raw pointer semantics are tied to raw pointer type rules.

## raw pointer type (raw_pointer_type)
- placement: `src/types-and-traits.rst`
- action: Upgraded the definition to :dt: in Raw Pointer Types.
- rationale: Raw pointer type semantics are defined in Raw Pointer Types.

## raw string literal (raw_string_literal)
- placement: `src/lexical-elements.rst`
- action: Upgraded the definition to :dt: in Raw String Literals.
- rationale: Raw string literal rules are defined in Lexical Elements.

## reachable control flow path (reachable_control_flow_path)
- placement: `src/values.rst`
- action: Added a :dt: definition in Variables.
- rationale: Reachable control flow paths are referenced in variable initialization rules.

## receiver operand (receiver_operand)
- placement: `src/expressions.rst`
- action: Upgraded the definition to :dt: in Method Call Expressions.
- rationale: Receiver operands are defined alongside method call semantics.

## receiver type (receiver_type)
- placement: `src/entities-and-resolution.rst`
- action: Verified existing :dt: definition in Method Resolution.
- rationale: Receiver type rules are defined in method resolution.

## record enum variant (record_enum_variant)
- placement: `src/types-and-traits.rst`
- action: Added a :dt: definition in Enum Types.
- rationale: Record enum variants are defined with enum variant kinds.

## record struct (record_struct)
- placement: `src/types-and-traits.rst`
- action: Added a :dt: definition in Struct Types.
- rationale: Record structs are defined with struct syntax and field lists.

## record struct field (record_struct_field)
- placement: `src/types-and-traits.rst`
- action: Added a :dt: definition in Struct Types.
- rationale: Record struct fields are defined with struct field rules.

## record struct pattern (record_struct_pattern)
- placement: `src/patterns.rst`
- action: Upgraded the definition to :dt: in Record Struct Patterns.
- rationale: Record struct pattern semantics are defined in that section.

## record struct type (record_struct_type)
- placement: `src/types-and-traits.rst`
- action: Added a :dt: definition in Struct Types.
- rationale: Record struct types are defined in the struct type rules.

## record struct value (record_struct_value)
- placement: `src/types-and-traits.rst`
- action: Added a :dt: definition in Struct Types.
- rationale: Record struct values are defined where record struct types are introduced.

## recursive type (recursive_type)
- placement: `src/types-and-traits.rst`
- action: Upgraded the definition to :dt: in Recursive Types.
- rationale: Recursive type semantics are defined in the type model.

## reference (reference)
- placement: `src/ownership-and-deconstruction.rst`
- action: Upgraded the definition to :dt: in References.
- rationale: Reference semantics are defined in the ownership rules.

## reference identifier pattern (reference_identifier_pattern)
- placement: `src/patterns.rst`
- action: Reworded and upgraded the definition to :dt: in Identifier Patterns.
- rationale: Reference identifier patterns are defined with identifier pattern rules.

## reference pattern (reference_pattern)
- placement: `src/patterns.rst`
- action: Upgraded the definition to :dt: in Reference Patterns.
- rationale: Reference pattern semantics are defined in that section.

## reference type (reference_type)
- placement: `src/types-and-traits.rst`
- action: Upgraded the definition to :dt: in Reference Types.
- rationale: Reference type semantics are defined in the type system section.

## referent (referent)
- placement: `src/ownership-and-deconstruction.rst`
- action: Upgraded the definition to :dt: in References.
- rationale: Referent semantics are defined alongside references.

## refutability (refutability)
- placement: `src/patterns.rst`
- action: Upgraded the definition to :dt: in Refutability.
- rationale: Refutability is defined with pattern matching rules.

## refutable constant (refutable_constant)
- placement: `src/patterns.rst`
- action: Upgraded the definition to :dt: in Refutability.
- rationale: Refutable constant rules are defined in the refutability section.

## refutable pattern (refutable_pattern)
- placement: `src/patterns.rst`
- action: Reworded and upgraded the definition to :dt: in Refutability.
- rationale: Refutable pattern semantics are defined with pattern matching rules.

## refutable type (refutable_type)
- placement: `src/patterns.rst`
- action: Added a :dt: definition in Refutability.
- rationale: Refutable type is needed to define refutable constants and patterns.

## register (register)
- placement: `src/inline-assembly.rst`
- action: Upgraded the definition to :dt: in Registers.
- rationale: Register semantics are defined in inline assembly.

## register argument (register_argument)
- placement: `src/inline-assembly.rst`
- action: Upgraded the definition to :dt: in Register Arguments.
- rationale: Register arguments are defined in inline assembly rules.

## register class (register_class)
- placement: `src/inline-assembly.rst`
- action: Upgraded the definition to :dt: in Register Classes.
- rationale: Register classes are defined in inline assembly rules.

## register class argument (register_class_argument)
- placement: `src/inline-assembly.rst`
- action: Upgraded the definition to :dt: in Register Arguments.
- rationale: Register class argument semantics are defined with register arguments.

## register class name (register_class_name)
- placement: `src/inline-assembly.rst`
- action: Upgraded the definition to :dt: in Register Classes.
- rationale: Register class names are defined in inline assembly rules.

## register expression (register_expression)
- placement: `src/inline-assembly.rst`
- action: Upgraded the definition to :dt: in Register Expressions.
- rationale: Register expressions are defined in inline assembly rules.

## register name (register_name)
- placement: `src/inline-assembly.rst`
- action: Upgraded the definition to :dt: in Registers.
- rationale: Register name semantics are defined with register rules.

## register parameter (register_parameter)
- placement: `src/inline-assembly.rst`
- action: Upgraded the definition to :dt: in Register Parameters.
- rationale: Register parameter syntax is defined in inline assembly.

## register parameter modifier (register_parameter_modifier)
- placement: `src/inline-assembly.rst`
- action: Upgraded the definition to :dt: in Register Parameter Modifiers.
- rationale: Register parameter modifiers are defined in inline assembly.

## remainder assignment (remainder_assignment)
- placement: `src/expressions.rst`
- action: Added a :dt: definition in Compound Assignment Expressions.
- rationale: Remainder assignment is defined with compound assignment rules.

## remainder assignment expression (remainder_assignment_expression)
- placement: `src/expressions.rst`
- action: Upgraded the definition to :dt: in Compound Assignment Expressions.
- rationale: The assignment expression semantics are defined in Expressions.

## remainder expression (remainder_expression)
- placement: `src/expressions.rst`
- action: Upgraded the definition to :dt: in Arithmetic Expressions.
- rationale: Remainder expression semantics are defined in Expressions.

## renaming (renaming)
- placement: `src/program-structure-and-compilation.rst`
- action: Added a :dt: definition in Crate Imports.
- rationale: Renaming semantics are used in crate imports and name binding rules.

## repeat operand (repeat_operand)
- placement: `src/expressions.rst`
- action: Upgraded the definition to :dt: in Array Expressions.
- rationale: Repeat operands are defined in array repetition constructor rules.

## repetition operator (repetition_operator)
- placement: `src/macros.rst`
- action: Upgraded the definition to :dt: in Macro Repetition.
- rationale: Repetition operator semantics are defined in macro repetition rules.

## representation modifier (representation_modifier)
- placement: `src/attributes.rst`
- action: Added a :dt: definition in Attribute repr rules.
- rationale: Representation modifiers are defined with repr alignment syntax.

## reserved keyword (reserved_keyword)
- placement: `src/lexical-elements.rst`
- action: Upgraded the definition to :dt: in Keywords.
- rationale: Reserved keyword semantics are part of lexical rules.

## resolution (resolution)
- placement: `src/entities-and-resolution.rst`
- action: Upgraded the definition to :dt: in Resolution.
- rationale: Resolution semantics are defined in Entities and Resolution.

## rest pattern (rest_pattern)
- placement: `src/patterns.rst`
- action: Upgraded the definition to :dt: in Rest Patterns.
- rationale: Rest pattern semantics are defined in Patterns.

## return expression (return_expression)
- placement: `src/expressions.rst`
- action: Upgraded the definition to :dt: in Return Expressions.
- rationale: Return expression semantics are defined in Expressions.

## return type (return_type)
- placement: `src/functions.rst`
- action: Upgraded the definition to :dt: in Functions.
- rationale: Return type semantics are defined in function rules.

## right operand (right_operand)
- placement: `src/expressions.rst`
- action: Upgraded the definition to :dt: in Expressions classification.
- rationale: Operand roles are defined with operator expressions.

## rule matching (rule_matching)
- placement: `src/macros.rst`
- action: Upgraded the definition to :dt: in Rule Matching.
- rationale: Rule matching semantics are defined with macro matching rules.

## rustc (rustc)
- placement: `src/general.rst`
- action: Added a :dt: definition in Scope.
- rationale: The scope section defines the compiler referenced by the specification.
