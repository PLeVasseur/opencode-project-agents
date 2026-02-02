# FLS Project Instructions

Verify `OPENCODE_CONFIG_DIR` immediately after reading this file, regardless of mode.

FLS is a Sphinx-built Rust language specification. Source content lives in `src/`.

## Edition Scope

- FLS documents the Rust 2021 edition. When aligning with the Rust Reference, exclude edition-specific rules introduced in 2024+ unless explicitly backported.

## Quick Commands

- `./make.py` build HTML
- `./make.py --serve` live rebuild at `http://localhost:8000`
- `./make.py --clear` clean rebuild
- `./make.py --check-links` run Rust linkchecker
- `./generate-random-ids.py` generate paragraph IDs
- `uv lock --upgrade` update Python dependency lockfile

## OpenCode Setup

- Ensure `opencode-env.sh` is sourced so `OPENCODE_CONFIG_DIR` is set and project skills are discoverable.

## Version Control

- Use Conventional Commits for commit messages: `type(scope?): subject`.
  - Example: `docs(inline-assembly): document asm_cfg attributes`.
  - Common types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`.
- Branch names should be plain, descriptive phrases without a type prefix.

## Pull Requests

- Upstream: `https://github.com/rust-lang/fls`.
- Work on a feature branch and push to the fork (`PLeVasseur/fls`) first.
- Create a PR on the fork for review, then open the upstream PR from the fork branch.
- Do not push directly to upstream or force-push.
- PR body format:
  - `## Summary`
  - `## Reference alignment` (include Reference PR/section links and deviations)
  - `## Testing`
- Include `Closes #<issue>` as the last line in `## Summary` when applicable.

## Plans

- Plan documents live in `$OPENCODE_CONFIG_DIR/plans/` and must not be written into the repo.

## Reports

- Report artifacts must be written under `$OPENCODE_CONFIG_DIR/reports/` and must not be written into the repo.

## Temporary artifacts and deletions

- Temporary artifacts (including intermediate logs or analysis outputs) must be written under `$OPENCODE_CONFIG_DIR/` and never in the repo.
- Do not delete files outside the repo, including under `$OPENCODE_CONFIG_DIR/`, without explicit user permission.

## Reviews

- Review comment drafts live in `$OPENCODE_CONFIG_DIR/reviews/<pr-number>/commentN.md` and include YAML with `file` and `line_hint` (right-side/new line in the PR diff).

## Skills

- Paragraph IDs: `skills/fls-paragraph-ids/SKILL.md`
- Roles definitions: `skills/fls-roles-definitions/SKILL.md`
- Syntax blocks: `skills/fls-syntax-blocks/SKILL.md`
- Informational style: `skills/fls-informational/SKILL.md`
- Build links: `skills/fls-build-links/SKILL.md`
- Changelog verification: `skills/fls-changelog-verification/SKILL.md`

## Where Things Live

- `src/` spec source (`.rst`), with the toctree in `src/index.rst`
- `src/conf.py` Sphinx config and lint configuration
- `exts/` custom Sphinx extensions and lints
- `themes/fls/` HTML theme and CSS
- `build/` generated output (do not edit)

## Authoring Rules

- Each section must include an explicit anchor: `.. _fls_<id>:`
- Each paragraph/list item/table first cell must start with `:dp:`; required everywhere except `index` and `changelog` (see `src/conf.py`)
- Glossary sections must be alphabetized (linted)
- When introducing a new term, define it in the glossary with `:dt:` and use `:t:` in prose thereafter.
- Use spec roles: `:t:`, `:c:`, `:s:`, `:std:` and the `.. syntax::` directive

## Progressive Disclosure

- For details on IDs/roles/syntax, read `exts/ferrocene_spec/README.rst` only when needed
- For lint behavior, see `exts/ferrocene_spec_lints/` and `src/conf.py`
- For deeper workflows, load skills: `fls-paragraph-ids`, `fls-roles-definitions`, `fls-syntax-blocks`, `fls-informational`, `fls-build-links`, `fls-changelog-verification`

## Avoid

- Do not edit `build/` or `.linkchecker/`
