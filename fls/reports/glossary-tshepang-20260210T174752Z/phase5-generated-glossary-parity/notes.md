# Phase 5 notes

- [x] Record determinism/parity decisions.
  - Canonical committed artifact: `src/glossary.rst.inc`.
  - Local regeneration path: `./generate-glossary.py`.
  - Parity policy: byte-for-byte (`diff -u build/generated.glossary.rst src/glossary.rst.inc`).
  - Determinism strategy: stable discovery order + natural-sort by term text + hash-derived section/paragraph IDs.
- [x] Record blockers and remediations.
  - Blocker: initial phase-5 strict run detected residual `:dt:` roles in generated glossary doctree.
  - Remediation: generator now rewrites all `:dt:` -> `:t:` and `:dc:` -> `:c:` in output body lines before commit/parity.
- [x] Link evidence artifacts.
  - `phase5-generated-glossary-parity/glossary-phase5-check.json`
  - `phase5-generated-glossary-parity/generate-glossary-help.log`
  - `phase5-generated-glossary-parity/glossary-parity.log`
  - `phase5-generated-glossary-parity/make-clear.log`
  - `phase5-generated-glossary-parity/make-check-links.log`
