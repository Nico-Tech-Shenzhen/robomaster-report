# Card: XJTLU-OMNIX-2026-POWER-TREE

## Source
- **Team:** 西交利物浦大学 OmniX战队
- **Year:** RM2025–2026 (deployed in RMUL 2026)
- **Title:** OmniCtrl 2 Pro 主控板开源
- **URLs:**
  - Forum: https://bbs.robomaster.com/article/1914397
  - Manual: OmniCtrl-Pro-2-Manual-1_0.pdf (Oct 2025)
  - Schematic: SCH_OMX_OmniCtrl_Pro_2_2558.pdf
  - OSHWHUB: https://oshwhub.com/misakasirin/project_gdvefyxb
- **Authority:** S (primary source: full schematic + manual + PCB files)

## Verified Facts

### Power input
- **Connector:** XT30-F + XT30-M (internally parallel), max 30 A through-current.
- **Input range:** 19–30 V typical; ±60 V absolute maximum (includes reverse-polarity protection).
- **Front-end protection:** TI TPS26600 eFuse / ideal-diode controller with UVLO, OVP, OCP, hot-swap control, reverse-polarity / reverse-current protection.

### Power tree (DCDC + LDO + eFuse cascade)
| Stage | Chip | Function | Limits |
|-------|------|----------|--------|
| Front-end | TI TPS26600 | eFuse / ideal diode | 30 V @ 500 mA max; ±60 V abs |
| DCDC | MPS MP4423AGQ | 24 V → 5 V buck | 3 A abs; 15 W capability |
| eFuse 5V | TI TPS25942A | 5V rail protection | 5 V @ 2.5 A max; bi-directional |
| eFuse USB | TI TPS2553 | USB SINK limit | 5 V @ 1 A max |
| LDO digital | TI TLV76733 | 5 V → 3.3 V (digital) | 0.5 A max |
| LDO analog | TI LP5912 | 5 V → 3.3 V (analog) | high PSRR for VDDA/VREF |
| Voltage ref | TI REF2933 | 3.3 V reference | reserved for future use |

### Power sequencing
- Each stage's **FLT/PGOOD** output drives the **EN** pin of the next stage.
- Creates strict power-up sequence; single-fault shutdown prevents downstream damage.
- 5V-D and 5V-E domains are separated by bidirectional eFuse; auto-selects supply direction and prevents back-feeding.

### Power domains
- **5V-D:** Main on-board switched rail (from internal DCDC or from 5V-E via eFuse).
- **5V-E:** External peripheral / expansion rail. Can be sourced externally or from 5V-D. All external-facing power interfaces use this domain.
- **3V3-D:** Digital supply for STM32H7, STM32F0, most logic.
- **3V3-A:** Analog supply for IMU (BMI088, DETA10) and H7 VDDA/VREF. Uses **high-PSRR LDO** to reduce noise.

### Protection features
| Feature | Implementation |
|---------|---------------|
| Reverse polarity | TPS26600 R2VP (reverse-polarity + reverse-direction protection) |
| Overvoltage | TPS26600 OVP (typ. 30 V shutdown); TPS25942A OVLO |
| Overcurrent | TPS26600 OCP; TPS25942A OCP; TPS2553 OCP |
| Short-circuit | TPS25942A SCP (auto-retry after 128 ms) |
| Thermal | TPS25942A OTP |
| Undervoltage | TPS26600 UVLO; TPS2553 UVLO |

### Observed robustness
- Author reports **no main-board burn-outs** during entire RM2026 preparation season except one GPIO level wiring error.
- Validation tests include: 15 V undervoltage, 40 V overvoltage, −24 V reverse polarity, 2 A overcurrent, short-circuit, 24-hour continuous operation.
- 6-layer PCB: signal–ground–signal / signal–power–signal, split power ground and digital ground to reduce crosstalk.

### Mechanical
- 4 × M2.5 mounting holes.
- Must use insulating bottom shell (PC FR recommended); otherwise risk of severe short.
- If using expansion board, must use standoffs to prevent B2B connector from taking direct force.

## Quotation
> "板载完善的电源支持与保护机制，使其能够在各类恶劣电源环境下稳定工作……支持最大30V电压输入，并自带±60V eFuse进行电源保护，支持防反接，浪涌、短路、过流、欠压、过压保护等功能。"
> — OmniX forum article

> "电源采用 DCDC+LDO 多层组合方案，并在关键节点前后穿插 eFuse 芯片实现冗余保护。每层电源芯片的 FLT/PGOOD 输出到下一层电源芯片的 EN 实现严格的上电时序控制，并在单点故障时及时关断后部电路避免异常动作。"
> — OmniCtrl 2 Pro Manual, §2 电源与电源域

## Reliability
- Full schematic (PDF) and PCB layout (Gerber, epro2) published.
- Manual provides component-level limits (MAX vs ABS ratings).
- Observed reliability is author-reported fleet experience (all OmniX robots in RMUL 2026 season), not independent third-party test.
