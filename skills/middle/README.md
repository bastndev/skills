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
/middle <option|focus> (@path)

/middle 0                        # health overview of the project
/middle (@src/) 0                # health overview of src/ only
/middle (@src/) 1                # performance improvement in src/
/middle security                 # names and aliases also work
/middle                          # shows the menu
```

Natural language works too: _"make this page faster"_ → `1`, _"harden security in src/api"_ → `3` on `src/api`. Ambiguous requests get the menu.

## The Menu

Every option is a number, so it's easy to call. `0` gives **statistics only**. Each focus `1–6` does the same three things for its dimension: **qualifies it** (score + counts), **reports** evidence-backed findings, and **proposes a correction plan** — executed phase by phase when you say `go`.

| #   | Option             | What it hunts                                          |
| --- | ------------------ | ------------------------------------------------------ |
| 0   | 📊 **overview**    | Scores the scope 0–100 + category bars — stats only    |
| -   |  |     |
| 1   | ⚡ **performance** | Wasted work, N+1 queries, waterfalls, heavy bundles    |
| 2   | 🎨 **ui-ux**       | Missing states, accessibility, consistency, feedback   |
| 3   | 🔒 **security**    | Secrets, unvalidated input, injection, missing authz   |
| 4   | 🏗️ **structure**   | Oversized files, wrong owners, weak boundaries         |
| 5   | 🧹 **cleanup**     | Dead code, unused deps, duplication, debug leftovers   |
| 6   | 🧩 **quality**     | Naming, complexity, swallowed errors, magic values     |

No `@path`? The whole project is analyzed — scope is discovered from the project's entry points (`package.json` → `pyproject.toml` → `Cargo.toml` → `go.mod` → `*.csproj`), the same way the `end` skill does it.

## How It Works

1. **Score it** (option `0`) — A 0–100 health overview of the project or folder, with findings and a pointer to the weakest area. Nothing is planned or modified.
2. **One lens** (options `1–6`) — Analyzes your scope through the chosen focus only. Everything else is ignored (except critical security issues, reported in one line).
3. **Focused diagnosis** — The same overview visual, scoped to one focus (0–100), evidence-backed findings sorted into Critical / Improvements / Polish, and a compact plan of 1–3 phases. Headers show your project's name, taken from the manifest (`package.json` `name`, etc.) or the folder name.
4. **You authorize** — Say `go` to begin. It executes **one phase**, reports changes + validations, then stops. Closes with an honest before → after score; `▲ +0` if nothing improved.

## What You Get

Option `0` — the project thermometer:

```
📊 [my-project] Health Overview — 74 / 100

🔴 Bugs 1    🟡 Debt/Risks 3    🟢 Suggestions 2

🏗️ Architecture     7/10
🧩 Maintainability  6/10
⚡ Performance       8/10
🔒 Security          5/10
📚 Documentation     7/10

Weakest bar: 🔒 Security 5/10 — run `/middle 3` to improve it.
```

Options `1–6` — the same visual, one focus, plus a plan:

```
📊 [my-project] ⚡ Performance Overview — 62 / 100

🔴 Critical 0    🟡 Improvements 2    🟢 Polish 1

⚠️ Findings:

🟡 Improvements

  01. User lookup runs once per request item instead of once per request.
      ↳ `src/api/session.ts` — getUser() called inside the items loop.
  02. The reports endpoint loads the full dataset to return the first page.

🗺️ Plan

Phase 1 — Cache repeated user lookups in session.ts
Outcome: One DB call per request instead of N.
Files: `src/api/session.ts`
Check: typecheck + manual verification
```

### Reading the Score

| Score | Meaning |
| ----- | ------- |
| **0–40** | 🚨 Critical — hard to maintain, risky to change |
| **40–60** | 🔴 Heavy debt — significant refactoring recommended |
| **60–70** | 🟡 Needs improvement — works, but address debt before production |
| **70–80** | 🟢 Production-ready — solid, maintainable code |
| **80–90** | ⭐ Excellent — clean architecture, praise-worthy |
| **90–100** | 🏆 Outstanding — reference-grade codebase |

## Guarantees

- No files modified during analysis
- One focus per run — no "while I was here" edits
- No new tests created if the project had none
- No dependencies added without permission
- Uncommitted work is never overwritten

## Middle vs End

| Question                        | Use          |
| ------------------------------- | ------------ |
| "How healthy is this folder?"   | **`middle`** |
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
