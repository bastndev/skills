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

Keep this workspace's translated assets in sync with the English source of truth — *without* burning tokens on full-file retranslation and *without* letting the model drop tables, code, or keys.

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

## Install

```bash
npx skills add bastndev/skills --skill l10n-sync
```

## Supported Workflows

- **`.md` mirror**: Mirrors a canonical English `.md` into per-language `docs/{lang}/` copies.
- **`package.nls.json`**: Syncs all `package.nls.{lang}.json`.
- **`l10n/bundle.l10n.en.json`**: Syncs all `l10n/bundle.l10n.{lang}.json` (or uses the English source as fallback).

## Supported Languages

es 🇪🇸, zh-cn 🇨🇳, de 🇩🇪, fr 🇫🇷, ja 🇯🇵, ko 🇰🇷, pt-br 🇧🇷, ru 🇷🇺, vi 🇻🇳, hi 🇮🇳, ar 🇸🇦

## Guarantees

- ✅ **English is the source of truth.** Never edits the English file during sync.
- ✅ **Token discipline.** The model NEVER sees the full markdown or bundles — only the translatable strings as a flat list.
- ✅ **Never translates invariants.** Code spans, frontmatter, URLs, and HTML are preserved verbatim.
- ✅ **Preserves structure.** Translated files keep exact heading hierarchy, list markers, and table structures.
- ✅ **One translation pass per language.**

---

→ Full behavior: [SKILL.md](./SKILL.md)

<div align="center">
  <sub>Built for developers who expect AI agents to localize like professionals.</sub>
  <br><br>
  <sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · MIT License</sub>
</div>