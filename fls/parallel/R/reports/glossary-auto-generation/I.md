# Glossary audit I

## Per-letter checklist
- Letter: I
- [x] Reconcile I terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate I terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for I
- [x] Update `migration-checklist.md` for all I terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint I migration`
- [x] Letter complete

## Term checklist
- [x] i8 (i8)
- [x] i16 (i16)
- [x] i32 (i32)
- [x] i64 (i64)
- [x] i128 (i128)
- [x] identifier (identifier)
- [x] identifier pattern (identifier_pattern)
- [x] if expression (if_expression)
- [x] if let expression (if_let_expression)
- [x] immutable (immutable)
- [x] immutable borrow (immutable_borrow)
- [x] immutable borrow expression (immutable_borrow_expression)
- [x] immutable place expression (immutable_place_expression)
- [x] immutable place expression context (immutable_place_expression_context)
- [x] immutable raw pointer type (immutable_raw_pointer_type)
- [x] immutable reference (immutable_reference)
- [x] immutable static (immutable_static)
- [x] immutable variable (immutable_variable)
- [x] impl header lifetime elision (impl_header_lifetime_elision)
- [x] impl trait type (impl_trait_type)
- [x] implementation (implementation)
- [x] implementation body (implementation_body)
- [x] implementation coherence (implementation_coherence)
- [x] implementation conformance (implementation_conformance)
- [x] implemented trait (implemented_trait)
- [x] implementing type (implementing_type)
- [x] implicit borrow (implicit_borrow)
- [x] implicitly declared entity (implicitly_declared_entity)
- [x] implied bound (implied_bound)
- [x] in scope (in_scope)
- [x] inclusive range pattern (inclusive_range_pattern)
- [x] incomplete associated constant (incomplete_associated_constant)
- [x] incomplete associated function (incomplete_associated_function)
- [x] incomplete associated type (incomplete_associated_type)
- [x] index expression (index_expression)
- [x] indexable type (indexable_type)
- [x] indexed deconstructor (indexed_deconstructor)
- [x] indexed field selector (indexed_field_selector)
- [x] indexed initializer (indexed_initializer)
- [x] indexed operand (indexed_operand)
- [x] indexing operand (indexing_operand)
- [x] indirection type (indirection_type)
- [x] inert attribute (inert_attribute)
- [x] inferred type (inferred_type)
- [x] infinite loop (infinite_loop)
- [x] infinite loop expression (infinite_loop_expression)
- [x] inherent implementation (inherent_implementation)
- [x] initialization (initialization)
- [x] initialization expression (initialization_expression)
- [x] initialization type (initialization_type)
- [x] inline assembly (inline_assembly)
- [x] inline module (inline_module)
- [x] inner attribute (inner_attribute)
- [x] inner block doc (inner_block_doc)
- [x] inner doc comment (inner_doc_comment)
- [x] inner line doc (inner_line_doc)
- [x] input register (input_register)
- [x] input register expression (input_register_expression)
- [x] input-output register expression (input_output_register_expression)
- [x] integer literal (integer_literal)
- [x] integer suffix (integer_suffix)
- [x] integer type (integer_type)
- [x] integer type variable (integer_type_variable)
- [x] interior mutability (interior_mutability)
- [x] intermediate match arm (intermediate_match_arm)
- [x] irrefutable constant (irrefutable_constant)
- [x] irrefutable pattern (irrefutable_pattern)
- [x] isize (isize)
- [x] item (item)
- [x] item scope (item_scope)
- [x] item statement (item_statement)
- [x] iteration expression (iteration_expression)

## i8 (i8)
- Placement: `src/types-and-traits.rst` (Integer Types)
- Action: Added a :dc: definition paragraph after signed integer type ranges.
- Rationale: Legacy glossary-only definition; numeric type semantics live in Integer Types.

## i16 (i16)
- Placement: `src/types-and-traits.rst` (Integer Types)
- Action: Added a :dc: definition paragraph after signed integer type ranges.
- Rationale: Legacy glossary-only definition; numeric type semantics live in Integer Types.

## i32 (i32)
- Placement: `src/types-and-traits.rst` (Integer Types)
- Action: Added a :dc: definition paragraph after signed integer type ranges.
- Rationale: Legacy glossary-only definition; numeric type semantics live in Integer Types.

## i64 (i64)
- Placement: `src/types-and-traits.rst` (Integer Types)
- Action: Added a :dc: definition paragraph after signed integer type ranges.
- Rationale: Legacy glossary-only definition; numeric type semantics live in Integer Types.

## i128 (i128)
- Placement: `src/types-and-traits.rst` (Integer Types)
- Action: Added a :dc: definition paragraph after signed integer type ranges.
- Rationale: Legacy glossary-only definition; numeric type semantics live in Integer Types.

## identifier (identifier)
- Placement: `src/lexical-elements.rst` (Lexical Elements)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Identifier semantics are defined in the lexical rules.

## identifier pattern (identifier_pattern)
- Placement: `src/patterns.rst` (Identifier Patterns)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Pattern binding rules live in Patterns.

## if expression (if_expression)
- Placement: `src/expressions.rst` (If Expressions)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: If expression semantics are defined in Expressions.

## if let expression (if_let_expression)
- Placement: `src/expressions.rst` (If Let Expressions)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: If let semantics are defined in Expressions.

## immutable (immutable)
- Placement: `src/values.rst` (Values)
- Action: Verified existing :dt: definition; no text change needed.
- Rationale: Value mutability is defined in Values.

## immutable borrow (immutable_borrow)
- Placement: `src/ownership-and-deconstruction.rst` (Borrowing)
- Action: Upgraded the definition to :dt: in Borrowing.
- Rationale: Borrowing rules live in Ownership and Deconstruction.

## immutable borrow expression (immutable_borrow_expression)
- Placement: `src/expressions.rst` (Borrow Expression)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Borrow expression semantics live in Expressions.

## immutable place expression (immutable_place_expression)
- Placement: `src/expressions.rst` (Place Expressions)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Place expression classification is defined in Expressions.

## immutable place expression context (immutable_place_expression_context)
- Placement: `src/expressions.rst` (Place Expressions)
- Action: Added a definition paragraph after mutable place expression contexts.
- Rationale: Context classification belongs in Place Expressions.

## immutable raw pointer type (immutable_raw_pointer_type)
- Placement: `src/types-and-traits.rst` (Raw Pointer Types)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Raw pointer type semantics live in Types and Traits.

## immutable reference (immutable_reference)
- Placement: `src/ownership-and-deconstruction.rst` (References)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Reference semantics are defined in Ownership and Deconstruction.

## immutable static (immutable_static)
- Placement: `src/values.rst` (Statics)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Static semantics are defined in Values.

## immutable variable (immutable_variable)
- Placement: `src/values.rst` (Variables)
- Action: Added a definition paragraph in Variables.
- Rationale: Variable mutability belongs in Values.

## impl header lifetime elision (impl_header_lifetime_elision)
- Placement: `src/types-and-traits.rst` (Impl Header Lifetime Elision)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Lifetime elision rules are defined in Types and Traits.

## impl trait type (impl_trait_type)
- Placement: `src/types-and-traits.rst` (Impl Trait Types)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Impl trait type semantics are defined in Types and Traits.

## implementation (implementation)
- Placement: `src/implementations.rst` (Implementations)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Implementation semantics are defined in Implementations.

## implementation body (implementation_body)
- Placement: `src/implementations.rst` (Implementations)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Implementation structure is defined in Implementations.

## implementation coherence (implementation_coherence)
- Placement: `src/implementations.rst` (Implementation Coherence)
- Action: Verified existing :dt: definition; no text change needed.
- Rationale: Coherence rules are defined in Implementations.

## implementation conformance (implementation_conformance)
- Placement: `src/implementations.rst` (Implementation Conformance)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Conformance rules are defined in Implementations.

## implemented trait (implemented_trait)
- Placement: `src/implementations.rst` (Implementations)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Implemented trait semantics are defined in Implementations.

## implementing type (implementing_type)
- Placement: `src/implementations.rst` (Implementations)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Implementing type semantics are defined in Implementations.

## implicit borrow (implicit_borrow)
- Placement: `src/ownership-and-deconstruction.rst` (Borrowing)
- Action: Upgraded the definition to :dt: in Borrowing.
- Rationale: Borrowing rules live in Ownership and Deconstruction.

## implicitly declared entity (implicitly_declared_entity)
- Placement: `src/entities-and-resolution.rst` (Entities)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Entity classification is defined in Entities.

## implied bound (implied_bound)
- Placement: `src/types-and-traits.rst` (Trait Bounds)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Implied bounds are specified in Types and Traits.

## in scope (in_scope)
- Placement: `src/entities-and-resolution.rst` (Scopes)
- Action: Verified existing :dt: definition; no text change needed.
- Rationale: Scope rules are defined in Entities and Resolution.

## inclusive range pattern (inclusive_range_pattern)
- Placement: `src/patterns.rst` (Range Patterns)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Pattern range rules are defined in Patterns.

## incomplete associated constant (incomplete_associated_constant)
- Placement: `src/associated-items.rst` (Associated Items)
- Action: Added a definition paragraph near associated item definitions.
- Rationale: Associated item completeness belongs in Associated Items.

## incomplete associated function (incomplete_associated_function)
- Placement: `src/associated-items.rst` (Associated Items)
- Action: Added a definition paragraph near associated item definitions.
- Rationale: Associated item completeness belongs in Associated Items.

## incomplete associated type (incomplete_associated_type)
- Placement: `src/associated-items.rst` (Associated Items)
- Action: Added a definition paragraph near associated item definitions.
- Rationale: Associated item completeness belongs in Associated Items.

## index expression (index_expression)
- Placement: `src/expressions.rst` (Index Expressions)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Index expression semantics live in Expressions.

## indexable type (indexable_type)
- Placement: `src/expressions.rst` (Index Expressions)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Indexing requirements are defined in Expressions.

## indexed deconstructor (indexed_deconstructor)
- Placement: `src/patterns.rst` (Record Struct Patterns)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Deconstruction semantics are defined in Patterns.

## indexed field selector (indexed_field_selector)
- Placement: `src/entities-and-resolution.rst` (Field Resolution)
- Action: Added a definition paragraph in Field Resolution.
- Rationale: Field resolution owns selector semantics.

## indexed initializer (indexed_initializer)
- Placement: `src/expressions.rst` (Struct Expressions)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Struct construction semantics live in Expressions.

## indexed operand (indexed_operand)
- Placement: `src/expressions.rst` (Index Expressions)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Index operand semantics live in Expressions.

## indexing operand (indexing_operand)
- Placement: `src/expressions.rst` (Index Expressions)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Index operand semantics live in Expressions.

## indirection type (indirection_type)
- Placement: `src/types-and-traits.rst` (Indirection Types)
- Action: Added a definition paragraph in Indirection Types.
- Rationale: Indirection semantics live in Types and Traits.

## inert attribute (inert_attribute)
- Placement: `src/attributes.rst` (Attribute Properties)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Attribute behavior is defined in Attributes.

## inferred type (inferred_type)
- Placement: `src/types-and-traits.rst` (Inferred Types)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Type inference rules live in Types and Traits.

## infinite loop (infinite_loop)
- Placement: `src/expressions.rst` (Infinite Loops)
- Action: Added a definition that references infinite loop expressions.
- Rationale: Legacy glossary term is a cross-reference to the expression form.

## infinite loop expression (infinite_loop_expression)
- Placement: `src/expressions.rst` (Infinite Loops)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Loop semantics are defined in Expressions.

## inherent implementation (inherent_implementation)
- Placement: `src/implementations.rst` (Implementations)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Inherent implementation semantics are defined in Implementations.

## initialization (initialization)
- Placement: `src/values.rst` (Values)
- Action: Added a definition paragraph in Values.
- Rationale: Initialization ties constants, statics, and variables.

## initialization expression (initialization_expression)
- Placement: `src/expressions.rst` (Destructuring Assignment)
- Action: Added a definition paragraph near destructuring assignment.
- Rationale: Initialization expressions are referenced in Expressions.

## initialization type (initialization_type)
- Placement: `src/types-and-traits.rst` (Type Aliases)
- Action: Added a definition paragraph in Type Aliases.
- Rationale: Initialization type is defined by type aliases.

## inline assembly (inline_assembly)
- Placement: `src/inline-assembly.rst` (Inline Assembly)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Inline assembly semantics live in Inline Assembly.

## inline module (inline_module)
- Placement: `src/program-structure-and-compilation.rst` (Modules)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Module forms are defined in Program Structure.

## inner attribute (inner_attribute)
- Placement: `src/attributes.rst` (Attributes)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Attribute placement is defined in Attributes.

## inner block doc (inner_block_doc)
- Placement: `src/lexical-elements.rst` (Comments)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Comment classes are defined in Lexical Elements.

## inner doc comment (inner_doc_comment)
- Placement: `src/lexical-elements.rst` (Comments)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Comment classes are defined in Lexical Elements.

## inner line doc (inner_line_doc)
- Placement: `src/lexical-elements.rst` (Comments)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Comment classes are defined in Lexical Elements.

## input register (input_register)
- Placement: `src/inline-assembly.rst` (Registers)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Register roles are defined in Inline Assembly.

## input register expression (input_register_expression)
- Placement: `src/inline-assembly.rst` (Register Arguments)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Register expression semantics live in Inline Assembly.

## input-output register expression (input_output_register_expression)
- Placement: `src/inline-assembly.rst` (Register Arguments)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Register expression semantics live in Inline Assembly.

## integer literal (integer_literal)
- Placement: `src/lexical-elements.rst` (Numeric Literals)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Literal forms are defined in Lexical Elements.

## integer suffix (integer_suffix)
- Placement: `src/lexical-elements.rst` (Numeric Literals)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Literal suffixes are defined in Lexical Elements.

## integer type (integer_type)
- Placement: `src/types-and-traits.rst` (Integer Types)
- Action: Added a definition paragraph in Integer Types.
- Rationale: Numeric type categories are defined in Types and Traits.

## integer type variable (integer_type_variable)
- Placement: `src/types-and-traits.rst` (Type Inference)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Type inference variable kinds are defined in Types and Traits.

## interior mutability (interior_mutability)
- Placement: `src/types-and-traits.rst` (Interior Mutability)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Interior mutability rules are defined in Types and Traits.

## intermediate match arm (intermediate_match_arm)
- Placement: `src/expressions.rst` (Match Expressions)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Match arm roles are defined in Expressions.

## irrefutable constant (irrefutable_constant)
- Placement: `src/patterns.rst` (Refutability)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Refutability rules are defined in Patterns.

## irrefutable pattern (irrefutable_pattern)
- Placement: `src/patterns.rst` (Refutability)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Refutability rules are defined in Patterns.

## isize (isize)
- Placement: `src/types-and-traits.rst` (Integer Types)
- Action: Upgraded the definition to :dc: in Legality Rules.
- Rationale: Integer type semantics are defined in Types and Traits.

## item (item)
- Placement: `src/entities-and-resolution.rst` (Entities)
- Action: Added a definition paragraph in Entities.
- Rationale: Item semantics belong in Entities and Resolution.

## item scope (item_scope)
- Placement: `src/entities-and-resolution.rst` (Item Scope)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Scope rules are defined in Entities and Resolution.

## item statement (item_statement)
- Placement: `src/statements.rst` (Statements)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Statement forms are defined in Statements.

## iteration expression (iteration_expression)
- Placement: `src/expressions.rst` (While Loops)
- Action: Upgraded the definition to :dt: in Legality Rules.
- Rationale: Loop criteria are defined in Expressions.
