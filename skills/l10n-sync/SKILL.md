---
name: l10n-sync
description: Keep translated README files in sync with the English README.md. Propagates only what changed in the English source into each README_<LANG>.md, preserving tables, code, and links — cheaply and without dropping anything. Use when the user asks to translate, localize, sync, or update a README / docs folder, or invokes this skill.
metadata:
  author: bastndev
  version: "3.0.0"
---

# l10n-sync

One English `README.md` is the source of truth; this skill keeps every
`README_<LANG>.md` in sync with it. The script does all structure work
(parsing, diffing, splicing, repairing, verifying); you do only the
translation. `plan` picks the mode per file, automatically:

- **incremental** — the file is structurally in sync and only some English
  blocks changed: you translate just those blocks. This is the normal case
  and the whole point of the skill: a 3-line edit costs 3 blocks × N
  languages, not a retranslation.
- **full** — first translation, a new file the user asked for, or a drifted
  file: you translate the whole file directly, naturally, in one Write — then
  `repair` fixes any structural slip for zero tokens. A baseline costs about
  the same as translating without the skill; every sync after it is nearly
  free. Do NOT ship a full file through block JSON.

## Hard rules (each one exists because a real run failed without it)

1. **Translate everything yourself, in this session, one language at a
   time. Never spawn subagents** unless the user explicitly asks for
   parallel agents — subagents hang on rate-limited models and multiply
   token cost by the number of agents.
2. **Never write helper scripts** (`extract.py`, `generate_xx.py`, …) and
   never hand-patch JSON with ad-hoc python. Every operation you need is
   already a command: `plan`, `merge`, `apply`, `verify`, `repair`. If you
   feel you need a script, re-read this file instead.
3. The work dir is **`.l10n-work/` at the project root** — every command
   defaults to it. Never use `/tmp`: files outside the workspace trigger
   permission prompts that freeze some harnesses. Delete `.l10n-work/`
   after a successful run.
4. **Never invent filenames or languages.** Folder mode syncs only the
   `README_<LANG>.md` files that already exist; create a file only when the
   user named it explicitly.
5. Always run python with `-B` (no `__pycache__/` litter).

## Reading the request

- **Source** = `README.md` at the project root, unless the user names a
  different `.md` as the base. Resolve `@mentions` to plain paths first.
- **Target**: a folder (e.g. `public/docs/`) → every existing
  `README_<LANG>.md` in it; a named file → just that file (create it if
  missing — the user asked for it). Language comes from the filename suffix
  (`README_AR.md` → Arabic).
- If both are missing, ask once which folder or file to sync. Otherwise
  proceed — do not re-ask what the user already said.

## Workflow

Let `SKILL` be this skill's directory. Run everything from the project root.

**1. Plan**
```bash
python3 -B "$SKILL/scripts/l10n.py" plan --source README.md --dir public/docs
# single file:  --file public/docs/README_ar.md
# force a re-baseline of every target (only if the user asks):  --full
```
It prints `up_to_date`, `translate_directly` (full mode), `incremental`, and
a `next` instruction — follow `next`. If a run ever dies midway, just re-run
`plan` (without `--full`): finished files drop out on their own.

**2a. Full files** (`translate_directly`) — one language at a time:

1. Write the **complete translated file** yourself in a single Write.
   The contract:
   - Translate prose only: headings, paragraphs, list items, and table
     cells that contain sentences.
   - Copy **byte-for-byte**: code fences, inline code, URLs and link
     targets, badges, every HTML tag with all its attributes, the
     language-switcher block, keyboard-shortcut cells.
   - Keep the exact same block structure — same headings, same rows, same
     lines. Never merge, split, or drop blocks. No notes, no "translated
     by", no restructuring.
   - RTL languages (ar, he, …): natural right-to-left prose; code, URLs and
     placeholders stay left-to-right; no bidi markers unless the source has
     them.
2. Immediately check that file:
   ```bash
   python3 -B "$SKILL/scripts/l10n.py" repair --source README.md --file public/docs/README_XX.md
   ```
   `repair` costs zero tokens: it restores structural slips, realigns
   dropped/extra blocks, refills emptied cells, and prints any line left in
   English. Fix **only** the lines it lists, in place, then move to the
   next language.

**2b. Incremental files** — read `.l10n-work/jobs.json`. `blocks` appears
**once** (the English is identical for every language); translate each block
once per language in `targets` and write `.l10n-work/results.json`:
```json
{ "public/docs/README_AR.md": { "1": "…", "2": "…" },
  "public/docs/README_ES.md": { "1": "…", "2": "…" } }
```
- Copy every substring in `keep` (inline code, URLs, paths, placeholders,
  HTML tags) verbatim; translate the meaning naturally.
- Splice and verify:
```bash
python3 -B "$SKILL/scripts/l10n.py" apply
```
The report is already located — line, exact token, English vs. translated.
Fix exactly what it lists (edit `results.json` or the file) and re-run
`apply`. Do not hunt for problems with your own scripts.

**Parallel agents — only if the user explicitly asked for them.** Group
languages into at most 3–4 agents; each writes
`.l10n-work/partial-<lang>.json` shaped `{"1": "…"}` and MUST validate it
with `python3 -m json.tool <file>` before finishing (unescaped `"` inside a
translation is the classic failure). Then:
```bash
python3 -B "$SKILL/scripts/l10n.py" merge   # validates all partials → results.json
```
If `merge` flags a partial, have that agent rewrite just that file and
re-run `merge`.

**3. Finish**
```bash
python3 -B "$SKILL/scripts/l10n.py" verify --source README.md --dir public/docs
rm -rf .l10n-work
```
(`verify` prints the readable report; add `--json` if you need to parse it.)

## Why nothing gets dropped

`repair` and `verify` re-parse every file against the source: same block
structure, code fences byte-identical, every code span / URL / placeholder /
HTML tag still present, tables intact cell by cell. `repair` restores
verbatim parts from English without touching translations — so even a sloppy
full translation converges in one pass plus the few line fixes it lists.

## Output to the user

Post one short table in chat — nothing else. Do not dump file contents.

```
| file             | lang | mode        | blocks | status |
|------------------|------|-------------|--------|--------|
| README_ES.md     | es   | incremental | 6      | ✅     |
| README_AR.md     | ar   | incremental | 6      | ✅     |
| README_DE.md     | de   | full        | —      | ✅ created |
```

Flag any file whose verify reported `issues` (e.g. `⚠ 1 invariant lost — fixing`).

## Fallback

- **No git** (source not committed): no delta is possible, so existing
  targets are treated as full — direct translation + `repair`. Still
  structurally safe.
- **No `python3` / script fails**: translate manually but keep the contract —
  edit each `README_<LANG>.md` in place block by block, never retranslate
  untouched sections, never restructure tables. Tell the user you're in
  manual mode.

## Reference

- `scripts/l10n.py` — the parser / differ / splicer / repairer / verifier.
- `references/langs.md` — filename-suffix → language map (extensible, non-gating).
