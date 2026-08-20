# Evidence Clusters — Strongest Multi-Source Cases

## Method
Each cluster aggregates sources across types (award panel → BBS → video →
repository → university source). Clusters are rated STRONG / MEDIUM / WEAK.
Only clusters with converging evidence from 2+ independent source types are
included.

---

## Cluster 1: Taurus Dual-Seven-Axis Engineer Robot ⭐ STRONG

**What**: 华南农业大学 Taurus built a dual-seven-axis humanoid engineer robot
with VR headset control, achieving the only 4-level assembly in the 2026 final.

**Sources**:
| Type | ID | Claim | Reliability |
|------|-----|-------|-------------|
| Award panel (seed) | E01 曹铖 | X-wing guided dart embedded + vision | Panel only |
| Award panel (seed) | E08 谭嘉豪 | Seven-DOF arm kinematics + embedded control | Panel only |
| Media | RM2026-0103 | 双七轴仿人形双臂, 4级难度装配, VR操作 | University primary |
| Media | RM2026-0101/0102 | National runner-up, "历史最佳成绩" | Media secondary |
| Bilibili video | RM2026-0442 | Dual-arm demonstration (49k views) | Official primary |
| Bilibili video | RM2026-0444 | VR headset control demonstration | Official primary |
| Competition | RM2026-0440/0445 | Match footage Taurus vs TDT final | Official primary |

**Safe report claims**:
- Taurus fielded a dual-seven-axis humanoid engineer robot at RMUC 2026 final.
- The robot achieved 4-level assembly difficulty (highest tier).
- Operators used a VR headset for teleoperation (gesture tracking).
- Taurus finished as national runner-up (best result in team history).

**Unsupported / needs qualification**:
- "全国唯一" (only team nationally) — not independently verified; safe wording:
  "the only team observed to achieve 4-level assembly at the 2026 final"
- Specific VR technical stack (tracking device, protocol, latency) — not verified

---

## Cluster 2: TDT Wheel-Leg Infantry + Four-Axis Sentry ⭐ STRONG

**What**: 东北大学 TDT won the 2026 championship with innovative wheel-leg
infantry and a four-axis gimbal sentry capable of tunnel traversal.

**Sources**:
| Type | ID | Claim | Reliability |
|------|-----|-------|-------------|
| Media interview | RM2026-0203 | TDT队长 interview, 4年比赛经历 | Media secondary |
| Media | RM2026-0101/0104 | Northern regional champion, national champion | Media secondary |
| Bilibili video | RM2026-0443 | Wheel-leg infantry (304k views) | Official primary |
| Bilibili video | RM2026-0441 | Four-axis gimbal tunnel-traversal sentry | Official primary |
| Competition | RM2026-0440/0445 | Match footage champion final | Official primary |
| GitHub | RM2026-0449 | 2025 radar open source | Repository primary |
| Award nominee | C03 李卓远 | Balance robot MPC, collision detection | Panel only |
| Exhibition panel | IMG_20260808_164237 | "1000+ professionals", textbook claim | Panel only |

**Safe report claims**:
- TDT won RMUC 2026 national championship (also 2019-2020).
- TDT fielded a wheel-leg infantry robot that attracted 304k video views.
- TDT's sentry used a four-axis gimbal configuration for tunnel traversal.
- TDT maintains an active open-source presence (radar, 2025).

**Unsupported / needs qualification**:
- "四轴云台越隧" exact mechanical details — video shows capability but not
  engineering drawings
- Exhibition panel claims: "1000+ professionals", textbook 《RoboMaster竞赛步兵机器人设计》,
  "100+ patents" — NOT verified
- Direct link between TDT and NEU formal course C3000000119 — NOT confirmed
  (instructor is ACTION/Robocon advisor, not TDT)

---

## Cluster 3: Fudan EGA Sliding-Mode Controller (SMC) ⭐ STRONG

**What**: 复旦大学 星云EGA used sliding-mode control (SMC) across all robot
types, achieving top sentry hit rate, and open-sourced the controller as
teaching material.

**Sources**:
| Type | ID | Claim | Reliability |
|------|-----|-------|-------------|
| Award panel (seed) | M01 包毅 | Team building: survival → system → growth | Panel only |
| Award panel (seed) | M15 张安 | Founded team,社团→战队孵化 | Panel only |
| Award panel (seed) | E14 张安 | Object-oriented general control framework | Panel only |
| BBS | RM2026-0416 | SMC云台控制器教学&开源, 全兵種适用 | Team primary |
| BBS/GitHub | RM2026-0416/0417 | SMC controller + over-tunnel infantry/sentry | Team primary |
| GitHub | xinruilee04/smc_controller | Open-source implementation | Repository primary |
| Bilibili | RM2026-0202 | RL wheel-leg "天枢号" | Team primary |

**Safe report claims**:
- Fudan EGA adopted SMC for gimbal control across all robot types (infantry,
  hero, sentry, drone).
- EGA open-sourced the SMC controller with detailed educational documentation.
- EGA's sentry achieved top hit rate in match averages (per BBS claim).
- EGA also developed a reinforcement-learning wheel-leg robot "天枢号".

**Unsupported / needs qualification**:
- "哨兵局均命中率Top 1" — sourced from BBS only; safe wording:
  "the team reports its sentry achieved the highest match-average hit rate"
- Specific numerical hit rate percentage — not provided

---

## Cluster 4: ZJU Hello World Energy Mechanism + Wheel-Leg Sentry Nav ⭐ STRONG

**What**: 浙江大学 Hello World open-sourced energy-mechanism auto-attack
algorithm and wheel-leg sentry navigation.

**Sources**:
| Type | ID | Claim | Reliability |
|------|-----|-------|-------------|
| Award nominee | A07 李树华 | Factor-graph odometry, terrain semantic planning, MPC | Panel only |
| Award nominee | W01 顾银峰 | Supercap + buffer cap power control board | Panel only |
| BBS/GitHub | RM2026-0422 | Energy mechanism auto-attack algorithm | Team primary |
| GitHub | RM2026-0423 | Wheel-leg sentry navigation (Polyacetone) | Repository primary |
| BBS | RM2026-0424 | Personal hardware project | Team primary |
| BBS | RM2026-0403/0406 | Fluorescent charging | Team primary |

**Safe report claims**:
- Hello World open-sourced an energy-mechanism auto-attack algorithm.
- Hello World open-sourced wheel-leg sentry navigation using ROS2.
- Individual members published hardware projects.

**Unsupported**:
- Competition performance claims beyond open-source (no match footage linked)

---

## Cluster 5: SZU RobotPilots Guided Dart + Visual Framework ⭐ STRONG

**What**: 深圳大学 RobotPilots open-sourced their 2026 guided dart system
(mechanical + hardware + OpenMV vision), YOLOv8-Pose energy mechanism,
and a plugin-based auto-aim framework.

**Sources**:
| Type | ID | Claim | Reliability |
|------|-----|-------|-------------|
| Award nominee | A12 张育铭 | FPGA all-hardware radar parsing, anti-jamming | Panel only |
| Award nominee | E05 梁衍强 | Embedded design/test methodology | Panel only |
| Award nominee | W07 庄腾辉 | Wireless charging + power optimization | Panel only |
| BBS | RM2026-0418 | Guided dart open source (mech+hw+OpenMV) | Team primary |
| BBS | RM2026-0420 | YOLOv8-Pose energy mechanism 5-point ID | Team primary |
| GitHub | RM2026-0421 | Plugin-based auto-aim framework | Repository primary |
| BBS | RM2026-0419 | Odin1 spatial memory module | Team primary |
| University | RM2026-0479 | ICRA 2018 3rd place, K-12 collaboration | University primary |
| Exhibition panel | IMG_20260805_124111 | 24h platform, mentorship (unverified) | Panel only |

**Safe report claims**:
- RobotPilots open-sourced their 2026 guided dart system.
- RobotPilots developed YOLOv8-Pose for energy-mechanism recognition.
- RobotPilots released a plugin-based auto-aim framework.
- The team placed 3rd at ICRA 2018 DJI RoboMaster AI Challenge.
- University provides formal support through the "Internationalization Action Plan".

**Unsupported**:
- "24-hour open experimental platform" — panel claim only
- "Matrix management / tier reform" — panel claim only
- FPGA radar claim (A12) — no repository found

---

## Cluster 6: BIT DreamChaser FPGA-Guided Dart ⭐ STRONG

**What**: 北京理工大学 DreamChaser built an FPGA-based guided dart system
with 300FPS recognition frame rate.

**Sources**:
| Type | ID | Claim | Reliability |
|------|-----|-------|-------------|
| Award nominee | A11 喻衡 | 3D sliding map, dynamic trajectory planning | Panel only |
| Award nominee | E10 王博 | Software architecture, semantic routing | Panel only |
| Award nominee | H09 王锐泽 | Transformable sentry (chassis deformation) | Panel only |
| Award nominee | W05 魏洲航 | FPGA-guided dart target ID + motion control | Panel only |
| BBS | RM2026-0405 | FPGA制导飞镖, 300FPS, 机械+制导+视觉 | Team primary |

**Safe report claims**:
- DreamChaser developed an FPGA-based guided dart system.
- The vision system achieves 300FPS recognition frame rate.
- The system covers mechanical, guidance, and vision subsystems.

**Unsupported**:
- "300FPS" — BBS claim only; safe wording: "the team reports 300FPS"
- Actual competition hit rate — not verified

---

## Cluster 7: ECUST Qiyuan Serial-Leg Infantry + Double Wheel-Leg ⭐ STRONG

**What**: 华东理工大学 起源 placed 3rd nationally with serial-leg infantry
and double wheel-leg structure.

**Sources**:
| Type | ID | Claim | Reliability |
|------|-----|-------|-------------|
| Media | RM2026-0105 | National 3rd place, first-time finalist | University primary |
| Media | RM2026-0101/0102 | Regional Shanghai 3rd place | Media secondary |
| Bilibili | RM2026-0446 | Low-profile tunnel-traversal serial-leg infantry | Official primary |
| BBS/GitHub | RM2026-0452 | 2024-2026 open source summary | Team primary |
| Award nominee | H01 陈诣博 | Tunnel-traversal serial-leg infantry | Panel only |
| Award nominee | E13 薛杰克 | Multi-modal self-recovery + gait state machine | Panel only |

**Safe report claims**:
- Qiyuan achieved national 3rd place at RMUC 2026 (first-time finalist).
- Qiyuan developed serial-leg infantry capable of tunnel traversal.
- Qiyuan used a double wheel-leg structure design.
- Qiyuan has an active open-source presence (custom controller, referee system).

**Unsupported**:
- Specific mechanical advantages over other serial-leg designs — not quantified

---

## Cluster 8: NPU WMJ Radar (Single SDR + GNU Radio) ⭐ STRONG

**What**: 西北工业大学 WMJ built a radar system using a single SDR and GNU
Radio, achieving 186.4s average countermeasure time.

**Sources**:
| Type | ID | Claim | Reliability |
|------|-----|-------|-------------|
| Award nominee | H05 缪越 | Mechanical innovations for engineer/dual-arm | Panel only |
| BBS/GitHub | RM2026-0411 | Full radar open source: single SDR + GNU Radio | Team primary |
| GitHub | zplszz/WMJRadar | Implementation repository | Repository primary |

**Safe report claims**:
- WMJ open-sourced a complete radar system using ROS2 Humble + Nav2 + MPPI +
  BehaviorTree.CPP.
- The radar uses a single SDR approach with GNU Radio.
- Match-average countermeasure time: 186.4 seconds (per BBS).
- Built from zero to full function in ~1 month.

**Unsupported / needs qualification**:
- "186.4s" — BBS claim only; safe wording: "the team reports 186.4s"
- Comparison to other teams' radar performance — not independently verified

---

## Cluster 9: SCUT South China Tiger SimulatorX ⭐ STRONG

**What**: 华南理工大学 华南虎 developed and open-sourced SimulatorX, a
full RMUC match simulator for operator training and tactical analysis.

**Sources**:
| Type | ID | Claim | Reliability |
|------|-----|-------|-------------|
| BBS/GitHub | RM2026-0465 | SimulatorX open-source technical report (2022) | Team primary |
| GitHub | scutrobotlab/RM2022_SimulatorX | Full repository | Repository primary |
| GitHub | wintbiit/Simulator | 2021 predecessor version | Repository primary |
| University | RM2026-0478 | 2017-2018 championships, experimental teaching center | University primary |
| Exhibition panel | IMG_20260805_124119 | "71 universities using SimulatorX" | Panel only |

**Safe report claims**:
- 华南虎 developed SimulatorX, a full RMUC match simulator.
- The simulator supports local practice and online multiplayer modes.
- 华南虎 won national championships in 2017 and 2018.
- The team operates under the university's official Experimental Teaching Center.

**Unsupported**:
- "71 universities using SimulatorX" — panel claim only
- "National first-class undergraduate course 《工业机器人》" — panel claim only

---

## Cluster 10: HEU Chuangmeng Education Model ⭐ STRONG

**What**: 哈尔滨工程大学 创梦之翼 operates a formal four-level progressive
training system integrated with robot engineering and AI majors.

**Sources**:
| Type | ID | Claim | Reliability |
|------|-----|-------|-------------|
| University | RM2026-0477 | Official hrbeu.edu.cn news (2022-06-29) | University primary |
| Exhibition panel | IMG_20260805_124057 | "三真实、三融合、五递进" | Panel only |

**Safe report claims**:
- Chuangmeng (founded 2011) operates a four-level competition system:
  intramural (Y1) → league (Y2) → RMUC (Y3) → AI challenge (Y4/graduate).
- The platform integrates course experiments, enterprise practice, technology
  innovation, and research training.
- Supports robot engineering and AI new-engineering majors.
- 6 innovation courses, 8000+ person-hours, 80%+ graduate school rate.

**Unsupported**:
- "三真实、三融合、五递进" specific terminology — not found in official source
- "313 students entered robot enterprises" — panel claim only

---

## Cluster 11: DGUT Robot Application Development Course ⭐ STRONG

**What**: 东莞理工学院 offers a named 3.5-credit/56-hour robot application
development course in its official Computer Science curriculum.

**Sources**:
| Type | ID | Claim | Reliability |
|------|-----|-------|-------------|
| University | RM2026-0476 | Official cs.dgut.edu.cn curriculum page | University primary |
| Exhibition panel | IMG_20260808_164259 | "机器人应用开发实践" 56学时 3.5学分 | Panel only |

**Safe report claims**:
- DGUT's Computer Science program lists "机器人应用开发实践" as a 3.5-credit
  disciplinary cross-integration course.
- The course runs 4 hours/week for 14 weeks (56 class hours total).
- This is a formal credited course in the official curriculum.

**Unsupported**:
- OpenCV/Webots/ROS/SLAM content details — syllabus not found
- 515 students in 3 years — panel claim only
- ACE Fund 200,000 RMB — panel claim only

---

## Cluster 12: HIT(SZ) Nangong Xiaoying Education Integration ⭐ MEDIUM

**What**: 哈工大(深圳) 南工骁鹰 operates under the official Experimental and
Innovative Practice Education Center with ~80 members and 54 awards.

**Sources**:
| Type | ID | Claim | Reliability |
|------|-----|-------|-------------|
| University | RM2026-0473 | Multiple hitsz.edu.cn articles (2018-2025) | University primary |
| GitHub/BBS | RM2026-0459 | Radar point-cloud localization open source | Team primary |
| Exhibition panel | IMG_20260808_164255 | 2 school-enterprise courses, 2 teaching papers | Panel only |

**Safe report claims**:
- Nangong Xiaoying was founded in 2016 with ~80 permanent members.
- The team operates under the university's Experimental and Innovative Practice
  Education Center.
- Cumulative 54 provincial-level+ awards.
- ICRA 2018 DJI RoboMaster AI Challenge global runner-up.

**Unsupported**:
- "2 school-enterprise collaborative courses" — panel claim only
- "2 teaching research papers" — panel claim only
- DJI EP teaching platform claim — panel claim only

---

## Cluster 13: JLU Jijia Master Innovation Base ⭐ MEDIUM

**What**: 吉林大学 吉甲大师双创基地 is an officially recognized innovation
base with a 1 million RMB fundraising target and cross-disciplinary platform.

**Sources**:
| Type | ID | Claim | Reliability |
|------|-----|-------|-------------|
| University | RM2026-0474 | Party Secretary visit (2025) + fund page | University primary |
| University | jlu.edu.cn (2020) | TARS-GO team profile | University primary |
| Exhibition panel | IMG_20260808_164253 | Course claims, award counts | Panel only |

**Safe report claims**:
- Jijia Master Base exists as an official university entity.
- The university Party Secretary visited in May 2025.
- An official fundraising page targets 1 million RMB.
- TARS-GO team (founded 2018) placed top 16 in its first competition.

**Unsupported**:
- "National first-class undergraduate course" — not verified against MoE lists
- 56 national-level awards — panel claim only
- 3 incubated companies — panel claim only

---

## Cluster 14: USTB Reborn + Innovation Base ⭐ MEDIUM

**What**: 北京科技大学 Reborn team (2018, 30+ members) operates within an
official student innovation base where all undergraduates must complete ≥2
innovation credits.

**Sources**:
| Type | ID | Claim | Reliability |
|------|-----|-------|-------------|
| University | RM2026-0475 | Official USTB PDF (academic affairs) | University primary |
| University | ustb.edu.cn (2014/2019) | Quality/employment reports | University primary |
| Exhibition panel | IMG_20260805_124052 | "竞技机器人实践" course | Panel only |

**Safe report claims**:
- Reborn team exists (2018, 30+ members, advisor 王旭).
- Innovation/entrepreneurship credits (≥2) are REQUIRED for all undergraduates.
- 8 innovation labs, ~2000 sqm, serving 1500+ students/year.
- 70%+ student competition coverage, 30%+ award rate.

**Unsupported**:
- "竞技机器人实践" as a specific course title — not confirmed
- Reborn directly serving as a teaching platform — not confirmed
- 1700+ students — panel claim; 1500+ confirmed

---

## Cluster 15: NEU Robot Innovation Design Course ⭐ MEDIUM

**What**: 东北大学 offers a formal elective course 《机器人创新设计》
(C3000000119) taught by a robot competition advisor.

**Sources**:
| Type | ID | Claim | Reliability |
|------|-----|-------|-------------|
| University | RM2026-0472 | Official course catalog PDF | University primary |
| Exhibition panel | IMG_20260808_164237 | TDT education model claims | Panel only |

**Safe report claims**:
- NEU offers 《机器人创新设计》 as a credited undergraduate elective.
- Instructor: 丛德宏, founder of ACTION team, ABU Robocon advisor.
- The course covers multi-disciplinary robot design content.

**Unsupported / needs qualification**:
- The instructor is linked to ACTION/Robocon, NOT TDT specifically.
- The course description does NOT mention RoboMaster.
- "《RoboMaster 竞赛步兵机器人设计》textbook" — NOT found
- "1000+ professionals", "100+ patents" — panel claims only

---

*Created: 2026-08-20*
*Total clusters: 15*
*STRONG: 11 | MEDIUM: 4 | WEAK: 0*
