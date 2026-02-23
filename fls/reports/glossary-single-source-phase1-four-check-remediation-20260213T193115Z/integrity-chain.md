# Four-Check Integrity Chain

- run_id: `20260213T193115Z`
- branch: `glossary-single-source-phase1-repack-upstream-main`
- upstream_main_pin: `fb8a46795eda1f1db5e3232002fd94a270bfbffd`
- old_capstone_sha: `e86d544b64753e7b3cf45d7f41827fea1804f76c`
- new_capstone_sha: `1132eb4c632c0d1b65bc7000d9bced2fca3842bd`

## Verification Commands

1. `./tools/verify-html-diff.py --mode refs --left-ref fb8a46795eda1f1db5e3232002fd94a270bfbffd --right-ref 6716db3a49cfbffa30ccac3a51cf76ebd9ab60a7 --report /home/pete.levasseur/opencode-project-agents/fls/reports/glossary-single-source-phase1-four-check-remediation-20260213T193115Z/artifacts/diff-upstream-main-vs-commit3.txt`
2. `./tools/verify-html-diff.py --mode refs --left-ref 6716db3a49cfbffa30ccac3a51cf76ebd9ab60a7 --right-ref 1132eb4c632c0d1b65bc7000d9bced2fca3842bd --report /home/pete.levasseur/opencode-project-agents/fls/reports/glossary-single-source-phase1-four-check-remediation-20260213T193115Z/artifacts/diff-commit3-vs-commit4.txt`
3. `./tools/verify-html-diff.py --mode refs --left-ref fb8a46795eda1f1db5e3232002fd94a270bfbffd --right-ref 1132eb4c632c0d1b65bc7000d9bced2fca3842bd --report /home/pete.levasseur/opencode-project-agents/fls/reports/glossary-single-source-phase1-four-check-remediation-20260213T193115Z/artifacts/diff-upstream-main-vs-commit4.txt`
4. `./tools/verify-html-diff.py --mode repro --ref 1132eb4c632c0d1b65bc7000d9bced2fca3842bd --report /home/pete.levasseur/opencode-project-agents/fls/reports/glossary-single-source-phase1-four-check-remediation-20260213T193115Z/capstone-repro-commit4.txt`

## Results

- `diff-upstream-main-vs-commit3.txt`: rc=0, result=`result: no differences under configured comparison policy.`
- `diff-commit3-vs-commit4.txt`: rc=0, result=`result: no differences under configured comparison policy.`
- `diff-upstream-main-vs-commit4.txt`: rc=0, result=`result: no differences under configured comparison policy.`
- `capstone-repro-commit4.txt`: rc=0, result=`result: no differences under configured comparison policy.`

## Parity Diagnostics

- `artifacts/chapter-macros-materialized.diff`: empty (0 bytes)
- `artifacts/glossary-term-anchor-map.diff`: empty (0 bytes)
- `artifacts/glossary-term-dp-map.diff`: empty (0 bytes)
- `artifacts/m7-up-vs-c3-provenance.txt`: deterministic M7 debug provenance
