# Glossary audit T

## Per-letter checklist
- Letter: T
- [x] Reconcile T terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate T terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for T
- [x] Update `migration-checklist.md` for all T terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint T migration`
- [x] Letter complete

## Term checklist
- [x] tail expression (tail_expression)
- [x] temporary (temporary)
- [x] terminated (terminated)
- [x] terminated macro invocation (terminated_macro_invocation)
- [x] textual macro scope (textual_macro_scope)
- [x] textual type (textual_type)
- [x] thin pointer (thin_pointer)
- [x] thin pointer type (thin_pointer_type)
- [x] token matching (token_matching)
- [x] tokens (token)
- [x] trait (trait)
- [x] trait body (trait_body)
- [x] trait bound (trait_bound)
- [x] trait implementation (trait_implementation)
- [x] trait object lifetime elision (trait_object_lifetime_elision)
- [x] trait object type (trait_object_type)
- [x] trait type (trait_type)
- [x] transparent representation (transparent_representation)
- [x] trivial predicate (trivial_predicate)
- [x] tuple (tuple)
- [x] tuple enum variant (tuple_enum_variant)
- [x] tuple enum variant value (tuple_enum_variant_value)
- [x] tuple expression (tuple_expression)
- [x] tuple field (tuple_field)
- [x] tuple initializer (tuple_initializer)
- [x] tuple pattern (tuple_pattern)
- [x] tuple struct (tuple_struct)
- [x] tuple struct call expression (tuple_struct_call_expression)
- [x] tuple struct field (tuple_struct_field)
- [x] tuple struct pattern (tuple_struct_pattern)
- [x] tuple struct type (tuple_struct_type)
- [x] tuple struct value (tuple_struct_value)
- [x] tuple type (tuple_type)
- [x] type (type)
- [x] type alias (type_alias)
- [x] type argument (type_argument)
- [x] type ascription (type_ascription)
- [x] type bound predicate (type_bound_predicate)
- [x] type cast expression (type_cast_expression)
- [x] type coercion (type_coercion)
- [x] type inference (type_inference)
- [x] type inference root (type_inference_root)
- [x] type parameter (type_parameter)
- [x] type parameter initializer (type_parameter_initializer)
- [x] type parameter type (type_parameter_type)
- [x] type path (type_path)
- [x] type path resolution (type_path_resolution)
- [x] type representation (type_representation)
- [x] type specification (type_specification)
- [x] type unification (type_unification)
- [x] type variable (type_variable)

## tail expression (tail_expression)
- placement: src/expressions.rst
- action: upgraded definition to :dt:
- rationale: Block Expressions define tail expression semantics.

## temporary (temporary)
- placement: src/values.rst
- action: upgraded definition to :dt:
- rationale: Temporaries are defined in Values legality rules.

## terminated (terminated)
- placement: src/expressions.rst
- action: confirmed existing :dt: definition
- rationale: Loop termination rules live in Expressions.

## terminated macro invocation (terminated_macro_invocation)
- placement: src/macros.rst
- action: upgraded definition to :dt:
- rationale: Macro invocation legality rules define the term.

## textual macro scope (textual_macro_scope)
- placement: src/entities-and-resolution.rst
- action: upgraded definition to :dt:
- rationale: Scope rules are defined in Entities and Resolution.

## textual type (textual_type)
- placement: src/types-and-traits.rst
- action: added definition as :dt:
- rationale: Textual type class is defined alongside char/str types.

## thin pointer (thin_pointer)
- placement: src/types-and-traits.rst
- action: added definition as :dt:
- rationale: Indirection Types define pointer categories.

## thin pointer type (thin_pointer_type)
- placement: src/types-and-traits.rst
- action: added definition as :dt:
- rationale: Indirection Types define pointer type classes.

## token matching (token_matching)
- placement: src/macros.rst
- action: upgraded definition to :dt:
- rationale: Macro Matching rules define token matching.

## tokens (token)
- placement: src/macros.rst
- action: upgraded definition to :dt:
- rationale: Macros consume tokens as a lexical subset.

## trait (trait)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Traits are defined in the Traits section.

## trait body (trait_body)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Trait syntax and structure are defined there.

## trait bound (trait_bound)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Type Bounds specify trait-bound semantics.

## trait implementation (trait_implementation)
- placement: src/implementations.rst
- action: upgraded definition to :dt:
- rationale: Implementations chapter defines trait implementations.

## trait object lifetime elision (trait_object_lifetime_elision)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Trait object lifetime elision rules live there.

## trait object type (trait_object_type)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Trait Object Types section defines the term.

## trait type (trait_type)
- placement: src/types-and-traits.rst
- action: added definition as :dt:
- rationale: Trait Types section covers impl and object trait types.

## transparent representation (transparent_representation)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Type Representation rules define representation modifiers.

## trivial predicate (trivial_predicate)
- placement: src/generics.rst
- action: upgraded definition to :dt:
- rationale: Where clause predicate rules define trivial predicates.

## tuple (tuple)
- placement: src/types-and-traits.rst
- action: added definition as :dt:
- rationale: Tuple Types define tuple values.

## tuple enum variant (tuple_enum_variant)
- placement: src/types-and-traits.rst
- action: added definition as :dt:
- rationale: Enum Types define variant forms.

## tuple enum variant value (tuple_enum_variant_value)
- placement: src/types-and-traits.rst
- action: added definition as :dt:
- rationale: Enum Types define tuple enum variant values.

## tuple expression (tuple_expression)
- placement: src/expressions.rst
- action: upgraded definition to :dt:
- rationale: Tuple Expressions define construction semantics.

## tuple field (tuple_field)
- placement: src/types-and-traits.rst
- action: added definition as :dt:
- rationale: Tuple Types define tuple fields.

## tuple initializer (tuple_initializer)
- placement: src/expressions.rst
- action: upgraded definition to :dt:
- rationale: Tuple Expressions define tuple initializers.

## tuple pattern (tuple_pattern)
- placement: src/patterns.rst
- action: upgraded definition to :dt:
- rationale: Tuple Patterns define tuple matching semantics.

## tuple struct (tuple_struct)
- placement: src/types-and-traits.rst
- action: added definition as :dt:
- rationale: Struct Types define tuple struct declarations.

## tuple struct call expression (tuple_struct_call_expression)
- placement: src/expressions.rst
- action: upgraded definition to :dt:
- rationale: Call Expressions define tuple struct and tuple enum calls.

## tuple struct field (tuple_struct_field)
- placement: src/types-and-traits.rst
- action: added definition as :dt:
- rationale: Struct Types define tuple struct fields.

## tuple struct pattern (tuple_struct_pattern)
- placement: src/patterns.rst
- action: upgraded definition to :dt:
- rationale: Tuple Struct Patterns define matching semantics.

## tuple struct type (tuple_struct_type)
- placement: src/types-and-traits.rst
- action: added definition as :dt:
- rationale: Struct Types define tuple struct types.

## tuple struct value (tuple_struct_value)
- placement: src/types-and-traits.rst
- action: added definition as :dt:
- rationale: Struct Types define tuple struct values.

## tuple type (tuple_type)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Tuple Types define tuple type semantics.

## type (type)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Types section defines the base term.

## type alias (type_alias)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Type Aliases section defines the term.

## type argument (type_argument)
- placement: src/generics.rst
- action: upgraded definition to :dt:
- rationale: Generic Arguments section defines type arguments.

## type ascription (type_ascription)
- placement: src/types-and-traits.rst
- action: added definition as :dt:
- rationale: Types section defines type ascription syntax.

## type bound predicate (type_bound_predicate)
- placement: src/generics.rst
- action: upgraded definition to :dt:
- rationale: Where clause predicates are defined in Generics.

## type cast expression (type_cast_expression)
- placement: src/expressions.rst
- action: upgraded definition to :dt:
- rationale: Type Cast Expressions define casting semantics.

## type coercion (type_coercion)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Type Coercion section defines implicit conversions.

## type inference (type_inference)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Type Inference section defines inference rules.

## type inference root (type_inference_root)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Type Inference section defines inference roots.

## type parameter (type_parameter)
- placement: src/generics.rst
- action: upgraded definition to :dt:
- rationale: Generic Parameters define type parameter semantics.

## type parameter initializer (type_parameter_initializer)
- placement: src/generics.rst
- action: upgraded definition to :dt:
- rationale: Generic Parameters define initializer defaults.

## type parameter type (type_parameter_type)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Type Parameters section defines placeholder types.

## type path (type_path)
- placement: src/entities-and-resolution.rst
- action: upgraded definition to :dt:
- rationale: Paths section defines type paths.

## type path resolution (type_path_resolution)
- placement: src/entities-and-resolution.rst
- action: upgraded definition to :dt:
- rationale: Type Path Resolution section defines the resolution rules.

## type representation (type_representation)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Type Representation section defines layout modifiers.

## type specification (type_specification)
- placement: src/types-and-traits.rst
- action: added definition as :dt:
- rationale: Types section defines type specification structure.

## type unification (type_unification)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Type Unification section defines the process.

## type variable (type_variable)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: Type Inference section defines placeholder types.
