# Phase 3 exit codes

| command | exit code | notes |
| --- | --- | --- |
| `uv run ./tools/glossary-migration-check.py --phase 3 --strict --report "$REPORT_ROOT/glossary-phase3-check.json"` | 0 | Final rerun after canonical-target inference update |
| `./make.py --clear` | 0 | Clean build passed |
| `./make.py --check-links` | 0 | Link checker passed |
