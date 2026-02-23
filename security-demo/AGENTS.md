# Project Instructions

## Overview

This repository is a live demo that shows Rust still has security challenges
even with strong memory safety. The goal is to walk through supply chain risk,
policy enforcement, logic flaws, unsafe code, and OS interaction hazards in a
clear, repeatable way.

## Workflow

- Follow the demo and verification steps in `DEMO_GUIDE.md` and
  `VERIFICATION.md`.
- Use the per-section plans in
  `~/opencode-project-agents/security-demo/plans/` as the authoritative
  checklists before running the demo.
- Keep the demo in a presentable state. If expected output is not produced,
  fix the demo so it still showcases the intended Rust security issue.

## Demo Verification Plans

Plans are stored outside the repo at:

`~/opencode-project-agents/security-demo/plans/`

Each plan documents:

- Commands to run for that section
- Expected output/behavior from the docs
- Known prerequisites and gotchas
- A note to fix any failures so the issue is still demonstrated

## Code Standards

- Keep changes minimal and aligned with the published docs.
- Do not change the narrative intent of a demo section unless required to
  restore expected output.

## Files to Know

- `DEMO_GUIDE.md`
- `VERIFICATION.md`
- `01-dependency-explosion/` through `07-clippy-unsafe/`
