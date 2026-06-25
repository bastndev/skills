<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/logo.webp" width="180" />
</p>

<h1 align="center">[開始] / 中間 / [終了]</h1>

<p align="center">
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_ES.md">Español 🇪🇸</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_ZH.md">中文 🇨🇳</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_DE.md">Deutsch 🇩🇪</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_FR.md">Français 🇫🇷</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_JA.md">日本語 🇯🇵</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_KO.md">한국어 🇰🇷</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_PT.md">Português 🇧🇷</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_RU.md">Русский 🇷🇺</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_VI.md">Tiếng Việt 🇻🇳</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_HI.md">हिन्दी 🇮🇳</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_AR.md">العربية 🇸🇦</a>
</p>

<br>

<p align="center">
  自信を持って新しいプロジェクトを立ち上げます。プロジェクトの成長に合わせて、反復的に改良・強化します。アーキテクチャの進化が必要な場合は、深く安全なリファクタリングを実行します。
</p>

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

```
npx skills add bastndev/skills
```

<br>

## 3つのフェーズ

| フェーズ | 目的 | 主な機能 | スキル例 | ステータス |
| ---------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------ |
| **Start** (開始) | プロジェクトの開始 — 新規の構築、または既存のものからの学習 | 最初のコミットから本番環境で使える構造と設定を作成します。または、既存のコードベースのアーキテクチャやパッケージを分析して文書化し、機能するパターンを自身のプロジェクトで再利用できるようにします。 | `start-package`, `skrapi`       | ㅤㅤ✅ |
| **Middle** (中間) | 継続的な改善と洗練 | 開発中にUI/UXの向上、セキュリティの強化、パフォーマンスの向上、ロジックのクリーンアップ、デッドコードの削除を行います。 | 特定の機能改善ツール (未定) | 計画中 |
| **End** (終了) | 監査、診断、安全なリファクタリング | 完全なアーキテクチャと品質の分析。ファイルレベルの証拠を伴う分類された発見。**明示的な承認がある場合のみ**実行される、優先順位付けされた段階的な計画。動作を維持します。マルチランタイムのサポート。 | `end` | ㅤㅤ✅ |

## 利用可能なスキル

使用する自然な順序でリストされています。新しいものを **Start** (開始) し（またはインスピレーションを得るために既存のコードベースを学習し）、**Middle** (中間) で洗練させ、**End** (終了) で強化します。

| スキル | 説明 |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[start-package](../../skills/start-package/README.md)** | _Start_ (開始) — バンドルされた型宣言、設定不要の `tsup` ビルド、CLIとエディタの両方でクリーンにビルドできるように `5.x` に固定された TypeScript を備えた、公開可能な **デュアル ESM + CJS** TypeScript パッケージを構築します。`package.json`、`tsconfig.json`、tsup設定、スモークテスト、`.vscode` 設定を生成し、インストール、ビルド、検証を実行します。<br><br>→ [完全なドキュメント](../../skills/start-package/README.md) |
| **[skrapi](../../skills/skrapi/README.md)**               | _Start_ (開始) — あなたが感銘を受けたプロジェクトに向けると、そのコードベースの構築方法を、フォーカスされたMarkdownの固定された `SKRAPI/` フォルダ（アーキテクチャ、依存関係、すぐに貼り付け可能なプロンプト）にマッピングします。これにより、開始前に自分のプロジェクトに合ったパターンを借りることができます。あらゆるスタック（Web、モバイル、拡張機能、ライブラリ、モノレポ）で機能します。すべての説明は実際のコードと照合され、パッケージ名から推測されることはありません。多言語出力 (🇪🇸 ES · 🇺🇸 EN · 🇨🇳 ZH)。<br><br>→ [完全なドキュメント](../../skills/skrapi/README.md) |
| **[end](../../skills/end/README.md)**                     | _End_ (終了) — プロジェクトをエンドツーエンドで理解します。具体的な参照を伴う明確な診断（確認されたバグ、リスク、機会、技術的負債）を提供し、_この_コードベースに適切なアーキテクチャの方向性を推奨し、順序付けられた実行計画を構築します。すべての変更は、隔離されたレビュー可能なフェーズで行われます。あなたが `go`、`start`、または `proceed` と言った場合にのみ続行され、分析中にファイルが変更されることはありません。<br><br>→ [完全なドキュメントと例](../../skills/end/README.md) |

> **注：** 各スキルには詳細な README が付属しています。ルートページは全体像を示します。詳細な使用方法、レポートの例、保証事項については、`./skills/<skill>/README.md` を詳しく見てください。

## インストール

すべてのスキルは同じ方法でインストールされます。必要なものを選択してください：

```bash
npx skills add bastndev/skills --skill start-package   # Start (開始) — TS npmパッケージを構築
npx skills add bastndev/skills --skill skrapi          # Start (開始) — 任意のコードベースを学習・文書化
npx skills add bastndev/skills --skill end             # End (終了) — 監査と安全なリファクタリング
```

## 「End」スキルの仕組み

`end` はスイートの中で最も成熟したスキルです。エンドツーエンドのワークフローは次のとおりです。

1. **まず分析** — エントリポイントをマッピングし、プロジェクトを理解します。**ファイルは1つも変更されません。**
2. **構造化されたレポート** — バグ（重大度別）、負債/リスク、提案に分類された明確な発見、さらにスコア化された健全性の概要、アーキテクチャの推奨事項、順序付けられた計画。これらすべてが、具体的なファイルと行の参照によって裏付けられています。
3. **あなたが各フェーズを承認する** — 一度に **正確に1つのフェーズ** のみを実行します。各フェーズの後、変更の正確な要約、実行された検証、および残りのフェーズのリストを受け取ります。
4. **完全な制御と安全性** — プロジェクトにテストがなかった場合、テストを作成することはありません。許可なく依存関係を追加したり、パッケージマネージャーを変更したりすることはありません。コミットされていない作業を尊重し、正当なバグを修正する場合を除き、常に現在の動作を維持します。

完全なワークフロー、正確なレポート形式（必須の終了ブロックを含む）、アーキテクチャの決定ルール、およびすべての安全保証については、専用のスキル ドキュメントをお読みください：

→ **[End – プロジェクトのリファクタリング](../../skills/end/README.md)**

完全な内部仕様は [skills/end/SKILL.md](../../skills/end/SKILL.md) にあります。

## ロードマップ

- **Start** (開始) — `start-package`（構築）と `skrapi`（既存のコードベースの学習）は現在利用可能です。さらに多くの `start-*` 構築ツールが準備中です。
- **Middle** (中間) — 焦点を絞ったオンデマンドの改善ツール（パフォーマンス、セキュリティ、UX、デッドコードの削除）が計画されています。
- **End** (終了) — `end` は現在利用可能です。より多くのランタイム、追加の特殊なリファクタリングモード、ユーティリティが計画されています。

各スキルには独自の専用ドキュメントが付属しています（現在の [End – プロジェクトのリファクタリング](../../skills/end/README.md) のように）。

---

<br>

<div align="center">
  <p align="center">
  <sub>AIエージェントにシニアエンジニアの規律を持って行動させたい開発者のために構築されました。</sub>
</p>

_バグを見つけたり、フィードバックがある場合は、お気軽に [Issue を開いて](https://github.com/bastndev/skills/issues/new) ください。_

<sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a> ライセンスの下で提供</sub>

</div>
