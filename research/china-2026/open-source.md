# RoboMaster 2026: オープンソースエコシステム

## 概要

RoboMaster 2026シーズンは、**過去最大規模のオープンソース活動**が見られた。公式のデータセット公開に加え、多数のチームが機械構造、電気回路、ソフトウェアコード、技術報告書をBBSやGitHub/Giteeで公開した。特に**セントリーのナビゲーション・決定・自瞄**を統合した全システム開源や、**FPGA制導ダーツ**の全棧開源など、高度な技術の公開が進んだ。

## 公式データ公開

### RMUC 2026区域赛部分赛事データ
- **公開日**: 2026年7月17日 [RM2026-0002]
- **形式**: SQLiteデータベース（113.42MB圧縮）
- **内容**: matches, timeseries, eventsの3テーブル
- **用途**: 戦略訓練用（ルール効力・競技賞の参考ではない）
- **コミュニティツール**: rm-battlescope [RM2026-0301]

## コミュニティ・データツール

### rm-battlescope（ezthor）
- **GitHub**: https://github.com/ezthor/rm-battlescope
- **機能**: 赛事データ解析、戦術リプレイ、攻撃関係推論、HTMLインタラクティブリプレイ
- **ライセンス**: MIT
- **対象**: RMUC 2026区域赛SQLiteデータセット

### RMUC2026-Registration-Dashboard（江南大学SHARK）
- **GitHub**: https://github.com/JNU-SHARK/RMUC2026-Registration-Dashboard
- **機能**: 区域赛志愿選択の分析・可視化、晋级確率シミュレーション
- **ライセンス**: CC BY-NC-SA 4.0

## エコシステム基盤

### RoboMaster OSS (RMOSS)
- **GitHub**: https://github.com/robomaster-oss
- **内容**: Gazeboシミュレーション、ROS2インターフェース、カメラドライバー等
- **主要リポジトリ**:
  - rmoss_gazebo: Gazeboプラグインとロボットモデル
  - rmoss_interfaces: ROSメッセージ・サービス定義
  - rmoss_core: カメラモジュール、弾道運動モジュール等
  - rmoss_contrib: 自動瞄准モジュール、エネルギー機関モジュール
- **ライセンス**: Apache-2.0 / MIT

### rm_vision（華南農業大学SCAU-RM-NAV）
- **GitHub**: https://github.com/SCAU-RM-NAV/rm_vision
- **内容**: RoboMaster視覚ROS2フレームワーク
- **含まれるプロジェクト**:
  - rm_auto_aim: 装甲板自動瞄准
  - ros2_mindvision_camera: MindVisionカメラモジュール
  - ros2_hik_camera: HikVisionカメラモジュール
  - rm_gimbal_description: ジンバルURDF
  - rm_serial_driver: 串口通信
  - rm_vision_simulator: 視覚アルゴリズムシミュレーター
- **Docker対応**: `chenjunnn/rm_vision:lastest`

## チーム別開源一覧

### ナビゲーション・セントリー

| チーム | 大学 | 内容 | プラットフォーム |
|--------|------|------|----------------|
| PolarBear | 深北莫 | Sim2Realナビゲーション、整車TF、BehaviorTree、Gazeboシミュ | GitHub |
| COD | 遼寧科技大 | ナビゲーション+決定+自瞄+下位機（ROS2/Nav2/MPPI） | Gitee |
| 起源 | 華東理工大 | レーダー辅助吊射、アルゴリズムフレームワーク | BBS |

### 自瞄・視覚

| チーム | 大学 | 内容 | プラットフォーム |
|--------|------|------|----------------|
| RobotPilots | 深圳大学 | RP-26AutoAim-Frame | GitHub |
| 奇点 | 仲恺農業工程 | 自瞄改良（FYTベース+交龍移植） | GitHub |
| SuperPower | 同済大学 | 自瞄アルゴリズム（25年開源、多くのチームが参考） | BBS |

### ダーツ

| チーム | 大学 | 内容 | 備考 |
|--------|------|------|------|
| DreamChaser | 北京理工大学 | FPGA制導ダーツ（300FPS）全棧開源 | Altium + コード |
| 斉奇 | 山東理工大学 | ダーツ構造開源 | 図面+技術文書 |

### エンジニア・ハードウェア

| チーム | 大学 | 内容 | 備考 |
|--------|------|------|------|
| Hello World | 浙江大学 | 蛍光充能装置 | 単套装40元以下、GitHub |
| Hello World | 浙江大学 | スーパーキャパシタ&無線充電 | BBS |
| CUBOT | 中国鉱業大学 | エンジニア+自定义控制器 | 百度网盘 |
| 南風 | 広州南方学院 | エンジニアソフトウェア | 1分20秒2級鉱石 |

### 機械構造

| チーム | 大学 | 内容 | 備考 |
|--------|------|------|------|
| Artisans | 安徽信息工程学院 | 隧道英雄機械構造 | STEP形式、229MB |

### レーダー

| チーム | 大学 | 内容 | 備考 |
|--------|------|------|------|
| SHARK | 江南大学 | 無線電+視覚融合識別 | 局均易傷1927.2s |
| Navigator | 香港浸会大学 | RF開発記録 | PlutoSDR、フィルター設計 |

## ライセンス分布

| ライセンス | 採用例 |
|-----------|--------|
| MIT | rm-battlescope、南風工程コード |
| Apache-2.0 | PolarBearリポジトリ群、RMOSS |
| CC BY-NC-SA 4.0 | SHARK Dashboard、浙江大学蛍光充能 |
| CC BY-NC-ND 4.0 | 中国鉱業大学CUBOT |
| 明示なし | 多数のBBS開源（慣行に従う） |

## 開源エコシステムの特徴

1. **階層的な引用構造**: 多くのチームが他チームの開源をベースに改良
   - 例：COD → PolarBear（ナビ）+ FYT（自瞄）+ 同済（熱量）+ 西交（功率）
   - 例：奇点 → FYT（ベース）+ 交龍（solver）+ 同済（EKF）

2. **ROS2の普及**: セントリー・ナビゲーションでROS2/Nav2が標準化しつつある

3. **GitHub + Giteeの併用**: 国内チームはGiteeを、国際的な公開はGitHubを使用

4. **BBSが中心の情報発信**: 技術ブログ・開源の主なプラットフォームはRoboMaster BBS

5. **「救命开源」文化**: 公式が「硬件救命开源」「电控救命开源」等を整理して紹介

## 証拠ギャップ

- 各開源の実際のダウンロード数・使用状況
- 開源からの技術的フィードバックループ
- 公式の開源奨励制度の詳細
- RM AWARDの開源賞の審査基準と2026年受賞者
- Giteeリポジトリの詳細な内容（アクセス制限あり）

---

## ソース引用
- [RM2026-0002] 区域赛データセット公開
- [RM2026-0201] NavigatorレーダーRF開発
- [RM2026-0301] rm-battlescope
- [RM2026-0302] Registration-Dashboard
- [RM2026-0303] RMOSS
- [RM2026-0304] rm_vision
- [RM2026-0305] PolarBear Sim2Real
- [RM2026-0401] Artisans機械構造開源
- [RM2026-0402] 南風工程コード開源
- [RM2026-0403] Hello World蛍光充能
- [RM2026-0404] CUBOTエンジニア開源
- [RM2026-0405] DreamChaser FPGAダーツ
- [RM2026-0406] Hello World蛍光充能
- [RM2026-0408] COD全開源
- [RM2026-0409] SHARKレーダー開源
