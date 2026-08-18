# RULES

## 1. Purpose and reader

- This is a Scramble research report that explains RoboMaster accurately to a first-time reader.
- Every chapter begins with the repository’s exact two metadata lines.
- Preserve information density: concrete facts, examples, tables, chronology, and sources take priority over short generic summaries.

## 2. Facts before analysis

- Present a concrete documented example before drawing a general conclusion.
- Separate source fact, report analysis, hypothesis, and recommendation.
- Do not turn correlation, organizational affiliation, geography, or chronology into causality without direct evidence.
- Retain uncertainty and counterexamples. Do not convert one team’s practice into a competition-wide rule.

## 3. Evidence and freshness

- Prefer, in order: current official rules and organizer documents; government or university documents; team BBS reports and repositories; company pages; reputable reporting; secondary summaries.
- Current claims require current 2025–2026 evidence. Historical sources remain valid for chronology when their date and scope are explicit.
- Link the most specific source: direct rule PDF, announcement, article, repository, release, or dataset rather than a generic home or search page.
- Record enough identity to recheck a source: publisher, title, year/date, version or commit where relevant, and direct URL.
- Non-public material may not be the sole support for a public factual claim.

## 4. Citations and links

- Visible in-text citations use `[n]` and are clickable to an anchored reference in the same chapter.
- Each factual number, quotation, institutional claim, and named case must point to the source that supports it.
- External URLs are clickable Markdown links. Bare URLs are not allowed in reader-facing prose.
- A reference list is not a substitute for claim-level citation. Never cite a generic source collection when a direct document exists.

## 5. Numbers

- State the date, population, unit, definition, and source of every important number.
- Do not merge registrations, actual participants, universities, teams, matches, rounds, club members, registered members, field personnel, operators, advisers, alumni, investment, discounts, sponsorship, or prize money.
- If historical sources use incompatible denominators, show them separately rather than constructing a trend.

## 6. Japanese and Chinese

- Reader-facing prose uses natural modern Japanese and Japanese new-character forms.
- Simplified or Traditional Chinese appears only in a source title, quotation, URL, code identifier, or useful official-name annotation at first occurrence.
- Translate Chinese administrative and competition terms by meaning; do not leave mechanical calques in Japanese prose.
- `dic.md` is the naming authority. Robot classes use one canonical Japanese name. Companies use an established official English brand where available.

## 7. Technical writing

- Explain current technology in the sequence: team → system → problem → implementation → evidenced result.
- Distinguish mandatory competition hardware, optional components, historical products, and educational products.
- For software and open hardware, record repository, season, license, dependency/version, and known reproduction limits when available.
- “Publicly visible,” “open source,” “reproducible,” “adopted by another team,” and “current standard” are different claims.

## 8. Structure and integrity

- Give each topic one canonical chapter; use cross-references instead of copying the same explanation.
- Structural edits require repository-wide checks of navigation, chapter numbers, headings, redirects, references, index, MkDocs configuration, and PDF inputs.
- Historical Git revisions are a research archive. Recover useful evidence from multiple commits; never assume one snapshot is the complete baseline.
- Delete material only for a recorded reason: false, unsupported, duplicated, irrelevant, dead, or superseded.

## 9. Completion checks

- Run all repository validators, `git diff --check`, and `mkdocs build --strict`.
- Read the rendered HTML sequentially and inspect every page of a regenerated PDF when the PDF is tracked.
- Confirm that all citations resolve locally, source links are specific, numeric statements agree, Chinese leakage is absent, and stale chapter references are gone.
- Do not commit or push unless explicitly requested.
