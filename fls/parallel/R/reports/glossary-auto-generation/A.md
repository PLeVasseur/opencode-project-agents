# Glossary audit A

## Per-letter checklist
- Letter: A
- [x] Reconcile A terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate A terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for A
- [x] Update `migration-checklist.md` for all A terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint A migration`
- [x] Letter complete

## Term checklist
- [x] ABI (abi)
- [x] ABI clobber (abi_clobber)
- [x] ABI kind (abi_kind)
- [x] abort (abort)
- [x] abstract data type (abstract_data_type)
- [x] active attribute (active_attribute)
- [x] addition assignment (addition_assignment)
- [x] addition assignment expression (addition_assignment_expression)
- [x] addition expression (addition_expression)
- [x] adjusted call operand (adjusted_call_operand)
- [x] alignment (alignment)
- [x] all configuration predicate (all_configuration_predicate)
- [x] anonymous loop expression (anonymous_loop_expression)
- [x] anonymous return type (anonymous_return_type)
- [x] anonymous type parameter (anonymous_type_parameter)
- [x] any configuration predicate (any_configuration_predicate)
- [x] Application Binary Interface (application_binary_interface)
- [x] argument operand (argument_operand)
- [x] arithmetic expression (arithmetic_expression)
- [x] arithmetic operator (arithmetic_operator)
- [x] arithmetic overflow (arithmetic_overflow)
- [x] arity (arity)
- [x] array (array)
- [x] array element constructor (array_element_constructor)
- [x] array expression (array_expression)
- [x] array repetition constructor (array_repetition_constructor)
- [x] array type (array_type)
- [x] assembly code block (assembly_code_block)
- [x] assembly directive (assembly_directive)
- [x] assembly instruction (assembly_instruction)
- [x] assembly option (assembly_option)
- [x] assigned operand (assigned_operand)
- [x] assignee expression (assignee_expression)
- [x] assignee operand (assignee_operand)
- [x] assignment expression (assignment_expression)
- [x] associated constant (associated_constant)
- [x] associated function (associated_function)
- [x] associated implementation constant (associated_implementation_constant)
- [x] associated implementation function (associated_implementation_function)
- [x] associated implementation type (associated_implementation_type)
- [x] associated item (associated_item)
- [x] associated trait constant (associated_trait_constant)
- [x] associated trait function (associated_trait_function)
- [x] associated trait implementation function (associated_trait_implementation_function)
- [x] associated trait implementation item (associated_trait_implementation_item)
- [x] associated trait item (associated_trait_item)
- [x] associated trait type (associated_trait_type)
- [x] associated type (associated_type)
- [x] associated type projection (associated_type_projection)
- [x] associativity (associativity)
- [x] async block (async_block)
- [x] async block expression (async_block_expression)
- [x] async closure expression (async_closure_expression)
- [x] async closure type (async_closure_type)
- [x] async control flow boundary (async_control_flow_boundary)
- [x] async function (async_function)
- [x] atomic type (atomic_type)
- [x] attribute (attribute)
- [x] attribute content (attribute_content)
- [x] attribute macro (attribute_macro)
- [x] auto trait (auto_trait)
- [x] await expression (await_expression)

## ABI (abi)
- Placement: `src/ffi.rst` :dp:`fls_q2wp45ZVk16O`
- Action: Added a dedicated `:dt:` sentence for `ABI` adjacent to the full term definition.
- Rationale: The FFI ABI section owns the normative definition for the abbreviation.

## ABI clobber (abi_clobber)
- Placement: `src/inline-assembly.rst` :dp:`fls_xa11ggykg0sh`
- Action: Upgraded the ABI clobber definition sentence to `:dt:`.
- Rationale: ABI clobbers are defined in inline assembly legality rules.

## ABI kind (abi_kind)
- Placement: `src/ffi.rst` :dp:`fls_2w0xi6rxw3uz`
- Action: Upgraded the ABI kind definition sentence to `:dt:`.
- Rationale: The FFI ABI section specifies ABI kind semantics.

## abort (abort)
- Placement: `src/exceptions-and-errors.rst` :dp:`fls_9a1izu3omkbn`
- Action: Upgraded the Abort definition sentence to `:dt:`.
- Rationale: The Abort section defines program termination semantics.

## abstract data type (abstract_data_type)
- Placement: `src/types-and-traits.rst` :dp:`fls_n9HtRM22YEv5`
- Action: Added a definition paragraph for abstract data type.
- Rationale: The Abstract Data Types section introduces enum/struct/union concepts.

## active attribute (active_attribute)
- Placement: `src/attributes.rst` :dp:`fls_p4potvq7x532`
- Action: Upgraded the active attribute definition sentence to `:dt:`.
- Rationale: Attribute Properties defines attribute categories.

## addition assignment (addition_assignment)
- Placement: `src/expressions.rst` :dp:`fls_UDyCznokIYFo`
- Action: Added a definition paragraph for addition assignment.
- Rationale: Compound assignment expressions define the `+=` operator semantics.

## addition assignment expression (addition_assignment_expression)
- Placement: `src/expressions.rst` :dp:`fls_tX1jlnTfON9X`
- Action: Added a definition paragraph for addition assignment expression.
- Rationale: Compound assignment expressions list each operator form.

## addition expression (addition_expression)
- Placement: `src/expressions.rst` :dp:`fls_kr8Opj3c7uvb`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Arithmetic expressions section defines addition.

## adjusted call operand (adjusted_call_operand)
- Placement: `src/expressions.rst` :dp:`fls_qOTBw10dW37D`
- Action: Added a definition paragraph in Call Expressions.
- Rationale: Call semantics reference adjusted call operand in invocation rules.

## alignment (alignment)
- Placement: `src/types-and-traits.rst` :dp:`fls_muxfn9soi47l`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Layout rules define alignment for values.

## all configuration predicate (all_configuration_predicate)
- Placement: `src/attributes.rst` :dp:`fls_y1MUhnKCxK6T`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Configuration predicate semantics live in the `cfg` attribute section.

## anonymous loop expression (anonymous_loop_expression)
- Placement: `src/expressions.rst` :dp:`fls_eg93m93gvwal`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Loop expression classification defines anonymous loops.

## anonymous return type (anonymous_return_type)
- Placement: `src/types-and-traits.rst` :dp:`fls_3aKZB0ILIkZw`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Impl Trait types section defines anonymous return types.

## anonymous type parameter (anonymous_type_parameter)
- Placement: `src/types-and-traits.rst` :dp:`fls_0rAmIzljJgWi`
- Action: Added a definition paragraph for anonymous type parameters.
- Rationale: Impl Trait types section defines anonymous parameters in function arguments.

## any configuration predicate (any_configuration_predicate)
- Placement: `src/attributes.rst` :dp:`fls_Rp73YEE3aFdI`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Configuration predicate semantics live in the `cfg` attribute section.

## Application Binary Interface (application_binary_interface)
- Placement: `src/ffi.rst` :dp:`fls_xangrq3tfze0`
- Action: Upgraded the full term definition to `:dt:` and kept `ABI` as a separate definition.
- Rationale: The FFI ABI section defines cross-language conventions.

## argument operand (argument_operand)
- Placement: `src/expressions.rst` :dp:`fls_jvz5z3eqxb39`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Call expressions define argument operands.

## arithmetic expression (arithmetic_expression)
- Placement: `src/expressions.rst` :dp:`fls_asibqpe3z95h`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Arithmetic expressions section defines the operator family.

## arithmetic operator (arithmetic_operator)
- Placement: `src/expressions.rst` :dp:`fls_I6ELmHXM1xv4`
- Action: Added a definition paragraph for arithmetic operators.
- Rationale: Arithmetic expressions section introduces the operator family.

## arithmetic overflow (arithmetic_overflow)
- Placement: `src/expressions.rst` :dp:`fls_oFIRXBPXu6Zv`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Arithmetic Overflow section defines overflow behavior.

## arity (arity)
- Placement: `src/types-and-traits.rst` :dp:`fls_ivWBnhfOZUrW`
- Action: Added a definition paragraph for tuple arity.
- Rationale: Tuple types own the element-count definition used elsewhere.

## array (array)
- Placement: `src/types-and-traits.rst` :dp:`fls_xmmgSHsTHDtc`
- Action: Added a definition paragraph for array values.
- Rationale: Array types section defines arrays as values of array types.

## array element constructor (array_element_constructor)
- Placement: `src/expressions.rst` :dp:`fls_fwtd3b10veiw`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Array Expressions define constructor forms.

## array expression (array_expression)
- Placement: `src/expressions.rst` :dp:`fls_ya9res33oxt6`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Array Expressions define array construction.

## array repetition constructor (array_repetition_constructor)
- Placement: `src/expressions.rst` :dp:`fls_81jf78m5uga4`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Array Expressions define repetition constructors.

## array type (array_type)
- Placement: `src/types-and-traits.rst` :dp:`fls_fx7b3qv3ghca`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Sequence types section defines array types.

## assembly code block (assembly_code_block)
- Placement: `src/inline-assembly.rst` :dp:`fls_2d05gcixjrzt`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Inline Assembly defines the structure of assembly code blocks.

## assembly directive (assembly_directive)
- Placement: `src/inline-assembly.rst` :dp:`fls_4tfod2vgz2m6`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Directive Support defines assembler directives.

## assembly instruction (assembly_instruction)
- Placement: `src/inline-assembly.rst` :dp:`fls_4jr7eg6e0g4w`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Inline assembly syntax defines instruction strings.

## assembly option (assembly_option)
- Placement: `src/inline-assembly.rst` :dp:`fls_i21l6t3vn95t`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Assembly options specify block characteristics.

## assigned operand (assigned_operand)
- Placement: `src/expressions.rst` :dp:`fls_dvy201zd6oym`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Compound assignment expressions define assigned operands.

## assignee expression (assignee_expression)
- Placement: `src/expressions.rst` :dp:`fls_oqj7s9fi3j3j`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Expression classification defines assignee expressions.

## assignee operand (assignee_operand)
- Placement: `src/expressions.rst` :dp:`fls_bsjw6f4a3wol`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Assignment expressions define assignee operands.

## assignment expression (assignment_expression)
- Placement: `src/expressions.rst` :dp:`fls_nhgexeu2h6wi`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Assignment Expressions define assignment semantics.

## associated constant (associated_constant)
- Placement: `src/associated-items.rst` :dp:`fls_5y6ae0xqux57`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Associated Items defines constants within traits and implementations.

## associated function (associated_function)
- Placement: `src/associated-items.rst` :dp:`fls_lj7492aq7fzo`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Associated Items defines functions within traits and implementations.

## associated implementation constant (associated_implementation_constant)
- Placement: `src/associated-items.rst` :dp:`fls_l3iwn56n1uz8`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Implementation-specific associated constants are defined in Associated Items.

## associated implementation function (associated_implementation_function)
- Placement: `src/associated-items.rst` :dp:`fls_qb5qpfe0uwk`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Implementation-specific associated functions are defined in Associated Items.

## associated implementation type (associated_implementation_type)
- Placement: `src/associated-items.rst` :dp:`fls_tw8u0cc5867l`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Implementation-specific associated types are defined in Associated Items.

## associated item (associated_item)
- Placement: `src/associated-items.rst` :dp:`fls_ckzd25qd213t`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Associated Items defines the umbrella term for trait/impl items.

## associated trait constant (associated_trait_constant)
- Placement: `src/associated-items.rst` :dp:`fls_x564isbhobym`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Associated Items defines trait-specific constants.

## associated trait function (associated_trait_function)
- Placement: `src/associated-items.rst` :dp:`fls_b6nns7oqvdpm`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Associated Items defines trait-specific functions.

## associated trait implementation function (associated_trait_implementation_function)
- Placement: `src/associated-items.rst` :dp:`fls_amWtS80fPtza`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Associated Items defines functions within trait implementations.

## associated trait implementation item (associated_trait_implementation_item)
- Placement: `src/associated-items.rst` :dp:`fls_N3cdn4lCZ2Bf`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Associated Items defines items within trait implementations.

## associated trait item (associated_trait_item)
- Placement: `src/associated-items.rst` :dp:`fls_bnTcCbDvdp94`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Associated Items defines items within traits.

## associated trait type (associated_trait_type)
- Placement: `src/associated-items.rst` :dp:`fls_yyhebj4qyk34`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Associated Items defines trait-specific associated types.

## associated type (associated_type)
- Placement: `src/associated-items.rst` :dp:`fls_8cz4rdrklaj4`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Associated Items defines type aliases within traits/implementations.

## associated type projection (associated_type_projection)
- Placement: `src/entities-and-resolution.rst` :dp:`fls_RZvIsApi4WQm`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Entities and Resolution defines qualified associated type paths.

## associativity (associativity)
- Placement: `src/expressions.rst` :dp:`fls_bezkcuwp5qol`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Expression precedence section defines associativity.

## async block (async_block)
- Placement: `src/expressions.rst` :dp:`fls_DnCb6ei84CeI`
- Action: Added a definition paragraph for async blocks.
- Rationale: Async Blocks section defines the construct in terms of async block expressions.

## async block expression (async_block_expression)
- Placement: `src/expressions.rst` :dp:`fls_hhidi5ukxo`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Async Blocks section defines async block expressions.

## async closure expression (async_closure_expression)
- Placement: `src/expressions.rst` :dp:`fls_My6pMgpeFCFg`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Closure expressions define async closures.

## async closure type (async_closure_type)
- Placement: `src/expressions.rst` :dp:`fls_7ln7IejTjdmi`
- Action: Added a definition paragraph for async closure types.
- Rationale: Async closure expressions introduce a distinct closure type.

## async control flow boundary (async_control_flow_boundary)
- Placement: `src/expressions.rst` :dp:`fls_sRfEgIkgKhlk`
- Action: Added a definition paragraph for async control flow boundaries.
- Rationale: Async constructs introduce control flow boundaries.

## async function (async_function)
- Placement: `src/functions.rst` :dp:`fls_m3jiunibqj81`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Function qualifiers define async functions.

## atomic type (atomic_type)
- Placement: `src/concurrency.rst` :dp:`fls_3pjla9s93mhd`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Atomics section defines atomic types.

## attribute (attribute)
- Placement: `src/attributes.rst` :dp:`fls_rnzxj1t0hehl`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Attributes section defines attributes.

## attribute content (attribute_content)
- Placement: `src/attributes.rst` :dp:`fls_9TMRVlQwAdTB`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Attributes section defines attribute content.

## attribute macro (attribute_macro)
- Placement: `src/macros.rst` :dp:`fls_l3epi1dqpi8o`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Attribute Macros section defines procedural attribute macros.

## auto trait (auto_trait)
- Placement: `src/types-and-traits.rst` :dp:`fls_YynbrIceKmsJ`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Auto Traits section defines automatically implemented traits.

## await expression (await_expression)
- Placement: `src/expressions.rst` :dp:`fls_sjz5s71hwm7l`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Await expression section defines awaiting futures.
