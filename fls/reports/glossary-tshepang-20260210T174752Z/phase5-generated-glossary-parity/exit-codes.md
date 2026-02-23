# Phase 5 exit codes

| command | exit code | notes |
| --- | --- | --- |
| `./generate-glossary.py --help` | 0 | Entry-point availability check passed |
| `uv run ./tools/glossary-migration-check.py --phase 5 --strict --report "$REPORT_ROOT/glossary-phase5-check.json"` | 0 | Phase-5 strict checks passed after generator role-conversion fix |
| `./make.py --clear` | 0 | Clean build passed |
| `./make.py --check-links` | 0 | Link checker passed |
| `./generate-glossary.py && diff -u build/generated.glossary.rst src/glossary.rst.inc` | 0 | CI-equivalent glossary parity succeeded |
