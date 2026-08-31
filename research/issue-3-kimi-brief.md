# Kimi research brief — Issue #3: power rules and student electrical architecture

Status: research request only; no production edits authorized. Reference date: 2026-08-31.
Review record: https://github.com/Nico-Tech-Shenzhen/robomaster-report/issues/3
Reviewer who identified the gap: @e-masafumi. Do not infer real name, affiliation, or final contributor status.

## Scope and stopping rule

Use supplied evidence first. Research only current 2026 official power rules, 2–4 technically distinct student implementations, and historical rules needed to resolve a specific change. Stop when these support the proposed additions. Do not survey more universities or pursue adjacent topics. Mark unsupported details as unknown instead of extending the search.

Keep the 79-card corpus frozen. Propose factual corrections to existing cards only; do not create cards. Return findings for human review before Codex verifies the claims selected for publication and makes targeted edits. Do not edit chapters, generate figures/PDFs, post to GitHub, commit, or push.

## Existing coverage and chapter ownership

- `docs/ch02.md`, §2.2: drivetrain, FPGA/vision-board integration, shock-related observations and computing resources; lacks a connected account of student power distribution, sensing and protection. Preserve existing examples.
- `docs/ch07.md`, §7.2: PMM chassis-power measurement and organizer/student responsibilities; lacks the concrete state-dependent limits, energy accounting and enforcement mechanisms. This is the primary home for competition governance.
- `docs/ch03.md`: rule-driven engineering changes and a Beijing Institute of Technology wireless-power example. Add at most one compact, verified power-rule chronology; avoid duplicating Chapter 7.
- Follow `research/china-2026/claims-audit.md`, `dic.md`, `REPORT_PLAN.md` and `CROSS_CHAPTER_MATRIX.md`. Source cards are evidence archives, not production prose.

## A. Official rules: precise questions

Confirm the latest applicable RMUC 2026 Chinese rules and identify differences in date/version from English translations. Starting candidates already collected: competition rules V2.2.0 (2026-08-07), construction specifications V2.0.0 (2026-06-26), communications protocol V2.0.0 (2026-06-26).
Official hub: https://bbs.robomaster.com/wiki/20204847/809871

Verify with section/table/page citations:

1. PMM measurement and switching boundaries: what counts as chassis power; which gimbal, launcher, computing or leg-joint loads are outside that quantity; mandatory routing and any controlled external-supply exceptions. Do not treat chassis power as total robot power.
2. Performance system/level and other modifiers: Hero/Infantry/Sentry initial chassis energy 20,000; maximum 40,000; zero-energy saving state and 35 W basic limit; at least 25,000 gives 125% of the applicable basic limit, capped at 200 W. Clarify Sentry-specific rules and whether 200 W caps the basic adjustment or every possible final limit.
3. Separate game-resource chassis energy, referee buffer energy, and physically stored capacitor energy. Verify PMM Chassis-port output accounting (1 J → resource −1), the precise charging condition and measured difference for replenishment (1 J → resource +8), and wireless replenishment. Do not imply physical energy multiplication or count all battery-to-capacitor charging as replenishment.
4. Buffer capacity/update rule, overload tolerance and chassis power-off duration. Explain how the Supercapacitor Management Module differs from the student converter/controller; required placement, communications and wireless receiver connection.
5. Support the causal explanation: rule → measured constraint → student sensing/model/control → circuit design → operating decisions. Distinguish deductions from measured team results.

Preserve this Japanese wording for later editorial review:
「ロボットの性能体系・レベルや競技中のエネルギー状態に応じて、裁判システムが許容するシャーシ電力上限が変化する。」

## B. Student implementations: bounded candidate set

Use 2–4 cases from this list; do not add teams merely to fill every checklist item.

| University / source | Distinct evidence to extract |
|---|---|
| Tianjin Polytechnic University, 304: https://bbs.robomaster.com/article/1882902 ; https://github.com/TGURM304/PowerManager | Prior overload failures; motor-power model and calibration; per-motor allocation; portability assumptions; supercapacitor interface; exact 2026 deployment scope. Required case. |
| Guilin University of Technology, 群星: https://bbs.robomaster.com/article/714505 ; https://github.com/DonotFreeze/RM-PCB-SuperCapControlBoard_Plus | Bidirectional conversion, remote voltage/current sensing, wiring-drop correction, hardware protection and connector/mounting decisions. Separate RM2025 design from later repository revisions. |
| Xi’an Jiaotong-Liverpool University, OmniX: https://bbs.robomaster.com/article/1914397 | OmniCtrl 2 Pro power tree: input range, DC-DC/LDO, internal/external and analog/digital domains, grounding, eFuse/sequence protection, connectors and supported board mounting. |
| Huazhong University of Science and Technology, 狼牙: https://bbs.robomaster.com/article/376777 | Optional fourth case: actuator-bus-to-computer DC-DC supply, ripple/thermal/layout evidence and protection; distinguish published design from demonstrated match use. |

Across selected cases, extract only documented voltage buses, domain separation, grounding/EMI, current/voltage sensing, protection, connector retention, PCB mounting and wiring strain relief. Record test conditions, operating versus absolute-maximum ratings, measured margins and reported failures. Do not infer galvanic isolation, locking performance, vibration qualification or safety factors from photographs/component names. Distinguish author-reported use, bench measurements, available design files and independently established results.

## C. Minimal historical and corpus conflict checks

- Verify the reported 2024 → 2025 change from overload HP loss to chassis cutoff, using official rules.
- Compare protocol 0x0202 fields across 2024/2025/2026: did voltage/current/power fields become reserved while referee measurement continued? Do not equate removed student telemetry with removed enforcement.
- Determine whether chassis energy and wireless replenishment already existed in 2025; identify the meaningful 2026 changes without calling an existing mechanism new.
- Check `sources/RM2026-0453.md` under the frozen corpus for the “introduced in 2026” wording and claims of completeness/match deployment. Check `RM2026-0469.md` only for any confusion between RMUL match use and national competition use.
- Resolve the existing Chapter 3 Beijing Institute of Technology example against its primary post, https://bbs.robomaster.com/article/1890297 : distinguish inspection passage from actual regional-match charging, including the reported supply-noise limitation. This is an existing-text conflict check, not another implementation survey.

## Return format and handoff

Return a compact claim ledger (claim, primary URL, version/date, section/page or repository commit/path, evidence type, caveat, proposed chapter), one implementation comparison table, and a short unresolved-gap/correction list. Supply short source excerpts only where needed to settle wording or a conflict. Do not draft replacement chapters.

Recommend targeted placement: governance and a three-energy distinction in §7.2; implementation comparison and engineering consequences in §2.2; one verified chronology in Chapter 3. Describe a possible diagram only if it separates state/control signals from physical power paths and preserves non-chassis domains.

Propose reviewer credit only if the eventual expansion warrants it; retain @e-masafumi’s documented role in identifying the gap and defer identity/contributor-table decisions to the human reviewer.

Local handoff aid, if supplied: `tmp/issue3/pdf-manifest.json` lists already collected primary PDFs; adjacent files contain preliminary extracts. These are working material, not approved findings. Reuse relevant documents and avoid repeating broad searches.
