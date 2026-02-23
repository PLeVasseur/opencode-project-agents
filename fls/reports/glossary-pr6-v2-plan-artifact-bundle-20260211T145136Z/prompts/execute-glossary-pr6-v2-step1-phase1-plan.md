Execute this plan in execute mode (not plan mode):
`$OPENCODE_CONFIG_DIR/planss/glossary-pr6-v2-step1-phase1-remediation-plan.md`

Requirements:
- Work in `/home/pete.levasseur/project/fls-wt/step1` on branch `glossary-step-1-main-text-coverage`.
- Do not push.
- Execute through Wave A, Wave B, and Gate B+ boundary.
- If Gate B+ is blocked on external v3 artifacts, stop cleanly and report blocked.

Reviewer handoff package:
- Build `$REMEDIATION_DIR/reviewer-bundle/`.
- Include all required artifacts (inputs, policy, wave term lists, checklist/ledger, batch summaries, validation outputs, logs, commit manifest, summary report).
- Add reviewer index file listing each artifact and purpose.
- Create a zip archive: `$REMEDIATION_DIR/reviewer-bundle.zip`.
- Return exact paths and sha256 for the zip.

Return:
- Run directory and gate outcomes.
- Wave A/B completion status and commit ranges.
- Gate B+ status and any blockers.
- Reviewer bundle path and `sha256`.
