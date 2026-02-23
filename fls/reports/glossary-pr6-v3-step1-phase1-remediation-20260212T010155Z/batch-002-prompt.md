Execute the v3 glossary remediation plan for this wave batch only.

Context:
- Worktree: `/home/pete.levasseur/project/fls-wt/step1`
- Expected branch: `glossary-step-1-main-text-coverage`
- Wave: `WB`
- Plan: `/home/pete.levasseur/opencode-project-agents/fls/plans/glossary-pr6-wave-ab-recovery-guardrails-v3-plan.md`
- Checklist: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T010155Z/manual-placement-checklist-v3.md`
- Ledger: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T010155Z/manual-placement-ledger-v3.csv`
- Baseline reference: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T010155Z/manual-placement-baseline-reference-v3.csv`
- Placement JSON: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/inputs/fls-pr6-placement-fitness-v2.json`
- Divergence JSON: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/inputs/fls-pr6-definition-divergence-v2.json`
- Reason rubric: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T010155Z/reason-rubric-v3.md`
- Rationale writer: `/home/pete.levasseur/opencode-project-agents/fls/reports/record-rationale-v3.py`
- Rationale analyzer: `/home/pete.levasseur/opencode-project-agents/fls/reports/analyze-rationale-patterns-v3.py`
- Rationale events log: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T010155Z/reports/rationale-events.jsonl`
- Validator: `/home/pete.levasseur/opencode-project-agents/fls/reports/validate-ledger-and-checklist-v3.py`
- Term lock manifest: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T010155Z/batch-002-term-lock.json`
- Remediation directory: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T010155Z`
- Batch number: `2`

Batch scope (exact IDs only): WB-001, WB-002, WB-003, WB-004, WB-005, WB-006, WB-007, WB-008, WB-009, WB-010, WB-011, WB-012, WB-013, WB-014, WB-015, WB-016, WB-017, WB-018, WB-019, WB-020

Terms:
- WB-001: field list
- WB-002: type specification
- WB-003: concrete type
- WB-004: generic function
- WB-005: variable
- WB-006: container operand
- WB-007: undefined behavior
- WB-008: code point
- WB-009: receiver operand
- WB-010: associated constant
- WB-011: crate root module
- WB-012: associated trait function
- WB-013: size
- WB-014: floating-point type
- WB-015: safety invariant
- WB-016: unit struct
- WB-017: unsafe context
- WB-018: associated trait constant
- WB-019: union value
- WB-020: pattern-without-alternation

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
   `python3 "/home/pete.levasseur/opencode-project-agents/fls/reports/record-rationale-v3.py" --checklist-id <ID> --checklist "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T010155Z/manual-placement-checklist-v3.md" --ledger "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T010155Z/manual-placement-ledger-v3.csv" --placement-json "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/inputs/fls-pr6-placement-fitness-v2.json" --divergence-json "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/inputs/fls-pr6-definition-divergence-v2.json" --events-jsonl "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T010155Z/reports/rationale-events.jsonl" --batch-id "batch-002" --implementer-id <implementer> --action-type <action> --decision-detail <detail> --reason-code <code> --reason-why <text> --semantic-change-flag <flag> --review-attention <attention> --after-file <file> --after-line <line> --after-dp-id <dp> --after-section <section> --phase1-status completed --final-quality resolved-high [--deviation-permit <path>]`
6. Ensure ledger fields are complete (`action_type`, `decision_detail`, `reason_*`, `semantic_change_flag`, `review_attention`, after anchors, statuses, rationale UUID metadata).
7. Do not commit or push (orchestrator handles commit).
8. Run validator in progress mode before responding:
   `python3 "/home/pete.levasseur/opencode-project-agents/fls/reports/validate-ledger-and-checklist-v3.py" --mode progress --checklist "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T010155Z/manual-placement-checklist-v3.md" --ledger "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T010155Z/manual-placement-ledger-v3.csv" --baseline "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T010155Z/manual-placement-baseline-reference-v3.csv" --recovery-guardrails --events-jsonl "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T010155Z/reports/rationale-events.jsonl" --json-out "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T010155Z/batch-002-validate-progress.json" --markdown-out "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T010155Z/checklist-progress.md"`
9. Run rationale analyzer and keep artifacts current:
   `python3 "/home/pete.levasseur/opencode-project-agents/fls/reports/analyze-rationale-patterns-v3.py" --ledger "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T010155Z/manual-placement-ledger-v3.csv" --json-out "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T010155Z/batch-002-rationale-patterns.json" --markdown-out "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T010155Z/batch-002-rationale-patterns.md"`

Response format:
- Completed IDs
- Quarantined IDs (if any)
- Files changed
- Any blockers (if none, say "none")
