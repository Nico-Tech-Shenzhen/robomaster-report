# RoboMaster 2026 Power-System Evidence Summary

Scope: targeted research to close GitHub Issue #3 evidence gaps.  
Reference date: 2026-08-31.

---

## 1. How does RoboMaster govern electrical power in 2026?

### 1.1 Chassis power limits by robot type and performance system (RMUC 2026 V2.2.0)

| Robot | Configuration | Level 1 | Level 10 | Fixed / Notes |
|-------|--------------|---------|----------|---------------|
| Hero | 近战优先 (melee-priority) | 70 W | 120 W | — |
| Hero | 远程优先 (remote-priority) | 50 W | 100 W | — |
| Infantry | 功率优先 (power-priority) | 60 W | 100 W | — |
| Infantry | 血量优先 (HP-priority) | 45 W | 100 W | — |
| Engineering | — | 120 W | 120 W | Fixed; no performance system |
| Sentinel (auto) | — | 100 W | 100 W | Fixed; 400 HP |
| Sentinel (semi-auto) | — | 60 W | 60 W | Fixed; 200 HP |

*Source:* §5.4.2 性能体系, 表 5-13, 表 5-14, 表 3-4, 表 3-7.

*Definition:* **底盘功率** = "机器人产生水平方向上平移、旋转运动的动力系统的功率" (§2 重要概念). The PMM measures power at the **Chassis port output**, not at motor terminals.

### 1.2 Buffer-energy (缓冲能量) mechanism (§5.1.4)

- **Q = 60 J** for all ground robots (hero, infantry, sentinel, engineering).
- **Settlement frequency: 10 Hz** (100 ms).
- When instantaneous chassis output **P_r > P_l** (limit), buffer energy **Z** is consumed: `Z = Z − (P_r − P_l) × 0.1`.
- When **Z ≤ 0** and **P_r > P_l**: **chassis powered off for 5 seconds** (底盘会被断电5秒). After 5 s, Z resets to Q.

### 1.3 Chassis-energy (底盘能量) mechanism (§5.6.7)

A separate **game-resource** energy pool distinct from physically stored capacitor energy:

- **Initial:** 20,000 per hero/infantry/sentinel.
- **Maximum:** 40,000.
- **Consumption:** PMM "Chassis" interface outputs 1 J → resource **−1**.
- **Replenishment:**
  - Wireless charging while occupying supply-zone buff.
  - When Supercapacitor Management Module (SCMM) is charging the supercap, the energy difference between SCMM input and PMM Chassis output accumulates; every **1 J difference → resource +8**.

### 1.4 Energy-saving state and performance boost (§5.6.7)

- When chassis energy drops to **0**: robot enters **"节能"** (energy-saving) state.
  - Chassis power limit **base value = 35 W**.
- When chassis energy **≥ 25,000**: base limit becomes **125 % of the applicable performance-system base limit**, **capped at 200 W**.

### 1.5 Supercapacitor governance (Spec V2.0.0 §2.1.1.1)

- **S6:** Single supercap module nominal energy ≤ **2,000 J**; measured ≤ **2,200 J**.
- **S7:** For chassis power path, capacitors **not participating in chassis power** are permitted with total nominal capacitance ≤ **10 mF**. Teams must show schematic at inspection. This enables joint-motor buffer capacitors (缓冲电容) for legged robots.
- SCMM must remain online; offline triggers HP deduction (§5.1.5, 图 5-3).

### 1.6 Referee-system telemetry removal

- **Protocol 0x0202** in 2024 provided `chassis_voltage`, `chassis_current`, `chassis_power` (float), and `buffer_energy`.
- In **2025 and 2026**, voltage/current/power fields became **`reserved`**. Only `buffer_energy` and barrel-heat data remain available to students.
- **Referee enforcement continues internally**; the removal affects student closed-loop control, not rule compliance.

---

## 2. What engineering problems does this create for teams?

### 2.1 Power-model uncertainty (caused by protocol change)
- Teams can no longer read chassis power directly from referee telemetry. They must build a **motor power model** from CAN feedback (torque, speed) and self-measure or estimate power.
- Without accurate self-measurement, a 5 W discrepancy can push a 100 W-limited robot into buffer depletion (桂林理工大学 observed −5 W error without remote compensation).

### 2.2 Buffer-energy penalty severity (caused by 2025 rule change)
- In 2024, buffer depletion caused gradual HP loss. In 2025–2026, it causes **5 seconds of complete mobility loss**.
- This makes "buffer-based burst acceleration" far riskier. One miscalculation = robot stops in place and is quickly killed.

### 2.3 Chassis-energy budget management (new in 2025–2026)
- Teams must track a **second energy pool** (chassis energy) that modulates the base power limit via the 35 W / 125 % rules.
- Supercap charging strategy now affects not only physical stored energy but also the **game-resource replenishment rate** (+8 per 1 J SCMM-Chassis difference).

### 2.4 Joint-motor undervoltage under peak torque (addressed by 2026 S7)
- Legged robots using joint motors (达妙 8009/8009P/10010) draw very high instantaneous bus current during jumps.
- Battery internal resistance + wiring resistance cause **undervoltage shutdown** of joint-motor controllers, especially with low-health TB48 batteries.
- The 2026 S7 relaxation permits buffer capacitors on the joint-motor bus, but teams must still design pre-charge / inrush protection and high-power relay shutdown circuits.

### 2.5 Vibration, wiring, and connector reliability
- Mechanical vibration causes connector loosening and wire fatigue.
- Observed failures in ZJU HelloWorld 2026: bolt falling into supercap board, XT30 loosening, wire breakage.
- Teams emphasize thick wire for joint-motor supply (不要用很细的线) and recommend testing battery internal resistance with electronic load rather than trusting health indicators.

---

## 3. What concrete student implementations demonstrate this?

### Case A — Motor power model / dynamic allocation
**天津工业大学 304战队 (RM2025–2026)**
- **Source:** GitHub `TGURM304/PowerManager`; forum article 1882902.
- **Model:** `W = K0 + K1·current + K2·speed + K3·current·speed + K4·current² + K5·speed²`, fitted with `Fitting.py` against bench measurements.
- **Allocation:** Error-based proportional distribution among 4 motors; 8 W reserved base power per motor when total limit > 54 W.
- **Supercap interface:** `buffer_power_attenuation` (0.0–1.0) scales total available power from supercap state-of-charge.
- **Swerve extension:** Two `ChassisPowerManager` instances with 50 % steer / 50 % wheel split.
- **Result:** Author reports no obvious overpower issues in RMUL 2026.

### Case B — Supercapacitor / energy control + wiring compensation
**桂林理工大学 群星战队 (RM2025)**
- **Source:** Forum 714505; GitHub `DonotFreeze/RM-PCB-SuperCapControlBoard_Plus`.
- **Topology:** Bidirectional buck-boost (series), STM32G431, 150 W rated, 7S 3V 60F cap bank.
- **Remote compensation:** Full-differential amplifier samples PMM Chassis port voltage via coaxial cable; achieves **±1 W** accuracy vs referee (vs −5 W without compensation) at 24 V / 0–10 A over 50 cm 18 AWG wire.
- **Protection:** SMC TVS, 5 A slow-blow fuse with blow detection, ESD on all power-connected pins, hardware PMOS/PWM timing delay circuit (motivated by Lite-version collective MOSFET blow-out).
- **Integration:** Pairs with XJTLU motor-power-model approach; control command reduced to "enable" + power-limit.

### Case C — Power tree / DC-DC / isolation / protection
**西交利物浦大学 OmniX战队 (RM2025–2026)**
- **Source:** Forum 1914397; OmniCtrl 2 Pro manual / schematic.
- **Input:** XT30, 19–30 V typical, ±60 V abs; TI TPS26600 eFuse with reverse-polarity, UVLO, OVP, OCP, hot-swap control.
- **Tree:** MPS MP4423 24 V→5 V buck → TPS25942A eFuse (5V@2.5A) → TPS2553 (USB 5V@1A) → TLV76733 digital 3.3 V + LP5912 analog 3.3 V (high PSRR for IMU).
- **Sequencing:** FLT/PGOOD cascade ensures strict power-up order; single-fault shutdown.
- **Domains:** 5V-D (on-board), 5V-E (external, bidirectional), 3V3-D (digital), 3V3-A (analog).
- **Result:** Zero main-board burn-outs during RM2026 season except one GPIO wiring error; validated through 24-hour continuous-op and abnormal-power tests.

### Case D — Power conversion / noise / ripple
**华中科技大学 狼牙战队 (RM2025–2026)**
- **Source:** Forum 376777; OSHWHUB `fengl/mp2980-ultra-small-buck-boost`.
- **Chip:** MPS MP2980GR four-switch buck-boost controller (valley/peak current mode, FCCM).
- **Specs:** 6–36 V in, 0.5–28 V out, 10 A max; 98.1 % peak efficiency; **77 mVpp ripple** @ 20 V / 7 A.
- **Application:** 24 V → 20 V NUC mini-PC supply, replacing traditional aluminum-block modules.
- **Cost:** < 55 RMB; 4-layer PCB, JLCPCB compatible.
- **Limitation:** QFN-32 soldering difficulty; TVS must be sized to actual input voltage.

---

## 4. Verified 2024→2026 rule changes worth adding to Chapter 3

| Year | Change | Evidence | Significance |
|------|--------|----------|--------------|
| **2024** | Buffer depletion → **HP deduction** (`Max HP × N% × 0.1`). | RMUC 2024 Rules (English) | Baseline penalty was survivable; gradual HP loss. |
| **2025** | Buffer depletion → **5-second chassis power cut**. | RMUC 2025 §5.1.4; identical in 2026 §5.1.4 | Makes power-control errors far more punishing; drives adoption of precise motor models and supercapacitors. |
| **2025** | **Chassis energy** system introduced (initial 23,000; "weakened" at 1/3 power; 125% boost at ≥90%). | RMUC 2025 §5.6.7 | New resource-management layer affects energy-budget strategy and supercap charging tactics. |
| **2025** | Chassis-power feedback **removed** from protocol 0x0202. | Protocol 2025 V1.7.0 | Forces all teams to self-measure or model power; eliminates simple buffer-energy closed loop against referee telemetry. |
| **2026** | Chassis energy revised: **20,000/40,000**; "energy-saving" at **35 W**; 125% boost at **≥25,000** (capped 200 W). | RMUC 2026 §5.6.7 | Widens dynamic range of power-limit modulation; rewards mid-game energy management. |
| **2026** | **S7 relaxed restrictions** on non-chassis supercapacitor banks (≤10 mF with schematic proof). | Spec 2026 V2.0.0 §S7 | Enables joint-motor buffer capacitors for legged robots, directly supporting jump-capable designs without illegal battery-cell replacement. |
| **2026** | Flywheel buffer buff (250 J) **removed**; buffer energy fixed at 60 J. | RMUC 2026 §5.1.4 vs RMUC 2025 §5.1.4 | Simplifies buffer-energy accounting; removes terrain-dependent power burst. |

**Verdict:** The 2025 protocol removal + penalty escalation, combined with the 2026 S7 supercap relaxation and chassis-energy revision, form a coherent three-step evolution that explains why 2026 teams are heavily investing in (a) motor power models, (b) high-performance supercapacitors with precise sensing, and (c) joint-motor buffer capacitors. This is worth a compact chronology in Chapter 3.

---

## 5. Best evidence for Ch2, Ch3 and Ch7

### Chapter 2 — Rules & Governance
- **Primary:** RMUC 2026 Rules V2.2.0 (2026-08-07) PDF — chassis power limits, buffer energy definition, 5s penalty, chassis energy, energy-saving state, performance system. [Card: OFFICIAL-2026-RULES]
- **Primary:** Spec 2026 V2.0.0 — S6/S7 supercap limits, wireless charging rules. [Card: OFFICIAL-2026-SPEC]

### Chapter 3 — Rule Evolution
- **Primary:** Protocol comparison 2024/2025/2026 — 0x0202 field removal. [Card: PROTOCOL-COMPARISON]
- **Supporting:** RMUC 2024 Rules (English) — HP-deduction baseline. [Card: RULE-EVOLUTION-2024-2026]
- **Supporting:** RMUC 2025 Rules — 5s cut, chassis energy v1, 250J flywheel buff. [Card: RULE-EVOLUTION-2024-2026]
- **Supporting:** RMUC 2026 Rules — revised chassis energy, S7 relaxation, flywheel buff removed. [Card: RULE-EVOLUTION-2024-2026]

### Chapter 7 — Student Engineering & Power Systems
- **Motor power model / allocation:** 天津工业大学 304战队 (GitHub + forum). [Card: TJU304-2026-MOTOR-MODEL]
- **Supercapacitor + remote compensation + protection:** 桂林理工大学 群星战队 (forum + GitHub). [Card: GLUT-2025-SUPERCAP]
- **Power tree / eFuse / domain separation:** 西交利物浦 OmniX (forum + manual + schematic). [Card: XJTLU-OMNIX-2026-POWER-TREE]
- **DC-DC conversion / ripple / thermal:** 华中科技大学 狼牙战队 (forum + OSHWHUB). [Card: HUST-2026-MP2980]
- **Buffer capacitor / legged robot (supporting):** 浙江大学 HelloWorld (forum 1936347). [Card: ZJU-2026-BUFFER in SOURCE-MAP]
- **Wireless charging / supply noise (supporting / conflict check):** 北京理工大学 DreamChaser (forum 1890297). [Card: BIT-2026-WIRELESS in SOURCE-MAP]

---

## Stop condition assessment

| Criterion | Status |
|-----------|--------|
| Latest official 2026 rule evidence | ✅ RMUC 2026 V2.2.0 + Spec V2.0.0 cited with exact section/table numbers |
| 2–4 technically distinct student implementations | ✅ 4 cases covering (A) motor model/allocation, (B) supercap/energy control/compensation, (C) power tree/eFuse/protection, (D) DC-DC conversion/ripple |
| Enough evidence to answer Issue #3 | ✅ All five SUMMARY questions answered with primary-source citations and exact values |

Research stopped per instruction.
