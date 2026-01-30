# FLS Project Instructions

FLS is a Sphinx-built Rust language specification. Source content lives in `src/`.

## Quick Commands

- `./make.py` build HTML
- `./make.py --serve` live rebuild at `http://localhost:8000`
- `./make.py --clear` clean rebuild
- `./make.py --check-links` run Rust linkchecker
- `./generate-random-ids.py` generate paragraph IDs
- `uv lock --upgrade` update Python dependency lockfile

## OpenCode Setup

- Ensure `opencode-env.sh` is sourced so `OPENCODE_CONFIG_DIR` is set and project skills are discoverable.

## Plans

- Plan documents live in `$OPENCODE_CONFIG_DIR/plans/` and must not be written into the repo.

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
- Use spec roles: `:t:`, `:c:`, `:s:`, `:std:` and the `.. syntax::` directive

## Progressive Disclosure

- For details on IDs/roles/syntax, read `exts/ferrocene_spec/README.rst` only when needed
- For lint behavior, see `exts/ferrocene_spec_lints/` and `src/conf.py`
- For deeper workflows, load skills: `fls-paragraph-ids`, `fls-roles-definitions`, `fls-syntax-blocks`, `fls-informational`, `fls-build-links`, `fls-changelog-verification`

## Avoid

- Do not edit `build/` or `.linkchecker/`
