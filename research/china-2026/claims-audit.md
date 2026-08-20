# RoboMaster 2026: Claims Audit

## Audit Method
- Every claim containing superlatives (only, first, highest, 100%, etc.) is audited
- Evidence type: official=组委会公告, media=新闻报道, team=战队自述, video=视频演示
- Confidence: high=多源交叉验证, medium=单一强源, low=弱源或间接推断

---

## Verified Claims

| Claim | Source IDs | Evidence type | Confidence | Safe wording | Notes |
|---|---|---|---|---|---|
| 2026 champion = 东北大学 TDT | RM2026-0101, RM2026-0102, RM2026-0104, RM2026-0105 | media + university + official live | **high** | "东北大学TDT战队获得2026年全国总冠军" | 多源一致：人民日报、中国青年报、中国科技网、搜狐、深圳政府网 |
| 2026 runner-up = 华南农业大学 Taurus | RM2026-0101, RM2026-0102, RM2026-0103, RM2026-0105 | media + university_primary | **high** | "华南农业大学Taurus战队获得全国亚军" | 多源一致，校官网确认 |
| 2026 third = 华东理工大学 起源 | RM2026-0101, RM2026-0105 | media + university_primary | **high** | "华东理工大学起源战队获得季军" | 校官网+多媒体报道一致 |
| 2026 fourth = 同济大学 SuperPower | RM2026-0101, RM2026-0102 | media | **high** | "同济大学SuperPower战队获得殿军" | 多源一致 |
| National final date = 2026-08-09 | RM2026-0101, RM2026-0102 | media + official | **high** | "全国总决赛于8月9日在深圳落幕" | 多源一致 |
| National final location = 深圳湾体育中心"春茧" | RM2026-0101, RM2026-0105 | media | **high** | "在深圳湾体育中心'春茧'体育馆举行" | 多源一致 |
| 44 teams at national final | RM2026-0101, RM2026-0102, RM2026-0105 | media | **high** | "来自全国各地的44支高校战队" | 多源一致 |
| Taurus dual-seven-axis arms exist | RM2026-0103, RM2026-0442, RM2026-0444 | university_primary + video | **high** | "战队首创的双七轴仿人形双臂工程机器人" | 校官网 + Bilibili官方视频交叉验证 |
| Taurus level-4 assembly achievement | RM2026-0103, RM2026-0440, RM2026-0445 | university_primary + video | **high** | "Taurus还成为了国赛首支且唯一完成四级难度装配的队伍" | 校官网 + 决赛视频交叉验证 |
| Taurus 3 level-4 assemblies at nationals | RM2026-0103 | university_primary | **medium** | "本赛季全国赛中，Taurus共完成3次四级难度装配" | 单一来源（校官网） |
| Taurus VR teleoperation used | RM2026-0102, RM2026-0103, RM2026-0444 | media + university + video | **medium** | "用VR头显去做手势追踪的话，完成装配、拿取等场上操作时会更贴合人的习惯" | 谭嘉豪口述 + 官方VR演示视频 |
| TDT wheel-leg infantry fielded | RM2026-0443 | video_primary | **high** | "东北大学TDT战队 fielded a 轮圈腿构型步兵机器人" | Bilibili official, 304k views |
| TDT four-axis gimbal tunnel sentry | RM2026-0101, RM2026-0441 | media + video | **high** | "四轴云台越隧哨兵机器人" | 人民日报 + Bilibili官方视频交叉验证 |
| Northeastern sentry praised by captain | RM2026-0102 | media (interview) | **medium** | "这一次，在赛场上表现亮眼的是哨兵机器人" | 队长张荣凯口述 |
| ~2000 students at national final | RM2026-0105 | media | **medium** | "来自全国32所顶尖高校的约2000名青年工程师" | 深圳新闻网，但"32所"与"44支"存在矛盾 |
| ~300 robots at national final | RM2026-0105 | media | **medium** | "携近300台自主研发的机器人展开角逐" | 深圳新闻网单一来源 |
| Cumulative 941 universities registered | RM2026-0101 | media | **medium** | "截至目前，赛事累计吸引全球941所高校报名" | 人民日报，"截至目前"时间锚点不明 |
| Cumulative ~200,000 engineers trained | RM2026-0101 | media | **medium** | "培养了近20万名具备系统性工程思维的复合型青年工程师" | 人民日报，累计数，计算方法不明 |
| 2026 regional patents 150+ | RM2026-0101 | media | **medium** | "2026赛季区域赛统计显示，参赛队伍产出专利150余项" | 人民日报，"区域赛统计"具体出处不明 |
| 2026 regional papers ~70 | RM2026-0101 | media | **medium** | "论文近70篇" | 人民日报，同上 |
| DJI 1000+ hires from RM participants | RM2026-0501 | official_primary | **medium** | "截至目前，已有超1000位参与过RoboMaster机甲大师赛的优秀人才入职大疆" | 官方招聘页面，"截至目前"时间锚点不明 |
| Employment rate near 100% | RM2026-0101, RM2026-0105 | media | **low** | "参赛学生就业率近100%" | 多媒体报道但无原始数据来源 |
| FPGA dart 300 FPS | RM2026-0405 | team_primary | **medium** | "300FPS识别帧率FPGA制导飞镖" | 北京理工DreamChaser自述，BBS开源，独立验证なし |
| Navigator radar V1.4.0 | RM2026-0201 | technical_secondary | **medium** | "V1.4.0开始...不需要再担心系统动态范围问题以及同频干扰问题" | BBS技术博客，个人经验 |
| SHARK radar 1927.2s average marked time | RM2026-0409 | team_primary | **low** | "局均易伤1927.2s" | 江南大学SHARK自述，计量方法不明 |
| ZJU fluo-charger 40 yuan cost | RM2026-0406 | team_primary | **medium** | "单套装置的复刻成本可控制在40元以内" | 浙江大学Hello World自述，开源验证可能 |
| ZJU fluo-charger brightness 150+ | RM2026-0406 | team_primary | **medium** | "官方检录亮度值可达150以上" | 浙江大学Hello World自述 |
| COD sentry 12.50kg | RM2026-0408 | team_primary | **medium** | "整车质量约12.50Kg（不计算裁判系统）" | 遼寧科技大学COD自述 |
| ECUST origin wheel-leg | RM2026-0105, RM2026-0446, RM2026-0452 | university_primary + video + repo | **high** | "双轮足机器人结构设计与控制" | 校官网 + Bilibili官方 + GitHub开源交叉验证 |
| Fudan EGA reinforcement learning wheel-leg | RM2026-0202 | video_primary | **medium** | "天枢号「强化学习」轮腿机器人" | Bilibili视频标题，具体算法不明 |
| Fudan EGA SMC controller open-sourced | RM2026-0416, RM2026-0417, xinruilee04/smc_controller | team_primary + repository | **high** | "滑模控制器教学&开源，适配全兵种" | BBS技术报告 + GitHub実装 |
| Hebei U Zhili mecha founded Nov 2024 | RM2026-0204 | university_primary | **high** | "河北大学直隶机甲战队自2024年11月成立以来" | 校官网 |
| North region champion = NEU TDT | RM2026-0104 | media | **high** | "东北大学中鸿TDT战队获得冠军" | 中国日报 |
| East region champion = UPC RPS | rm.ecustcic.com | official_secondary | **high** | 官方数据平台确认 | |
| South region champion = SCAU Taurus | rm.ecustcic.com | official_secondary | **high** | 官方数据平台确认 | |
| ZJU energy mechanism auto-attack open-sourced | RM2026-0422 | team_primary + repository | **high** | "能量机关自动攻击算法开源" | BBS + GitHub |
| ZJU wheel-leg sentry navigation open-sourced | RM2026-0423 | repository_primary | **high** | "轮腿哨兵导航算法开源（ROS2）" | GitHub Polyacetone |
| SZU guided dart system open-sourced | RM2026-0418 | team_primary | **high** | "制导飞镖全面开源（机械+硬件+OpenMV）" | BBS技术报告 |
| SZU YOLOv8-Pose energy mechanism | RM2026-0420 | team_primary + repository | **high** | "YOLOv8-Pose能量机关五点识别" | BBS + GitHub |
| SZU plugin-based auto-aim framework | RM2026-0421 | repository_primary | **high** | "自瞄算法框架开源" | GitHub |
| NPU WMJ radar single SDR + GNU Radio | RM2026-0411, zplszz/WMJRadar | team_primary + repository | **high** | "单SDR方案+GNU Radio雷达开源" | BBS + GitHub |
| SCUT SimulatorX open-sourced | RM2026-0465, scutrobotlab/RM2022_SimulatorX | team_primary + repository | **high** | "SimulatorX仿真平台开源（2022）" | BBS + GitHub |
| **DGUT 3.5-credit/56-hour robot course** | RM2026-0476 | university_primary | **high** | "计算机科学与技术专业开设'机器人应用开发实践'课程，3.5学分，56学时" | 公式課程大綱完全一致。展示パネルと大学カタログが完全一致 |
| **HEU Chuangmeng four-level progressive system** | RM2026-0477 | university_primary | **high** | "建立'校内赛→联盟赛→超级对抗赛→AI挑战赛'四级递进培养体系" | 公式校報（hrbeu.edu.cn） |
| **HEU 6 innovation courses, 8000+ person-hours** | RM2026-0477 | university_primary | **medium** | "开设6门创新课程，累计8000余人时" | 公式校報。累計の範囲不明 |
| **HEU 80%+ team members enter graduate school** | RM2026-0477 | university_primary | **medium** | "团队学生升学率超80%" | 公式校報。対象コーホートの定義不明 |
| **NEU 《机器人创新设计》elective exists** | RM2026-0472 | university_primary | **medium** | "东北大学开设《机器人创新设计》选修课程（C3000000119）" | 课程目录確認済み。教員はACTION/RoboconでTDTとの直接関連未確認。RoboMaster言及なし |
| **JLU Jijia Master Base recognized** | RM2026-0474 | university_primary | **medium** | "吉林大学设立'吉甲大师'大学生双创实践基地" | 党委書記視察（2025年5月）+ 100万元募金目標確認 |
| **HIT(SZ) Nangong Xiaoying 80 members, 54 awards** | RM2026-0473 | university_primary | **medium** | "南工骁鹰机器人战队现有队员约80人，获省级以上奖项54项" | 複数のhitsz.edu.cn記事で交叉验证 |
| **USTB Reborn innovation base 8 labs, 1500+/year** | RM2026-0475 | university_primary | **medium** | "拥有8间创新实验室，总面积近2000平方米，每年服务学生1500余人" | 公式教務PDF |
| **USTB all undergraduates required ≥2 innovation credits** | RM2026-0475 | university_primary | **high** | "本科生在校期间必须完成不少于2个创新创业学分" | 公式教務PDF。全学生必修 |

---

## Claims Requiring Downgrade

| Original Claim | Problem | Downgraded Wording |
|---|---|---|
| "Taurus became the first and only team to complete level-4 assembly" | "first and only" = superlative; only source is SCAU's own website | "Taurus reported completing level-4 assembly at the national final; no other team publicly claimed this achievement" |
| "Employment rate near 100%" | No primary source or methodology given | "Media reports cited a high employment rate among participants; exact methodology unavailable" |
| "Cumulative 200,000 engineers" | Calculation method unclear; cumulative since 2013? | "The competition has reportedly attracted participants from many universities over multiple years" |
| "SHARK radar 1927.2s average marked time" | Single team claim; measurement method undefined | "SHARK team reported an average marked-time metric of 1927.2s" |
| "Northeastern 4-axis gimbal tunnel sentry" | Description appears in media as industrial application potential, not confirmed competition spec | "Media described Northeastern's sentry as having tunnel-crossing capabilities with potential industrial applications" |
| **"SimulatorX used by 71 universities"** | **Panel claim only; no independent verification found** | **"SCUT's exhibition panel claimed SimulatorX was used by 71 universities; this could not be independently verified"** |
| **"TDT 1000+ professionals, 100+ patents, 《RoboMaster竞赛步兵机器人设计》textbook"** | **Panel claim only; textbook NOT found in any catalog or database** | **"NEU exhibition panel claimed TDT had cultivated 1000+ professionals and published a textbook; these remain unverified"** |
| **"ACE Fund 200,000 RMB"** | **Panel claim only; no corroborating source found** | **"DGUT exhibition panel mentioned an ACE Fund of 200,000 RMB; no corroborating source was found"** |
| **"HEU 313 students entered robot enterprises"** | **Panel claim only; official source confirms 80%+ graduate school rate, not enterprise placement** | **"HEU panel claimed 313 students entered robot-related enterprises; official sources only confirm 80%+ graduate school rate"** |
| **"JLU 56 national-level awards, 3 incubated companies"** | **Panel claim only; fundraising page and base visit confirmed but not specific counts** | **"JLU panel claimed 56 national awards and 3 incubated companies; only base existence and 1M RMB fundraising target were verified"** |
| **"USTB 竞技机器人实践 course, 1700+ students"** | **Specific course title not confirmed; 1500+/year confirmed from innovation base** | **"USTB runs robot-related practice through its innovation base serving 1500+ students/year; the specific course title '竞技机器人实践' was not confirmed"** |
| **"TYUST 280 class hours, 800+/year, 99 awards, 6 companies"** | **Panel claim only; no primary source found (search returned 404)** | **"TYUST panel claimed multiple quantitative achievements; none could be verified through primary sources"** |
| **"HIT(SZ) 2 school-enterprise courses, 2 teaching papers on DJI Education platform"** | **Panel claim only; team existence confirmed but curriculum details not found** | **"HIT(SZ) panel claimed 2 school-enterprise courses and 2 teaching papers; only team existence and award counts were verified"** |

---

## Conflicting Claims

| Claim A | Claim B | Resolution |
|---|---|---|
| "44 teams at national final" (多源) | "32 universities, ~2000 students" (深圳新闻网) | "44 teams" is from official tournament structure; "32 universities" may refer to a subset or be a reporting error |
| "Taurus only team with level-4 assembly" (校官网) | No other team claims level-4 | Unverified; other teams may have achieved it without public announcement |
| **"HEU 313 students entered enterprises" (panel)** | **"HEU 80%+ enter graduate school" (official)** | **Panel claims enterprise placement; official source confirms graduate school. These may describe different cohorts or time periods, but direct conflict exists** |

---

## Metrics Separation Record

| Metric | Original Chinese | Year | Scope | Cumulative/Annual | Type | Primary Source |
|--------|-----------------|------|-------|------------------|------|---------------|
| 专利150余项 | "参赛队伍产出专利150余项" | 2026 | 区域赛 | Annual (2026 season only) | Patent applications (implied, not granted) | 人民日报 [RM2026-0101] |
| 论文近70篇 | "论文近70篇" | 2026 | 区域赛 | Annual | Papers (academic, not further specified) | 人民日报 [RM2026-0101] |
| 其他创新成果50余项 | "其他创新成果50余项" | 2026 | 区域赛 | Annual | Other innovation outputs | 深圳新闻网 [RM2026-0105] |
| 累计941所高校 | "赛事累计吸引全球941所高校报名" | 截至2026 | Global | Cumulative (since ~2013) | Registered universities | 人民日报 [RM2026-0101] |
| 近20万名工程师 | "培养了近20万名...青年工程师" | 截至2026 | Global | Cumulative | Engineers trained | 人民日报 [RM2026-0101] |
| 超千项专利和开源报告 | "参赛队员提交的国家专利申请及开源技术报告超千项" | 截至2026 | Global | Cumulative | Patent applications + open-source reports (combined) | 人民日报 [RM2026-0101] |
| 超1000位入职大疆 | "已有超1000位...优秀人才入职大疆" | 截至2026 | Global | Cumulative | DJI hires from RM participants | 大疆官方 [RM2026-0501] |
| **8000余人时** | **"开设6门创新课程，累计8000余人时"** | **—** | **HEU Chuangmeng** | **Cumulative** | **Innovation course person-hours** | **hrbeu.edu.cn [RM2026-0477]** |
| **升学率超80%** | **"团队学生升学率超80%"** | **—** | **HEU Chuangmeng** | **Annual/Cohort** | **Graduate school admission rate** | **hrbeu.edu.cn [RM2026-0477]** |
| **515名学生** | **"近3年累计选课学生515人"** | **—** | **DGUT (panel)** | **Cumulative (3 years)** | **Course enrollment** | **Panel only [IMG_20260808_164259]** |
| **1000余名机器人领域专业人才** | **"累计培养机器人领域专业人才1000余名"** | **—** | **NEU TDT (panel)** | **Cumulative** | **Professionals trained** | **Panel only [IMG_20260808_164237]** |
| **每年服务学生1500余人** | **"每年服务学生1500余人"** | **—** | **USTB Reborn** | **Annual** | **Innovation base students served** | **ustb.edu.cn [RM2026-0475]** |
| **280学时新生培训教材** | **"组织完成280学时新生培训教材"** | **—** | **TYUST (panel)** | **Cumulative** | **Training materials** | **Panel only [IMG_20260808_164242]** |
| **每年公益培训800余名学生** | **"每年公益培训800余名学生"** | **—** | **TYUST (panel)** | **Annual** | **Public welfare training** | **Panel only [IMG_20260808_164242]** |

---

## Education Evidence Clusters — Quick Reference

| Cluster | University | Claim | Strength | Key Source |
|---------|-----------|-------|----------|------------|
| 11 | DGUT | 3.5-credit/56-hour course in official CS curriculum | **STRONG** | RM2026-0476 |
| 10 | HEU | Four-level progressive system; 6 courses; 8000+ hrs | **STRONG** | RM2026-0477 |
| 12 | HIT(SZ) | Team under official education center; 80 members; 54 awards | **MEDIUM** | RM2026-0473 |
| 13 | JLU | Official innovation base; Party Secretary visit; 1M RMB target | **MEDIUM** | RM2026-0474 |
| 14 | USTB | Innovation base 8 labs, 1500+/year; ≥2 credits required | **MEDIUM** | RM2026-0475 |
| 15 | NEU | Elective course C3000000119 exists; instructor ACTION/Robocon | **MEDIUM** | RM2026-0472 |

*Last updated: 2026-08-20*
*Status: Final audit pass — education claims integrated, evidence clusters reflected*
