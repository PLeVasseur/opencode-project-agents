# Glossary audit S

## Per-letter checklist
- Letter: S
- [x] Reconcile S terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate S terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for S
- [x] Update `migration-checklist.md` for all S terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint S migration`
- [x] Letter complete

## Term checklist
- [x] safety invariant (safety_invariant)
- [x] scalar type (scalar_type)
- [x] scope (scope)
- [x] scope hierarchy (scope_hierarchy)
- [x] selected field (selected_field)
- [x] Self (self)
- [x] self parameter (self_parameter)
- [x] self public modifier (self_public_modifier)
- [x] Self scope (self_scope)
- [x] send type (send_type)
- [x] separator (separator)
- [x] sequence type (sequence_type)
- [x] shadowing (shadowing)
- [x] shared borrow (shared_borrow)
- [x] shared reference (shared_reference)
- [x] shared reference type (shared_reference_type)
- [x] shift left assignment (shift_left_assignment)
- [x] shift left assignment expression (shift_left_assignment_expression)
- [x] shift left expression (shift_left_expression)
- [x] shift right assignment (shift_right_assignment)
- [x] shift right assignment expression (shift_right_assignment_expression)
- [x] shift right expression (shift_right_expression)
- [x] shorthand deconstructor (shorthand_deconstructor)
- [x] shorthand initializer (shorthand_initializer)
- [x] signed integer type (signed_integer_type)
- [x] simple byte string literal (simple_byte_string_literal)
- [x] simple c string literal (simple_c_string_literal)
- [x] simple import (simple_import)
- [x] simple path (simple_path)
- [x] simple path prefix (simple_path_prefix)
- [x] simple path public modifier (simple_path_public_modifier)
- [x] simple path resolution (simple_path_resolution)
- [x] simple public modifier (simple_public_modifier)
- [x] simple register expression (simple_register_expression)
- [x] simple string literal (simple_string_literal)
- [x] single segment path (single_segment_path)
- [x] size (size)
- [x] size operand (size_operand)
- [x] sized type (sized_type)
- [x] slice (slice)
- [x] slice pattern (slice_pattern)
- [x] slice type (slice_type)
- [x] source file (source_file)
- [x] statement (statement)
- [x] static (static)
- [x] static initializer (static_initializer)
- [x] static lifetime elision (static_lifetime_elision)
- [x] str (str)
- [x] strict keyword (strict_keyword)
- [x] string literal (string_literal)
- [x] struct (struct)
- [x] struct expression (struct_expression)
- [x] struct field (struct_field)
- [x] struct pattern (struct_pattern)
- [x] struct type (struct_type)
- [x] struct value (struct_value)
- [x] subexpression (subexpression)
- [x] subject expression (subject_expression)
- [x] subject let expression (subject_let_expression)
- [x] subpattern (subpattern)
- [x] subtraction assignment (subtraction_assignment)
- [x] subtraction assignment expression (subtraction_assignment_expression)
- [x] subtraction expression (subtraction_expression)
- [x] subtrait (subtrait)
- [x] subtype (subtype)
- [x] subtyping (subtyping)
- [x] suffixed float (suffixed_float)
- [x] suffixed integer (suffixed_integer)
- [x] super public modifier (super_public_modifier)
- [x] supertrait (supertrait)
- [x] sync type (sync_type)
- [x] syntactic category (syntactic_category)

## safety invariant (safety_invariant)
- placement: src/unsafety.rst
- action: added :dt: definition
- rationale: Unsafety owns invariants tied to undefined behavior.

## scalar type (scalar_type)
- placement: src/types-and-traits.rst
- action: added :dt: definition
- rationale: Scalar Types classifies bool, char, and numeric types.

## scope (scope)
- placement: src/entities-and-resolution.rst
- action: upgraded :t: to :dt:
- rationale: Scopes section defines name visibility regions.

## scope hierarchy (scope_hierarchy)
- placement: src/entities-and-resolution.rst
- action: upgraded :t: to :dt:
- rationale: Scope Hierarchy section defines nested scope structure.

## selected field (selected_field)
- placement: src/expressions.rst
- action: upgraded :t: to :dt:
- rationale: Field access semantics define selected fields.

## Self (self)
- placement: src/types-and-traits.rst
- action: added :dt: definition
- rationale: Traits section defines the implicit Self type.

## self parameter (self_parameter)
- placement: src/functions.rst
- action: upgraded :t: to :dt:
- rationale: Functions defines self parameter syntax and meaning.

## self public modifier (self_public_modifier)
- placement: src/entities-and-resolution.rst
- action: upgraded :t: to :dt:
- rationale: Visibility Modifiers defines pub(self) behavior.

## Self scope (self_scope)
- placement: src/entities-and-resolution.rst
- action: upgraded :t: to :dt:
- rationale: Self Scope describes where Self is in scope.

## send type (send_type)
- placement: src/concurrency.rst
- action: upgraded :t: to :dt:
- rationale: Send and Sync define Send types.

## separator (separator)
- placement: src/lexical-elements.rst
- action: upgraded :t: to :dt:
- rationale: Lexical Elements defines separators between tokens.

## sequence type (sequence_type)
- placement: src/types-and-traits.rst
- action: added :dt: definition
- rationale: Sequence Types introduces the category for arrays/slices/tuples.

## shadowing (shadowing)
- placement: src/entities-and-resolution.rst
- action: added :dt: definition
- rationale: Entities section defines name hiding rules.

## shared borrow (shared_borrow)
- placement: src/ownership-and-deconstruction.rst
- action: added :dt: definition
- rationale: Borrowing section distinguishes shared borrows.

## shared reference (shared_reference)
- placement: src/ownership-and-deconstruction.rst
- action: added :dt: definition
- rationale: References section defines shared reference values.

## shared reference type (shared_reference_type)
- placement: src/types-and-traits.rst
- action: upgraded :t: to :dt:
- rationale: Reference Types defines shared references.

## shift left assignment (shift_left_assignment)
- placement: src/expressions.rst
- action: added :dt: definition
- rationale: Compound assignment section names the operator form.

## shift left assignment expression (shift_left_assignment_expression)
- placement: src/expressions.rst
- action: upgraded :t: to :dt:
- rationale: Compound assignment expressions define the operator.

## shift left expression (shift_left_expression)
- placement: src/expressions.rst
- action: upgraded :t: to :dt:
- rationale: Bit expressions define shift-left semantics.

## shift right assignment (shift_right_assignment)
- placement: src/expressions.rst
- action: added :dt: definition
- rationale: Compound assignment section names the operator form.

## shift right assignment expression (shift_right_assignment_expression)
- placement: src/expressions.rst
- action: upgraded :t: to :dt:
- rationale: Compound assignment expressions define the operator.

## shift right expression (shift_right_expression)
- placement: src/expressions.rst
- action: upgraded :t: to :dt:
- rationale: Bit expressions define shift-right semantics.

## shorthand deconstructor (shorthand_deconstructor)
- placement: src/patterns.rst
- action: upgraded :t: to :dt:
- rationale: Record Struct Patterns defines shorthand field binding.

## shorthand initializer (shorthand_initializer)
- placement: src/expressions.rst
- action: upgraded :t: to :dt:
- rationale: Struct Expressions define shorthand field initialization.

## signed integer type (signed_integer_type)
- placement: src/types-and-traits.rst
- action: added :dt: definition
- rationale: Integer Types defines signed ranges.

## simple byte string literal (simple_byte_string_literal)
- placement: src/lexical-elements.rst
- action: upgraded :t: to :dt:
- rationale: Simple Byte String Literals define the term.

## simple c string literal (simple_c_string_literal)
- placement: src/lexical-elements.rst
- action: upgraded :t: to :dt:
- rationale: Simple C String Literals define the term.

## simple import (simple_import)
- placement: src/entities-and-resolution.rst
- action: upgraded :t: to :dt:
- rationale: Use Imports defines simple import behavior.

## simple path (simple_path)
- placement: src/entities-and-resolution.rst
- action: upgraded :t: to :dt:
- rationale: Paths section defines simple paths.

## simple path prefix (simple_path_prefix)
- placement: src/entities-and-resolution.rst
- action: upgraded :t: to :dt:
- rationale: Use Imports defines simple path prefixes.

## simple path public modifier (simple_path_public_modifier)
- placement: src/entities-and-resolution.rst
- action: upgraded :t: to :dt:
- rationale: Visibility Modifiers defines pub(in ...).

## simple path resolution (simple_path_resolution)
- placement: src/entities-and-resolution.rst
- action: upgraded :t: to :dt:
- rationale: Simple Path Resolution owns the resolution rules.

## simple public modifier (simple_public_modifier)
- placement: src/entities-and-resolution.rst
- action: upgraded :t: to :dt:
- rationale: Visibility Modifiers defines pub.

## simple register expression (simple_register_expression)
- placement: src/inline-assembly.rst
- action: upgraded :t: to :dt:
- rationale: Register Expressions define simple register operands.

## simple string literal (simple_string_literal)
- placement: src/lexical-elements.rst
- action: upgraded :t: to :dt:
- rationale: Simple String Literals define the term.

## single segment path (single_segment_path)
- placement: src/entities-and-resolution.rst
- action: upgraded :t: to :dt:
- rationale: Paths section defines single segment paths.

## size (size)
- placement: src/types-and-traits.rst
- action: upgraded :t: to :dt:
- rationale: Type Layout defines size of types.

## size operand (size_operand)
- placement: src/types-and-traits.rst
- action: added :dt: definition
- rationale: Array Types defines length operands.

## sized type (sized_type)
- placement: src/types-and-traits.rst
- action: added :dt: definition
- rationale: Type Layout defines Sized types.

## slice (slice)
- placement: src/types-and-traits.rst
- action: added :dt: definition
- rationale: Slice Types defines slice values.

## slice pattern (slice_pattern)
- placement: src/patterns.rst
- action: upgraded :t: to :dt:
- rationale: Slice Patterns defines matching semantics.

## slice type (slice_type)
- placement: src/types-and-traits.rst
- action: upgraded :t: to :dt:
- rationale: Slice Types defines slice types.

## source file (source_file)
- placement: src/program-structure-and-compilation.rst
- action: upgraded :t: to :dt:
- rationale: Source Files owns file structure definitions.

## statement (statement)
- placement: src/statements.rst
- action: added :dt: definition
- rationale: Statements section defines the construct.

## static (static)
- placement: src/values.rst
- action: upgraded :t: to :dt:
- rationale: Statics section defines static values.

## static initializer (static_initializer)
- placement: src/values.rst
- action: upgraded :t: to :dt:
- rationale: Statics section defines initialization rules.

## static lifetime elision (static_lifetime_elision)
- placement: src/types-and-traits.rst
- action: upgraded :t: to :dt:
- rationale: Lifetime Elision defines elided static lifetimes.

## str (str)
- placement: src/types-and-traits.rst
- action: upgraded :t: to :dt:
- rationale: Str Type defines the str type.

## strict keyword (strict_keyword)
- placement: src/lexical-elements.rst
- action: upgraded :t: to :dt:
- rationale: Keywords section defines strict keywords.

## string literal (string_literal)
- placement: src/lexical-elements.rst
- action: upgraded :t: to :dt:
- rationale: String Literals define the term.

## struct (struct)
- placement: src/types-and-traits.rst
- action: added :dt: definition
- rationale: Struct Types owns the struct item category.

## struct expression (struct_expression)
- placement: src/expressions.rst
- action: upgraded :t: to :dt:
- rationale: Struct Expressions define construction forms.

## struct field (struct_field)
- placement: src/types-and-traits.rst
- action: added :dt: definition
- rationale: Struct Types defines field ownership.

## struct pattern (struct_pattern)
- placement: src/patterns.rst
- action: upgraded :t: to :dt:
- rationale: Struct Patterns define matching semantics.

## struct type (struct_type)
- placement: src/types-and-traits.rst
- action: upgraded :t: to :dt:
- rationale: Struct Types define product types.

## struct value (struct_value)
- placement: src/types-and-traits.rst
- action: added :dt: definition
- rationale: Struct Types define values of struct types.

## subexpression (subexpression)
- placement: src/expressions.rst
- action: added :dt: definition
- rationale: Expression classification defines nested expressions.

## subject expression (subject_expression)
- placement: src/expressions.rst
- action: upgraded :t: to :dt:
- rationale: Expression classification defines control expressions.

## subject let expression (subject_let_expression)
- placement: src/expressions.rst
- action: upgraded :t: to :dt:
- rationale: Expression classification defines let control expressions.

## subpattern (subpattern)
- placement: src/patterns.rst
- action: upgraded :t: to :dt:
- rationale: Patterns section defines nested patterns.

## subtraction assignment (subtraction_assignment)
- placement: src/expressions.rst
- action: added :dt: definition
- rationale: Compound assignment section names the operator form.

## subtraction assignment expression (subtraction_assignment_expression)
- placement: src/expressions.rst
- action: upgraded :t: to :dt:
- rationale: Compound assignment expressions define the operator.

## subtraction expression (subtraction_expression)
- placement: src/expressions.rst
- action: upgraded :t: to :dt:
- rationale: Arithmetic Expressions define subtraction semantics.

## subtrait (subtrait)
- placement: src/types-and-traits.rst
- action: upgraded :t: to :dt:
- rationale: Traits section defines supertrait relationships.

## subtype (subtype)
- placement: src/types-and-traits.rst
- action: added :dt: definition
- rationale: Subtyping requirements define substitution rules.

## subtyping (subtyping)
- placement: src/types-and-traits.rst
- action: added :dt: definition
- rationale: Subtyping requirements define the relation.

## suffixed float (suffixed_float)
- placement: src/lexical-elements.rst
- action: upgraded :t: to :dt:
- rationale: Float Literals define suffix behavior.

## suffixed integer (suffixed_integer)
- placement: src/lexical-elements.rst
- action: upgraded :t: to :dt:
- rationale: Integer Literals define suffix behavior.

## super public modifier (super_public_modifier)
- placement: src/entities-and-resolution.rst
- action: upgraded :t: to :dt:
- rationale: Visibility Modifiers define pub(super).

## supertrait (supertrait)
- placement: src/types-and-traits.rst
- action: upgraded :t: to :dt:
- rationale: Traits section defines supertrait requirements.

## sync type (sync_type)
- placement: src/concurrency.rst
- action: upgraded :t: to :dt:
- rationale: Send and Sync define Sync types.

## syntactic category (syntactic_category)
- placement: src/general.rst
- action: added :dt: definition
- rationale: General notation defines grammar categories.
