# Feedback baseline reconciliation

- Run ID: `20260211T012738Z`
- Feedback bundle commit (`term_reliability.json`): `1c2c2b73313fb48987ed02ac044ff68cec69968e`
- Current `glossary-step-1-main-text-coverage` head: `1c2c2b73313fb48987ed02ac044ff68cec69968e`
- Current `glossary-step-2-align-duplicate-text` head: `9005a21f6ca30120ec15435e37acd345834fe2a2`
- Snapshot staleness vs step1: `same`

## PR stack mapping

- Expected PR IDs: `6,7,8,9,10`
- Discovered PR IDs by head branch: `6,7,8,9,10`
- Divergence: none (expected and discovered stack IDs match)

## Metric reconciliation

| Metric | Feedback snapshot count | Current strict output / recompute | Reconciliation note |
|---|---:|---:|---|
| missing | 3 | 0 (`post-tooling-phase1-check.json`) | Missing set is now closed on step1 after tooling + chapter definition fixes. |
| low | 68 | 0 direct low bucket in strict checker | Current strict checker reports aggregate mismatch artifacts; baseline phase2 mismatch artifact contains only 2 role-only differences (no semantic low-confidence wording mismatches). |
| moderate | 49 | 0 direct moderate bucket in strict checker | Moderate bucket is not emitted by strict checker JSON; only 2 role-only mismatches were present at baseline. |
| chapter_only | 183 | 176 (recomputed from current glossary/chapter term-id sets) | Difference reflects current branch state and inventory normalization; chapter-only is advisory in phase1/phase2 strict checks. |

## Mismatch driver notes

- `baseline-phase2-check.json` reported `mismatch_count=2`.
- `mismatch-report.json` classifications were both `role-only` (`scope`, `in scope`), indicating role-tag divergence rather than semantic wording drift.
- Feedback files remain authoritative for triage provenance, but disposition decisions in this run are grounded in current branch outputs and recorded artifacts.
