# File-kind detection

Pick the workflow from the source the user gives. `@mentions` are resolved first (see `mention-syntax.md`).

| source                              | workflow | target dir / files                                  |
|-------------------------------------|----------|------------------------------------------------------|
| `@<file>.md`                        | A        | `<target_dir>/{lang}/README.md`                      |
| `@<folder>/` (directory mention)    | A target | overrides the default target dir for `.md` mirrors   |
| `@package.nls.json`                 | B        | `package.nls.{lang}.json` (same dir)                 |
| `@l10n/` or `@bundle.l10n.en.json`  | C        | `l10n/bundle.l10n.{lang}.json`                       |

### `.md` target dir resolution (workflow A)

1. The folder named via `@<folder>/` — use it verbatim (strip trailing `/`).
2. Else `public/docs/` if it exists in the workspace.
3. Else `docs/` (create on first run).

If the user gives a `.md` source but no folder, and `public/docs/` does not exist either, ask once: "Which folder should the mirrors go into? (default: `public/docs/`)"

### "all" mode

If the user says "all" without further specifics, run A, B, C in order. You still need a `.md` source for A — ask once if not given. For B and C the sources are fixed (`package.nls.json`, the English l10n bundle).

### Other paths

If the user gives a path that matches none of the patterns above, ask in chat: "I can sync `.md` mirrors, `package.nls.*.json`, or `l10n/bundle.l10n.*.json`. Which do you mean?"