# FLS Audit Deployments Endpoint Plan

## Goal

Make `scripts/fls_audit.py` rely on the public GitHub Deployments API (no Pages build endpoints) and remove token-related guidance from docs.

## Progress Tracking

- [x] 1. Update `scripts/fls_audit.py` to use Deployments API only
- [x] 2. Update README audit section to remove token/Pages references
- [x] 3. Run `uv run ruff check --fix` and fix any remaining issues
- [x] 4. Clean ignored artifacts with `git clean -fdX`
- [x] 5. Verify audit runs without token and outputs reports

## Plan Details

### 1) Audit script refactor (deployments-only)

- Remove Pages constants and functions:
  - `PAGES_BUILDS_URL`, `PAGES_LATEST_URL`, `fetch_pages_latest`, `fetch_pages_builds`,
    `select_pages_build`, `resolve_pages_commit`.
- Add Deployments API helpers (mirror `builder/build_cli.py` logic):
  - `fetch_pages_deployments(per_page=...)`
  - `fetch_deployment_status(statuses_url)`
  - `select_pages_deployment(offset)`:
    - Prefer most recent `success` deployment.
    - Support `--baseline-deployment-offset` and `--current-deployment-offset` indexing.
- Update commit resolution in `main()`:
  - Current commit from deployments (offset 0 by default).
  - Baseline commit from deployments (offset 1 by default), unless explicitly provided.

### 2) README audit section

- Remove token examples and token-related text.
- Keep snapshot/diff usage and cache/report paths intact.

### 3) Lint

- Run `uv run ruff check --fix` and fix any remaining issues.

### 4) Clean ephemeral artifacts

- Run `git clean -fdX` to remove ignored build/cache artifacts.

### 5) Verification

- `uv run python scripts/fls_audit.py --summary-only`
- `uv run python scripts/fls_audit.py --baseline-deployment-offset 1 --summary-only`
- `uv run python scripts/fls_audit.py` and confirm:
  - `build/fls_audit/report.json`
  - `build/fls_audit/report.md`
