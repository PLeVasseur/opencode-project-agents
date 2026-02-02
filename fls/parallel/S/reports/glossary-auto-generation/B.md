# Glossary audit B

## Per-letter checklist
- Letter: B
- [x] Reconcile B terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate B terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for B
- [x] Update `migration-checklist.md` for all B terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint B migration`
- [x] Letter complete

## Term checklist
- [x] base initializer (base_initializer)
- [x] basic assignment (basic_assignment)
- [x] binary crate (binary_crate)
- [x] binary literal (binary_literal)
- [x] binary operator (binary_operator)
- [x] binding (binding)
- [x] binding argument (binding_argument)
- [x] binding bound argument (binding_bound_argument)
- [x] binding mode (binding_mode)
- [x] binding pattern (binding_pattern)
- [x] binding scope (binding_scope)
- [x] bit and assignment (bit_and_assignment)
- [x] bit and assignment expression (bit_and_assignment_expression)
- [x] bit and expression (bit_and_expression)
- [x] bit expression (bit_expression)
- [x] bit or assignment (bit_or_assignment)
- [x] bit or assignment expression (bit_or_assignment_expression)
- [x] bit or expression (bit_or_expression)
- [x] bit xor assignment (bit_xor_assignment)
- [x] bit xor assignment expression (bit_xor_assignment_expression)
- [x] bit xor expression (bit_xor_expression)
- [x] block comment (block_comment)
- [x] block expression (block_expression)
- [x] bool (bool)
- [x] boolean literal (boolean_literal)
- [x] borrow (borrow)
- [x] borrow expression (borrow_expression)
- [x] borrowed (borrowed)
- [x] borrowing (borrowing)
- [x] bound (bound)
- [x] bound pattern (bound_pattern)
- [x] break expression (break_expression)
- [x] break type (break_type)
- [x] break value (break_value)
- [x] built-in attribute (built_in_attribute)
- [x] built-in trait (built_in_trait)
- [x] byte literal (byte_literal)
- [x] byte string literal (byte_string_literal)

## base initializer (base_initializer)
- Placement: `src/expressions.rst` :dp:`fls_uib1ml41mfrn`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Struct expression legality rules define base initializers.

## basic assignment (basic_assignment)
- Placement: `src/expressions.rst` :dp:`fls_uhcodvq75nlr`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Assignment expressions define basic assignment.

## binary crate (binary_crate)
- Placement: `src/program-structure-and-compilation.rst` :dp:`fls_9ub6ks8qrang`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Program structure defines crate types.

## binary literal (binary_literal)
- Placement: `src/lexical-elements.rst` :dp:`fls_nxqncu5yq4eu`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Integer literal definitions cover binary literals.

## binary operator (binary_operator)
- Placement: `src/expressions.rst` :dp:`fls_yOW2wnLPzlPy`
- Action: Added a definition paragraph for binary operators.
- Rationale: Operand rules define binary operator structure.

## binding (binding)
- Placement: `src/patterns.rst` :dp:`fls_vnh9wfrvumdz`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Binding modes define how patterns bind values.

## binding argument (binding_argument)
- Placement: `src/generics.rst` :dp:`fls_9pda3ja0ihks`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Generics define binding arguments for associated types.

## binding bound argument (binding_bound_argument)
- Placement: `src/generics.rst` :dp:`fls_mcUMWsYcxzmZ`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Generics define binding bound arguments for associated types.

## binding mode (binding_mode)
- Placement: `src/patterns.rst` :dp:`fls_u8Yzdc7Xrksg`
- Action: Added a definition paragraph for binding modes.
- Rationale: Binding modes classify how values are captured in patterns.

## binding pattern (binding_pattern)
- Placement: `src/patterns.rst` :dp:`fls_7xby6d1903kw`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Pattern binding rules define binding patterns.

## binding scope (binding_scope)
- Placement: `src/entities-and-resolution.rst` :dp:`fls_ncg9etb3x7k0`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Scopes define binding visibility.

## bit and assignment (bit_and_assignment)
- Placement: `src/expressions.rst` :dp:`fls_H5zoK7zj9NZZ`
- Action: Added a definition paragraph for bit-and assignment.
- Rationale: Compound assignment expressions define `&=`.

## bit and assignment expression (bit_and_assignment_expression)
- Placement: `src/expressions.rst` :dp:`fls_w2hbhb989yr4`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Compound assignment expressions define bit-and assignment.

## bit and expression (bit_and_expression)
- Placement: `src/expressions.rst` :dp:`fls_f6mmva3lbj1i`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Bit expressions define bit-and operations.

## bit expression (bit_expression)
- Placement: `src/expressions.rst` :dp:`fls_3zd59yuywz6l`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Bit expressions define bitwise operator evaluation.

## bit or assignment (bit_or_assignment)
- Placement: `src/expressions.rst` :dp:`fls_JxiaXUUJY7lz`
- Action: Added a definition paragraph for bit-or assignment.
- Rationale: Compound assignment expressions define `|=`.

## bit or assignment expression (bit_or_assignment_expression)
- Placement: `src/expressions.rst` :dp:`fls_ak4g5112jkl`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Compound assignment expressions define bit-or assignment.

## bit or expression (bit_or_expression)
- Placement: `src/expressions.rst` :dp:`fls_3136k1y6x3cu`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Bit expressions define bit-or operations.

## bit xor assignment (bit_xor_assignment)
- Placement: `src/expressions.rst` :dp:`fls_0PENxft8n4Vz`
- Action: Added a definition paragraph for bit-xor assignment.
- Rationale: Compound assignment expressions define `^=`.

## bit xor assignment expression (bit_xor_assignment_expression)
- Placement: `src/expressions.rst` :dp:`fls_lkjwyy78m2vx`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Compound assignment expressions define bit-xor assignment.

## bit xor expression (bit_xor_expression)
- Placement: `src/expressions.rst` :dp:`fls_j7ujcuthga1i`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Bit expressions define bit-xor operations.

## block comment (block_comment)
- Placement: `src/lexical-elements.rst` :dp:`fls_qsbnl11be35s`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Comment forms are defined in lexical elements.

## block expression (block_expression)
- Placement: `src/expressions.rst` :dp:`fls_nf65p0l0v0gr`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Block expressions are defined in expressions.

## bool (bool)
- Placement: `src/types-and-traits.rst` :dp:`fls_h5994su1yft3`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Scalar type definitions include `bool`.

## boolean literal (boolean_literal)
- Placement: `src/lexical-elements.rst` :dp:`fls_1lll64ftupjd`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Literal definitions cover boolean literals.

## borrow (borrow)
- Placement: `src/ownership-and-deconstruction.rst` :dp:`fls_j9kof0px3l7s`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Borrowing section defines borrows as references.

## borrow expression (borrow_expression)
- Placement: `src/expressions.rst` :dp:`fls_nnqfkl228hjx`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Borrow expressions are defined in expressions.

## borrowed (borrowed)
- Placement: `src/ownership-and-deconstruction.rst` :dp:`fls_yL6cMahJUIqO`
- Action: Added a definition paragraph for the borrowed state.
- Rationale: Borrowing rules describe when values are borrowed.

## borrowing (borrowing)
- Placement: `src/ownership-and-deconstruction.rst` :dp:`fls_c02flohk54pc`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Borrowing section defines the process.

## bound (bound)
- Placement: `src/types-and-traits.rst` :dp:`fls_5g508z6c7q5f`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Bounds are defined in the trait and lifetime bounds section.

## bound pattern (bound_pattern)
- Placement: `src/patterns.rst` :dp:`fls_vy9uw586wy0d`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Identifier pattern rules define bound patterns.

## break expression (break_expression)
- Placement: `src/expressions.rst` :dp:`fls_i5ko1t2wbgxe`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Break expressions are defined in loop control flow.

## break type (break_type)
- Placement: `src/expressions.rst` :dp:`fls_1wdybpfldj7q`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Break expressions define break types.

## break value (break_value)
- Placement: `src/expressions.rst` :dp:`fls_bgd7d5q69q0g`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Break expressions define break values.

## built-in attribute (built_in_attribute)
- Placement: `src/attributes.rst` :dp:`fls_92tqo8uas8kd`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Attributes section defines built-in attributes.

## built-in trait (built_in_trait)
- Placement: `src/types-and-traits.rst` :dp:`fls_u2XiDIAk6tQz`
- Action: Added a definition paragraph for built-in traits.
- Rationale: Traits section defines language-defined traits.

## byte literal (byte_literal)
- Placement: `src/lexical-elements.rst` :dp:`fls_q0qwr83frszx`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Literal definitions cover byte literals.

## byte string literal (byte_string_literal)
- Placement: `src/lexical-elements.rst` :dp:`fls_t63zfv5JdUhj`
- Action: Upgraded the definition sentence to `:dt:`.
- Rationale: Literal definitions cover byte string literals.
