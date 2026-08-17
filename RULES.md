# RULES

## 1. References

- **URLs must be specific**, not top-level pages. Click → direct document.
- **URLs must be clickable links**: Wrap all `Available: URL` with angle brackets: `Available: <URL>`. This enables MkDocs auto-linking.
- **In-body URLs must be links**: Any URL mentioned in body text must be a clickable link: `[text](<URL>)` or `<URL>` for bare URLs.
- **Priority**: ①Chinese primary docs (DJI, teams) ②Zhihu/bbs ③GitHub/Gitee ④Chinese media ⑤EN/JP secondary
- **Format**: IEEE style
  ```
  [n] Author, "Title," Location, Year. [Online]. Available: <URL>
  ```

## 2. Facts First

- No speculation ("〜と考えられる"). Use numbers + quotes.
- Attribute all quotes: `Name (Org) said: "..."[n]`
- No anonymous "experts" or "industry sources"

## 3. Structure

- **Inductive**: concrete example → analysis. Never analysis-first.
- Use data tables. One-line note after each table.

## 4. Chinese Terms

- Attach **simplified Chinese** in parens on first use.
- Example: `全国普通高校大学生競技リスト（全国普通高校大学生竞赛榜单）`

## 5. Kanji

- Use **Japanese kanji** (新字体) in body text.
- Simplified Chinese **only** in: direct quotes, titles, proper nouns, URLs.
- **First-use annotation only**: Attach simplified Chinese in parens on first use of a Chinese term. Subsequent uses use Japanese kanji only.
- Example first use: `全国普通高校大学生競技リスト（全国普通高校大学生竞赛榜单）`
- Example subsequent uses: `ホワイトリスト` (never `白名单` in body text).

## 6. Hyperlinks in Body Text

- Any URL, repository name, BBS post, or forum thread mentioned in body text **must be a clickable link**.
- Examples: `[华南虎战队](<URL>)`, `[bbs.robomaster.com](<URL>)`, `[rmoss_core](<URL>)`.
- Never mention a GitHub repo, Gitee repo, or BBS thread without linking it.

## 7. Topic Ownership

- Each substantial topic has **one canonical chapter**.
- Do not repeat detailed explanations elsewhere.
- Other chapters may mention the topic in 1–2 sentences and point to the canonical chapter.

## 8. Freshness

- Statements about the current state must be verified with recent sources (2025–2026 preferred).
- Historical sources are fine for historical claims.

## 9. Evidence Hierarchy

- Prefer primary official/team sources over secondary summaries.
- Do not use secondary reporting to override newer official information.

## 10. Causality

- Do not infer direct causation from affiliation or technical similarity.
- Distinguish: A. directly documented transfer, B. developed by alumni, C. similar stack, D. speculative.
- Only A or B should be described as direct transfer.

## 11. Numeric Consistency

- The same metric must not have conflicting values across chapters unless definitions differ explicitly.
- If a reliable number cannot be confirmed, remove it or qualify it.
- Do not preserve impressive numbers just because they make the report stronger.

## 12. Cross-Reference Integrity

- Any structural change requires a full repository-wide cross-reference check.
- Update ALL references to chapter numbers, titles, section numbers, and "see Chapter X" links.

## 13. Self-Check on Edit

Before each chapter edit, re-read this file. After adding rules, check for:
- Contradictions with existing rules
- Redundancy (merge don't append)
- Token bloat (shorten, don't elaborate)

---

## IEEE Quick Ref

| Type | Format |
|---|---|
| Online report | `[n] Author, "Title," Location, Year. [Online]. Available: <URL>` |
| Web page | `[n] Author, "Page Title," Website, Date. [Online]. Available: <URL>` |
| GitHub repo | `[n] Author/Org, "Repo Name," GitHub, Year. [Online]. Available: <URL>` |
| Gitee repo | `[n] Author/Org, "Repo Name," Gitee, Year. [Online]. Available: <URL>` |
| Quote/Interview | `[n] Name (Title, Org), "Statement," Context, Date.` |

---

*Adopted 2026-08-17. Apply to all chapters.*
