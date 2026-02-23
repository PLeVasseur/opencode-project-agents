# V2 tooling contract for Step1/Phase1 templates

These templates are coupled to the v2 remediation tooling and must not be executed with the v1 scripts.

- Validator: `$OPENCODE_CONFIG_DIR/reports/validate-ledger-and-checklist-v2.py`
- Orchestrator: `$OPENCODE_CONFIG_DIR/reports/glossary-batch-orchestrator-v2.py`

Compatibility assumptions:

- Parent checklist IDs use `WA-###`, `WB-###`, `WC-###`, `WD-###`, `QQ-###`.
- Every parent row has six rubric sub-items (`.1` through `.6`).
- Ledger schema includes v2 fields such as `action_type`, `decision_detail`, `semantic_change_flag`, and `review_attention`.

Do not rename these template files unless all consuming scripts and docs are updated in lockstep.
