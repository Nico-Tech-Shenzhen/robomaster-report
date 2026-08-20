# RoboMaster 2026 中国語圏調査: ソースマップ

## ソース間の関連図

```
【公式・データ】
RM2026-0001 (公式サイト) ─┬─→ RM2026-0101 (人民日報)
                         ├─→ RM2026-0102 (中国青年報)
                         ├─→ RM2026-0103 (華南農業大学)
                         ├─→ RM2026-0105 (華東理工大学)
                         └─→ RM2026-0002 (データセット)

RM2026-0002 (データセット) ──→ RM2026-0301 (rm-battlescope)

【大会結果・報道】
RM2026-0101 (人民日報) ─┬─→ RM2026-0103 (Taurus詳細)
                        ├─→ RM2026-0105 (起源詳細)
                        ├─→ RM2026-0203 (TDTインタビュー)
                        └─→ RM2026-0501 (大疆採用)

RM2026-0102 (中国青年報) ──→ RM2026-0203 (TDTインタビュー)
                          ──→ RM2026-0103 (Taurus VR操作)

【技術・チーム】
RM2026-0103 (Taurus) ─┬─→ 双七軸両腕 [robots-engineer.md]
                       ├─→ 輪脚歩兵
                       ├─→ VR操作
                       └─→ 産業応用

RM2026-0105 (起源) ─┬─→ 双輪足 [robots-sentry-radar.md]
                     ├─→ セントリー
                     └─→ 上海站戦績

RM2026-0201 (Navigator) ──→ レーダーRF [robots-sentry-radar.md]

RM2026-0202 (復旦EGA) ──→ 強化学習轮脚 [software-simulation.md]

【第二パス: シーズン終了後集中開源エコシステム】

【復旦大学 EGA - 全兵種制御+機械】
RM2026-0416 (SMC滑模制御) ─┬─→ 歩兵/英雄/哨兵/ドローン (全兵種)
                            ├─→ GitHub: xinruilee04/smc_controller
                            └─→ RM2026-0417 (過洞機械構造)

【深圳大学 RobotPilots - 視覚・ダーツ・セントリー】
RM2026-0418 (制導ダーツ) ─┬─→ 機械+ハードウェア+OpenMV
                           ├─→ RM2026-0419 (Odin1 SLAM)
                           ├─→ RM2026-0420 (YOLOv8-Pose能量機関)
                           └─→ RM2026-0421 (自瞄フレームワーク)
                           
RP-26AutoAim-Frame ─┬─→ プラグイン式アーキテクチャ
                     ├─→ RuneDetectionModel (能量機関)
                     └─→ 全兵種適用

【浙江大学 Hello World - エネルギー+ナビ+ハード】
RM2026-0422 (能量機関) ─┬─→ GitHub: IC-Alan/HWauto_buff2026
                          ├─→ RM2026-0423 (轮腿哨兵ナビ)
                          │   └─→ GitHub: Polyacetone/HWSentryNav26
                          ├─→ RM2026-0403/0406 (蛍光充能)
                          └─→ RM2026-0424 (ハードウェア)

【南京理工大学 Alliance - ダーツ+通信+制御】
RM2026-0426 (4Z軸調平) ─┬─→ GitHub: floatpigeon/4z-axis-chassis-leveling
                          ├─→ RM2026-0425 (FEC通信+自定义客户端)
                          │   ├─→ GitHub: floatpigeon/Meteor-Long-Exposure
                          │   └─→ GitHub: Alliance-Algorithm/Alliance-Client
                          └─→ RM2026-0427 (五自由度科技核心)
                          
RMCS (無下位機制御システム) ─┬─→ Linux+ROS2ベース
                            ├─→ Docker統一環境
                            └─→ 多板同一コード管理

【オープンソース・GitHub】
RM2026-0301 (rm-battlescope) ←── RM2026-0002 (データセット)

RM2026-0303 (RMOSS) ─┬─→ rmoss_gazebo (シミュレーション)
                      ├─→ rmoss_interfaces (ROS)
                      └─→ rmoss_contrib (自瞄等)

RM2026-0304 (rm_vision) ─┬─→ rm_auto_aim
                          ├─→ カメラドライバー群
                          └─→ rm_vision_simulator

RM2026-0305 (PolarBear) ─┬─→ pb2025_sentry_nav (ナビ)
                          ├─→ rmu_gazebo_simulator (シミュ)
                          ├─→ pb_sentry_behavior_tree (決定)
                          └─→ small_gicp_relocalization (定位)
                          
                          ↑ 参照
RM2026-0408 (COD) ─┬─→ PolarBearのナビツリー
                    ├─→ PolarBearの脱困プラグイン
                    ├─→ PolarBearのfake yaw
                    ├─→ FYT (自瞄ベース)
                    ├─→ 同済SuperPower (自瞄最適化・熱量)
                    ├─→ 中科技大学 (熱量)
                    └─→ 西交リバプール (功率)

【BBS技術開源】
RM2026-0402 (南風工程) ──→ エンジニアソフトウェア

RM2026-0403/0406 (浙大Hello World) ─┬─→ 蛍光充能
                                      └─→ スーパーキャパシタ・無線充電

RM2026-0404 (CUBOT) ──→ エンジニア+自定义控制器

RM2026-0405 (DreamChaser) ──→ FPGA制導ダーツ

RM2026-0408 (COD) ──→ セントリー全システム

RM2026-0409 (SHARK) ──→ レーダー融合識別

【新規: レーダー・無線電】
RM2026-0411 (WMJ雷达) ─┬─→ GitHub: zplszz/WMJRadar
                        ├─→ GNU Radio + 単SDR方案
                        ├─→ 南理工Combat開源を参照
                        └─→ 華南師範PIONEER開源を参照

【新規: 轮脚・脚型ロボット】
RM2026-0435 (HKUST ENTERPRIZE 串联腿) ─┬─→ 局均伤害Top 1
                                         ├─→ 12rad/s目標に近距離100%命中
                                         └─→ 上海交大串联腿を参考

RM2026-0414 (Born of Fire 偏置並列腿) ─┬─→ VMC解算
                                         ├─→ 卡腿検出・質心補償
                                         └─→ 最高命中率40%

RM2026-0415 (齐奇 MPC+LESO) ──→ 轮足制御
                                └─→ 哈工程モデリング参考

【新規: エンジニア・自定义控制器】
RM2026-0428 (SmartRobot 重力補償) ─┬─→ 三角基関数+Ridge+Huber
                                     ├─→ 広西大学開源を参照
                                     └─→ 左右個別擬合

RM2026-0432 (printk 自定义控制器) ─┬─→ 主従同構示教器
                                    ├─→ 総線サーボ/ステッピングモーター
                                    └─→ 吉林大学楊名揚開源を参照

【新規: 反無人機】
RM2026-0431 (Horizon レーザー追跡) ─┬─→ GitHub: BreCaspian/LaserTracking-2026
                                      ├─→ 30K+データセット
                                      ├─→ 螺旋探索戦略
                                      └─→ 20m追跡

【採用・産業】
RM2026-0501 (大疆採用) ←── RM2026-0101 (人民日報)
                        ←── RM2026-0103 (Taurus)
                        ←── 多数のチーム報道
```

## トピック別ソースマトリクス

### エンジニアロボット
| ソース | 双七軸両腕 | VR操作 | 輪脚 | 自定义控制器 | 重力補償 |
|--------|-----------|--------|------|------------|---------|
| RM2026-0101 | ○ | ○ | | | |
| RM2026-0102 | ○ | ○ | | | |
| RM2026-0103 | ● | ● | ○ | | |
| RM2026-0402 | | | | | |
| RM2026-0403 | | | | | |
| RM2026-0404 | ○ | | | ○ | |
| RM2026-0428 | | | | ○ | ● |
| RM2026-0432 | | | | ● | ○ |

### 轮脚・脚型ロボット
| ソース | 串联腿 | 偏置並列腿 | 双輪足 | 轮腿 | MPC | VMC | 強化学習 |
|--------|--------|-----------|--------|------|-----|-----|---------|
| RM2026-0202 | | | | ● | | | ● |
| RM2026-0305 | | | | | | | |
| RM2026-0423 | | | | ● | | | |
| RM2026-0435 | ● | | | | | | |
| RM2026-0414 | | ● | | | | ● | |
| RM2026-0415 | | | | | ● | | |

### セントリー・ナビゲーション
| ソース | 四軸ジンバル | 轮腿 | ROS2/Nav2 | Sim2Real | BehaviorTree | SLAM (Odin1) |
|--------|-------------|------|-----------|----------|-------------|-------------|
| RM2026-0101 | ○ | | | | | |
| RM2026-0102 | ○ | | | | | |
| RM2026-0105 | | ● | | | | |
| RM2026-0305 | | | ● | ● | ● | |
| RM2026-0408 | | | ● | ○ | ● | |
| RM2026-0419 | | | | | | ● |
| RM2026-0423 | | ● | | | | |

### レーダー
| ソース | SDR | RF設計 | 視覚融合 | 無線電 | 多モーダル | GNU Radio |
|--------|-----|--------|---------|--------|-----------|-----------|
| RM2026-0201 | ● | ● | | | | |
| RM2026-0409 | | | ● | ● | ● | |
| RM2026-0411 | ● | | | ● | | ● |

### ダーツ
| ソース | FPGA | 300FPS | 構造設計 | 制導 | 4Z軸調平 | 皮筋系 |
|--------|------|--------|---------|------|---------|--------|
| RM2026-0405 | ● | ● | ● | ● | | |
| RM2026-0418 | | | ● | ● | | |
| RM2026-0426 | | | | | ● | |
| RM2026-0433 | | | | | | ● |

### ビジョン・自瞄
| ソース | YOLOv8 | 能量機関 | 自瞄フレームワーク | 滑模制御 | 反無人機 | 插件式 |
|--------|--------|---------|-------------------|---------|---------|--------|
| RM2026-0420 | ● | ● | | | | |
| RM2026-0421 | | | ● | | | ● |
| RM2026-0422 | | ● | | | | |
| RM2026-0416 | | | | ● | | |
| RM2026-0431 | | | | | ● | |

### ソフトウェア・シミュレーション
| ソース | ROS2 | Gazebo | Nav2 | 自瞄 | 強化学習 | FEC |
|--------|------|--------|------|------|---------|-----|
| RM2026-0202 | | | | | ● | |
| RM2026-0301 | | | | | | |
| RM2026-0303 | ● | ● | | | | |
| RM2026-0304 | ● | | | ● | | |
| RM2026-0305 | ● | ● | ● | | | |
| RM2026-0408 | ● | ○ | ● | ● | | |
| RM2026-0409 | | | | ● | | |
| RM2026-0425 | ● | | | | | ● |
| RM2026-0438 | | | | | ● | |

## チーム別ソース関連

### 東北大学 TDT
- RM2026-0101, RM2026-0102, RM2026-0104, RM2026-0203

### 華南農業大学 Taurus
- RM2026-0101, RM2026-0102, RM2026-0103

### 華東理工大学 起源
- RM2026-0101, RM2026-0105

### 同済大学 SuperPower
- RM2026-0101, RM2026-0102

### 浙江大学 Hello World
- RM2026-0403, RM2026-0406, RM2026-0422, RM2026-0423, RM2026-0424

### 深北莫 PolarBear
- RM2026-0305

### 遼寧科技大学 COD
- RM2026-0408

### 江南大学 SHARK
- RM2026-0302, RM2026-0409

### 復旦大学 星雲EGA
- RM2026-0202, RM2026-0416, RM2026-0417

### 香港浸会大学 Navigator
- RM2026-0201

### 北京理工大学 DreamChaser
- RM2026-0405

### 中国鉱業大学 CUBOT
- RM2026-0404, RM2026-0439

### 深圳大学 RobotPilots
- RM2026-0418, RM2026-0419, RM2026-0420, RM2026-0421

### 南京理工大学 Alliance
- RM2026-0425, RM2026-0426, RM2026-0427

### 香港科技大学 ENTERPRIZE
- RM2026-0435

### 南航金城学院 Born of Fire
- RM2026-0414

### 西北工业大学 WMJ
- RM2026-0411

### 华北理工大学 Horizon
- RM2026-0431

### 山东科技大学 SmartRobot
- RM2026-0428

### 贵州大学 printk
- RM2026-0432

### 五邑大学 IMCA
- RM2026-0433

### 西安科技大学 秦风
- RM2026-0430

### 山东理工大学 齐奇
- RM2026-0415

### 福州大学 浮舟湿地
- RM2026-0438

### 东北大学 TDT（追加）
- RM2026-0449: 2025雷达开源（T-DT_Radar）

### 武汉科技大学 WUST-RM
- RM2026-0450: awakening — 中国RMエコシステム関係図

### 华南农业大学 Taurus（追加）
- RM2026-0451: SCAU-RM-NAV GitHub組織（哨兵ナビ+五摩擦轮英雄）

### 华东理工大学 起源（追加）
- RM2026-0452: 2024自定义控制器+2026串联腿英雄+校内赛裁判系统

### 上海交通大学 交龙
- RM2026-0453: GitHub 29リポジトリ、無線充電、技術ブログ

### 中国石油大学（华东）RPS
- RM2026-0454: 雷达+串联腿步兵+P17轮毂减速器

### 华北理工大学 Horizon（追加）
- RM2026-0455: LiDAR+工業カメラ視覚融合雷达站

### 西安交通大学 笃行
- RM2026-0456: 飞镖系统开源 (RM2025)
- RM2026-0457: 关节电容和控制器开源 (RM2026)
- RM2026-0458: 视觉组知识库 (Obsidian/GitHub)

### 哈尔滨工业大学（深圳） 南工骁鹰
- RM2026-0459: 雷达站点云定位模块开源 (500Hz+)

### 电子科技大学中山学院 RoboBraver
- RM2026-0460: 柳幸之 MPC+LQR+PSO+KNN 技术报告

### 天津大学 北洋机甲
- RM2026-0461: OpenRM-2024 视觉算法库
- RM2026-0462: TJURM-2024 自瞄框架

### 哈尔滨工业大学 I Hiter
- RM2026-0463: 哨兵导航开源 (ROS1 Noetic)

### 华中科技大学 狼牙
- RM2026-0464: 管理成果报告 (RM AWARD 2024)

### 华南理工大学 华南虎
- RM2026-0465: SimulatorX 模拟器开源

### 青岛大学 未来
- RM2026-0466: 低成本3508减速箱开源
- RM2026-0467: 视觉AI+哨兵导航开源

### 广州城市理工学院 野狼
- RM2026-0468: 飞镖系统开源 (RM2025)

### 合肥工业大学（宣城校区） WDR
- RM2026-0469: COT硬件内环超级电容开源

### 西安电子科技大学 IRobot
- RM2026-0470: 嵌入式软件中间件开源

### 中南大学 FYT
- RM2026-0471: 2026工程机器人机械结构开源

---

## 【第三パス: 从赛场到课堂 — 教育展示パネル調査】

### 东北大学 TDT + 教育体系
- RM2026-0472: 《机器人创新设计》选修课程 (C3000000119) — neu.edu.cn 公式課程目録
  - Instructor: 丛德宏 (ACTION team founder, ABU Robocon advisor)
  - ⚠️ Course does NOT explicitly mention RoboMaster; instructor linked to ACTION not TDT
- ←── RM2026-0203 (TDT interview), RM2026-0441 (TDT sentry), RM2026-0449 (TDT radar)
- Exhibition panel: IMG_20260808_164237.jpg

### 哈工大(深圳) 南工骁鹰 + 教育体系
- RM2026-0473: 官方校報複数記事 (hitsz.edu.cn 2018-2025)
  - Team: founded 2016, ~80 members, under 实验与创新实践教育中心
  - 54 provincial+ awards confirmed
  - ICRA 2018 global runner-up confirmed
- ←── RM2026-0459: 雷达站点云定位模块开源
- Exhibition panel: IMG_20260808_164255.jpg

### 吉林大学 吉甲大师 + 教育体系
- RM2026-0474: 吉甲大师双创基地 — 校党委书记公式訪問＋基金ページ
  - Fund target: 1 million RMB
  - Team TARS-GO founded 2018, first entry top 16
  - Cross-disciplinary platform with science outreach
- Exhibition panel: IMG_20260808_164253.jpg

### 北京科技大学 Reborn + 教育体系
- RM2026-0475: Reborn team (2018, 30+ members) + 学生创新创业基地
  - Innovation credits ≥2 REQUIRED for all undergraduates
  - 8 innovation labs, ~2000 sqm, 1500+ students/year
- Exhibition panel: IMG_20260805_124052.jpg

### 东莞理工学院 — 完全検証コース
- RM2026-0476: 《机器人应用开发实践》3.5学分・56学时
  - ✅ 课程名称・学分・学时 = 展示パネルと完全一致
  - Computer Science and Technology program, 学科交叉融合课程
  - STRONGEST verified case: exact credit/hour match to exhibition panel
- Exhibition panel: IMG_20260808_164259.jpg


### 哈工程 创梦之翼 + 教育体系
- RM2026-0477: 公式校報・教育モデル詳細 (hrbeu.edu.cn 2022-06-29)
  - Four-level progressive system: 校内赛→联盟赛→超级对抗赛→AI挑战赛
  - Multi-dimensional platform: 课程实验-企业实践-科技创新-科研训练
  - 6 innovation courses, 8000+ person-hours, 80%+ graduate school rate
  - Supports robot engineering + AI new engineering majors
- Exhibition panel: IMG_20260805_124057.jpg

### 华南理工大学 华南虎 + 教育体系
- RM2026-0478: 公式実験教学センター (scut.edu.cn 2018-12-30)
  - 2017, 2018 RoboMaster championships confirmed
  - Guided by Experimental Teaching Center teacher 张东
  - Industry collaborations: Microchip, PTC, UG
- ←── RM2026-0465: SimulatorX 模拟器开源
- Exhibition panel: IMG_20260805_124119.jpg

### 深圳大学 RobotPilots + 教育体系
- RM2026-0479: ICRA 2018 DJI AI Challenge 季军 + 公式校報 (szu.edu.cn 2018-05-28)
  - Supported by university "国际化行动计划"
  - K-12 collaboration with Shenzhen Middle School (空间智能创新实验室)
- ←── RM2026-0411, RM2026-0418-0421: 2026 season open source
- Exhibition panel: IMG_20260805_124111.jpg

---

*本マップは調査過程で収集されたソース間の関係性を示すものであり、網羅的ではない。*
*最終更新: 2026-08-20*
*総ソース数: 79*
*从赛场到课堂調査新規追加: 8ソース (0472-0479)*
