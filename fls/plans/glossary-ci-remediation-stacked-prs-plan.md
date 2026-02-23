# Glossary stacked PR CI remediation plan

- [x] Confirm failing checks and group failures by root cause across PRs 6-10.
- [x] Fix step1 Python style/lint failures (Black + flake8) and re-run local CI-equivalent checks.
- [x] Fix step2 malformed glossary entries that trigger docutils indentation and paragraph-id failures.
- [x] Restack step3 and step4 from updated lower phases and re-verify strict/build/link checks.
- [x] Fix step5 glossary generator output shape for list-item definitions and remove resulting RST parse failures.
- [x] Resolve remaining step5 Python style/lint issues (Black + flake8).
- [x] Re-run per-branch local CI-equivalent checks (`./make.py --clear --check-links`, `uvx black`, `uvx flake8`) for step1-step5.
- [x] Commit, push updated phase branches, and verify GitHub checks pass for PRs 6-10.
- [x] Summarize remediation actions, remaining risks, and follow-ups.
