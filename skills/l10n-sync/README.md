<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/github/image/xyz/blue.webp" width="150" />
</p>

<h1 align="center">[l10n] / Sync</h1>

<p align="center">
  <strong>The disciplined, token-efficient localization skill</strong>
</p>

<p align="center">
  <a href="../../README.md">← Back to Start / Middle / [End]</a>
</p>

---

Keep this workspace's translated assets in sync with the English source of truth — *without* burning tokens on retranslating what didn't change, and *without* letting the model drop tables, code, links, or keys.

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

## Install

```bash
npx skills add bastndev/skills --skill l10n-sync
```

## Supported Sources

| Source (English)       | Synced targets                  |
| ---------------------- | ------------------------------- |
| `README.md`            | every existing `README_<LANG>.md` next to it (e.g. `public/docs/`) |
| `package.nls.json`     | every existing `package.nls.<lang>.json` sibling |
| `l10n/bundle.l10n.json`| every existing `l10n/bundle.l10n.<lang>.json` sibling |

Any flat `X.json` → `X.<lang>.json` family works the same way. Targets are
discovered automatically — the skill **never invents filenames or languages**;
it only writes to files that already exist (or one the user names explicitly).

## How It Works

A bundled Python script (`scripts/l10n.py`) owns all the structure; the model
only translates. Two modes, chosen automatically per file:

- **Incremental** — the normal case. A git delta finds the blocks that changed
  in the English source; the model translates *only those*, and the script
  splices them back into the exact same positions. A 3-line edit costs
  3 blocks × N languages, not a retranslation.
- **Full** — first translation or a drifted file. The model translates the
  whole file naturally, then `repair` restores anything structural at zero
  token cost and reports any line left in English.

Every run ends with `verify`: a located, actionable report (line/key, exact
token, English vs. translated) — never a guessing game.

## Supported Languages

**Any language whose file exists.** The sync is driven by your files, not by a
fixed list — create `README_TR.md` or `package.nls.it.json` and it gets synced.
The suffix → language map (`ar`, `es`, `pt-br`, `zh-cn`, …) lives in
[`references/langs.md`](./references/langs.md) and is extensible, non-gating.

## Guarantees

- ✅ **English is the source of truth.** The English file is never edited
  during a sync.
- ✅ **Token discipline.** Incremental syncs send the model only the changed
  blocks — never the whole file. Baselines cost the same as translating
  directly, with verification on top.
- ✅ **Invariants survive.** Code spans, URLs, HTML tags, and placeholders
  (`{0}`, `%s`) are preserved verbatim and checked by `verify`.
- ✅ **Structure preserved.** Headings, list markers, and tables are
  reconstructed cell by cell; JSON targets are written by the script itself —
  valid syntax, correct escaping, source key order, removed keys pruned.
- ✅ **Zero-token repair.** `repair` restores verbatim content and realigns
  drifted files without retranslating a single word.

---

→ Full behavior: [SKILL.md](./SKILL.md)

<div align="center">
  <sub>Built for developers who expect AI agents to localize like professionals.</sub>
  <br><br>
  <sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · MIT License</sub>
</div>
