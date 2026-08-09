# RoboMaster 完全研究レポート

[![Build Status](https://github.com/Nico-Tech-Shenzhen/robomaster-report/actions/workflows/mkdocs-pdf.yml/badge.svg)](https://github.com/Nico-Tech-Shenzhen/robomaster-report/actions/workflows/mkdocs-pdf.yml)

本リポジトリは、DJI RoboMaster に関する包括的研究レポートのソースです。
MkDocs + Material テーマで構築され、GitHub Actions により自動的にビルド・デプロイされます。

## 公開サイト

- **GitHub Pages**: https://nico-tech-shenzhen.github.io/robomaster-report/

## レポート構成

| 章 | タイトル | 状態 |
|---|---|---|
| 第1章 | RoboMasterとは何か | 🟡 Skeleton |
| 第2章 | 歴史と進化 | 🟡 Skeleton |
| 第3章 | 政策と制度 | ✅ **Complete** |
| 第4章 | DJIの戦略 | 🟡 Skeleton |
| 第5章 | 参加者のプロフィール | 🟡 Skeleton |
| 第6章 | 技術的深掘り | 🟡 Skeleton |
| 第7章 | 教育インパクト | 🟡 Skeleton |
| 第8章 | エコシステム | ✅ **Complete** |
| 第9章 | コミュニティとオープンソース | 🟡 Skeleton |
| 第10章 | 国際比較 | 🟡 Skeleton |
| 第11章 | ビジネスモデル | 🟡 Skeleton |
| 第12章 | 未来展望 | 🟡 Skeleton |
| 付録 | | 🟡 Skeleton |

## 初回セットアップ（GitHub Pages の有効化）

リポジトリ作成時は **GitHub Pages が無効** になっています。以下の手順で有効化してください：

### 1. GitHub Pages を有効化

1. リポジトリの **Settings > Pages** を開く
2. **Build and deployment** → **Source** で **Deploy from a branch** を選択
3. **Branch** で `gh-pages` / `/(root)` を選択
4. **Save** をクリック

> `gh-pages` ブランチは、最初のワークフロー実行時に自動作成されます。

### 2. ワークフローを実行

1. **Actions > Build and Deploy MkDocs** を開く
2. **Run workflow** をクリックして手動実行

または、`main` ブランチに新しいコミットを push すると自動実行されます。

### 3. カスタムドメイン（オプション）

`https://takasumasakazu.net/robomaster-report/` 等のカスタムドメインを使用する場合：

1. **Settings > Pages** の **Custom domain** にドメインを入力
2. DNS で以下の A レコードを設定：
   - `185.199.108.153`
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`

## ローカルプレビュー

```bash
pip install mkdocs-material mkdocs-with-pdf pymdown-extensions
mkdocs serve
```

PDF を含めてビルドする場合：

```bash
ENABLE_PDF_EXPORT=1 mkdocs build
```

## PDF 出力

GitHub Actions の実行結果から PDF アーティファクトをダウンロードできます：

1. **Actions** タブで最新の実行を開く
2. **Artifacts** セクションから `robomaster-report-pdf` をダウンロード

## ライセンス

© 2026 Nico Tech Shenzhen
