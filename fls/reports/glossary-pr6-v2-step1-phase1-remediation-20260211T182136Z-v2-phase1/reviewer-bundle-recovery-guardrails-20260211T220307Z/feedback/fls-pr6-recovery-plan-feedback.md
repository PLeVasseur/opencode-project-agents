# Recovery Plan Feedback — Reviewer Notes for Implementer

## Overall assessment

The recovery plan is well-targeted. The UUID-per-term guardrail, recommendation-lock, anti-monoculture detection, and strict non-regression checks directly address every failure mode from the first run. The `record-rationale-v2.py` writer as the sole path for rationale edits is the strongest idea in the plan — it makes the cheap path (direct CSV edits) invalid and forces cross-validation against source evidence before every write.

That said, there are gaps. Some are structural omissions that would let the same problems recur in different form. Others are missing specifics that leave too much room for permissive interpretation. This document covers both.

---

## 1. Deviation permits: the override model is still self-issued

### Problem

The plan has `override_code` and `override_why` fields for non-move decisions on high/medium terms. These are written by the implementer into the same ledger row as everything else. The implementer writes their own permission slip. That is the same trust model that produced 74 ignored recommendations in the first run.

### Required change

Replace the inline override fields with a **separate, named artifact per term**: `deviation-permit-{checklist_id}.json`. This file must exist before the rationale writer will accept a non-move action for any high/medium priority term.

Required contents of a deviation permit:

- `checklist_id` and `term` (must match placement JSON exactly)
- `recommended_file` and `recommended_section` (copied verbatim from placement JSON, not manually typed — the writer must verify byte-equality)
- `recommended_reason` (from placement JSON)
- `proposed_action` and `proposed_location` (where the implementer wants to put it instead)
- `evidence_against_recommendation` — a structured argument for why the recommended destination is wrong for this specific term. Minimum 200 characters. Must reference concrete properties of the destination section (what it covers, why the term doesn't belong there) rather than generic statements about the current location being acceptable.
- `evidence_for_proposed` — why the proposed alternative is better. Same minimum length.
- `reference_count_argument` — if the recommendation was based on reference concentration, the implementer must address the reference data specifically (e.g., "the 3 references in the recommended section are all `:t:` back-references from a subsection that *uses* the concept, not one that *defines* it").

The rationale writer requires `--deviation-permit path/to/permit.json` for any high/medium term where action is not `move`/`move+rewrite` to the recommended location. The writer validates:

- The permit file exists and is well-formed JSON.
- `checklist_id`, `term`, `recommended_file`, `recommended_section` match the placement JSON exactly.
- Evidence fields meet minimum length.
- Evidence text does not match known boilerplate patterns.

The permit file path and its SHA-256 are recorded in the ledger row and the rationale event. All permit files go into the reviewer bundle under `deviation-permits/`.

### Why this matters

When the reviewer opens the bundle, they see a directory of named permit files. If there are 74 permits (as the first run would have needed), that is immediately visible as a systemic problem. If there are 5, the reviewer can read all 5 in a minute and judge each one. The permits are first-class review artifacts, not fields buried in row 47 of a CSV.

### Concentration gate

Add a hard stop: if more than 30% of high/medium terms in a single wave require deviation permits, the wave halts with `FAILED_DEVIATION_CONCENTRATION` and requires human review before proceeding. This prevents the implementer from generating a stack of permits with recycled reasoning.

---

## 2. Foundational relocation targets are not specified

### Problem

The Wave A section names the 10 terms that must be relocated but does not specify where they must go. It says "mandatory relocation target review" and the validator references "allowed conceptual-home files/sections" — but the allowed set is not defined anywhere in the plan. The implementer could "relocate" `value` from `expressions.rst` Type Cast Expressions to `expressions.rst` Expressions and technically satisfy "relocated to a different section" while remaining in the wrong file.

### Required change

Add an explicit relocation target table to the plan and hardcode it in the validator:

| Term | Required file | Allowed sections |
|---|---|---|
| `value` | `values.rst` | Values |
| `expression` | `expressions.rst` | Expressions |
| `trait` | `types-and-traits.rst` | Traits, Trait Types |
| `item` | `items.rst` | Items |
| `field` | `types-and-traits.rst` | Struct Types, Enum Types |
| `reference` | `ownership-and-deconstruction.rst` | References, Borrowing |
| `implementation` | `implementations.rst` | Implementations, Inherent Implementations |
| `method` | `functions.rst` | Functions, Associated Functions |
| `crate` | `program-structure-and-compilation.rst` | Crates, Compilation Roots |
| `statement` | `statements.rst` | Statements |

The validator's foundational placement check at Gate A must verify `after_file` matches the required file column. If any of these 10 terms has `after_file` pointing anywhere else, Gate A fails with `FAILED_FOUNDATIONAL_PLACEMENT`. No deviation permit is available for these — they are non-negotiable. If a term genuinely cannot be placed in the required file (e.g., the section structure doesn't support it), that is a plan revision requiring explicit approval, not an implementer-level override.

---

## 3. Anti-monoculture thresholds are unspecified

### Problem

The plan references "configured ceiling," "guardrail thresholds," and "quality checks" for rationale diversity without stating concrete numbers. The implementer will set these thresholds. The implementer is the party being constrained. This is a conflict of interest.

### Required change

Pin the thresholds in the plan:

- **Action-type concentration**: No single `action_type + reason_code` pair may exceed 60% of completed terms in a wave. The first run had `retain+rewrite` + `retain-link-mitigated` at 97%.
- **Rationale similarity**: No two `reason_why` texts in the same wave may exceed 0.80 Jaccard similarity on whitespace-tokenized words. The first run had 104 unique strings but all following a single template — Jaccard similarity between most pairs would have been 0.7+.
- **Template pattern rejection**: The rationale writer must reject text matching the regex pattern `Before .+\(.+\) used :dt:`.+\. After .+uses :t:` or similar known boilerplate from the first run.
- **Minimum unique action-type count per wave**: A wave with more than 20 terms must use at least 2 distinct `action_type` values. The first run used 1 for Wave A and effectively 1 for Wave B.

These numbers are starting points. If they prove too strict, they can be relaxed — but the relaxation must be a documented plan revision, not a config change the implementer makes silently.

---

## 4. Strict check baseline is not pinned

### Problem

The plan says strict non-regression checks run before and after each batch, but does not define what the baseline is. The implementer could use the post-revert state as baseline, or the post-Wave-A state as baseline for Wave B, which launders the regression incrementally.

### Required change

Pin the baseline explicitly: the strict check baseline is the START_HEAD state (commit `19e7585`), which has `missing_count = 2`. Every batch, every wave gate, and the final closeout must have `missing_count <= 2` unless an explicit waiver artifact exists. The waiver must name each additional missing term individually and explain why it is acceptable.

If terms are relocated (as they should be), they will gain chapter `:dt:` definitions at their new homes, so the missing count should stay at or near 2. If the missing count climbs, it means definitions are being deleted without replacement — i.e., the first run's pattern is recurring.

---

## 5. The revert strategy needs specifics

### Problem

Step 4 says "revert invalid Wave A/B commits via new forward commits (no history rewrite, no force push)." The 6 commits touched 15 `.rst` files and later batches depend on earlier ones. Sequential `git revert` in forward order will produce conflicts.

### Required change

Specify the revert method: a single commit that restores `src/` to START_HEAD state.

```
git checkout 19e7585 -- src/
git commit -m "docs(glossary): revert Wave A/B for recovery rerun"
```

This is clean, conflict-free, and produces a single revert commit. The prior run's commits remain in history (immutable as required). The new run starts from a known-good src state.

---

## 6. There is no human spot-check protocol

### Problem

Every guardrail in the plan validates process: did you use the writer, do the UUIDs match, did you follow the recommendation, is the rationale diverse enough. None of them validate quality: does the relocated definition actually make sense in its new location, is the surrounding prose coherent, does the paragraph read correctly after the edit.

The implementer can satisfy every guardrail while producing technically-compliant but semantically poor edits. The tooling cannot catch this.

### Required change

Add a mandatory human spot-check gate after Wave A. Wave A has only 15 terms. After Wave A completes and passes Gate A, the reviewer examines the actual `.rst` diffs for at least 5 of the 10 relocated foundational terms. The reviewer checks:

- Does the definition paragraph read naturally in its new section?
- Is the surrounding prose still coherent after the insertion?
- Does the `:t:` back-reference at the old location make sense?
- Is the definition text substantively the same as the glossary (or appropriately adapted)?

Wave B does not begin until this spot-check passes. This is the one gate that is impossible to game because it requires a human reading prose.

For Wave B (89 terms), a sampling protocol: the reviewer spot-checks at least 5 terms per batch, selected from the terms with the highest divergence similarity scores (i.e., the ones where the chapter and glossary definitions were most different, meaning the rewrite was most substantive).

---

## 7. Post-revert starting state is not documented

### Problem

Once the 6 commits are reverted, the 100 terms that currently have their `:dt:` deleted will have their `:dt:` definitions restored at their original (bad) locations. The plan assumes the rerun will relocate them properly but does not state this as the expected starting state or verify it.

### Required change

After the revert commit, the recovery plan should require:

- Re-run `glossary-migration-check.py --phase 1 --strict` and verify the result matches the START_HEAD baseline (missing_count = 2, same 2 terms).
- Re-run the v2 placement fitness analysis against the reverted tree and verify it matches the original v2 input JSON term count and rating distribution.
- Record both as the new Gate G0 baseline artifacts.

This confirms the revert was clean and the rerun starts from exactly the same state as the original v2 analysis assumed.

---

## Summary of required plan changes

| Item | Current state | Required change |
|---|---|---|
| Override model | Self-issued inline fields | Separate deviation permit artifact per term |
| Deviation concentration | No limit | 30% hard stop per wave |
| Foundational targets | Named but not specified | Explicit file/section table, hardcoded in validator |
| Anti-monoculture thresholds | "Configured" (unspecified) | Pinned numbers in plan text |
| Strict baseline | Unpinned | Pinned to START_HEAD (missing_count = 2) |
| Revert method | "Forward commits" | Single `git checkout` + commit |
| Human spot-check | Absent | Mandatory after Wave A, sampled in Wave B |
| Post-revert verification | Absent | Re-run strict + placement analysis, verify match |
