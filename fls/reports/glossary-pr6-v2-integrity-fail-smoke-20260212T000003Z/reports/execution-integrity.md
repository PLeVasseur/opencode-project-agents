# Execution integrity

- Verdict: `FAILED_INVALID_EXECUTION`
- Start head: `19e75856eac5694e5d613c7c59b429848d333992`
- Wave A end head: `19e75856eac5694e5d613c7c59b429848d333992`
- End head: `19e75856eac5694e5d613c7c59b429848d333992`
- New commit count: `0`
- Has Wave A/B scope: `True`
- Wave A complete: `True`
- Wave B complete: `True`
- Batches completed (current run): `0`
- Batches completed (total): `0`

## Changed src files

- none

## New commits

- none

## Integrity checks

- `new_commit_count > 0`: `False`
- `changed_src_files` non-empty: `False`
- wave completion implies nonzero batches: `False`

## Failures

- new_commit_count == 0
- changed_src_files is empty
- wave A/B marked complete while orchestrator recorded zero completed batches
