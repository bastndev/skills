---
name: end
description: "Analyzes the project's architecture, structure, and code quality. Builds a phased refactoring plan and applies changes only with explicit authorization."
license: MIT
metadata:
  author: bastndev
  version: "1.0.0"
---

# Refactor Project

## Goal
Understand the project as-is, identify what needs attention and in what
order, then present a clear diagnosis before touching any file.
Preserve current behavior at all times.

## Instructions

1. Read the path provided by the user. If none, find `package.json`
   and follow its entry points to map the relevant project code.
   If no `package.json` exists, look for the following files in order
   and adapt entry points to the detected runtime:
   `pyproject.toml` → `Cargo.toml` → `go.mod` → `*.csproj`
   If none of these are found either, inspect only the root-level files
   first, infer the runtime from the files present, then choose the
   smallest relevant source scope before proceeding.
   Do not scan the entire repository blindly.

2. Analyze the user-provided path first. If no path is provided, use the
   project entry points to decide which areas are relevant.

3. Ignore generated, dependency, cache, and build folders unless they are
   directly relevant to the user's request.

   Do not analyze by default:
   - `node_modules/`
   - `dist/`
   - `build/`
   - `.next/`
   - `out/`
   - `coverage/`
   - `.turbo/`
   - `.cache/`
   - `.git/`
   - generated files
   - minified files

   Do not automatically ignore configuration files that start with a dot.

   You may inspect files such as:
   - `.gitignore`
   - `.prettierignore`
   - `.vscodeignore`
   - `.eslintrc`
   - `.prettierrc`
   - `.npmrc`
   - `.env.example`

   when they are relevant to understanding project configuration,
   packaging, linting, formatting, dependencies, environment variables,
   or architecture.

   Only inspect lockfiles when reviewing dependency issues, package
   manager consistency, or install problems.

4. Understand before judging — build a mental model of what the project
   does, how it's organized, and which decisions are intentional.

5. Do not modify, move, create, or delete any file during analysis.

6. Do not refactor if:
   - There is no clear purpose for the change
   - The change is only aesthetic and does not improve maintainability,
     scalability, security, performance, readability, architecture, or
     future development cost
   - The requested change is outside the authorized scope
   - The change could alter current behavior without a justified reason
   - The change requires touching areas the user did not ask to analyze
     or modify

   Working code is not a reason to avoid refactoring by itself.
   Functional code may be refactored when there is a clear reason, such
   as reducing complexity, improving architecture, separating
   responsibilities, removing duplication, improving maintainability,
   improving scalability, improving security, improving performance, or
   making future changes easier.

   When a clear architectural, maintainability, scalability, or
   complexity reason exists, that reason IS the clear purpose — the
   fact that the code works does not cancel it.

7. Test rules:
   - If the project does not already have an existing test structure, do
     not create new test folders, test files, or test suites.
   - This applies to any language or framework. Do not create:
     - JavaScript/TypeScript: `.test.*`, `.spec.*`, `__tests__/`, `__test__/`
     - Python: `test_*.py`, `*_test.py`, `tests/`, `test/`
     - Rust: new `tests/` integration test files
     - Go: `*_test.go`
     - C#: new test projects or test folders
   - If no tests exist, validate changes using the safest available
     project methods:
     - build
     - typecheck
     - lint
     - manual verification of entry points
     - review of main runtime flows
   - Missing tests may be reported as a risk or technical debt, but must
     not block the refactor and must not cause automatic test creation.

8. Review only what applies to this project:
   - Architecture — files with too many responsibilities, circular deps,
     tight coupling, weak boundaries
   - Dead/duplicate code — unused imports, repeated logic, unreachable code
   - Security — hardcoded secrets, unvalidated input, dynamic `eval`
   - Performance — repeated calculations, unreleased resources, inefficient loops
   - Error handling — empty `catch`, unhandled promises, swallowed errors
   - UI/UX — missing loading/error/empty states when relevant
   - Config/deps — unused packages, unvalidated env vars, package manager mismatch
   - Maintainability — unclear naming, excessive complexity, poor module boundaries

9. Separate findings into four categories. Never present a risk or an
   assumption as a confirmed bug:
   - **Confirmed Bugs** — defects that already produce incorrect behavior
   - **Risks** — works today, could break with future changes
   - **Refactoring Opportunities** — maintainability/readability/scalability gains
   - **Technical Debt** — design decisions that raise future development cost

10. Every finding must include concrete evidence. When possible, reference:
    - exact file path
    - function, class, component, hook, service, or module name
    - line or line range

    Do not report vague findings such as "bad architecture" or "poor
    performance" without pointing to the specific code area that supports
    the finding.

11. For every confirmed bug, assign severity:
    - **Critical** — security holes, data loss, crashes, or anything that blocks the work
    - **Non-critical** — incorrect but contained behavior that doesn't affect other areas

12. Architecture decision — after analyzing the project, decide the best
    architecture direction yourself. Do not ask the user to choose between
    keeping the current architecture or restructuring it.

    Recommend one clear direction:
    - **Keep current architecture** — when the structure is solid enough
      and only needs internal cleanup, boundary improvements, naming
      improvements, dependency cleanup, or responsibility separation.
    - **Restructure architecture** — only when there are clear reasons:
      poor scalability, weak module boundaries, excessive coupling,
      repeated architectural patterns, confusing ownership, or high future
      development cost.

    If keeping the current architecture is recommended:
    - Explain briefly why it is viable.
    - List the specific adjustments needed.
    - Keep the refactor in place without unnecessary folder moves.

    If restructuring is recommended:
    - Explain why the current structure limits the project.
    - Propose a structure adapted to the project's framework and conventions.
    - Never force a generic template.
    - Show two directory trees in ASCII tree format before any change:
      the current relevant structure and the proposed one.

    Example of the expected style:

    ```
    src/
    │
    ├── core/
    │   ├── error/
    │   └── utils/
    │
    ├── feature_name/
    │   ├── data/
    │   ├── domain/
    │   └── presentation/
    │
    └── shared/
        ├── components/
        └── widgets/
    ```

    Rules for the proposed tree:
    - Show only directories and key entry files; do not list every file.
    - Mark moved or renamed areas with a short inline comment (`# was src/x`).
    - The restructure becomes its own phase in the plan.
    - The restructure phase must be a pure move/rename phase: no logic
      changes mixed with structure changes.

13. Order the plan by actual refactoring value for this specific project —
    which area, if improved first, makes everything after it easier.
    There is no fixed order; let the codebase decide.

14. Each item in the proposed plan must become an independent executable
    phase.

    When the user says `go`, `start`, `green light`, or `proceed`,
    execute only the first pending phase.

    Do not execute multiple phases in one response.

    After completing one phase:
    - Report what was completed.
    - List the files changed.
    - Explain what changed and why.
    - Report the validations that were run.
    - Report any validations that could not be run.
    - Show the remaining phases.
    - Ask for explicit confirmation before continuing.

    Do not continue with the next phase until the user explicitly
    authorizes it.

    The workflow must be:
    1. Analyze the project.
    2. Build the recommended plan in the best order for this specific project.
    3. Wait for user authorization.
    4. Execute only the first pending phase.
    5. Stop and report.
    6. Wait for user authorization before continuing with the next phase.

15. Bug handling — hierarchy rule:
    - Critical bugs always jump the queue: they become step 1 of the plan.
    - Non-critical bugs attach to the area they belong to and are fixed in that phase.
    - Every bug must appear in the plan exactly once, with the phase where it will be fixed.

16. Dependency and package manager rules:
    - Do not add new dependencies unless explicitly authorized by the user.
    - Do not change the package manager unless explicitly authorized.
    - Do not modify lockfiles unless the change is required by an
      authorized dependency or package manager change.
    - Prefer improving existing code before introducing new packages.

17. Execution safety:
    - Before making changes, check the working tree status when possible.
    - If there are existing user changes, report them before modifying anything.
    - Never overwrite, remove, or rewrite user changes that were already
      present before the refactor phase started.
    - If a file already has user changes, modify only the authorized area
      and preserve the existing work.
    - Before starting any refactor phase:
      - Confirm the exact phase to execute.
      - Check available project scripts.
      - Detect the package manager used by the project.
      - Identify the safest validation commands.
      - Keep changes limited to the authorized scope.

18. Keep each finding concise but evidence-based:
    - 1 line for the problem, including the concrete code reference
    - 1 line for the impact
    - 1 line for the recommendation

    Do not write long explanations inside findings.
    Use extra explanation only when needed in the architecture decision
    or proposed plan.

19. End the analysis with:

    > No files were modified.
    >
    > Recommended architecture decision: [keep current architecture | restructure architecture].
    >
    > Reason: [short reason].
    >
    > Recommended first phase: [phase name].
    >
    > Ready when you are — say `go`, `start`, or `proceed` to begin phase 1.

20. Refactor only when the user gives explicit authorization (`go`,
    `start`, `green light`, `proceed`, etc.). The architecture direction
    is recommended by the analysis, not chosen by the user as A/B.

21. Respect the authorized scope. Preserve current behavior and run
    available validations after each change. If no test suite exists, use
    the safest available validations. Never create test files or folders
    that did not exist before unless the user explicitly authorizes adding tests.

22. After completing each phase, report using this exact format:

    ✅ Phase N complete — [phase name]

    Changed files:
    - `path/file` — what changed and why

    Validations:
    - [command or method] — [passed | failed | not run + reason]

    Then show remaining phases:
    > Remaining: phase N+1 ([name]), phase N+2 ([name]), ...
    > Continue with phase N+1?

    Wait for explicit confirmation before starting the next phase.

23. When all phases are marked ✅, emit a closing summary using this format:

    ## 🎉 Refactor Complete

    ### What was done
    - ✅ Phase 1 ([name]) — [1-line summary of what changed]
    - ✅ Phase 2 ([name]) — [1-line summary of what changed]
    - ...

    ### Final validations
    - [command or method] — [passed | failed | not run + reason]

    ### Out of scope (not touched)
    - [area] — [reason it was not touched]

    ### Project state after refactor
    [2–3 lines describing the current state of the project: what improved,
    what the structure looks like now, and whether any known risks or debt remain.]

## Report Format

### 🔍 Project Understanding
- Main purpose
- Entry points
- Main modules
- High-level data flow

Maximum 10 lines.

### ⚠️ Findings

#### Confirmed Bugs
- `path/file:function-or-module` — problem — impact — recommendation — **[severity: critical | non-critical → phase N]**

#### Risks
- `path/file:function-or-module` — risk — impact — recommendation

#### Refactoring Opportunities
- `path/file:function-or-module` — opportunity — benefit — recommendation

#### Technical Debt
- `path/file:function-or-module` — debt — impact — recommendation

### 🏗️ Architecture Decision
**Recommended decision:** [keep current architecture | restructure architecture]

**Reason:** [short reason based on the actual project]

**What this means:** [1–3 lines explaining what will happen structurally]

If restructuring is recommended, include both trees:

#### Current structure
```
[ASCII tree of the current relevant directories]
```

#### Proposed structure
```
[ASCII tree of the proposed structure, with `# was ...` notes on moves]
```

If keeping the current architecture is recommended, include:

#### Architecture adjustments
- [specific adjustment 1]
- [specific adjustment 2]
- [specific adjustment 3]

### 🗺️ Proposed Plan
1. [phase 1] [area] — what to fix first and why (critical bugs always here)
2. [phase 2] [area] — ... (+ non-critical bugs belonging to this area)
3. [phase 3] [area] — ...

If restructuring is recommended, the restructure must be its own dedicated
phase and must not mix move/rename changes with logic changes.

### 🚫 Out of Scope
[what will NOT be touched and why]

---
No files were modified.

Recommended architecture decision: [keep current architecture | restructure architecture].

Reason: [short reason].

Recommended first phase: [phase name].

Ready when you are — say `go`, `start`, or `proceed` to begin phase 1.