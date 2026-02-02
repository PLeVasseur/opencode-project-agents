# Glossary audit C

## Per-letter checklist
- Letter: C
- [ ] Reconcile C terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [ ] Migrate C terms into chapters (upgrade/add :dt: definitions)
- [ ] Update `glossary-only-placement.md` entries for C
- [ ] Update `migration-checklist.md` for all C terms
- [ ] Run `./make.py --check-generated-glossary`
- [ ] Update `glossary-coverage-compare.md`
- [ ] Commit: `docs(glossary): checkpoint C migration`
- [ ] Letter complete

## Term checklist
- [x] C (c)
- [x] C representation (c_representation)
- [x] c string literal (c_string_literal)
- [x] Call conformance (call_conformance)
- [x] call expression (call_expression)
- [x] call operand (call_operand)
- [x] call resolution (call_resolution)
- [x] call site hygiene (call_site_hygiene)
- [x] callee type (callee_type)
- [x] capture mode (capture_mode)
- [x] capture target (capture_target)
- [x] capturing (capturing)
- [x] capturing environment (capturing_environment)
- [x] capturing expression (capturing_expression)
- [x] cast (cast)
- [ ] char (char)
- [x] character literal (character_literal)
- [x] closure body (closure_body)
- [x] closure expression (closure_expression)
- [x] closure parameter (closure_parameter)
- [x] closure type (closure_type)
- [x] code point (code_point)
- [x] comment (comment)
- [x] comparison expression (comparison_expression)
- [x] compilation root (compilation_root)
- [x] compound assignment (compound_assignment)
- [x] compound assignment expression (compound_assignment_expression)
- [x] concrete type (concrete_type)
- [x] conditional compilation (conditional_compilation)
- [x] conditionally-compiled source code (conditionally_compiled_source_code)
- [x] configuration predicate (configuration_predicate)
- [x] const block expression (const_block_expression)
- [x] constant (constant)
- [x] constant argument (constant_argument)
- [x] constant context (constant_context)
- [x] constant expression (constant_expression)
- [x] constant function (constant_function)
- [x] constant initializer (constant_initializer)
- [x] constant parameter (constant_parameter)
- [x] constant parameter initializer (constant_parameter_initializer)
- [x] constant promotion (constant_promotion)
- [x] constrain (constrain)
- [x] construct (construct)
- [x] constructee (constructee)
- [x] container operand (container_operand)
- [x] continue expression (continue_expression)
- [x] control flow boundary (control_flow_boundary)
- [x] copy type (copy_type)
- [x] crate (crate)
- [x] crate import (crate_import)
- [x] crate indication (crate_indication)
- [x] crate public modifier (crate_public_modifier)
- [x] crate root (crate_root)
- [x] crate root module (crate_root_module)
- [x] crate type (crate_type)

## C (c)
- Placement: src/ffi.rst
- Action: Added definition paragraph.
- Rationale: FFI ABI section is the normative place that introduces C ABIs and interoperability.

## C representation (c_representation)
- Placement: src/types-and-traits.rst
- Action: Upgraded definition to :dt:.
- Rationale: Type Representation section specifies layout semantics for C representation.

## c string literal (c_string_literal)
- Placement: src/lexical-elements.rst
- Action: Upgraded definition to :dt:.
- Rationale: Lexical elements chapter defines literal forms and their semantics.

## Call conformance (call_conformance)
- Placement: src/expressions.rst
- Action: Added definition paragraph.
- Rationale: Call Expressions section defines ABI requirements for calls.

## call expression (call_expression)
- Placement: src/expressions.rst
- Action: Upgraded definition to :dt:.
- Rationale: Call Expressions section defines the construct and its semantics.

## call operand (call_operand)
- Placement: src/expressions.rst
- Action: Upgraded definition to :dt:.
- Rationale: Call Expressions section defines operands used in calls.

## call resolution (call_resolution)
- Placement: src/entities-and-resolution.rst
- Action: Upgraded definition to :dt:.
- Rationale: Resolution chapter specifies call resolution mechanics.

## call site hygiene (call_site_hygiene)
- Placement: src/macros.rst
- Action: Upgraded definition to :dt:.
- Rationale: Hygiene section defines call-site behavior for macros.

## callee type (callee_type)
- Placement: src/expressions.rst
- Action: Upgraded definition to :dt:.
- Rationale: Call Expressions section defines callee types for invocation.

## capture mode (capture_mode)
- Placement: src/expressions.rst
- Action: Upgraded definition to :dt:.
- Rationale: Capturing section defines capture modes and their selection.

## capture target (capture_target)
- Placement: src/expressions.rst
- Action: Upgraded definition to :dt:.
- Rationale: Capturing section defines which values are captured.

## capturing (capturing)
- Placement: src/expressions.rst
- Action: Upgraded definition to :dt:.
- Rationale: Capturing section defines the capture process.

## capturing environment (capturing_environment)
- Placement: src/expressions.rst
- Action: Upgraded definition to :dt:.
- Rationale: Capturing section defines the environment contents.

## capturing expression (capturing_expression)
- Placement: src/expressions.rst
- Action: Upgraded definition to :dt:.
- Rationale: Capturing section defines which expressions capture.

## cast (cast)
- Placement: src/expressions.rst
- Action: Upgraded definition to :dt:.
- Rationale: Type Cast Expressions section defines casting semantics.

## char (char)
- Placement: src/types-and-traits.rst
- Action: Upgraded definition to :dt:.
- Rationale: Char Type section defines the char type range.

## character literal (character_literal)
- Placement: src/lexical-elements.rst
- Action: Upgraded definition to :dt:.
- Rationale: Character literal rules are defined in lexical elements.

## closure body (closure_body)
- Placement: src/expressions.rst
- Action: Upgraded definition to :dt:.
- Rationale: Closure Expressions section defines closure bodies.

## closure expression (closure_expression)
- Placement: src/expressions.rst
- Action: Upgraded definition to :dt:.
- Rationale: Closure Expressions section defines closure construction.

## closure parameter (closure_parameter)
- Placement: src/expressions.rst
- Action: Upgraded definition to :dt:.
- Rationale: Closure Expressions section defines closure parameters.

## closure type (closure_type)
- Placement: src/types-and-traits.rst
- Action: Upgraded definition to :dt:.
- Rationale: Closure Types section specifies closure type semantics.

## code point (code_point)
- Placement: src/lexical-elements.rst
- Action: No change (already :dt:).
- Rationale: Character set definitions already provide the code point term.

## comment (comment)
- Placement: src/lexical-elements.rst
- Action: Upgraded definition to :dt:.
- Rationale: Comment rules are defined in lexical elements.

## comparison expression (comparison_expression)
- Placement: src/expressions.rst
- Action: Upgraded definition to :dt:.
- Rationale: Comparison Expressions section defines comparison semantics.

## compilation root (compilation_root)
- Placement: src/program-structure-and-compilation.rst
- Action: Upgraded definition to :dt:.
- Rationale: Compilation Roots section defines compilation inputs.

## compound assignment (compound_assignment)
- Placement: src/expressions.rst
- Action: Added definition paragraph.
- Rationale: Compound Assignment Expressions section defines the construct.

## compound assignment expression (compound_assignment_expression)
- Placement: src/expressions.rst
- Action: Upgraded definition to :dt:.
- Rationale: Compound Assignment Expressions section defines expression behavior.

## concrete type (concrete_type)
- Placement: src/types-and-traits.rst
- Action: Added definition paragraph.
- Rationale: Types section is the right place for generic substitution terminology.

## conditional compilation (conditional_compilation)
- Placement: src/program-structure-and-compilation.rst
- Action: Upgraded definition to :dt:.
- Rationale: Conditional Compilation section specifies compilation behavior.

## conditionally-compiled source code (conditionally_compiled_source_code)
- Placement: src/program-structure-and-compilation.rst
- Action: Upgraded definition to :dt:.
- Rationale: Conditional Compilation section defines this source category.

## configuration predicate (configuration_predicate)
- Placement: src/attributes.rst
- Action: Upgraded definition to :dt:.
- Rationale: cfg attribute rules define configuration predicates.

## const block expression (const_block_expression)
- Placement: src/expressions.rst
- Action: Upgraded definition to :dt:.
- Rationale: Const Blocks section defines const block semantics.

## constant (constant)
- Placement: src/values.rst
- Action: Upgraded definition to :dt:.
- Rationale: Constants section defines constant declarations and behavior.

## constant argument (constant_argument)
- Placement: src/generics.rst
- Action: Upgraded definition to :dt:.
- Rationale: Generic Arguments section defines constant arguments.

## constant context (constant_context)
- Placement: src/expressions.rst
- Action: Upgraded definition to :dt:.
- Rationale: Constant Expressions section defines constant contexts.

## constant expression (constant_expression)
- Placement: src/expressions.rst
- Action: Upgraded definition to :dt:.
- Rationale: Constant Expressions section defines evaluable expressions.

## constant function (constant_function)
- Placement: src/functions.rst
- Action: Upgraded definition to :dt:.
- Rationale: Functions section defines const functions.

## constant initializer (constant_initializer)
- Placement: src/values.rst
- Action: Upgraded definition to :dt:.
- Rationale: Constants section defines constant initializers.

## constant parameter (constant_parameter)
- Placement: src/generics.rst
- Action: Upgraded definition to :dt:.
- Rationale: Generics section defines constant parameters.

## constant parameter initializer (constant_parameter_initializer)
- Placement: src/generics.rst
- Action: Upgraded definition to :dt:.
- Rationale: Generics section defines constant parameter defaults.

## constant promotion (constant_promotion)
- Placement: src/values.rst
- Action: Upgraded definition to :dt:.
- Rationale: Constant Promotion section specifies the promotion rules.

## constrain (constrain)
- Placement: src/generics.rst
- Action: No change (already :dt:).
- Rationale: Constrain definition already lives in Generics.

## construct (construct)
- Placement: src/entities-and-resolution.rst
- Action: Added definition paragraph.
- Rationale: Entities chapter introduces the core construct terminology used throughout.

## constructee (constructee)
- Placement: src/expressions.rst
- Action: Upgraded definition to :dt:.
- Rationale: Struct Expressions section defines constructees.

## container operand (container_operand)
- Placement: src/expressions.rst
- Action: Upgraded definition to :dt:.
- Rationale: Field Access Expressions section defines container operands.

## continue expression (continue_expression)
- Placement: src/expressions.rst
- Action: Added definition paragraph.
- Rationale: Continue Expressions section defines the construct.

## control flow boundary (control_flow_boundary)
- Placement: src/expressions.rst
- Action: Added definition paragraph.
- Rationale: Async Blocks introduces control flow boundary terminology used by returns.

## copy type (copy_type)
- Placement: src/ownership-and-deconstruction.rst
- Action: Upgraded definition to :dt:.
- Rationale: Passing Conventions section defines copy types.

## crate (crate)
- Placement: src/program-structure-and-compilation.rst
- Action: Upgraded definition to :dt:.
- Rationale: Crates section defines compilation units.

## crate import (crate_import)
- Placement: src/program-structure-and-compilation.rst
- Action: Upgraded definition to :dt:.
- Rationale: Crate Imports section defines extern crate usage.

## crate indication (crate_indication)
- Placement: src/program-structure-and-compilation.rst
- Action: Upgraded definition to :dt:.
- Rationale: Crate Imports section defines crate indications.

## crate public modifier (crate_public_modifier)
- Placement: src/entities-and-resolution.rst
- Action: Upgraded definition to :dt:.
- Rationale: Visibility modifiers define crate-limited visibility.

## crate root (crate_root)
- Placement: src/program-structure-and-compilation.rst
- Action: Added definition paragraph.
- Rationale: Compilation Roots section is where crate root modules are defined.

## crate root module (crate_root_module)
- Placement: src/program-structure-and-compilation.rst
- Action: Upgraded definition to :dt:.
- Rationale: Compilation Roots section defines the root module.

## crate type (crate_type)
- Placement: src/program-structure-and-compilation.rst
- Action: Upgraded definition to :dt:.
- Rationale: Crates section defines crate types and their meanings.
