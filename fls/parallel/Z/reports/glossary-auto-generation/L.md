# Glossary audit L

## Per-letter checklist
- Letter: L
- [x] Reconcile L terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate L terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for L
- [x] Update `migration-checklist.md` for all L terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint L migration`
- [x] Letter complete

## Term checklist
- [x] label (label)
- [x] label indication (label_indication)
- [x] label scope (label_scope)
- [x] layout (layout)
- [x] lazy and expression (lazy_and_expression)
- [x] lazy boolean expression (lazy_boolean_expression)
- [x] lazy or expression (lazy_or_expression)
- [x] left operand (left_operand)
- [x] less-than expression (less_than_expression)
- [x] less-than-or-equals expression (less_than_or_equals_expression)
- [x] let binding (let_binding)
- [x] let initializer (let_initializer)
- [x] let statement (let_statement)
- [x] lexical element (lexical_element)
- [x] library crate (library_crate)
- [x] lifetime (lifetime)
- [x] lifetime argument (lifetime_argument)
- [x] lifetime bound (lifetime_bound)
- [x] lifetime bound predicate (lifetime_bound_predicate)
- [x] lifetime elision (lifetime_elision)
- [x] lifetime parameter (lifetime_parameter)
- [x] lifetime variable (lifetime_variable)
- [x] line (line)
- [x] line comment (line_comment)
- [x] literal (literal)
- [x] literal expression (literal_expression)
- [x] literal pattern (literal_pattern)
- [x] local trait (local_trait)
- [x] local type (local_type)
- [x] local variable (local_variable)
- [x] loop (loop)
- [x] loop body (loop_body)
- [x] loop expression (loop_expression)

## label (label)
- placement: `src/expressions.rst`
- action: added :dt: definition in Loop Expressions
- rationale: label syntax and named loop semantics live in Expressions

## label indication (label_indication)
- placement: `src/expressions.rst`
- action: upgraded definition to :dt:
- rationale: Loop Labels section defines label indication semantics

## label scope (label_scope)
- placement: `src/entities-and-resolution.rst`
- action: upgraded definition to :dt:
- rationale: scope rules are specified in Entities and Resolution

## layout (layout)
- placement: `src/types-and-traits.rst`
- action: added :dt: definition in Type Layout
- rationale: layout is defined alongside alignment/size rules

## lazy and expression (lazy_and_expression)
- placement: `src/expressions.rst`
- action: upgraded definition to :dt:
- rationale: Lazy Boolean Expressions section specifies semantics

## lazy boolean expression (lazy_boolean_expression)
- placement: `src/expressions.rst`
- action: upgraded definition to :dt:
- rationale: Lazy Boolean Expressions section defines the category

## lazy or expression (lazy_or_expression)
- placement: `src/expressions.rst`
- action: upgraded definition to :dt:
- rationale: Lazy Boolean Expressions section specifies semantics

## left operand (left_operand)
- placement: `src/expressions.rst`
- action: upgraded definition to :dt:
- rationale: operand classification lives in Operator Expressions

## less-than expression (less_than_expression)
- placement: `src/expressions.rst`
- action: upgraded definition to :dt:
- rationale: Comparison Expressions define relational operators

## less-than-or-equals expression (less_than_or_equals_expression)
- placement: `src/expressions.rst`
- action: upgraded definition to :dt:
- rationale: Comparison Expressions define relational operators

## let binding (let_binding)
- placement: `src/statements.rst`
- action: added :dt: definition in Let Statements
- rationale: let bindings are introduced by let/if let/while let

## let initializer (let_initializer)
- placement: `src/statements.rst`
- action: upgraded definition to :dt:
- rationale: Let Statements specify initializer semantics

## let statement (let_statement)
- placement: `src/statements.rst`
- action: upgraded definition to :dt:
- rationale: Let Statements are defined in Statements chapter

## lexical element (lexical_element)
- placement: `src/lexical-elements.rst`
- action: upgraded definition to :dt:
- rationale: lexical elements are defined at the start of Lexical Elements

## library crate (library_crate)
- placement: `src/program-structure-and-compilation.rst`
- action: upgraded definition to :dt:
- rationale: crate kinds are specified in Program Structure

## lifetime (lifetime)
- placement: `src/types-and-traits.rst`
- action: upgraded definition to :dt:
- rationale: lifetime syntax and rules are in Types and Traits

## lifetime argument (lifetime_argument)
- placement: `src/generics.rst`
- action: upgraded definition to :dt:
- rationale: Generic Arguments define lifetime arguments

## lifetime bound (lifetime_bound)
- placement: `src/types-and-traits.rst`
- action: upgraded definition to :dt:
- rationale: bounds are defined in Types and Traits

## lifetime bound predicate (lifetime_bound_predicate)
- placement: `src/generics.rst`
- action: upgraded definition to :dt:
- rationale: where-clause predicates are defined in Generics

## lifetime elision (lifetime_elision)
- placement: `src/types-and-traits.rst`
- action: upgraded definition to :dt:
- rationale: elision rules are specified in Lifetime Elision

## lifetime parameter (lifetime_parameter)
- placement: `src/generics.rst`
- action: upgraded definition to :dt:
- rationale: Generic Parameters define lifetime parameters

## lifetime variable (lifetime_variable)
- placement: `src/types-and-traits.rst`
- action: kept existing :dt: definition
- rationale: lifetime variables are defined in Type Inference

## line (line)
- placement: `src/lexical-elements.rst`
- action: upgraded definition to :dt:
- rationale: lines are defined with source file structure

## line comment (line_comment)
- placement: `src/lexical-elements.rst`
- action: upgraded definition to :dt:
- rationale: comment kinds are specified in Lexical Elements

## literal (literal)
- placement: `src/lexical-elements.rst`
- action: upgraded definition to :dt:
- rationale: literals are defined in Lexical Elements

## literal expression (literal_expression)
- placement: `src/expressions.rst`
- action: upgraded definition to :dt:
- rationale: literal expressions are defined in Expressions

## literal pattern (literal_pattern)
- placement: `src/patterns.rst`
- action: upgraded definition to :dt:
- rationale: literal patterns are defined in Patterns

## local trait (local_trait)
- placement: `src/types-and-traits.rst`
- action: upgraded definition to :dt:
- rationale: trait classification lives in Types and Traits

## local type (local_type)
- placement: `src/types-and-traits.rst`
- action: upgraded definition to :dt:
- rationale: type classification lives in Types and Traits

## local variable (local_variable)
- placement: `src/values.rst`
- action: added :dt: definition in Variables
- rationale: variables and their kinds are defined in Values

## loop (loop)
- placement: `src/expressions.rst`
- action: added :dt: definition in Loop Expressions
- rationale: loop is an alias to loop expression in Expressions

## loop body (loop_body)
- placement: `src/expressions.rst`
- action: upgraded definition to :dt:
- rationale: loop body is defined with loop semantics

## loop expression (loop_expression)
- placement: `src/expressions.rst`
- action: upgraded definition to :dt:
- rationale: loop expressions are defined in Expressions
