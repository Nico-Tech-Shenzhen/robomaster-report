# Global editorial review

This is the canonical archival record of the user's latest report-wide review. It preserves concrete editorial intent and resolves ambiguity that remains after consulting `REPORT_PLAN.md` and `CROSS_CHAPTER_MATRIX.md`. Normal chapter tasks should not load this entire file.

# 1. Report-wide requirements

1. Keep permanent rules in Markdown and repeatable workflows in repository Skills so later chapter sessions do not rediscover them.
2. Integrate the 2026 Kimi corpus throughout the report without copying source-card prose or loading all cards at once.
3. `dic.md` is the terminology authority: use「ダートシステム」rather than「飛鏢システム」.
4. Introduce implementations with the university as the prose subject:「南京理工大学（Allianceチーム）は……」and normally use the university name thereafter.
5. Explain RoboMaster positively, factually, and academically. Evidence limitations belong in attribution and internal QA, not in defensive reader-facing prose.
6. Embed or link Bilibili and other videos when they provide useful visual technical evidence. Important mechanisms should use photographs, diagrams, CAD images, or video when rights and availability permit.
7. Convert structures into tables/diagrams when that improves comprehension, especially competition-series structure, entry paths, regional scale, robot classes, technical systems, DJI-provided versus student-developed systems, open-source transfer, education cases, institutional chronology, and competition comparison.
8. Preserve report-wide balance, narrative flow, terminology, relative depth, and usefulness; do not optimize a chapter in isolation at the expense of another chapter's role.

Precedence when instructions conflict: explicit current user instruction → `GLOBAL_REVIEW.md` → `REPORT_PLAN.md` → `RULES.md` → old report prose. Always-on safety constraints in `AGENTS.md` remain binding.

# 2. Chapter-order requirements

The final publication order is fixed unless the user explicitly approves a change:

1. RoboMasterの規模と競技の全体像
2. 2026年のロボットと技術
3. ルール変更と技術開発の変化
4. オープンソースと技術移転
5. チーム運営と大学教育・研究
6. 人材・スタートアップとロボット産業
7. DJIが提供する競技基盤
8. RoboMasterの制度化と社会的位置づけ
9. 中国の大学ロボット競技との比較

Publication order is not drafting order:

- Phase A: finalize the nine-chapter skeleton.
- Phase B: draft Chapters 2–3; perform an integration review.
- Phase C: draft Chapters 4–6; perform an integration review.
- Phase D: draft Chapters 7–9; perform an integration review.
- Phase E: write/finalize Chapter 1 after Chapters 2–9 are substantially stable; perform a final full-report integration review.

Chapter 1 comes last in drafting because its overview must accurately preview the scale, technology, education, and industrial significance actually demonstrated by the completed body.

# 3. Chapter-by-chapter requirements

### Chapter 1 — RoboMasterの規模と競技の全体像

Make a first-time reader understand why RoboMaster is worth studying and want to continue. Establish scale, what a match looks like, robot number/variety, clearly defined student/university counts, engineering breadth, representative strong universities, national competition structure, and visible connections to startups, employment, and robotics industry. Include photographs and/or video.

Show RMUC/RMUL/AI Challenge structure in a diagram or table as well as prose. Put figures such as「96 universities / 266 matches / 613 rounds」in a definition-rich scale table or figure rather than burying them in prose. Preview later chapters without duplicating their detailed technology, industry, education, or history. Do not turn Chapter 1 into a rulebook. Finalize it after Chapters 2–9 stabilize.

### Chapter 2 — 2026年のロボットと技術

This is one of the report's most important and substantial chapters. Explain what technologies RoboMaster requires, how they are developed, how Physical AI is embodied, and how broad the engineering work is. Cover more than AI algorithms: mechanical design; advanced hardware; actuators; electronics; power; embedded systems; sensors; localization; radar; vision; auto-aim; control; autonomous navigation; decisions; operator interfaces and VR; custom client software; simulation; Sim2Real; process and system integration.

Avoid vague「AI化」language and explain actual systems. Use parallel technical subsection categories rather than mixing a mechanism such as「車輪脚と射撃」with a robot class such as「エンジニアロボット」. A strong starting hierarchy is mechanical structures; drive/power/circuits; embedded control; sensing/localization/radar; vision/auto-aim; autonomy/decision; operation/UI; simulation/development platform; system integration. Improve it only while preserving parallelism.

Use Kimi 2026 evidence extensively. Important visual cases include South China Agricultural University's Taurus dual-seven-axis engineer robot and VR operation, Northeastern University's TDT ring-wheel-leg system and four-axis sentry, East China University of Science and Technology's Qiyuan serial-leg system, and other consequential 2026 mechanisms. Add hardware/system tables where useful.

### Chapter 3 — ルール変更と技術開発の変化

Explain recent rule changes—especially 2026—and the additional engineering they required. Cover major changes in team ranking and evidenced technical or management/development reasons. Recover valid material lost from older revisions.

Where evidence permits, use the chain: rule change → engineering requirement → university/team response → competition outcome. Do not overclaim causality. Remove methodological headings such as「読み方」and present the evidence as reader-facing history and engineering analysis.

### Chapter 4 — オープンソースと技術移転

Explain how technology moves between RoboMaster universities. Begin with transfer mechanisms: incentives; source declaration; open-source review; technical-report review; awards; technical exchange meetings/events; reuse/extension examples; then BBS and GitHub/Gitee repositories. Do not begin with a repository list.

Explain open-source review and award systems in detail and use RoboMaster AWARD 2026 field evidence. Show documented cases where one university cited, reused, modified, or extended another university's work. Retain detailed university repository information so readers can follow sources. Introduce universities that are strong in open-source and technical sharing. Do not collapse public visibility, licensing, reproducibility, reuse, and adoption into one claim.

### Chapter 5 — チーム運営と大学教育・研究

Explain both how a team operates and how RoboMaster relates to formal education, research, and individual academic work. Begin with structure, technical groups, management roles, recruitment, training, annual workflow, competition operation, and handover. Then expand substantially into classes, credits, laboratories, research, graduation work, teaching-reform programs, and industry collaboration.

Use「从赛场到课堂」extensively and present multiple university cases. Keep formal curriculum, laboratory support, extracurricular team, research, graduation project, and industry collaboration analytically distinct. Remove reader-useless headings such as「名簿の種類を分ける」and「仮説への回答」.

### Chapter 6 — 人材・スタートアップとロボット産業

Explain RoboMaster's industrial role through graduates, startups, DJI employment, recruitment by other companies, sponsors, related companies, suppliers, and alumni networks. Start with the strongest human and industrial outcomes. Recover valid older evidence about graduate startups, alumni, DJI hiring, and employers explicitly valuing RoboMaster experience; then cover sponsors and related firms.

Do not make Huaqiangbei a major topic. The current「華強北で即日試作を検証する」framing should disappear unless narrowly supported procurement evidence makes a minor mention useful. Keep participant, DJI alumnus, sponsor, supplier, recruiting company, and startup founder as distinct relationship categories.

### Chapter 7 — DJIが提供する競技基盤

Draw a clear boundary between what DJI/RoboMaster supplies and what students develop. Explain the mandatory referee system in sufficient detail: armor/hit detection, power limits, heat/projectile management, match server/data, image transmission, official components and motors, optional components, and student-designed components. Provide a clear comparison table.

Separately explain historical education products—RoboMaster S1, RoboMaster EP, SDK/education products—and investigate their status or discontinuation where evidence permits. Never confuse finished educational robots with student-built RMUC robots.

### Chapter 8 — RoboMasterの制度化と社会的位置づけ

Explain how an activity originating within DJI became a nationwide university robotics event and how its institutional position changed. Recover valid historical detail from Git: 2013 origins; 2015 national expansion; early DJI organization; 共青団/全国学联 involvement; local governments; 全国大学生机器人大赛 structure; competition-list/whitelist history and later removal/change; universities; current industry-led operation.

Investigate whether RoboMaster moved from a government/youth-league-supported stage toward an ecosystem capable of industry-led operation. Do not turn chronology into causality. Present documented chronology plus clearly identified analysis without filling reader-facing prose with disclaimers. Explain what RoboMaster contributed to Chinese engineering education and how the state and universities treated it over time.

### Chapter 9 — 中国の大学ロボット競技との比較

Expand the currently usable comparison to show how Chinese universities use RoboMaster, ABU ROBOCON, ROBOTAC, RoboCup, and other relevant competitions where evidence permits. Compare team size, robot count, operator/autonomy balance, engineering disciplines, annual workload, entry difficulty, university organization, formal educational use, research relationship, and competition progression. Avoid unsupported scoring systems and ensure comparison dimensions share definitions.

# 4. Visual/table/media requirements

- Chapter 1: competition overview, series/entry structure, and scale table; photo/video for reader orientation.
- Chapter 2: the largest concentration of technical photographs, videos, CAD/mechanism images, system diagrams, and hardware/system tables.
- Chapter 3: rule/version timeline and rule → requirement → response → outcome figures.
- Chapter 4: transfer mechanism, reuse lineage, review/AWARD process, and AWARD field evidence.
- Chapter 5: team lifecycle/organization, education-case tables, and「从赛场到课堂」field photographs.
- Chapter 6: participant/alumni/company/sponsor/supplier relationship visualizations.
- Chapter 7: referee-system architecture and supplied-versus-student-developed table.
- Chapter 8: institutional chronology and organization-role changes.
- Chapter 9: normalized comparison tables and competition-progression diagram.

Visual distribution follows chapter purpose; do not add decorative media or equalize counts mechanically. Bilibili embeds require fallback links and cited timestamps. External images/CAD require a verified reuse basis.

# 5. Writing and heading requirements

- Titles and subsections must operate at consistent granularity. Prefer parallel technical or analytical categories.
- Use concrete systems and mechanisms rather than vague labels such as「AI化」.
- Use university names as subjects and team names as secondary identifiers.
- Write positive, factual academic prose for readers. Encode limits through precise scope and attribution.
- Avoid headings or framing whose main function is narrating author caution, process, or report revision.
- Reader-facing prohibited patterns include「読み方」「仮説への回答」「確認できる範囲」「本報告では断定しない」「今回確認した範囲では」「この一大会を全国へ当てはめない」「旧版では」「書けること／書けないこと」.

# 6. Cross-chapter balance requirements

Depth is deliberately asymmetric. Chapter 2 is among the most substantial because actual engineering is central. Chapters 4 and 5 also require substantial depth because technology transfer and engineering education are major findings. Chapter 1 is compelling and information-rich but does not duplicate the body. Chapters 7–9 are complete without expanding through repetition. Do not impose equal length or rigid word counts.

Ownership boundaries:

- Chapter 1 motivates and previews; it does not own detailed technology, industry, or institutional history.
- Chapter 2 owns implementation; Chapter 3 owns rule evolution and resulting development.
- Chapter 4 owns knowledge transfer; Chapter 5 owns team organization and education/research.
- Chapter 6 owns people/industry; Chapter 7 owns DJI technical infrastructure/products; Chapter 8 owns institutional/policy history.
- Chapter 9 compares competitions and relies on cross-references instead of repeating the full RoboMaster explanation.

Integration reviews occur after Chapters 2–3, 4–6, and 7–9, followed by a final review after Chapter 1. They check omissions and surviving evidence as well as duplication and balance.

# 7. Explicitly rejected patterns

- Finalizing Chapter 1 before the report body stabilizes.
- Treating all nine chapters as equal-length units.
- Beginning Chapter 4 with a generic repository catalogue.
- Letting Chapter 2 become an algorithm-only or vague「AI化」chapter.
- Letting Chapter 3 re-explain complete systems instead of analyzing rule-driven change.
- Conflating curriculum, lab support, extracurricular activity, research, graduation work, and industry collaboration.
- Conflating participant, alumnus, founder, sponsor, supplier, and recruiter relationships.
- Making Huaqiangbei a major Chapter 6 framing.
- Confusing RoboMaster S1/EP educational products with RMUC student-built robots.
- Turning Chapter 8 chronology into unsupported causal claims or defensive prose.
- Unsupported competition scores/rankings in Chapter 9.
- Decorative galleries, unlicensed imagery, or visuals added only to equalize chapter counts.
- Team-name-first implementation prose, inconsistent heading granularity, methodological headings, revision narration, and report-writing excuses.
