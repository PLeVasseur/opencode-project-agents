# Phase 3 notes

- [x] Record canonical-target ownership decisions.
  - Replaced glossary `:dt:` roles with `:t:` roles so canonical term ownership moves to chapter documents.
  - Extended target validation to accept chapter-owned `code_terms` entries for code-like glossary terms.
- [x] Record blockers and remediations.
  - Blocker: initial strict run reported canonical-target failures for terms inferred only from heading text.
  - Remediation: infer glossary-term IDs from matching `:t:` references when `:dt:` is absent; rerun strict checks to green.
- [x] Link evidence artifacts.
  - `phase3-dt-main-only/glossary-phase3-check.json`
  - `phase3-dt-main-only/term-target-validation.json`
  - `phase3-dt-main-only/make-clear.log`
  - `phase3-dt-main-only/make-check-links.log`
