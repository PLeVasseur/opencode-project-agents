# Exit codes

| command/check | exit code | status | remediation / note |
|---|---:|---|---|
| `uv run ./tools/glossary-migration-check.py --phase 1 --strict` (baseline) | 0 | pass | baseline artifact captured |
| `uv run ./tools/glossary-migration-check.py --phase 2 --strict` (baseline) | 1 | fail | expected baseline mismatch debt (`glossary-chapter-definition-match`) |
| `uv run ./tools/glossary-migration-check.py --phase 1 --strict` (first post-tooling run) | 1 | fail | found `tokens` / `unifiable types` false-missing inventory entries; tooling corrected |
| `./make.py --clear` (step1 Gate G1) | 0 | pass | Gate G1 build requirement satisfied |
| `./make.py --check-links` (step1 Gate G1) | 0 | pass | Gate G1 link requirement satisfied |
| `./make.py --check-links` (step2 first validation attempt) | 1 | fail | duplicate `term_scope` / `term_in_scope` ids; reverted duplicate dt edit and changed harmonization approach |
| `git -C step2 merge --ff-only glossary-step-1-main-text-coverage` | 1 | fail | diverged published branch; switched to merge-based sync |
| `git -C step3 merge --ff-only glossary-step-2-align-duplicate-text` | 1 | fail | diverged published branch; switched to merge-based sync |
| `git -C step4 merge --ff-only glossary-step-3-dt-main-only` | 1 | fail | diverged published branch; switched to merge-based sync |
| `git -C step5 merge --ff-only glossary-step-4-remove-see-paragraphs` | 1 | fail | diverged published branch; switched to merge-based sync |
| `uv run ./tools/glossary-migration-check.py --phase 5 --strict` (first post-sync run) | 1 | fail | generated glossary parity mismatch; regenerated + refreshed `src/glossary.rst.inc` |
| `uv run ./tools/glossary-migration-check.py --phase 1 --strict --report final-phase1-check.json` | 0 | pass | final PR6 strict gate |
| `uv run ./tools/glossary-migration-check.py --phase 2 --strict --report final-phase2-check.json` | 0 | pass | final PR7 strict gate |
| `./make.py --clear` (step1 final matrix) | 0 | pass | final PR6 build |
| `./make.py --check-links` (step1 final matrix) | 0 | pass | final PR6 links |
| `./make.py --clear` (step2 final matrix) | 0 | pass | final PR7 build |
| `./make.py --check-links` (step2 final matrix) | 0 | pass | final PR7 links |
| `uv run ./tools/glossary-migration-check.py --phase 3 --strict` (step3 post-sync) | 0 | pass | downstream validation |
| `uv run ./tools/glossary-migration-check.py --phase 4 --strict` (step4 post-sync) | 0 | pass | downstream validation |
| `uv run ./tools/glossary-migration-check.py --phase 5 --strict` (step5 post-sync rerun) | 0 | pass | downstream validation |
| `./make.py --check-links` (step3 post-sync) | 0 | pass | downstream validation |
| `./make.py --check-links` (step4 post-sync) | 0 | pass | downstream validation |
| `./make.py --check-links` (step5 post-sync) | 0 | pass | downstream validation |
| `git push origin step1..step5` | 0 | pass | all updated stack branches pushed |
| `gh pr edit` / `gh pr comment` updates | 0 | pass | PR6/PR7 bodies and PR8-PR10 restack notes posted |
