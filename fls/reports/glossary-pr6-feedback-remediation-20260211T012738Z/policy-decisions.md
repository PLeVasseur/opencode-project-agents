# Policy decisions

## A0 disallowed directive enforcement

- Decision: **remove disallowed-directive enforcement** from glossary migration tooling and Sphinx lint extension for this remediation run.
- Rationale:
  - Requested remediation direction for PR6/PR7 feedback was to decouple this policy gate from phase strict migration accounting.
  - Strict phase reports in this run should focus on migration coverage/alignment outcomes rather than directive policy checks.
- Implemented changes:
  - Removed `no-disallowed-directives` check emission from `tools/glossary-migration-check.py`.
  - Removed disallowed-directive enforcement from `exts/ferrocene_spec_lints/glossary_migration.py` runtime `check()` path.
- Test/expectation impact:
  - Phase strict reports no longer include `no-disallowed-directives` entries.
  - Phase1/Phase2 strict pass criteria for this remediation use coverage + definition-alignment gates only.
