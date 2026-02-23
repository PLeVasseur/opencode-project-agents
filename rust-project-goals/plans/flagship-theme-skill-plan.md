# Plan: Flagship Theme Skill

## Objective
Create an OpenCode skill that reliably guides authors in writing 2026 flagship
theme pages and wiring them into the Rust project goals docs.

## Inputs
- src/FLAGSHIP_TEMPLATE.md (theme structure, tone, and length guidance)
- src/2026/flagships.md (theme list and milestone link style)
- src/2026/flagship-*.md (exemplar theme narratives)
- Goal docs in src/2026/*.md with Flagship metadata (linkage rules)
- OpenCode docs on skills and OPENCODE_CONFIG_DIR usage

## Steps
1. Draft SKILL.md frontmatter with name, description, compatibility, metadata.
2. Encode the flagship theme narrative rules:
   - Summary, status quo, what we are shooting for, key use cases, axioms, FAQ.
   - Tone and length rules, present-tense outcomes, bolded use cases.
3. Encode linkage rules and file placement:
   - Create src/2026/flagship-<slug>.md and add to src/2026/flagships.md.
   - Add nav entry in src/SUMMARY.md.
   - Ensure FLAGSHIP GOALS placeholder matches plain-text Flagship metadata.
4. Add validation checklist and common pitfalls.
5. Reference exemplar files for authors to follow.

## Deliverables
- $OPENCODE_CONFIG_DIR/skills/flagship-theme/SKILL.md

## Validation
- Skill name matches directory and regex requirements.
- Instructions align with FLAGSHIP_TEMPLATE.md structure and tone.
- Linkage rules ensure goals appear under the correct theme.
- Checklist calls out missing theme files or broken links.
