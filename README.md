<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/logo.webp" width="140" />
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

**Agent skills for the complete project lifecycle.**

Bootstrap new projects with confidence. Iteratively refine and harden them as they grow. Perform deep, safe refactoring when the architecture needs to evolve.

[![skills.sh](https://skills.sh/b/bastndev/skills)](https://skills.sh/bastndev/skills)

## The Three Phases

| Phase      | Purpose                              | Key Capabilities                                                                                                                                                                                   | Example Skills                                   | Status       |
| ---------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ------------ |
| **Start**  | Project initialization & scaffolding | Create production-ready folder structures, initialize frameworks, apply best-practice defaults and configs from commit #1.                                                                         | `start-nextjs`, `start-vite`, `start-fastapi`... | Planned      |
| **Middle** | Continuous improvement & polish      | Enhance UI/UX, harden security, boost performance, clean logic, eliminate dead code, improve maintainability — during active development.                                                          | Targeted enhancers (TBD)                         | Planned      |
| **End**    | Audit, diagnosis & safe refactoring  | Full architecture & quality analysis. Categorized findings with file-level evidence. Prioritized phased plan executed **only with explicit approval**. Behavior-preserving. Multi-runtime support. | `refactor-project` (the `end` skill)             | ✅ Available |

## Available Skills

| Skill                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **[end](./skills/end)** | **`refactor-project`** — Understands your project end-to-end. Delivers a clear diagnosis (confirmed bugs, risks, opportunities, technical debt) with concrete references. Recommends the right architecture direction for _this_ codebase and builds an ordered execution plan. Every change happens in an isolated, reviewable phase. You stay in full control: the skill only proceeds when you say `go`, `start`, or `proceed`. No files are touched during analysis. |

## Installation

```bash
# Add the current skill (End / refactor-project)
npx skills add bastndev/skills --skill end
```

Future skills will be installable the same way:

```bash
npx skills add bastndev/skills --skill start-nextjs
npx skills add bastndev/skills --skill middle-perf   # example name
```

## How the End Skill Works

1. **Analysis only** — It maps entry points, understands structure, reviews relevant code. **Zero modifications.**
2. **Structured report** — Findings are separated into Confirmed Bugs, Risks, Refactoring Opportunities, and Technical Debt — each backed by specific files, functions, and line references.
3. **Tailored plan** — Phases are ordered by real value for your project. Critical issues surface first.
4. **Step-by-step execution** — After you authorize, it performs _one_ phase, reports exactly what changed + validations, then stops and waits for your next `go`.
5. **Safety first** — Never creates tests if none existed. Never adds dependencies without permission. Never overwrites your uncommitted work.

See the complete specification and report format in [skills/end/SKILL.md](./skills/end/SKILL.md).

## Roadmap

- **Start** family: One-command project generators for the most popular stacks.
- **Middle** family: Focused improvement specialists you invoke while building.
- Expanded **End** capabilities and additional language/runtime coverage.

## License

MIT

---

<p align="center">
  <sub>Built for developers who want their AI agents to act with the discipline of a senior engineer.</sub>
</p>
