# CODEX Handoff — RoboMaster 2026 China Corpus

## 1. Corpus Overview

**Total sources**: 79  
**Coverage**: 2026 season (regional → national final) + post-season open-source wave (August 2026) + education exhibition panels (from-arena-to-classroom)  
**Language**: Primarily Chinese (Simplified)  
**Date range**: 2022–2026 (strongest density in 2026-03 to 2026-08)

### Category Breakdown

| Category | Count | Description |
|----------|-------|-------------|
| Official / primary | 4 | robomaster.com rules, live results, BBS official posts |
| Media reports | 5 | People's Daily, China Youth Daily, Shenzhen News, etc. |
| Team / technical docs | 4 | University news, captain interviews, team profiles |
| Open-source GitHub/Gitee | 5 | Ecosystem tools: rm-battlescope, RMOSS, rm_vision, etc. |
| BBS first-pass open source | 8 | March–May 2026 team technical releases |
| BBS second-pass open source | 24 | August 2026 post-season concentrated open source |
| Bilibili technical videos | 9 | Official DJI competition videos + fan compilations |
| Team GitHub (second pass) | 7 | Team-specific repo discoveries |
| AWARD 2026 nominee related | 16 | Nominee panel seeds + derived repository findings |
| 从赛场到课堂 education survey | 8 | Exhibition panel transcriptions + primary source verification |
| Recruitment / industry | 1 | DJI official hiring page |

### Team Source Count Leaders

| Team | University | Sources |
|------|-----------|---------|
| Taurus | 华南农业大学 | 6 |
| TDT | 东北大学 | 6 |
| Hello World | 浙江大学 | 5 |
| RobotPilots | 深圳大学 | 5 |
| EGA / 星云EGA | 复旦大学 | 4 |
| Alliance | 南京理工大学 | 4 |
| 笃行 | 西安交通大学 | 4 |
| 起源 | 华东理工大学 | 3 |
| 未来 | 青岛大学 | 3 |

---

## 2. Strongest Evidence Clusters (15)

These clusters have **converging evidence from 2+ independent source types** (media + video + repository + university source). They are the safest material for report writing.

| # | Cluster | Team/University | Source Types | Strength |
|---|---------|----------------|--------------|----------|
| 1 | **Dual-seven-axis engineer robot + VR teleop** | Taurus / 华南农业大学 | Award panel + media + Bilibili video + competition footage | ⭐ STRONG |
| 2 | **Wheel-leg infantry + four-axis tunnel sentry** | TDT / 东北大学 | Media + Bilibili video + competition + GitHub + exhibition | ⭐ STRONG |
| 3 | **Sliding-mode controller (SMC) open-sourced** | EGA / 复旦大学 | Award panel + BBS + GitHub + Bilibili | ⭐ STRONG |
| 4 | **Energy mechanism auto-attack + wheel-leg sentry nav** | Hello World / 浙江大学 | Award nominee + BBS + GitHub | ⭐ STRONG |
| 5 | **Guided dart + YOLOv8-Pose + auto-aim framework** | RobotPilots / 深圳大学 | Award nominee + BBS + GitHub + university | ⭐ STRONG |
| 6 | **FPGA-guided dart 300FPS** | DreamChaser / 北京理工大学 | Award nominee + BBS | ⭐ STRONG |
| 7 | **Serial-leg infantry tunnel traversal** | 起源 / 华东理工大学 | Media + Bilibili + BBS/GitHub + award nominee | ⭐ STRONG |
| 8 | **Radar: single SDR + GNU Radio** | WMJ / 西北工业大学 | Award nominee + BBS + GitHub | ⭐ STRONG |
| 9 | **SimulatorX match simulator open-sourced** | 华南虎 / 华南理工大学 | BBS + GitHub + university + exhibition | ⭐ STRONG |
| 10 | **Four-level progressive training system** | 创梦之翼 / 哈尔滨工程大学 | University primary + exhibition panel | ⭐ STRONG |
| 11 | **3.5-credit/56-hour robot course** | DGUT / 东莞理工学院 | University primary + exhibition panel (exact match) | ⭐ STRONG |
| 12 | **Education center team: 80 members, 54 awards** | 南工骁鹰 / 哈工大(深圳) | University primary + GitHub + exhibition | MEDIUM |
| 13 | **Official innovation base + fundraising** | 吉甲大师 / 吉林大学 | University primary + exhibition | MEDIUM |
| 14 | **Innovation base: 8 labs, 1500+/year, required credits** | Reborn / 北京科技大学 | University primary + exhibition | MEDIUM |
| 15 | **Elective course C3000000119** | TDT / 东北大学 | University primary + exhibition | MEDIUM |

---

## 3. Safe-to-Use Claims vs. Claims Requiring Verification

### ✅ SAFE — High Confidence, Multi-Source

Use these freely with standard attribution:

- **Competition results**: TDT champion, Taurus runner-up, 起源 3rd, SuperPower 4th (multi-source media + official)
- **Taurus dual-seven-axis arms + level-4 assembly**: Verified by university source + official Bilibili video + match footage
- **TDT wheel-leg infantry**: 304k-view official Bilibili video
- **TDT four-axis tunnel sentry**: Official Bilibili video + People's Daily
- **Fudan SMC controller**: Open-sourced on GitHub with educational documentation (xinruilee04/smc_controller)
- **ZJU energy mechanism + wheel-leg sentry nav**: BBS + GitHub (Polyacetone)
- **SZU guided dart + YOLOv8-Pose + plugin auto-aim**: BBS + GitHub
- **BIT FPGA dart**: BBS technical report
- **ECUST serial-leg tunnel traversal**: Bilibili official + GitHub open source
- **NPU WMJ radar**: GitHub (zplszz/WMJRadar) + BBS
- **SCUT SimulatorX**: GitHub (scutrobotlab/RM2022_SimulatorX) + BBS
- **DGUT 3.5-credit/56-hour course**: Official cs.dgut.edu.cn curriculum page
- **HEU four-level progressive system**: Official hrbeu.edu.cn
- **USTB required innovation credits (≥2)**: Official academic affairs PDF

### ⚠️ USE WITH QUALIFICATION — Single Source or Panel Only

These require careful wording ("the team reported...", "exhibition panel claimed..."):

- **Taurus "only team with level-4 assembly"** → "the only team observed to achieve level-4 assembly at the 2026 final"
- **Taurus "3 level-4 assemblies"** → "Taurus reported completing 3 level-4 assemblies"
- **FPGA "300FPS"** → "the team reports 300FPS recognition frame rate"
- **SHARK radar "1927.2s"** → "SHARK team reported an average marked-time metric of 1927.2s"
- **WMJ radar "186.4s"** → "the team reports 186.4s average countermeasure time"
- **Employment rate "near 100%"** → "media reports cited a high employment rate; exact methodology unavailable"
- **Cumulative numbers** (941 universities, 200,000 engineers, 1000+ DJI hires) → Always note "cumulative" and time-anchor ambiguity

### ❌ DO NOT USE WITHOUT PRIMARY SOURCE

These are **exhibition panel claims only** with no corroboration found:

- SimulatorX "used by 71 universities"
- TDT "1000+ professionals", "100+ patents", textbook 《RoboMaster竞赛步兵机器人设计》
- DGUT "ACE Fund 200,000 RMB"
- HEU "313 students entered robot enterprises"
- JLU "56 national-level awards", "3 incubated companies"
- USTB "竞技机器人实践" as a specific course title (base confirmed, exact title not)
- TYUST "280 class hours", "800+/year", "99 awards", "6 companies"
- HIT(SZ) "2 school-enterprise courses", "2 teaching papers"

---

## 4. Instructions to Codex

### Before Writing
1. **Read `claims-audit.md` first**. It is the single source of truth for claim safety.
2. **Read `evidence-clusters.md`** for multi-source convergence details.
3. **Read `from-arena-to-classroom.md`** for education exhibition panel context.

### While Writing
- **Prioritize STRONG clusters** (1–11) for technical claims.
- **Always use safe wording** from the Claims Audit "Safe wording" column.
- **Never use superlatives** (only, first, 100%) unless multi-source verified.
- **Distinguish panel claims from verified claims**: exhibition panels are field notes, not primary documentation.
- **URL-verify before citing**: many BBS/GitHub links may decay; check accessibility.
- **Credit properly**: BBS post = 战队自述; university news = 校官网; Bilibili = 官方视频 or 战队投稿.

### What This Corpus Does NOT Cover
- Detailed V1→V2 rule comparisons (only high-level changes)
- Quantitative Sim2Real gap analysis
- 2027 rule predictions (hero→heavy robot rumors)
- Wireless charging implementation details (awaiting SJTU Jiaolong open-source confirmation)
- Alumni network specifics
- Complete AWARD nominee technical profiles (selective search only)

---

## 5. Remaining Evidence Gaps

| Gap | Priority | Notes |
|-----|----------|-------|
| TDT textbook confirmation | Medium | 《RoboMaster竞赛步兵机器人设计》— not found in CNKI or university catalog |
| SimulatorX 71-school claim | Medium | Panel only; no download analytics or institutional list found |
| ACE Fund 200k RMB | Low | DGUT panel claim; may be internal fund with no public record |
| HEU enterprise placement (313) | Low | Conflicts with 80%+ grad-school rate in official source |
| HIT(SZ) school-enterprise courses | Low | 2 courses claimed; not found in hitsz.edu.cn course catalog |
| TYUST NewMaker base details | Low | Search returned 404; may need direct contact |
| 2027 rule changes | Low | Beyond corpus scope; rumors only |
| SJTU Jiaolong wireless charging | Medium | RM2026-0453 may contain this; not yet analyzed |
| RMOSS/rm_vision 2026 combat usage | Low | Ecosystem tools exist but battle-proven status unclear |

---

## 6. File Map

```
research/china-2026/
├── INDEX.md                     # Master source list (79 entries)
├── source-map.md                # Cross-source relationship map
├── claims-audit.md              # ⭐ START HERE — claim safety ratings
├── evidence-clusters.md         # 15 multi-source clusters
├── from-arena-to-classroom.md   # 15-university education panel transcription
├── award-priority-table.md      # AWARD nominee search priorities (completed)
├── rules-and-results.md         # Competition rules & results
├── robots-engineer.md           # Engineer robot findings
├── robots-sentry-radar.md       # Sentry & radar findings
├── vision-autoaim.md            # Vision & auto-aim findings
├── dart-air.md                  # Dart & aerial findings
├── software-simulation.md       # Software & simulation findings
├── open-source.md               # Open-source ecosystem findings
├── team-operation.md            # Team operation findings
├── recruitment-industry.md      # Recruitment & industry findings
├── universities-policy.md       # University policy findings
└── sources/
    └── RM2026-NNNN.md           # Individual source cards
```

---

*Created: 2026-08-20*  
*Corpus status: Final research pass complete*  
*Handoff target: Codex report-writing phase*
