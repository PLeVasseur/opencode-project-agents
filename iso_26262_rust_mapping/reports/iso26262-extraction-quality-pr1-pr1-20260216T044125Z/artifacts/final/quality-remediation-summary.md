# Quality Remediation Summary

- MODE: kickoff-auto-pr1
- RUN_ID: pr1-20260216T044125Z
- CURRENT_STAGE before/after: EQ0 -> EQ12
- STOP_REASON: blocked_by_stop_condition

## Blockers
- EQ12 hard gate failure: P06:paragraph_fragment_start, P06:table_scope, P06:unit_type_provenance_overlap, P08:paragraph_fragment_start, P08:table_scope, P08:unit_type_provenance_overlap, P09:paragraph_fragment_start, P09:paragraph_meaningful, P09:table_scope, P09:triad_source_set_identity, P09:unit_type_provenance_overlap, overall:paragraph_fragment_start, overall:table_scope, overall:unit_type_provenance_overlap

## Resume
- OPENCODE_CONFIG_DIR=/home/pete.levasseur/opencode-project-agents/iso_26262_rust_mapping RUN_ID=pr1-20260216T044125Z START_STAGE=EQ12 MAX_STAGES=all uv run python tools/traceability/mining/execute_quality_remediation.py
- RUN_ID=pr1-20260216T044125Z START_STAGE=EQ12 MAX_STAGES=all OPENCODE_CONFIG_DIR=/home/pete.levasseur/opencode-project-agents/iso_26262_rust_mapping opencode prompt "Execute ISO 26262 Unit Boundary Pathology Remediation Repair (Resumable + One-Shot)"
