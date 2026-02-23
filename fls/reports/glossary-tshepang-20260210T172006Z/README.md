# Glossary Tshepang phase scaffold

Use this scaffold as the starting point for each timestamped execution report root.

## Usage

- `export REPORT_ROOT="$OPENCODE_CONFIG_DIR/reports/glossary-tshepang-$(date -u +%Y%m%dT%H%M%SZ)"`
- `mkdir -p "$REPORT_ROOT"`
- `cp -R "$OPENCODE_CONFIG_DIR/reports/glossary-tshepang-phase-scaffold"/. "$REPORT_ROOT"/`

## Expected structure

- `phase1-main-text-coverage/`
- `phase2-align-duplicate-text/`
- `phase3-dt-main-only/`
- `phase4-remove-see-paragraphs/`
- `phase5-generated-glossary-parity/`

Each phase directory includes:

- `term-wave-checklist.md`
- `artifacts-checklist.md`

Shared files:

- `term-wave-groups.md`

Fill these files during execution and keep all generated logs/reports in the same phase directory.
