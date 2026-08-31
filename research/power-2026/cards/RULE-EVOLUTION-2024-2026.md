# Card: RULE-EVOLUTION-2024-2026

## Sources
- RMUC 2024 Rules V2.1 (2024-07-22) — English PDF
- RMUC 2025 Rules V2.1.0 (2025-08-02) — Chinese PDF
- RMUC 2026 Rules V2.2.0 (2026-08-07) — Chinese PDF
- Protocol 2024 V1.6.4, 2025 V1.7.0, 2026 V2.0.0

## Verified Facts

### 2024 baseline
- **Buffer energy depletion penalty:** HP deduction.
  - Formula: `deducted HP = Maximum HP × N% × 0.1` per 100 ms cycle.
  - Excess percentage: `K = (P_r − P_l) / P_l × 100%`.
  - Source: RMUC 2024 Rules, §Chassis Power Consumption detection.
- **Protocol 0x0202:** Provided `chassis_voltage` (mV), `chassis_current` (mA), `chassis_power` (float W), `buffer_energy` (J).
- **No chassis energy system.** No wireless replenishment mechanic.

### 2025 changes
- **Buffer energy depletion penalty changed to 5-second chassis power cut.**
  - Source: RMUC 2025 Rules §5.1.4: "当缓冲能量耗尽，底盘功率仍超限时，底盘会被断电5秒。"
- **Chassis energy system introduced.**
  - Initial: 23,000; max: 23,000 (same value).
  - "Weakened" state (虚弱): when energy = 0, power limit = 1/3 of applicable base limit (rounded).
  - 125 % boost when energy ≥ 90 % of max (i.e., ≥ 20,700).
- **Flywheel ramp buff added:** Buffer energy temporarily increased to 250 J after triggering flywheel terrain buff; recovers to 60 J max after depletion.
- **Protocol 0x0202:** `chassis_voltage`, `chassis_current`, `chassis_power` fields became `reserved`. Only `buffer_energy` and barrel-heat data remain.
- **Wireless charging introduced** as part of chassis energy replenishment.

### 2026 changes
- **Chassis energy revised:**
  - Initial: 20,000; max: 40,000.
  - Energy-saving state (节能): when energy = 0, base limit = **35 W** (fixed, not 1/3 of base).
  - 125 % boost when energy **≥ 25,000** (i.e., 50 % of max), capped at **200 W**.
- **Flywheel buffer buff removed.** Buffer energy remains fixed at 60 J for all ground robots (no 250 J exception).
- **S7 rule relaxation:** Non-chassis capacitors on Chassis rail permitted up to 10 mF with schematic proof. Enables joint-motor buffer capacitors for legged robots.
- **Protocol 0x0202:** Same as 2025 — voltage/current/power fields remain reserved.

### Engineering significance
1. **2025 power-feedback removal** forces all teams to self-measure or model chassis power; eliminates simple closed-loop control against referee telemetry.
2. **2025 penalty escalation** (HP loss → 5 s mobility loss) makes buffer-energy miscalculation far more punishing; drives adoption of precise motor models and supercapacitors.
3. **2026 S7 relaxation** enables a new hardware category (joint-motor buffer caps) that was previously non-compliant, directly supporting legged-robot designs.

## Quotations
> "After buffer energy has been exhausted, when the chassis power consumption of Hero, Standard, and Sentry exceeds the limit, the deducted HP for each detection cycle = Maximum HP × N% × 0.1."
> — RMUC 2024 Rules (English)

> "当缓冲能量耗尽，底盘功率仍超限时，底盘会被断电5秒。"
> — RMUC 2025 Rules §5.1.4; identical wording in RMUC 2026 §5.1.4

> "在底盘能量消耗至0后，机器人将进入'虚弱'状态。处于'虚弱'状态下的机器人，其底盘功率上限将变为对应性能体系和等级的1/3……"
> — RMUC 2025 Rules §5.6.7 (removed in 2026)

## Reliability
- All three rule PDFs and all three protocol PDFs are official DJI/RoboMaster releases.
- Direct text extraction; no OCR used for Chinese files.
- English 2024 rules confirm the HP-deduction formula explicitly.
