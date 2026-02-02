# Plan: Issue 647 (asm_cfg) and skill capture

## Goals
- Update FLS inline-assembly documentation for stabilized `asm_cfg`.
- Record paragraph-ID changes in `src/changelog.rst` for Rust 1.93.0.
- Build FLS to validate.
- Produce an issue report and grammar-driven validation artifacts.
- Write a generic `fls-issue-triage` skill capturing the workflow.

## Steps
1. Inspect upstream change context
   - Issue: https://github.com/rust-lang/fls/issues/647
   - Rust PR: https://github.com/rust-lang/rust/pull/147736
   - Reference PR: https://github.com/rust-lang/reference/pull/2063

2. Update inline-assembly spec
   - Adjust grammar to allow outer attributes on template strings and operands.
   - Add an Attributes subsection:
     - only `cfg`/`cfg_attr` are accepted on templates/operands,
     - other attributes are rejected,
     - `cfg`-false arguments are ignored,
     - at least one template string is required before operands.
   - Add examples mirroring the reference PR (no compile-fail directive).

3. Update changelog
   - Under Rust 1.93.0, add “Changed/New paragraphs” for `asm_cfg` with `:p:` IDs.

4. Paragraph IDs
   - Add `:dp:` to every new paragraph/list/table cell in `src/inline-assembly.rst`.
   - Run `./generate-random-ids.py` if any IDs are missing.

5. Build
   - Run `./make.py`.
   - If it fails, fix issues and re-run.

6. Report and validation
   - Create `$OPENCODE_CONFIG_DIR/reports/issue-647.md`.
   - Store grammar-driven validation snippets in `$OPENCODE_CONFIG_DIR/reports/issue-647/`.
   - Install toolchain with `rustup toolchain install 1.93.0` if needed.
   - Compile examples with `rustc +1.93.0`:
     - Positive: `asm!` with `#[cfg]` on templates/operands/options/clobber_abi.
     - Positive: `global_asm!` with `#[cfg]` on templates/options.
     - Negative: operand/options before template under `#[cfg(false)]` (expect error).
   - Summarize results in the report with key diagnostics.

7. Skill capture
   - Write `$OPENCODE_CONFIG_DIR/skills/fls-issue-triage/SKILL.md`.
   - Include: issue triage steps, link-following, mapping to FLS sections,
     changelog updates, ID handling, report creation, grammar validation,
     and verification commands.

## Notes
- Keep changes in `src/` only; avoid `build/` and `.linkchecker/`.
- Prefer FLS terminology and roles (`:t:`, `:c:`, `:s:`, `:std:`).
