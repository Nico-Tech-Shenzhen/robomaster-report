# RoboMaster 2026 中国語圏調査コーパス INDEX

## 調査方針
- 既存レポートの編集・書き換えは行わない
- 新たな中国語圏エビデンスの発見と収集を目的とする
- 主に2026年シーズン中・シーズン終了後に公開された一次資料を優先する

## ディレクトリ構造
```
research/china-2026/
├── INDEX.md              # 本ファイル
├── source-map.md         # ソース間の関連マップ
├── sources/              # 個別ソースカード
│   └── RM2026-NNNN.md
├── rules-and-results.md  # ルールと大会結果
├── robots-engineer.md    # エンジニアロボット
├── robots-sentry-radar.md # セントリー・レーダー
├── vision-autoaim.md     # ビジョン・オートエイム
├── dart-air.md           # ダーツ・空中ロボット
├── software-simulation.md # ソフトウェア・シミュレーション
├── open-source.md        # オープンソース
├── team-operation.md     # チーム運営
├── recruitment-industry.md # 採用・産業連携
├── universities-policy.md # 大学・制度支援
├── claims-audit.md       # クレーム検証レポート
├── evidence-clusters.md  # エビデンスクラスタ
├── from-arena-to-classroom.md # 教育展示パネル調査
├── award-priority-table.md # AWARD nominee優先度表
└── CODEX-HANDOFF.md      # Codex引き継ぎドキュメント
```

## 収集済みソース一覧

### 公式・一次資料
| ID | タイトル | ソース | 日付 | 信頼性 |
|----|---------|--------|------|--------|
| RM2026-0001 | RoboMaster 2026 全国总决赛直播・赛程赛果 | robomaster.com | 2026-08 | official_primary |
| RM2026-0002 | RMUC 2026 区域赛部分赛事数据发布 | BBS | 2026-07-17 | official_primary |
| RM2026-0003 | 🎯 RMUC 2026 完整形态考核指南 | BBS | 2026-03-11 | official_primary |
| RM2026-0004 | RMUC 2026规则讨论&意见征集 | BBS | 2026-05-11 | official_primary |

### メディア報道
| ID | タイトル | ソース | 日付 | 信頼性 |
|----|---------|--------|------|--------|
| RM2026-0101 | 一项机器人赛事，走出20万青年工程师 | 人民日报 | 2026-08-10 | media_secondary (S級) |
| RM2026-0102 | RoboMaster 2026机甲大师赛收官 | 中国青年报/新浪 | 2026-08-10 | media_secondary |
| RM2026-0103 | 华农学子斩获2026年全国亚军 | 华南农业大学官网 | 2026-08-11 | university_primary |
| RM2026-0104 | 东北大学勇夺北部赛区冠军 | 中国日报 | 2026-06-03 | media_secondary |
| RM2026-0105 | 华东理工大学ORIGIN起源战队获季军 | 华东理工大学官网 | 2026-08-13 | university_primary |

### チーム・技術資料
| ID | タイトル | ソース | 日付 | 信頼性 |
|----|---------|--------|------|--------|
| RM2026-0201 | Navigator RMUC 2026雷达射频开发小记 | BBS | 2026-04-28 | technical_secondary |
| RM2026-0202 | 天枢号「强化学习」轮腿机器人｜复旦大学星云EGA | Bilibili | 2026-06-30 | team_primary |
| RM2026-0203 | 东北大学TDT战队队长インタビュー | 中国青年报 | 2026-08-10 | team_primary |
| RM2026-0204 | 河北大学直隶机甲战队华北站佳绩 | 校官网 | 2026-05-27 | team_primary |

### オープンソース・GitHub/Gitee
| ID | タイトル | ソース | 日付 | 信頼性 |
|----|---------|--------|------|--------|
| RM2026-0301 | rm-battlescope: RMUC 2026 赛事数据解析ツール | GitHub | 2026-07-19 | repository_primary |
| RM2026-0302 | RMUC2026-Registration-Dashboard | GitHub | 2026-04-13 | repository_primary |
| RM2026-0303 | RoboMaster OSS (RMOSS) | GitHub | 2026-01-28 | repository_primary |
| RM2026-0304 | rm_vision: RoboMaster 视觉ROS2 框架 | GitHub | 2023-06-11 | repository_primary |
| RM2026-0305 | 深北莫PolarBear Sim2Realナビゲーション開源 | GitHub/BBS | 2025-04-13 | team_primary |

### BBS技術開源（第一パス）
| ID | タイトル | ソース | 日付 | 信頼性 |
|----|---------|--------|------|--------|
| RM2026-0401 | 安徽信息工程学院Artisans-隧道英雄机械结构开源 | BBS | 2026-03-17 | team_primary |
| RM2026-0402 | 2026RM工程挑战赛（华南站）软件代码开源 | BBS | 2026-03-20 | team_primary |
| RM2026-0403 | 浙江大学Hello World-自制荧光充能开源 | BBS | 2026-08-02 | team_primary |
| RM2026-0404 | 中国矿业大学CUBOT-工程机器人和自定义控制器开源 | BBS | 2026-05-28 | team_primary |
| RM2026-0405 | 北京理工大学DreamChaser-FPGA制导飞镖开源 | BBS | 2026-08-18 | team_primary |
| RM2026-0406 | 浙江大学Hello World-自制荧光充能开源 | BBS/GitHub | 2026-08-02 | team_primary |
| RM2026-0408 | 遼寧科技大学COD-哨兵导航决策自瞄全开源 | BBS/Gitee | 2026-03-31 | team_primary |
| RM2026-0409 | 江南大学SHARK-雷达站无线电+视觉融合识别系统开源 | BBS | 2026-08- | team_primary |

### BBS技術開源（第二パス・シーズン終了後集中開源）
| ID | タイトル | ソース | 日付 | 信頼性 |
|----|---------|--------|------|--------|
| RM2026-0410 | 厦门大学嘉庚学院TCR-雷达地面视觉、无线电与无人机反制开源 | BBS | 2026-08 | team_primary |
| RM2026-0411 | 西北工业大学WMJ-雷达开源（局均186.4s反制+单SDR） | BBS/GitHub | 2026-08-09 | team_primary |
| RM2026-0412 | 河北科技大学Actor&Thinker-视觉算法仿真器Daedalus开源 | BBS/GitHub | 2026-06-09 | team_primary |
| RM2026-0413 | 香港科技大学ENTERPRIZE-RM26串联腿步兵开源 | BBS | 2026-08 | team_primary |
| RM2026-0414 | 南航金城学院Born of Fire-偏置并联腿整车电控开源 | BBS | 2026-06-03 | team_primary |
| RM2026-0415 | 山东理工大学齐奇-轮足机器人MPC+LESO控制开源 | BBS | 2026-08-09 | team_primary |
| RM2026-0416 | 复旦大学EGA-云台滑模控制器教学&开源（2026版） | BBS/GitHub | 2026-08-17 | team_primary |
| RM2026-0417 | 复旦大学EGA-过洞步兵&哨兵机械结构开源 | BBS | 2026-08-16 | team_primary |
| RM2026-0418 | 深圳大学RobotPilots-制导飞镖开源 | BBS | 2026-08-15 | team_primary |
| RM2026-0419 | 深圳大学RobotPilots-Odin1空间记忆模组方案 | BBS | 2026-08-16 | team_primary |
| RM2026-0420 | 深圳大学RobotPilots-YOLOv8-Pose能量机关五点识别 | BBS/GitHub | 2026-08-14 | team_primary |
| RM2026-0421 | 深圳大学RobotPilots-自瞄算法框架开源 | GitHub | 2026-08-14 | team_primary |
| RM2026-0422 | 浙江大学Hello World-能量机关算法开源 | BBS/GitHub | 2026-08-09 | team_primary |
| RM2026-0423 | 浙江大学Hello World-轮腿哨兵导航算法开源 | GitHub | 2026-08-09 | team_primary |
| RM2026-0424 | 浙江大学Hello World-个人硬件项目开源 | BBS | 2026-08-09 | team_primary |
| RM2026-0425 | 南京理工大学Alliance-FEC前向纠错通信与自定义客户端 | GitHub | 2026年シーズン | team_primary |
| RM2026-0426 | 南京理工大学Alliance-镖架4Z轴底座自动调平算法 | BBS/GitHub | 2026-08-13 | team_primary |
| RM2026-0427 | 南京理工大学Alliance-五自由度科技核心机械开源 | BBS | 2026-08-15 | team_primary |
| RM2026-0428 | 山东科技大学SmartRobot-自定义控制器重力补偿开源 | BBS/GitHub | 2026-08-11 | team_primary |
| RM2026-0429 | 北京信息科技大学星辰-大弹丸偏置式中心供弹模块 | BBS | 2026-08-17 | team_primary |
| RM2026-0430 | 西安科技大学秦风-三摩擦英雄机器人机械设计开源 | BBS | 2026-08-16 | team_primary |
| RM2026-0431 | 华北理工大学Horizon-反无人机激光追踪方案 | BBS/GitHub | 2026-04-05 | team_primary |
| RM2026-0432 | 贵州大学printk-工程自定义控制器结构和代码开源 | BBS | 2026-04-04 | team_primary |
| RM2026-0433 | 五邑大学IMCA-RM2025皮筋类飞镖系统技术开源 | BBS | 2025-09-29 | team_primary |
| RM2026-0438 | 福州大学浮舟湿地-ROBOCON马术强化学习运控开源 | BBS/GitHub | 2026-08-09 | team_primary |
| RM2026-0439 | 中国矿业大学CUBOT-RM AWARD 2025工程与轮腿技术报告 | BBS | 2025年 | team_primary |

### 採用・産業連携
| ID | タイトル | ソース | 日付 | 信頼性 |
|----|---------|--------|------|--------|
| RM2026-0501 | RoboMaster 专属招聘通道（大疆DJI） | robomaster.com | 継続的 | official_primary |

### Bilibili技術動画（第二パス）
| ID | タイトル | ソース | 日付 | 信頼性 |
|----|---------|--------|------|--------|
| RM2026-0440 | 全国赛第96场 Taurus vs TDT 冠军争夺战 | Bilibili公式 | 2026-08-09 | official_primary |
| RM2026-0441 | 四轴云台越隧哨兵｜东北大学 TDT 战队 | Bilibili公式 | 2026-08-09 | official_primary |
| RM2026-0442 | 双七轴仿人形机械臂｜华南农业大学 工程机器人 | Bilibili公式 | 2026-08-09 | official_primary |
| RM2026-0443 | 「轮圈腿构型」步兵机器人！｜东北大学 TDT战队 | Bilibili公式 | 2026-08-09 | official_primary |
| RM2026-0444 | VR链路带来新突破！｜华南农业大学 工程机器人 | Bilibili公式 | 2026-08-09 | official_primary |
| RM2026-0445 | 载入历史的对局！｜全国赛第93场 Taurus vs 起源 | Bilibili公式 | 2026-08-09 | official_primary |
| RM2026-0446 | 低姿越隧串联腿｜华东理工大学 步兵机器人 | Bilibili公式 | 2026-08-09 | official_primary |
| RM2026-0447 | 夜空的RM2026赛季总结【一小时剧场版】 | Bilibiliファン制作 | 2026年 | media_secondary |
| RM2026-0448 | RoboMaster 2026 赛季启动｜规则改动宣讲会 | Bilibili公式 | 2025-10-21 | official_primary |

### GitHub/Giteeチーム別検索（第二パス追加）
| ID | タイトル | ソース | 日付 | 信頼性 |
|----|---------|--------|------|--------|
| RM2026-0449 | 东北大学TDT战队 2025雷达开源 (T-DT_Radar) | GitHub/BBS | 2025年 | team_primary |
| RM2026-0450 | 武汉科技大学 WUST-RM/awakening — 中国RMエコシステム関係図 | GitHub | 2026年 | team_primary |
| RM2026-0451 | 华南农业大学Taurus战队 GitHub組織開源 (SCAU-RM-NAV) | GitHub/BBS | 2023-2025 | team_primary |
| RM2026-0452 | 华东理工大学ORIGIN起源战队 2024-2026開源まとめ | GitHub/BBS | 2024-2026 | team_primary |
| RM2026-0453 | 上海交通大学交龙战队 GitHub開源 (SJTU-RoboMaster-Team) | GitHub | 2026-08 | team_primary |
| RM2026-0454 | 中国石油大学（华东）RPS战队 GitHub開源 (RoboPioneers) | GitHub/BBS | 2023-2026 | team_primary |
| RM2026-0455 | 华北理工大学Horizon战队 激光雷达雷达站開源 | GitHub | 2025年 | team_primary |

### AWARD 2026 提名奖関連発見
| ID | タイトル | ソース | 日付 | 信頼性 |
|----|---------|--------|------|--------|
| RM2026-0456 | 西安交通大学笃行战队 飞镖系统开源 (RM2025) | BBS | 2025-08-25 | team_primary |
| RM2026-0457 | 西安交通大学笃行战队 关节电容和控制器开源 (RM2026) | BBS | 2026年 | team_primary |
| RM2026-0458 | 西安交通大学笃行战队 视觉组知识库 (Obsidian/GitHub) | GitHub | 2023-08 | team_primary |
| RM2026-0459 | 哈工大（深圳）南工骁鹰战队 雷达站点云定位模块开源 | BBS | 2024年 | team_primary |
| RM2026-0460 | 电子科大中山学院RoboBraver 柳幸之 平衡步兵+空中机器人技术报告 | BBS | 2024-09-01 | team_primary |
| RM2026-0461 | 天津大学北洋机甲战队 OpenRM-2024 视觉算法库 | GitHub | 2024-08 | team_primary |
| RM2026-0462 | 天津大学北洋机甲战队 TJURM-2024 自瞄框架 | GitHub | 2024-08 | team_primary |
| RM2026-0463 | 哈工大I Hiter战队 哨兵导航开源 (ROS1 Noetic) | GitHub | 2025-09 | team_primary |
| RM2026-0464 | 华中科技大学狼牙战队 管理成果报告 (RM AWARD 2024) | BBS | 2024-09-03 | team_primary |
| RM2026-0465 | 华南理工大学华南虎战队 SimulatorX 模拟器开源 (RM2022) | BBS | 2022-10-08 | team_primary |
| RM2026-0466 | 青岛大学未来战队 低成本3508减速箱开源 (RM2026) | BBS | 2025-04-30 | team_primary |
| RM2026-0467 | 青岛大学未来战队 视觉AI+哨兵导航开源 | GitHub/BBS | 2023-2025 | team_primary |
| RM2026-0468 | 广州城市理工学院野狼战队 飞镖系统开源 (RM2025) | BBS | 2025-09-28 | team_primary |
| RM2026-0469 | 合肥工业大学WDR战队 COT硬件内环超级电容开源 (RM2026) | BBS | 2026-03-22 | team_primary |
| RM2026-0470 | 西安电子科技大学IRobot战队 嵌入式软件中间件开源 (RM2026) | BBS | 2026年 | team_primary |
| RM2026-0471 | 中南大学FYT战队 2026工程机器人机械结构开源 | BBS | 2026年 | team_primary |

### 从赛场到课堂 — 教育展示パネル調査
| ID | タイトル | ソース | 日付 | 信頼性 |
|----|---------|--------|------|--------|
| RM2026-0472 | 东北大学《机器人创新设计》课程（C3000000119） | neu.edu.cn 课程目录PDF | 2024-2025 | university_primary |
| RM2026-0473 | 哈工大(深圳) 南工骁鹰战队 — 官方校報複数記事 | hitsz.edu.cn | 2018-2025 | university_primary |
| RM2026-0474 | 吉林大学 吉甲大师双创基地 — 校党委書記調査＋基金 | jlu.edu.cn | 2020-2026 | university_primary |
| RM2026-0475 | 北京科技大学 Reborn战队＋创新创业基地 — 公式文書 | ustb.edu.cn PDF | 2021-2022 | university_primary |
| RM2026-0476 | 东莞理工学院《机器人应用开发实践》— 公式課程大綱 | cs.dgut.edu.cn | 2024-03 | university_primary |
| RM2026-0477 | 哈工程创梦之翼 — 公式校報・教育モデル詳細 | hrbeu.edu.cn | 2022-06 | university_primary |
| RM2026-0478 | 华南理工大学华南虎 — 公式実験教学センター | scut.edu.cn | 2018-12 | university_primary |
| RM2026-0479 | 深圳大学RobotPilots — ICRA 2018＋公式校報 | szu.edu.cn | 2018-05 | university_primary |

## 統計サマリー

| カテゴリ | ソース数 |
|---------|---------|
| 公式・一次資料 | 4 |
| メディア報道 | 5 |
| チーム・技術資料 | 4 |
| オープンソース・GitHub/Gitee | 5 |
| BBS技術開源（第一パス） | 8 |
| BBS技術開源（第二パス） | 27 |
| Bilibili技術動画 | 9 |
| GitHub/Giteeチーム別検索（第二パス追加） | 7 |
| AWARD 2026 提名奖関連発見 | 16 |
| 从赛场到课堂 教育調査 | 8 |
| 採用・産業連携 | 1 |
| **合計** | **79** |

## チーム別ソース数ランキング

| チーム | 大学 | ソース数 |
|--------|------|---------|
| Taurus | 华南农业大学 | 6 |
| TDT | 东北大学 | 6 |
| Hello World | 浙江大学 | 5 |
| RobotPilots | 深圳大学 | 5 |
| EGA / 星云EGA | 复旦大学 | 4 |
| Alliance | 南京理工大学 | 4 |
| 笃行 | 西安交通大学 | 3 |
| 起源 | 华东理工大学 | 3 |
| 未来 | 青岛大学 | 3 |
| 南工骁鹰 | 哈工大(深圳) | 2 |
| 华南虎 | 华南理工大学 | 1 |
| 北洋机甲 | 天津大学 | 2 |
| 星辰 | 北京信息科技大学 | 2 |
| Horizon | 华北理工大学 | 2 |
| CUBOT | 中国矿业大学 | 2 |
| 其他（各1ソース） | — | 35チーム |

## 大会結果サマリー

### 全国総決勝（2026年8月9日、深圳）
| 順位 | チーム | 大学 | 備考 |
|------|--------|------|------|
| 優勝 | TDT | 東北大学 | 北部赛区チャンピオン |
| 準優勝 | Taurus | 華南農業大学 | 南部赛区チャンピオン、過去最高成績 |
| 3位 | 起源 | 華東理工大学 | 全国大会初進出→3位 |
| 4位 | SuperPower | 同済大学 | 上海站季軍 |

### 区域赛チャンピオン
| 赛区 | 優勝チーム | 大学 |
|------|-----------|------|
| 北部赛区 | TDT | 東北大学 |
| 南部赛区 | Taurus | 華南農業大学 |
| 東部赛区 | RPS | 中国石油大学（華東） |

## 主要技術発見（第二パス更新版）

### エンジニアロボット
- **双七軸倣人型両腕**: 華南農業大学Taurusが全国大会初・唯一の4級難易度アッセンブリ達成
- **VRヘッドセット操作**: ジェスチャートラッキングによる操作
- **自定义控制器重力補償**: 山东科技大学SmartRobotが三角基関数+Ridge+Huberによる頑健な重力補償を開源（RM2026-0428）
- **工程自定义控制器**: 贵州大学printkが低コスト（ステッピングモーター80元）で実現（RM2026-0432）

### 輪脚・輪足・脚型ロボット
- **華東理工大学起源**: 双輪足構造設計と制御、全国大会3位
- **復旦大学星雲EGA**: 強化学習轮脚「天枢号」
- **華南農業大学Taurus**: 轮脚歩兵を「全明星」構成に含む
- **香港科技大学ENTERPRIZE**: 串联腿歩兵で局均伤害Top 1、12rad/s目標に近距離100%命中率（RM2026-0435）
- **南航金城Born of Fire**: 偏置並列脚（轮腿）の整车電控制御、最高命中率40%（RM2026-0414）
- **浙江大学Hello World**: 轮腿哨兵ナビゲーション開源（RM2026-0423）
- **山东理工大学齐奇**: MPC腿长制御+LESO動的擾動観測（RM2026-0415）

### セントリー・ナビゲーション
- **東北大学TDT**: 四軸ジンバル越トンネルセントリー
- **遼寧科技大学COD**: ROS2 Humble + Nav2 + MPPI + BehaviorTree.CPPの全開源（RM2026-0408）
- **深北莫PolarBear**: Sim2Real開発フロー、Gazeboシミュレーション（RM2026-0305）
- **浙江大学Hello World**: 轮腿哨兵ナビゲーション（RM2026-0423）
- **深圳大学RobotPilots**: Odin1空間記憶モジュールの実戦運用（RM2026-0419）

### レーダー
- **江南大学SHARK**: 無線電+視覚融合識別、局均易傷1927.2秒（RM2026-0409）
- **香港浸会大学Navigator**: PlutoSDRベースRF開発（RM2026-0201）
- **西北工业大学WMJ**: 単SDR方案+GNU Radioで局均186.4s反制、1ヶ月でゼロから全機能構築（RM2026-0411）

### ダーツ
- **北京理工大学DreamChaser**: FPGA制導ダーツ、300FPS認識フレームレート（RM2026-0405）
- **深圳大学RobotPilots**: 2026年シーズン制導ダーツ全面開源（機械+ハードウェア+OpenMV視覚）（RM2026-0418）
- **南京理工大学Alliance**: 4Z軸底座自動調平（3Dプリンター熱床調平方式応用）（RM2026-0426）
- **五邑大学IMCA**: 皮筋系ダーツの核心技術開源（RM2026-0433）

### ビジョン・自瞄
- **深圳大学RobotPilots**: YOLOv8-Pose能量机关五点識別（RM2026-0420）
- **深圳大学RobotPilots**: プラグイン式自瞄フレームワーク（RM2026-0421）
- **浙江大学Hello World**: 能量機関自動攻撃アルゴリズム（RM2026-0422）
- **复旦大学EGA**: 滑模制御器（SMC）による云台制御、哨兵局均命中率Top 1（RM2026-0416）

### 空中ロボット・反無人機
- **华北理工大学Horizon**: 反無人機レーザー追跡、30K+データセット公開（RM2026-0431）

### 制御理論・アルゴリズム
- **滑模制御（SMC）**: 复旦大学EGAが全兵種で採用、教育資料として詳細に開源（RM2026-0416）
- **MPC+LQR+LESO**: 山东理工大学齐奇が轮足制御に応用（RM2026-0415）
- **FEC前向誤り訂正**: 南京理工大学Allianceが吊射図伝に採用（RM2026-0425）

### オープンソースエコシステム
- **rm-battlescope**: 区域赛データ解析・戦術リプレイツール（RM2026-0301）
- **RMOSS**: Gazeboシミュレーション、ROS2ドライバー等（RM2026-0303）
- **rm_vision**: ROS2ベース視覚フレームワーク（RM2026-0304）
- **シーズン終了後の集中開源**: 2026年8月に20+チームが一斉に機械構造・コード・回路を開源
- **Bilibili公式技術動画**: 四軸ジンバル越トンネルセントリー、双七軸倣人型機械臂、轮腿歩兵、VR操作等の視覚的証拠

### Bilibili技術動画発見
- **东北大学TDT 轮腿歩兵**: 30.4万再生（2026年最も注目された技術動画の1つ）
- **华南农业大学Taurus 双七軸機械臂**: 4.9万再生
- **TDT 四軸ジンバル越トンネルセントリー**: 2.8万再生
- **夜空の1時間劇場版シーズン総括**: ファン制作の包括的レビュー

### 教育・産業効果
- 累計941校参加、約20万人のエンジニア育成
- 2026年区域赛：特許150件超、論文70篇近く
- 大疆への累計入社者1000人超
- 就業率ほぼ100%

## 調査継続中のトピック・証拠ギャップ

### 証拠が十分なトピック
- [x] 大会結果とメディア報道
- [x] 双七軸両腕エンジニアの存在と性能
- [x] 輪脚ロボットの複数事例（5+チーム）
- [x] ROS2/Nav2ベースのセントリーナビゲーション
- [x] FPGAダーツの存在
- [x] オープンソースエコシステムの規模（79ソース）
- [x] 大疆との採用連携
- [x] 滑模制御の実戦応用
- [x] 反無人機システム
- [x] 串联腿/偏置並列腿の機動性
- [x] 大学の単位・研究室支援制度の詳細 → 8ソース追加、3大学が公式課程を確認

### 証拠が不足しているトピック
- [ ] 2026年V1→V2ルール変更の詳細な比較
- [ ] 無線充電システムの詳細な実装事例（→上海交大交龙の開源を確認 RM2026-0453）
- [ ] Sim2Realの定量的性能評価（仿真→実車の差）
- [ ] RMOSS/rm_visionの2026年シーズンでの実戦使用状況
- [ ] 飛翔体システムの詳細（空中ロボット）
- [ ] 校友ネットワークの具体的な活動
- [ ] 2027年ルール変更の影響（英雄→重装ロボット？）
- [ ] 东北大学TDT「RoboMaster竞赛步兵机器人设计」教材の確認
- [ ] 哈工大(深圳)「2门校企合作课程」の正式確認
- [ ] 华南理工大学SimulatorX「71所高校使用」の確認
- [ ] 太原科技大学NewMaker基地の詳細
- [ ] 东莞理工学院ACE基金20万元の確認
- [ ] 哈工程「313名学生进入机器人相关企业」の確認

### 矛盾・検証が必要な主張
- 東北大学TDTのセントリーが「四軸ジンバル越トンネル」と報じられるが、具体的な構造の詳細は不明
- 華南農業大学のVR操作の具体的な技術スタック（トラッキングデバイス、通信プロトコル等）
- 輪脚ロボットが「強化学習」で制御されているという主張の範囲（全体制御か部分制御か）
- 深圳大学RobotPilotsの制導ダーツが「競技場で安定命中」できたかどうか
- 哈工程の「313名学生进入企业」と「80%以上升学率」の間の矛盾

---

*最終更新: 2026-08-20*  
*総ソース数: 79*  
*从赛场到课堂調査新規追加: 8ソース (0472-0479)*  
*状態: 最終調査パス完了 — Codex引き継ぎ準備完了*
