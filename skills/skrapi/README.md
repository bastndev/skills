<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/github/icons/start.webp" width="150" />
</p>

<h1 align="center">[Architecture Analyzer] / Documentation Generator</h1>

<p align="center">
  <strong>Architecture Analyzer</strong> — The codebase documentation skill
</p>

<p align="center">
  <a href="../../README.md">← Back to Start / Middle / [End]</a>
</p>

---

Analyzes any software project's architecture and produces a folder of focused Markdown files covering architecture and packages/dependencies. Web, mobile, browser extension, npm package, monorepo — any JS/TS stack or other languages if needed.

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

## Install

```bash
npx skills add bastndev/skills --skill architecture-analyzer
```

## How It Works

1. **Inspect** — Reads package.json, config files, directory tree. Detects the stack before writing anything.
2. **Classify** — Picks the matching reference guide (web, mobile, extension, library) for project-specific analysis.
3. **Generate** — Writes `architecture.md` and `packages.md` with real findings from the codebase, not generic observations.
4. **Complete** — Optional `recommendations.md` and `SKILLS.md` only when they earn their place.

## Guarantees

- Never describes dependencies from their name alone — confirms actual usage
- No padding files — only generates what the project justifies
- Supports ES, EN, ZH output languages
- Skips node_modules, build output, and lockfiles automatically

## Output Structure

```
<project-slug>-architecture/
├── architecture.md     — Stack, structure, routing, data flow, Mermaid diagrams
├── packages.md         — Dependencies with project-specific descriptions
├── recommendations.md  — Actionable patterns to borrow (only when applicable)
└── SKILLS.md           — Custom AI skills found in the repo (only if they exist)
```

---

→ Full spec & rules: [SKILL.md](./SKILL.md)

<div align="center">
  <sub>Built for developers who want their AI agents to document codebases with the rigor of a senior engineer.</sub>
  <br><br>
  <sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="https://github.com/bastndev/skills/blob/main/LICENSE">MIT</a></sub>
</div>
