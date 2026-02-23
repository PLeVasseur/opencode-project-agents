# Commit4 CI format remediation summary

- run_id: `20260213T205932Z`
- branch: `glossary-single-source-phase1-repack-upstream-main`
- upstream_main_pin: `fb8a46795eda1f1db5e3232002fd94a270bfbffd`
- old_commit4_sha: `1132eb4c632c0d1b65bc7000d9bced2fca3842bd`
- new_commit4_sha: `8e93f35547fcc123ec47ba723ed13129bc19600f`

## What changed

- Scoped remediation to `tools/verify-html-diff.py`.
- Applied Black formatting and manual line wrapping required for Flake8 E501.
- Rebuilt capstone commit from `COMMIT3_SHA` so only commit4 changed.

## Local gates

- `uvx black . --check --diff --color`: pass
- `uvx flake8 . --exclude .venv`: pass
- `./tools/verify-html-diff.py --mode repro --ref HEAD`: pass
- `./tools/verify-html-diff.py --mode repro --ref 8e93f35547fcc123ec47ba723ed13129bc19600f`: pass

## Topology confirmation

- Commit count over pin: `4`
- First three commits unchanged:
  - `06da2fde57a1b195325e91fa322614ce1bbe2d04`
  - `85a60b64f816b284a3191dfc730b9e5d8ac49030`
  - `6716db3a49cfbffa30ccac3a51cf76ebd9ab60a7`

## Push and CI

- Push used explicit lease against old remote SHA `1132eb4c632c0d1b65bc7000d9bced2fca3842bd`.
- Remote branch now points to `8e93f35547fcc123ec47ba723ed13129bc19600f`.
- CI run: `https://github.com/PLeVasseur/fls/actions/runs/22002785018`
- CI conclusion: `success`
- Required job/steps status:
  - `Build the documentation`: success
  - `Verify Python code formatting`: success
  - `Lint Python code with flake8`: success
