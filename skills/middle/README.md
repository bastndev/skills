<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/github/icons/middle.webp" width="150" />
</p>

<h1 align="center">[Middle] / Improve Project</h1>

<p align="center">
  <strong>Middle</strong> — The focused improvement skill
</p>

<p align="center">
  <a href="../../README.md">← Back to Start / [Middle] / End</a>
</p>

---

Improves **one dimension at a time** — performance, security, UI/UX, structure, cleanup, or code quality — inside the path you point at. Small surface, fast diagnosis, surgical changes. Zero edits until you say `go`.

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

## Install

```bash
npx skills add bastndev/skills --skill middle
```

## Usage

```
/middle <focus> (@path)

/middle performance (@src/api)
/middle security
/middle 3 (@components/)
/middle                          # shows the focus menu
```

## The Six Focuses

| #   | Focus              | What it hunts                                          |
| --- | ------------------ | ------------------------------------------------------ |
| 1   | ⚡ **performance** | Wasted work, N+1 queries, waterfalls, heavy bundles    |
| 2   | 🔒 **security**    | Secrets, unvalidated input, injection, missing authz   |
| 3   | 🎨 **ui-ux**       | Missing states, accessibility, consistency, feedback   |
| 4   | 🏗️ **structure**   | Oversized files, wrong owners, weak boundaries         |
| 5   | 🧹 **cleanup**     | Dead code, unused deps, duplication, debug leftovers   |
| 6   | 🧩 **quality**     | Naming, complexity, swallowed errors, magic values     |

## How It Works

1. **One lens** — Analyzes your scope through the chosen focus only. Everything else is ignored (except critical security issues, reported in one line).
2. **Focused diagnosis** — A single focus score (0–10), evidence-backed findings sorted into Critical / Improvements / Polish, and a compact plan of 1–3 phases.
3. **You authorize** — Say `go` to begin. It executes **one phase**, reports changes + validations, then stops.
4. **Proven gain** — Closes with an honest before → after score for the focus. `▲ +0` if nothing improved.

## What You Get

```
🎯 [middle] ⚡ Performance — @src/api — 6/10

⚠️ Findings:

🟡 Improvements

  01. User lookup runs once per request item instead of once per request.
  02. The reports endpoint loads the full dataset to return the first page.

🗺️ Plan

Phase 1 — Cache repeated user lookups in session.ts
Outcome: One DB call per request instead of N.
Files: `src/api/session.ts`
Check: typecheck + manual verification
```

## Guarantees

- No files modified during analysis
- One focus per run — no "while I was here" edits
- No new tests created if the project had none
- No dependencies added without permission
- Uncommitted work is never overwritten

## Middle vs End

| Question                        | Use          |
| ------------------------------- | ------------ |
| "Make this page faster"         | **`middle`** |
| "Harden security in `src/api`"  | **`middle`** |
| "Clean the dead code here"      | **`middle`** |
| "Audit my whole project"        | **`end`**    |
| "Restructure the architecture"  | **`end`**    |

---

→ Full spec & rules: [SKILL.md](./SKILL.md)

<div align="center">
  <sub>Built for developers who want their AI agents to act with the discipline of a senior engineer.</sub>
  <br><br>
  <sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="https://github.com/bastndev/skills/blob/main/LICENSE">MIT</a></sub>
</div>
