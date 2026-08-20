# Editorial policy

This file is the canonical detailed policy for reader-facing report content. Workflow routing belongs in `AGENTS.md` and Skills; terminology belongs in `dic.md`; chapter ownership belongs in `REPORT_PLAN.md`.

## Reader and prose

- Explain RoboMaster accurately to a first-time reader. Use academic, concrete, reader-first Japanese.
- Preserve information density: facts, examples, tables, chronology, uncertainty, and sources take priority over generic compression.
- Start from a documented example before generalizing. Use university names as grammatical subjects; introduce a team as a secondary identifier.
- Distinguish source fact, report analysis, hypothesis, and recommendation. Do not infer causality from correlation, affiliation, geography, or chronology alone.
- Retain uncertainty and counterexamples. A team practice is not automatically a competition-wide practice.
- Every chapter begins with the repository's exact two metadata lines used in `docs/ch01.md`.

## Evidence and claims

- Prefer: current official rules/organizer documents; government or university documents; team reports and repositories; company pages; reputable reporting; secondary summaries.
- Use current 2025–2026 evidence for current claims. Date and scope historical evidence explicitly.
- `research/china-2026/claims-audit.md` governs wording and confidence for audited claims. Panel-only, team-reported, and single-source claims require explicit attribution.
- Avoid unverified superlatives and causal claims. Keep incompatible denominators separate.
- Kimi source cards archive evidence; rewrite their content for the reader rather than copying their prose.
- Non-public material cannot be the sole support for a public factual claim. Field notes and photographs must be labelled as such.

## Citations and source identity

- Use clickable local citations in the form `[[n]](#ref-n)` with a matching `<a id="ref-n"></a>` reference in the same chapter.
- Cite factual numbers, quotations, institutional claims, named cases, and consequential technical claims at claim level.
- Link the most specific document, release, repository, dataset, or media item. Reader-facing prose must not contain bare URLs.
- Record publisher/creator, title, date/year, version or commit where relevant, direct URL, and access date for unstable web material.
- A bibliography or corpus ID alone is not a substitute for a claim-level citation to the underlying source.

## Numbers and comparisons

- State date, population, unit, definition, and source for important numbers.
- Do not conflate registrations, participants, universities, teams, matches, rounds, club members, registered members, field personnel, operators, advisers, alumni, investment, discounts, sponsorship, or prize money.
- When definitions differ, present values separately; do not manufacture a trend.
- Comparison tables must define common dimensions and flag missing or non-comparable data.

## Language and technical explanation

- Use natural modern Japanese and Japanese new-character forms. Follow `dic.md` for canonical names and forbidden terms.
- Chinese forms may appear only in source titles, quotations, URLs, code identifiers, or a useful official-name annotation at first occurrence.
- Explain technology as university/team → system → problem → implementation → evidenced result.
- Distinguish mandatory competition hardware, optional components, historical products, and educational products.
- For software/open hardware, record repository, season, license, dependency/version, and reproduction limits when available.
- “Publicly visible,” “source available,” “open source,” “reproducible,” “adopted elsewhere,” and “current standard” are distinct claims.

## Structure, media, and deletion

- Give each topic one canonical chapter as defined by `REPORT_PLAN.md`; cross-reference instead of duplicating explanations.
- Use media to explain or evidence, not decorate. Captions identify what to observe and give attribution; licensing and web/PDF behavior follow the media Skill.
- Historical Git revisions are a research archive. Recover targeted evidence from relevant commits, never old prose wholesale.
- Delete report material only for a recorded reason: false, unsupported, duplicated, irrelevant, dead, or superseded. Preserve useful detail in the appropriate canonical location or evidence archive.

## Completion standard

- Run applicable repository validators, `git diff --check`, and `mkdocs build --strict`.
- For release or layout changes, inspect rendered HTML sequentially and every page of a regenerated PDF.
- Confirm citations resolve locally, links are specific, source IDs exist or are explicitly marked legacy, numbers agree, terminology passes, and chapter/media references are current.
