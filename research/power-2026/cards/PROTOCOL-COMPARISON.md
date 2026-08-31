# Card: PROTOCOL-COMPARISON

## Sources

### Protocol 2024
- **Title:** RoboMaster 裁判系统串口协议附录 V1.6.4
- **Date:** 2024-07-15
- **URL:** https://terra-1-g.djicdn.com/b2a076471c6c4b72b574a977334d3e05/RM2024/RoboMaster%20%E8%A3%81%E5%88%A4%E7%B3%BB%E7%BB%9F%E4%B8%B2%E5%8F%A3%E5%8D%8F%E8%AE%AE%E9%99%84%E5%BD%95%20V1.6.4%EF%BC%8820240715%EF%BC%89.pdf
- **Authority:** A (official primary)

### Protocol 2025
- **Title:** RoboMaster 裁判系统串口协议附录 V1.7.0
- **Date:** 2024-12-25
- **URL:** https://terra-1-g.djicdn.com/b2a076471c6c4b72b574a977334d3e05/RoboMaster%20%E8%A3%81%E5%88%A4%E7%B3%BB%E7%BB%9F%E4%B8%B2%E5%8F%A3%E5%8D%8F%E8%AE%AE%E9%99%84%E5%BD%95%20V1.7.0%EF%BC%8820241225%EF%BC%89.pdf
- **Authority:** A (official primary)

### Protocol 2026
- **Title:** RoboMaster 2026 机甲大师高校系列赛通信协议 V2.0.0
- **Date:** 2026-06-26
- **URL:** https://hz-rm-bbs-web-prod.oss-cn-hangzhou.aliyuncs.com/2568625171b44e49a44541ec0dbdd2d51782458406243/RoboMaster%202026%20%E6%9C%BA%E7%94%B2%E5%A4%A7%E5%B8%88%E9%AB%98%E6%A0%A1%E7%B3%BB%E5%88%97%E8%B5%9B%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE%20V2.0.0%EF%BC%88260626%EF%BC%89.pdf
- **Authority:** A (official primary)

## Verified Facts

### Command 0x0202 — Power / Heat Data

| Field | 2024 (V1.6.4) | 2025 (V1.7.0) | 2026 (V2.0.0) |
|-------|---------------|---------------|---------------|
| Bytes 0–1 | `chassis_voltage` (mV) | `reserved` | `reserved` |
| Bytes 2–3 | `chassis_current` (mA) | `reserved` | `reserved` |
| Bytes 4–7 | `chassis_power` (float, W) | `reserved` | `reserved` |
| Bytes 8–9 | `buffer_energy` (J) | `buffer_energy` (J) | `buffer_energy` (J) |
| Remaining | barrel heat fields | barrel heat fields | barrel heat fields (17 mm + 42 mm only) |
| Total size | 16 bytes | 16 bytes | 14 bytes |

### Interpretation
- **2024:** Student robots received real-time PMM Chassis-port voltage, current, and computed power via serial protocol.
- **2025 → 2026:** Voltage, current, and power fields were **removed from student telemetry** (marked `reserved`). Only `buffer_energy` and barrel-heat data remain.
- **Referee-system enforcement continues:** The PMM still measures chassis power internally; the removal affects **student-side closed-loop control**, not rule enforcement.

## Quotation (2025 protocol)
> 表 2-9 0x0202
> 字节偏移量 大小 说明
> 0 2 保留位
> 2 2 保留位
> 4 4 保留位
> 8 2 缓冲能量（单位：J）

## Reliability
- All three PDFs downloaded from official DJI / RoboMaster CDNs.
- Field names and offsets verified against C struct definitions in each PDF.
