# Coding Guideline Review Plan

Date: 2026-02-02

Scope:
- Review PRs: #302, #368, #358, #305, #256
- Produce review artifacts under $OPENCODE_CONFIG_DIR/reviews

Approach:
1. Preflight
   - Confirm gh auth and repo access.
   - Confirm $OPENCODE_CONFIG_DIR/reviews exists.
2. PR intake (repeat for each PR)
   - Collect PR context with `gh pr view` (title, body, labels, reviewers, checks).
   - Collect full diff with `gh pr diff`.
   - Note `closes #<id>` presence if applicable.
3. CI and checks
   - Validate `build` and `check_typos` status.
   - Record any failures and classify per policy.
4. Guideline validation
   - File placement and chapter index updates.
   - Required fields and valid values.
   - RFC 2119 language in title and amplification.
   - Exceptions handling.
5. FLS linkage and scope alignment
   - Verify `:fls:` paragraph IDs and scope match.
   - Ensure content maps to FLS without overreach.
6. Citations and bibliography
   - No inline URLs; use `:std:`, `:cite:`, `:bibentry:`.
   - Check citation key format and consistency.
7. Technical correctness
   - Validate all claims against authoritative sources.
   - Treat unverified or incorrect claims as blocking.
8. Claims map
   - Create `claims.md` per PR with summary table and per-claim entries.
   - Include field-choice claims with justification.
9. rust-example validation
   - Require compliant and non-compliant examples.
   - Validate directives and miri usage for unsafe code.
10. Cross-guideline consistency
   - Check overlaps, replacements, and cross-references.
11. Verdict and artifacts
   - Decide approve/comment/request changes based on findings.
   - Write `summary.md` and `comment-###.md` files per PR.

Deliverables:
- $OPENCODE_CONFIG_DIR/reviews/pr-<number>-<short-slug>/summary.md
- $OPENCODE_CONFIG_DIR/reviews/pr-<number>-<short-slug>/comment-###.md (as needed)
- $OPENCODE_CONFIG_DIR/reviews/pr-<number>-<short-slug>/claims.md

Order:
- Process PRs in the order provided: 302, 368, 358, 305, 256.
