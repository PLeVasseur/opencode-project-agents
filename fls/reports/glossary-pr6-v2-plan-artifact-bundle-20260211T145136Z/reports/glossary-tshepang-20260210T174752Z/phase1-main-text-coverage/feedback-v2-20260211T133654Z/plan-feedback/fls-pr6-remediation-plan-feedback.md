# Feedback on V2 Remediation Plan Proposal

## Overall Assessment

This is a well-structured plan. The core tradeoffs from the analysis were clearly internalized. The section-by-section feedback below covers where I strongly agree, where I'd push back or refine, and one missing piece.

## Where I Strongly Agree

**Stage 1 (Policy Gate)** is exactly right and correctly identified as critical. The "conceptual-home-first for foundational terms" policy is the right call. The v2 PR demonstrated what happens without this policy — `value` ends up defined inside Type Cast Expressions, `expression` inside Type Inference, `trait` inside Path Expression Resolution. These are specification-defining terms; readers will look for them in their home chapters, not wherever they happen to first appear. The point about treating recommender targets as "signals, not authoritative destinations" also shows good judgment — the analysis flagged reference density patterns, but the recommendations for terms like `value` (→ Type Cast Expressions) were clearly wrong as actual placement advice.

**Stage 4 (Quality Controls)** — the requirement to rewrite inline definitions as standalone definitional sentences is exactly what's needed. The sim=0.073 `arity` and sim=0.059 `crate root module` cases happened because `:dt:` was slapped onto an incidental mention rather than crafting a proper definition. The rule "when relocating, convert old occurrence to `:t:`" is clean and prevents duplicate canonicals.

**Stage 5 (Validation Gates)** — the layered gating (batch → wave → milestone → final) is appropriate for a 233-term remediation. Running `glossary-migration-check.py --phase 1 --strict` per wave catches regressions early.

**The closure thresholds** are ambitious but correct. High priority 49 → 0 is achievable because most of those 49 are foundational terms that should return home. Low reliability 160 → near 0 is the harder target but the right one.

## Where I'd Push Back or Refine

**Stage 2 — the 233 number may be inflated.** The plan says "172 placement poor/questionable + 160 divergence low, overlap accounted for." But a significant chunk of those 160 low-reliability divergences will self-resolve once placement is fixed. When `crate` moves back from `macros.rst` (where it's defined in a sentence about proc-macro crates) to its conceptual home (where the definition will match the glossary), the divergence disappears without any separate divergence remediation. I'd estimate 60–80 of the 160 divergences are placement-caused. So the true unique backlog is probably closer to 170–180 terms, not 233. I'd suggest the plan acknowledge this and let Waves A/B settle before scoping Wave C.

**Stage 3 — Wave structure could be sharper.** The plan lists Wave A as "foundational/high-risk terms first" with examples, but doesn't quantify it. From the analysis, there are roughly 10–15 truly foundational terms (`value`, `expression`, `type`, `trait`, `construct`, `entity`, `name`, `item`, `field`, `reference`, `implementation`, `method`, `crate`, `module`, `statement`). These should be Wave A explicitly, and they should all go back to their conceptual home chapters with a simple rule: if the term names the chapter or section it belongs to, that's where it lives. Wave A should be small and decisive — these 15 terms set the pattern everything else follows.

**Stage 3 — 20 terms per batch may be too granular** for Waves C/D. Once the policy is established and the pattern is clear from Waves A/B, the remaining low-risk terms could go in larger batches (40–50). The per-batch validation overhead of small batches will slow things down without proportional quality benefit for routine cases. I'd suggest 20/batch for Waves A/B (high risk, pattern-setting) and 40–50/batch for C/D (mechanical follow-through).

**Stage 6 — the reporting deliverables may be overengineered.** Five separate markdown reports (`phase1-v2-before-after-why.md`, `placement-v2-resolution-summary.md`, `divergence-v2-resolution-summary.md`, `core-term-disposition.md`, `open-issues.md`) plus per-batch annex tables is a lot of documentation overhead for what is ultimately a preparatory phase of the glossary migration. The master checklist/ledger from Stage 2 already captures the per-term before/after/why. I'd consolidate to two deliverables: the ledger itself (which is the source of truth) and one summary report. The v3 re-analysis (Stage 7) will provide the authoritative "did it work" answer — intermediate reporting should be lightweight.

**Stage 0 — `./make.py --check-links` may not work in isolation.** The FLS build requires Sphinx with custom extensions. If this is being run outside the full Ferrocene build system, verify the build toolchain works before locking the baseline. Minor point but could waste time.

## One Missing Piece

The plan doesn't address **the 2 missing terms** (`crate import` → `[crate import]s`, `declaration` → `[declaration]s`). Stage 4 mentions "resolve with an explicit decision" but doesn't propose one. My recommendation: these plural `:dt:` forms are fine — the glossary has singular entries but the FLS's `:dt:` system handles pluralization through the bracket syntax. Just document that `[crate import]s` serves as the canonical definition for `crate import` and close the finding.

## Bottom Line

The plan is sound. The policy decision (conceptual-home-first) is correct. The wave structure is right in principle but could be tightened on scoping and batch sizes. The reporting is overweight for the task. If I had to summarize the feedback in one sentence: **sharpen Wave A to exactly the 10–15 foundational terms, let their resolution cascade into the divergence numbers before scoping Waves C/D, and cut the reporting deliverables in half.**
