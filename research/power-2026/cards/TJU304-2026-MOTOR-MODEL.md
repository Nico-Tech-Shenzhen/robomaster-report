# Card: TJU304-2026-MOTOR-MODEL

## Source
- **Team:** 天津工业大学 304战队
- **Year:** RM2025–2026 (deployed in RMUL 2026)
- **Title:** 天津工业大学 304 战队功率控制算法
- **URLs:**
  - GitHub: https://github.com/TGURM304/PowerManager
  - Forum: https://bbs.robomaster.com/article/1882902
- **Authority:** S (primary source: open code + first-hand documentation)

## Verified Facts

### Architecture
- Single-motor power model + 4-motor chassis power manager.
- Supports omnidirectional wheels, Mecanum wheels, and **swerve-drive** (舵轮) allocation.
- C++ implementation with `power_manager.h` / `power_manager.cpp`; Python `Fitting.py` for parameter identification.
- MIT License.

### Motor power model
```
W = K0
  + K1 × current
  + K2 × speed
  + K3 × current × speed
  + K4 × current²
  + K5 × speed²
```
- `current` = motor feedback current / `real_current_conversion` (default 1000 for M3508).
- `speed` = motor feedback speed (rpm).
- Fitted against bench measurements: power meter in series with motor+ESC branch, sampling at varied speed and load.

### Tested parameters
**M3508:**
- K0 = 0.65213, K1 = −0.15659, K2 = 0.00041660, K3 = 0.00235415, K4 = 0.20022, K5 = 1.08×10⁻⁷

**GM6020:**
- K0 = 0.7507578, K1 = −0.0759636, K2 = −0.00153397, K3 = 0.01225624, K4 = 0.19101805, K5 = 0.0000066450

### Power allocation strategy
- **Error-based distribution:** `ChassisPowerManager::allocatePower()` distributes total limit among 4 motors proportionally to PID error magnitude.
- **Reserved base power:** When total limit > 54 W, each motor reserves 8 W base power; remaining power split by error ratio. When limit ≤ 54 W, split purely by error.
- **Supercap attenuation interface:** `buffer_power_attenuation` (0.0–1.0) scales total available power; intended to map supercap state-of-charge to temporary headroom.

### Swerve-drive extension
- Two `ChassisPowerManager` instances (steer group + wheel group).
- Total power split: 50 % to steer motors first, remainder to wheel motors.
- Author notes this 50 % ratio is empirically tuned and should be adjusted per chassis design.

### Observed results
- Author reports: "在 26 赛季 RMUL 中，部署该模块的机器人均未出现明显超功率问题，实际效果较好。"
- Prior season (RM2025): team had no mature power-control module; frequent overpower caused robots to "停在原地、被迅速击杀".

### Limitations noted by author
- Example parameters are preliminary; teams should re-sample and re-fit for their own motors, supply topology, and load conditions.
- No load data significantly affects model quality; high-speed region hard to cover manually.

## Quotation
> "刚开始做功率控制时，我曾尝试直接通过电机反馈数据计算电机消耗功率，但由于误差较大，很难用简单公式直接算准。后来在观看中科大电控教程并参考其他开源项目后，才意识到更常见的做法是先拟合电机模型，再根据模型预测功率。"
> — TJU304 README, "算法思路" section

## Reliability
- Full source code (`power_manager.cpp`, `power_manager.h`, `Fitting.py`) available on GitHub.
- README includes self-reported test conditions and deployment scope (RMUL 2026).
- No independent verification of match performance beyond author's claim.
