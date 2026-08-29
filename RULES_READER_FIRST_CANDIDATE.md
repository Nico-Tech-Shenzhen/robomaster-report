# Reader-First Editorial Posture — Candidate Rules

These rules are experimental.
Do not merge them into RULES.md until a human A/B review approves them.

## 1. Write what the reader can learn, not what the researcher could not prove

The main text should primarily contain:

- verified facts;
- concrete examples;
- supported relationships;
- evidence-based analysis.

Research-process statements are normally not reader-facing content.

Avoid prose such as:

- 本資料群では資料が不足している
- 確認できなかった
- 比較できる資料はない
- 断定できない
- 推定できない
- 今回の調査では
- 本報告では確認できない

when the same problem can be handled by simply narrowing or omitting the claim.

BAD:
「本資料群では東北大学の運営要因を比較できる資料が不足している。」

BETTER:
「東北大学は車輪・リング脚歩兵、四軸ジンバル哨兵、自律測位・意思決定を全国大会へ投入した。」

If no verified management factor is available, do not create a reader-facing
sentence about the absence.

## 2. Absence of evidence is usually a data-design issue, not prose

When a table cell cannot be supported:

- use "—";
- remove the column if it produces many meaningless blanks;
- or use one concise table note.

Do not fill cells with sentences such as:

「本資料群では資料が不足」

A table must present information, not the researcher's search history.

## 3. Keep uncertainty only when it changes interpretation

A limitation belongs in the main text only when omitting it would cause a
reasonable reader to misunderstand the evidence.

Examples where qualification IS useful:

- a figure is cumulative rather than annual;
- a ranking mixes regional and national stages;
- an AWARD panel is a nomination rather than a final award;
- an official English company name cannot be verified;
- a relationship is correlation rather than documented causation.

State that distinction once, precisely.

Do not repeatedly remind the reader that other explanations may exist.

## 4. Replace defensive prose with bounded claims

Do not solve overclaiming by writing long disclaimers.

Instead reduce the claim itself.

BAD:
「各機構の寄与率、故障、操縦、戦術を共通指標で比較できる資料はないため、
これが勝因とは断定できない。」

BETTER:
「2026年の上位校では、地形対応、装配、自律運用、操作系を
一台の競技システムへ統合する開発が共通して確認できる。」

The second sentence makes a narrower claim and therefore needs no defensive
paragraph.

## 5. Positive framing does not permit stronger causality

Reader-first writing is not promotional writing.

Do not convert:

A and B were observed together

into:

A caused B.

Use causal verbs only when the source supports causality.

Preferred analytical forms include:

- ～を可能にした
- ～の開発条件になった
- ～へ接続された
- ～が後続実装で参照された
- ～という構造が確認できる
- ～という役割を担っている

when supported by evidence.

## 6. Every chapter needs an evidence-backed thesis

A chapter should not merely catalogue material.

The opening 2-3 sentences must state the main relationship that the evidence
in the chapter demonstrates.

The chapter then develops that thesis through concrete cases.

## 7. Chapter 4 editorial posture

Chapter 4 should begin from this evidence-backed position:

RoboMaster actively promotes technical openness through review, reporting,
awards, technical exchange and public repositories.

The important result is not simply that files are public.

Public designs are cited, modified and reused by later teams, creating
multi-season engineering assets.

Write the chapter around this cycle:

development
→ disclosure
→ review / exchange
→ publication
→ reuse
→ modification
→ next-season asset

Do not frame the chapter primarily around limitations of open-source evidence.

## 8. Chapter 5 editorial posture

Chapter 5 should treat a RoboMaster team as a large multidisciplinary
engineering project resembling product development.

Students must coordinate:

- requirements;
- mechanical design;
- electronics;
- embedded systems;
- algorithms;
- software;
- testing;
- procurement;
- project management;
- operation;
- repair;
- documentation.

The analytical direction should connect this experience to:

- university education and research;
- technical capability accumulated in the university;
- entrepreneurship and employment discussed in Chapter 6.

Do not reduce the educational argument to generic teamwork or extracurricular
activity.

## 9. Chapter 6 editorial posture

Chapter 6 should show how RoboMaster engineering experience moves into the
robotics industry through identifiable relationships:

- participant → founder;
- participant → employee;
- competition experience → hiring preference;
- company → sponsor;
- company → supplier.

Use these relationships to explain the talent / company network.

Do not organize the prose around companies that were investigated and excluded.

## 10. Taxonomies must be operational

If the report defines categories such as A / B / C / D / E / F / G,
the categories must be used in subsequent tables or analysis.

For example:

A = participant → founder
B = participant → employee
C = DJI employee → founder
D = sponsor
E = supplier
F = employer explicitly valuing competition experience
G = unverified relationship

Later examples should carry these labels where useful.

If the classification does not help the later analysis, remove it.

Never introduce a taxonomy and then abandon it.

## 11. Company names

For Chinese companies, first occurrence should include:

Chinese official name + verified official English name

Example format:

中文公司名（Official English Name）

If no official English corporate name can be verified, do NOT invent one.

Use a clearly identified romanized name if useful, or retain the Chinese
corporate name until a reliable English form is found.

Do not silently machine-translate legal company names.

After first occurrence, use the recognized short English or brand name where
appropriate.

## 12. Prefer informative tables over methodological tables

A table should answer a reader question.

Good:
University | technology | organizational structure | competition change

Bad:
University | evidence we found | evidence we did not find

If one column repeatedly produces statements about unavailable evidence,
redesign the table.

## 13. Move methodology out of the narrative

Detailed notes about:

- search coverage;
- unresolved evidence;
- excluded claims;
- failed verification;
- source limitations

belong in:

- research notes;
- claims audit;
- appendix;
- source cards;

not normally in the main chapter.

The publication should present the strongest defensible account produced by
that research process, not narrate the research process itself.
