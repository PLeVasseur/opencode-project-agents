# Phase 2 notes

- [x] Record mismatch-resolution rationale.
  - Used `mismatch-report.json` from strict phase-2 checks as the source of truth.
  - Rewrote glossary definition paragraphs to chapter-paragraph wording while preserving glossary paragraph IDs.
  - Resolved one residual mismatch (`unit struct constant`) caused by a stray trailing colon after `:dp:`.
- [x] Record blockers and remediations.
  - Blocker: initial phase-2 strict check reported 180 mismatches.
  - Remediation: automated paragraph replacement plus one manual cleanup; strict mismatch count returned to zero.
- [x] Link evidence artifacts.
  - `phase2-align-duplicate-text/glossary-phase2-check.json`
  - `phase2-align-duplicate-text/mismatch-report.json`
  - `phase2-align-duplicate-text/make-clear.log`
  - `phase2-align-duplicate-text/make-check-links.log`
