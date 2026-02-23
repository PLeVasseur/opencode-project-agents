# Phase 4 exit codes

| command | exit code | notes |
| --- | --- | --- |
| `uv run ./tools/glossary-migration-check.py --phase 4 --strict --report "$REPORT_ROOT/glossary-phase4-check.json"` | 0 | Redundant-see detector passed |
| `./make.py --clear` | 0 | Clean build passed |
| `./make.py --check-links` | 0 | Link checker passed |
