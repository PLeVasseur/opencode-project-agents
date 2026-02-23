# Manual Placement Checklist v2 (Run Local)

## Run metadata

- Run ID: `20260211T182136Z-v2-phase1`
- Remediation dir: `/home/pete.levasseur/opencode-project-agents/fls/reports/glossary-pr6-v2-step1-phase1-remediation-20260211T182136Z-v2-phase1`
- Step1 branch head (start): `19e75856eac5694e5d613c7c59b429848d333992`
- Baseline commit (v2 source): `19e75856eac5694e5d613c7c59b429848d333992`
- Policy doc: `$REMEDIATION_DIR/reports/policy-decisions-v2.md`
- Validator tool: `$OPENCODE_CONFIG_DIR/reports/validate-ledger-and-checklist-v2.py`
- Orchestrator tool: `$OPENCODE_CONFIG_DIR/reports/glossary-batch-orchestrator-v2.py`

## Global gates

- [ ] G0 preflight complete
- [ ] Policy gate complete
- [ ] Wave A complete
- [ ] Wave B complete
- [ ] Gate B+ complete (external v3 artifacts received and C/D scope frozen)

## Wave A checklist (foundational terms)

- [x] WA-001 term="value"
  - [x] WA-001.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WA-001.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WA-001.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WA-001.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WA-001.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WA-001.6 status finalized (`phase1_status`, `final_quality`)

- [x] WA-002 term="expression"
  - [x] WA-002.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WA-002.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WA-002.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WA-002.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WA-002.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WA-002.6 status finalized (`phase1_status`, `final_quality`)

- [x] WA-003 term="type"
  - [x] WA-003.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WA-003.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WA-003.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WA-003.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WA-003.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WA-003.6 status finalized (`phase1_status`, `final_quality`)

- [x] WA-004 term="trait"
  - [x] WA-004.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WA-004.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WA-004.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WA-004.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WA-004.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WA-004.6 status finalized (`phase1_status`, `final_quality`)

- [x] WA-005 term="construct"
  - [x] WA-005.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WA-005.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WA-005.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WA-005.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WA-005.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WA-005.6 status finalized (`phase1_status`, `final_quality`)

- [x] WA-006 term="entity"
  - [x] WA-006.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WA-006.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WA-006.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WA-006.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WA-006.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WA-006.6 status finalized (`phase1_status`, `final_quality`)

- [x] WA-007 term="name"
  - [x] WA-007.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WA-007.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WA-007.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WA-007.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WA-007.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WA-007.6 status finalized (`phase1_status`, `final_quality`)

- [x] WA-008 term="item"
  - [x] WA-008.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WA-008.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WA-008.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WA-008.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WA-008.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WA-008.6 status finalized (`phase1_status`, `final_quality`)

- [x] WA-009 term="field"
  - [x] WA-009.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WA-009.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WA-009.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WA-009.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WA-009.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WA-009.6 status finalized (`phase1_status`, `final_quality`)

- [x] WA-010 term="reference"
  - [x] WA-010.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WA-010.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WA-010.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WA-010.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WA-010.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WA-010.6 status finalized (`phase1_status`, `final_quality`)

- [x] WA-011 term="implementation"
  - [x] WA-011.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WA-011.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WA-011.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WA-011.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WA-011.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WA-011.6 status finalized (`phase1_status`, `final_quality`)

- [x] WA-012 term="method"
  - [x] WA-012.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WA-012.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WA-012.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WA-012.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WA-012.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WA-012.6 status finalized (`phase1_status`, `final_quality`)

- [x] WA-013 term="crate"
  - [x] WA-013.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WA-013.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WA-013.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WA-013.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WA-013.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WA-013.6 status finalized (`phase1_status`, `final_quality`)

- [x] WA-014 term="module"
  - [x] WA-014.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WA-014.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WA-014.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WA-014.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WA-014.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WA-014.6 status finalized (`phase1_status`, `final_quality`)

- [x] WA-015 term="statement"
  - [x] WA-015.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WA-015.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WA-015.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WA-015.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WA-015.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WA-015.6 status finalized (`phase1_status`, `final_quality`)

## Wave B checklist (high/medium relocation priority excluding Wave A)

- [x] WB-001 term="field list"
  - [x] WB-001.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-001.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-001.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-001.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-001.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-001.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-002 term="type specification"
  - [x] WB-002.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-002.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-002.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-002.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-002.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-002.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-003 term="concrete type"
  - [x] WB-003.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-003.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-003.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-003.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-003.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-003.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-004 term="generic function"
  - [x] WB-004.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-004.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-004.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-004.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-004.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-004.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-005 term="variable"
  - [x] WB-005.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-005.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-005.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-005.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-005.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-005.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-006 term="container operand"
  - [x] WB-006.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-006.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-006.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-006.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-006.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-006.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-007 term="undefined behavior"
  - [x] WB-007.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-007.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-007.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-007.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-007.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-007.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-008 term="code point"
  - [x] WB-008.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-008.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-008.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-008.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-008.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-008.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-009 term="receiver operand"
  - [x] WB-009.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-009.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-009.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-009.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-009.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-009.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-010 term="associated constant"
  - [x] WB-010.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-010.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-010.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-010.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-010.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-010.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-011 term="crate root module"
  - [x] WB-011.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-011.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-011.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-011.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-011.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-011.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-012 term="associated trait function"
  - [x] WB-012.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-012.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-012.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-012.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-012.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-012.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-013 term="size"
  - [x] WB-013.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-013.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-013.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-013.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-013.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-013.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-014 term="floating-point type"
  - [x] WB-014.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-014.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-014.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-014.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-014.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-014.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-015 term="safety invariant"
  - [x] WB-015.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-015.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-015.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-015.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-015.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-015.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-016 term="unit struct"
  - [x] WB-016.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-016.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-016.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-016.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-016.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-016.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-017 term="unsafe context"
  - [x] WB-017.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-017.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-017.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-017.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-017.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-017.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-018 term="associated trait constant"
  - [x] WB-018.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-018.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-018.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-018.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-018.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-018.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-019 term="union value"
  - [x] WB-019.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-019.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-019.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-019.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-019.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-019.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-020 term="pattern-without-alternation"
  - [x] WB-020.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-020.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-020.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-020.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-020.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-020.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-021 term="discriminant"
  - [x] WB-021.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-021.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-021.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-021.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-021.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-021.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-022 term="field index"
  - [x] WB-022.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-022.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-022.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-022.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-022.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-022.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-023 term="static"
  - [x] WB-023.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-023.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-023.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-023.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-023.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-023.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-024 term="evaluation"
  - [x] WB-024.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-024.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-024.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-024.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-024.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-024.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-025 term="enum variant value"
  - [x] WB-025.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-025.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-025.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-025.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-025.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-025.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-026 term="immutable"
  - [x] WB-026.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-026.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-026.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-026.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-026.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-026.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-027 term="signed integer type"
  - [x] WB-027.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-027.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-027.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-027.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-027.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-027.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-028 term="execution"
  - [x] WB-028.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-028.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-028.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-028.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-028.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-028.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-029 term="function body"
  - [x] WB-029.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-029.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-029.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-029.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-029.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-029.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-030 term="attribute content"
  - [x] WB-030.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-030.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-030.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-030.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-030.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-030.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-031 term="borrowed"
  - [x] WB-031.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-031.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-031.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-031.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-031.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-031.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-032 term="irrefutable pattern"
  - [x] WB-032.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-032.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-032.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-032.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-032.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-032.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-033 term="record enum variant"
  - [x] WB-033.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-033.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-033.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-033.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-033.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-033.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-034 term="structurally equal"
  - [x] WB-034.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-034.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-034.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-034.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-034.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-034.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-035 term="implementation body"
  - [x] WB-035.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-035.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-035.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-035.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-035.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-035.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-036 term="dangling"
  - [x] WB-036.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-036.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-036.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-036.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-036.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-036.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-037 term="pointer"
  - [x] WB-037.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-037.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-037.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-037.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-037.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-037.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-038 term="underscore expression"
  - [x] WB-038.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-038.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-038.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-038.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-038.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-038.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-039 term="element type"
  - [x] WB-039.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-039.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-039.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-039.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-039.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-039.6 status finalized (`phase1_status`, `final_quality`)

- [x] WB-040 term="mutable variable"
  - [x] WB-040.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [x] WB-040.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [x] WB-040.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [x] WB-040.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [x] WB-040.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [x] WB-040.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-041 term="discriminant initializer"
  - [ ] WB-041.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-041.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-041.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-041.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-041.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-041.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-042 term="[unifiable type]s"
  - [ ] WB-042.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-042.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-042.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-042.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-042.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-042.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-043 term="elaboration"
  - [ ] WB-043.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-043.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-043.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-043.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-043.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-043.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-044 term="exported function"
  - [ ] WB-044.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-044.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-044.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-044.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-044.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-044.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-045 term="expression-with-block"
  - [ ] WB-045.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-045.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-045.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-045.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-045.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-045.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-046 term="external function item type"
  - [ ] WB-046.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-046.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-046.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-046.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-046.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-046.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-047 term="mutable"
  - [ ] WB-047.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-047.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-047.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-047.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-047.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-047.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-048 term="where clause"
  - [ ] WB-048.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-048.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-048.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-048.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-048.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-048.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-049 term="associated function"
  - [ ] WB-049.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-049.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-049.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-049.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-049.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-049.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-050 term="renaming"
  - [ ] WB-050.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-050.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-050.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-050.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-050.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-050.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-051 term="separator"
  - [ ] WB-051.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-051.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-051.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-051.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-051.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-051.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-052 term="struct pattern"
  - [ ] WB-052.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-052.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-052.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-052.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-052.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-052.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-053 term="tuple enum variant"
  - [ ] WB-053.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-053.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-053.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-053.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-053.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-053.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-054 term="associated item"
  - [ ] WB-054.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-054.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-054.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-054.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-054.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-054.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-055 term="destructor"
  - [ ] WB-055.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-055.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-055.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-055.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-055.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-055.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-056 term="escaped character"
  - [ ] WB-056.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-056.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-056.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-056.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-056.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-056.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-057 term="generic substitution"
  - [ ] WB-057.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-057.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-057.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-057.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-057.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-057.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-058 term="trait implementation"
  - [ ] WB-058.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-058.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-058.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-058.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-058.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-058.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-059 term="function"
  - [ ] WB-059.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-059.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-059.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-059.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-059.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-059.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-060 term="type path"
  - [ ] WB-060.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-060.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-060.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-060.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-060.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-060.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-061 term="inherent implementation"
  - [ ] WB-061.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-061.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-061.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-061.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-061.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-061.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-062 term="self parameter"
  - [ ] WB-062.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-062.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-062.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-062.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-062.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-062.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-063 term="tuple"
  - [ ] WB-063.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-063.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-063.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-063.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-063.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-063.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-064 term="type parameter"
  - [ ] WB-064.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-064.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-064.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-064.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-064.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-064.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-065 term="implicit borrow"
  - [ ] WB-065.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-065.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-065.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-065.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-065.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-065.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-066 term="associated type"
  - [ ] WB-066.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-066.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-066.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-066.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-066.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-066.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-067 term="binding argument"
  - [ ] WB-067.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-067.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-067.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-067.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-067.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-067.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-068 term="future"
  - [ ] WB-068.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-068.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-068.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-068.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-068.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-068.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-069 term="label"
  - [ ] WB-069.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-069.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-069.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-069.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-069.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-069.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-070 term="static initializer"
  - [ ] WB-070.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-070.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-070.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-070.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-070.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-070.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-071 term="arity"
  - [ ] WB-071.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-071.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-071.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-071.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-071.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-071.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-072 term="constant parameter"
  - [ ] WB-072.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-072.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-072.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-072.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-072.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-072.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-073 term="mutable static"
  - [ ] WB-073.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-073.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-073.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-073.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-073.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-073.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-074 term="scalar type"
  - [ ] WB-074.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-074.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-074.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-074.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-074.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-074.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-075 term="constant parameter initializer"
  - [ ] WB-075.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-075.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-075.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-075.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-075.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-075.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-076 term="immutable reference"
  - [ ] WB-076.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-076.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-076.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-076.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-076.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-076.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-077 term="external function"
  - [ ] WB-077.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-077.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-077.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-077.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-077.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-077.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-078 term="external static"
  - [ ] WB-078.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-078.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-078.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-078.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-078.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-078.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-079 term="unit enum variant"
  - [ ] WB-079.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-079.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-079.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-079.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-079.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-079.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-080 term="tuple struct"
  - [ ] WB-080.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-080.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-080.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-080.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-080.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-080.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-081 term="binary crate"
  - [ ] WB-081.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-081.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-081.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-081.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-081.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-081.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-082 term="c"
  - [ ] WB-082.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-082.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-082.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-082.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-082.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-082.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-083 term="qualifying trait"
  - [ ] WB-083.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-083.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-083.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-083.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-083.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-083.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-084 term="temporary"
  - [ ] WB-084.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-084.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-084.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-084.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-084.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-084.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-085 term="pattern-without-range"
  - [ ] WB-085.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-085.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-085.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-085.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-085.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-085.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-086 term="qualified type"
  - [ ] WB-086.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-086.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-086.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-086.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-086.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-086.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-087 term="tuple struct type"
  - [ ] WB-087.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-087.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-087.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-087.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-087.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-087.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-088 term="trait body"
  - [ ] WB-088.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-088.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-088.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-088.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-088.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-088.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WB-089 term="base initializer"
  - [ ] WB-089.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WB-089.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WB-089.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WB-089.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WB-089.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WB-089.6 status finalized (`phase1_status`, `final_quality`)

## Gate B+ checklist

- [ ] v3 analysis markdown received (`fls-pr6-updated-analysis-v3.md`)
- [ ] v3 placement json received (`fls-pr6-placement-fitness-v3.json`)
- [ ] v3 divergence json received (`fls-pr6-definition-divergence-v3.json`)
- [ ] v3 checksums recorded
- [ ] v2-v3 delta report generated
- [ ] wave-c-terms.json frozen
- [ ] wave-d-terms.json frozen
