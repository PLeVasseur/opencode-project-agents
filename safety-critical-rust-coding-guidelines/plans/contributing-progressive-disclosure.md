# Plan: Progressive disclosure for CONTRIBUTING.md

Date: 2026-02-05

## Goals
- Make the first-time contributor experience less intimidating.
- Keep the full workflow details available without front-loading them.
- Move reviewer/bot guidance out of CONTRIBUTING.md and into REVIEWING.md.

## Non-goals
- Change the actual contribution workflow or requirements.
- Remove content that is still needed by reviewers or advanced contributors.

## Proposed changes
1) Create REVIEWING.md
- Move the entire reviewer/bot section (commands, deadlines, queue status).
- Add a short intro that this document is for Producers/reviewers.
- Link back to CONTRIBUTING.md for contributor workflow.

2) Update CONTRIBUTING.md structure
- Add a GitHub NOTE near the top that links to REVIEWING.md.
- Add a "First-time contributor quick start" (5-7 steps) with links to detailed sections.
- Slim the TOC to only top-level sections plus Quick start.
- Wrap long sections in <details> blocks:
  - Flowchart
  - FLS ID how-to
  - Writing a guideline locally
- Keep all detailed workflow text, but move it below the quick start.

## Steps
1) Create REVIEWING.md and move content from CONTRIBUTING.md.
2) Edit CONTRIBUTING.md to add NOTE, quick start, slim TOC, and <details> blocks.
3) Update links/anchors so internal references still work.
4) Re-scan CONTRIBUTING.md for readability and ensure the top screen is light.

## Risks and checks
- Risk: heading moves change anchor links. Mitigation: verify all internal links.
- Risk: REVIEWING.md discoverability. Mitigation: prominent NOTE near top of CONTRIBUTING.md.
