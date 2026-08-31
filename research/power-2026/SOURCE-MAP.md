# Source Map — RoboMaster 2026 Power-System Research (Issue #3)

Last updated: 2026-08-31

---

## Official Sources

### OFFICIAL-2026-RULES
- **Title:** RoboMaster 2026 机甲大师超级对抗赛比赛规则手册 V2.2.0
- **Date:** 2026-08-07
- **URL:** https://hz-rm-bbs-web-prod.oss-cn-hangzhou.aliyuncs.com/e354d2750e17485e8f67e5b5a9d1a2891786094242879/RoboMaster%202026%20%E6%9C%BA%E7%94%B2%E5%A4%A7%E5%B8%88%E8%B6%85%E7%BA%A7%E5%AF%B9%E6%8A%97%E8%B5%9B%E6%AF%94%E8%B5%9B%E8%A7%84%E5%88%99%E6%89%8B%E5%86%8CV2.2.0%EF%BC%88260807%EF%BC%89.pdf
- **Authority:** A (official primary)
- **Key sections:** §2 (底盘功率 definition), §3.1–3.5 (robot key features), §5.1.4 (buffer energy / 5s cut), §5.4.2 (performance system tables), §5.6.7 (chassis energy / 节能状态 / wireless replenishment)
- **Scope verified:** Chassis power limits by type/level, buffer energy Q=60J / 10Hz, 5s power-cut penalty, chassis energy 20000/40000, energy-saving 35W, 125% boost capped at 200W, replenishment accounting (1J out = −1, 1J SCMM diff = +8).

### OFFICIAL-2026-SPEC
- **Title:** RoboMaster 2026 机甲大师高校系列赛机器人制作规范手册 V2.0.0
- **Date:** 2026-06-26
- **URL:** https://hz-rm-bbs-web-prod.oss-cn-hangzhou.aliyuncs.com/413aa7734f004c9bb2a9da532c503f111782458120014/RoboMaster%202026%20%E6%9C%BA%E7%94%B2%E5%A4%A7%E5%B8%88%E9%AB%98%E6%A0%A1%E7%B3%BB%E5%88%97%E8%B5%9B%E6%9C%BA%E5%99%A8%E4%BA%BA%E5%88%B6%E4%BD%9C%E8%A7%84%E8%8C%83%E6%89%8B%E5%86%8CV2.0.0%EF%BC%88260626%EF%BC%89.pdf
- **Authority:** A (official primary)
- **Key data:** S6 (supercap 2000J nominal / 2200J measured), S7 (non-chassis caps ≤10mF), S70–S77 (wireless charging frequency, power, size, safety).

### PROTOCOL-COMPARISON
- **Titles:** Protocol 2024 V1.6.4, 2025 V1.7.0, 2026 V2.0.0
- **Authority:** A (official primary)
- **Key data:** 0x0202 field changes: 2024 had chassis_voltage, chassis_current, chassis_power, buffer_energy; 2025/2026 replaced first three with reserved, keeping only buffer_energy.

---

## Student Implementation Sources

### TJU304-2026-MOTOR-MODEL
- **Team:** 天津工业大学 304战队
- **Year:** RM2025–2026
- **Title:** 天津工业大学 304 战队功率控制算法
- **URLs:**
  - GitHub: https://github.com/TGURM304/PowerManager
  - Forum: https://bbs.robomaster.com/article/1882902
- **Authority:** S (primary source, full code + README)
- **Key data:** 6-coeff motor power model (K0–K5); Fitting.py; error-based allocation; supercap attenuation interface; swerve-drive split; deployed in RMUL 2026.

### GLUT-2025-SUPERCAP
- **Team:** 桂林理工大学 群星战队
- **Year:** RM2025
- **Title:** RM2025超级电容控制板Plus「硬件篇」
- **URLs:**
  - Forum: https://bbs.robomaster.com/article/714505
  - GitHub: https://github.com/DonotFreeze/RM-PCB-SuperCapControlBoard_Plus
- **Authority:** S (primary source, open hardware + documentation)
- **Key data:** STM32G431 buck-boost; 150W rated; remote voltage compensation (±1W vs referee); low-side current sampling; TVS/fuse/ESD/PMOS-timing hardware protection; 45×75×20mm; collective MOSFET blow-out incident in Lite version.

### XJTLU-OMNIX-2026-POWER-TREE
- **Team:** 西交利物浦大学 OmniX战队
- **Year:** RM2025–2026
- **Title:** OmniCtrl 2 Pro 主控板开源
- **URLs:**
  - Forum: https://bbs.robomaster.com/article/1914397
  - Manual: OmniCtrl-Pro-2-Manual-1_0.pdf
  - Schematic: SCH_OMX_OmniCtrl_Pro_2_2558.pdf
  - OSHWHUB: https://oshwhub.com/misakasirin/project_gdvefyxb
- **Authority:** S (primary source, full schematic + manual + PCB)
- **Key data:** 6-layer PCB; TPS26600 front-end eFuse (±60V); MP4423 24V→5V DCDC; TPS25942A/TPS2553 eFuse cascade; 3V3-D / 3V3-A split; FLT/PGOOD sequencing; 24h continuous-op validation; zero burn-outs in RM2026 season.

### HUST-2026-MP2980
- **Team:** 华中科技大学 狼牙战队
- **Year:** RM2025–2026
- **Title:** MP2980超小BUCK-BOOST升降压模块
- **URLs:**
  - Forum: https://bbs.robomaster.com/article/376777
  - OSHWHUB: https://oshwhub.com/fengl/mp2980-ultra-small-buck-boost
- **Authority:** S (primary source, open design + measured data)
- **Key data:** MP2980 four-switch buck-boost; 6–36V in, 0.5–28V out, 10A max; 98.1% efficiency, 77mVpp ripple @ 20V/7A; <55 RMB; for NUC 24V→20V supply.

---

## Historical Rule Sources

### RMUC-2024-RULES
- **Title:** RoboMaster 2024 University Championship Rules Manual V2.1
- **Date:** 2024-07-22
- **URL:** https://terra-1-g.djicdn.com/b2a076471c6c4b72b574a977334d3e05/RM2024/RoboMaster%202024%20University%20Championship%20Rules%20Manual%20V2.1%20(20240722).pdf
- **Authority:** A (official archival)
- **Key data:** Buffer depletion → HP deduction (Max HP × N% × 0.1); no chassis energy; no wireless charging.

### RMUC-2025-RULES
- **Title:** RoboMaster 2025 机甲大师超级对抗赛比赛规则手册 V2.1.0
- **Date:** 2025-08-02
- **URL:** https://terra-1-g.djicdn.com/b2a076471c6c4b72b574a977334d3e05/RM2025/RoboMaster%202025%20%E6%9C%BA%E7%94%B2%E5%A4%A7%E5%B8%88%E8%B6%85%E7%BA%A7%E5%AF%B9%E6%8A%97%E8%B5%9B%E6%AF%94%E8%B5%9B%E8%A7%84%E5%88%99%E6%89%8B%E5%86%8CV2.1.0%EF%BC%8820250802%EF%BC%89.pdf
- **Authority:** A (official primary)
- **Key data:** 5s chassis cut penalty introduced; chassis energy initial 23000/max 23000; "weakened" state at 1/3 power; 125% boost at ≥90%; flywheel buffer 250J; protocol fields removed.

---

## Supporting / Cited Sources

### BIT-2026-WIRELESS
- **Team:** 北京理工大学 DreamChaser
- **Year:** RM2026
- **Title:** 基于DAB双有源桥的无线充电装置开源
- **URL:** https://bbs.robomaster.com/article/1890297
- **Authority:** B (primary open-source documentation)
- **Key data:** DAB topology; 40×58mm; >85% efficiency; passed inspection at northern regional; supply noise caused false coil detection → charging disabled during matches.

### ZJU-2026-BUFFER
- **Team:** 浙江大学 HelloWorld战队
- **Year:** RM2026
- **Title:** 超级电容&缓冲电容 硬件同构
- **URL:** https://bbs.robomaster.com/article/1936347
- **Authority:** B (primary open-source with PCB files)
- **Key data:** Shared FSBB board for chassis supercap and joint-motor buffer cap; S7 rule relaxation enabling buffer caps outside chassis; ~1300W peak; 45×45×25mm board.
