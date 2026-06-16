<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/github/image/xyz/end.webp" width="150" />
</p>

<h1 align="center">[End] / Refactor Project</h1>

<p align="center">
  <strong>End</strong> — The disciplined refactoring skill
</p>

<p align="center">
  <a href="../../README.md">← Back to Start / Middle / [End]</a>
</p>

---

Analyzes your project, builds a prioritized refactoring plan, and applies every change **only with your explicit authorization**. Zero guessing. Zero rushing. Zero edits until you say `go`.

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

## Install

```bash
npx skills add bastndev/skills --skill end
```

## How It Works

1. **Analysis** — Maps entry points, reads only relevant source. Nothing is touched.
2. **Diagnosis** — Structured report: Confirmed Bugs (with severity), Risks, Refactoring Opportunities, Technical Debt + an architecture recommendation and ordered plan.
3. **You authorize** — Say `go`, `start`, or `proceed` to begin. It executes **one phase**, reports what changed + validations, then stops.
4. **Repeat** — Phase by phase, until done. Closes with a full summary.

## Guarantees

- No files modified during analysis
- No new tests created if the project had none
- No dependencies added without permission
- Uncommitted work is never overwritten

## Finding Format

```
src/api/handler.ts:processRequest — missing input validation on userId
  → can lead to unauthorized data access
  → add schema validation [severity: critical → phase 1]
```

---

→ Full spec & rules: [SKILL.md](./SKILL.md)

<div align="center">
  <sub>Built for developers who want their AI agents to act with the discipline of a senior engineer.</sub>
  <br><br>
  <sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="https://github.com/bastndev/skills/blob/main/LICENSE">MIT</a></sub>
</div>