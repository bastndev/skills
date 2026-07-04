# Reassembly spec

The reassembler is the only thing that touches the translated file structure. The model MUST trust it — never hand-edit the markdown layout.

## What the extractor pulls into the payload

For a `.md` source, the extractor walks lines and classifies each:

| block type              | in payload? | in skeleton (verbatim)? |
|-------------------------|-------------|-------------------------|
| frontmatter (`---` … `---`) | no      | yes                     |
| ATX heading text (`# Foo`)  | yes (text only) | marker (`#`) kept in skeleton |
| fenced code block ```` ``` ```` | no   | yes (whole block)       |
| inline code span `` `x` ``   | no   | yes (verbatim)          |
| table separator row (`|---|`) | no  | yes                     |
| table cell text            | yes (per cell) | pipes/whitespace kept in skeleton |
| list item text             | yes (text only) | marker (`-`/`1.`) kept |
| blockquote text            | yes        | `>` kept in skeleton    |
| URL in `[text](url)` or `<url>` | text only (yes); url no | url kept verbatim |
| raw HTML `<...>`           | no         | yes                     |
| blank line                 | no         | yes                     |
| paragraph text             | yes        | yes (the surrounding lines) |

SKU: the payload is a *flat list* of strings keyed by `markdown:<lineNumber>:<kind>`. No nesting. No HTML. No code. The model can't drop a table because there is no table in its payload — only cells.

## Reassembly rules

1. Read the skeleton (line-by-line record of each source line with its block type and verbatim prefix/suffix).
2. For each skeleton slot that has a payload ID, interpolate the translated value. For slots without an ID, write the verbatim skeleton line.
3. Preserve trailing newline if the source has one.
4. Preserve the source's line ending (LF) — do not convert to CRLF.
5. After write, run the checker: line count must match the English source ±1. If it drifts by more than that, the script refuses to finalize and prints a diff of the offending lines.

## Invariant enforcement (extractor side)

Before a segment is put into the payload, the extractor checks:
- Code spans (` `…` `) → excluded; the span is replaced in the skeleton with the original text.
- Placeholders matching `^\{[a-zA-Z0-9_]+\}$` or `%s` or `%d` → excluded from the payload if they are the ENTIRE cell/item; if mixed with prose, included but the placeholder substring is tagged (see below).
- URLs (`https?://…`, `mailto:`, `vscode-webview://…`) → excluded.
- Emoji → excluded (kept in skeleton verbatim).
- The prefixes `[My Skills]`, `[My Memory]`, `[MySkills]`, `[My CLI]` → kept verbatim at the start of a translated segment; only the prose after the prefix is translated. The extractor splits at the prefix boundary.

For placeholder substrings *inside* a translated segment (e.g. `Delete {0}?`), the extractor emits the payload value with the placeholder wrapped in sentinel chars: `Delete «{0}»?`. The model is instructed to keep `«{0}»` untouched (translate around it). The reassembler strips the sentinels on the way back out. This is the ONLY transformation the model sees; it's a hint, not a structure.

## NLS / bundle specifics

`package.nls.*.json`: the extractor reads the English source as an ordered dict. The payload preserves key order (Python 3.7+ dicts). Translation values become the values; keys stay as the English source keys.

`l10n/bundle.l10n.*.json`: the key IS the English source. The payload is `{"english-source": ""}` (empty value = needs translation). After translation the value is filled. Keys never change. Order: keep the existing lang bundle's order; append new keys at the end.