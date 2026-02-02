# Glossary-only definitions and placement

| Term | Term id | Placement | Rationale |
| --- | --- | --- | --- |
| code point | code_point | src/lexical-elements.rst | Reviewed usages in src/lexical-elements.rst (definition) and src/expressions.rst; added definition to Character Set section where Unicode terminology is normative. |
| plane | plane | src/lexical-elements.rst | Only usage in src/lexical-elements.rst; definition added alongside code point in Character Set section. |
| constrain | constrain | src/generics.rst | Reviewed uses in src/generics.rst and other chapters; upgraded the normative definition in Generics to :dt:. |
| dangling | dangling | src/values.rst | Reviewed uses in src/values.rst and src/expressions.rst; added definition in Values legality rules near indirection semantics. |
| fundamental | fundamental | src/implementations.rst | Reviewed multiple uses in Implementation Coherence; upgraded the normative definition paragraph to :dt:. |
| hygienic | hygienic | src/macros.rst | Split hygienic into its own :dt: paragraph after the hygiene list to keep one term per :dp:. |
| partially hygienic | partially_hygienic | src/macros.rst | Split partially hygienic into its own :dt: paragraph after the hygiene list to keep one term per :dp:. |
| unhygienic | unhygienic | src/macros.rst | Split unhygienic into its own :dt: paragraph after the hygiene list to keep one term per :dp:. |
| immutable | immutable | src/values.rst | Reviewed uses across values/ownership chapters; added definition near base value definition in Values. |
| mutable | mutable | src/values.rst | Reviewed uses across values/ownership chapters; added definition near base value definition in Values. |
| implementation coherence | implementation_coherence | src/implementations.rst | Reviewed Implementation Coherence section usages; upgraded the normative definition paragraph to :dt:. |
| in scope | in_scope | src/entities-and-resolution.rst | Reviewed Scopes and binding scope usages; upgraded the Scopes definition sentence to :dt:. |
| object safe | object_safe | src/types-and-traits.rst | Reviewed Trait Object Types section; added definition immediately after principal trait sentence. |
| overlap | overlap | src/values.rst | Reviewed usages in Values and Ownership; upgraded the overlap definition to :dt:. |
| structurally equal | structurally_equal | src/types-and-traits.rst | Reviewed Structural Equality section usages; upgraded the normative definition paragraph to :dt:. |
| terminated | terminated | src/expressions.rst | Reviewed loop semantics in Expressions; upgraded loop termination sentence to :dt:. |
| under resolution | under_resolution | src/entities-and-resolution.rst | Reviewed Resolution section usages; upgraded the definition sentence to :dt:. |
| unifiable types | unifiable_type | src/types-and-traits.rst | Reviewed Type Unification section usages; upgraded the unifiable types sentence to :dt:. |
| unify | unify | src/types-and-traits.rst | Reviewed Type Unification section usages; upgraded the unify definition sentence to :dt:. |
| ABI | abi | src/ffi.rst | Reviewed usages in src/ffi.rst, src/expressions.rst, src/attributes.rst, and src/inline-assembly.rst; upgraded the ABI definition in the FFI ABI section to :dt:. |
| Application Binary Interface | application_binary_interface | src/ffi.rst | Reviewed usages in src/ffi.rst and related chapters; defined the term alongside ABI in the FFI ABI section where cross-language conventions are specified. |
| ABI kind | abi_kind | src/ffi.rst | Reviewed usages in src/ffi.rst; upgraded the normative ABI kind sentence in the FFI ABI section to :dt:. |
| ABI clobber | abi_clobber | src/inline-assembly.rst | Reviewed inline assembly usages; upgraded the legality rules definition in ABI Clobbers to :dt:. |
| abort | abort | src/exceptions-and-errors.rst | Reviewed usages in src/exceptions-and-errors.rst; upgraded the Abort legality rules sentence to :dt:. |
| abstract data type | abstract_data_type | src/types-and-traits.rst | Reviewed usage across type system chapters; added a definition in Abstract Data Types before enum/struct/union specifics. |
| active attribute | active_attribute | src/attributes.rst | Reviewed Attribute Properties section; upgraded the active attribute definition to :dt:. |
| addition assignment | addition_assignment | src/expressions.rst | Added a definition paragraph for addition assignment in the compound assignment expressions section. |
| addition assignment expression | addition_assignment_expression | src/expressions.rst | Added a definition paragraph for the `+=` compound assignment form. |
| addition expression | addition_expression | src/expressions.rst | Upgraded the arithmetic expression definition for addition to :dt:. |
| adjusted call operand | adjusted_call_operand | src/expressions.rst | Added a definition in Call Expressions to describe implicit call adjustments. |
| alignment | alignment | src/types-and-traits.rst | Upgraded the value alignment definition to :dt:. |
| all configuration predicate | all_configuration_predicate | src/attributes.rst | Upgraded the predicate definition in the cfg attribute rules to :dt:. |
| anonymous loop expression | anonymous_loop_expression | src/expressions.rst | Upgraded the loop classification sentence to :dt:. |
| anonymous return type | anonymous_return_type | src/types-and-traits.rst | Upgraded the impl trait return type definition to :dt:. |
| any configuration predicate | any_configuration_predicate | src/attributes.rst | Upgraded the predicate definition in the cfg attribute rules to :dt:. |
| argument operand | argument_operand | src/expressions.rst | Upgraded the call expression argument operand definition to :dt:. |
| arithmetic expression | arithmetic_expression | src/expressions.rst | Upgraded the arithmetic expression definition to :dt:. |
| arithmetic operator | arithmetic_operator | src/expressions.rst | Added a definition for arithmetic operators in the arithmetic expressions section. |
| arithmetic overflow | arithmetic_overflow | src/expressions.rst | Upgraded the Arithmetic Overflow definition to :dt:. |
| arity | arity | src/types-and-traits.rst | Added a definition for tuple arity in Tuple Types. |
| array | array | src/types-and-traits.rst | Added a definition for array values in Array Types. |
| array element constructor | array_element_constructor | src/expressions.rst | Upgraded the array element constructor definition to :dt:. |
| array expression | array_expression | src/expressions.rst | Upgraded the array expression definition to :dt:. |
| array repetition constructor | array_repetition_constructor | src/expressions.rst | Upgraded the array repetition constructor definition to :dt:. |
| array type | array_type | src/types-and-traits.rst | Upgraded the array type definition to :dt:. |
| assembly code block | assembly_code_block | src/inline-assembly.rst | Upgraded the assembly code block definition to :dt:. |
| assembly directive | assembly_directive | src/inline-assembly.rst | Upgraded the assembly directive definition to :dt:. |
| assembly instruction | assembly_instruction | src/inline-assembly.rst | Upgraded the assembly instruction definition to :dt:. |
| assembly option | assembly_option | src/inline-assembly.rst | Upgraded the assembly option definition to :dt:. |
| async block | async_block | src/expressions.rst | Added a definition for async blocks in the Async Blocks section. |
| async block expression | async_block_expression | src/expressions.rst | Upgraded the async block expression definition to :dt:. |
| async closure expression | async_closure_expression | src/expressions.rst | Upgraded the async closure expression definition to :dt:. |
| async closure type | async_closure_type | src/expressions.rst | Added a definition for async closure types near closure expression rules. |
| async control flow boundary | async_control_flow_boundary | src/expressions.rst | Added a definition for async control flow boundaries alongside async blocks. |
| async function | async_function | src/functions.rst | Upgraded the async function definition to :dt:. |
| atomic type | atomic_type | src/concurrency.rst | Upgraded the atomic type definition to :dt:. |
| attribute | attribute | src/attributes.rst | Upgraded the attribute definition to :dt:. |
| attribute content | attribute_content | src/attributes.rst | Upgraded the attribute content definition to :dt:. |
| attribute macro | attribute_macro | src/macros.rst | Upgraded the attribute macro definition to :dt:. |
| auto trait | auto_trait | src/types-and-traits.rst | Upgraded the auto trait definition to :dt:. |
| await expression | await_expression | src/expressions.rst | Upgraded the await expression definition to :dt:. |
| associated constant | associated_constant | src/associated-items.rst | Upgraded the associated constant definition to :dt:. |
| associated function | associated_function | src/associated-items.rst | Upgraded the associated function definition to :dt:. |
| associated implementation constant | associated_implementation_constant | src/associated-items.rst | Upgraded the associated implementation constant definition to :dt:. |
| associated implementation function | associated_implementation_function | src/associated-items.rst | Upgraded the associated implementation function definition to :dt:. |
| associated implementation type | associated_implementation_type | src/associated-items.rst | Upgraded the associated implementation type definition to :dt:. |
| associated item | associated_item | src/associated-items.rst | Upgraded the associated item definition to :dt:. |
| associated trait constant | associated_trait_constant | src/associated-items.rst | Upgraded the associated trait constant definition to :dt:. |
| associated trait function | associated_trait_function | src/associated-items.rst | Upgraded the associated trait function definition to :dt:. |
| associated trait implementation function | associated_trait_implementation_function | src/associated-items.rst | Upgraded the associated trait implementation function definition to :dt:. |
| associated trait implementation item | associated_trait_implementation_item | src/associated-items.rst | Upgraded the associated trait implementation item definition to :dt:. |
| associated trait item | associated_trait_item | src/associated-items.rst | Upgraded the associated trait item definition to :dt:. |
| associated trait type | associated_trait_type | src/associated-items.rst | Upgraded the associated trait type definition to :dt:. |
| associated type | associated_type | src/associated-items.rst | Upgraded the associated type definition to :dt:. |
| associated type projection | associated_type_projection | src/entities-and-resolution.rst | Upgraded the associated type projection definition to :dt:. |
| associativity | associativity | src/expressions.rst | Upgraded the associativity definition to :dt:. |
| anonymous type parameter | anonymous_type_parameter | src/types-and-traits.rst | Added a definition for anonymous type parameters in the impl trait section. |
| base initializer | base_initializer | src/expressions.rst | Upgraded the base initializer definition to :dt:. |
| basic assignment | basic_assignment | src/expressions.rst | Upgraded the basic assignment definition to :dt:. |
| binary crate | binary_crate | src/program-structure-and-compilation.rst | Upgraded the binary crate definition to :dt:. |
| binary literal | binary_literal | src/lexical-elements.rst | Upgraded the binary literal definition to :dt:. |
| binary operator | binary_operator | src/expressions.rst | Added a definition for binary operators near operand rules. |
| assigned operand | assigned_operand | src/expressions.rst | Upgraded the assigned operand definition in compound assignment expressions to :dt:. |
| assignee expression | assignee_expression | src/expressions.rst | Upgraded the assignee expression classification definition to :dt:. |
| assignee operand | assignee_operand | src/expressions.rst | Upgraded the assignee operand definition in assignment expressions to :dt:. |
| assignment expression | assignment_expression | src/expressions.rst | Upgraded the assignment expression definition to :dt:. |
| binding | binding | src/patterns.rst | Upgraded the binding definition in Binding Modes to :dt:. |
| binding argument | binding_argument | src/generics.rst | Upgraded the binding argument definition to :dt:. |
| binding bound argument | binding_bound_argument | src/generics.rst | Upgraded the binding bound argument definition to :dt:. |
| binding mode | binding_mode | src/patterns.rst | Added a definition for binding modes in Binding Modes. |
| binding pattern | binding_pattern | src/patterns.rst | Upgraded the binding pattern definition to :dt:. |
| binding scope | binding_scope | src/entities-and-resolution.rst | Upgraded the binding scope definition to :dt:. |
| bit and assignment | bit_and_assignment | src/expressions.rst | Added a definition for bit-and assignment in compound assignment expressions. |
| bit and assignment expression | bit_and_assignment_expression | src/expressions.rst | Upgraded the bit-and assignment expression definition to :dt:. |
| bit and expression | bit_and_expression | src/expressions.rst | Upgraded the bit-and expression definition to :dt:. |
| bit expression | bit_expression | src/expressions.rst | Upgraded the bit expression definition to :dt:. |
| bit or assignment | bit_or_assignment | src/expressions.rst | Added a definition for bit-or assignment in compound assignment expressions. |
| bit or assignment expression | bit_or_assignment_expression | src/expressions.rst | Upgraded the bit-or assignment expression definition to :dt:. |
| bit or expression | bit_or_expression | src/expressions.rst | Upgraded the bit-or expression definition to :dt:. |
| bit xor assignment | bit_xor_assignment | src/expressions.rst | Added a definition for bit-xor assignment in compound assignment expressions. |
| bit xor assignment expression | bit_xor_assignment_expression | src/expressions.rst | Upgraded the bit-xor assignment expression definition to :dt:. |
| bit xor expression | bit_xor_expression | src/expressions.rst | Upgraded the bit-xor expression definition to :dt:. |
| block comment | block_comment | src/lexical-elements.rst | Upgraded the block comment definition to :dt:. |
| block expression | block_expression | src/expressions.rst | Upgraded the block expression definition to :dt:. |
| bool | bool | src/types-and-traits.rst | Upgraded the bool type definition to :dt:. |
| boolean literal | boolean_literal | src/lexical-elements.rst | Upgraded the boolean literal definition to :dt:. |
| borrow | borrow | src/ownership-and-deconstruction.rst | Upgraded the borrow definition to :dt:. |
| borrow expression | borrow_expression | src/expressions.rst | Upgraded the borrow expression definition to :dt:. |
| borrowed | borrowed | src/ownership-and-deconstruction.rst | Added a definition for the borrowed state. |
| borrowing | borrowing | src/ownership-and-deconstruction.rst | Upgraded the borrowing definition to :dt:. |
| bound | bound | src/types-and-traits.rst | Upgraded the bound definition to :dt:. |
| bound pattern | bound_pattern | src/patterns.rst | Upgraded the bound pattern definition to :dt:. |
| break expression | break_expression | src/expressions.rst | Upgraded the break expression definition to :dt:. |
| break type | break_type | src/expressions.rst | Upgraded the break type definition to :dt:. |
| break value | break_value | src/expressions.rst | Upgraded the break value definition to :dt:. |
| built-in attribute | built_in_attribute | src/attributes.rst | Upgraded the built-in attribute definition to :dt:. |
| built-in trait | built_in_trait | src/types-and-traits.rst | Added a definition for built-in traits in the Traits section. |
| byte literal | byte_literal | src/lexical-elements.rst | Upgraded the byte literal definition to :dt:. |
| byte string literal | byte_string_literal | src/lexical-elements.rst | Upgraded the byte string literal definition to :dt:. |
| C | c | src/ffi.rst | Added a definition in the FFI ABI section to ground references to C ABIs. |
| C representation | c_representation | src/types-and-traits.rst | Upgraded the C representation definition to :dt: in Type Representation. |
| c string literal | c_string_literal | src/lexical-elements.rst | Upgraded the C string literal definition to :dt: in C String Literals. |
| Call conformance | call_conformance | src/expressions.rst | Added a definition in Call Expressions alongside the ABI requirement. |
| call expression | call_expression | src/expressions.rst | Upgraded the call expression definition to :dt: in Call Expressions. |
| call operand | call_operand | src/expressions.rst | Upgraded the call operand definition to :dt: in Call Expressions. |
| call resolution | call_resolution | src/entities-and-resolution.rst | Upgraded the call resolution definition to :dt: in Call Resolution. |
| call site hygiene | call_site_hygiene | src/macros.rst | Upgraded the call site hygiene definition to :dt: in Hygiene. |
| callee type | callee_type | src/expressions.rst | Upgraded the callee type definition to :dt: in Call Expressions. |
| capture mode | capture_mode | src/expressions.rst | Upgraded the capture mode definition to :dt: in Capturing. |
| capture target | capture_target | src/expressions.rst | Upgraded the capture target definition to :dt: in Capturing. |
| capturing | capturing | src/expressions.rst | Upgraded the capturing definition to :dt: in Capturing. |
| capturing environment | capturing_environment | src/expressions.rst | Upgraded the capturing environment definition to :dt: in Capturing. |
| capturing expression | capturing_expression | src/expressions.rst | Upgraded the capturing expression definition to :dt: in Capturing. |
| cast | cast | src/expressions.rst | Upgraded the cast definition to :dt: in Type Cast Expressions. |
| char | char | src/types-and-traits.rst | Upgraded the char type definition to :dt: in Char Type. |
| character literal | character_literal | src/lexical-elements.rst | Upgraded the character literal definition to :dt: in Character Literals. |
| closure body | closure_body | src/expressions.rst | Upgraded the closure body definition to :dt: in Closure Expressions. |
| closure expression | closure_expression | src/expressions.rst | Upgraded the closure expression definition to :dt: in Closure Expressions. |
| closure parameter | closure_parameter | src/expressions.rst | Upgraded the closure parameter definition to :dt: in Closure Expressions. |
| closure type | closure_type | src/types-and-traits.rst | Upgraded the closure type definition to :dt: in Closure Types. |
| comment | comment | src/lexical-elements.rst | Upgraded the comment definition to :dt: in Comments. |
| comparison expression | comparison_expression | src/expressions.rst | Upgraded the comparison expression definition to :dt: in Comparison Expressions. |
| compilation root | compilation_root | src/program-structure-and-compilation.rst | Upgraded the compilation root definition to :dt: in Compilation Roots. |
| compound assignment | compound_assignment | src/expressions.rst | Added a definition for compound assignment in Compound Assignment Expressions. |
| compound assignment expression | compound_assignment_expression | src/expressions.rst | Upgraded the compound assignment expression definition to :dt: in Compound Assignment Expressions. |
| concrete type | concrete_type | src/types-and-traits.rst | Added a definition near Types for fully substituted generic types. |
| conditional compilation | conditional_compilation | src/program-structure-and-compilation.rst | Upgraded the conditional compilation definition to :dt: in Conditional Compilation. |
| conditionally-compiled source code | conditionally_compiled_source_code | src/program-structure-and-compilation.rst | Upgraded the conditionally-compiled source code definition to :dt: in Conditional Compilation. |
| configuration predicate | configuration_predicate | src/attributes.rst | Upgraded the configuration predicate definition to :dt: in cfg attribute rules. |
| const block expression | const_block_expression | src/expressions.rst | Upgraded the const block expression definition to :dt: in Const Blocks. |
| constant | constant | src/values.rst | Upgraded the constant definition to :dt: in Constants. |
| constant argument | constant_argument | src/generics.rst | Upgraded the constant argument definition to :dt: in Generic Arguments. |
| constant context | constant_context | src/expressions.rst | Upgraded the constant context definition to :dt: in Constant Expressions. |
| constant expression | constant_expression | src/expressions.rst | Upgraded the constant expression definition to :dt: in Constant Expressions. |
| constant function | constant_function | src/functions.rst | Upgraded the constant function definition to :dt: in Functions. |
| constant initializer | constant_initializer | src/values.rst | Upgraded the constant initializer definition to :dt: in Constants. |
| constant parameter | constant_parameter | src/generics.rst | Upgraded the constant parameter definition to :dt: in Generics. |
| constant parameter initializer | constant_parameter_initializer | src/generics.rst | Upgraded the constant parameter initializer definition to :dt: in Generics. |
| constant promotion | constant_promotion | src/values.rst | Upgraded the constant promotion definition to :dt: in Constant Promotion. |
| construct | construct | src/entities-and-resolution.rst | Added a definition for constructs at the start of Entities. |
| constructee | constructee | src/expressions.rst | Upgraded the constructee definition to :dt: in Struct Expressions. |
| container operand | container_operand | src/expressions.rst | Upgraded the container operand definition to :dt: in Field Access Expressions. |
| continue expression | continue_expression | src/expressions.rst | Added a definition for continue expression in Continue Expressions. |
| control flow boundary | control_flow_boundary | src/expressions.rst | Added a definition in Async Blocks to anchor return boundaries. |
| copy type | copy_type | src/ownership-and-deconstruction.rst | Upgraded the copy type definition to :dt: in Passing Conventions. |
| crate | crate | src/program-structure-and-compilation.rst | Upgraded the crate definition to :dt: in Crates. |
| crate import | crate_import | src/program-structure-and-compilation.rst | Upgraded the crate import definition to :dt: in Crate Imports. |
| crate indication | crate_indication | src/program-structure-and-compilation.rst | Upgraded the crate indication definition to :dt: in Crate Imports. |
| crate public modifier | crate_public_modifier | src/entities-and-resolution.rst | Upgraded the crate public modifier definition to :dt: in Visibility Modifiers. |
| crate root | crate_root | src/program-structure-and-compilation.rst | Added a definition for crate root in Compilation Roots. |
| crate root module | crate_root_module | src/program-structure-and-compilation.rst | Upgraded the crate root module definition to :dt: in Compilation Roots. |
| crate type | crate_type | src/program-structure-and-compilation.rst | Upgraded the crate type definition to :dt: in Crates. |
| dereference | dereference | src/expressions.rst | Reviewed usages in src/expressions.rst; added definition to the owning section. |
| discriminant initializer | discriminant_initializer | src/types-and-traits.rst | Reviewed usages in src/types-and-traits.rst; added definition to the owning section. |
| discriminant type | discriminant_type | src/types-and-traits.rst | Reviewed usages in src/types-and-traits.rst; added definition to the owning section. |
| division assignment | division_assignment | src/expressions.rst | Reviewed usages in src/expressions.rst; added definition to the owning section. |
| drop order | drop_order | src/ownership-and-deconstruction.rst | Reviewed usages in src/ownership-and-deconstruction.rst; added definition to the owning section. |
| element type | element_type | src/types-and-traits.rst | Reviewed usages in src/types-and-traits.rst; added definition to the owning section. |
| elided | elided | src/types-and-traits.rst | Reviewed usages in src/types-and-traits.rst; added definition to the owning section. |
| elided lifetime | elided_lifetime | src/types-and-traits.rst | Reviewed usages in src/types-and-traits.rst; added definition to the owning section. |
| enum | enum | src/types-and-traits.rst | Reviewed usages in src/types-and-traits.rst; added definition to the owning section. |
| enum field | enum_field | src/types-and-traits.rst | Reviewed usages in src/types-and-traits.rst; added definition to the owning section. |
| enum value | enum_value | src/types-and-traits.rst | Reviewed usages in src/types-and-traits.rst; added definition to the owning section. |
| enum variant value | enum_variant_value | src/types-and-traits.rst | Reviewed usages in src/types-and-traits.rst; added definition to the owning section. |
| escaped character | escaped_character | src/lexical-elements.rst | Reviewed usages in src/lexical-elements.rst; added definition to the owning section. |
| f32 | f32 | src/types-and-traits.rst | Reviewed usages in src/types-and-traits.rst; added definition to Floating Point Types. |
| f64 | f64 | src/types-and-traits.rst | Reviewed usages in src/types-and-traits.rst; added definition to Floating Point Types. |
| fat pointer | fat_pointer | src/types-and-traits.rst | Reviewed usages in src/types-and-traits.rst; added definition to the owning section. |
| field | field | src/types-and-traits.rst | Reviewed usages in src/types-and-traits.rst; added definition to the owning section. |
| field index | field_index | src/types-and-traits.rst | Reviewed usages in src/types-and-traits.rst; added definition to the owning section. |
| field list | field_list | src/types-and-traits.rst | Reviewed usages in src/types-and-traits.rst; added definition to the owning section. |
| fixed sized type | fixed_sized_type | src/types-and-traits.rst | Reviewed usages in src/types-and-traits.rst; added definition to the owning section. |
| floating-point type | floating_point_type | src/types-and-traits.rst | Reviewed usages in src/types-and-traits.rst; added definition to the owning section. |
| floating-point value | floating_point_value | src/types-and-traits.rst | Reviewed usages in src/types-and-traits.rst; added definition to the owning section. |
| for loop | for_loop | src/expressions.rst | Reviewed usages in src/expressions.rst; added definition to the owning section. |
| function pointer type parameter | function_pointer_type_parameter | src/types-and-traits.rst | Reviewed usages in src/types-and-traits.rst; added definition to the owning section. |
| function type | function_type | src/types-and-traits.rst | Reviewed usages in src/types-and-traits.rst; added definition to the owning section. |
| generic substitution | generic_substitution | src/generics.rst | Reviewed usages in src/generics.rst; added definition to the owning section. |
| generic type | generic_type | src/generics.rst | Reviewed usages in src/generics.rst; added definition to the owning section. |
| i8 | i8 | src/types-and-traits.rst | Reviewed Integer Types; added definition after signed integer type ranges. |
| i16 | i16 | src/types-and-traits.rst | Reviewed Integer Types; added definition after signed integer type ranges. |
| i32 | i32 | src/types-and-traits.rst | Reviewed Integer Types; added definition after signed integer type ranges. |
| i64 | i64 | src/types-and-traits.rst | Reviewed Integer Types; added definition after signed integer type ranges. |
| i128 | i128 | src/types-and-traits.rst | Reviewed Integer Types; added definition after signed integer type ranges. |
| identifier | identifier | src/lexical-elements.rst | Upgraded the identifier definition to :dt: in Lexical Elements. |
| identifier pattern | identifier_pattern | src/patterns.rst | Upgraded the identifier pattern definition to :dt: in Identifier Patterns. |
| if expression | if_expression | src/expressions.rst | Upgraded the if expression definition to :dt: in If Expressions. |
| if let expression | if_let_expression | src/expressions.rst | Upgraded the if let expression definition to :dt: in If Let Expressions. |
| immutable borrow | immutable_borrow | src/ownership-and-deconstruction.rst | Upgraded the immutable borrow definition to :dt: in Borrowing. |
| immutable borrow expression | immutable_borrow_expression | src/expressions.rst | Upgraded the immutable borrow expression definition to :dt: in Borrow Expressions. |
| immutable place expression | immutable_place_expression | src/expressions.rst | Upgraded the immutable place expression definition to :dt: in Place Expressions. |
| immutable place expression context | immutable_place_expression_context | src/expressions.rst | Added a definition after mutable place expression contexts. |
| immutable raw pointer type | immutable_raw_pointer_type | src/types-and-traits.rst | Upgraded the immutable raw pointer type definition to :dt: in Raw Pointer Types. |
| immutable reference | immutable_reference | src/ownership-and-deconstruction.rst | Upgraded the immutable reference definition to :dt: in References. |
| immutable static | immutable_static | src/values.rst | Upgraded the immutable static definition to :dt: in Statics. |
| immutable variable | immutable_variable | src/values.rst | Added a definition in Variables. |
| impl header lifetime elision | impl_header_lifetime_elision | src/types-and-traits.rst | Upgraded the impl header lifetime elision definition to :dt:. |
| impl trait type | impl_trait_type | src/types-and-traits.rst | Upgraded the impl trait type definition to :dt:. |
| implementation | implementation | src/implementations.rst | Upgraded the implementation definition to :dt: in Implementations. |
| implementation body | implementation_body | src/implementations.rst | Upgraded the implementation body definition to :dt: in Implementations. |
| implementation conformance | implementation_conformance | src/implementations.rst | Upgraded the implementation conformance definition to :dt:. |
| implemented trait | implemented_trait | src/implementations.rst | Upgraded the implemented trait definition to :dt: in Implementations. |
| implementing type | implementing_type | src/implementations.rst | Upgraded the implementing type definition to :dt: in Implementations. |
| implicit borrow | implicit_borrow | src/ownership-and-deconstruction.rst | Upgraded the implicit borrow definition to :dt: in Borrowing. |
| implicitly declared entity | implicitly_declared_entity | src/entities-and-resolution.rst | Upgraded the implicitly declared entity definition to :dt: in Entities. |
| implied bound | implied_bound | src/types-and-traits.rst | Upgraded the implied bound definition to :dt: in Type Bounds. |
| inclusive range pattern | inclusive_range_pattern | src/patterns.rst | Upgraded the inclusive range pattern definition to :dt: in Range Patterns. |
| incomplete associated constant | incomplete_associated_constant | src/associated-items.rst | Added a definition in Associated Items. |
| incomplete associated function | incomplete_associated_function | src/associated-items.rst | Added a definition in Associated Items. |
| incomplete associated type | incomplete_associated_type | src/associated-items.rst | Added a definition in Associated Items. |
| index expression | index_expression | src/expressions.rst | Upgraded the index expression definition to :dt: in Index Expressions. |
| indexable type | indexable_type | src/expressions.rst | Upgraded the indexable type definition to :dt: in Index Expressions. |
| indexed deconstructor | indexed_deconstructor | src/patterns.rst | Upgraded the indexed deconstructor definition to :dt: in Record Struct Patterns. |
| indexed field selector | indexed_field_selector | src/entities-and-resolution.rst | Added a definition in Field Resolution. |
| indexed initializer | indexed_initializer | src/expressions.rst | Upgraded the indexed initializer definition to :dt: in Struct Expressions. |
| indexed operand | indexed_operand | src/expressions.rst | Upgraded the indexed operand definition to :dt: in Index Expressions. |
| indexing operand | indexing_operand | src/expressions.rst | Upgraded the indexing operand definition to :dt: in Index Expressions. |
| indirection type | indirection_type | src/types-and-traits.rst | Added a definition in Indirection Types. |
| inert attribute | inert_attribute | src/attributes.rst | Upgraded the inert attribute definition to :dt: in Attribute Properties. |
| inferred type | inferred_type | src/types-and-traits.rst | Upgraded the inferred type definition to :dt: in Inferred Types. |
| infinite loop | infinite_loop | src/expressions.rst | Added a glossary cross-reference in Infinite Loops. |
| infinite loop expression | infinite_loop_expression | src/expressions.rst | Upgraded the infinite loop expression definition to :dt: in Infinite Loops. |
| inherent implementation | inherent_implementation | src/implementations.rst | Upgraded the inherent implementation definition to :dt: in Implementations. |
| initialization | initialization | src/values.rst | Added a definition near Values. |
| initialization expression | initialization_expression | src/expressions.rst | Added a definition near Destructuring Assignment. |
| initialization type | initialization_type | src/types-and-traits.rst | Added a definition in Type Aliases. |
| inline assembly | inline_assembly | src/inline-assembly.rst | Upgraded the inline assembly definition to :dt:. |
| inline module | inline_module | src/program-structure-and-compilation.rst | Upgraded the inline module definition to :dt: in Modules. |
| inner attribute | inner_attribute | src/attributes.rst | Upgraded the inner attribute definition to :dt: in Attributes. |
| inner block doc | inner_block_doc | src/lexical-elements.rst | Upgraded the inner block doc definition to :dt: in Comments. |
| inner doc comment | inner_doc_comment | src/lexical-elements.rst | Upgraded the inner doc comment definition to :dt: in Comments. |
| inner line doc | inner_line_doc | src/lexical-elements.rst | Upgraded the inner line doc definition to :dt: in Comments. |
| input register | input_register | src/inline-assembly.rst | Upgraded the input register definition to :dt: in Registers. |
| input register expression | input_register_expression | src/inline-assembly.rst | Upgraded the input register expression definition to :dt: in Register Arguments. |
| input-output register expression | input_output_register_expression | src/inline-assembly.rst | Upgraded the input-output register expression definition to :dt: in Register Arguments. |
| integer literal | integer_literal | src/lexical-elements.rst | Upgraded the integer literal definition to :dt: in Numeric Literals. |
| integer suffix | integer_suffix | src/lexical-elements.rst | Upgraded the integer suffix definition to :dt: in Numeric Literals. |
| integer type | integer_type | src/types-and-traits.rst | Added a definition in Integer Types. |
| integer type variable | integer_type_variable | src/types-and-traits.rst | Upgraded the integer type variable definition to :dt: in Type Inference. |
| interior mutability | interior_mutability | src/types-and-traits.rst | Upgraded the interior mutability definition to :dt:. |
| intermediate match arm | intermediate_match_arm | src/expressions.rst | Upgraded the intermediate match arm definition to :dt: in Match Expressions. |
| irrefutable constant | irrefutable_constant | src/patterns.rst | Upgraded the irrefutable constant definition to :dt: in Refutability. |
| irrefutable pattern | irrefutable_pattern | src/patterns.rst | Upgraded the irrefutable pattern definition to :dt: in Refutability. |
| isize | isize | src/types-and-traits.rst | Upgraded the isize definition to :dc: in Integer Types. |
| item | item | src/entities-and-resolution.rst | Added a definition in Entities. |
| item scope | item_scope | src/entities-and-resolution.rst | Upgraded the item scope definition to :dt:. |
| item statement | item_statement | src/statements.rst | Upgraded the item statement definition to :dt: in Statements. |
| iteration expression | iteration_expression | src/expressions.rst | Upgraded the iteration expression definition to :dt: in While Loops. |
| keyword | keyword | src/lexical-elements.rst | Upgraded the keyword definition to :dt: in Keywords. |
| label | label | src/expressions.rst | Defined label in Loop Expressions alongside label syntax and named loop rules. |
| label indication | label_indication | src/expressions.rst | Upgraded Loop Labels definition to :dt: for label indication. |
| label scope | label_scope | src/entities-and-resolution.rst | Upgraded Label Scope definition in Scopes. |
| layout | layout | src/types-and-traits.rst | Added layout definition in Type Layout with alignment, size, and field offsets. |
| lazy and expression | lazy_and_expression | src/expressions.rst | Upgraded Lazy Boolean Expressions definition for lazy and. |
| lazy boolean expression | lazy_boolean_expression | src/expressions.rst | Upgraded Lazy Boolean Expressions definition for lazy boolean expression. |
| lazy or expression | lazy_or_expression | src/expressions.rst | Upgraded Lazy Boolean Expressions definition for lazy or. |
| left operand | left_operand | src/expressions.rst | Upgraded operand classification definition in Operator Expressions. |
| less-than expression | less_than_expression | src/expressions.rst | Upgraded Comparison Expressions definition for less-than. |
| less-than-or-equals expression | less_than_or_equals_expression | src/expressions.rst | Upgraded Comparison Expressions definition for less-than-or-equals. |
| let binding | let_binding | src/statements.rst | Added let binding definition in Let Statements to cover let/if let/while let. |
| let initializer | let_initializer | src/statements.rst | Upgraded Let Statements definition for let initializer. |
| let statement | let_statement | src/statements.rst | Upgraded Let Statements definition for let statement. |
| lexical element | lexical_element | src/lexical-elements.rst | Upgraded Lexical Elements definition near source file rules. |
| library crate | library_crate | src/program-structure-and-compilation.rst | Upgraded Crates section definition for library crate. |
| lifetime | lifetime | src/types-and-traits.rst | Upgraded Lifetimes definition. |
| lifetime argument | lifetime_argument | src/generics.rst | Upgraded Generic Arguments definition for lifetime argument. |
| lifetime bound | lifetime_bound | src/types-and-traits.rst | Upgraded Type Bounds definition for lifetime bound. |
| lifetime bound predicate | lifetime_bound_predicate | src/generics.rst | Upgraded Where Clause predicate definition for lifetime bound predicate. |
| lifetime elision | lifetime_elision | src/types-and-traits.rst | Upgraded Lifetime Elision definition. |
| lifetime parameter | lifetime_parameter | src/generics.rst | Upgraded Generic Parameters definition for lifetime parameter. |
| lifetime variable | lifetime_variable | src/types-and-traits.rst | Reviewed Type Inference definition; already defined in Lifetime Variables. |
| line | line | src/lexical-elements.rst | Upgraded source file line definition. |
| line comment | line_comment | src/lexical-elements.rst | Upgraded comment definition for line comment. |
| literal | literal | src/lexical-elements.rst | Upgraded Literals definition. |
| literal expression | literal_expression | src/expressions.rst | Upgraded Literal Expressions definition. |
| literal pattern | literal_pattern | src/patterns.rst | Upgraded Literal Patterns definition. |
| local trait | local_trait | src/types-and-traits.rst | Upgraded Traits definition for local trait. |
| local type | local_type | src/types-and-traits.rst | Upgraded Types definition for local type. |
| local variable | local_variable | src/values.rst | Added local variable definition in Variables. |
| loop | loop | src/expressions.rst | Added loop definition in Loop Expressions referencing loop expression. |
| loop body | loop_body | src/expressions.rst | Upgraded Loop Expressions definition for loop body. |
| loop expression | loop_expression | src/expressions.rst | Upgraded Loop Expressions definition for loop expression. |
| macro | macro | src/macros.rst | Upgraded definition in Macros overview. |
| macro expansion | macro_expansion | src/macros.rst | Upgraded definition in Macro Expansion legality rules. |
| macro implementation function | macro_implementation_function | src/macros.rst | Upgraded definition in Procedural Macros. |
| macro invocation | macro_invocation | src/macros.rst | Upgraded definition in Macro Invocation. |
| macro match | macro_match | src/macros.rst | Upgraded definition in Declarative Macros legality rules. |
| macro matcher | macro_matcher | src/macros.rst | Upgraded definition in Declarative Macros legality rules. |
| macro matching | macro_matching | src/macros.rst | Upgraded definition in Macro Matching. |
| macro repetition | macro_repetition | src/macros.rst | Upgraded definition in Repetition legality rules. |
| macro repetition in matching | macro_repetition_in_matching | src/macros.rst | Upgraded definition in Repetition legality rules. |
| macro repetition in transcription | macro_repetition_in_transcription | src/macros.rst | Upgraded definition in Repetition legality rules. |
| macro rule | macro_rule | src/macros.rst | Upgraded definition in Declarative Macros legality rules. |
| macro statement | macro_statement | src/statements.rst | Upgraded definition in Statements. |
| macro transcriber | macro_transcriber | src/macros.rst | Upgraded definition in Declarative Macros legality rules. |
| macro transcription | macro_transcription | src/macros.rst | Upgraded definition in Macro Transcription. |
| main function signature | main_function_signature | src/program-structure-and-compilation.rst | Reworded and upgraded definition in Program Entry Point. |
| match arm | match_arm | src/expressions.rst | Upgraded definition in Match Expressions. |
| match arm body | match_arm_body | src/expressions.rst | Upgraded definition in Match Expressions. |
| match arm guard | match_arm_guard | src/expressions.rst | Upgraded definition in Match Expressions. |
| match arm matcher | match_arm_matcher | src/expressions.rst | Upgraded definition in Match Expressions. |
| match expression | match_expression | src/expressions.rst | Upgraded definition in Match Expressions. |
| metavariable | metavariable | src/macros.rst | Upgraded definition in Metavariables. |
| metavariable indication | metavariable_indication | src/macros.rst | Upgraded definition in Metavariables. |
| method | method | src/associated-items.rst | Upgraded definition in Associated Items. |
| method call expression | method_call_expression | src/expressions.rst | Upgraded definition in Method Call Expressions. |
| method operand | method_operand | src/expressions.rst | Upgraded definition in Method Call Expressions. |
| method resolution | method_resolution | src/entities-and-resolution.rst | Upgraded definition in Method Resolution. |
| mixed site hygiene | mixed_site_hygiene | src/macros.rst | Reworded hygiene category definition to be glossary-ready. |
| modifying operand | modifying_operand | src/expressions.rst | Upgraded definition in Compound Assignment Expressions. |
| module | module | src/program-structure-and-compilation.rst | Upgraded definition in Modules. |
| move type | move_type | src/ownership-and-deconstruction.rst | Upgraded definition in Passing Conventions. |
| multi segment path | multi_segment_path | src/entities-and-resolution.rst | Upgraded definition in Paths. |
| multiplication assignment | multiplication_assignment | src/expressions.rst | Added definition in Compound Assignment Expressions. |
| multiplication assignment expression | multiplication_assignment_expression | src/expressions.rst | Upgraded definition in Compound Assignment Expressions. |
| multiplication expression | multiplication_expression | src/expressions.rst | Upgraded definition in Arithmetic Expressions. |
| mutability | mutability | src/values.rst | Added definition in Values legality rules. |
| mutable assignee expression | mutable_assignee_expression | src/expressions.rst | Added definition in Assignee Expressions. |
| mutable binding | mutable_binding | src/patterns.rst | Added definition in Binding Modes. |
| mutable borrow | mutable_borrow | src/ownership-and-deconstruction.rst | Upgraded definition in Borrowing. |
| mutable borrow expression | mutable_borrow_expression | src/expressions.rst | Upgraded definition in Borrow Expression. |
| mutable place expression | mutable_place_expression | src/expressions.rst | Upgraded definition in Place Expressions. |
| mutable place expression context | mutable_place_expression_context | src/expressions.rst | Upgraded definition in Place Expression Contexts. |
| mutable raw pointer type | mutable_raw_pointer_type | src/types-and-traits.rst | Upgraded definition in Raw Pointer Types. |
| mutable reference | mutable_reference | src/ownership-and-deconstruction.rst | Upgraded definition in References. |
| mutable reference type | mutable_reference_type | src/types-and-traits.rst | Upgraded definition in Reference Types. |
| mutable static | mutable_static | src/values.rst | Upgraded definition in Statics. |
| mutable variable | mutable_variable | src/values.rst | Added definition in Variables. |
| name | name | src/entities-and-resolution.rst | Reviewed Entities and Namespaces usages; upgraded the Entities definition to :dt:. |
| named block expression | named_block_expression | src/expressions.rst | Upgraded the Named Blocks definition to :dt:. |
| named deconstructor | named_deconstructor | src/patterns.rst | Upgraded the Record Struct Patterns definition to :dt:. |
| named field selector | named_field_selector | src/entities-and-resolution.rst | Added a definition in Field Resolution alongside indexed field selector. |
| named initializer | named_initializer | src/expressions.rst | Upgraded the Struct Expressions definition to :dt:. |
| named loop expression | named_loop_expression | src/expressions.rst | Upgraded the Loop Expressions definition to :dt:. |
| named register argument | named_register_argument | src/inline-assembly.rst | Upgraded the Register Arguments definition to :dt:. |
| namespace | namespace | src/entities-and-resolution.rst | Upgraded the Namespaces definition to :dt:. |
| NaN-boxing | nan_boxing | src/inline-assembly.rst | Added a definition near the register size rules where the term is used. |
| negation expression | negation_expression | src/expressions.rst | Upgraded the Negation Expression definition to :dt:. |
| nesting import | nesting_import | src/entities-and-resolution.rst | Upgraded the Use Imports definition to :dt:. |
| never type | never_type | src/types-and-traits.rst | Upgraded the Never Type definition to :dt:. |
| non-reference pattern | non_reference_pattern | src/patterns.rst | Upgraded the Binding Modes definition to :dt:. |
| not configuration predicate | not_configuration_predicate | src/attributes.rst | Upgraded the cfg predicate definition to :dt:. |
| not-equals expression | not_equals_expression | src/expressions.rst | Upgraded the Comparison Expressions definition to :dt:. |
| null | null | src/values.rst | Added a definition in Values legality rules for the address ``0``. |
| numeric literal | numeric_literal | src/lexical-elements.rst | Upgraded the Numeric Literals definition to :dt:. |
| numeric literal pattern | numeric_literal_pattern | src/patterns.rst | Upgraded the Literal Patterns definition to :dt:. |
| numeric type | numeric_type | src/types-and-traits.rst | Added a Numeric Types definition before the floating-point and integer subsections. |
| object safety | object_safety | src/types-and-traits.rst | Added a definition in the Object Safety rules to describe the trait object suitability check. |
| obsolete range pattern | obsolete_range_pattern | src/patterns.rst | Upgraded the Range Patterns definition to :dt:. |
| octal literal | octal_literal | src/lexical-elements.rst | Upgraded the Numeric Literals definition to :dt:. |
| operand | operand | src/expressions.rst | Upgraded the operand definition in Expressions classification to :dt:. |
| operator expression | operator_expression | src/expressions.rst | Upgraded the Operator Expressions definition to :dt:. |
| opt-out trait bound | opt_out_trait_bound | src/types-and-traits.rst | Upgraded the Trait and Lifetime Bounds definition to :dt:. |
| or-pattern | or_pattern | src/patterns.rst | Upgraded the Patterns legality rules definition to :dt:. |
| outer attribute | outer_attribute | src/attributes.rst | Upgraded the outer attribute definition to :dt:. |
| outer block doc | outer_block_doc | src/lexical-elements.rst | Upgraded the Comments definition to :dt:. |
| outer doc comment | outer_doc_comment | src/lexical-elements.rst | Upgraded the Comments definition to :dt:. |
| outer line doc | outer_line_doc | src/lexical-elements.rst | Upgraded the Comments definition to :dt:. |
| outline module | outline_module | src/program-structure-and-compilation.rst | Upgraded the Modules definition to :dt:. |
| outlives bound | outlives_bound | src/types-and-traits.rst | Upgraded the Trait and Lifetime Bounds definition to :dt:. |
| output register | output_register | src/inline-assembly.rst | Upgraded the Registers definition to :dt:. |
| output register expression | output_register_expression | src/inline-assembly.rst | Upgraded the Register Expressions definition to :dt:. |
| owner | owner | src/ownership-and-deconstruction.rst | Upgraded the Ownership definition to :dt:. |
| ownership | ownership | src/ownership-and-deconstruction.rst | Upgraded the Ownership definition to :dt:. |
| panic | panic | src/exceptions-and-errors.rst | Reviewed Panic in src/exceptions-and-errors.rst; upgraded the definition to :dt:. |
| parenthesized expression | parenthesized_expression | src/expressions.rst | Reviewed Parenthesized Expressions in src/expressions.rst; upgraded the definition to :dt:. |
| parenthesized pattern | parenthesized_pattern | src/patterns.rst | Reviewed Parenthesized Patterns in src/patterns.rst; upgraded the definition to :dt:. |
| parenthesized type | parenthesized_type | src/types-and-traits.rst | Reviewed Parenthesized Types in src/types-and-traits.rst; upgraded the definition to :dt:. |
| passing convention | passing_convention | src/ownership-and-deconstruction.rst | Reviewed Passing Conventions in src/ownership-and-deconstruction.rst; upgraded the definition to :dt:. |
| path | path | src/entities-and-resolution.rst | Reviewed Paths in src/entities-and-resolution.rst; upgraded the definition to :dt:. |
| path attribute | path_attribute | src/attributes.rst | Clarified Attribute ``path`` as a :dt:`path attribute` to avoid colliding with the glossary path term while keeping the literal spelling via :c:`path`. |
| path expression | path_expression | src/expressions.rst | Reviewed Path Expressions in src/expressions.rst; upgraded the definition to :dt:. |
| path expression resolution | path_expression_resolution | src/entities-and-resolution.rst | Reviewed Path Expression Resolution in src/entities-and-resolution.rst; upgraded the definition to :dt:. |
| path pattern | path_pattern | src/patterns.rst | Reviewed Path Patterns in src/patterns.rst; upgraded the definition to :dt:. |
| path resolution | path_resolution | src/entities-and-resolution.rst | Reviewed Path Resolution in src/entities-and-resolution.rst; upgraded the definition to :dt:. |
| path segment | path_segment | src/entities-and-resolution.rst | Reviewed Paths in src/entities-and-resolution.rst; upgraded the definition to :dt:. |
| pattern | pattern | src/patterns.rst | Reviewed Patterns intro in src/patterns.rst; upgraded the definition to :dt:. |
| pattern-without-alternation | pattern_without_alternation | src/patterns.rst | Reviewed Patterns legality rules in src/patterns.rst; upgraded the definition to :dt:. |
| pattern-without-range | pattern_without_range | src/patterns.rst | Reviewed Patterns legality rules in src/patterns.rst; upgraded the definition to :dt:. |
| place | place | src/expressions.rst | Reviewed Place Expressions in src/expressions.rst; added a definition before place expression rules. |
| place expression | place_expression | src/expressions.rst | Reviewed Place Expressions in src/expressions.rst; upgraded the definition to :dt:. |
| place expression context | place_expression_context | src/expressions.rst | Reviewed Place Expressions in src/expressions.rst; upgraded the definition to :dt:. |
| pointer | pointer | src/types-and-traits.rst | Reviewed Indirection Types in src/types-and-traits.rst; added a definition near pointer types. |
| pointer type | pointer_type | src/types-and-traits.rst | Reviewed Indirection Types in src/types-and-traits.rst; added a definition to ground pointer size references. |
| positional register argument | positional_register_argument | src/inline-assembly.rst | Reviewed Register Arguments in src/inline-assembly.rst; upgraded the definition to :dt:. |
| precedence | precedence | src/expressions.rst | Reviewed Expression Precedence in src/expressions.rst; upgraded the definition to :dt:. |
| prelude | prelude | src/entities-and-resolution.rst | Reviewed Preludes in src/entities-and-resolution.rst; upgraded the definition to :dt:. |
| prelude entity | prelude_entity | src/entities-and-resolution.rst | Reviewed Preludes in src/entities-and-resolution.rst; added a standalone definition. |
| prelude name | prelude_name | src/entities-and-resolution.rst | Reviewed Preludes in src/entities-and-resolution.rst; added a standalone definition. |
| primitive representation | primitive_representation | src/types-and-traits.rst | Reviewed Type Representation in src/types-and-traits.rst; upgraded the definition to :dt:. |
| principal trait | principal_trait | src/types-and-traits.rst | Reviewed Trait Object Types in src/types-and-traits.rst; upgraded the definition to :dt:. |
| private visibility | private_visibility | src/entities-and-resolution.rst | Reviewed Visibility Modifiers in src/entities-and-resolution.rst; upgraded the definition to :dt:. |
| proc-macro crate | proc_macro_crate | src/program-structure-and-compilation.rst | Reviewed Crates in src/program-structure-and-compilation.rst; upgraded the definition to :dt:. |
| procedural macro | procedural_macro | src/macros.rst | Reviewed Procedural Macros in src/macros.rst; upgraded the definition to :dt:. |
| program entry point | program_entry_point | src/program-structure-and-compilation.rst | Reviewed Program Entry Point in src/program-structure-and-compilation.rst; upgraded the definition to :dt:. |
| public visibility | public_visibility | src/entities-and-resolution.rst | Reviewed Visibility Modifiers in src/entities-and-resolution.rst; upgraded the definition to :dt:. |
| punctuator | punctuator | src/lexical-elements.rst | Reviewed Punctuators in src/lexical-elements.rst; added a definition before simple punctuators. |
| pure identifier | pure_identifier | src/lexical-elements.rst | Reviewed Identifiers in src/lexical-elements.rst; upgraded the definition to :dt:. |
| qualified path expression | qualified_path_expression | src/entities-and-resolution.rst | Reviewed qualified path expression usage and resolution rules; upgraded the definition in Paths and Resolutions to :dt:. |
| qualified type | qualified_type | src/entities-and-resolution.rst | Reviewed qualified type rules; upgraded the definition in Paths and Resolutions to :dt:. |
| qualified type path | qualified_type_path | src/entities-and-resolution.rst | Reviewed qualified type path resolution; upgraded the definition in Paths and Resolutions to :dt:. |
| qualifying trait | qualifying_trait | src/entities-and-resolution.rst | Reviewed qualifying trait rules; upgraded the definition in Paths and Resolutions to :dt:. |
| range expression | range_expression | src/expressions.rst | Upgraded the definition to :dt: in Range Expressions. |
| range expression high bound | range_expression_high_bound | src/expressions.rst | Upgraded the definition to :dt: in Range Expressions. |
| range expression low bound | range_expression_low_bound | src/expressions.rst | Upgraded the definition to :dt: in Range Expressions. |
| range pattern | range_pattern | src/patterns.rst | Upgraded the definition to :dt: in Range Patterns. |
| range pattern bound | range_pattern_bound | src/patterns.rst | Upgraded the definition to :dt: in Range Patterns. |
| range pattern high bound | range_pattern_high_bound | src/patterns.rst | Upgraded the definition to :dt: in Range Patterns. |
| range pattern low bound | range_pattern_low_bound | src/patterns.rst | Upgraded the definition to :dt: in Range Patterns. |
| range-from expression | range_from_expression | src/expressions.rst | Upgraded the definition to :dt: in Range Expressions. |
| range-from-to expression | range_from_to_expression | src/expressions.rst | Upgraded the definition to :dt: in Range Expressions. |
| range-full expression | range_full_expression | src/expressions.rst | Verified existing :dt: definition in Range Expressions. |
| range-inclusive expression | range_inclusive_expression | src/expressions.rst | Upgraded the definition to :dt: in Range Expressions. |
| range-to expression | range_to_expression | src/expressions.rst | Upgraded the definition to :dt: in Range Expressions. |
| range-to-inclusive expression | range_to_inclusive_expression | src/expressions.rst | Upgraded the definition to :dt: in Range Expressions. |
| raw borrow expression | raw_borrow_expression | src/expressions.rst | Upgraded the definition to :dt: in Raw Borrow Expression. |
| raw byte string literal | raw_byte_string_literal | src/lexical-elements.rst | Upgraded the definition to :dt: in Raw Byte String Literals. |
| raw c string literal | raw_c_string_literal | src/lexical-elements.rst | Upgraded the definition to :dt: in Raw C String Literals. |
| raw pointer | raw_pointer | src/types-and-traits.rst | Added a :dt: definition in Raw Pointer Types. |
| raw pointer type | raw_pointer_type | src/types-and-traits.rst | Upgraded the definition to :dt: in Raw Pointer Types. |
| raw string literal | raw_string_literal | src/lexical-elements.rst | Upgraded the definition to :dt: in Raw String Literals. |
| reachable control flow path | reachable_control_flow_path | src/values.rst | Added a :dt: definition in Variables. |
| receiver operand | receiver_operand | src/expressions.rst | Upgraded the definition to :dt: in Method Call Expressions. |
| receiver type | receiver_type | src/entities-and-resolution.rst | Verified existing :dt: definition in Method Resolution. |
| record enum variant | record_enum_variant | src/types-and-traits.rst | Added a :dt: definition in Enum Types. |
| record struct | record_struct | src/types-and-traits.rst | Added a :dt: definition in Struct Types. |
| record struct field | record_struct_field | src/types-and-traits.rst | Added a :dt: definition in Struct Types. |
| record struct pattern | record_struct_pattern | src/patterns.rst | Upgraded the definition to :dt: in Record Struct Patterns. |
| record struct type | record_struct_type | src/types-and-traits.rst | Added a :dt: definition in Struct Types. |
| record struct value | record_struct_value | src/types-and-traits.rst | Added a :dt: definition in Struct Types. |
| recursive type | recursive_type | src/types-and-traits.rst | Upgraded the definition to :dt: in Recursive Types. |
| reference | reference | src/ownership-and-deconstruction.rst | Upgraded the definition to :dt: in References. |
| reference identifier pattern | reference_identifier_pattern | src/patterns.rst | Reworded and upgraded the definition to :dt: in Identifier Patterns. |
| reference pattern | reference_pattern | src/patterns.rst | Upgraded the definition to :dt: in Reference Patterns. |
| reference type | reference_type | src/types-and-traits.rst | Upgraded the definition to :dt: in Reference Types. |
| referent | referent | src/ownership-and-deconstruction.rst | Upgraded the definition to :dt: in References. |
| refutability | refutability | src/patterns.rst | Upgraded the definition to :dt: in Refutability. |
| refutable constant | refutable_constant | src/patterns.rst | Upgraded the definition to :dt: in Refutability. |
| refutable pattern | refutable_pattern | src/patterns.rst | Reworded and upgraded the definition to :dt: in Refutability. |
| refutable type | refutable_type | src/patterns.rst | Added a :dt: definition in Refutability. |
| register | register | src/inline-assembly.rst | Upgraded the definition to :dt: in Registers. |
| register argument | register_argument | src/inline-assembly.rst | Upgraded the definition to :dt: in Register Arguments. |
| register class | register_class | src/inline-assembly.rst | Upgraded the definition to :dt: in Register Classes. |
| register class argument | register_class_argument | src/inline-assembly.rst | Upgraded the definition to :dt: in Register Arguments. |
| register class name | register_class_name | src/inline-assembly.rst | Upgraded the definition to :dt: in Register Classes. |
| register expression | register_expression | src/inline-assembly.rst | Upgraded the definition to :dt: in Register Expressions. |
| register name | register_name | src/inline-assembly.rst | Upgraded the definition to :dt: in Registers. |
| register parameter | register_parameter | src/inline-assembly.rst | Upgraded the definition to :dt: in Register Parameters. |
| register parameter modifier | register_parameter_modifier | src/inline-assembly.rst | Upgraded the definition to :dt: in Register Parameter Modifiers. |
| remainder assignment | remainder_assignment | src/expressions.rst | Added a :dt: definition in Compound Assignment Expressions. |
| remainder assignment expression | remainder_assignment_expression | src/expressions.rst | Upgraded the definition to :dt: in Compound Assignment Expressions. |
| remainder expression | remainder_expression | src/expressions.rst | Upgraded the definition to :dt: in Arithmetic Expressions. |
| renaming | renaming | src/program-structure-and-compilation.rst | Added a :dt: definition in Crate Imports. |
| repeat operand | repeat_operand | src/expressions.rst | Upgraded the definition to :dt: in Array Expressions. |
| repetition operator | repetition_operator | src/macros.rst | Upgraded the definition to :dt: in Macro Repetition. |
| representation modifier | representation_modifier | src/attributes.rst | Added a :dt: definition in Attribute repr rules. |
| reserved keyword | reserved_keyword | src/lexical-elements.rst | Upgraded the definition to :dt: in Keywords. |
| resolution | resolution | src/entities-and-resolution.rst | Upgraded the definition to :dt: in Resolution. |
| rest pattern | rest_pattern | src/patterns.rst | Upgraded the definition to :dt: in Rest Patterns. |
| return expression | return_expression | src/expressions.rst | Upgraded the definition to :dt: in Return Expressions. |
| return type | return_type | src/functions.rst | Upgraded the definition to :dt: in Functions. |
| right operand | right_operand | src/expressions.rst | Upgraded the definition to :dt: in Expressions classification. |
| rule matching | rule_matching | src/macros.rst | Upgraded the definition to :dt: in Rule Matching. |
| rustc | rustc | src/general.rst | Added a :dt: definition in Scope. |
| safety invariant | safety_invariant | src/unsafety.rst | Added definition in Unsafety legality rules to ground invariant references. |
| scalar type | scalar_type | src/types-and-traits.rst | Added definition in Scalar Types to cover bool/char/numeric types. |
| scope | scope | src/entities-and-resolution.rst | Upgraded scope definition in Scopes to :dt:. |
| scope hierarchy | scope_hierarchy | src/entities-and-resolution.rst | Upgraded Scope Hierarchy definition to :dt:. |
| selected field | selected_field | src/expressions.rst | Upgraded Field Access Expressions definition to :dt:. |
| Self | self | src/types-and-traits.rst | Added definition in Traits to cover implicit Self in traits/implementations. |
| self parameter | self_parameter | src/functions.rst | Upgraded self parameter definition to :dt: in Functions. |
| self public modifier | self_public_modifier | src/entities-and-resolution.rst | Upgraded Visibility Modifiers definition to :dt:. |
| Self scope | self_scope | src/entities-and-resolution.rst | Upgraded Self Scope definition to :dt:. |
| send type | send_type | src/concurrency.rst | Upgraded Send and Sync definition to :dt:. |
| separator | separator | src/lexical-elements.rst | Upgraded separator definition in Lexical Elements to :dt:. |
| sequence type | sequence_type | src/types-and-traits.rst | Added definition at start of Sequence Types. |
| shadowing | shadowing | src/entities-and-resolution.rst | Added definition in Entities to describe name hiding. |
| shared borrow | shared_borrow | src/ownership-and-deconstruction.rst | Added definition in Borrowing for immutable borrow results. |
| shared reference | shared_reference | src/ownership-and-deconstruction.rst | Added definition in References for shared reference values. |
| shared reference type | shared_reference_type | src/types-and-traits.rst | Upgraded Reference Types definition to :dt:. |
| shift left assignment | shift_left_assignment | src/expressions.rst | Added definition in Compound Assignment Expressions. |
| shift left assignment expression | shift_left_assignment_expression | src/expressions.rst | Upgraded compound assignment expression definition to :dt:. |
| shift left expression | shift_left_expression | src/expressions.rst | Upgraded bit expression definition to :dt:. |
| shift right assignment | shift_right_assignment | src/expressions.rst | Added definition in Compound Assignment Expressions. |
| shift right assignment expression | shift_right_assignment_expression | src/expressions.rst | Upgraded compound assignment expression definition to :dt:. |
| shift right expression | shift_right_expression | src/expressions.rst | Upgraded bit expression definition to :dt:. |
| shorthand deconstructor | shorthand_deconstructor | src/patterns.rst | Upgraded Record Struct Patterns definition to :dt:. |
| shorthand initializer | shorthand_initializer | src/expressions.rst | Upgraded Struct Expressions definition to :dt:. |
| signed integer type | signed_integer_type | src/types-and-traits.rst | Added definition in Integer Types. |
| simple byte string literal | simple_byte_string_literal | src/lexical-elements.rst | Upgraded Simple Byte String Literals definition to :dt:. |
| simple c string literal | simple_c_string_literal | src/lexical-elements.rst | Upgraded Simple C String Literals definition to :dt:. |
| simple import | simple_import | src/entities-and-resolution.rst | Upgraded Use Imports definition to :dt:. |
| simple path | simple_path | src/entities-and-resolution.rst | Upgraded Paths definition to :dt:. |
| simple path prefix | simple_path_prefix | src/entities-and-resolution.rst | Upgraded Use Imports definition to :dt:. |
| simple path public modifier | simple_path_public_modifier | src/entities-and-resolution.rst | Upgraded Visibility Modifiers definition to :dt:. |
| simple path resolution | simple_path_resolution | src/entities-and-resolution.rst | Upgraded Simple Path Resolution definition to :dt:. |
| simple public modifier | simple_public_modifier | src/entities-and-resolution.rst | Upgraded Visibility Modifiers definition to :dt:. |
| simple register expression | simple_register_expression | src/inline-assembly.rst | Upgraded Register Expressions definition to :dt:. |
| simple string literal | simple_string_literal | src/lexical-elements.rst | Upgraded Simple String Literals definition to :dt:. |
| single segment path | single_segment_path | src/entities-and-resolution.rst | Upgraded Paths definition to :dt:. |
| size | size | src/types-and-traits.rst | Upgraded Type Layout definition to :dt:. |
| size operand | size_operand | src/types-and-traits.rst | Added definition in Array Types. |
| sized type | sized_type | src/types-and-traits.rst | Added definition in Type Layout. |
| slice | slice | src/types-and-traits.rst | Added definition in Slice Types. |
| slice pattern | slice_pattern | src/patterns.rst | Upgraded Slice Patterns definition to :dt:. |
| slice type | slice_type | src/types-and-traits.rst | Upgraded Slice Types definition to :dt:. |
| source file | source_file | src/program-structure-and-compilation.rst | Upgraded Source Files definition to :dt:. |
| statement | statement | src/statements.rst | Added definition in Statements. |
| static | static | src/values.rst | Upgraded Statics definition to :dt:. |
| static initializer | static_initializer | src/values.rst | Upgraded Statics definition to :dt:. |
| static lifetime elision | static_lifetime_elision | src/types-and-traits.rst | Upgraded Lifetime Elision definition to :dt:. |
| str | str | src/types-and-traits.rst | Upgraded Str Type definition to :dt:. |
| strict keyword | strict_keyword | src/lexical-elements.rst | Upgraded Keywords definition to :dt:. |
| string literal | string_literal | src/lexical-elements.rst | Upgraded String Literals definition to :dt:. |
| struct | struct | src/types-and-traits.rst | Added definition in Struct Types. |
| struct expression | struct_expression | src/expressions.rst | Upgraded Struct Expressions definition to :dt:. |
| struct field | struct_field | src/types-and-traits.rst | Added definition in Struct Types. |
| struct pattern | struct_pattern | src/patterns.rst | Upgraded Struct Patterns definition to :dt:. |
| struct type | struct_type | src/types-and-traits.rst | Upgraded Struct Types definition to :dt:. |
| struct value | struct_value | src/types-and-traits.rst | Added definition in Struct Types. |
| subexpression | subexpression | src/expressions.rst | Added definition near expression operands. |
| subject expression | subject_expression | src/expressions.rst | Upgraded expression classification definition to :dt:. |
| subject let expression | subject_let_expression | src/expressions.rst | Upgraded expression classification definition to :dt:. |
| subpattern | subpattern | src/patterns.rst | Upgraded Patterns definition to :dt:. |
| subtraction assignment | subtraction_assignment | src/expressions.rst | Added definition in Compound Assignment Expressions. |
| subtraction assignment expression | subtraction_assignment_expression | src/expressions.rst | Upgraded compound assignment expression definition to :dt:. |
| subtraction expression | subtraction_expression | src/expressions.rst | Upgraded arithmetic expression definition to :dt:. |
| subtrait | subtrait | src/types-and-traits.rst | Upgraded Traits definition to :dt:. |
| subtype | subtype | src/types-and-traits.rst | Added definition in Subtyping requirements. |
| subtyping | subtyping | src/types-and-traits.rst | Added definition in Subtyping requirements. |
| suffixed float | suffixed_float | src/lexical-elements.rst | Upgraded Float Literals definition to :dt:. |
| suffixed integer | suffixed_integer | src/lexical-elements.rst | Upgraded Integer Literals definition to :dt:. |
| super public modifier | super_public_modifier | src/entities-and-resolution.rst | Upgraded Visibility Modifiers definition to :dt:. |
| supertrait | supertrait | src/types-and-traits.rst | Upgraded Traits definition to :dt:. |
| sync type | sync_type | src/concurrency.rst | Upgraded Send and Sync definition to :dt:. |
| syntactic category | syntactic_category | src/general.rst | Added definition in General notation rules. |
| tail expression | tail_expression | src/expressions.rst | Upgraded definition to :dt:. |
| temporary | temporary | src/values.rst | Upgraded definition to :dt:. |
| terminated macro invocation | terminated_macro_invocation | src/macros.rst | Upgraded definition to :dt:. |
| textual macro scope | textual_macro_scope | src/entities-and-resolution.rst | Upgraded definition to :dt:. |
| textual type | textual_type | src/types-and-traits.rst | Added definition as :dt:. |
| thin pointer | thin_pointer | src/types-and-traits.rst | Added definition as :dt:. |
| thin pointer type | thin_pointer_type | src/types-and-traits.rst | Added definition as :dt:. |
| token matching | token_matching | src/macros.rst | Upgraded definition to :dt:. |
| tokens | token | src/macros.rst | Upgraded definition to :dt:. |
| trait | trait | src/types-and-traits.rst | Upgraded definition to :dt:. |
| trait body | trait_body | src/types-and-traits.rst | Upgraded definition to :dt:. |
| trait bound | trait_bound | src/types-and-traits.rst | Upgraded definition to :dt:. |
| trait implementation | trait_implementation | src/implementations.rst | Upgraded definition to :dt:. |
| trait object lifetime elision | trait_object_lifetime_elision | src/types-and-traits.rst | Upgraded definition to :dt:. |
| trait object type | trait_object_type | src/types-and-traits.rst | Upgraded definition to :dt:. |
| trait type | trait_type | src/types-and-traits.rst | Added definition as :dt:. |
| transparent representation | transparent_representation | src/types-and-traits.rst | Upgraded definition to :dt:. |
| trivial predicate | trivial_predicate | src/generics.rst | Upgraded definition to :dt:. |
| tuple | tuple | src/types-and-traits.rst | Added definition as :dt:. |
| tuple enum variant | tuple_enum_variant | src/types-and-traits.rst | Added definition as :dt:. |
| tuple enum variant value | tuple_enum_variant_value | src/types-and-traits.rst | Added definition as :dt:. |
| tuple expression | tuple_expression | src/expressions.rst | Upgraded definition to :dt:. |
| tuple field | tuple_field | src/types-and-traits.rst | Added definition as :dt:. |
| tuple initializer | tuple_initializer | src/expressions.rst | Upgraded definition to :dt:. |
| tuple pattern | tuple_pattern | src/patterns.rst | Upgraded definition to :dt:. |
| tuple struct | tuple_struct | src/types-and-traits.rst | Added definition as :dt:. |
| tuple struct call expression | tuple_struct_call_expression | src/expressions.rst | Upgraded definition to :dt:. |
| tuple struct field | tuple_struct_field | src/types-and-traits.rst | Added definition as :dt:. |
| tuple struct pattern | tuple_struct_pattern | src/patterns.rst | Upgraded definition to :dt:. |
| tuple struct type | tuple_struct_type | src/types-and-traits.rst | Added definition as :dt:. |
| tuple struct value | tuple_struct_value | src/types-and-traits.rst | Added definition as :dt:. |
| tuple type | tuple_type | src/types-and-traits.rst | Upgraded definition to :dt:. |
| type | type | src/types-and-traits.rst | Upgraded definition to :dt:. |
| type alias | type_alias | src/types-and-traits.rst | Upgraded definition to :dt:. |
| type argument | type_argument | src/generics.rst | Upgraded definition to :dt:. |
| type ascription | type_ascription | src/types-and-traits.rst | Added definition as :dt:. |
| type bound predicate | type_bound_predicate | src/generics.rst | Upgraded definition to :dt:. |
| type cast expression | type_cast_expression | src/expressions.rst | Upgraded definition to :dt:. |
| type coercion | type_coercion | src/types-and-traits.rst | Upgraded definition to :dt:. |
| type inference | type_inference | src/types-and-traits.rst | Upgraded definition to :dt:. |
| type inference root | type_inference_root | src/types-and-traits.rst | Upgraded definition to :dt:. |
| type parameter | type_parameter | src/generics.rst | Upgraded definition to :dt:. |
| type parameter initializer | type_parameter_initializer | src/generics.rst | Upgraded definition to :dt:. |
| type parameter type | type_parameter_type | src/types-and-traits.rst | Upgraded definition to :dt:. |
| type path | type_path | src/entities-and-resolution.rst | Upgraded definition to :dt:. |
| type path resolution | type_path_resolution | src/entities-and-resolution.rst | Upgraded definition to :dt:. |
| type representation | type_representation | src/types-and-traits.rst | Upgraded definition to :dt:. |
| type specification | type_specification | src/types-and-traits.rst | Added definition as :dt:. |
| type unification | type_unification | src/types-and-traits.rst | Upgraded definition to :dt:. |
| type variable | type_variable | src/types-and-traits.rst | Upgraded definition to :dt:. |
| validity invariant | validity_invariant | src/unsafety.rst | Added definition alongside safety invariant in Unsafety. |
| value | value | src/values.rst | Upgraded Values legality rule definition to :dt:. |
| value expression | value_expression | src/expressions.rst | Upgraded Value Expressions definition to :dt:. |
| value expression context | value_expression_context | src/expressions.rst | Upgraded Value Expressions context definition to :dt:. |
| value operand | value_operand | src/expressions.rst | Upgraded Assignment Expressions definition to :dt:. |
| variable | variable | src/values.rst | Upgraded Variables definition to :dt:. |
| variadic part | variadic_part | src/types-and-traits.rst | Upgraded Function Pointer Types definition to :dt:. |
| variance | variance | src/types-and-traits.rst | Upgraded Subtyping and Variance definition to :dt:. |
| visibility | visibility | src/entities-and-resolution.rst | Upgraded Visibility definition to :dt:. |
| visibility modifier | visibility_modifier | src/entities-and-resolution.rst | Upgraded Visibility modifier definition to :dt:. |
| visible emptiness | visible_emptiness | src/types-and-traits.rst | Upgraded Visible Emptiness definition to :dt:. |
| visible empty enum variant | visible_empty_enum_variant | src/types-and-traits.rst | Upgraded Visible Emptiness enum variant definition to :dt:. |
| visible empty type | visible_empty_type | src/types-and-traits.rst | Upgraded Visible Emptiness type definition to :dt:. |
