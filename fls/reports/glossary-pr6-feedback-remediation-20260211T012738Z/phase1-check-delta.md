# Phase 1 strict check delta

## Baseline vs post-tooling

| Report | Check | Result | Details |
|---|---|---|---|
| `baseline-phase1-check.json` | `no-disallowed-directives` | pass | Present at baseline; removed by A0 policy decision in this run. |
| `baseline-phase1-check.json` | `glossary-terms-covered-by-chapters` | pass | `missing_count=0` |
| `post-tooling-phase1-check.json` | `glossary-terms-covered-by-chapters` | pass | `missing_count=0` after tooling + chapter-term remediation |

## Corrective iteration captured in this run

- First post-tooling execution exposed two false-missing inventory entries (`tokens`, `unifiable types`) caused by heading-title fallback always being included.
- Tooling was corrected to use heading fallback only when a glossary section has no `:dt:`/`:dc:` definitions.
- Re-run produced green phase1 strict output with full glossary-term coverage.
