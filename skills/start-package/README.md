<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/refs/heads/main/public/github/image/icons/start.webp" width="150" />
</p>

<h1 align="center">[Start] / npm-package-starter</h1>

<p align="center">
  <strong>Start Package</strong> — Scaffold a zero-config, dual ESM/CJS TypeScript npm package
</p>

<p align="center">
  <a href="../../README.md">← Back to Start / Middle / [End]</a>
</p>

---

Scaffolds a publishable TypeScript library that ships as a **dual ESM + CJS** package with **bundled type declarations** and (optionally) **zero runtime dependencies**. Uses the exact toolchain that builds cleanly without surprises.

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

## Install

```bash
npx skills add bastndev/skills --skill start-package
```

## Features

- **Dual Build** — ESM and CJS outputs via `tsup`.
- **Fully Typed** — Bundled `.d.ts` and `.d.cts` declarations.
- **No Surprises** — TypeScript pinned strictly to `5.x`.
- **Zero Runtime Deps** (Optional) — Inlines dependencies easily.
- **Pre-configured** — Includes `tsconfig.json`, `package.json`, unit tests, and `.vscode` settings.

---

→ Full spec & rules: [SKILL.md](./SKILL.md)

<div align="center">
  <sub>Built for developers who want a robust foundation for their new npm packages.</sub>
  <br><br>
  <sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="https://github.com/bastndev/skills/blob/main/LICENSE">MIT</a></sub>
</div>