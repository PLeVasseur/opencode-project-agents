# Contributor experience issues triage plan (2026-01-30)

## Scope
- Repo: rustfoundation/safety-critical-rust-coding-guidelines
- Label: contributor experience
- Goal: identify duplicates/done and outline handling for each issue

## Immediate closures (duplicate or already done)
### #381 [CI / Automation] Only run PR tests that are relevant for the files being changed (open)
Action: close as duplicate of #200.
Steps:
1. Comment that #200 is the canonical tracking issue for CI scoping.
2. Close as duplicate.

### #141 Investigate having > 1 compliant and non-compliant example per coding guideline (open)
Action: close as completed.
Evidence:
- `.github/ISSUE_TEMPLATE/CODING-GUIDELINE.yml` supports up to 4 compliant and non-compliant examples.
- `scripts/common/guideline_templates.py` and `scripts/guideline_utils.py` generate multiple examples.

### #139 Define the tag "decidability" (open)
Action: close as completed.
Evidence:
- `src/process/style-guideline.rst` already defines decidability and how to interpret it.

## Open issues - planned handling
### #35 Improve process and front-matter (open)
Action: keep open.
Plan:
1. Inventory missing context in front-matter and process docs.
2. Update `src/process/*` and introduction content with rationale and alignment notes.
3. Cross-link to #83 and #245 where relevant.

### #36 Make guideline contributions to help find areas of improvement (open)
Action: keep open.
Plan:
1. Add a short status update noting current contributions and findings.
2. Link to any new issues created from contribution feedback.
3. Clarify expected next steps for contributors in the tracking issue.

### #38 Flesh out Guideline Lifecycle chapter (open)
Action: keep open.
Plan:
1. Draft lifecycle stages and transition criteria in `src/process/guideline-lifecycle.rst`.
2. Link from `src/process/index.rst` and the style guide.

### #40 Add Rust release coverage versioning (open)
Action: keep open.
Plan:
1. Define attributes for version and edition ranges in the guideline directive.
2. Implement parsing/rendering in the Sphinx extension and templates.
3. Update style guide and template guidance.

### #49 `guideline::release` listing should allow for ranges (open)
Action: keep open.
Plan:
1. Decide release range syntax (e.g., `1.70-1.79`, `>=1.70 <1.79`).
2. Update style guide and validation in scripts.
3. Add tests for range parsing.

### #50 local `guideline::scope`? (open)
Action: keep open.
Plan:
1. Decide whether to add `item` (or similar) scope.
2. Update `needs_scopes` in `src/conf.py` and style guide text.
3. Update the issue template dropdown.

### #58 Enforce manual paragraph IDs (open)
Action: keep open.
Plan:
1. Set `needs_id_required = True` in `src/conf.py`.
2. Confirm build behavior and update contributor docs.

### #65 Read the Docs diff view broken by sphinx-needs styling (open)
Action: keep open.
Plan:
1. Identify the diff-view selectors used by Read the Docs.
2. Add CSS overrides in `src/_static/*.css` to neutralize `.need` backgrounds in diff view.
3. Verify in RTD preview/diff.

### #78 Show full workflow from guideline => link to clippy lint (open)
Action: keep open.
Plan:
1. Pick a candidate guideline and identify a matching clippy lint (or gap).
2. Document the end-to-end workflow in docs.
3. Coordinate with clippy team for lint creation and policy.
Dependencies: #201, #82.

### #82 Look into guidelines that may qualify for clippy lints (open)
Action: keep open.
Plan:
1. Create a list of guidelines with likely clippy coverage.
2. Map to existing lints or identify missing lints.
3. Publish the list in docs or a tracking issue.

### #83 Examples of different guideline styles (open)
Action: keep open.
Plan:
1. Expand `src/process/style-guideline.rst` with defect vs subset guidance.
2. Provide concrete examples and category guidance.
3. Cross-link to profile/deviation guidance.
Dependencies: #142, #205.

### #142 Consider if we should have a `style` tag or similar for `subset` and `defect` to be applied (open)
Action: keep open.
Plan:
1. Decide whether to use tags or a dedicated field for flavor.
2. Update `src/conf.py` tag list or add a new field.
3. Document the choice in the style guide.
Dependencies: #205.

### #143 Fix the coding guideline issue template dropdown choices to be lowercase (open)
Action: keep open.
Plan:
1. Normalize dropdown options in `.github/ISSUE_TEMPLATE/CODING-GUIDELINE.yml`.
2. Ensure the parser and generation logic accept lowercase values.

### #144 Add Automatic Rebase GitHub action (open)
Action: keep open.
Plan:
1. Confirm policy for automatic rebasing in this repo.
2. Select and configure an action if approved.
3. Document behavior for contributors.

### #147 Create mechanism in Sphinx coding guidelines extension for supporting guideline reference => references addendum generation (open)
Action: keep open.
Plan:
1. Define requirements for the addendum output.
2. Implement Sphinx extension functionality.
3. Update docs and build process.

### #177 Potential for `Observations` section in Guidelines (open)
Action: keep open.
Plan:
1. Define the Observations section purpose and formatting.
2. Add an optional field to the issue template and generation pipeline.
3. Update style guide.

### #186 [Sphinx] [Automation] Make it possible to create hierarchical document structures (open)
Action: keep open.
Plan:
1. Identify acceptable heading syntax in guideline sections.
2. Update conversion pipeline to preserve structure.
3. Document allowed formatting and add tests.

### #194 Figure out how to preserve reading material and references (open)
Action: keep open.
Plan:
1. Choose a home for reading materials (process docs vs a dedicated section).
2. Seed with current references and define contribution rules.
3. Link from README or front-matter.

### #197 Create and maintain a list of rules being / to be implemented (open)
Action: keep open.
Plan:
1. Decide on a canonical list location (docs or GitHub project/label view).
2. Add a link from `README.md`.
3. Document how to update and maintain the list.

### #200 [CI/CD] Scope workflows to run only when relevant (open)
Action: keep open.
Plan:
1. Audit `.github/workflows/*` and identify relevant path filters.
2. Add `paths` or conditional job filters to reduce unnecessary runs.
3. Validate with PRs that touch doc-only files.
Dependencies: #381.

### #201 Add an extra field to Guidelines: "Lints for this Rule" (open)
Action: keep open.
Plan:
1. Add a field to the issue template.
2. Update generation scripts and Sphinx rendering to show lint references.
3. Update style guide and contributing docs.

### #205 Improve handling of guideline flavors (open)
Action: keep open.
Plan:
1. Decide on a dedicated flavor property vs tags.
2. Add validation requiring the flavor field.
3. Add a link field for related guidelines.
Dependencies: #217, #218, #142.

### #210 [Sphinx] [Automation] Make sure Issue -> PR conversion of tables is correct (open)
Action: keep open.
Plan:
1. Reproduce with a minimal issue example containing tables.
2. Adjust Markdown to RST conversion or formatting guidance.
3. Add snapshot tests for table conversion.

### #211 [Sphinx] [Automation] Make sure Issue -> PR conversion of code blocks is correct (open)
Action: keep open.
Plan:
1. Reproduce with real issue input and current pipeline.
2. Fix indentation handling in conversion logic if needed.
3. Add snapshot tests to prevent regressions.

### #214 Lag most recent Python by X releases (open)
Action: keep open.
Plan:
1. Choose a supported Python range and lag policy.
2. Update CI, docs, and `pyproject.toml` constraints.
3. Document the policy for contributors.

### #217 Add description of tiers to the contribution guide (open)
Action: keep open.
Plan:
1. Define and document the tiers in `CONTRIBUTING.md`.
2. Update issue template tag hints.
3. Backfill tags on existing guidelines if needed.
Dependencies: #205.

### #218 Introduce a new field to enable linking issues (open)
Action: keep open.
Plan:
1. Add a field to the issue template (link type + target guideline).
2. Update parser and guideline output to show links.
3. Document link types in `CONTRIBUTING.md`.

### #223 [Automation] Make sure Markdown to ReStructured Text conversion is correct (open)
Action: keep open.
Plan:
1. Define supported formatting and known failures.
2. Add regression tests for lists, tables, and code blocks.
3. Update `docs/issue-formatting-guide.md` to align with pipeline.
Dependencies: #210, #211.

### #237 Unclear how to select or add tags from reading CONTRIBUTING.md (open)
Action: keep open.
Plan:
1. Document `needs_tags` in `CONTRIBUTING.md` and link to `src/conf.py`.
2. Add guidance for adding new tags and running checks.
3. Update the issue template placeholder text if needed.

### #245 We should clarify which parts our guidelines cover: language + `core` + `std` (open)
Action: keep open.
Plan:
1. Add coverage statement to `README.md`.
2. Add front-matter mention in rendered docs (intro).
3. Align with goals in `GOALS.md`.

### #263 Deprecate the `sign-off: create pr from issue` label (open)
Action: keep open.
Plan:
1. Locate and remove automation that creates PRs on label toggle.
2. Confirm docs already updated; then delete or archive the label.

### #267 Add descriptions of the rule tags to the generated guidelines (open)
Action: keep open.
Plan:
1. Decide where tag descriptions should render (guideline pages or separate section).
2. Add rendering support using `needs_tags` descriptions.
3. Update style guide to reference the rendered tag glossary.

### #268 ISO/IEC 25000 (open)
Action: keep open.
Plan:
1. Add citations and definitions for relevant tag terms.
2. Align tag descriptions in `src/conf.py` and docs.
3. Document sources in bibliography/reading materials.

### #271 Document style guide (open)
Action: keep open.
Plan:
1. Add references to Chicago Manual and Merriam-Webster.
2. Decide and document spelling (e.g., "non-compliant").
3. Update the style guide and issue formatting guide if needed.

### #272 Each release should be hosted for stability of reference (open)
Action: keep open.
Plan:
1. Define versioned URL scheme and retention policy.
2. Update deploy workflow to publish versioned builds.
3. Add links to current and stable releases in docs.

### #307 Clarify that if Rust compiler releases are unknown, mark as "unknown" (open)
Action: keep open.
Plan:
1. Update issue template text from "unclear" to "unknown" or accept both.
2. Ensure parsing/validation treat "unknown" as valid.
3. Update documentation to match.

### #317 WAVE accessibility report of the Guidelines page (open)
Action: keep open.
Plan:
1. Re-run WAVE on current site to confirm findings.
2. Adjust colors, headings, and access keys in templates/CSS.
3. Remove layout table usage where possible and re-test.

## Closed issues (no further action)
- #371 [Guidelines-Bot] /label command has trouble parsing certain label names (closed)
- #362 [Guidelines-Bot] The bot might be too eager, we should probably fix that. (closed)
- #361 RST Preview suggestions (closed)
- #306 Add bibliography directive to guideline (closed)
- #303 Should code examples be self-contained? (closed)
- #291 Coding Guideline generated in reStructuredText should have its code examples tested and errors reported (closed)
- #290 Coding Guideline issue template should have more extra compliant and non-compliant fields (closed)
- #282 Make typo check step shorter (closed)
- #280 Split coding guidelines source files to make conflicts happen less (closed)
- #265 Guidelines text boxes render up to a fixed width and crop the rest (closed)
- #261 Exception(s) portion of Coding Guideline issue template not propagated to guideline in RST (closed)
- #224 [Automation] Modify workflow to, instead of PR, add comment with ReStructured Text (closed)
- #221 [Sphinx] [Automation] Make sure Issue -> PR conversion of hyperlinks is correct (closed)
- #212 Project configuration to allow CI to pass: likely Python version too new (closed)
- #173 [Automation] Update the FLS spec lock_file whenever it's trivial to do (closed)
- #166 Have a written explanation of how to fill the Guideline Form so everything is gucci (closed)
- #128 Field for citations and references (closed)
- #47 Document how to build the doc on different platforms (Linux, Windows, macOS) (closed)
