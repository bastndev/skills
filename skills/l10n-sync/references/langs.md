# Filename-suffix → language map

The language is read from the filename suffix: `README_<SUFFIX>.md`, or for
JSON bundles `package.nls.<suffix>.json` (VS Code locale codes like `pt-br`,
`zh-cn` are rows in this same map). The suffix is matched case-insensitively
(`README_AR.md`, `readme_ar.md`, `README-ar.md` all → Arabic). This map is **extensible and non-gating**: files drive the sync,
not this list. To support a new language the user just creates the file — if its
suffix isn't below, the script still processes it and asks you to infer the
language from the code.

| suffix        | language              | rtl |
|---------------|-----------------------|-----|
| ar            | Arabic                | yes |
| de            | German                | no  |
| es            | Spanish               | no  |
| fr            | French                | no  |
| hi            | Hindi                 | no  |
| ja            | Japanese              | no  |
| ko            | Korean                | no  |
| pt            | Portuguese            | no  |
| pt-br         | Brazilian Portuguese  | no  |
| ru            | Russian               | no  |
| vi            | Vietnamese            | no  |
| zh / zh-cn    | Simplified Chinese    | no  |
| zh-tw         | Traditional Chinese   | no  |
| it, nl, tr, pl, id, th, uk, cs, ro, el, sv, da, fi, no, hu, bn, ta, ms, fil | (as named) | no |
| he, fa, ur    | Hebrew / Persian / Urdu | yes |

The authoritative copy of this map lives in `scripts/l10n.py` (`LANG_NAMES`,
`RTL`). Add rows there when you add rows here.

**RTL languages** (`ar`, `he`, `fa`, `ur`): write natural right-to-left prose,
keep code / URLs / placeholders left-to-right, and add no bidi control marks
unless the English source already has them.
