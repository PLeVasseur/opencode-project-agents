# Glossary audit W

## Per-letter checklist
- Letter: W
- [x] Reconcile W terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate W terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for W
- [x] Update `migration-checklist.md` for all W terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint W migration`
- [x] Letter complete

## Term checklist
- [x] weak keyword (weak_keyword)
- [x] where clause (where_clause)
- [x] where clause predicate (where_clause_predicate)
- [x] while let loop (while_let_loop)
- [x] while let loop expression (while_let_loop_expression)
- [x] while loop (while_loop)
- [x] while loop expression (while_loop_expression)
- [x] whitespace string (whitespace_string)

## weak keyword (weak_keyword)
- placement: src/lexical-elements.rst (Weak Keywords)
- action: upgraded the legality rules definition to :dt:
- rationale: weak keyword meaning is defined in lexical elements

## where clause (where_clause)
- placement: src/generics.rst (Where Clauses)
- action: upgraded the definition sentence to :dt:
- rationale: where clause semantics are defined in generics

## where clause predicate (where_clause_predicate)
- placement: src/generics.rst (Where Clauses)
- action: upgraded the definition sentence to :dt:
- rationale: predicates are defined in the where clause grammar and rules

## while let loop (while_let_loop)
- placement: src/expressions.rst (While Let Loops)
- action: added a :dt: sentence tying the term to the loop expression
- rationale: loop form is specified in expressions

## while let loop expression (while_let_loop_expression)
- placement: src/expressions.rst (While Let Loops)
- action: upgraded the definition sentence to :dt:
- rationale: expression semantics are defined in expressions

## while loop (while_loop)
- placement: src/expressions.rst (While Loops)
- action: added a :dt: sentence tying the term to the loop expression
- rationale: loop form is specified in expressions

## while loop expression (while_loop_expression)
- placement: src/expressions.rst (While Loops)
- action: upgraded the definition sentence to :dt:
- rationale: expression semantics are defined in expressions

## whitespace string (whitespace_string)
- placement: src/lexical-elements.rst (Character Set)
- action: upgraded the definition sentence to :dt:
- rationale: whitespace classification is defined in lexical elements
