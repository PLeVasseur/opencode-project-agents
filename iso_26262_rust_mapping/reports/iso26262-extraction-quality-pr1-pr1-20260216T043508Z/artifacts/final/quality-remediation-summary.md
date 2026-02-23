# Quality Remediation Summary

- MODE: resume-explicit-pr1
- RUN_ID: pr1-20260216T043508Z
- CURRENT_STAGE before/after: EQ11 -> EQ12
- STOP_REASON: blocked_by_stop_condition

## Blockers
- EQ12 hard gate failure: P06:list_boundary_f1, P06:list_meaningful, P06:paragraph_boundary_f1, P06:paragraph_fragment_start, P06:table_cell_boundary_f1, P06:table_meaningful, P06:table_pattern, P06:table_scope, P06:unit_type_provenance_overlap, P08:list_boundary_f1, P08:list_meaningful, P08:paragraph_boundary_f1, P08:paragraph_fragment_start, P08:table_cell_boundary_f1, P08:table_meaningful, P08:table_pattern, P08:table_scope, P08:unit_type_provenance_overlap, P09:list_boundary_f1, P09:list_meaningful, P09:paragraph_boundary_f1, P09:paragraph_fragment_end, P09:paragraph_fragment_start, P09:paragraph_meaningful, P09:table_cell_boundary_f1, P09:table_meaningful, P09:table_scope, P09:triad_source_set_identity, P09:unit_type_provenance_overlap, overall:list_boundary_f1, overall:list_meaningful, overall:paragraph_boundary_f1, overall:paragraph_fragment_start, overall:table_cell_boundary_f1, overall:table_meaningful, overall:table_pattern, overall:table_scope, overall:unit_type_provenance_overlap

## Resume
- OPENCODE_CONFIG_DIR=/home/pete.levasseur/opencode-project-agents/iso_26262_rust_mapping RUN_ID=pr1-20260216T043508Z START_STAGE=EQ12 MAX_STAGES=all uv run python tools/traceability/mining/execute_quality_remediation.py
- RUN_ID=pr1-20260216T043508Z START_STAGE=EQ12 MAX_STAGES=all OPENCODE_CONFIG_DIR=/home/pete.levasseur/opencode-project-agents/iso_26262_rust_mapping opencode prompt "Execute ISO 26262 Unit Boundary Pathology Remediation Repair (Resumable + One-Shot)"
