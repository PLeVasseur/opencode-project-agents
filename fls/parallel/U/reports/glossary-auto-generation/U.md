# Glossary audit U

## Per-letter checklist
- Letter: U
- [x] Reconcile U terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate U terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for U
- [x] Update `migration-checklist.md` for all U terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint U migration`
- [x] Letter complete

## Term checklist
- [x] u8 (u8)
- [x] u16 (u16)
- [x] u32 (u32)
- [x] u64 (u64)
- [x] u128 (u128)
- [x] unary operator (unary_operator)
- [x] undefined behavior (undefined_behavior)
- [x] under resolution (under_resolution)
- [x] underscore expression (underscore_expression)
- [x] underscore pattern (underscore_pattern)
- [x] unhygienic (unhygienic)
- [x] Unicode (unicode)
- [x] unifiable (unifiable)
- [x] unifiable types (unifiable_type)
- [x] unified type (unified_type)
- [x] unify (unify)
- [x] union (union)
- [x] union field (union_field)
- [x] union type (union_type)
- [x] union value (union_value)
- [x] unique immutable reference (unique_immutable_reference)
- [x] unit enum variant (unit_enum_variant)
- [x] unit struct (unit_struct)
- [x] unit struct constant (unit_struct_constant)
- [x] unit struct type (unit_struct_type)
- [x] unit struct value (unit_struct_value)
- [x] unit tuple (unit_tuple)
- [x] unit type (unit_type)
- [x] unit value (unit_value)
- [x] unnamed constant (unnamed_constant)
- [x] unnamed lifetime (unnamed_lifetime)
- [x] unqualified path expression (unqualified_path_expression)
- [x] unsafe block (unsafe_block)
- [x] unsafe block expression (unsafe_block_expression)
- [x] unsafe context (unsafe_context)
- [x] unsafe external block (unsafe_external_block)
- [x] unsafe function (unsafe_function)
- [x] unsafe function item type (unsafe_function_item_type)
- [x] unsafe function pointer type (unsafe_function_pointer_type)
- [x] unsafe operation (unsafe_operation)
- [x] unsafe Rust (unsafe_rust)
- [x] unsafe trait (unsafe_trait)
- [x] unsafe trait implementation (unsafe_trait_implementation)
- [x] unsafety (unsafety)
- [x] unsigned integer type (unsigned_integer_type)
- [x] unsized coercion (unsized_coercion)
- [x] unsized type (unsized_type)
- [x] unsuffixed float (unsuffixed_float)
- [x] unsuffixed integer (unsuffixed_integer)
- [x] use capture (use_capture)
- [x] use import (use_import)
- [x] usize (usize)

## u8 (u8)
- placement: src/types-and-traits.rst
- action: added :dc: definition in Integer Types
- rationale: unsigned integer ranges are specified there

## u16 (u16)
- placement: src/types-and-traits.rst
- action: added :dc: definition in Integer Types
- rationale: unsigned integer ranges are specified there

## u32 (u32)
- placement: src/types-and-traits.rst
- action: added :dc: definition in Integer Types
- rationale: unsigned integer ranges are specified there

## u64 (u64)
- placement: src/types-and-traits.rst
- action: added :dc: definition in Integer Types
- rationale: unsigned integer ranges are specified there

## u128 (u128)
- placement: src/types-and-traits.rst
- action: added :dc: definition in Integer Types
- rationale: unsigned integer ranges are specified there

## unary operator (unary_operator)
- placement: src/expressions.rst
- action: added :dt: definition near operator classification
- rationale: operator classification is defined there

## undefined behavior (undefined_behavior)
- placement: src/unsafety.rst
- action: added :dt: definition in Unsafety
- rationale: unsafety section grounds UB references

## under resolution (under_resolution)
- placement: src/entities-and-resolution.rst
- action: verified existing :dt: definition
- rationale: resolution semantics are defined there

## underscore expression (underscore_expression)
- placement: src/expressions.rst
- action: upgraded definition to :dt:
- rationale: underscore expressions are defined there

## underscore pattern (underscore_pattern)
- placement: src/patterns.rst
- action: upgraded definition to :dt:
- rationale: underscore patterns are defined there

## unhygienic (unhygienic)
- placement: src/macros.rst
- action: verified existing :dt: definition
- rationale: hygiene rules are defined there

## Unicode (unicode)
- placement: src/lexical-elements.rst
- action: added :dt: definition in Character Set
- rationale: Unicode terminology is defined in lexical elements

## unifiable (unifiable)
- placement: src/types-and-traits.rst
- action: added :dt: definition in Type Unification
- rationale: unification rules define unifiability

## unifiable types (unifiable_type)
- placement: src/types-and-traits.rst
- action: verified existing :dt: definition
- rationale: type unification defines unifiable types

## unified type (unified_type)
- placement: src/types-and-traits.rst
- action: added :dt: definition in Type Unification
- rationale: unified types are produced by type unification

## unify (unify)
- placement: src/types-and-traits.rst
- action: verified existing :dt: definition
- rationale: type unification defines unify

## union (union)
- placement: src/types-and-traits.rst
- action: added :dt: definition in Union Types
- rationale: union declarations are defined there

## union field (union_field)
- placement: src/types-and-traits.rst
- action: added :dt: definition in Union Types
- rationale: union field rules are defined there

## union type (union_type)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: union type semantics are defined there

## union value (union_value)
- placement: src/types-and-traits.rst
- action: added :dt: definition in Union Types
- rationale: union values are defined alongside union types

## unique immutable reference (unique_immutable_reference)
- placement: src/expressions.rst
- action: added :dt: definition in Capturing
- rationale: capture modes describe unique immutable references

## unit enum variant (unit_enum_variant)
- placement: src/types-and-traits.rst
- action: added :dt: definition in Enum Types
- rationale: enum variants are specified there

## unit struct (unit_struct)
- placement: src/types-and-traits.rst
- action: added :dt: definition in Struct Types
- rationale: struct forms are defined there

## unit struct constant (unit_struct_constant)
- placement: src/types-and-traits.rst
- action: added :dt: definition in Struct Types
- rationale: unit structs define an implicit constant

## unit struct type (unit_struct_type)
- placement: src/types-and-traits.rst
- action: added :dt: definition in Struct Types
- rationale: struct types are defined there

## unit struct value (unit_struct_value)
- placement: src/types-and-traits.rst
- action: added :dt: definition in Struct Types
- rationale: struct values are defined there

## unit tuple (unit_tuple)
- placement: src/types-and-traits.rst
- action: added :dt: definition in Tuple Types
- rationale: tuple forms are defined there

## unit type (unit_type)
- placement: src/types-and-traits.rst
- action: added :dt: definition in Tuple Types
- rationale: unit type is the zero-arity tuple type

## unit value (unit_value)
- placement: src/types-and-traits.rst
- action: added :dt: definition in Tuple Types
- rationale: unit value is the value of the unit type

## unnamed constant (unnamed_constant)
- placement: src/values.rst
- action: upgraded definition to :dt:
- rationale: constants are defined in Values

## unnamed lifetime (unnamed_lifetime)
- placement: src/types-and-traits.rst
- action: added :dt: definition in Lifetime Elision
- rationale: lifetime elision rules define unnamed lifetimes

## unqualified path expression (unqualified_path_expression)
- placement: src/entities-and-resolution.rst
- action: upgraded definition to :dt:
- rationale: path expression resolution is defined there

## unsafe block (unsafe_block)
- placement: src/expressions.rst
- action: added :dt: definition in Unsafe Blocks
- rationale: unsafe blocks are expression constructs

## unsafe block expression (unsafe_block_expression)
- placement: src/expressions.rst
- action: upgraded definition to :dt:
- rationale: unsafe block expression rules are defined there

## unsafe context (unsafe_context)
- placement: src/unsafety.rst
- action: upgraded definition to :dt:
- rationale: unsafety section defines contexts

## unsafe external block (unsafe_external_block)
- placement: src/ffi.rst
- action: upgraded definition to :dt:
- rationale: external block rules are defined there

## unsafe function (unsafe_function)
- placement: src/functions.rst
- action: upgraded definition to :dt:
- rationale: function safety rules are defined there

## unsafe function item type (unsafe_function_item_type)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: function item type rules are defined there

## unsafe function pointer type (unsafe_function_pointer_type)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: function pointer type rules are defined there

## unsafe operation (unsafe_operation)
- placement: src/unsafety.rst
- action: upgraded definition to :dt:
- rationale: unsafety section defines unsafe operations

## unsafe Rust (unsafe_rust)
- placement: src/unsafety.rst
- action: added :dt: cross-reference definition
- rationale: unsafe Rust is defined in terms of unsafe operations

## unsafe trait (unsafe_trait)
- placement: src/types-and-traits.rst
- action: added :dt: definition in Traits
- rationale: trait declarations are defined there

## unsafe trait implementation (unsafe_trait_implementation)
- placement: src/implementations.rst
- action: upgraded definition to :dt:
- rationale: implementation rules are defined there

## unsafety (unsafety)
- placement: src/unsafety.rst
- action: upgraded definition to :dt:
- rationale: unsafety is defined there

## unsigned integer type (unsigned_integer_type)
- placement: src/types-and-traits.rst
- action: added :dt: definition in Integer Types
- rationale: integer type rules are defined there

## unsized coercion (unsized_coercion)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: type coercion rules are defined there

## unsized type (unsized_type)
- placement: src/types-and-traits.rst
- action: added :dt: definition in Type Layout
- rationale: sized and unsized definitions live there

## unsuffixed float (unsuffixed_float)
- placement: src/lexical-elements.rst
- action: upgraded definition to :dt:
- rationale: float literal rules are defined there

## unsuffixed integer (unsuffixed_integer)
- placement: src/lexical-elements.rst
- action: upgraded definition to :dt:
- rationale: integer literal rules are defined there

## use capture (use_capture)
- placement: src/types-and-traits.rst
- action: upgraded definition to :dt:
- rationale: impl trait rules define use captures

## use import (use_import)
- placement: src/entities-and-resolution.rst
- action: upgraded definition to :dt:
- rationale: use import rules are defined there

## usize (usize)
- placement: src/types-and-traits.rst
- action: added :dc: definition in Integer Types
- rationale: unsigned integer ranges are specified there
