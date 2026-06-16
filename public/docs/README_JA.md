<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/logo.webp" width="180" />
</p>

<h1 align="center">スタート / ミドル / エンド</h1>

<p align="center">
  <a href="https://github.com/bastndev/skills/blob/main/README.md">English 🇺🇸</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_ES.md">Español 🇪🇸</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_ZH.md">中文 🇨🇳</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_DE.md">Deutsch 🇩🇪</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_FR.md">Français 🇫🇷</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_KO.md">한국어 🇰🇷</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_PT.md">Português 🇧🇷</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_RU.md">Русский 🇷🇺</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_VI.md">Tiếng Việt 🇻🇳</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_HI.md">हिन्दी 🇮🇳</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_AR.md">العربية 🇸🇦</a>
</p>

<br>

<p align="center">
  自信を持って新しいプロジェクトを立ち上げましょう。成長に合わせて反復的に改良・強化し、アーキテクチャの進化が必要な時には深く安全なリファクタリングを実施します。
</p>

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

## 3つのフェーズ

| フェーズ | 目的 | 主要機能 | スキル例 | ステータス |
| --- | --- | --- | --- | --- |
| **Start** | プロジェクトの初期化 | 本番環境に対応したフォルダ構造の作成、フレームワークの初期化、最初のコミットからベストプラクティスを適用。 | `start-nextjs`... | 計画中 |
| **Middle** | 継続的な改善と洗練 | UI/UXの向上、セキュリティの強化、パフォーマンス向上、ロジックのクリーンアップ。 | TBD | 計画中 |
| **End** | 監査、診断、リファクタリング | 完全なアーキテクチャと品質分析。**明示的な承認がある場合のみ**実行される優先順位付きのフェーズ別プラン。 | `refactor-project` | ✅ 利用可能 |

## 利用可能なスキル

| スキル | 説明 |
| --- | --- |
| **[end](../../skills/end/README.md)** | **`refactor-project`** — プロジェクト全体を理解し、具体的な参照を伴う明確な診断を提供します。適切なアーキテクチャの方向性を推奨し、整然とした実行計画を構築します。常にあなたが完全にコントロールします。<br><br>→ [完全なドキュメントと例](../../skills/end/README.md) |

> **注:** 各スキルには独自の詳細なREADMEが付属しています。ルートページは概要を説明しています。詳細な使用方法、レポート例、および保証については、`../../skills/<skill>/README.md`を参照してください。

## インストール

```bash
# 現在のスキルを追加 (End / refactor-project)
npx skills add bastndev/skills --skill end
```

今後のスキルも同じ方法でインストール可能になります:

```bash
npx skills add bastndev/skills --skill start-nextjs
```

## Endスキルの仕組み

1. **まず分析** — エントリポイントをマッピングし、プロジェクトを理解します。**ファイルは変更されません。**
2. **構造化されたレポート** — 4つのカテゴリ（重大度を伴う確認済みバグ、リスク、リファクタリングの機会、技術的負債）の明確な結果 + アーキテクチャの推奨事項と順序付けられた計画。すべての項目に具体的なファイルと行の参照が含まれます。
3. **各フェーズを承認する** — 1度に**1つのフェーズだけ**を実行します。各フェーズの後に、変更の正確な要約、実行された検証、および残りのフェーズのリストが提供されます。
4. **完全な制御と安全性** — プロジェクトにテストがない場合、テストを作成することはありません。許可なく依存関係を追加したり、パッケージマネージャーを変更したりすることはありません。コミットされていない作業を尊重し、正当なバグを修正しない限り、常に現在の動作を保持します。

完全なワークフロー、正確なレポート形式、アーキテクチャの決定ルール、およびすべての安全性の保証については、専用のスキルドキュメントをお読みください。

→ **[End – Refactor Project](../../skills/end/README.md)**

完全な内部仕様は [skills/end/SKILL.md](../../skills/end/SKILL.md) にあります。

## ロードマップ

- **Startスキル** — 人気のあるスタック（Next.js、Vite、FastAPIなど）向けの1コマンドプロジェクトスキャフォールディング。
- **Middleスキル** — オンデマンドの重点的な改善（パフォーマンス、セキュリティ、UX、デッドコードの削除など）。
- **Endの拡張** — より多くのランタイム、追加の専用リファクタリングモード、およびユーティリティ。

各スキルには独自の専用ドキュメントがあります（現在の [End – Refactor Project](../../skills/end/README.md) のように）。

---

<br>

<div align="center">
  <p align="center">
  <sub>AIエージェントにシニアエンジニアの規律を持って行動させたい開発者のために構築されました。</sub>
</p>

_If you find any bugs or have feedback, feel free to [open an issue](https://github.com/bastndev/skills/issues/new)._

<sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a></sub>

</div>
