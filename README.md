# RoboMaster 2026 research report

Japanese evidence-based report explaining RoboMaster to first-time readers.

## Chapters

1. RoboMaster 2026の現場
2. 2024→2025→2026の進化——ルール変更が技術をどう動かすか
3. 2026年の機体とソフトウェア
4. 設計資産が次のシーズンへ残る仕組み
5. 誰がチームを動かすのか——学年、登録区分、年間運営
6. 調達、スポンサー、人材と企業
7. DJIと競技用ハードウェアの境界
8. 政府はどう関わるか——制度・政策とRoboMaster
9. 中国の大学ロボット競技の中でRoboMasterは何が違うか

The report is followed by an appendix. Editorial rules are in `RULES.md`, and canonical terminology is in `dic.md`.

## Validation

Run all Python validators under `scripts/`, then `mkdocs build --strict` and `git diff --check`. `scripts/build_pdf.py` provides the separate PDF build.
