# Card: OFFICIAL-2026-SPEC

## Source
- **Title:** RoboMaster 2026 机甲大师高校系列赛机器人制作规范手册 V2.0.0
- **Date:** 2026-06-26
- **URL:** https://hz-rm-bbs-web-prod.oss-cn-hangzhou.aliyuncs.com/413aa7734f004c9bb2a9da532c503f111782458120014/RoboMaster%202026%20%E6%9C%BA%E7%94%B2%E5%A4%A7%E5%B8%88%E9%AB%98%E6%A0%A1%E7%B3%BB%E5%88%97%E8%B5%9B%E6%9C%BA%E5%99%A8%E4%BA%BA%E5%88%B6%E4%BD%9C%E8%A7%84%E8%8C%83%E6%89%8B%E5%86%8CV2.0.0%EF%BC%88260626%EF%BC%89.pdf
- **Authority:** A (official primary)

## Verified Facts

### S6 — Supercapacitor energy limit (§2.1.1.1)
- Hero, Infantry, Sentinel: single supercapacitor module nominal energy ≤ **2,000 J**; measured energy ≤ **2,200 J**.
- Nominal energy formula: `E = ½ × C × U²` (U = rated voltage, C = capacitance).

### S7 — Non-chassis capacitors (§2.1.1.1)
> "对于受功率限制的机器人的底盘动力能源，接入 Chassis 接口但不参与底盘功率的电容标称容量之和不大于 10mF。"
> 
> "如超级电容模组中使用的电容组不参与底盘功率，需携带对应的原理图在检录时进行佐证。"

- **Key implication:** The 2026 rule explicitly permits capacitors on the Chassis power rail that do **not** participate in chassis power, provided total nominal capacitance ≤ 10 mF and schematic is shown at inspection. This enables joint-motor buffer capacitors (缓冲电容) for legged robots.

### S67–S77 — Wireless charging (§2.1.10)
- S70: Operating frequency **100 kHz – 148.5 kHz**.
- S72: Transmitter idle power ≤ **1 W**.
- S74: Max sensing distance ≤ **30 mm**.
- S75: Supply-zone transmitter max size **500 × 500 × 300 mm**.
- S76: Must use official 24 V ± 1 V, max 200 W DC supply (XT60 female); cable ≤ 500 mm.
- S77: Receiver only allowed on hero/infantry/sentinel; max **1 per robot**.

## Reliability
- Direct PDF from official RoboMaster CDN.
- Section numbers verified against PDF text extract.
