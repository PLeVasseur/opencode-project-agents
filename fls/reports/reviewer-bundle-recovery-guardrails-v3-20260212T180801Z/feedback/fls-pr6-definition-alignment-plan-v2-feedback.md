# Definition-Alignment Tooling Plan v2 — Reviewer Feedback

## Overall

All 8 prior feedback items are addressed and traceable. The tracking section maps each issue to a specific implementation point, and the corresponding plan sections deliver on each one. Three minor clarifications needed before execution.

---

## 1. Compound split check needs a precise definition of "content word"

The plan says "reject if token immediately after `:dt:`term`` is a content word." This is the right rule, but "content word" is undefined. The implementer will make a judgment call and likely under-specify, which matters because this is one of the two critical anti-shortcut checks.

### Required clarification

Define explicitly: a content word is any alphabetic token that is **not** a stopword and **not** the start of another RST role. Specifically:

- **Stopwords** (do not trigger rejection): `is`, `are`, `was`, `were`, `a`, `an`, `the`, `of`, `in`, `that`, `which`, `and`, `or`, `for`, `with`, `by`, `to`, `from`
- **RST role prefixes** (do not trigger rejection): tokens starting with `:t:`, `:s:`, `:c:`, `:dp:`, `:dc:`, `:ds:`
- **Punctuation and whitespace** (do not trigger rejection): any non-alphabetic token, line breaks, commas, periods, etc.
- **Everything else** triggers `FAILED_COMPOUND_DT_SPLIT`.

This list should be hardcoded in both the writer and the validator, not derived dynamically.

---

## 2. `insert` diff cross-check has a whole-file edge case

The plan checks "positive net line delta in `after_file` within `after_commit` diff." This is almost right but has an edge case: if the implementer inserts a glossary definition but also deletes an equal number of lines elsewhere in the same file (unrelated cleanup, removing a redundant passage), the net delta could be zero and the check would incorrectly fire `FAILED_INSERT_DIFF_MISMATCH`.

### Required clarification

The ideal check is scoped to the specific hunk containing the `:dt:` marker, not the whole-file net — `git diff` can be parsed at hunk granularity. If hunk-level parsing is too complex for the implementation timeline, whole-file net-positive is acceptable with a documented known limitation: `insert` operations should avoid same-file deletions in the same commit, or the implementer should split the work across commits.

---

## 3. Phase 3 needs to sequence the 3 fixup terms separately

Phase 3 says "re-run rationale recording for all 15 WA-001..WA-015 rows using `--definition-operation`." But the 3 terms that need prose fixups (`method`, `item`, `field`) can't be re-recorded until the fixup edits are committed. The writer will correctly reject them — non-definitional sentence, compound split — and Phase 3 stalls.

### Required clarification

Split Phase 3 into two sub-phases:

- **Phase 3a**: Re-record the 12 terms whose destination prose is already correct. These will be `promote` with high similarity. Run against current committed state.
- **Phase 3b**: Author and commit the prose fixups for `method`, `item`, `field`. Then re-record those 3 terms as `insert`. Run against the new committed state.

This ensures Phase 3 doesn't block on terms that are known to fail the new checks.

---

## Summary

| # | Issue | Severity |
|---|---|---|
| 1 | "Content word" undefined in compound split check | Medium — ambiguity in critical check |
| 2 | Whole-file net delta edge case for `insert` | Low — edge case, documentable |
| 3 | Phase 3 sequencing for fixup terms | Medium — will block execution |

The plan is ready to execute once these are addressed.
