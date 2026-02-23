Execute the v3 glossary remediation plan for this wave batch only.

Context:
- Worktree: `/home/pete.levasseur/project/fls`
- Expected branch: `glossary-single-source-phase1`
- Wave: `WA`
- Plan: `/home/pete.levasseur/opencode-project-agents/fls/plans/glossary-pr6-wave-ab-recovery-guardrails-v3-plan.md`
- Checklist: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/orchestrator-dryrun-v3/manual-placement-checklist-v3.md`
- Ledger: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/orchestrator-dryrun-v3/manual-placement-ledger-v3.csv`
- Baseline reference: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/orchestrator-dryrun-v3/manual-placement-baseline-reference-v3.csv`
- Placement JSON: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/fixtures/placement-v3.json`
- Divergence JSON: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/fixtures/divergence-v3.json`
- Reason rubric: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/orchestrator-dryrun-v3/reason-rubric-v3.md`
- Rationale writer: `/home/pete.levasseur/opencode-project-agents/fls/reports/record-rationale-v3.py`
- Rationale analyzer: `/home/pete.levasseur/opencode-project-agents/fls/reports/analyze-rationale-patterns-v3.py`
- Rationale events log: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/orchestrator-dryrun-v3/reports/rationale-events.jsonl`
- Validator: `/home/pete.levasseur/opencode-project-agents/fls/reports/validate-ledger-and-checklist-v3.py`
- Term lock manifest: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/orchestrator-dryrun-v3/batch-001-term-lock.json`
- Remediation directory: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/orchestrator-dryrun-v3`
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
   `python3 "/home/pete.levasseur/opencode-project-agents/fls/reports/record-rationale-v3.py" --checklist-id <ID> --checklist "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/orchestrator-dryrun-v3/manual-placement-checklist-v3.md" --ledger "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/orchestrator-dryrun-v3/manual-placement-ledger-v3.csv" --placement-json "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/fixtures/placement-v3.json" --divergence-json "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/fixtures/divergence-v3.json" --events-jsonl "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/orchestrator-dryrun-v3/reports/rationale-events.jsonl" --batch-id "batch-001" --implementer-id <implementer> --action-type <action> --decision-detail <detail> --reason-code <code> --reason-why <text> --semantic-change-flag <flag> --review-attention <attention> --after-file <file> --after-line <line> --after-dp-id <dp> --phase1-status completed --final-quality resolved-high [--deviation-permit <path>]`
6. Ensure ledger fields are complete (`action_type`, `decision_detail`, `reason_*`, `semantic_change_flag`, `review_attention`, after anchors, statuses, rationale UUID metadata).
7. Do not commit or push (orchestrator handles commit).
8. Run validator in progress mode before responding:
   `python3 "/home/pete.levasseur/opencode-project-agents/fls/reports/validate-ledger-and-checklist-v3.py" --mode progress --checklist "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/orchestrator-dryrun-v3/manual-placement-checklist-v3.md" --ledger "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/orchestrator-dryrun-v3/manual-placement-ledger-v3.csv" --baseline "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/orchestrator-dryrun-v3/manual-placement-baseline-reference-v3.csv" --recovery-guardrails --events-jsonl "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/orchestrator-dryrun-v3/reports/rationale-events.jsonl" --json-out "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/orchestrator-dryrun-v3/batch-001-validate-progress.json" --markdown-out "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/orchestrator-dryrun-v3/checklist-progress.md"`
9. Run rationale analyzer and keep artifacts current:
   `python3 "/home/pete.levasseur/opencode-project-agents/fls/reports/analyze-rationale-patterns-v3.py" --ledger "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/orchestrator-dryrun-v3/manual-placement-ledger-v3.csv" --json-out "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/orchestrator-dryrun-v3/batch-001-rationale-patterns.json" --markdown-out "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1/validation/recovery-guardrails-v3/orchestrator-dryrun-v3/batch-001-rationale-patterns.md"`

Response format:
- Completed IDs
- Quarantined IDs (if any)
- Files changed
- Any blockers (if none, say "none")
