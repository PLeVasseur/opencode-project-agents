# Phase 2 exit codes

| command | exit code | notes |
| --- | --- | --- |
| `uv run ./tools/glossary-migration-check.py --phase 2 --strict --report "$REPORT_ROOT/glossary-phase2-check.json"` | 0 | Final rerun after mismatch harmonization |
| `./make.py --clear` | 0 | Clean build passed |
| `./make.py --check-links` | 0 | Link checker passed |
