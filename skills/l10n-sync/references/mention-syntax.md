# `@mention` resolution

Editors (Antigravity, Cursor, VS Code with mentions enabled) expand `@path` tokens before the agent sees the message. The agent receives the expanded text — typically the path literally, sometimes with surrounding backticks or whitespace. Resolve as follows.

## Rules

1. **Strip wrapping quotes/backticks/whitespace** before parsing.
2. **Resolve relative to the workspace root**, never the home directory. `@public/docs/` → `<workspace>/public/docs/`. `~/` is NOT home — treat it as a literal `~` segment and ask the user.
3. **Trailing `/` means directory**. A directory mention in a `.md` sync message is the *target dir* for the mirror, NOT the source.
4. **No trailing `/` and ends in `.md`** → English source for workflow A.
5. **`package.nls.json`** → workflow B source.
6. **`l10n/` or `bundle.l10n.en.json`** → workflow C source.
7. **Multiple `@<file>.md` mentions** → the first is the English source; treat any additional `.md` mentions as "also sync these" and run A once per file.
8. **Multiple directory mentions** → ask once: "You mentioned several folders. Which is the target dir for the mirror?" Do not guess.
9. **Path doesn't exist** → ask once. Do not silently create from a wrong guess.

## Examples

| user message                                                              | source              | target dir          | workflow |
|---------------------------------------------------------------------------|---------------------|----------------------|----------|
| `@public/docs/ use @src/.../default/README.md as a reference`              | …/default/README.md | `public/docs/`       | A        |
| `update @src/foo/README.md`                                               | src/foo/README.md   | `public/docs/` (default) | A   |
| `sync @package.nls.json`                                                  | package.nls.json    | —                    | B        |
| `@l10n/`                                                                   | bundle.l10n.en.json | —                    | C        |
| `translate everything` (no `@`)                                            | ask once            | `public/docs/` (default) | A + ask |

## What NOT to do

- Do not treat `@public/docs/` as the English source — directories are targets.
- Do not expand `~` to home. If a path starts with `~`, ask.
- Do not run workflow A without an explicit `.md` source — even if the user named only a target dir.
- Do not run `find`/`rg` to discover sources; only use what the user named.