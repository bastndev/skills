---
name: start-package
description: Scaffold a new dual ESM/CJS TypeScript npm package with the proven, known-good toolchain — Bun as the package manager/runtime, zero-config build, bundled types, and TypeScript pinned to 5.x. Use when starting, creating, or bootstrapping a new npm package, library, or "packete" from scratch. Generates package.json, tsconfig.json, tsup config, a smoke test, .gitignore and .vscode settings, then installs, builds and verifies.
license: Complete terms in LICENSE.txt
metadata:
  author: bastndev
  version: "1.1.0"
---

# npm-package-starter

Scaffolds a publishable TypeScript library that ships as a **dual ESM + CJS** package with **bundled type declarations** and (optionally) **zero runtime dependencies**, using the exact toolchain that builds cleanly without surprises.

## When to use

The user wants to start a new package: "create/scaffold/bootstrap a new npm package / library / packete", "set up a TS package", or they have an empty repo and want the base files.

---

## ⚠️ The one rule that prevents the known breakage

**Pin TypeScript to 5.x** (`"typescript": "^5"`). Do **not** install an unpinned `typescript` — it floats to 6.x and breaks the build.

**Why:** `tsup` hardcodes `baseUrl: "."` when generating `.d.ts` files (`node_modules/tsup/dist/rollup.js`). TypeScript **6.0** turned `baseUrl` into a removal-bound deprecation that errors (`TS5101`) unless you set `"ignoreDeprecations": "6.0"`. But editors bundle their own (often older) TypeScript that doesn't recognize the value `"6.0"` → permanent red squiggle in the IDE even though the CLI build passes. Staying on TS **5.x** sidesteps the whole thing: no flag needed, clean in both CLI and editor.

> Revisit TS 6+ only once `tsup` stops injecting `baseUrl`. Until then: TS 5.x.

**Also** pin the editor to the workspace TypeScript via `.vscode/settings.json` (included below) so the IDE and CLI always use the same compiler.

### Known-good versions (tested)

| Tool | Range to use | Verified |
| --- | --- | --- |
| typescript | `^5` (must be < 6) | 5.9.3 |
| tsup | `^8` | 8.5.1 |
| @types/node | `^22` | — |
| node (engines) | `>=20` | 25.x |
| bun | latest | 1.3.4 |

---

## Procedure

1. **Gather inputs** (ask only if not obvious; otherwise use the defaults):
   - `NAME` — npm package name (bare like `my-lib`, or scoped `@bastndev/my-lib`)
   - `DESCRIPTION` — one line
   - `AUTHOR` — default `Gohit X (bastndev)`
   - `REPO` — default `https://github.com/bastndev/{NAME}`
   - `HOMEPAGE` — default `https://gohit.xyz/package/{NAME}`
   - `YEAR` — current year
2. **(Optional) check the name is free:** `npm view {NAME} version` → a `404` means it's available.
3. **Create the files** in the "Templates" section, substituting `{{PLACEHOLDERS}}`. Scaffold into the current directory unless the user gives a target folder.
4. **Install:** `bun install` (the template already pins the dev tools). Commit the generated `bun.lock` — it is the lockfile; do **not** generate a `package-lock.json`.
5. **Build + test + verify:**
   ```bash
   bunx tsc --noEmit    # type-check (must be exit 0)
   bun run build        # tsup → dist/ (ESM + CJS + .d.ts/.d.cts)
   bun run test         # smoke test loads BOTH builds
   npm pack --dry-run   # inspect tarball contents + size
   ```
   Do not report success until `tsc`, `build`, and `test` all pass.
6. **Do not publish** unless asked. When the user is ready: `npm login` → `npm whoami` → `npm publish`.

---

## Templates

### `package.json`

```json
{
  "name": "{{NAME}}",
  "version": "0.1.0",
  "description": "{{DESCRIPTION}}",
  "type": "module",
  "main": "./dist/index.cjs",
  "module": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "import": {
        "types": "./dist/index.d.ts",
        "default": "./dist/index.js"
      },
      "require": {
        "types": "./dist/index.d.cts",
        "default": "./dist/index.cjs"
      }
    }
  },
  "files": [
    "dist"
  ],
  "sideEffects": false,
  "scripts": {
    "build": "tsup",
    "clean": "rm -rf dist",
    "prepublishOnly": "bun run build",
    "test": "bun test/smoke.mjs"
  },
  "keywords": [],
  "author": "{{AUTHOR}}",
  "license": "MIT",
  "homepage": "{{HOMEPAGE}}",
  "repository": {
    "type": "git",
    "url": "git+{{REPO}}.git"
  },
  "bugs": {
    "url": "{{REPO}}/issues"
  },
  "publishConfig": {
    "access": "public"
  },
  "engines": {
    "node": ">=20"
  },
  "devDependencies": {
    "@types/node": "^22",
    "tsup": "^8",
    "typescript": "^5"
  }
}
```

> `files` is an allowlist: only `dist/` (plus `package.json`, `README`, `LICENSE`, which npm always includes) ships. It overrides `.gitignore`, so `dist/` publishes even though it's git-ignored. Add any runtime asset folders here (e.g. `"assets"`, `"dictionaries"`).

### `tsconfig.json`

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "lib": ["ES2022"],
    "types": ["node"],
    "declaration": true,
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "verbatimModuleSyntax": true,
    "isolatedModules": true,
    "outDir": "dist",
    "rootDir": "src"
  },
  "include": ["src"]
}
```

> No `ignoreDeprecations` here — that's only needed on TS 6.x and is the very thing that caused the IDE error. On TS 5.x this file is clean.

### `tsup.config.ts`

```ts
import { defineConfig } from 'tsup';

export default defineConfig({
  entry: { index: 'src/index.ts' },
  format: ['esm', 'cjs'],
  dts: true,
  clean: true,
  sourcemap: false, // leaner published tarball
  target: 'node20',
  // import.meta.url works in the CJS output and __dirname in the ESM output —
  // needed if you resolve bundled asset paths relative to the module.
  shims: true,
  // To ship ZERO runtime dependencies, inline everything (node: builtins stay
  // external). This also lets a CJS host require() the package without ESM
  // gymnastics, even when a dependency is ESM-only:
  // noExternal: [/.*/],
  outExtension({ format }) {
    return { js: format === 'esm' ? '.js' : '.cjs' };
  },
});
```

### `src/index.ts`

```ts
export function hello(name: string): string {
  return `Hello, ${name}!`;
}
```

### `test/smoke.mjs`

```js
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';

import { hello } from '../dist/index.js';

// ESM build
assert.equal(hello('world'), 'Hello, world!');

// The CJS build must load and expose the same API.
const require = createRequire(import.meta.url);
const cjs = require('../dist/index.cjs');
assert.equal(typeof cjs.hello, 'function', 'CJS build exports hello');

console.log('✅ smoke test passed');
```

### `.gitignore`

```
node_modules/
dist/
*.tsbuildinfo
.DS_Store
npm-debug.log*
*.tgz
```

### `.vscode/settings.json`

```json
{
  "typescript.tsdk": "node_modules/typescript/lib"
}
```

> `typescript.tsdk` alone is enough to point the IDE at the workspace compiler. Do **not** add `typescript.enablePromptUseWorkspaceTsdk` — it triggers a "use workspace TypeScript?" popup on every IDE launch, which is unnecessary noise when `typescript.tsdk` is already set.

### `LICENSE` (MIT)

```
MIT License

Copyright (c) {{YEAR}} {{AUTHOR}}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Optional patterns

**Bundle runtime assets (data files):** put them in a folder (e.g. `assets/`), add it to `files`, and resolve paths relative to the build with:
```ts
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
const PACKAGE_ROOT = join(dirname(fileURLToPath(import.meta.url)), '..'); // dist/ -> root
```
This works in both ESM and CJS thanks to `shims: true`.

**Inline a dependency for zero deps:** add it as a `devDependency`, set `noExternal: [/.*/]` in tsup, and it gets compiled into `dist/`. If you do this, preserve the inlined library's license notice (e.g. append a short "Third-party software" section to `LICENSE`).

---

## Gotchas checklist (verify before declaring done)

- [ ] `typescript` pinned to `^5` (NOT 6.x) — the #1 rule
- [ ] `.vscode/settings.json` points the IDE at the workspace TS (`typescript.tsdk` only)
- [ ] `exports` map has per-condition `types` for `import` and `require`
- [ ] `files` allowlist includes `dist` + any asset folders
- [ ] `sourcemap: false` for a leaner publish
- [ ] `bun.lock` committed; no `package-lock.json`
- [ ] `bunx tsc --noEmit`, `bun run build`, and `bun run test` all pass
- [ ] If a dependency was inlined: its license is attributed in `LICENSE`
- [ ] Not published unless explicitly requested
