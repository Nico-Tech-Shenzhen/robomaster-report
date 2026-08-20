# RoboMaster report plan and chapter evidence map

This is the chapter-structure and evidence-routing authority. Read it with the target row in `CROSS_CHAPTER_MATRIX.md`. Evidence IDs are starting sets, not automatic citations: **H** multi-source/primary; **M** single strong source or qualified report; **L** panel/summary-only or unresolved. Verify used claims against `claims-audit.md` and actual source cards.

## Fixed publication order and drafting workflow

Publication order is Chapters 1–9 below and requires explicit user approval to change. Drafting order is different: finalize this skeleton; draft 2–3 and integrate; draft 4–6 and integrate; draft 7–9 and integrate; then finalize Chapter 1 and perform full-report integration. Chapter 1 remains provisional until the body demonstrates the significance it previews.

## Chapter map

### 1. RoboMasterの規模と競技の全体像

- Purpose/sections: why RoboMaster matters; what a match looks like; robot classes and engineering breadth; RMUC/RMUL/AI Challenge and entry paths; defined 2026 scale; representative universities; concise previews of education, employment, startups, and industry.
- Boundary: information-rich motivation, not a detailed rulebook or substitute for Chapters 2, 6, 7, or 8. Finalize after Chapters 2–9.
- Evidence: `RM2026-0101, RM2026-0103, RM2026-0105` (H); `RM2026-0201, RM2026-0301` (M–H after scope check). Define values such as universities, matches, and rounds rather than mixing denominators.
- Media: M01 competition-series/entry diagram; M02 scale table plus match photograph/video.
- Git recovery/gaps: overview and scale tables, role diagrams; current season-wide denominators; legacy summary IDs lack cards.

### 2. 2026年のロボットと技術

- Purpose/sections: a deep, parallel account of mechanical structures; drive/power/electronics; embedded control; sensing/localization/radar; vision/auto-aim; autonomy/decision; operation/UI/VR; simulation/Sim2Real/development platforms; system/process integration.
- Boundary: explain concrete systems rather than vague「AI化」; leave rule chronology and outcomes to Chapter 3.
- Evidence: Taurus `RM2026-0103, RM2026-0440, RM2026-0442, RM2026-0444, RM2026-0445` (H/M); TDT `RM2026-0441, RM2026-0443` (H); ECUST `RM2026-0446, RM2026-0452` (H); radar `RM2026-0411`; RobotPilots `RM2026-0405, RM2026-0431`; BIT `RM2026-0433`; candidates `RM2026-0406, RM2026-0408, RM2026-0409, RM2026-0416, RM2026-0418, RM2026-0419, RM2026-0420, RM2026-0421, RM2026-0422, RM2026-0423, RM2026-0426, RM2026-0428, RM2026-0432, RM2026-0435, RM2026-0439`.
- Media: M03–M06, the report's largest technical concentration: Taurus dual arms/VR, TDT wheel-leg/four-axis sentry, ECUST serial-leg, radar/vision pipelines, CAD/mechanism images, hardware/system tables.
- Git recovery/gaps: robot specification/control-stack tables; comparable test conditions; match-use proof; `RM2026-0453` wireless charging analysis.

### 3. ルール変更と技術開発の変化

- Purpose/sections: recent/2026 versioned rule changes; resources/assembly; terrain/mobility; autonomy/information; procurement/referee constraints; ranking changes and evidenced technical/management reasons. Organize cases as rule → requirement → response → outcome.
- Boundary: no「読み方」or process headings; do not repeat full Chapter 2 systems or infer causality from chronology.
- Evidence: `RM2026-0201, RM2026-0301`; context `RM2026-0101, RM2026-0103, RM2026-0105`; selected response cards from `RM2026-0405, RM2026-0406, RM2026-0408, RM2026-0409, RM2026-0411, RM2026-0418, RM2026-0423, RM2026-0426, RM2026-0428, RM2026-0431, RM2026-0432, RM2026-0433, RM2026-0439, RM2026-0440–RM2026-0446, RM2026-0452`.
- Media: M07 version/ranking timeline; M08 rule-to-outcome chain.
- Git recovery/gaps: lost V1/V2 comparisons, chronology, ranking explanations, rule-PDF URLs; corpus lacks a complete detailed version comparison.

### 4. オープンソースと技術移転

- Purpose/sections in order: incentives; source declaration; open-source review; technical-report review; awards/AWARD 2026; exchange meetings/events; documented reuse and extension; BBS; GitHub/Gitee and reproducibility details.
- Boundary: explain transfer and actual lineage before repository inventory; distinguish visibility, licensing, reproducibility, reuse, and adoption.
- Evidence: `RM2026-0201, RM2026-0301, RM2026-0305, RM2026-0405, RM2026-0406, RM2026-0408, RM2026-0409`; selected releases `RM2026-0411, RM2026-0415–RM2026-0429, RM2026-0431, RM2026-0432, RM2026-0433, RM2026-0435, RM2026-0438, RM2026-0439, RM2026-0446–RM2026-0471`.
- Media: M09 transfer/reuse lineage and review/AWARD process; M10 AWARD field evidence plus artifact/reproduction matrix.
- Git recovery/gaps: audit/incentive systems, exchange events, reuse examples, license/repository tables; downstream adoption and SimulatorX「71 universities」remain unresolved.

### 5. チーム運営と大学教育・研究

- Purpose/sections in order: team/technical groups and management; recruitment/training; annual workflow/competition/handover; formal curricula/credits; labs; research/graduation work; teaching reform; industry collaboration.
- Boundary: explicitly distinguish formal curriculum, lab support, extracurricular team, research, graduation work, and industry collaboration; employment/startups belong to Chapter 6. Avoid process headings such as「名簿の種類を分ける」「仮説への回答」.
- Evidence: operations `RM2026-0408, RM2026-0105`; education `RM2026-0472–RM2026-0479`; DGUT `RM2026-0476` and HEU `RM2026-0477` (H); `RM2026-0473, RM2026-0474, RM2026-0475, RM2026-0478, RM2026-0479` (M); `RM2026-0501` where relevant.
- Media: M11 team lifecycle/organization; M12 multi-university curriculum table and provenance-cleared「从赛场到课堂」photos.
- Git recovery/gaps: onboarding, membership, research/graduation examples; team composition and panel-only outcomes.

### 6. 人材・スタートアップとロボット産業

- Purpose/sections: strongest graduate/alumni/startup and hiring outcomes first; DJI and other recruiters; alumni networks; then sponsors, suppliers, and related companies. Keep participant, DJI alumnus, founder, sponsor, supplier, and recruiter distinct.
- Boundary: Huaqiangbei is at most a narrow evidenced procurement note; DJI component/referee architecture belongs to Chapter 7.
- Evidence: `RM2026-0501` (primary); `RM2026-0101, RM2026-0105`; `RM2026-0408` and selected portfolio cases; verified outcomes from `RM2026-0473–RM2026-0478` only.
- Media: M13 relationship-category map; M14 verified people/company/startup case table.
- Git recovery/gaps: alumni, startups, hiring preference, sponsors/suppliers; longitudinal data, startup counts, hiring causality, cumulative-number anchors.

### 7. DJIが提供する競技基盤

- Purpose/sections: DJI/RoboMaster-provided versus student-developed boundary; referee system; armor/hit detection; power and heat/projectile management; match server/data; image transmission; official motors/components; optional/student parts; separately, S1/EP/SDK education products and their later status.
- Boundary: never confuse finished education robots with student-built RMUC robots; broader industry and institutional history belong to Chapters 6 and 8.
- Evidence: `RM2026-0201, RM2026-0301, RM2026-0101, RM2026-0105, RM2026-0501`; integrations `RM2026-0408, RM2026-0409` after exact checks.
- Media: M15 referee/system architecture; M16 mandatory/optional/student-developed and education-product tables.
- Git recovery/gaps: product/referee tables, compatibility notices, S1/EP/SDK status; authoritative current product/version matrix.

### 8. RoboMasterの制度化と社会的位置づけ

- Purpose/sections: 2013 origins; 2015 expansion; early DJI organization; 共青団/全国学联; local governments; 全国大学生机器人大赛; competition-list/whitelist history and removal/change; university treatment; current industry-led operation; documented chronology followed by identified analysis.
- Boundary: investigate transition toward sustainable industry-led operation without converting chronology into causality or filling prose with defensive caveats. Technology and DJI system architecture belong to Chapters 2 and 7.
- Evidence: `RM2026-0101, RM2026-0103, RM2026-0105, RM2026-0202, RM2026-0501, RM2026-0472–RM2026-0478`; legacy IDs are lookup leads only.
- Media: M17 institutional chronology; M18 changing organization-role/evidence table.
- Git recovery/gaps: historical policy chapter, youth-body/government/university roles, competition-list changes; current formal status and historical primary sources.

### 9. 中国の大学ロボット競技との比較

- Purpose/sections: compare RoboMaster, ABU ROBOCON, ROBOTAC, RoboCup, and other relevant competitions by team/robot scale, operator/autonomy, disciplines, annual workload, entry difficulty, university organization, formal education, research, and progression.
- Boundary: do not repeat the full RoboMaster description or invent scoring systems; use normalized definitions and primary sources.
- Evidence: RoboMaster facts from Chapters 1, 5, 7, 8; newly verify current official sources for every comparison target.
- Media: M19 normalized comparison table; M20 competition progression/entry diagram.
- Git recovery/gaps: prior comparison/source matrices; current rules and denominators for all comparison targets.

## Evidence access protocol

For orientation read only `CODEX-HANDOFF.md`, `corpus-integrity.md`, and relevant portions of `claims-audit.md`. Read `evidence-clusters.md` to select converging evidence. Then use this map to choose one thematic summary or `source-map.md`; consult `INDEX.md` only to resolve candidates. Open individual cards only for claims being written, confidence checks, or citation/media metadata. Missing-card legacy IDs are search leads, never citations.
