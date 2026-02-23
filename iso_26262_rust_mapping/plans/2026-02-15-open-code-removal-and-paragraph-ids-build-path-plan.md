# OpenCode Removal and Paragraph IDs Build Path Plan

- [x] Confirm all repository references to OpenCode paths/env vars and decide target replacement paths.
- [x] Add a repository-local paragraph IDs schema under `traceability/iso26262/schema/`.
- [x] Update Sphinx extension outputs so `paragraph-ids.json` is written to `build/` (not `build/html/`) and validated against the repo-local schema.
- [x] Remove OpenCode-specific config wiring and report writes from the extension.
- [x] Update `make.py` trace validation to stop reading `OPENCODE_CONFIG_DIR` and validate against the repo-local schema.
- [x] Update docs and ignore rules to reflect the new artifact paths and env-var contract.
- [x] Run the project checks used by CI and confirm no `opencode` references remain in the repository.

## Verification run

- `./make.py validate`
- `./make.py build`
- `SPHINX_MIGRATION_RUN_ROOT=/tmp/sphinx-traceability-run ./make.py trace-validate`
- `uvx black . --check --diff --color`
- `uvx flake8 . --exclude .venv`
- repo-wide search for `OPENCODE_CONFIG_DIR|opencode` and old paragraph schema paths returned no matches
