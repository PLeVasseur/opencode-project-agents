# Phase 1 exit codes

| command | exit code | notes |
| --- | --- | --- |
| `uv run ./tools/glossary-migration-check.py --phase 1 --strict --report "$REPORT_ROOT/glossary-phase1-check.json"` | 0 | Coverage + directive ban passed |
| `./make.py --clear` | 0 | Clean build passed |
| `./make.py --check-links` | 0 | Link checker passed |
