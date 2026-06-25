<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/github/icons/middle.webp" width="150" />
</p>

<h1 align="center">[Skrapi] / Architecture Analyzer</h1>

<p align="center">
  <strong>Skrapi</strong> — The codebase documentation skill
</p>

<p align="center">
  <a href="../../README.md">← Back to Start / Middle / [End]</a>
</p>

---

Analyzes any project — web, mobile, browser extension, npm package, or monorepo, in any JS/TS stack — and writes a fixed `SKRAPI/` folder of focused Markdown: how it's built, what it depends on, and paste-ready prompts to rebuild the same patterns. Every description is verified against real code, never guessed from a package name.

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

## Install

```bash
npx skills add bastndev/skills --skill skrapi
```

## How It Works

1. **Pick a language** — Asks once: 🇪🇸 ES · 🇺🇸 EN · 🇨🇳 ZH. No answer → defaults to EN.
2. **Inspect** — Reads `package.json`, config files, and the directory tree to detect the real stack before writing anything.
3. **Classify** — Loads the matching reference guide (web, mobile, extension, library) so analysis fits the project type, not generic boilerplate.
4. **Generate** — Writes `ARCHITECTURE.md`, `PACKAGES.md`, and `PROMPT.md`, each grounded in actual findings from the code.

## Guarantees

- Confirms every dependency by its real usage — never from the name alone
- Fixed, recognizable `SKRAPI/` folder — never scattered loose next to your code
- No padding files — extras like `SKILLS.md` appear only when the project earns them
- Skips `node_modules`, build output, and lockfiles automatically

## Output Structure

```
SKRAPI/
├── ARCHITECTURE.md  — Stack, structure, rendering, data flow, Mermaid diagram
├── PACKAGES.md      — Each dependency's real role + a "common needs" checklist
├── PROMPT.md        — Paste-ready prompts to rebuild the architecture & packages
└── SKILLS.md        — Custom AI skills in the repo (only when others exist)
```

---

→ Full spec & rules: [SKILL.md](./SKILL.md)

<div align="center">
  <sub>Built for developers who want their AI agents to document codebases with the rigor of a senior engineer.</sub>
  <br><br>
  <sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="https://github.com/bastndev/skills/blob/main/LICENSE">MIT</a></sub>
</div>
