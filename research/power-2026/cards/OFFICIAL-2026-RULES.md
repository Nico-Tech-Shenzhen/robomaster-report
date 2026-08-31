# Card: OFFICIAL-2026-RULES

## Source
- **Title:** RoboMaster 2026 机甲大师超级对抗赛比赛规则手册 V2.2.0
- **Date:** 2026-08-07
- **URL:** https://hz-rm-bbs-web-prod.oss-cn-hangzhou.aliyuncs.com/e354d2750e17485e8f67e5b5a9d1a2891786094242879/RoboMaster%202026%20%E6%9C%BA%E7%94%B2%E5%A4%A7%E5%B8%88%E8%B6%85%E7%BA%A7%E5%AF%B9%E6%8A%97%E8%B5%9B%E6%AF%94%E8%B5%9B%E8%A7%84%E5%88%99%E6%89%8B%E5%86%8CV2.2.0%EF%BC%88260807%EF%BC%89.pdf
- **Authority:** A (official primary)

## Verified Facts

### Chassis power definition (§2, 表 2-1)
> 底盘功率 — "机器人产生水平方向上平移、旋转运动的动力系统的功率，详见《RoboMaster 2026 机甲大师高校系列赛机器人制作规范手册》中'裁判系统安装规范'章节中底盘功率的定义。"

### Chassis power limits by robot type (§3.1–3.5, §5.4.2)

| Robot | Configuration | Level 1 | Level 10 | Notes |
|-------|--------------|---------|----------|-------|
| Hero — 近战优先 | melee-priority | 70 W | 120 W | 上限血量 260→600 |
| Hero — 远程优先 | remote-priority | 50 W | 100 W | 上限血量 200→400 |
| Infantry — 功率优先 | power-priority | 60 W | 100 W | 上限血量 150→400 |
| Infantry — 血量优先 | HP-priority | 45 W | 100 W | 上限血量 200→400 |
| Engineering | — | 120 W (fixed) | 120 W | 不适用经验与性能体系 |
| Sentinel — 自动 | auto-run | 100 W (fixed) | 100 W | 上限血量 400 |
| Sentinel — 半自动 | semi-auto | 60 W (fixed) | 60 W | 上限血量 200 |

*Source: §5.4.2 性能体系, 表 5-13, 表 5-14, 表 3-4, 表 3-7*

### Buffer-energy mechanism (§5.1.4)
- **Q** = buffer energy upper limit = **60 J** for all ground robots.
- **Settlement frequency: 10 Hz** (100 ms cycle).
- When instantaneous chassis output power **P_r > P_l** (limit), buffer energy **Z** is consumed proportionally to excess power: `Z = Z − (P_r − P_l) × 0.1`.
- When **Z ≤ 0** and **P_r > P_l**: **chassis powered off for 5 seconds** (底盘会被断电5秒).
- After 5 s, Z resets to Q.

### Chassis-energy mechanism (§5.6.7)
- **Initial chassis energy:** 20,000 per hero/infantry/sentinel robot.
- **Maximum chassis energy:** 40,000.
- **Consumption:** PMM "Chassis" interface outputs 1 J → resource decreases by 1. Cannot go negative.
- **Replenishment:**
  - Wireless charging while occupying supply-zone buff.
  - When Supercapacitor Management Module (input) is charging the supercap, the difference between SCMM input energy and PMM Chassis output energy accumulates; every **1 J difference → resource +8**.

### Energy-saving state and performance boost (§5.6.7)
- When chassis energy drops to **0**: robot enters **"节能"** (energy-saving) state.
- In energy-saving state: chassis power limit **base value = 35 W**.
- When chassis energy **≥ 25,000**: base limit becomes **125 % of the applicable performance-system base limit**, **capped at 200 W**.

### Module-offline penalty (§5.1.5, 图 5-3)
- Referee server detects module connection at **2 Hz**.
- Offline supercapacitor management module triggers **HP deduction** (not chassis power cut).

## Quotations (transcribed)
> "裁判系统持续监控机器人底盘功率，机器人底盘需在功率限制范围内运行。地面机器人底盘功率超限时，该机器人将扣除缓冲能量。当缓冲能量耗尽，底盘功率仍超限时，底盘会被断电5秒。裁判系统进行底盘功率检测的结算频率是10Hz。"
> — §5.1.4

> "每局比赛中，每台英雄、步兵、哨兵机器人各具有20000的初始底盘能量和40000的底盘能量上限。在底盘能量消耗至0后，机器人将进入'节能'状态。处于'节能'状态下的机器人，其底盘功率上限基础值将变为35W。在底盘能量大于等于25000时，机器人底盘功率上限基础值将变为对应性能体系和等级底盘功率上限基础值的125%，最高不会超过200W。"
> — §5.6.7

> "电源管理模块'Chassis'接口每输出1J能量，底盘能量减少1。底盘能量不会变为负值。"
> — §5.6.7

> "在超级电容管理模块接口（输入）正在向超级电容传输能量时，超级电容管理模块接口（输入）与电源管理模块Chassis接口的输出能量之差每达到1J，底盘能量增加8。"
> — §5.6.7

## Reliability
- Direct PDF from RoboMaster official OSS CDN.
- Text extracted and section references verified against PDF page numbers and TOC.
