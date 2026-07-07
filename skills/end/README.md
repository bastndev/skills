<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/github/icons/end.webp" width="150" />
</p>

<h1 align="center">[End] / Refactor Project</h1>

<p align="center">
  <strong>The disciplined refactoring skill</strong>
</p>

<p align="center">
  <a href="../../README.md">← Back to Start / Middle / [End]</a>
</p>

---

Analyze any project, generate a prioritized refactoring plan, and apply changes **only after your approval**.

**Nothing is modified until you say:** `go`

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

## Install

```bash
npx skills add bastndev/skills --skill end
```

## Health Overview

Every analysis starts with a project health score.

| Score | Meaning |
| ----- | ------- |
| **0–40** | 🚨 Critical — hard to maintain, risky to change |
| **40–60** | 🔴 Heavy debt — significant refactoring recommended |
| **60–70** | 🟡 Needs improvement — address debt before production |
| **70–80** | 🟢 Production-ready — solid and maintainable |
| **80–90** | ⭐ Excellent — clean architecture |
| **90–100** | 🏆 Outstanding — reference-grade codebase |

Example:

```text
📊 my-project Health Overview — 74 / 100 🟢

🔴 Bugs 1    🟡 Debt/Risks 3    🟢 Suggestions 2

🏗️ Architecture     7/10
🧩 Maintainability  6/10
⚡ Performance       8/10
🔒 Security          5/10
📚 Documentation     7/10
```

`my-project` is replaced with your project's real name (from its manifest, or the folder name).

## Workflow

1. Analyze the project (read-only).
2. Report bugs, risks, technical debt, and opportunities.
3. Generate a phased refactoring plan.
4. Wait for `go`.
5. Execute **one phase**, validate it, stop, and wait again.
   (Say `run all phases` to execute the whole plan, with a report after each phase.)

## Guarantees

- ✅ Read-only analysis
- ✅ No edits without approval
- ✅ No new dependencies without permission
- ✅ No tests added if none exist
- ✅ Never overwrites uncommitted work
- ✅ Reports in your language

---

→ Full behavior: [SKILL.md](./SKILL.md)

<div align="center">
  <sub>Built for developers who expect AI agents to refactor like senior engineers.</sub>
  <br><br>
  <sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · MIT License</sub>
</div>