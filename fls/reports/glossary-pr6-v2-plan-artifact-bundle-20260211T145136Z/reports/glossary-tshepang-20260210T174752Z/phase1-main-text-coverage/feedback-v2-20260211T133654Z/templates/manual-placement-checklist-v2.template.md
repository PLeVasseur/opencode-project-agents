# Manual Placement Checklist v2 (Template)

## Run metadata

- Run ID: `<fill>`
- Remediation dir: `<fill>`
- Step1 branch head (start): `<fill>`
- Baseline commit (v2 source): `<fill>`
- Policy doc: `$REMEDIATION_DIR/reports/policy-decisions-v2.md`
- Notes:
  - Mark a parent term checkbox only after all child checks pass.
  - Every checked term must have a completed ledger row in `manual-placement-ledger-v2.csv`.
  - Any rewrite action requires `review_attention=required`.

## Global gates

- [ ] G0 preflight complete
- [ ] Policy gate complete
- [ ] Wave A complete
- [ ] Wave B complete
- [ ] Gate B+ complete (external v3 artifacts received and C/D scope frozen)
- [ ] Wave C complete
- [ ] Wave D complete
- [ ] Final validation complete

## Wave A checklist (foundational terms)

- [ ] WA-001 term="value"
  - [ ] WA-001.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WA-001.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WA-001.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WA-001.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WA-001.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WA-001.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WA-002 term="expression"
  - [ ] WA-002.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WA-002.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WA-002.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WA-002.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WA-002.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WA-002.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WA-003 term="type"
  - [ ] WA-003.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WA-003.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WA-003.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WA-003.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WA-003.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WA-003.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WA-004 term="trait"
  - [ ] WA-004.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WA-004.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WA-004.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WA-004.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WA-004.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WA-004.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WA-005 term="construct"
  - [ ] WA-005.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WA-005.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WA-005.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WA-005.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WA-005.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WA-005.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WA-006 term="entity"
  - [ ] WA-006.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WA-006.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WA-006.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WA-006.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WA-006.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WA-006.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WA-007 term="name"
  - [ ] WA-007.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WA-007.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WA-007.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WA-007.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WA-007.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WA-007.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WA-008 term="item"
  - [ ] WA-008.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WA-008.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WA-008.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WA-008.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WA-008.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WA-008.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WA-009 term="field"
  - [ ] WA-009.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WA-009.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WA-009.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WA-009.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WA-009.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WA-009.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WA-010 term="reference"
  - [ ] WA-010.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WA-010.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WA-010.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WA-010.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WA-010.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WA-010.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WA-011 term="implementation"
  - [ ] WA-011.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WA-011.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WA-011.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WA-011.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WA-011.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WA-011.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WA-012 term="method"
  - [ ] WA-012.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WA-012.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WA-012.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WA-012.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WA-012.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WA-012.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WA-013 term="crate"
  - [ ] WA-013.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WA-013.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WA-013.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WA-013.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WA-013.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WA-013.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WA-014 term="module"
  - [ ] WA-014.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WA-014.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WA-014.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WA-014.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WA-014.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WA-014.6 status finalized (`phase1_status`, `final_quality`)

- [ ] WA-015 term="statement"
  - [ ] WA-015.1 before snapshot locked (`baseline_file`, `baseline_line`, `baseline_dp_id`, `baseline_commit`)
  - [ ] WA-015.2 action recorded (`action_type`, `decision_detail`, `reason_code`)
  - [ ] WA-015.3 rationale quality pass (`reason_why`, `reason_quality=pass`)
  - [ ] WA-015.4 semantic review fields complete (`semantic_change_flag`, `review_attention`)
  - [ ] WA-015.5 after snapshot captured (`after_file`, `after_line`, `after_dp_id`, `after_commit`)
  - [ ] WA-015.6 status finalized (`phase1_status`, `final_quality`)

## Wave B checklist template block (repeat as needed)

- [ ] WB-<nnn> term="<term>"
  - [ ] WB-<nnn>.1 before snapshot locked
  - [ ] WB-<nnn>.2 action recorded
  - [ ] WB-<nnn>.3 rationale quality pass
  - [ ] WB-<nnn>.4 semantic review fields complete
  - [ ] WB-<nnn>.5 after snapshot captured
  - [ ] WB-<nnn>.6 status finalized

## Gate B+ checklist

- [ ] v3 analysis markdown received (`fls-pr6-updated-analysis-v3.md`)
- [ ] v3 placement json received (`fls-pr6-placement-fitness-v3.json`)
- [ ] v3 divergence json received (`fls-pr6-definition-divergence-v3.json`)
- [ ] v3 checksums recorded
- [ ] v2-v3 delta report generated
- [ ] wave-c-terms.json frozen
- [ ] wave-d-terms.json frozen

## Wave C checklist template block (repeat as needed)

- [ ] WC-<nnn> term="<term>"
  - [ ] WC-<nnn>.1 before snapshot locked
  - [ ] WC-<nnn>.2 action recorded
  - [ ] WC-<nnn>.3 rationale quality pass
  - [ ] WC-<nnn>.4 semantic review fields complete
  - [ ] WC-<nnn>.5 after snapshot captured
  - [ ] WC-<nnn>.6 status finalized

## Wave D checklist template block (repeat as needed)

- [ ] WD-<nnn> term="<term>"
  - [ ] WD-<nnn>.1 before snapshot locked
  - [ ] WD-<nnn>.2 action recorded
  - [ ] WD-<nnn>.3 rationale quality pass
  - [ ] WD-<nnn>.4 semantic review fields complete
  - [ ] WD-<nnn>.5 after snapshot captured
  - [ ] WD-<nnn>.6 status finalized

## Quarantine queue checklist

- [ ] QQ-<nnn> term="<term>" reason="<why quarantined>" retry_batch="<id>" status="open"

## Final closeout checklist

- [ ] All scoped checklist parent items checked
- [ ] All scoped sub-items checked
- [ ] All ledger rows final_quality set
- [ ] All rewrite rows reviewed (`review_attention=required` satisfied)
- [ ] Final strict check pass
- [ ] Final build pass
- [ ] Final summary report completed
