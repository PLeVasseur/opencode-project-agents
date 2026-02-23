# Current State Baseline

- run_id: `20260214T184350Z`
- generated_at_utc: `2026-02-14T19:26:12Z`
- repo_root: `/home/pete.levasseur/personal/iso_26262_rust_mapping`
- target_branch: `docs/iso26262-sphinx-traceability-migration-20260214T184350Z`

## Source inventory snapshot
- narrative headings: 60
- narrative paragraph blocks: 101
- narrative list items: 21
- table files: 26
- table rows: 401
- non-empty table cell entries: 2055

## Legacy token baseline
- `{{TABLE:` occurrences: 26
- `{{PAGE_BREAK}}` occurrences: 2
- `{{BLANK}}` occurrences: 25

## Traceability baseline snapshot
- markdown `{dp}` role markers: 0
- markdown `{ts}` role markers: 0
- YAML row `_trace` units: 0
- YAML `cell_trace` units: 0
- `build/html/paragraph-ids.json` exists: False
- latest coverage JSON exists: False
- latest coverage Markdown exists: False
- commit ledger entries: 0

## Existing make.py command behavior
- `make.py --help` exit code: 0
- has `trace-validate`: False
- has `trace-report`: False

```text
usage: make.py [-h] {validate,build,verify} ...

positional arguments:
  {validate,build,verify}
    validate            Validate all table YAML files against their JSON
                        schemas.
    build               Build DOCX from src/ into
                        build/docx/iso26262_rust_mapping_generated.docx.
    verify              Build + compare + render (default 2 pages; requires
                        soffice and pdftoppm).

options:
  -h, --help            show this help message and exit
```

## Artifact references
- `/home/pete.levasseur/opencode-project-agents/iso_26262_rust_mapping/reports/sphinx-traceability-migration-20260214T184350Z/artifacts/baseline/source-statement-inventory.json`
