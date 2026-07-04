# File-kind detection

Pick the workflow from the source path the user gives.

| source path pattern                               | workflow | targets                                |
|---------------------------------------------------|----------|----------------------------------------|
| `**/*.md`                                          | A        | `docs/{lang}/README.md`                |
| `package.nls.json`                                | B        | `package.nls.{lang}.json`               |
| `l10n/bundle.l10n.en.json`                         | C        | `l10n/bundle.l10n.{lang}.json`          |
| `**/*.nls.json` (not `package.nls.json`)          | B        | same dir, swap suffix to `.{lang}.json` |
| `l10n/bundle.l10n.{lang}.json` (single lang given)| C        | that one lang only                      |

If the user gives a path that matches none of these, ask in chat: "I can sync `.md` mirrors, `package.nls.*.json`, or `l10n/bundle.l10n.*.json`. Which do you mean?"

If the user says "all", run A, B, and C in order. Ask once for the `.md` source path (there is no canonical default — the workspace has several READMEs). For B and C the sources are fixed (`package.nls.json`, `l10n/bundle.l10n.en.json`).