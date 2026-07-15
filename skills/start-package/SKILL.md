---
name: start-package
description: Scaffold or refresh a minimal Node.js TypeScript library with Bun, TypeScript 7, tsdown, strict type checking, dual ESM/CJS outputs, declaration files, and package validation. Use when creating a new npm package or library from this known-good base. Generate a project-specific NOTES.md with manual release guidance, but never generate .github/workflows/publish.yml or publish the package unless the user separately requests it.
license: Complete terms in LICENSE.txt
metadata:
  author: bastndev
  version: "1.1.0"
---

# TypeScript package scaffold

Create a minimal Node.js library from the files in `assets/template/`. Keep the generated project small and preserve the dual ESM/CJS package contract.

## Required inputs

Infer values when they are already clear. Otherwise ask only for the missing values.

- `NAME`: npm package name, such as `my-lib` or `@scope/my-lib`.
- `PROJECT_NAME`: repository/folder name. Default to the unscoped part of `NAME`.
- `DESCRIPTION`: one-line package description. Default to `A minimal TypeScript library package with ESM, CommonJS, and declaration outputs.`
- `AUTHOR`: default to `Gohit X (bastndev)`.
- `NPM_OWNER`: npm organization or user. Default to `bastndev`.
- `REPO`: HTTPS repository URL without a trailing `.git`. Default to `https://github.com/bastndev/{{PROJECT_NAME}}`.
- `HOMEPAGE`: default to `https://gohit.xyz/package/{{NAME}}`.
- `YEAR`: current year.

## Scaffold procedure

1. Inspect the target directory before writing. Do not overwrite unrelated or user-modified files without explicit approval.
2. Copy every file from `assets/template/`, including `.gitignore`, into the target directory.
3. Replace all `{{NAME}}`, `{{PROJECT_NAME}}`, `{{DESCRIPTION}}`, `{{AUTHOR}}`, `{{NPM_OWNER}}`, `{{REPO}}`, `{{HOMEPAGE}}`, and `{{YEAR}}` placeholders.
4. Confirm no placeholder remains:

   ```bash
   rg -n '\{\{[A-Z_]+\}\}' .
   ```

5. Install dependencies with `bun install` and keep the generated `bun.lock`. Do not generate `package-lock.json`.
6. Run `bun run check`. Do not report success unless type-checking, the ESM/CJS build, `attw`, `publint`, and the smoke test all pass.
7. Run `git diff --check` when the target is a Git repository.

## Release boundary

- Generate `NOTES.md`. It is a project-named manual guide whose placeholders must be replaced.
- Do not execute or automate any command described in `NOTES.md` unless the user separately asks.
- Never create `.github/workflows/publish.yml` as part of this skill.
- Never create another publish workflow or CI substitute unless the user separately asks.
- Never publish, tag, push, log in to npm, or change npm trusted-publishing settings unless the user separately asks.

## Base guarantees

- Bun is declared through `packageManager` and used for development scripts.
- TypeScript 7 performs strict, no-emit type checking.
- tsdown emits ESM, CJS, `.d.ts`, and `.d.cts` outputs.
- `isolatedDeclarations` enables fast declaration generation.
- `publint` runs in strict mode and `attw` failures are errors.
- `bun run test` is self-contained: it builds before loading both package export conditions.
- The smoke test imports through `NAME`, so renaming mistakes fail visibly.
- `sideEffects: false` is appropriate only for side-effect-free libraries. Change it when the package intentionally performs import-time work or ships side-effectful assets.

## Template inventory

- `assets/template/package.json`
- `assets/template/tsconfig.json`
- `assets/template/tsdown.config.ts`
- `assets/template/src/index.ts`
- `assets/template/test/smoke.mjs`
- `assets/template/README.md`
- `assets/template/NOTES.md`
- `assets/template/.gitignore`
- `assets/template/LICENSE`

Do not add `.vscode/settings.json`, a publishing workflow, source maps, linting, a test framework, or runtime dependencies unless the user asks for them.
