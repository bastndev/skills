<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/logo.webp" width="180" />
</p>

<h1 align="center">[Start] / Middle / [End]</h1>

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
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_AR.md">العربية 🇸🇦</a><span>...</span>
</p>

<br>

<p align="center">
  新しいプロジェクトを自信を持って立ち上げましょう。成長に合わせて反復的に洗練し、強化します。アーキテクチャの進化が必要な場合、深く安全なリファクタリングを実行します。
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

| フェーズ | 目的 | 主要機能 | スキル例 | ステータス |
| ---------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------ |
| **Start** | プロジェクトを開始する — 新規作成するか、既存のプロジェクトから学ぶ | コミット#1から本番環境に対応した構造と設定を作成します。または、既存のコードベースのアーキテクチャとパッケージを分析し、自プロジェクトで再利用できるものを文書化します。 | `start-package`, `start-astro`, `skrapi` | ㅤㅤ✅ |
| **Middle** | 継続的な改善と磨き上げ | プロジェクトを評価します（0–100のヘルス概要）、然后**一度に1つの次元**を改善します — パフォーマンス、UI/UX、整頓（ファイル順序+コメントの清潔さ）、セキュリティ、構造、クリーンアップ、コード品質 — `go`と入力した場合のみ実行される集中プランで。 | `middle` | ㅤㅤ✅ |
| **End** | 監査、診断と安全なリファクタリング | 完全なアーキテクチャと品質分析。ファイルレベルのエビデンス付きの分類された発見事項。**明示的な承認のみ**で実行される優先度付き段階プラン。動作保持。マルチランタイムサポート。 | `end` | ㅤㅤ✅ |

## 利用可能なスキル

必要になる自然な順序で並べられています — **Start**で新しいものを作成（または既存のコードベースを研究してインスピレーションを得る）、**Middle**で洗練し、**End**で強化します。

| スキル | 説明 |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[start-package](./skills/start-package/README.md)** | _Start_ — バンドルされた型宣言、ゼロコンフィグの`tsup`ビルド、CLIとエディタの両方でクリーンにビルドされるように`5.x`に固定されたTypeScriptを備えた、公開可能な**デュアルESM + CJS** TypeScriptパッケージをスキャフォールドします。`package.json`、`tsconfig.json`、tsup設定、スモークテスト、`.vscode`設定を生成し、インストール、ビルド、検証を行います。<br><br>→ [完全なドキュメント](./skills/start-package/README.md) |
| **[start-astro](./skills/start-astro/README.md)** | _Start_ — `minimal`テンプレートを使用して新しいAstroプロジェクトを作成し、クリーンで**スケーラブルな**アーキテクチャをオーバーレイ — ポートフォリオから完全なアプリに成長する準備が整いました。共有レイアウト、ヘッダー、フッター、ページ、ライト/ダークテーマ切り替え、ネイティブView Transitions、パスエイリアス、Content Collectionsを箱から出してセットアップします。<br><br>→ [完全なドキュメント](./skills/start-astro/README.md) |
| **[skrapi](./skills/skrapi/README.md)** | _Start_ — 難倒するプロジェクトに向け、そのコードベースが固定フォルダ`SKRAPI/`に構築されている方法をマッピング — アーキテクチャ、依存関係、貼り付け可能なプロンプト — 開始前に自分のプロジェクトに合ったパターンを借用できるようにします。任意のスタック（Web、モバイル、拡張機能、ライブラリ、モノレポ）で動作；すべての記述は実際のコードに対して検証され、パッケージ名から推測されることはありません。多言語出力（🇪🇸 ES · 🇺🇸 EN · 🇨🇳 ZH）。<br><br>→ [完全なドキュメント](./skills/skrapi/README.md) |
| **[middle](./skills/middle/README.md)** | _Middle_ — アクティブな開発のための番号付きオンデマンド改善ツール。`0`はプロジェクトやフォルダを0–100のヘルス概要で評価し、最も弱い領域を指摘；`1–7`はそれぞれ1つの次元（⚡パフォーマンス · 🎨 UI/UX · 🗂️整頓 · 🔒セキュリティ · 🏗️構造 · 🧹クリーンアップ · 🧩品質）を評価し、エビデンスに基づいた発見事項を報告し、修正プランを提案 — `go`と入力した場合のみフェーズごとに実行。<br><br>→ [完全なドキュメント](./skills/middle/README.md) |
| **[end](./skills/end/README.md)** | _End_ — プロジェクトを最初から最後まで理解します。明確な診断（確認されたバグ、リスク、機会、技術的負債）を具体的な参照付きで提供し、_この_コードベースに適したアーキテクチャの方向性を推奨し、順序付き実行プランを構築します。すべての変更は隔離されたレビュー可能なフェーズで行われ — `go`、`start`、`proceed`と入力した場合のみ進行し、分析中にファイルは触れられません。<br><br>→ [完全なドキュメントと例](./skills/end/README.md) |
| **[l10n-sync](./skills/l10n-sync/README.md)** | _Utility_ — 慎重でトークン効率の高いローカライゼーションスキル。完全なファイル再翻訳なしで、英語の信頼できるソースと翻訳されたアセットを同期します。11言語で不変要素（コード、HTML）と正確な構造が保持されることを保証します。<br><br>→ [完全なドキュメント](./skills/l10n-sync/README.md) |

> **注意：** 各スキルは独自の詳細なREADMEを同梱しています。ルートページはハイレベルな概要を提供します。深い使用法、レポート例、保証については`./skills/<skill>/README.md`を参照してください。

## インストール

各スキルは同じ方法でインストールします — 必要なものを選んでください：

```bash
npx skills add bastndev/skills --skill start-package   # Start  — scaffold a TS npm package
npx skills add bastndev/skills --skill start-astro     # Start  — scaffold an Astro project
npx skills add bastndev/skills --skill skrapi          # Start  — study & document any codebase
npx skills add bastndev/skills --skill middle          # Middle — score & improve one dimension
npx skills add bastndev/skills --skill end             # End    — audit & safely refactor
npx skills add bastndev/skills --skill l10n-sync       # Utility — sync localized assets safely
```

## Endスキルの仕組み

`end`はスイートで最も成熟したスキルです。そのワークフローを最初から最後まで紹介します：

1. **まず分析** — エントリポイントをマッピングし、プロジェクトを理解します。**ファイルは変更されません。**
2. **構造化レポート** — バグ（重大度付き）、負債/リスク、提案に分類された明確な発見事項に加え、スコア付きヘルス概要、アーキテクチャの推奨、順序付きプラン — すべて具体的なファイル+行の参照で裏付けられています。
3. **各フェーズを承認** — **正確に1つのフェーズ**を一度に実行します。各フェーズ後、変更の正確な要約、実行された検証、残りのフェーズのリストが得られます。
4. **完全な制御と安全性** — プロジェクトにテストがなければ作成しません。許可なく依存関係を追加したりパッケージマネージャーを変更したりしません。未コミットの作業を尊重し、正当なバグを修正する場合を除き、現在の動作を常に保持します。

完全なワークフロー、正確なレポート形式（必須のクロージングブロックを含む）、アーキテクチャの意思決定ルール、すべての安全性の保証については、専用のスキルドキュメントをお読みください：

→ **[End – Refactor Project](./skills/end/README.md)**

完全な内部仕様は[skills/end/SKILL.md](./skills/end/SKILL.md)にあります。

## ロードマップ

- **Start** — `start-package`（スキャフォールド）、`start-astro`（Astroスキャフォールド）、`skrapi`（既存のコードベースの研究）が今日利用可能；さらに多くの`start-*`スキャフォルダーが開発中。
- **Middle** — `middle`が今日利用可能（ヘルス概要+6つの番号付きフォーカス改善ツール）；より深いディメンション別ツールが計画されています。
- **End** — `end`が今日利用可能；追加のランタイム、追加の専門的なリファクタリングモード、ユーティリティが計画されています。
- **Utility** — `l10n-sync`が今日利用可能。慎重でトークン効率の高いワークスペースローカライゼーション用。

各スキルは独自の専用ドキュメントを同梱しています（現在の[End – Refactor Project](./skills/end/README.md)のように）。

---

<br>

<div align="center">
  <p align="center">
  <sub>シニアエンジニアの規律でAIエージェントに行動してほしい開発者のために構築。</sub>
</p>

_バグを見つけたりフィードバックがある場合は、[issueを開いてください](https://github.com/bastndev/skills/issues/new)。_

<sub>🇵🇪で<a href="https://gohit.xyz">Gohit X</a>が制作 · <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a>でライセンス</sub>

</div>
