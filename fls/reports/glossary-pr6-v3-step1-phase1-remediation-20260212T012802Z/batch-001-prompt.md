Execute the v3 glossary remediation plan for this wave batch only.

Context:
- Worktree: `/home/pete.levasseur/project/fls-wt/step1`
- Expected branch: `glossary-step-1-main-text-coverage`
- Wave: `WA`
- Plan: `/home/pete.levasseur/opencode-project-agents/fls/plans/glossary-pr6-wave-ab-recovery-guardrails-v3-plan.md`
- Checklist: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T012802Z/manual-placement-checklist-v3.md`
- Ledger: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T012802Z/manual-placement-ledger-v3.csv`
- Baseline reference: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T012802Z/manual-placement-baseline-reference-v3.csv`
- Placement JSON: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/inputs/fls-pr6-placement-fitness-v2.json`
- Divergence JSON: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/inputs/fls-pr6-definition-divergence-v2.json`
- Reason rubric: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T012802Z/reason-rubric-v3.md`
- Rationale writer: `/home/pete.levasseur/opencode-project-agents/fls/reports/record-rationale-v3.py`
- Rationale analyzer: `/home/pete.levasseur/opencode-project-agents/fls/reports/analyze-rationale-patterns-v3.py`
- Rationale events log: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T012802Z/reports/rationale-events.jsonl`
- Validator: `/home/pete.levasseur/opencode-project-agents/fls/reports/validate-ledger-and-checklist-v3.py`
- Term lock manifest: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T012802Z/batch-001-term-lock.json`
- Remediation directory: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T012802Z`
- Batch number: `1`

Batch scope (exact IDs only): WA-001, WA-002, WA-003, WA-004, WA-005, WA-006, WA-007, WA-008, WA-009, WA-010, WA-011, WA-012, WA-013, WA-014, WA-015

Terms:
- WA-001: value
- WA-002: expression
- WA-003: type
- WA-004: trait
- WA-005: construct
- WA-006: entity
- WA-007: name
- WA-008: item
- WA-009: field
- WA-010: reference
- WA-011: implementation
- WA-012: method
- WA-013: crate
- WA-014: module
- WA-015: statement

ROLE LOCK (MANDATORY):
- YOU ARE THE IMPLEMENTER.
- YOU ARE NOT THE REVIEWER.
- DO NOT RUN `approve-deviation.py`.
- IF A DEVIATION IS NEEDED: FILE THE PERMIT, THEN STOP AND HAND OFF TO REVIEWER.
- ANY SELF-APPROVAL IS A POLICY VIOLATION.

Required workflow:
1. Process each listed term manually, one by one.
2. Apply step1 spec edits as needed.
3. Update only these term rows in checklist and ledger.
4. For each completed term, ensure checklist sub-items `.1`..`.6` are checked.
5. Use rationale writer once per completed term (no direct rationale edits in CSV):
   `python3 "/home/pete.levasseur/opencode-project-agents/fls/reports/record-rationale-v3.py" --checklist-id <ID> --checklist "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T012802Z/manual-placement-checklist-v3.md" --ledger "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T012802Z/manual-placement-ledger-v3.csv" --placement-json "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/inputs/fls-pr6-placement-fitness-v2.json" --divergence-json "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/inputs/fls-pr6-definition-divergence-v2.json" --events-jsonl "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T012802Z/reports/rationale-events.jsonl" --batch-id "batch-001" --implementer-id <implementer> --action-type <action> --decision-detail <detail> --reason-code <code> --reason-why <text> --semantic-change-flag <flag> --review-attention <attention> --after-file <file> --after-line <line> --after-dp-id <dp> --after-section <section> --phase1-status completed --final-quality resolved-high [--deviation-permit <path>]`
6. Ensure ledger fields are complete (`action_type`, `decision_detail`, `reason_*`, `semantic_change_flag`, `review_attention`, after anchors, statuses, rationale UUID metadata).
7. Do not commit or push (orchestrator handles commit).
8. Run validator in progress mode before responding:
   `python3 "/home/pete.levasseur/opencode-project-agents/fls/reports/validate-ledger-and-checklist-v3.py" --mode progress --checklist "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T012802Z/manual-placement-checklist-v3.md" --ledger "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T012802Z/manual-placement-ledger-v3.csv" --baseline "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T012802Z/manual-placement-baseline-reference-v3.csv" --recovery-guardrails --events-jsonl "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T012802Z/reports/rationale-events.jsonl" --json-out "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T012802Z/batch-001-validate-progress.json" --markdown-out "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T012802Z/checklist-progress.md"`
9. Run rationale analyzer and keep artifacts current:
   `python3 "/home/pete.levasseur/opencode-project-agents/fls/reports/analyze-rationale-patterns-v3.py" --ledger "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T012802Z/manual-placement-ledger-v3.csv" --json-out "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T012802Z/batch-001-rationale-patterns.json" --markdown-out "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T012802Z/batch-001-rationale-patterns.md"`

Response format:
- Completed IDs
- Quarantined IDs (if any)
- Files changed
- Any blockers (if none, say "none")
