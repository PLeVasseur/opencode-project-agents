# Integrity chain (recovery)

- recovery_run_id: `20260213T175028Z`
- old_commit4_sha: `0d81919732c5040ace6a2e947e5adaab30e2385f`
- new_commit4_sha: `e86d544b64753e7b3cf45d7f41827fea1804f76c`

## Required gates

- diff-commit3-vs-commit4: exit `0`; result: no differences under configured comparison policy.
- capstone-repro-commit4: exit `0`; result: no differences under configured comparison policy.

## Informational upstream comparisons (non-blocking)

- diff-upstream-main-vs-commit3: exit `1`; result: differences found under configured comparison policy.
- diff-upstream-main-vs-commit4: exit `1`; result: differences found under configured comparison policy.

Upstream comparison differences are informational-only and MUST NOT block recovery finalization.
