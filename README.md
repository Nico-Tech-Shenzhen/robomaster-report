# RoboMaster 完全研究レポート

[![Build Status](https://github.com/Nico-Tech-Shenzhen/robomaster-report/actions/workflows/mkdocs-pdf.yml/badge.svg)](https://github.com/Nico-Tech-Shenzhen/robomaster-report/actions/workflows/mkdocs-pdf.yml)

本リポジトリは、次世代ロボットエンジニア支援機構 Scramble（一般社団法人）が作成する、DJI RoboMaster に関する包括的研究レポートのソースです。MkDocs + Material テーマで構築され、GitHub Actions により **Web サイト** と **PDF** を自動生成・デプロイします。

## 公開サイト

| 形式 | URL |
|---|---|
| **Web サイト** | https://nico-tech-shenzhen.github.io/robomaster-report/ |
| **PDF** | GitHub Actions の Artifacts からダウンロード |

## レポート進捗

| 章 | タイトル | 状態 |
|---|---|---|
| [第1章](docs/ch01.md) | RoboMasterとは何か | ✅ Complete |
| [第2章](docs/ch02.md) | 人材と成果 | ✅ Complete |
| [第3章](docs/ch03.md) | エコシステムとコミュニティ | ✅ Complete |
| [第4章](docs/ch04.md) | 教育インパクト | ✅ Complete |
| [第5章](docs/ch05.md) | 技術的深掘り | ✅ Complete |
| [第6章](docs/ch06.md) | DJIの戦略 | ✅ Complete |
| [第7章](docs/ch07.md) | 政策と制度 | ✅ Complete |
| [第8章](docs/ch08.md) | エコシステム（国内比較予定） | 🟡 Skeleton |
| [第9章](docs/ch09.md) | コミュニティとオープンソース | 🟡 Skeleton |
| [第10章](docs/ch10.md) | 国際比較 | 🟡 Skeleton |
| [第11章](docs/ch11.md) | ビジネスモデル | 🟡 Skeleton |
| [第12章](docs/ch12.md) | 未来展望 | 🟡 Skeleton |
| [付録](docs/appendix.md) | | 🟡 Skeleton |

> ✅ = 執筆・レビュー完了　🟡 = 未執筆または Skeleton

## ローカル開発

```bash
pip install mkdocs-material mkdocs-with-pdf pymdown-extensions
mkdocs serve
```

## 構成ツール

| ツール | 用途 |
|---|---|
| [MkDocs](https://www.mkdocs.org/) | 静的サイトジェネレーター |
| [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) | レスポンシブテーマ |
| [mkdocs-with-pdf](https://github.com/orzih/mkdocs-with-pdf) | PDF 出力プラグイン |
| GitHub Actions | 自動ビルド・デプロイ |

## ライセンス

© 2026 Nico Tech Shenzhen / 次世代ロボットエンジニア支援機構 Scramble
