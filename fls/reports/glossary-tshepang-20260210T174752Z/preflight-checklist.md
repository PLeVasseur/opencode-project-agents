# Preflight checklist

- [x] `OPENCODE_CONFIG_DIR` set and writable
- [x] `origin` remote points to `git@github.com:PLeVasseur/fls.git`
- [x] `gh auth status` succeeded
- [x] Baseline toolchain present (`uv --version`, `./make.py --help`)
- [x] Generator availability branch check handled
  - Current branch (`glossary-single-source-phase1`): `./generate-glossary.py --help` succeeded
  - `origin/main`-based worktrees: generator absent at start; deferred check recorded and enforced before phase 5
- [x] `origin/main` and `origin/glossary-single-source-phase1` verified after fetch
- [x] `../fls-wt/` topology verified reusable
- [x] Target branch names verified reusable
