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
| **Start**  | Begin a project — scaffold new, or learn from an existing one | Create production-ready structures and configs from commit #1. Or analyze an existing codebase's architecture & packages and document it, so you can reuse what works in your own project.          | `start-package`, `start-astro`, `skrapi` | ㅤㅤ✅ |
| **Middle** | Continuous improvement & polish      | Score the project (0–100 health overview), then improve **one dimension at a time** — performance, UI/UX, security, structure, cleanup, code quality, or tidy (file order + comment hygiene) — with a focused plan executed only on your `go`.                                                                                 | `middle`        | ㅤㅤ✅ |
| **End**    | Audit, diagnosis & safe refactoring  | Full architecture & quality analysis. Categorized findings with file-level evidence. Prioritized phased plan executed **only with explicit approval**. Behavior-preserving. Multi-runtime support. | `end`                           | ㅤㅤ✅ |

## Available Skills

Listed in the natural order you'd reach for them — **Start** something new (or study an existing codebase for inspiration), refine it in the **Middle**, and harden it at the **End**.

| Skill                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[start-package](./skills/start-package/README.md)** | _Start_ — Scaffolds a publishable **dual ESM + CJS** TypeScript package with bundled type declarations, a zero-config `tsup` build, and TypeScript pinned to `5.x` so it builds cleanly in both CLI and editor. Generates `package.json`, `tsconfig.json`, tsup config, a smoke test, and `.vscode` settings, then installs, builds, and verifies.<br><br>→ [Full documentation](./skills/start-package/README.md)                                                                            |
| **[start-astro](./skills/start-astro/README.md)** | _Start_ — Scaffolds a new Astro project using the `minimal` template, overlaid with a clean, **scalable** architecture — ready to grow from a portfolio to a full app. Sets up a shared layout, header, footer, pages, light/dark theme toggle, native View Transitions, path alias, and Content Collections out of the box.<br><br>→ [Full documentation](./skills/start-astro/README.md) |
| **[skrapi](./skills/skrapi/README.md)**               | _Start_ — Point it at a project you admire and it maps how that codebase is built into a fixed `SKRAPI/` folder of focused Markdown — architecture, dependencies, and paste-ready prompts — so you can borrow the patterns that fit your own project before you start. Works on any stack (web, mobile, extension, library, monorepo); every description is verified against real code, never guessed from a package name. Multilingual output (🇪🇸 ES · 🇺🇸 EN · 🇨🇳 ZH).<br><br>→ [Full documentation](./skills/skrapi/README.md)                                                                  |
| **[middle](./skills/middle/README.md)**               | _Middle_ — Numbered, on-demand improvers for active development. `0` scores your project or folder with a 0–100 health overview and points at the weakest area; `1–7` each qualify one dimension (⚡ performance · 🎨 ui-ux · 🔒 security · 🏗️ structure · 🧹 cleanup · 🧩 quality · 🗂️ tidy), report evidence-backed findings, and propose a correction plan — executed phase by phase only when you say `go`.<br><br>→ [Full documentation](./skills/middle/README.md)                                                                  |
| **[end](./skills/end/README.md)**                     | _End_ — Understands your project end-to-end. Delivers a clear diagnosis (confirmed bugs, risks, opportunities, technical debt) with concrete references, recommends the right architecture direction for _this_ codebase, and builds an ordered execution plan. Every change happens in an isolated, reviewable phase — it only proceeds when you say `go`, `start`, or `proceed`, and no files are touched during analysis.<br><br>→ [Full documentation & examples](./skills/end/README.md) |

> **Note:** Each skill ships with its own detailed README. The root page gives the high-level overview; dive into `./skills/<skill>/README.md` for deep usage, report examples, and guarantees.

## Installation

Every skill installs the same way — pick the one you need:

```bash
npx skills add bastndev/skills --skill start-package   # Start  — scaffold a TS npm package
npx skills add bastndev/skills --skill start-astro     # Start  — scaffold an Astro project
npx skills add bastndev/skills --skill skrapi          # Start  — study & document any codebase
npx skills add bastndev/skills --skill middle          # Middle — score & improve one dimension
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

- **Start** — `start-package` (scaffold), `start-astro` (Astro scaffold) and `skrapi` (study an existing codebase) ship today; more `start-*` scaffolders are on the way.
- **Middle** — `middle` ships today (health overview + six numbered focus improvers); deeper per-focus tooling is planned.
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
