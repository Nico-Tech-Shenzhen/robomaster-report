# Card: GLUT-2025-SUPERCAP

## Source
- **Team:** 桂林理工大学 群星战队
- **Year:** RM2025
- **Title:** RM2025超级电容控制板Plus「硬件篇」
- **URLs:**
  - Forum (hardware): https://bbs.robomaster.com/article/714505
  - Forum (manual): https://bbs.robomaster.com/article/715177
  - GitHub: https://github.com/DonotFreeze/RM-PCB-SuperCapControlBoard_Plus
- **Authority:** S (primary source: open hardware + documentation)

## Verified Facts

### Topology and specs
- **Topology:** Bidirectional buck-boost (series topology, not four-switch buck-boost).
- **MCU:** STM32G431CBT6.
- **Gate driver:** LM5109.
- **Half-bridge MOSFET:** IRFH7440TRPBF.
- **Inductor:** 106-125 toroid, 22 µH (4-wire 1.0 mm, 11 turns).
- **Rated power:** 150 W @ 24 V / 12 V.
- **Efficiency:** 96 % (author claim, not independently verified).
- **Capacitor bank:** 7S 3 V 60 F (nominal ~1,890 J @ 21 V).

### Remote voltage compensation (远端补偿)
- **Purpose:** Eliminate wiring-resistance voltage-drop error between PMM Chassis port and supercap board battery port, aligning student power measurement with referee measurement.
- **Method:** Full-differential amplifier samples voltage at PMM Chassis port via MMCX-KWE → SMA coaxial cable; board measures `V_MMI` instead of `V_BAT`.
- **Tested accuracy:** With ~50 cm 18 AWG silicone wire at 24 V / 0–10 A load, power detection error vs referee: **±1 W** (with compensation) vs **−5 W** (without compensation).
- **Critical design note:** Must use **full-differential amplifier**; single-ended measurement cannot compensate negative-wire drop.

### Current sensing
- **Low-side (bottom-switch) current sampling** via TLV9061 + 2 mΩ sense resistor.
- Gain 20 V/A; 2.5 V reference, 0.82 V offset → range −20 A (charge) to +40 A (discharge).
- Author estimates effective resolution ~0.1 A after noise.
- Replaced INA181 from Lite version due to burn-out incidents from hot-plug surges.

### Hardware protection
| Protection | Implementation |
|-----------|----------------|
| Input surge | SMC TVS at battery and cap ports |
| Aux supply surge | Self-resetting fuse (100 mA) + series resistor + small TVS |
| ESD | Added to all pins connected to power lines (learned from OPA1_OUT burn-out in Lite) |
| Overcurrent / short | 5 A slow-blow fuse; fuse-blow detection via voltage-divider (`BOOM_IN`) |
| PMOS/PWM timing | Hardware delay circuit (AND + OR gates) ensures PMOS always on before PWM starts and off after PWM stops |

### Connector / mounting
- Board size: 45 × 75 × 20 mm (Plus), stackable with capacitor bank.
- 3D-printed TPU cover for bottom-side components.
- CAN bus with switchable 120 Ω termination resistor.

### Observed failures
- **Lite version (RM2024):** Collective MOSFET blow-out just before league match, possibly due to PWM/PMOS timing bug in code V1.1. This motivated hardware timing protection in Plus.
- **INA181 burn-out** in Lite from hot-plug surges.
- **Buffer-energy depletion during sharp turns:** Author reports that when using pure buffer-energy closed loop, a sudden turn during full-power driving could exhaust buffer energy and trigger chassis power cut.

### Power-control integration
- Library V1.2 pairs with XJTLU motor-power-model approach: supercap automatically compensates when chassis power exceeds limit; control command reduced to "enable" flag + power-limit value.

## Quotation
> "经过测试，加入线损补偿之后，电源管理模块chassis接口到超级电容控制板之间使用约50cm的18AWG硅胶线进行连接，在24V，0-10A负载的范围内，超级电容控制板Plus的功率检测数值与裁判系统显示的数值误差在±1W；去掉线损补偿后，误差达到了-5W。"
> — GLUT RM2025 Plus hardware article

## Reliability
- Full KiCad 8.0 project, Gerber, and BOM published.
- Author distinguishes Plus (RM2025) from Lite (RM2024); this card covers Plus only.
- Performance claims (efficiency, accuracy) are author-reported bench measurements, not match conditions.
