# Recovery guardrail smoke tests (v3)

- Passed: `18/18`

- [x] `record-rationale-v3.py --help`
- [x] `validate-ledger-and-checklist-v3.py --help`
- [x] `glossary-batch-orchestrator-v3.py --help`
- [x] `analyze-rationale-patterns-v3.py --help`
- [x] record-rationale success case writes UUID/event
- [x] record-rationale mismatch case hard-fails term-source lock
- [x] record-rationale high-priority non-move without permit hard-fails
- [x] record-rationale self-approved permit hard-fails
- [x] record-rationale invalid permit path format hard-fails
- [x] validator recovery success case passes
- [x] validator duplicate UUID fixture fails (`FAILED_UUID_GUARDRAIL` present)
- [x] validator strict regression fixture fails (`FAILED_STRICT_REGRESSION` present)
- [x] orchestrator v3 dry-run output exists
- [x] orchestrator v3 dry-run prompt artifact exists
- [x] orchestrator v3 dry-run term-lock artifact exists
- [x] orchestrator validator classification helper quarantines UUID/recommendation errors by checklist ID
- [x] orchestrator validator hard-fail classification helper flags strict regression codes
- [x] rationale analyzer fixture smoke test emits JSON + Markdown
