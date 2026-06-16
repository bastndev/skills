<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/github/image/xyz/end.webp" width="150" />
</p>

<h1 align="center">Refactor Project</h1>

<p align="center">
  <strong>End</strong> — The disciplined refactoring skill
</p>

<p align="center">
  <a href="https://github.com/bastndev/skills/blob/main/README.md">← Back to Start / Middle / [End]</a>
</p>

---

**Analyzes your project's architecture, structure, and code quality. Builds a clear, prioritized, phased refactoring plan — and applies every change only with your explicit authorization.**

It never guesses. It never rushes. It never modifies anything until you say `go`.

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

## Installation

```bash
npx skills add bastndev/skills --skill end
```

## When to Use This Skill

Use **End** (refactor-project) when you need a senior-level audit and safe structural work:

- The codebase has grown organically and boundaries are blurry
- You are preparing for a major feature, migration, or scaling phase
- Tech debt or inconsistent patterns are slowing the team down
- You want **evidence-based** recommendations instead of vague "clean this up" advice
- You want full control: the agent diagnoses first, then you approve every phase

It is the natural final stage in the **Start → Middle → End** workflow.

## What Makes It Different

| Traditional AI refactoring                  | Refactor Project (End)                                      |
|---------------------------------------------|-------------------------------------------------------------|
| Starts editing immediately                  | **Analysis only** — zero files touched until you approve   |
| One giant, hard-to-review diff              | Discrete, reviewable **phases** executed one at a time     |
| May invent tests or add dependencies        | Never creates tests if none existed. Never adds packages without explicit permission |
| Vague claims ("I improved maintainability") | Every finding includes **exact file paths + lines + functions** |
| No memory of your previous instructions     | Follows a strict 23-rule protocol (see SKILL.md)           |

## How It Works (The Actual Flow)

1. **Deep Analysis (read-only)**  
   It intelligently locates entry points (`package.json`, `pyproject.toml`, `Cargo.toml`, etc.) and maps only the relevant source. It ignores `node_modules`, `dist`, `.next`, `build`, `.git`, generated/minified files, etc. by default.  
   **No files are created, moved, or edited.**

2. **Structured Diagnosis**  
   It produces a report in a fixed, scannable format:
   - 🔍 Project Understanding (purpose, entry points, modules, data flow — max 10 lines)
   - ⚠️ Findings broken into four categories:
     - **Confirmed Bugs** (with severity: Critical / Non-critical)
     - **Risks**
     - **Refactoring Opportunities**
     - **Technical Debt**
   - 🏗️ Architecture Decision (recommends **keep current** or **restructure**, with reasons + ASCII directory trees when restructuring is advised)
   - 🗺️ Proposed Plan (ordered phases; critical bugs always surface first)
   - Out of scope

3. **You Are In Control**  
   At the end of the report you will see:
   > No files were modified.
   >
   > Recommended architecture decision: ...
   >
   > Recommended first phase: ...
   >
   > Ready when you are — say `go`, `start`, or `proceed` to begin phase 1.

4. **Phased Execution**  
   When you authorize, it executes **exactly one phase**. After the phase it reports:
   - ✅ Phase N complete — [phase name]
   - Changed files (with what & why)
   - Validations run (build, typecheck, lint, etc.)
   - Remaining phases
   - Then it **stops** and waits for your next explicit authorization.

5. **Completion**  
   When every phase is done it emits a clean closing summary:
   - What was done (one line per phase)
   - Final validations
   - Out of scope areas
   - Project state after the refactor

## Core Safety Guarantees

- **Behavior preservation** is the default. Changes are only made when there is a clear purpose (maintainability, scalability, security, performance, readability, architecture, or reduced future development cost).
- Working code is **never** a reason to skip refactoring when a real improvement exists.
- No new test folders or files are created if the project had none.
- No dependencies or package manager changes unless you explicitly authorize them.
- It respects uncommitted work and the current working tree.
- It only touches what you asked it to analyze.

## Example Finding Format (What You Will See)

**Confirmed Bugs**
- `src/api/handler.ts:processRequest` — missing input validation on `userId` — can lead to unauthorized data access — add schema validation — **[severity: critical → phase 1]**

**Refactoring Opportunities**
- `components/Dashboard.tsx:fetchData` — repeated data-fetching logic duplicated across 4 components — maintenance burden — extract to shared hook

All findings are concrete. Vague statements are not allowed.

## Full Rules & Report Specification

The complete instruction set, edge cases, architecture tree rules, phase ordering logic, validation requirements, and exact output templates are in:

→ [SKILL.md](./SKILL.md)

This file is the single source of truth for how the skill behaves.

## Related

- Main suite documentation & the other phases: [../../README.md](../../README.md)
- Install other skills the same way once available (Start & Middle families coming)

---

<div align="center">
  <sub>Built for developers who want their AI agents to act with the discipline of a senior engineer.</sub>
  <br><br>
  <sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="https://github.com/bastndev/skills/blob/main/LICENSE">MIT</a></sub>
</div>