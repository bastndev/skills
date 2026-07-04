---
name: l10n-sync
description: Keep translated README files in sync with the English README.md. Propagates only what changed in the English source into each README_<LANG>.md, preserving tables, code, and links — cheaply and without dropping anything. Use when the user asks to translate, localize, sync, or update a README / docs folder, or invokes this skill.
metadata:
  author: bastndev
  version: "2.0.0"
---

# l10n-sync

Sync translated READMEs from one English source of truth. The script does the
structure (parsing, diffing, splicing, verifying); you do only the translation —
and only of the lines that actually changed.

## The one rule that makes this cheap

**The English `README.md` is the source of truth. You only ever translate the
blocks that changed.** The script diffs the English file against its last git
version, hands you just those blocks, splices your translations back into the
exact same place in each translated file, and verifies nothing was dropped. You
never see the whole file, never see code or URLs, never touch a table by hand.

The skill **never invents filenames or languages**. It writes only to files that
already exist (folder mode) or that the user names explicitly.

## Reading the request

- **Source** = `README.md` at the project root, unless the user names a
  different `.md` as the base. Resolve `@mentions` to plain paths first.
- **Target**:
  - user names a folder (e.g. `docs/`, `public/docs/`) → sync **every existing**
    `README_<LANG>.md` in it.
  - user names a file (e.g. `README_ar.md`) → sync just that file. If it does
    **not** exist yet, create it (the user asked for it explicitly).
- Language comes from the filename suffix (`README_AR.md` → Arabic). No fixed
  language list — whatever files exist is what gets synced.

If the request is missing both a target file and folder, ask once which folder
or file to sync. Otherwise proceed — do not re-ask what the user already said.

## Workflow

Let `SKILL` be this skill's directory and `WORK` a fresh temp dir
(e.g. `/tmp/l10n-work`). Run from the project root.

**1. Plan** — compute what changed:
```bash
python3 "$SKILL/scripts/l10n.py" plan \
  --source README.md \
  --dir public/docs \
  --work "$WORK"
# or a single file:  --file public/docs/README_ar.md
```
This writes `WORK/jobs.json` (blocks to translate) and `WORK/state.json`
(the splice plan). It prints which files need work and which are already
up to date.

**2. Translate** — read `WORK/jobs.json`. For each target it lists `language`
and a small array of `blocks`, each `{id, text, keep}`. Translate `text` into
that language and write `WORK/results.json`:
```json
{ "public/docs/README_AR.md": { "1": "…", "2": "…" },
  "public/docs/README_ES.md": { "1": "…", "2": "…" } }
```
Translation rules:
- Copy every substring listed in `keep` (inline code, URLs, paths, placeholders
  like `{0}`/`%s`, HTML tags) **verbatim** into your translation.
- Translate the *meaning*, naturally. Don't add notes, don't say "translation of",
  don't call yourself an AI, don't restructure.
- Arabic/Hebrew/etc. (`rtl: true`): write natural right-to-left prose; keep code,
  URLs, and placeholders left-to-right; add no bidi markers unless the source has them.
- If a `mode` is `full`, you're establishing a baseline for a new or drifted file —
  translate every block. If `incremental`, you only see the changed blocks.

**3. Apply** — splice and verify:
```bash
python3 "$SKILL/scripts/l10n.py" apply --work "$WORK"
```
This writes every target file and runs the verifier. It reports, per file, slot
parity and any lost invariants. If a file shows `issues`, fix those blocks in
`results.json` (or re-run `plan` in `full` mode for that file) and `apply` again.

You can also verify at any time without writing:
```bash
python3 "$SKILL/scripts/l10n.py" verify --source README.md --dir public/docs
```

## Why nothing gets dropped

Tables, code fences, frontmatter, and links are structural — the script copies
them across verbatim and reconstructs tables cell by cell, so a translation can
never lose a row or a column. After writing, `verify` re-parses every file and
checks: same block count as English, code blocks byte-identical, every
code-span / URL / placeholder still present. That is the guarantee the plain
"just translate the file" approach was missing.

## Output to the user

Post one short table in chat — nothing else. Do not dump file contents.

```
| file             | lang | mode        | blocks | status |
|------------------|------|-------------|--------|--------|
| README_ES.md     | es   | incremental | 6      | ✅     |
| README_AR.md     | ar   | incremental | 6      | ✅     |
| README_DE.md     | de   | full        | 16     | ✅ created |
```

Flag any file whose verify reported `issues` (e.g. `⚠ 1 invariant lost — fixing`).

## Fallback

- **No git** (source not committed): the script can't compute a delta, so every
  existing target is treated as `full` (a clean re-baseline). Costs more tokens
  that one time; still structurally safe.
- **No `python3` / script fails**: translate manually but keep the contract —
  read the English source, edit each `README_<LANG>.md` in place block by block,
  never retranslate untouched sections, never restructure tables. Tell the user
  you're in manual mode.

## Reference

- `scripts/l10n.py` — the parser / differ / splicer / verifier.
- `references/langs.md` — filename-suffix → language map (extensible, non-gating).
