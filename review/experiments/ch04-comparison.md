# Chapter 4 reader-first A/B comparison

## Experiment controls

- **Control (A):** `docs/ch04.md`
- **Candidate (B):** `review/experiments/ch04-reader-first.md`
- **Candidate policy:** `RULES_READER_FIRST_CANDIDATE.md`
- **Evidence freeze:** The candidate uses the same 14 inline citations, the same 14 reference entries, the same cited sources, and the same cases as the control. No web research or new source cards were used.
- **Scope:** Editorial posture, organization, sentence subjects, and table design. This comparison does not select a winner.

## Metric comparison

| Dimension | Control (A) | Candidate (B) | Neutral trade-off |
|---|---|---|---|
| 1. Reader clarity | The opening states the circulation of engineering assets, but some later passages switch from explaining the system to explaining evidentiary limits. | The opening names the thesis in three steps—formal disclosure routes, later citation and modification, multi-season assets—and section openings continue that sequence. | B supplies a more continuous reading path. A makes the boundary between observation and interpretation more conspicuous at the point of each claim. |
| 2. Factual density | High. It includes all institutional details, transfer cases, repository examples, numerical counts, and licensing distinctions. | High. It retains the same cases, counts, repository rows, technical terms, and citations, while converting several methodological statements into descriptions of what the evidence establishes. | B is 106 characters shorter (1.1%) and remains approximately equal in information volume. Some of B's added synthesis occupies space previously used for evidentiary cautions. |
| 3. Defensive prose | Ten reader-facing sentences were removed or transformed because their main work was to state what could not be verified, ranked, guaranteed, or inferred. Seven AWARD table cells were also redesigned from evidence-status commentary into direct links between candidate fields and public material. | Necessary distinctions remain: AWARD panels are nominations rather than final awards; publication is not permission to modify; RMOSS is not a competition-wide standard. | B reduces narration of the research process. A more visibly signals how the authors constrained claims, which some expert readers may value. |
| 4. Causal rigor | Generally rigorous, often using explicit caution before analytical conclusions. | No claim says open source caused technical progress. Relations are limited to formal incentives, documented citations, documented modifications, and persistence of assets across seasons. | B relies more on bounded verbs and less on disclaimers. Its concluding synthesis may feel causally stronger even though each link was already present in A. |
| 5. Risk of promotional tone | Low; limitations and verification language interrupt any celebratory reading. | Low to moderate; the chapter consistently foregrounds a functioning disclosure-and-reuse cycle. | B can sound more affirmative because countervailing absences are less visible. It mitigates this by preserving license limits, the nomination/final-award distinction, and RMOSS's non-standard status. |
| 6. Usefulness of tables | Tables are information-rich, but the AWARD table's final column often reports how far the researchers could verify each row. | Tables answer how disclosure works, what was transferred and modified, how media divide roles, and where reusable assets are found. The AWARD table has four rather than five columns. | B is easier to scan for engineering relationships. A preserves more source-audit detail in the table itself. |
| 7. Strength of chapter thesis | The thesis appears in the opening and transfer cases, but the chapter ends with common software rather than an explicit synthesis. | The thesis appears in the opening, section transitions, transfer-table header, and a new synthesis paragraph at the end. | B has a stronger argumentative arc. Repetition of the cycle may be perceived as editorial steering if the reader prefers a reference-style chapter. |
| 8. Total character count | 9,970 characters, including Markdown and references. | 9,864 characters, including Markdown and references. | B is 106 characters shorter, a reduction of approximately 1.1%; this is not a compression-led rewrite. |
| 9. Citations retained | 14 inline citations; references 1–14. | 14 inline citations; references 1–14. | All citations and source URLs are retained. None were added, replaced, or removed. |
| 10. Factual claims changed | Baseline. | No substantive new factual claims. Dates, counts, institutions, technical elements, reuse relationships, licenses, and repository descriptions remain the same. | Interpretive emphasis changed: B presents the documented sequence as a coherent ecosystem more consistently. That is an editorial synthesis, not a new event, measurement, or causal claim. |

## Defensive and research-process language count

The manual sentence-level comparison identifies **10 sentences removed or transformed**. These include statements centered on what must be understood, what files do not reveal, what must be shown before the report will call something transfer, what cannot be ranked, what an old implementation cannot guarantee, and what evidence does not establish about RMOSS. The count excludes three limitations retained because they change interpretation:

1. AWARD candidate panels are not final awards.
2. Public availability does not itself grant modification or redistribution rights.
3. RMOSS is not a competition-wide unified standard.

The AWARD table also replaces **7 evidence-status cells** with reader-facing publication connections. Those cells are reported separately and are not counted as sentences.

## Representative before/after passages

### Pair 1 — Chapter introduction

**BEFORE**

> RoboMasterでは、ある大学が解いた設計課題が、技術報告、審査、表彰、交流会、BBS、GitHubやGiteeを通じて、別の大学が検証・改良できる工学資産へ変わる。この循環は、公開件数の多さだけではなく、出典を申告し、自校での変更点を説明し、次のシーズンに適用し直す仕組みとして理解する必要がある。

**AFTER**

> RoboMasterは、技術公開を競技後の任意活動だけに委ねず、審査、技術報告、表彰、交流の制度へ組み込んでいる。BBS、GitHub、Giteeへ公開された設計は、後発大学が出典を示して引用し、自校の機体や規則へ合わせて変更し、再び次のシーズンの工学資産として残している。

**WHY IT CHANGED**

The candidate leads with the institutional relationship and documented downstream behavior, rather than telling the reader how the cycle “must be understood.”

**RISK INTRODUCED, IF ANY**

“制度へ組み込んでいる” is more assertive in tone, although Sections 4.1–4.3 directly describe the procedures and awards that support it.

### Pair 2 — Open-source review

**BEFORE**

> したがって、制度の中心は既存成果の利用禁止ではなく、利用関係の可視化にある。先行チームのコードを含む場合は出典を記し、自校のセンサー、座標系、機構、計算資源、競技年へ合わせた変更を説明する。

**AFTER**

> この制度は、既存成果の利用を禁じるのではなく、利用関係を検査可能にする。先行チームのコードを含む場合、大学は出典を記し、自校のセンサー、座標系、機構、計算資源、競技年へ合わせた変更を説明する。

**WHY IT CHANGED**

“検査可能” connects the claim directly to the review procedure, and the university becomes the acting subject.

**RISK INTRODUCED, IF ANY**

None material. The wording remains bounded to what the cited procedure inspects.

### Pair 3 — AWARD

**BEFORE**

> 現地で確認できた71件は候補展示であって、最終受賞者一覧ではない。

**AFTER**

> 2026年8月の全国大会会場では、管理、アルゴリズム、ソフトウェア、組み込み、制御、機械、ハードウェアの候補者パネル71件が展示された。この数は候補展示の集計であり、最終受賞者数ではない。

**WHY IT CHANGED**

The sentence first states what the 71 items are, then preserves the one distinction essential to interpretation.

**RISK INTRODUCED, IF ANY**

None. The candidate/final-award distinction is retained explicitly.

### Pair 4 — Technology-transfer cases

**BEFORE**

> 技術移転を示すには、外観の類似ではなく、後発側が先行資料を明記している必要がある。以下は、出典、再利用箇所、変更内容を後発大学の文書で追える事例である。

**AFTER**

> 後発大学が先行資料を明記し、再利用箇所と変更内容を記録した事例では、公開資産が大学間を移動する過程を追跡できる。

**WHY IT CHANGED**

The candidate states the evidentiary relationship directly and removes a sentence about the report's threshold for accepting a transfer claim.

**RISK INTRODUCED, IF ANY**

The exclusion of visual similarity as evidence is less explicit, though every included case still requires a documented citation and modification.

### Pair 5 — Repositories and media

**BEFORE**

> 索引は有用だが、再利用時には必ず元記事と元リポジトリへ戻り、版とライセンスを確認する必要がある。

**AFTER**

> 索引から元記事と元リポジトリへ進むことで、利用者は版とライセンスを特定できる。BBSの説明、リポジトリの履歴、配布物の実体が組み合わさって、再利用可能な資産になる。

**WHY IT CHANGED**

The candidate explains the information path and its result instead of issuing a methodological instruction.

**RISK INTRODUCED, IF ANY**

The imperative force of checking the original license is weaker. The licensing requirement remains explicit in Section 4.2.

### Pair 6 — RMOSS

**BEFORE**

> 競技全体の統一標準として採用されていることを示す資料はなく、複数の機能を共有・再構成するための基盤と位置づけられる。

**AFTER**

> 競技全体の統一標準ではなく、公開エコシステムから機能を選び、共有・再構成するための基盤である。

**WHY IT CHANGED**

The essential non-universality qualification is retained while the sentence no longer makes the source set its subject.

**RISK INTRODUCED, IF ANY**

The categorical “ではなく” can sound stronger than the control's source-bounded wording. Human review should decide whether “統一標準ではない” or “統一標準とは位置づけない” is preferable.

### Pair 7 — Chapter conclusion

**BEFORE**

> こうした共通基盤は、繰り返し実装する通信・座標・構成管理を共有し、各大学が規則固有の認識、制御、試験へ時間を振り向けるための足場である。

**AFTER**

> こうした共通基盤は、通信、座標、構成管理を毎年ゼロから作り直す範囲を減らし、各大学が規則固有の認識、制御、試験へ開発を接続する足場になる。審査と出典申告が参照関係を可視化し、技術報告、表彰、交流が説明を促し、BBSとリポジトリが成果物と変更履歴を残す。

**WHY IT CHANGED**

The candidate closes the chapter by reconnecting common software to the disclosure–review–publication–reuse cycle tested by the experiment.

**RISK INTRODUCED, IF ANY**

The synthesis is more rhetorically forceful. Its component relations are documented in the chapter, but their arrangement into one ecosystem is analytical rather than a statement taken from one source.

## Factual-meaning audit

No dates, counts, universities, technologies, licenses, citations, or documented reuse relationships were added or removed. No substantive factual meaning changed.

Two wording choices deserve human attention because they alter the strength of presentation without adding facts:

- RMOSS changes from “no material shows competition-wide adoption” to “not a competition-wide unified standard.” The intended scope is the same, but the candidate is grammatically more categorical.
- The final synthesis combines separately documented mechanisms into one ecosystem-level interpretation. It does not assert that open source caused technical progress, but it makes the chapter's analytical thesis more prominent.

## Decision space for human review

The experiment supports three possible editorial decisions without preferring one:

- **A. Merge:** Adopt the candidate posture if continuity of thesis and reader-facing density outweigh the reduced visibility of research-process cautions.
- **B. Revise:** Retain the reader-first structure but soften the two formulations identified in the factual-meaning audit or restore selected source-bound qualifiers.
- **C. Reject:** Keep the control posture if visible evidentiary self-limitation is considered more important than the candidate's narrative continuity.
