---
name: l10n-sync
description: Sync translation files for this workspace — mirrors a canonical English `.md` into per-language `docs/{lang}/` copies, and keeps `package.nls.{lang}.json` + `l10n/bundle.l10n.{lang}.json` in sync with the English source. Use when the user asks to translate, localize, sync, or update README/nls/l10n files, or explicitly invokes this skill.
license: Complete terms in LICENSE.txt
metadata:
  author: bastndev
  version: "1.0.0"
---

# l10n-sync

Keep this workspace's translated assets in sync with the English source of truth — *without* burning tokens on full-file retranslation and *without* letting the model drop tables, code, or keys.

## When to run

The user invokes this skill (e.g. via `/skill`) or asks in natural language to translate / sync / update README or nls files.

**Resolve `@mentions` from the user's message FIRST** (see `references/mention-syntax.md`):
- `@<file>.md` → English source for workflow A.
- `@<folder>/` → target directory for the `.md` mirror (overrides the default `public/docs/`).
- `@package.nls.json` → workflow B.
- `@l10n/` or `@bundle.l10n.en.json` → workflow C.

**If the message already names a source AND (for `.md`) a target dir, proceed directly — do NOT ask again.** Only ask in chat when something is missing or ambiguous:

- ".md" workflow but no `@file.md` source given → ask once: "Which English `.md` should I mirror? (the workspace has several READMEs)"
- ".md" workflow, source given, but no target dir and `public/docs/` does not exist → ask once: "Which folder should the mirrors go into? (default: `public/docs/`)"
- Ambiguous nls source (e.g. no `bundle.l10n.en.json` and the canonical English source is unclear) → ask once.
- User says "all" → run A, B, C in order. For A you still need a source path — ask once if not given.

Do NOT scan unrelated files. Do NOT guess the source file. Do NOT re-ask what the user already said.

## Supported languages

es, zh-cn, de, fr, ja, ko, pt-br, ru, vi, hi, ar

Map (code → label, used only for the chat summary):

| code   | label              |
|--------|--------------------|
| es     | Español 🇪🇸        |
| zh-cn  | 中文 🇨🇳           |
| de     | Deutsch 🇩🇪        |
| fr     | Français 🇫🇷      |
| ja     | 日本語 🇯🇵        |
| ko     | 한국어 🇰🇷         |
| pt-br  | Português 🇧🇷    |
| ru     | Русский 🇷🇺       |
| vi     | Tiếng Việt 🇻🇳   |
| hi     | हिन्दी 🇮🇳         |
| ar     | العربية 🇸🇦        |

## Rules — read these before doing anything

1. **English is the source of truth.** Never edit the English file while running this skill. If a translated file has drifted (extra/missing keys, wrong line count), the English file wins on the next sync; the translated file is regenerated.
2. **Never translate invariants — copy them verbatim:**
   - Code spans `` `like this` `` and fenced code blocks ```` ``` ````.
   - Frontmatter blocks (`---` … `---`).
   - URLs and bare file paths.
   - Raw HTML tags.
   - `{0}` / `{1}` / `%s` / `{name}` style placeholders.
   - The `[My Skills]` / `[My Memory]` / `[MySkills]` prefixes.
   - Emoji and the surrounding whitespace that anchors them.
3. **Don't restructure.** Translated files keep the exact heading hierarchy, list markers, table columns/rows, and blank-line spacing as the English source. The script enforces this — but don't fight it.
4. **Don't call yourself an AI/translator** inside the produced strings. No preambles ("Here is the translation…"), no notes in the output files.
5. **One translation pass per language.** Translate the *flat payload* (`{"id": "English string"}`) and return the same shape back. Nothing else.
6. **RTL**: Arabic strings keep LTR punctuation for placeholders/code, but surrounding prose flows RTL. Don't add bidi markers unless the source has them.
7. **Don't skip a language.** If a folder/file is missing for a language, create it — don't silently drop the language.

## Workflow

### A. `.md` mirror

Source: `path/to/README.md` (English canonical).
Targets: `<target_dir>/{lang}/README.md` for each supported lang — where `<target_dir>` is:
1. the folder the user named via `@<folder>/` if present, else
2. `public/docs/` if it exists in the workspace, else
3. `docs/` (created on first run).

1. Run the extractor on the **English** source:
   ```bash
   python3 future-skill/scripts/extract_reassemble.py extract \
     --source path/to/README.md \
     --out future-skill/scripts/.work/payload.{lang}.json
   ```
   (The extractor produces one payload template per language — identical keys, empty values — so you can run them in parallel.)
2. The output is a flat JSON: `{"markdown:1": "Home", "markdown:3": "Build better prompts", …}`. Keys are positional IDs; values are the English segments. Code/URLs/frontmatter are NOT in the payload (they're recorded in a separate skeleton file the reassembler uses).
3. You translate the payload: for each `lang` in the supported set, produce `payload.{lang}.json` with the same keys and translated values. **Invariants stay byte-identical** (copy from the English payload).
4. Reassemble:
   ```bash
   python3 future-skill/scripts/extract_reassemble.py reassemble \
     --source path/to/README.md \
     --payload future-skill/scripts/.work/payload.{lang}.json \
     --out <target_dir>/{lang}/README.md
   ```
5. Verify with the script's `check` subcommand (line-count parity + "untranslated" detector). If it reports blanks, translate the missing IDs and re-run `reassemble`.

### B. `package.nls.*.json`

Source: `package.nls.json`.
Targets: `package.nls.{lang}.json` for each supported lang.

1. Run:
   ```bash
   python3 future-skill/scripts/extract_reassemble.py extract-nls \
     --source package.nls.json \
     --missing package.nls.{lang}.json \
     --out future-skill/scripts/.work/nls-payload.{lang}.json
   ```
   `--missing` is optional; when given, the payload only includes keys whose value still equals the English value (i.e. likely untranslated) — so you only re-translate what drifted.
2. Translate the payload (same flat-JSON rule).
3. Reassemble:
   ```bash
   python3 future-skill/scripts/extract_reassemble.py reassemble-nls \
     --source package.nls.json \
     --payload future-skill/scripts/.work/nls-payload.{lang}.json \
     --out package.nls.{lang}.json
   ```
4. Run `check-nls` for key-count parity per language.

### C. `l10n/bundle.l10n.*.json`

Source: the English bundle. Look for `l10n/bundle.l10n.en.json`; if absent, the canonical source is the set of keys present in code (`vscode.l10n.t(...)` / `package.nls.json`). Ask the user once which file is canonical if ambiguous — do not guess.

1. Run:
   ```bash
   python3 future-skill/scripts/extract_reassemble.py extract-bundle \
     --source l10n/bundle.l10n.en.json \
     --missing l10n/bundle.l10n.{lang}.json \
     --out future-skill/scripts/.work/bundle-payload.{lang}.json
   ```
   The payload only contains new/changed keys (keys missing from the lang bundle, or whose value still equals English).
2. Translate. NOTE: bundle format is `{"English source": "translated"}` — the **key** is the English source and stays the English source after translation; only the **value** gets translated.
3. Reassemble (merges the translated values into the existing lang bundle, preserving untouched keys):
   ```bash
   python3 future-skill/scripts/extract_reassemble.py reassemble-bundle \
     --source l10n/bundle.l10n.en.json \
     --payload future-skill/scripts/.work/bundle-payload.{lang}.json \
     --out l10n/bundle.l10n.{lang}.json
   ```
4. Run `check-bundle` for key-count parity.

## Token discipline (why this skill exists)

- The model NEVER sees the full markdown — only the translatable strings as a flat list.
- The model NEVER sees code, frontmatter, URLs, or HTML — they're stripped by the extractor and reinserted verbatim by the reassembler.
- For nls, the model only sees keys that drifted (value still equals English) or are missing — never the whole bundle.
- Tables never get dropped: the model sees table cells as flat `id: string` pairs; the reassembler reconstructs the table from the skeleton.
- One model round per language (or one round with a `{"es": {...}, "ja": {...}, …}` envelope if you want all langs in one call — see `references/batching.md`).

## Output to the user

After running, post a short table in chat:

```
| lang   | kind   | keys/lines | status |
|--------|--------|------------|--------|
| es     | md     | 12 / 12    | ✅     |
| zh-cn  | nls    | 2 / 2      | ✅     |
| ja     | bundle | 18 / 18    | ⚠ 1 blank, retranslating |
```

Do not dump file contents into chat. Do not write summaries into `.md` files. Keep all chatter to this table + any failures.

## Fallback when the script is unavailable

If `python3` is missing or the script fails, fall back to manual mode but KEEP THE SAME CONTRACT: read the English source, produce a flat per-language payload in your head, and write the target files preserving structure. Do NOT translate inline in the full markdown — that's exactly the failure mode this skill avoids. Tell the user in chat: "Script unavailable — running in manual mode. Expect higher token use."

## References

- `references/langs.md` — language code → label map and RTL notes.
- `references/file-kinds.md` — how to detect which workflow to run from the source path + target dir resolution.
- `references/mention-syntax.md` — how to resolve `@path` tokens from the user's message.
- `references/reassembly-spec.md` — exact rules the reassembler follows (heading/list/table/code handling).
- `references/batching.md` — how to batch multiple languages into one LLM call.
- `scripts/extract_reassemble.py` — the extractor / reassembler / checker.