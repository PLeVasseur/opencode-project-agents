# Definition-Alignment Tooling Plan — Reviewer Feedback

## Overall

The plan correctly targets the root cause: validating what the project is supposed to produce (glossary definitions present in chapter text) rather than validating process artifacts around it. The glossary-chapter alignment check, the operation type taxonomy, and the Wave A quality gate blocking Wave B are all the right structural choices. Eight issues follow, in order of severity.

---

## 1. No git diff cross-check for `insert` declarations

The plan validates similarity between glossary and chapter `:dt:` sentence, but doesn't verify that text was actually added to the file. An implementer declares `definition_operation=insert` and the validator checks similarity ≥ 0.85 — but what if the chapter already had a near-identical sentence and the implementer just promoted the marker? That's a `promote`, not an `insert`, and the distinction matters because it determines whether the plan is tracking reality.

For 7 of the 10 Wave A terms, this exact scenario would have produced a passing `insert` declaration on what was actually a marker swap.

### Required change

For `insert` operations, verify the destination file has a net line increase in the batch commit. A pure marker swap produces +1/−1 per hunk. A real text insertion produces net new lines. The orchestrator already has access to `git diff --numstat` at commit time — surface the per-file net-line-change in the batch summary and cross-check against declared operations.

---

## 2. Compound term rejection needs generalization

The plan calls out the `:dt:`method` call expression` split as a known false-definition pattern. But this needs to be a general structural check, not an enumerated pattern. The 89 Wave B terms will have their own compound term traps that can't be listed in advance.

### Required change

Implement a general rule: if the word immediately following the closing backtick of `:dt:`term`` is a content word (not punctuation, not "is", not a line break), then the `:dt:` is probably tagging a substring of a compound term rather than defining the term itself. Check this structurally in both the rationale writer and the validator.

---

## 3. Multi-sentence glossary definitions need explicit handling

Some glossary entries have multiple sentences. `item` has two definitional sentences plus a "See :s:`Item`." cross-reference. The plan says "parse glossary text for exact target term definition sentence(s)" but doesn't specify which sentences are canonical, leaving a judgment call for the implementer to make during script implementation.

### Required change

Specify the rule explicitly: take sentences containing `:dt:`term`` as the canonical definition set. Exclude bare "See :s:`...`" cross-reference lines. If additional sentences follow the `:dt:` sentence before the next glossary entry heading, include them only if they don't start with "See". Document this in the plan so the parser is deterministic.

---

## 4. `adapt` at 0.55 similarity is too permissive

Jaccard 0.55 on content words is low enough that a sentence with the right domain vocabulary but no actual definitional relationship could pass. For example, "The `:dt:`field` of the operand is resolved during type checking" shares content words with "A field is an element of an abstract data type" (`field`, `type`) and could approach 0.55 depending on sentence length. The `review_attention=required` gate catches this eventually, but the writer shouldn't accept it in the first place.

### Required change

Either lower the `adapt` floor to 0.40 (acknowledging the automation can't reliably distinguish at this range) and rely entirely on the reviewer gate, or keep 0.55 but add a structural check: the `:dt:` sentence must have the term as grammatical subject (not object, not modifier), same requirement as for `promote` and `insert`.

---

## 5. Similarity recomputation tolerance is unspecified

The validator "compares recomputed similarity to stored value within tolerance" but doesn't specify the tolerance. Floating-point Jaccard on tokenized text should be deterministic given the same normalization, so tolerance should be zero (exact equality). If it's not zero, that implies the normalization isn't deterministic, which is a bug that should be fixed rather than tolerated.

### Required change

Pin the comparison to exact equality. Fail if recomputed similarity diverges from stored similarity. This forces the normalization to be reproducible rather than papering over inconsistencies.

---

## 6. The 7 "good" Wave A terms need revalidation through this pipeline

The plan is framed as tooling changes only, with "source text remediation execution" out of scope. But the 7 terms that passed by coincidence have never been validated through the alignment check. When the Wave A fixup runs for `method`/`item`/`field`, the other 12 terms should also be re-processed through `record-rationale-v3.py` with the new `--definition-operation` flag so they get glossary hashes, similarity scores, and operation declarations.

### Required change

Add an explicit step: after tooling changes and before the Wave A quality gate, all 15 Wave A terms must be revalidated through the updated rationale writer with `--definition-operation`. The 12 existing terms will likely be `promote` with high similarity; the 3 fixed terms will be `insert`. Without this, the gate check will either fail on missing fields or skip the 12 terms.

---

## 7. Validator chapter extraction needs a specified file state

The validator reads actual `.rst` files to extract the chapter-side `:dt:` sentence. But which version of the files? The validator runs at multiple points: pre-batch (worktree may have uncommitted changes), post-batch (just committed), gate (should be committed). If the validator reads uncommitted state, it could see in-progress edits that don't match the final committed result.

### Required change

Specify that the validator reads from the worktree at `HEAD` (committed state) and that the orchestrator ensures glossary-alignment validation runs after commit, not before. Add this to the execution order.

---

## 8. Hash target should be normalized text, not raw RST

The plan adds `glossary_definition_sha256` and `chapter_definition_sha256` but doesn't specify whether they hash raw RST (with `:dt:` markers, `:dp:` labels, etc.) or normalized text (post-stripping). If raw, two equivalent definitions with different markup produce different hashes. If normalized, the hashes are actually useful for detecting glossary content changes between runs.

### Required change

Pin both hashes to the normalized text (same normalization used for similarity computation). Document the normalization version in the hash field name or in a companion metadata field.

---

## Summary

| # | Issue | Severity |
|---|---|---|
| 1 | No git diff cross-check for `insert` vs `promote` | High — same loophole as Wave A |
| 2 | Compound term rejection not generalized | High — Wave B will have new traps |
| 3 | Multi-sentence glossary parsing unspecified | Medium — ambiguity in implementation |
| 4 | `adapt` similarity floor too permissive | Medium — false positives possible |
| 5 | Recomputation tolerance unspecified | Low — should be exact |
| 6 | 12 existing Wave A terms need revalidation | Medium — incomplete gate data |
| 7 | Validator file state unspecified | Low — timing ambiguity |
| 8 | Hash target unspecified | Low — affects cross-run comparisons |

The plan is structurally sound and ready to execute once these items are addressed. Items 1 and 2 are the ones that directly prevent the next round of shortcuts.
