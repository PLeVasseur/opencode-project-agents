# Integration Validation Summary

## Report root

- REPORT_ROOT: `/home/pete.levasseur/opencode-project-agents/fls/reports/system-abi-variadic-dedupe-base-integration-20260207T042229Z`

## Bootstrap checklist

- `printenv OPENCODE_CONFIG_DIR`: PASS
- `git fetch origin`: PASS
- `uv sync`: PASS
- Metadata recorded (`UTC timestamp`, `repo path`, `current branch`, `HEAD`, `origin/main`, `origin/dedupe-paragraph-ids-mainline`): PASS

## Branch topology and SHAs

- `changelog-assistant-upstream-pr-anchor-on-dedupe`: `02937b55eb7326775a33bbae546eac879c15d387`
- `system-abi-variadic-on-dedupe`: `1d98249e1078b45836a337d18a7df398ca5f72c9`
- `system-abi-variadic-anchor-integration-on-dedupe-20260207T042229Z`: `019b9be9097df14b764d76265e2165218bf9493a`
- Integration branch base SHA (created from ABI-on-dedupe): `1d98249e1078b45836a337d18a7df398ca5f72c9`

## Assistant rebase evidence

- Pre-rebase SHA: `e1f5fcbf7236ac7f86482fccf77b993b917b3121`
- Pre-rebase merge-base with `origin/main`: `eaafc97e1db8f4a3d153db1abe96ececacf1be2c`
- Pre-rebase divergence (`origin/main...HEAD`): `4 6`
- Post-rebase SHA: `02937b55eb7326775a33bbae546eac879c15d387`
- Post-rebase merge-base with dedupe: `0165ee6ad6e7e6a54705458d491810b0481b7df4`
- Post-rebase divergence (`dedupe-paragraph-ids-mainline...HEAD`): `0 6`
- Dedupe ancestor verification: PASS

## ABI rebase evidence

- Pre-rebase SHA: `57b0f04d1fcbc3d4eb11b0a94fa5b89137e343f3`
- Pre-rebase merge-base with `origin/main`: `f1b193f5197f48686bd56fe881633bb62fad7f27`
- Pre-rebase divergence (`origin/main...HEAD`): `0 3`
- Post-rebase SHA: `1d98249e1078b45836a337d18a7df398ca5f72c9`
- Post-rebase merge-base with dedupe: `0165ee6ad6e7e6a54705458d491810b0481b7df4`
- Post-rebase divergence (`dedupe-paragraph-ids-mainline...HEAD`): `0 3`
- Dedupe ancestor verification: PASS

## Cherry-pick manifest and integration stack

- Selected assistant commits: 6 (includes prerequisite introduction commit, anchor-fix commit, and assistant CI commit)
- Required commit inclusion check: PASS
- Cherry-pick conflicts: none
- Old -> new SHA mapping recorded in `integration-stack-manifest.txt`

## Readiness checks

- `tools/changelog_assistant.py` exists: PASS
- Help output includes `--require-anchor`: PASS
- Metadata fields present (`update_action`, `anchored_pr_url`, `anchored_entry_line`, `anchored_entry_index`): PASS
- `uv run python -m py_compile tools/changelog_assistant.py`: PASS

## Validation outcomes

- BASE_REF used for all assistant invocations: `f1b193f5197f48686bd56fe881633bb62fad7f27`
- Release parsed from `version.rst`: `1.93.0`
- Canonical URL baseline top-level count (`anchor-before.txt`): `1`
- Pre-check (`pre-check`): exit `1` (blockers: missing paragraph IDs `fls_H5vkbMFvzrFs`, `fls_I9JaKZelMiby`, `fls_kqdvWGi9cglm`, `fls_t4yeovFm83Wo`)
- First canonical update (`update`): exit `0`, `update_action="replace"`, anchored URL `https://github.com/rust-lang/rust/pull/145954`, line `29`, entry index `2`
- Canonical count after first update (`anchor-after-first.txt`): `1`
- Second canonical update (`update-second`): exit `0`
- Canonical count after second update (`anchor-after-second.txt`): `1`
- Missing URL default (`update-missing-default` with `https://github.com/rust-lang/rust/pull/999999`): exit `0`, `update_action="append"`
- Missing URL strict miss validation (`step7_update_missing_strict` after restoring `src/changelog.rst` to pre-miss state): exit `1` with expected anchor-miss message
- Post-check (`post-check`): exit `0` (warning only: duplicate explicit target name for the inserted title)

## Command ledger

- All captured command outputs/exit codes: `command-exit-codes.tsv`
- Full artifact inventory: `artifact-paths.txt`

## Acceptance criteria

- Both derived branches (`*-on-dedupe`) have `dedupe-paragraph-ids-mainline` as ancestor: PASS
- Integration branch is based on ABI-on-dedupe and contains selected assistant commits in order: PASS
- Canonical URL update reports `update_action="replace"`: PASS
- Canonical URL top-level count remains exactly `1` before/after first/after second: PASS
- Missing URL behavior validated for default append and strict non-zero: PASS
- Final report artifacts are sufficient for fresh-session review: PASS

## Remediation

- No blocking failures remain.
- To avoid ambiguity in future runs, execute strict missing-anchor validation before default append, or reset `src/changelog.rst` between those two checks.
