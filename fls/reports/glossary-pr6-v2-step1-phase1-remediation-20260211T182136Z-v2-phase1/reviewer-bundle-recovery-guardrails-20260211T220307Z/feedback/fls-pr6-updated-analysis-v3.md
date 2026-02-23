# FLS PR #6 Updated Analysis — v3 (Post-Wave A+B)

## Context

This analysis runs against commit `63bde89` (END_HEAD), which includes six new commits added by the Wave A+B remediation cycle on top of the v2 baseline at `19e7585` (START_HEAD). It serves as the externally-provided v3 artifact required by the Gate B+ checkpoint before Wave C/D scope can be frozen.

The reviewer bundle for this analysis covers the complete Wave A (15 foundational terms, 1 batch, 1 commit) and Wave B (89 high/medium-priority terms, 5 batches, 5 commits) execution, touching 15 of 28 `src/*.rst` files across 104 remediated terms with zero quarantined terms and zero batch failures.

## Placement Fitness

### v2 → v3 delta

| Metric | v2 | v3 | Delta |
|---|---|---|---|
| Terms in scope | 776 | 676 | −100 |
| Good | 302 | 326 | +24 |
| Acceptable | 302 | 283 | −19 |
| Questionable | 111 | 53 | −58 |
| Poor | 61 | 14 | −47 |
| Forward references | 248 | 197 | −51 |
| High priority | 49 | 4 | −45 |
| Medium priority | 49 | 0 | −49 |

The 100 terms removed from scope are exactly the 100 Wave A+B terms whose chapter `:dt:` definitions were converted to `:t:` references as part of the conceptual-home-first policy. Four Wave B terms (`code point`, `floating-point type`, `implementation`, `size`) remain in scope because their `:dt:` definitions were retained in place after manual review confirmed the canonical definition resided at a different anchor than the analyzer flagged.

### Adjusted ratings (accounting for conceptual-home)

| Rating | v2 | v3 | Delta |
|---|---|---|---|
| Good | 302 | 326 | +24 |
| Acceptable | 302 | 283 | −19 |
| Acceptable-at-home | 65 | 54 | −11 |
| Questionable | 58 | 9 | −49 |
| Poor | 49 | 4 | −45 |

33 terms improved their fitness rating (1 questionable→good, 18 acceptable→good, 14 questionable→acceptable). One term (`future operand`) degraded good→acceptable due to reference redistribution from Wave B edits. Net quality trajectory is strongly positive.

### Remaining high-priority terms (4)

All four were processed in Wave B and have ledger status `completed` / `resolved-high`:

1. **`implementation`** (WA-011) — `retain+rewrite` in `generics.rst`. Rewrote `:dt:` to `:t:` while keeping `:dt:generic implementation` as the local defined concept. Analyzer still scores the definition poorly because the old `:dt:` anchor was replaced but a different definition text remains at the same location.

2. **`floating-point type`** (WB-014) — `retain` in `types-and-traits.rst`. Manual review confirmed the conceptual owner at `types-and-traits.rst:392` already uses `:t:floating-point type` correctly. No change needed.

3. **`code point`** (WB-008) — `retain` in `lexical-elements.rst`. Manual review confirmed `lexical-elements.rst:33` already uses `:t:code point` in the Character Set section. No change needed.

4. **`size`** (WB-013) — `retain` in `types-and-traits.rst`. Manual review confirmed `types-and-traits.rst:1640` already uses `:t:size` in the Type Layout section. No change needed.

These four represent deliberate retain decisions, not missed work. The analyzer's "poor" rating reflects the original flagged location, not the actual canonical usage site.

## Definition Divergence

### v2 → v3 delta

| Category | v2 | v3 | Delta |
|---|---|---|---|
| Exact match | 461 | 442 | −19 |
| Cosmetic | 50 | 48 | −2 |
| Glossary xref | 24 | 24 | 0 |
| Extended | 27 | 27 | 0 |
| Chapter redirect | 1 | 1 | 0 |
| Moderate divergence | 44 | 39 | −5 |
| Inline definition | 7 | 6 | −1 |
| **Significant reword** | **160** | **87** | **−73** |
| Missing from chapter | 2 | 102 | +100 |
| Chapter only | 185 | 185 | 0 |

### Interpretation

The 100-term increase in `missing_from_chapter` is the direct consequence of Wave A+B's remediation: converting `:dt:` chapter definitions to `:t:` references removes the chapter-side definition, so the term now only has a glossary entry. This is the expected and intended outcome of the conceptual-home-first policy — the glossary retains the canonical definition while chapters reference it.

The significant-reword count dropped from 160 to 87 (−73), meaning 73 previously low-reliability divergences were resolved by the Wave A+B edits. The remaining 87 significant-reword terms are candidates for Wave C scope.

### Reliability summary

| Reliability | v2 | v3 | Delta |
|---|---|---|---|
| High | 535 | 514 | −21 |
| Medium | 79 | 73 | −6 |
| Low | 160 | 87 | −73 |
| Missing | 2 | 102 | +100 |
| New term | 185 | 185 | 0 |

## Strict Phase Check Status

The `glossary-migration-check.py --phase 1 --strict` check reports 100 missing terms at Gate B. These are exactly the 100 terms whose `:dt:` definitions were converted to `:t:` references. The strict check expects every glossary term to have a chapter `:dt:` counterpart; the conceptual-home-first policy deliberately violates this expectation for terms where the glossary is the canonical owner and chapters should reference rather than redefine.

This is a known and accepted consequence. Wave C/D will address remaining divergence terms, which may restore some `:dt:` definitions. The build check and link-check both pass cleanly at Gate B.

## Reviewer Bundle Cross-Validation

The reviewer bundle evidence confirms:

- **Execution integrity**: `pass` — all checks green (non-dry-run, Wave A+B complete, non-zero commits, changed src files non-empty).
- **Batch outcomes**: 6 batches (1 Wave A + 5 Wave B), all 104 terms completed, zero quarantined, zero failures.
- **Ledger composition**: 101 `retain+rewrite` actions, 3 `retain` actions. 101 with `semantic_change_flag=clarification-only`, 3 with `none`. 101 requiring review attention, 3 not.
- **Commit manifest**: 6 commits from `52f1285` (Wave A) through `63bde89` (Wave B final), all on branch `glossary-step-1-main-text-coverage`.
- **Validator gate**: 104/104 parent items checked, 624/624 sub-items checked, all `resolved-high`.
- **Build and link checks**: Both pass at Gate A and Gate B boundaries.

## Gate B+ Scoping Recommendations

### Wave C candidates (significant-reword residuals)

87 terms with `reliability=low` / `match_category=significant_reword` remain after Wave A+B. These are definition-quality issues where the glossary and chapter wordings diverge substantially. Wave C should focus on rewriting chapter definitions to align with glossary canonical text or vice versa, using `retain+rewrite` or `rewrite` actions.

### Wave D candidates (placement poor/questionable residuals)

After adjusting for conceptual-home, the residual placement issues are:
- 4 poor (all deliberately retained with justification)
- 9 questionable (no recommended relocation target or at conceptual home)
- 38 low-forward-ref (acceptable at home but with forward-reference debt)

Given that all 4 high-priority items were manually reviewed and retained, and zero medium-priority items remain, Wave D's scope is minimal. The 9 questionable terms and 38 forward-reference terms could be reviewed but represent low-risk items.

### Recommended scope freeze

- **Wave C**: 87 significant-reword terms from divergence analysis.
- **Wave D**: 9 questionable + 38 low-forward-ref = 47 terms from placement analysis. Alternatively, defer Wave D entirely given the low risk profile.

## File inventory

| Artifact | Description |
|---|---|
| `fls-pr6-placement-fitness-v3.json` | 676 terms, full placement fitness analysis |
| `fls-pr6-definition-divergence-v3.json` | 961 terms, full definition divergence analysis |
| `fls-pr6-updated-analysis-v3.md` | This report |
| `fls-pr6-v3-wave-ab-review.md` | Reviewer-focused Wave A+B execution review |
