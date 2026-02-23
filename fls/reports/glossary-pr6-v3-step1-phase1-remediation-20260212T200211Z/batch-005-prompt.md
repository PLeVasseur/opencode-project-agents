Execute the v3 glossary remediation plan for this wave batch only.

Context:
- Worktree: `/home/pete.levasseur/project/fls-wt/step1`
- Expected branch: `glossary-step-1-main-text-coverage`
- Wave: `WA`
- Plan: `/home/pete.levasseur/opencode-project-agents/fls/plans/glossary-pr6-wave-ab-recovery-guardrails-v3-plan.md`
- Checklist: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T200211Z/manual-placement-checklist-v3.md`
- Ledger: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T200211Z/manual-placement-ledger-v3.csv`
- Baseline reference: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T200211Z/manual-placement-baseline-reference-v3.csv`
- Placement JSON: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/fls-pr6-placement-fitness-v2.json`
- Divergence JSON: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/fls-pr6-definition-divergence-v2.json`
- Reason rubric: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T200211Z/reason-rubric-v3.md`
- Rationale writer: `/home/pete.levasseur/opencode-project-agents/fls/reports/record-rationale-v3.py`
- Rationale analyzer: `/home/pete.levasseur/opencode-project-agents/fls/reports/analyze-rationale-patterns-v3.py`
- Rationale events log: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T200211Z/reports/rationale-events.jsonl`
- Validator: `/home/pete.levasseur/opencode-project-agents/fls/reports/validate-ledger-and-checklist-v3.py`
- Glossary file: `src/glossary.rst`
- Term lock manifest: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T200211Z/batch-005-term-lock.json`
- Remediation directory: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T200211Z`
- Batch number: `5`

Batch scope (exact IDs only): WA-007, WA-008, WA-009

Terms:
- WA-007: name
- WA-008: item
- WA-009: field

ROLE LOCK (MANDATORY):
- YOU ARE THE IMPLEMENTER.
- YOU ARE NOT THE REVIEWER.
- DO NOT RUN `approve-deviation.py`.
- IF A DEVIATION IS NEEDED: FILE THE PERMIT, THEN STOP AND HAND OFF TO REVIEWER.
- ANY SELF-APPROVAL IS A POLICY VIOLATION.

Definition alignment rules (MANDATORY):
- Canonical definition text is in `glossary.rst`.
- For each term, ensure a chapter `:dt:` definition paragraph aligns with glossary canonical text.
- Use `definition_operation=promote` only when an equivalent chapter sentence already exists.
- Use `definition_operation=insert` when equivalent sentence does not exist and glossary text must be inserted.
- Use `definition_operation=adapt` only for justified contextual rewording with reviewer attention.
- For `insert`, add a new definitional sentence; do not satisfy `insert` by relabeling an existing in-place `:t:` occurrence to `:dt:`.
- DO NOT satisfy the task with non-definitional marker swaps.

Required workflow:
1. Process each listed term manually, one by one.
2. Apply step1 spec edits as needed.
3. Update only these term rows in checklist and ledger.
4. For each completed term, ensure checklist sub-items `.1`..`.6` are checked.
5. Anchor integrity rules are mandatory for every completed term:
   - `after_dp_id` must exist in the edited `after_file` in the current worktree.
   - The paragraph immediately after `:dp:`after_dp_id`` must contain `:dt:`<term>``.
   - Do not invent `after_dp_id` values that are not present in the edited file.
   - Leave `after_commit` empty; orchestrator sets it after commit.
6. Use rationale writer once per completed term (no direct rationale edits in CSV):
   `python3 "/home/pete.levasseur/opencode-project-agents/fls/reports/record-rationale-v3.py" --checklist-id <ID> --checklist "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T200211Z/manual-placement-checklist-v3.md" --ledger "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T200211Z/manual-placement-ledger-v3.csv" --placement-json "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/fls-pr6-placement-fitness-v2.json" --divergence-json "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-tshepang-20260210T174752Z/phase1-main-text-coverage/feedback-v2-20260211T133654Z/fls-pr6-definition-divergence-v2.json" --events-jsonl "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T200211Z/reports/rationale-events.jsonl" --batch-id "batch-005" --implementer-id <implementer> --action-type <action> --decision-detail <detail> --reason-code <code> --reason-why <text> --semantic-change-flag <flag> --review-attention <attention> --after-file <file> --after-line <line> --after-dp-id <dp> --after-section <section> --definition-operation <promote|insert|adapt> --workdir "/home/pete.levasseur/project/fls-wt/step1" --glossary-file "src/glossary.rst" --phase1-status completed --final-quality resolved-high [--deviation-permit <path>]`
7. Ensure ledger fields are complete (`action_type`, `decision_detail`, `reason_*`, `semantic_change_flag`, `review_attention`, after anchors, statuses, rationale UUID metadata).
8. Do not commit or push (orchestrator handles commit).
9. Run validator in progress mode before responding:
   `python3 "/home/pete.levasseur/opencode-project-agents/fls/reports/validate-ledger-and-checklist-v3.py" --mode progress --checklist "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T200211Z/manual-placement-checklist-v3.md" --ledger "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T200211Z/manual-placement-ledger-v3.csv" --baseline "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T200211Z/manual-placement-baseline-reference-v3.csv" --recovery-guardrails --workdir "/home/pete.levasseur/project/fls-wt/step1" --glossary-file "src/glossary.rst" --min-glossary-similarity 0.50 --min-promote-similarity 0.72 --events-jsonl "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T200211Z/reports/rationale-events.jsonl" --json-out "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T200211Z/batch-005-validate-progress.json" --markdown-out "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T200211Z/checklist-progress.md"`
10. Run rationale analyzer and keep artifacts current:
   `python3 "/home/pete.levasseur/opencode-project-agents/fls/reports/analyze-rationale-patterns-v3.py" --ledger "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T200211Z/manual-placement-ledger-v3.csv" --json-out "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T200211Z/batch-005-rationale-patterns.json" --markdown-out "/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v3-step1-phase1-remediation-20260212T200211Z/batch-005-rationale-patterns.md"`

Response format:
- Completed IDs
- Quarantined IDs (if any)
- Files changed
- Any blockers (if none, say "none")
