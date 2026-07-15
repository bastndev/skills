# {{NAME}} — First Publish

This file is a manual guide. The package skill does not execute these commands or create the workflow described below.

```bash
# Login (only once)
npm login --auth-type=web

# Verify session
npm whoami

# Check if the package name is available
npm view {{NAME}}

# Review the files that will be published
npm pack --dry-run

# Publish
npm publish
```

<!-- -- -- --- ---- --- TODO: Update --- --- --- -- - -->

# Verify `{{NAME}}` NPM package ✅

## 1 — npm Token **Settings**

```text
https://www.npmjs.com/package/{{NAME}}/access
```

| Field | Value |
| --- | --- |
| Organization or user | `{{NPM_OWNER}}` |
| Repository | `{{PROJECT_NAME}}` |
| Workflow filename | `publish.yml` |
| Environment name | None |
| Allowed actions | `Allow npm publish` |

Select **Set up connection**.

## 2 — Create the workflow manually

Create `.github/workflows/publish.yml` yourself when you are ready:

```yaml
name: Publish

on:
  push:
    tags:
      - "v*"

jobs:
  publish:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: read

    steps:
      - uses: actions/checkout@v4

      - uses: oven-sh/setup-bun@v2
        with:
          bun-version: latest

      - name: Install dependencies
        run: bun install

      - name: Build
        run: bun run build

      - uses: actions/setup-node@v4
        with:
          node-version: "22"
          registry-url: "https://registry.npmjs.org"

      - name: Update npm
        run: npm install -g npm@latest

      - name: Publish with provenance
        run: npm publish --provenance --access public
```

Commit and push the workflow to `main` manually.

## 3 — Publish and deploy

```bash
git checkout main
git pull
```

```bash
npm version patch
git push origin main
git push origin v0.1.0
```

> Use the tag created by `npm version`; update the example tag when the version changes.
