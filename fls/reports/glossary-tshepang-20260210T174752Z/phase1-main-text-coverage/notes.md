# Phase 1 notes

- [x] Record placement decisions and tie-break rationale.
  - Imported donor wave edits (`c13b26a`..`d77ab3c`) to seed chapter-side term definitions.
  - Added missing chapter definitions for `code point`, `plane`, `constrain`, `implementation coherence`, `fundamental`, `unify`, `unifiable type`, `structurally equal`, `object safe`, and `terminated` at the first normative chapter locations.
- [x] Record blockers and remediations.
  - Blocker: two cherry-pick conflicts (`src/values.rst`, `src/entities-and-resolution.rst`) while replaying donor checkpoints.
  - Remediation: resolved both conflicts with the donor-final versions from `d77ab3c`, then resumed import.
- [x] Link evidence artifacts.
  - `phase1-main-text-coverage/glossary-phase1-check.json`
  - `phase1-main-text-coverage/term-inventory.json`
  - `phase1-main-text-coverage/missing-terms.json`
  - `phase1-main-text-coverage/non-obvious-placement-rationale.md`
  - `phase1-main-text-coverage/non-obvious-placement-context.md`
  - `phase1-main-text-coverage/make-clear.log`
  - `phase1-main-text-coverage/make-check-links.log`
