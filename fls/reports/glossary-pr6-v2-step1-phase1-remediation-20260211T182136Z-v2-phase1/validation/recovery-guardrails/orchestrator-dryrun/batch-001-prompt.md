Execute the v2 glossary remediation plan for this wave batch only.

Context:
- Worktree: `/home/pete.levasseur/project/fls-wt/step1`
- Expected branch: `glossary-step-1-main-text-coverage`
- Wave: `WA`
- Plan: `/home/pete.levasseur/opencode-project-agents/fls/plans/glossary-pr6-wave-ab-recovery-guardrails-plan.md`
- Checklist: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails/orchestrator-dryrun/manual-placement-checklist-v2.md`
- Ledger: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails/orchestrator-dryrun/manual-placement-ledger-v2.csv`
- Baseline reference: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails/orchestrator-dryrun/manual-placement-baseline-reference-v2.csv`
- Placement JSON: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails/fixtures/placement.json`
- Divergence JSON: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails/fixtures/divergence.json`
- Reason rubric: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails/orchestrator-dryrun/reason-rubric-v2.md`
- Rationale writer: `/home/pete.levasseur/opencode-project-agents/fls/reports/record-rationale-v2.py`
- Rationale events log: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails/orchestrator-dryrun/reports/rationale-events.jsonl`
- Validator: `/home/pete.levasseur/opencode-project-agents/fls/reports/validate-ledger-and-checklist-v2.py`
- Term lock manifest: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails/orchestrator-dryrun/batch-001-term-lock.json`
- Remediation directory: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails/orchestrator-dryrun`
- Batch number: `1`

Batch scope (exact IDs only): WA-001

Terms:
- WA-001: value

Required workflow:
1. Process each listed term manually, one by one.
2. Apply step1 spec edits as needed.
3. Update only these term rows in checklist and ledger.
4. For each completed term, ensure checklist sub-items `.1`..`.6` are checked.
5. Use rationale writer once per completed term (no direct rationale edits in CSV):
   `python3 "/home/pete.levasseur/opencode-project-agents/fls/reports/record-rationale-v2.py" --checklist-id <ID> --checklist "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails/orchestrator-dryrun/manual-placement-checklist-v2.md" --ledger "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails/orchestrator-dryrun/manual-placement-ledger-v2.csv" --placement-json "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails/fixtures/placement.json" --divergence-json "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails/fixtures/divergence.json" --events-jsonl "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails/orchestrator-dryrun/reports/rationale-events.jsonl" --batch-id "batch-001" --implementer-id <implementer> --action-type <action> --decision-detail <detail> --reason-code <code> --reason-why <text> --semantic-change-flag <flag> --review-attention <attention> --after-file <file> --after-line <line> --after-dp-id <dp> --phase1-status completed --final-quality resolved-high [--deviation-permit <path>]`
6. Ensure ledger fields are complete (`action_type`, `decision_detail`, `reason_*`, `semantic_change_flag`, `review_attention`, after anchors, statuses, rationale UUID metadata).
7. Do not commit or push (orchestrator handles commit).
8. Run validator in progress mode before responding:
   `python3 "/home/pete.levasseur/opencode-project-agents/fls/reports/validate-ledger-and-checklist-v2.py" --mode progress --checklist "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails/orchestrator-dryrun/manual-placement-checklist-v2.md" --ledger "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails/orchestrator-dryrun/manual-placement-ledger-v2.csv" --baseline "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails/orchestrator-dryrun/manual-placement-baseline-reference-v2.csv" --recovery-guardrails --events-jsonl "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails/orchestrator-dryrun/reports/rationale-events.jsonl" --json-out "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails/orchestrator-dryrun/batch-001-validate-progress.json" --markdown-out "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails/orchestrator-dryrun/checklist-progress.md"`

Response format:
- Completed IDs
- Quarantined IDs (if any)
- Files changed
- Any blockers (if none, say "none")
