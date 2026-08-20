# RoboMaster 2026: ソフトウェア・シミュレーション

## ROS2/Nav2ベースのセントリーシステム

### 遼寧科技大学 COD（完全なROS2スタック）

- **ROS2 Humble + Nav2 + BehaviorTree.CPP + MPPI** [RM2026-0408]
- 以下のGiteeリポジトリ群で公開：
  - ナビゲーション: `cod_-rm2026_-navigation`
  - 決定: `cod_-rm2026_-behavior-tree`
  - 自瞄: `sentry-auto-aim`
  - 下位機: `rmcod2026_-sentry`

### Nav2構成詳細

| モジュール | 実装 | 備考 |
|-----------|------|------|
| SLAM | SLAM Toolbox + small_pointlio | 純LIO方式 |
| ナビゲーション | Navigate Through Poses | 連続航路点通過 |
| コントローラー | MPPI Controller | 障害物回避性能一流 |
| Goal Checker | PositionGoalChecker | 角度朝向を考慮しない |
| 脱困 | PolarBearプラグイン | コピー |
| シミュレーション | loopback sim | Gazebo不要 |

### MPPIコントローラーの調整ポイント
- stdではなく**temperatureとgamma**に注目
- pathfollow/pathalignのweightは10以下
- GoalCriticのweightとthreshold_to_considerを上げることで速度向上
- 目標点付近での円周運動問題は、wrapperコントローラーで強制固定速度+KP誘導で解決

## Sim2Realフレームワーク

### 深北莫 PolarBear

- **「アルゴリズム仿真→半实物テスト→実車検証」**の開発フロー [RM2026-0305]
- **Gazeboシミュレーター**: `rmu_gazebo_simulator`（JavaScript, 94 stars）
- **セントリーSim2Real**: `pb2025_sentry_nav`（C++, 409 stars）
- **整車TFモデリング**: chassis-gimbal間にgimbal_odomを挿入
- **Robot Description**: joint_states → robot_state_publisher → /tf, /tf_static
- **コード品質**: pre-commit + GitHub Action

### シミュレーション環境比較

| チーム | シミュレーター | 特徴 |
|--------|--------------|------|
| PolarBear | Gazebo | ROS2対応、整車モデリング |
| COD | loopback sim | Gazebo不要、pixiワンクリック展開 |
| RMOSS | Gazebo/Ignition | 公式エコシステム |

## 視覚アルゴリズムフレームワーク

### rm_vision（SCAU-RM-NAV）

- **GitHub**: https://github.com/SCAU-RM-NAV/rm_vision
- **目的**: 規範的・使いやすい・堅牢・高性能な視覚フレームワーク
- **含まれるモジュール**:
  - `rm_auto_aim`: 装甲板自動瞄准
  - `ros2_mindvision_camera`: MindVisionカメラ
  - `ros2_hik_camera`: HikVisionカメラ
  - `rm_gimbal_description`: ジンバルURDF
  - `rm_serial_driver`: 串口通信
  - `rm_vision_simulator`: 視覚シミュレーター
- **Docker対応**: `chenjunnn/rm_vision:lastest`

### 同済大学 SuperPowerフレームワーク（影響力大）

- **傘库（umbrella library）形式**: 多数のモジュールを単一の共有库に集約
- **最小自瞄单元**: 串口-DM_IMU-カメラの独立動作構造
- **ROS2ノード化**: PlotJuggler連携、Topicによるモジュール間通信
- 多くのチーム（COD、奇点等）が参考にしている

### 自瞄アルゴリズムの進化

| チーム | ベース | 独自改良 |
|--------|--------|---------|
| COD | FYT | sp_vision_25最適化、2段階装甲板分類、Yaw最適化 |
| 奇点 | FYT + 交龍 | Matcher馬氏距離、同済EKF Q/R行列 |
| RobotPilots | 独自 | RP-26AutoAim-Frame |

## データ解析ツール

### rm-battlescope

- **機能**: 赛事データ解析、戦術リプレイ、攻撃関係推論
- **入力**: SQLite秒級テレメトリ
- **出力**: HTMLインタラクティブリプレイ、静的図、品質レポート
- **軌跡処理**: クリーニング→跳点識別→補間→平滑化→超速断線
- **推論機能**: 即時復活、英雄吊射、砦占領等
- **制約**: 秒級データのため制御ループ・衝突判断には不適

## BehaviorTree.CPPによる決定

### 採用チーム
- **PolarBear**: `pb_sentry_behavior_tree`（42 stars）
- **COD**: `cod_-rm2026_-behavior-tree`

### 特徴
- Groot2によるリアルタイムデバッグ
- 状態機より表現力が高い
- ROS2連携が容易

## 強化学習の応用

### 復旦大学 星雲EGA「天枢号」

- **強化学習輪脚ロボット** [RM2026-0202]
- Bilibili動画でデモンストレーション確認
- 具体的なアルゴリズム（PPO/SAC等）は不明
- 強化学習が実際の競技ロボットに適用された珍しい例

## 強化学習の応用

### 復旦大学 星雲EGA「天枢号」
- **強化学習轮脚ロボット** [RM2026-0202]
- Bilibili動画でデモンストレーション確認
- 具体的なアルゴリズム（PPO/SAC等）は不明
- 強化学習が実際の競技ロボットに適用された珍しい例

### 福州大学 浮舟湿地 - ROBOCON马术強化学習
- **ROBOCON马术赛道**での強化学習運動制御訓練を開源 [RM2026-0438]
- RoboMasterの姉妹大会ROBOCONでの強化学習応用
- GitHubでコード公開

## MPC・LQR・LESO制御

### 山东理工大学 齐奇 - 轮足MPC+LESO
- **MPC（Model Predictive Control）腿长制御** + **LESO動的擾動観測** [RM2026-0415]
- 極めて軽量化的な腿长モデリング
- マイコン展開時はLQRに変更可能
- 哈工程のモデリングを参考
- 154ダウンロード、26いいね

## 熱管理・功率制御

### 熱量制御（CODの実装例）

```
残熱 > 100: 19発/秒
100 → 40: 線形減速
40 → 30: 残熱 = 回復熱
最後に3発冗長（超発防止）
```

- 同済大学・中科技大学を参考
- 双発による裁判システムのダメージ吸収問題を回避

### 功率制御

- **西交リバプール大学**のモデルを参考（COD）
- **小陀螺時の功率管理**: 低速（充電）/高速（自瞄対策）

## 証拠ギャップ

- rm_visionの2026年シーズンでの実戦使用状況
- 強化学習の具体的なアルゴリズムと学習時間
- Sim2Realの性能差の定量的評価
- MPPIコントローラーと伝統的PIDの比較データ
- 各フレームワークの実際の採用チーム数

---

## ソース引用
- [RM2026-0202] 復旦大学星雲EGA轮脚
- [RM2026-0301] rm-battlescope
- [RM2026-0303] RMOSS
- [RM2026-0304] rm_vision
- [RM2026-0305] PolarBear Sim2Real
- [RM2026-0408] COD全開源
- [RM2026-0409] SHARKレーダー・同済フレームワーク
- [RM2026-0415] 山东理工大学齐奇MPC+LESO轮足制御
- [RM2026-0438] 福州大学浮舟湿地ROBOCON马术強化学習
- [RM2026-0202] 復旦大学星雲EGA輪脚
- [RM2026-0301] rm-battlescope
- [RM2026-0303] RMOSS
- [RM2026-0304] rm_vision
- [RM2026-0305] PolarBear Sim2Real
- [RM2026-0408] COD全開源
- [RM2026-0409] SHARKレーダー・同済フレームワーク
