# Glossary audit Q

## Per-letter checklist
- Letter: Q
- [x] Reconcile Q terms against `$OPENCODE_CONFIG_DIR/legacy/src/glossary.rst`
- [x] Migrate Q terms into chapters (upgrade/add :dt: definitions)
- [x] Update `glossary-only-placement.md` entries for Q
- [x] Update `migration-checklist.md` for all Q terms
- [x] Run `./make.py --check-generated-glossary`
- [x] Update `glossary-coverage-compare.md`
- [x] Commit: `docs(glossary): checkpoint Q migration`
- [x] Letter complete

## Term checklist
- [x] qualified path expression (qualified_path_expression)
- [x] qualified type (qualified_type)
- [x] qualified type path (qualified_type_path)
- [x] qualifying trait (qualifying_trait)

## qualified path expression (qualified_path_expression)
- placement: `src/entities-and-resolution.rst`
- action: upgraded existing definition to :dt:
- rationale: owning resolution rules for qualified path expressions live in Paths and Resolutions.

## qualified type (qualified_type)
- placement: `src/entities-and-resolution.rst`
- action: upgraded existing definition to :dt:
- rationale: qualified type semantics are defined in the qualified path/type resolution section.

## qualified type path (qualified_type_path)
- placement: `src/entities-and-resolution.rst`
- action: upgraded existing definition to :dt:
- rationale: qualified type path resolution is specified in the same path resolution section.

## qualifying trait (qualifying_trait)
- placement: `src/entities-and-resolution.rst`
- action: upgraded existing definition to :dt:
- rationale: qualifying trait requirements are specified with qualified type resolution rules.
