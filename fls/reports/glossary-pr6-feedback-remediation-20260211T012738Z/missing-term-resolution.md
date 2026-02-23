# PR6 missing-term resolution

All `missing_from_chapter` terms from feedback are now resolved in chapter definitions.

| term | chapter location | chosen wording | rationale |
|---|---|---|---|
| `casting` | `src/expressions.rst:2185` | `A :dt:`cast` or :dt:`casting` is the process of changing the :t:`type` of an :t:`expression`.` | Preserves glossary co-definition and keeps alias at first normative cast definition site. |
| `namespace qualifier` | `src/entities-and-resolution.rst:302` | `A :dt:`path` is a sequence of :t:`[path segment]s` logically separated by :dt:`namespace qualifier` ``::`` that resolves to an :t:`entity`.` | Promotes first in-chapter normative use from reference role to chapter definition with unchanged semantics. |
| `shadowed` | `src/entities-and-resolution.rst:41` | `:dt:`shadowing` is a property of :t:`[name]s`. A :t:`name` is :dt:`shadowed` when ...` | Keeps alias tied to canonical `shadowing` concept in its primary definition paragraph. |

Verification source: `post-tooling-phase1-check.json` + term inventory evidence in `coverage-accounting-regression.md`.
