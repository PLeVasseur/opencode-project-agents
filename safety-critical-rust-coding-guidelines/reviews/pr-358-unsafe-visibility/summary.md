# PR 358 Review Summary

Verdict: Request changes

CI status:
- build: success
- check_typos: success
- check_rust_examples: success (Test Guidelines Nightly skipped)
- Netlify header/redirect checks: neutral (informational)

Blocking issues:
1. ``:fls: fls_8kqo952gjhaf`` is in the FLS Unsafety chapter, but the guideline is filed under Attributes. The guideline must move to Unsafety or use an Attributes paragraph ID.
2. The normative bullet list and the Rust 2024 note require citations to the Rust Reference and/or Edition Guide to verify the required ``unsafe`` forms.
3. Several technical claims about undefined behavior (``#[no_mangle]`` collisions, ``#[export_name]``/``#[link_section]`` misuse, and extern misdeclarations even when unused) are overstated or unverified; they need correction and sources.

Non-blocking notes:
- ``:miri: skip`` is used without a justification in the example prose; add a short reason per the rust-example guidelines.

Notes:
- PR body does not include a ``closes #<id>`` reference.
