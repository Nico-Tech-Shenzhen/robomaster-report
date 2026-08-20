---
name: robomaster-report-qa
description: Check one RoboMaster report chapter or the complete report for editorial, evidence, structural, build, and rendering defects. Use for review/validation, not substantive drafting.
---

# Report QA

Choose chapter scope by default; use complete-report scope only when requested or after structural changes. Read `RULES.md`, the relevant `REPORT_PLAN.md` section and `CROSS_CHAPTER_MATRIX.md` row, the relevant `REVISION_STATUS.md` row, and only applicable `dic.md` entries. Consult `GLOBAL_REVIEW.md` only to resolve ambiguity or during an explicitly requested full global-review audit.

Prefer deterministic scripts for terminology, prohibited wording, headings, university/team naming, citations, source IDs, links, media references, numeric consistency, and stale references. Use model judgment for evidentiary sufficiency, causal language, reader comprehension, and whether examples support conclusions.

Run relevant Python validators in `scripts/`, `git diff --check`, and `mkdocs build --strict`. For release or layout-affecting work, build the PDF and inspect rendered HTML sequentially and every PDF page. Report failures with file and line when possible; do not silently rewrite substantive prose during a QA-only task. Update the applicable `REVISION_STATUS.md` QA field after checks.

## Integration review mode

Use after Chapters 2–3, Chapters 4–6, Chapters 7–9, and for the final full report after Chapter 1. This is model-judgment work; scripts supplement it but cannot replace it.

Check across the relevant chapters that:

- each chapter's purpose and ownership boundary remain intact;
- important findings have not been omitted, including mapped Kimi evidence and valid targeted Git-history material;
- misplaced material moves to its owning chapter, and duplicate explanations become concise cross-references;
- relative depth remains asymmetric and appropriate, with Chapter 2 deepest and Chapters 4–5 also substantial;
- heading granularity, terminology, and university-first naming are consistent;
- visual/media distribution follows purpose rather than equal counts;
- Chapter 1 previews but does not duplicate the body and is not finalized prematurely;
- Chapters 2/3 divide technical implementation from rule evolution;
- Chapters 4/5 divide knowledge transfer from team organization and education/research;
- Chapters 6/7/8 divide people/industry from DJI technical infrastructure/products and institutional history;
- Chapter 9 compares normalized dimensions without repeating the full RoboMaster account.

Record the result in the relevant report-level integration checkpoint in `REVISION_STATUS.md`, including concise unresolved transfers or omissions.
