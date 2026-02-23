# Glossary Prelude Split Plan

Date: 2026-02-05

## Goal
- Keep `src/glossary.rst.inc` as the static glossary while moving the shared prelude into `src/glossary.prelude.rst.inc`.
- Update the generator to read only the prelude file for header preservation.

## Scope
- Rename the static glossary file to a shorter path.
- Introduce a prelude-only include file.
- Update generator defaults, build glue, and migration helper paths.

## Steps
- [x] 1) Rename the static glossary file
  - [x] `git mv src/glossary.static.rst.inc src/glossary.rst.inc`.
  - [x] Update includes and tooling references to the new path.

- [x] 2) Add a prelude include file
  - [x] Create `src/glossary.prelude.rst.inc`.
  - [x] Copy only the prelude section from the current static glossary:
    - [x] Top anchor `.. _fls_bc2qwbfibrcs:`
    - [x] Glossary title line
    - [x] Title underline (exact length)
    - [x] Any blank lines or introductory text before the first entry
  - [x] Do not include any term entries or `.. _fls_...:` anchors.

- [x] 3) Update the generator
  - [x] Add `--prelude` option to `generate-glossary.py` with default `src/glossary.prelude.rst.inc`.
  - [x] `load_prelude` reads only the prelude file for header preservation.
  - [x] Remove `--static` and the static file existence check; the generator should not read the static glossary at all.
  - [x] Remove the `--update-static` flag and its writeback behavior so static updates only happen via `make.py`.
  - [x] Ensure the output still rebuilds entries from the Sphinx env only.

- [x] 4) Update tooling paths
  - [x] Search repo references for `glossary.static.rst.inc`, `--static`, and `--update-static`.
    - [x] Update references to the new paths/flags.
    - [x] Ignore `build/` artifacts/logs.
  - [x] `generate-glossary-entry.py` default glossary path -> `src/glossary.rst.inc`.
  - [x] `make.py` warning and overwrite paths -> `src/glossary.rst.inc`.
  - [x] `src/glossary.rst` include target -> `glossary.rst.inc`.
  - [x] `.github/workflows/ci.yml` diff target -> `src/glossary.rst.inc`.
  - [x] Update the migration helper outside the repo:
    `/home/pete.levasseur/opencode-project-agents/fls/glossary-insert-dp.py`.
  - [x] Update any `generate-glossary.py` invocations that pass `--static` (if any).

- [x] 5) Verify
  - [x] `uv run ./generate-glossary.py`
  - [x] `diff -u build/generated.glossary.rst src/glossary.rst.inc`
  - [x] `uv run ./make.py` (confirm mismatch warning behavior)
  - [ ] Optional: `uv run ./make.py --serve --use-generated-glossary`

## Notes
- `src/glossary.rst.inc` retains its full current content; the prelude file is the only input used for header preservation in the generator.
- If we later want to remove duplication, we can strip the header from `src/glossary.rst.inc` and treat it as entries-only.
- Make a commit after completing the steps.
