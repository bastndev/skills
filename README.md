<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/logo.webp" width="180" />
</p>

<h1 align="center">[Start] / Middle / [End]</h1>

<p align="center">
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_ES.md">Español 🇪🇸</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_ZH.md">中文 🇨🇳</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_DE.md">Deutsch 🇩🇪</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_FR.md">Français 🇫🇷</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_JA.md">日本語 🇯🇵</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_KO.md">한국어 🇰🇷</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_PT.md">Português 🇧🇷</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_RU.md">Русский 🇷🇺</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_VI.md">Tiếng Việt 🇻🇳</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_HI.md">हिन्दी 🇮🇳</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_AR.md">العربية 🇸🇦</a><span>...</span>
</p>

<br>

<p align="center">
  Bootstrap new projects with confidence. Iteratively refine and harden them as they grow. Perform deep, safe refactoring when the architecture needs to evolve.
</p>

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

```
npx skills add bastndev/skills
```

<br>

## The Three Phases

| Phase      | Purpose                              | Key Capabilities                                                                                                                                                                                   | Example Skills                  | Status |
| ---------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------ |
| **Start**  | Project initialization & scaffolding | Create production-ready folder structures, initialize frameworks, apply best-practice defaults and configs from commit #1.                                                                         | `start-package` _(more coming)_ | ㅤㅤ✅ |
| **Middle** | Understand, document & improve       | Analyze any codebase and document it into a portable folder of focused Markdown. Enhance UI/UX, harden security, boost performance, and clean logic during active development.                     | `skrapi`                        | ㅤㅤ✅ |
| **End**    | Audit, diagnosis & safe refactoring  | Full architecture & quality analysis. Categorized findings with file-level evidence. Prioritized phased plan executed **only with explicit approval**. Behavior-preserving. Multi-runtime support. | `end`                           | ㅤㅤ✅ |

## Available Skills

Listed in the natural order you'd reach for them — **Start** a project, understand it in the **Middle**, harden it at the **End**.

| Skill                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[start-package](./skills/start-package/README.md)** | _Start_ — Scaffolds a publishable **dual ESM + CJS** TypeScript package with bundled type declarations, a zero-config `tsup` build, and TypeScript pinned to `5.x` so it builds cleanly in both CLI and editor. Generates `package.json`, `tsconfig.json`, tsup config, a smoke test, and `.vscode` settings, then installs, builds, and verifies.<br><br>→ [Full documentation](./skills/start-package/README.md)                                                                            |
| **[skrapi](./skills/skrapi/README.md)**               | _Middle_ — Analyzes any codebase (web, mobile, extension, library, monorepo) and writes a fixed `SKRAPI/` folder of focused Markdown — architecture, dependencies, and paste-ready prompts. Every description is verified against real code, never guessed from a package name. Multilingual output (🇪🇸 ES · 🇺🇸 EN · 🇨🇳 ZH).<br><br>→ [Full documentation](./skills/skrapi/README.md)                                                                                                         |
| **[end](./skills/end/README.md)**                     | _End_ — Understands your project end-to-end. Delivers a clear diagnosis (confirmed bugs, risks, opportunities, technical debt) with concrete references, recommends the right architecture direction for _this_ codebase, and builds an ordered execution plan. Every change happens in an isolated, reviewable phase — it only proceeds when you say `go`, `start`, or `proceed`, and no files are touched during analysis.<br><br>→ [Full documentation & examples](./skills/end/README.md) |

> **Note:** Each skill ships with its own detailed README. The root page gives the high-level overview; dive into `./skills/<skill>/README.md` for deep usage, report examples, and guarantees.

## Installation

Every skill installs the same way — pick the one you need:

```bash
npx skills add bastndev/skills --skill start-package   # Start  — scaffold a TS npm package
npx skills add bastndev/skills --skill skrapi          # Middle — analyze & document a codebase
npx skills add bastndev/skills --skill end             # End    — audit & safely refactor
```

## How the End Skill Works

`end` is the most mature skill in the suite. Here's its workflow end to end:

1. **Analysis first** — Maps entry points and understands the project. **Zero files are modified.**
2. **Structured report** — Clear findings categorized into Bugs (with severity), Debt/Risks, and Suggestions, plus a scored health overview, an architecture recommendation, and an ordered plan — all backed by concrete file + line references.
3. **You authorize every phase** — It executes **exactly one phase** at a time. After each phase you get a precise summary of changes, validations performed, and the list of remaining phases.
4. **Full control & safety** — Never creates tests if the project had none. Never adds dependencies or changes the package manager without permission. Respects your uncommitted work and always preserves current behavior unless fixing a justified bug.

For the complete workflow, exact report formats (including the required closing blocks), architecture decision rules, and all safety guarantees, read the dedicated skill documentation:

→ **[End – Refactor Project](./skills/end/README.md)**

The full internal specification lives in [skills/end/SKILL.md](./skills/end/SKILL.md).

## Roadmap

- **Start** — `start-package` ships today; more `start-*` scaffolders (frameworks & stacks) are on the way.
- **Middle** — `skrapi` ships today; focused, on-demand improvers (performance, security, UX, dead-code removal) are planned.
- **End** — `end` ships today; more runtimes, additional specialized refactoring modes, and utilities are planned.

Each skill ships with its own dedicated documentation (like the current [End – Refactor Project](./skills/end/README.md)).

---

<br>

<div align="center">
  <p align="center">
  <sub>Built for developers who want their AI agents to act with the discipline of a senior engineer.</sub>
</p>

_If you find any bugs or have feedback, feel free to [open an issue](https://github.com/bastndev/skills/issues/new)._

<sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a></sub>

</div>
