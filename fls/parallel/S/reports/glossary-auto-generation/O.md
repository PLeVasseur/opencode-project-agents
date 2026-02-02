# Glossary audit O

## Per-letter checklist
- Letter: O
- [x] Reconcile O terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate O terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for O
- [x] Update `migration-checklist.md` for all O terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint O migration`
- [x] Letter complete

## Term checklist
- [x] object safe (object_safe)
- [x] object safety (object_safety)
- [x] obsolete range pattern (obsolete_range_pattern)
- [x] octal literal (octal_literal)
- [x] operand (operand)
- [x] operator expression (operator_expression)
- [x] opt-out trait bound (opt_out_trait_bound)
- [x] or-pattern (or_pattern)
- [x] outer attribute (outer_attribute)
- [x] outer block doc (outer_block_doc)
- [x] outer doc comment (outer_doc_comment)
- [x] outer line doc (outer_line_doc)
- [x] outline module (outline_module)
- [x] outlives bound (outlives_bound)
- [x] output register (output_register)
- [x] output register expression (output_register_expression)
- [x] overlap (overlap)
- [x] owner (owner)
- [x] ownership (ownership)

## object safe (object_safe)
- placement: `src/types-and-traits.rst`
- action: already defined as `:dt:` in Trait Object Types.
- rationale: Trait object type legality rules define object safety for traits.

## object safety (object_safety)
- placement: `src/types-and-traits.rst`
- action: added a `:dt:` definition in Object Safety.
- rationale: Object Safety rules define the trait object suitability process.

## obsolete range pattern (obsolete_range_pattern)
- placement: `src/patterns.rst`
- action: upgraded definition to `:dt:` in Range Patterns.
- rationale: Pattern syntax and semantics are defined in Patterns.

## octal literal (octal_literal)
- placement: `src/lexical-elements.rst`
- action: upgraded definition to `:dt:` in Numeric Literals.
- rationale: Literal bases are defined in Lexical Elements.

## operand (operand)
- placement: `src/expressions.rst`
- action: upgraded definition to `:dt:` in expression classification.
- rationale: Operands are defined as nested expressions in Expressions.

## operator expression (operator_expression)
- placement: `src/expressions.rst`
- action: upgraded definition to `:dt:` in Operator Expressions.
- rationale: Operator expression semantics live in Expressions.

## opt-out trait bound (opt_out_trait_bound)
- placement: `src/types-and-traits.rst`
- action: upgraded definition to `:dt:` in Trait and Lifetime Bounds.
- rationale: Trait bound forms are defined in Types and Traits.

## or-pattern (or_pattern)
- placement: `src/patterns.rst`
- action: upgraded definition to `:dt:` in pattern legality rules.
- rationale: Or-pattern matching rules live in Patterns.

## outer attribute (outer_attribute)
- placement: `src/attributes.rst`
- action: upgraded definition to `:dt:` in Attributes overview.
- rationale: Attribute application rules are defined in Attributes.

## outer block doc (outer_block_doc)
- placement: `src/lexical-elements.rst`
- action: upgraded definition to `:dt:` in Comments.
- rationale: Doc comment forms are defined in Lexical Elements.

## outer doc comment (outer_doc_comment)
- placement: `src/lexical-elements.rst`
- action: upgraded definition to `:dt:` in Comments.
- rationale: Doc comment forms are defined in Lexical Elements.

## outer line doc (outer_line_doc)
- placement: `src/lexical-elements.rst`
- action: upgraded definition to `:dt:` in Comments.
- rationale: Doc comment forms are defined in Lexical Elements.

## outline module (outline_module)
- placement: `src/program-structure-and-compilation.rst`
- action: upgraded definition to `:dt:` in Modules.
- rationale: Module forms are defined in Program Structure and Compilation.

## outlives bound (outlives_bound)
- placement: `src/types-and-traits.rst`
- action: upgraded definition to `:dt:` in Trait and Lifetime Bounds.
- rationale: Lifetime and trait bounds are defined there.

## output register (output_register)
- placement: `src/inline-assembly.rst`
- action: upgraded definition to `:dt:` in Registers.
- rationale: Inline assembly register semantics define output registers.

## output register expression (output_register_expression)
- placement: `src/inline-assembly.rst`
- action: upgraded definition to `:dt:` in Register Expressions.
- rationale: Inline assembly register expression semantics are defined there.

## overlap (overlap)
- placement: `src/values.rst`
- action: already defined as `:dt:` in Values legality rules.
- rationale: Overlap semantics are defined in Values and used by ownership rules.

## owner (owner)
- placement: `src/ownership-and-deconstruction.rst`
- action: upgraded definition to `:dt:` in Ownership.
- rationale: Ownership rules define owner relationships for values.

## ownership (ownership)
- placement: `src/ownership-and-deconstruction.rst`
- action: upgraded definition to `:dt:` in Ownership.
- rationale: Ownership is defined at the start of the Ownership section.
