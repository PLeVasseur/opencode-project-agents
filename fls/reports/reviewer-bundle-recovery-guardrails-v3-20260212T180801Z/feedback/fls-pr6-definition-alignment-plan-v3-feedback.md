# Definition-Alignment Tooling Plan v3 — Reviewer Feedback

## Overall

All prior feedback items are incorporated correctly. The compound split token policy is explicit with a hardcoded stopword list, the insert diff check has hunk-primary with whole-file fallback, and Phase 3 is properly split into 3a/3b. No structural objections. Two minor observations, neither blocking.

---

## 1. Stopword list is missing common function words

The exempt stopword list (`is`, `are`, `was`, `were`, `a`, `an`, `the`, `of`, `in`, `that`, `which`, `and`, `or`, `for`, `with`, `by`, `to`, `from`) is tuned for prepositions and determiners but misses common function words. For example, `not` is alphabetic, not in the stopword list, and not an RST role prefix — so "A `:dt:`value` not stored in memory..." would trigger `FAILED_COMPOUND_DT_SPLIT`.

### Suggested addition

Add `not`, `no`, `but`, `as`, `if`, `so` to the exempt list. These are function words, not content words, and their presence after a `:dt:` marker does not indicate a compound term split. Not blocking — the implementer can extend the list during implementation if false positives appear in fixtures.

---

## 2. Validator hunk-vs-fallback mode selection is unspecified

The orchestrator captures both `git diff --numstat` (whole-file) and hunk-level patch metadata, and the validator supports both hunk mode and whole-file fallback. But the plan doesn't specify how the validator selects between modes — whether it's driven by CLI flag, presence of an artifact, or something else. Without this, it's ambiguous whether hunk mode ever activates in practice.

### Suggested clarification

Add a one-liner to the validator or orchestrator section specifying the selection logic. For example: "The validator uses hunk mode when `batch-XXX-diff-audit.json` is present and contains hunk data for the target file; falls back to whole-file net delta from `batch-XXX-summary.json` otherwise."

---

## Summary

| # | Issue | Severity |
|---|---|---|
| 1 | Stopword list incomplete for function words | Non-blocking — extend during implementation |
| 2 | Hunk-vs-fallback mode selection unspecified | Non-blocking — one-liner clarification |

The plan is ready to execute.
