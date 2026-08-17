# Audit Findings — RoboMaster Report Restructure

*Generated: 2026-08-17*

---

## 1. STRUCTURAL PROBLEMS

### 1.1 Index vs. Files Mismatch
README.md and docs/index.md describe a completely different chapter structure from what actually exists:
- Index says ch02 = "人材と成果" but file is "技術の進化と産業への移転"
- Index says ch03 = "エコシステムとコミュニティ" but file content overlaps heavily with ch01
- Index says ch08 = "エコシステム" but ch03 is also ecosystem
- mkdocs.yml nav only lists ch01-ch08 + appendix, silently omitting ch09-ch12

### 1.2 Chapter Title ≠ Content
- ch01 "RoboMasterエコシステム概観" actually covers: open-source review, awards, BBS, RMOSS, GitHub, competition format, robot types, rule changes, startups, hiring, project management — it is an everything-bag
- ch02 "技術の進化と産業への移転" actually covers: open-source history, RMOSS, rm_vision, standards, industry applications, startups, rule co-evolution — massive overlap with ch01 and ch05
- ch04 "教育インパクト" actually covers: PBL, DJI training, skill evolution, hiring/career pipeline, enterprise recruitment — overlaps heavily with ch03, ch06, ch07

### 1.3 Empty Chapters
- ch09: Community/Open Source — 100% TODO
- ch10: International Comparison — 100% TODO
- ch11: Business Model — 100% TODO
- ch12: Future Outlook — 100% TODO
- appendix.md: 100% TODO

---

## 2. DUPLICATION MAP

| Topic | Appears In | Canonical Home Should Be |
|---|---|---|
| RMOSS technical details | ch01, ch02, ch03, ch05, ch08 | Technology chapter |
| rm_vision framework | ch01, ch02, ch03, ch05 | Technology chapter |
| Open-source review system (2025) | ch01, ch02, ch03 | Open-source chapter |
| Open-source awards | ch01, ch02, ch03 | Open-source chapter |
| GitHub/Gitee repos table | ch01, ch02, ch03 | Open-source chapter |
| BBS post culture/examples | ch01, ch02, ch03 | Open-source chapter |
| DJI hiring pipeline/RM channel | ch01, ch03, ch04, ch06, ch07 | Industry/human pipeline chapter |
| DJI ~1,000 hires statistic | ch01, ch04, ch06, ch07 | Industry/human pipeline chapter |
| Startup examples (AgileX, Mammotion, Bambu Lab, Damiao) | ch01, ch02, ch07, ch08 | Industry/human pipeline chapter |
|魏基栋/AgileX founding story | ch01, ch02, ch07 | Industry/human pipeline chapter |
| Robot type definitions (hero, infantry, engineer, etc.) | ch01, ch05 | Introductory/technical chapter |
| 2025-2026 rule changes | ch01, ch05, ch02 | Rules chapter |
| Supply chain / Shenzhen hardware | ch03, ch08 | Ecosystem/supply chapter |
| Team structure / roles | ch01, ch03, ch04 | Team operations chapter |
| Education / PBL / DJI training | ch04, ch06 | Education chapter |
| DJI founding story / Wang Tao | ch06 only | DJI strategy chapter |
| Whitelist policy | ch07 only | Policy chapter |
| Communist Youth League withdrawal | ch06, ch07 | Policy chapter |

**Conclusion: The same 10-15 topics are scattered across 7+ chapters. This must be fixed structurally.**

---

## 3. CONTRADICTORY NUMBERS

| Metric | Value A (Location) | Value B (Location) | Status |
|---|---|---|---|
| Cumulative participants | "近20万名" (ch01[20][21], ch04[8][9]) | "近10万人" (ch07[1]) | **CONFLICT** — 20万 is from 2026 media reports; 10万 is from older 2024 report. Prefer 20万 with source. |
| DJI cumulative hires | "1,000人以上" (ch01[21][31]) | "近1,000名" (ch06[9]) | **CONFLICT** — ch04 says "超1,000名". Media [31] says "近1,000名". Prefer "近1,000名" from 2026 media. |
| Startup count | "累計約100" (ch01[21]) | "累計で200余り" (ch07[2]) | **CONFLICT** — ch07 cites internal white paper. Need to verify which is correct. Both may be using different definitions. |
| 2024 finals participants | "近万名" (ch01[22]) | "728台" robots (ch01[22]) | **UNCLEAR** — 2025/2026 say "約2,000名" + "約300台" for finals only. The 2024 numbers may include regional qualifiers. |
| DJI investment | "累計3.5億元" (ch06[7]) | "累計5,394万元" (ch06[8]) | **NOT A CONFLICT** — 5,394万 is only物资割引 (component discounts), not total investment. 3.5億 is total cumulative investment per 2019 article. Need to clarify. |

---

## 4. OUTDATED / WEAK CLAIMS

### 4.1 Startup Causality Issues
- **Bambu Lab**: Only evidence is "DJI消費級ドローン事業部元責任者" — this is DJI origin, NOT RoboMaster origin. No evidence links Bambu Lab founders to RoboMaster participation. Must reword carefully.
- **Damiao**: "DJI元エンジニア" — again, DJI origin, not necessarily RoboMaster. Need to verify.
- **AgileX**: Wei Jidong was "DJI RM 一号员工" — this IS a direct RoboMaster link. OK.
- **Mammotion**: Described as "AgileX子ブランド" but also said to recruit RM participants. Need to verify direct RoboMaster link for founders.
- "RoboMasterから約100の硬科技スタートアップが生まれた" — The source is DJI internal white paper, but it doesn't distinguish between "RoboMaster participant founded" vs "DJI employee founded" vs "general robotics founder."

### 4.2 Technology Transfer Claims
- "Bambu Labの3Dプリンタに搭載される機械視覚モジュール...RoboMasterコミュニティで3〜5年前に開発された技術の直接の流用" — No direct evidence. Similar tech stack ≠ direct transfer. Must downgrade to "technically similar" or remove.
- "Mammotionの芝刈り機に搭載されるSLAMナビゲーション...RoboMasterコミュニティで開発された技術の直接の流用" — Same issue.
- "DJI M400シリーズの電力線巡視...RoboMasterの空中ロボット・レーダーシステムと同じ技術系譜" — DJI is the common denominator, not RoboMaster→DJI transfer. Weak causal claim.

### 4.3 Policy Claims
- "RoboMaster left the whitelist because the ecosystem became self-sustaining" — No authoritative source states this as the reason. Only facts: it left in 2019. Must separate fact from interpretation.
- "政府が後退したのではなく、エコシステムが前進した" — Interpretation presented as analysis, but should be clearly labeled as such.

### 4.4 Historical Data
- ch07 uses 2024 Annual Competition Report for participant data, but 2026 media reports newer numbers.
- Multiple chapters cite the DJI internal white paper (2024) for startup counts, hire counts, etc. — this is a primary source but not independently verifiable.

---

## 5. CHINESE CHARACTER CONTAMINATION (Partial List)

The following appear in body text where Japanese equivalents should be used:

- 开源 → オープンソース (ch01, ch02, ch03, ch04, ch05, ch06, ch07, ch08)
- 赛季 → シーズン (ch01, ch02, ch03, ch04, ch05, ch06, ch07)
- 区域赛 → 地域大会 (ch01)
- 全国赛 → 全国大会 (ch01, ch03, ch04, ch07)
- 参赛 → 出場 (ch01, ch03, ch04, ch07)
- 培训 → 研修/教育 (ch01, ch03, ch04, ch06, ch07)
- 算法 → アルゴリズム (ch01, ch03, ch04, ch05, ch07, ch08)
- 硬件 → ハードウェア (ch01, ch03, ch04, ch05, ch07, ch08)
- 小组 → チーム/グループ (ch01)
- 组委会 → 組織委員会 (ch01, ch03, ch04, ch06, ch07)
- 智能 → スマート/知能 (ch01, ch04, ch05, ch06, ch07)
- 点云 → 点群 (ch02, ch05)
- 封装 → ラッパー/カプセル化 (ch05)
- 单板 → 単板 (ch05)
- 增益 → 増幅/ゲイン (ch01, ch05, ch07)
- 交流赛 → 交流試合 (ch03)
- 成本价 → 原価 (ch03)
- 课堂 → 教室/講義 (ch04)
- 赛场 → 競技場/フィールド (ch04, ch07)
- 职场 → 職場 (ch04)
- 视觉 → 視覚 (ch01, ch03, ch04, ch05, ch07, ch08)
- 雷达 → レーダー (ch01, ch03, ch05, ch07, ch08)
- 底盘 → シャーシ (ch01, ch05)
- 云台 → 雲台 (ch01, ch05, ch06)
- 电控 → 電装制御 (ch01, ch03, ch05)
- 机械 → 機械 (ch01, ch03, ch05) — OK as Japanese kanji
- 嵌入式 → 組み込み (ch01, ch03, ch05)
- 总线 → 総線 (ch01, ch05)
- 保研 → 推薦研究生 (ch01, ch04, ch07)
- 教改课题 → 教育制度改革研究プロジェクト (ch04)
- 课程沙龙 → 教育ライブ配信・フォーラム (ch04)
- 参赛攻略 → 大会参加ガイド (ch04)
- 品牌视觉识别系统 → ブランドビジュアルアイデンティティシステム (ch01)
- 答辩 → 答弁 (ch01, ch03)
- 检录长 → 検録長 (ch01)
- 检录 → 検録 (ch01)
- 瑞士轮 → スイス式トーナメント (ch01)
- 図伝 → 画像伝送 (ch01, ch05, ch06)

---

## 6. dic.md ISSUES

- Mixed simplified/traditional Chinese in Japanese column: 华为（ファーウェイ）should be ファーウェイ only in Japanese column
- 騰訊（テンセント）should be テンセント
- 小米（シャオミ）should be シャオミ
- 美的集団 uses traditional 団 instead of 団 — inconsistent
- 课程沙龙 uses 沙龙 (Chinese) in Japanese column
- 参赛攻略 uses 參賽攻略 (Chinese) in Japanese column
- 开源材料 in ch04 dic entry missing
- Several team/university names use Chinese characters in Japanese column when katakana or standard Japanese kanji would be better

---

## 7. MISSING 2025-2026 EVIDENCE

The following are mentioned briefly but lack concrete 2026 team examples:

- 2026 engineer robot designs (dual-arm / multi-DOF manipulation)
- Energy-unit manipulation (2026 rule)
- Wheel-legged chassis (2025-2026 evolution)
- Autonomous sentry behavior (2026)
- Radar perception and decision systems (2026 team examples)
- LiDAR-camera fusion (need 2026 repos)
- Wireless charging (mentioned in ch01/ch05 but no team implementation details)
- Current dart systems (2026)
- Current auto-aim implementations (2026 team repos)
- ROS2 stacks (need 2026 repo updates)
- Simulation environments (2026)
- 2026 open-source repositories
- 2026 season planning documents
- 2026 season reports (season retrospectives)
- 2026 competition results (Northeastern University T-DT won — only mentioned in ch04 reference)

---

## 8. CROSS-REFERENCE ISSUES

- mkdocs.yml only lists ch01-ch08 + appendix in nav, ignoring ch09-ch12
- index.md TOC shows ch09-ch12 as "🟡 執筆中・要追記" but they are actually empty
- Internal references like "詳細は第2章" may become stale after restructuring
- README.md TOC doesn't match actual file contents

---

## 9. REFERENCES ISSUES

- Reference [11] in references.md is marked as non-public internal document — should be used carefully
- Several references in body text don't appear in references.md (ch01 has 32 refs but references.md has fewer)
- Some URLs point to BBS threads without specific article numbers
- Chinese characters used in reference titles where Japanese translations should be considered

---

## 10. SUMMARY: WHAT NEEDS TO HAPPEN

1. **Merge ch01-ch03, ch05, ch08** into coherent thematic chapters with single topic ownership
2. **Delete ch09-ch12** (empty/TODO) and redistribute any useful content
3. **Resolve all number conflicts** using newest authoritative sources
4. **Fix all Chinese character contamination** in body text
5. **Fix dic.md** to have clean Japanese equivalents
6. **Add 2025-2026 concrete evidence** for all major technical claims
7. **Downgrade/remove unsupported causal claims** about startups and tech transfer
8. **Separate fact from interpretation** in policy chapter
9. **Update all cross-references** after restructuring
10. **Rebuild index.md, README.md, mkdocs.yml** to reflect new structure
11. **Add validation scripts** for Chinese chars, stale refs, broken links
12. **Update RULES.md** with topic ownership, freshness, causality rules
