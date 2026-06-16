<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/logo.webp" width="180" />
</p>

<h1 align="center">Start / Middle / End</h1>

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

## The Three Phases

| Phase      | Purpose                              | Key Capabilities                                                                                                                                                                                   | Example Skills                                   | Status  |
| ---------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ------- |
| **Start**  | Project initialization & scaffolding | Create production-ready folder structures, initialize frameworks, apply best-practice defaults and configs from commit #1.                                                                         | `start-nextjs`, `start-vite`, `start-fastapi`... | Planned     |
| **Middle** | Continuous improvement & polish      | Enhance UI/UX, harden security, boost performance, clean logic, eliminate dead code, improve maintainability — during active development.                                                          | Targeted enhancers (TBD)                         | Planned     |
| **End**    | Audit, diagnosis & safe refactoring  | Full architecture & quality analysis. Categorized findings with file-level evidence. Prioritized phased plan executed **only with explicit approval**. Behavior-preserving. Multi-runtime support. | `refactor-project` (the `end` skill)             | ✅ Available |

## Available Skills

| Skill                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **[end](./skills/end/README.md)** | **`refactor-project`** — Understands your project end-to-end. Delivers a clear diagnosis (confirmed bugs, risks, opportunities, technical debt) with concrete references. Recommends the right architecture direction for _this_ codebase and builds an ordered execution plan. Every change happens in an isolated, reviewable phase. You stay in full control: the skill only proceeds when you say `go`, `start`, or `proceed`. No files are touched during analysis.<br><br>→ [Full documentation & examples](./skills/end/README.md) |

> **Note:** Each skill ships with its own detailed README. The root page gives the high-level overview; dive into `./skills/<skill>/README.md` for deep usage, report examples, and guarantees.

## Installation

```bash
# Install the End skill (refactor-project)
npx skills add bastndev/skills --skill end
```

Additional skills (once released) are installed the same way:

```bash
npx skills add bastndev/skills --skill start-nextjs
```

## How the End Skill Works

1. **Analysis first** — Maps entry points and understands the project. **Zero files are modified.**
2. **Structured report** — Clear findings in four categories (Confirmed Bugs with severity, Risks, Refactoring Opportunities, Technical Debt) + an architecture recommendation and ordered plan. All items include concrete file + line references.
3. **You authorize every phase** — It executes **exactly one phase** at a time. After each phase you get a precise summary of changes, validations performed, and the list of remaining phases.
4. **Full control & safety** — Never creates tests if the project had none. Never adds dependencies or changes the package manager without permission. Respects your uncommitted work and always preserves current behavior unless fixing a justified bug.

For the complete workflow, exact report formats (including the required closing blocks), architecture decision rules, and all safety guarantees, read the dedicated skill documentation:

→ **[End – Refactor Project](./skills/end/README.md)**

The full internal specification lives in [skills/end/SKILL.md](./skills/end/SKILL.md).

## Roadmap

- **Start** skills — One-command project scaffolding for popular stacks (Next.js, Vite, FastAPI, etc.)
- **Middle** skills — Focused, on-demand improvers (performance, security, UX, dead-code removal, etc.)
- **End** expansions — More runtimes, additional specialized refactoring modes, and utilities

Each skill will have its own dedicated documentation (like the current [End – Refactor Project](./skills/end/README.md)).

---

<br>

<div align="center">
  <p align="center">
  <sub>Built for developers who want their AI agents to act with the discipline of a senior engineer.</sub>
</p>

_If you find any bugs or have feedback, feel free to [open an issue](https://github.com/bastndev/skills/issues/new)._

<sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a></sub>

</div>
