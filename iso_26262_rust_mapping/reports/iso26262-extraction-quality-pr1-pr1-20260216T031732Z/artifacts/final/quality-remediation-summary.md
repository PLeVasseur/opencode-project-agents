# Quality Remediation Summary

- MODE: resume-explicit-pr1
- RUN_ID: pr1-20260216T031732Z
- CURRENT_STAGE before/after: EQ11 -> EQ12
- STOP_REASON: blocked_by_stop_condition

## Blockers
- EQ12 hard gate failure: P06:paragraph_boundary_f1, P06:paragraph_fragment_end, P06:paragraph_fragment_start, P06:paragraph_singleton_page, P06:residual_legal_zero, P06:triad_source_set_identity, P06:unit_type_provenance_overlap, P08:paragraph_boundary_f1, P08:paragraph_fragment_end, P08:paragraph_fragment_start, P08:paragraph_singleton_page, P08:residual_legal_zero, P08:triad_source_set_identity, P08:unit_type_provenance_overlap, P09:paragraph_boundary_f1, P09:paragraph_fragment_end, P09:paragraph_fragment_start, P09:paragraph_meaningful, P09:paragraph_singleton_page, P09:residual_legal_zero, P09:triad_source_set_identity, P09:unit_type_provenance_overlap, overall:paragraph_fragment_end, overall:paragraph_fragment_start, overall:paragraph_singleton_page, overall:residual_legal_zero, overall:triad_source_set_identity, overall:unit_type_provenance_overlap, percent:P06.scope_extraction.table_scope_detection_recall_pct=766.6666666666667, percent:P08.scope_extraction.table_scope_detection_recall_pct=766.6666666666667, percent:P09.scope_extraction.table_scope_detection_recall_pct=766.6666666666667, percent:overall.scope_extraction.table_scope_detection_recall_pct=766.6666666666667

## Resume
- OPENCODE_CONFIG_DIR=/home/pete.levasseur/opencode-project-agents/iso_26262_rust_mapping RUN_ID=pr1-20260216T031732Z START_STAGE=EQ12 MAX_STAGES=all uv run python tools/traceability/mining/execute_quality_remediation.py
- RUN_ID=pr1-20260216T031732Z START_STAGE=EQ12 MAX_STAGES=all OPENCODE_CONFIG_DIR=/home/pete.levasseur/opencode-project-agents/iso_26262_rust_mapping opencode prompt "Execute ISO 26262 Unit Boundary Pathology Diagnosis and Remediation (Resumable + One-Shot)"
