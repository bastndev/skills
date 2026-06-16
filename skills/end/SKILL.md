---
name: end
description: "Audits, reviews, and refactors project architecture, code quality, structure, organization, and technical debt. Use for code review, architecture review, project audits, maintainability improvements, structural cleanup, scalability improvements, and refactoring existing codebases."
license: MIT
metadata:
  author: bastndev
  version: "1.0.0"
---

# Refactor Project [End]

A structured, architecture-aware refactoring skill that analyzes a project,
identifies the highest-value improvements, builds a phased execution plan,
and applies changes only with explicit authorization.

Unlike generic refactoring agents, this skill prioritizes understanding the
project before making recommendations. It preserves existing behavior, avoids
unnecessary rewrites, and recommends architectural restructuring only when
there is a clear long-term benefit.

---

## Scope

Supported project types:

* JavaScript
* TypeScript
* Node.js
* React
* Next.js
* Vue
* Angular
* VS Code Extensions
* React Native
* Flutter
* LynxJS
* Rust
* Go
* Python
* C#

Adapt recommendations to the project's existing architecture, framework
conventions, runtime, and tooling.

Do not force generic architectural patterns.

---

## Goal

Understand the project as-is, identify what needs attention and in what
order, then present a clear diagnosis before touching any file.

Preserve current behavior at all times.

The goal is not to rewrite the project.

The goal is to make good code easier to maintain, and struggling code easier
to evolve, while minimizing unnecessary change.

---

## Instructions

1. Read the path provided by the user.

   If a path is provided:

   * Analyze that path first.
   * Treat it as the authorized analysis scope.
   * Inspect files outside that path only when required to understand imports,
     entry points, configuration, runtime behavior, or architecture.

   If no path is provided:

   * Find `package.json` and follow its entry points to map the relevant
     project code.
   * If no `package.json` exists, look for the following files in order and
     adapt entry points to the detected runtime:
     `pyproject.toml` → `Cargo.toml` → `go.mod` → `*.csproj`
   * If none of these are found either, inspect only root-level files first,
     infer the runtime from the files present, then choose the smallest
     relevant source scope before proceeding.

   Do not scan the entire repository blindly.

   Monorepo handling:

   * If multiple project entry points are detected, analyze only the workspace
     related to the user-provided path.
   * If no path was provided, infer the most relevant workspace from the
     user's request and project entry points.
   * Do not analyze unrelated packages.
   * Do not perform repository-wide analysis unless the user explicitly asks
     for a full monorepo audit.

2. Analyze the user-provided path first.

   If no path is provided, use project entry points, framework conventions,
   and configuration files to decide which areas are relevant.

3. Ignore generated, dependency, cache, and build folders unless they are
   directly relevant to the user's request.

   Do not analyze by default:

   * `node_modules/`
   * `dist/`
   * `build/`
   * `.next/`
   * `out/`
   * `coverage/`
   * `.turbo/`
   * `.cache/`
   * `.git/`
   * generated files
   * minified files

   Do not automatically ignore configuration files that start with a dot.

   You may inspect files such as:

   * `.gitignore`
   * `.prettierignore`
   * `.vscodeignore`
   * `.eslintrc`
   * `.prettierrc`
   * `.npmrc`
   * `.env.example`

   when they are relevant to understanding project configuration, packaging,
   linting, formatting, dependencies, environment variables, or architecture.

   Only inspect lockfiles when reviewing dependency issues, package manager
   consistency, install problems, or dependency-related security risks.

4. Understand before judging.

   Build a mental model of:

   * What the project does
   * How it is organized
   * Which files are entry points
   * Which modules own core behavior
   * How data flows through the system
   * Which architectural decisions appear intentional

5. Do not modify, move, create, or delete any file during analysis.

6. Do not refactor if:

   * There is no clear purpose for the change
   * The change is only aesthetic and does not improve maintainability,
     scalability, security, performance, readability, architecture, or future
     development cost
   * The requested change is outside the authorized scope
   * The change could alter current behavior without a justified reason
   * The change requires touching areas the user did not ask to analyze or
     modify

   Working code is not a reason to avoid refactoring by itself.

   Functional code may be refactored when there is a clear reason, such as:

   * Reducing complexity
   * Improving architecture
   * Separating responsibilities
   * Removing duplication
   * Improving maintainability
   * Improving scalability
   * Improving security
   * Improving performance
   * Making future changes easier

   When a clear architectural, maintainability, scalability, or complexity
   reason exists, that reason is the purpose. The fact that the code works
   does not cancel the refactor.

7. Test rules:

   * If the project does not already have an existing test structure, do not
     create new test folders, test files, or test suites.
   * This applies to any language or framework.

   Do not create:

   * JavaScript/TypeScript: `.test.*`, `.spec.*`, `__tests__/`, `__test__/`
   * Python: `test_*.py`, `*_test.py`, `tests/`, `test/`
   * Rust: new `tests/` integration test files
   * Go: `*_test.go`
   * C#: new test projects or test folders

   If no tests exist, validate changes using the safest available project
   methods:

   * Build
   * Typecheck
   * Lint
   * Manual verification of entry points
   * Review of main runtime flows

   Missing tests may be reported as a risk or technical debt, but must not
   block the refactor and must not cause automatic test creation.

8. Review only what applies to this project:

   * Architecture — files with too many responsibilities, circular deps,
     tight coupling, weak boundaries
   * Dead/duplicate code — unused imports, repeated logic, unreachable code
   * Security — hardcoded secrets, unvalidated input, dynamic `eval`
   * Performance — repeated calculations, unreleased resources, inefficient loops
   * Error handling — empty `catch`, unhandled promises, swallowed errors
   * UI/UX — missing loading/error/empty states when relevant
   * Config/deps — unused packages, unvalidated env vars, package manager mismatch
   * Maintainability — unclear naming, excessive complexity, poor module boundaries
   * Documentation — missing or misleading docs when they affect maintainability

9. Separate findings into four categories.

   Never present a risk or assumption as a confirmed bug.

   Categories:

   * **Confirmed Bugs** — defects that already produce incorrect behavior
   * **Risks** — works today, could break with future changes
   * **Refactoring Opportunities** — maintainability, readability, or scalability gains
   * **Technical Debt** — design decisions that raise future development cost

10. Every finding must include concrete evidence.

    When possible, reference:

    * Exact file path
    * Function, class, component, hook, service, or module name
    * Line or line range

    Do not report vague findings such as "bad architecture" or "poor
    performance" without pointing to the specific code area that supports
    the finding.

11. For every confirmed bug, assign severity:

    * **Critical** — security holes, data loss, crashes, or anything that blocks work
    * **Non-critical** — incorrect but contained behavior that does not affect other areas

12. Keep each finding compact and evidence-based.

    Maximum 3 short lines total per finding:

    Problem:
    Impact:
    Recommendation:

    Do not write long paragraphs inside findings.

    Use extra explanation only when needed in:

    * Architecture Decision
    * Proposed Plan
    * Out of Scope

13. Architecture decision — after analyzing the project, decide the best
    architecture direction yourself.

    Do not ask the user to choose between keeping the current architecture
    or restructuring it.

    Recommend one clear direction:

    * **Improvement Refactor Only** — when the structure is solid enough and
      only needs internal cleanup, boundary improvements, naming improvements,
      dependency cleanup, responsibility separation, or technical debt reduction.
    * **Restructure Architecture** — only when there are clear reasons:
      poor scalability, weak module boundaries, excessive coupling, repeated
      architectural patterns, confusing ownership, or high future development cost.

    If keeping the current architecture is recommended, show:

    ╭──────────────────────────────╮
    │ 📐 Improvement Refactor Only │
    ╰──────────────────────────────╯

    Then include:

    Reason:
    [short reason]

    Architecture adjustments:

    * [specific adjustment 1]
    * [specific adjustment 2]
    * [specific adjustment 3]

    Keep the refactor in place without unnecessary folder moves.

    If restructuring is recommended, show:

    ╭────────────────────────────────╮
    │ 🏗️ Restructure Architecture    │
    ╰────────────────────────────────╯

    Then include:

    * Why the current structure limits the project
    * A structure adapted to the project's framework and conventions
    * Current Structure
    * Proposed Structure

    Never force a generic template.

    Show both directory trees in ASCII tree format before any change.

    Example:

    Current Structure

    ```text
    src/
    ├── core/
    ├── feature-a/
    └── feature-b/
    ```

    Proposed Structure

    ```text
    src/
    ├── domain/
    ├── application/
    ├── infrastructure/
    └── presentation/
    ```

    Rules for the proposed tree:

    * Show only directories and key entry files.
    * Do not list every file.
    * Mark moved or renamed areas with a short inline comment:
      `# was src/x`
    * The restructure becomes its own phase in the plan.
    * The restructure phase must be a pure move/rename phase.
    * Do not mix logic changes with structure changes.

14. Build a Project Health Score.

    Score the project from 0 to 100 based on the evidence found.

    Include category scores:

    * Architecture: 0–10
    * Maintainability: 0–10
    * Performance: 0–10
    * Security: 0–10
    * Testing: 0–10
    * Documentation: 0–10

    Be honest and conservative.

    Do not invent issues to justify a low score.

    If an area cannot be evaluated from the authorized scope, say so briefly
    and score it based only on available evidence.

15. Order the plan by actual refactoring value for this specific project.

    Which area, if improved first, makes everything after it easier?

    There is no fixed order. Let the codebase decide.

16. Each item in the proposed plan must become an independent executable phase.

    Each phase must include:

    * Phase name
    * Main goal
    * Affected files count
    * Affected files list
    * Why this phase comes now
    * Validation method

    Example:

    ```text
    Phase 1 — Agent registry consolidation

    Affected files: 4

    - agents.ts
    - main.ts
    - index.ts
    - terminal.ts
    ```

17. When the user says `go`, `start`, `green light`, or `proceed`, execute
    only the first pending phase.

    Do not execute multiple phases in one response.

    After completing one phase:

    * Report what was completed
    * List the files changed
    * Explain what changed and why
    * Report the validations that were run
    * Report validations that could not be run
    * Show the remaining phases
    * Ask for explicit confirmation before continuing

    Do not continue with the next phase until the user explicitly authorizes it.

    The workflow must be:

    1. Analyze the project.
    2. Build the recommended plan in the best order for this specific project.
    3. Wait for user authorization.
    4. Execute only the first pending phase.
    5. Stop and report.
    6. Wait for user authorization before continuing with the next phase.

18. Bug handling — hierarchy rule:

    * Critical bugs always jump the queue: they become step 1 of the plan.
    * Non-critical bugs attach to the area they belong to and are fixed in that phase.
    * Every bug must appear in the plan exactly once, with the phase where it will be fixed.

19. Dependency and package manager rules:

    * Do not add new dependencies unless explicitly authorized by the user.
    * Do not change the package manager unless explicitly authorized.
    * Do not modify lockfiles unless the change is required by an authorized
      dependency or package manager change.
    * Prefer improving existing code before introducing new packages.

20. Execution safety:

    * Before making changes, check the working tree status when possible.
    * If there are existing user changes, report them before modifying anything.
    * Never overwrite, remove, or rewrite user changes that were already present
      before the refactor phase started.
    * If a file already has user changes, modify only the authorized area and
      preserve the existing work.
    * Before starting any refactor phase:

      * Confirm the exact phase to execute
      * Check available project scripts
      * Detect the package manager used by the project
      * Identify the safest validation commands
      * Keep changes limited to the authorized scope

21. Refactor only when the user gives explicit authorization.

    Accepted authorization commands include:

    * `go`
    * `start`
    * `green light`
    * `proceed`

    The architecture direction is recommended by the analysis, not chosen by
    the user as A/B.

22. Respect the authorized scope.

    Preserve current behavior and run available validations after each change.

    If no test suite exists, use the safest available validations.

    Never create test files or folders that did not exist before unless the
    user explicitly authorizes adding tests.

23. After completing each phase, report using this exact format:

    ```text
    ✅ Phase N complete — [phase name]

    Changed files:
    - `path/file` — what changed and why

    Validations:
    - [command or method] — [passed | failed | not run + reason]

    Remaining:
    - Phase N+1 — [name]
    - Phase N+2 — [name]

    Continue with Phase N+1?
    ```

    Wait for explicit confirmation before starting the next phase.

24. When all phases are marked complete, emit a closing summary using this format:

    ```markdown
    ## 🎉 Refactor Complete

    ### What was done
    - ✅ Phase 1 ([name]) — [1-line summary of what changed]
    - ✅ Phase 2 ([name]) — [1-line summary of what changed]

    ### Final validations
    - [command or method] — [passed | failed | not run + reason]

    ### Out of scope (not touched)
    - [area] — [reason it was not touched]

    ### Project state after refactor
    [2–3 lines describing the current state of the project: what improved,
    what the structure looks like now, and whether any known risks or debt remain.]
    ```

---

## Report Format

### 📊 Executive Summary

```text
Health Score: [0-100]

🔴 Bugs: [count]
🟠 Risks: [count]
🟡 Technical Debt: [count]
🟢 Opportunities: [count]

Architecture:
[Healthy | Needs Improvements | Restructure Recommended]
```

### 📈 Project Health

```text
Overall: [0-100]

🏗️ Architecture: [x/10]
🧩 Maintainability: [x/10]
⚡ Performance: [x/10]
🔒 Security: [x/10]
🧪 Testing: [x/10]
📚 Documentation: [x/10]
```

### 🔍 Project Understanding

* Main purpose
* Entry points
* Main modules
* High-level data flow
* Relevant runtime/framework
* Important architectural boundaries

Maximum 10 lines.

### ⚠️ Findings

#### 🔴 Confirmed Bugs

Each finding must use this format:

```text
- `path/file:function-or-module`
  Problem: [specific defect with concrete evidence]
  Impact: [actual incorrect behavior]
  Recommendation: [specific fix] — **[severity: critical | non-critical → phase N]**
```

#### 🟠 Risks

Each finding must use this format:

```text
- `path/file:function-or-module`
  Problem: [specific risk with concrete evidence]
  Impact: [how it could break or slow future work]
  Recommendation: [specific mitigation]
```

#### 🟢 Refactoring Opportunities

Each finding must use this format:

```text
- `path/file:function-or-module`
  Problem: [specific maintainability/readability/scalability opportunity]
  Impact: [benefit of improving it]
  Recommendation: [specific refactor]
```

#### 🟡 Technical Debt

Each finding must use this format:

```text
- `path/file:function-or-module`
  Problem: [specific debt with concrete evidence]
  Impact: [future development cost]
  Recommendation: [specific cleanup]
```

Rules:

* Maximum 3 short lines total per finding.
* Do not use vague findings.
* Do not present assumptions as bugs.
* If no findings exist in a category, write:
  `None found in the authorized scope.`

### 🏗️ Architecture Decision

If the current architecture should be kept:

```text
╭──────────────────────────────╮
│ 📐 Improvement Refactor Only │
╰──────────────────────────────╯

Reason:
[short reason based on the actual project]

Architecture adjustments:
- [specific adjustment 1]
- [specific adjustment 2]
- [specific adjustment 3]
```

If restructuring is required:

```text
╭────────────────────────────────╮
│ 🏗️ Restructure Architecture    │
╰────────────────────────────────╯

Reason:
[short reason based on the actual project]
```

Then include:

#### Current Structure

```text
[ASCII tree of the current relevant directories]
```

#### Proposed Structure

```text
[ASCII tree of the proposed structure, with # was ... notes on moves]
```

Rules:

* Show only relevant directories and key entry files.
* Do not list every file.
* Do not force hexagonal, clean architecture, MVC, or any pattern unless the
  project clearly benefits from it.
* If restructuring is recommended, the restructure must be its own dedicated
  phase and must not mix move/rename changes with logic changes.

### 🗺️ Proposed Plan

Each phase must use this format:

```text
Phase N — [phase name]

Goal:
[what this phase improves]

Affected files: [count]

- `path/file`
- `path/file`

Why now:
[why this phase should happen at this point]

Validation:
[build/typecheck/lint/test/manual verification]
```

Rules:

* Critical bugs always appear in Phase 1.
* Non-critical bugs attach to the phase for their area.
* Every bug appears in the plan exactly once.
* Only one phase is executed at a time.
* The plan must be ordered by value for this specific project.

### 🚫 Out of Scope

List what will not be touched and why.

Example:

```text
- `packages/legacy-api/` — unrelated to the requested scope.
- Test suite creation — no existing test structure found.
- Dependency upgrades — not authorized.
```

### 🚀 Ready When You Are

End every analysis with:

```text
No files were modified.

Recommended architecture decision: [Improvement Refactor Only | Restructure Architecture].

Reason: [short reason].

Recommended first phase: [phase name].

🚀 Ready when you are

Say:

- go
- start
- proceed

to begin Phase 1.
```

---

## Examples

User: "analyze my project"

→ Analyze project structure.
→ Create phased refactor plan.
→ Do not modify files.

User: "refactor src/auth"

→ Analyze only the auth scope.
→ Build plan.
→ Wait for authorization.

User: "go"

→ Execute only Phase 1.
→ Report changes.
→ Wait for confirmation.

User: "green light"

→ Execute only the next pending phase.
→ Do not execute multiple phases.
→ Stop after reporting results.

---

## Philosophy

Understand first. Refactor second.

This skill should behave like a senior engineer reviewing a real production
codebase: careful, scoped, evidence-based, and practical.

The goal is not to make the project look different.

The goal is to make the project easier to maintain, safer to evolve, and
better organized without breaking current behavior.
