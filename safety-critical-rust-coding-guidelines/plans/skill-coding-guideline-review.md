# Skill: Coding Guideline Review

## Context
- We need a new OpenCode skill that formalizes how to review coding guideline PRs.
- The skill should be grounded in merged PRs #234, #232, #220 and the repo's guideline style, validation checks, and goals.
- The skill must enforce CI awareness, Rust Reference and std/core/alloc citations, and external standard coverage (CERT, MISRA) when claimed.

## Goals
- Create a discoverable skill named `coding-guideline-review` under `$OPENCODE_CONFIG_DIR/skills/`.
- Provide a clear, repeatable review checklist aligned with repo style and validation rules.
- Update `~/opencode-project-agents/safety-critical-rust-coding-guidelines/AGENTS.md` to list the new skill.

## Plan
1. Review PRs #234, #232, #220 via `gh` and inspect the corresponding guideline files in `src/coding-guidelines/`.
2. Extract review practices from repo docs and checks:
   - `src/process/style-guideline.rst`, `CONTRIBUTING.md`, `GOALS.md`
   - `exts/coding_guidelines/*` checks (inline URLs, bibliography, FLS, rust-example, required fields).
3. Draft the skill at `$OPENCODE_CONFIG_DIR/skills/coding-guideline-review/SKILL.md` with:
   - YAML front matter: name, description, compatibility
   - Sections: Purpose, Inputs, Steps, Output
   - Steps covering CI, guideline structure/fields, FLS linkage, citations/bibliography, rust-example and Miri rules, Rust Reference and std/core/alloc linkage, and external standards coverage.
4. Update `~/opencode-project-agents/safety-critical-rust-coding-guidelines/AGENTS.md` to include the new skill.
5. Verify ASCII-only edits and consistent formatting with existing skills.

## Success criteria
- New skill file exists at `$OPENCODE_CONFIG_DIR/skills/coding-guideline-review/SKILL.md` with Purpose, Inputs, Steps, and Output sections.
- `~/opencode-project-agents/safety-critical-rust-coding-guidelines/AGENTS.md` lists `coding-guideline-review` under Skills.
- The skill steps explicitly cover CI status, guideline structure and required fields, FLS linkage, citation and bibliography rules, rust-example validation, Miri requirements for unsafe code, Rust Reference and std/core/alloc links, and external standards coverage when claimed.
