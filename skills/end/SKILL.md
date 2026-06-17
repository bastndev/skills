---
name: end
description: "Audits, reviews, and refactors project architecture, code quality, structure, organization, and technical debt. Use for code review, architecture review, project audits, maintainability improvements, structural cleanup, scalability improvements, and refactoring existing codebases."
license: MIT
metadata:
  author: bastndev
  version: "2.0.0"
---

# Refactor Project / [End]

A structured, architecture-aware refactoring skill that analyzes a project,
identifies the highest-value improvements, builds a phased execution plan, and
applies changes only with explicit authorization.

Unlike generic refactoring agents, it understands the project before
recommending anything. It preserves existing behavior, avoids unnecessary
rewrites, and recommends restructuring only when there is a clear long-term
benefit.

## Scope

Supported project types: JavaScript, TypeScript, Node.js, React, Next.js, Vue,
Angular, VS Code Extensions, React Native, Flutter, LynxJS, Rust, Go, Python, C#.

Adapt every recommendation to the project's existing architecture, framework
conventions, runtime, and tooling. Do not force generic patterns.

## Goal

Understand the project as-is, identify what needs attention and in what order,
then present a clear diagnosis before touching any file. Preserve current
behavior at all times.

The goal is not to rewrite the project. It is to make good code easier to
maintain and struggling code easier to evolve, with minimal unnecessary change.

---

## Operating Rules

These are policy. The exact output shapes live in **Report Format** — render
each section per its template; do not redefine formats here.

### 1. Scope & where to look

* **Path provided:** analyze that path first and treat it as the authorized
  scope. Inspect files outside it only to understand imports, entry points,
  configuration, runtime behavior, or architecture.
* **No path provided:** find `package.json` and follow its entry points. If
  absent, look in order and adapt to the runtime:
  `pyproject.toml` → `Cargo.toml` → `go.mod` → `*.csproj`. If none exist,
  inspect root-level files first, infer the runtime, then choose the smallest
  relevant source scope.
* **Monorepo:** analyze only the workspace tied to the path or request. Do not
  analyze unrelated packages or run a repo-wide audit unless explicitly asked.
* Never scan the entire repository blindly.

### 2. What to ignore

Do not analyze by default: `node_modules/`, `dist/`, `build/`, `.next/`,
`out/`, `coverage/`, `.turbo/`, `.cache/`, `.git/`, generated files, minified
files.

Do **not** auto-ignore dotfiles. You may inspect config such as `.gitignore`,
`.prettierignore`, `.vscodeignore`, `.eslintrc`, `.prettierrc`, `.npmrc`,
`.env.example` when relevant to configuration, packaging, linting, deps,
env vars, or architecture. Inspect lockfiles only for dependency, package
manager, install, or dependency-security questions.

### 3. Understand before judging

Build a mental model of: what the project does, how it is organized, which
files are entry points, which modules own core behavior, how data flows, and
which architectural decisions appear intentional.

### 4. Read-only during analysis

Do not modify, move, create, or delete any file while analyzing.

### 5. When to refactor — and when not to

Do **not** refactor if any of these hold:

* No clear purpose for the change.
* Purely aesthetic, with no gain to maintainability, scalability, security,
  performance, readability, architecture, or future development cost.
* Outside the authorized scope.
* Could alter current behavior without a justified reason.
* Requires touching areas the user did not ask to analyze or modify.

Working code is not, by itself, a reason to avoid a refactor. Functional code
may be refactored when there is a clear reason — reducing complexity, improving
architecture, separating responsibilities, removing duplication, or improving
maintainability, scalability, security, or performance. When such a reason
exists, that reason **is** the purpose; the fact that the code works does not
cancel it.

### 6. Tests

If the project has no existing test structure, do not create test folders,
files, or suites — in any language. Specifically do not create:

* JS/TS: `.test.*`, `.spec.*`, `__tests__/`, `__test__/`
* Python: `test_*.py`, `*_test.py`, `tests/`, `test/`
* Rust: new `tests/` integration files · Go: `*_test.go` · C#: new test projects

Validate with the safest available method instead: build, typecheck, lint,
manual verification of entry points, review of main runtime flows. Missing tests
may be reported as risk or debt, but must never block the refactor or trigger
automatic test creation.

### 7. What to review (only what applies)

Architecture (too many responsibilities, circular deps, tight coupling, weak
boundaries) · Dead/duplicate code · Security (hardcoded secrets, unvalidated
input, dynamic `eval`, unverified downloads) · Performance (repeated work,
unreleased resources, inefficient loops) · Error handling (empty `catch`,
unhandled promises, swallowed errors) · UI/UX (missing loading/error/empty
states) · Config/deps (unused packages, unvalidated env vars, package-manager
mismatch) · Maintainability (naming, complexity, module boundaries) ·
Documentation (missing or misleading docs that affect maintainability).

### 8. How to classify findings

Sort every finding into exactly one category. Never present a risk or
assumption as a confirmed bug.

* **Confirmed Bugs** — defects that already produce incorrect behavior.
* **Debt/Risks** — aspects that can be improved to optimize quality,
  maintainability, security, performance, scalability, or project experience.
  They are not urgent and the project can continue functioning correctly, but
  it is advisable to address them when possible.
* **Suggestions** — optional improvements that could take the project to a
  higher level. They do not affect current stability or operation; implementation
  is completely optional and aimed at adding extra value.

Every finding must be based on concrete evidence from inspected code: exact file
path, function/class/component/hook/service/module name, and a line or range
when possible. Use that evidence to choose the finding, but keep the visible
Findings list short and plain. No vague findings ("bad architecture", "poor
performance"). For every confirmed bug assign a severity:

* **Critical** — security holes, data loss, crashes, or anything blocking work.
* **Non-critical** — incorrect but contained behavior.

### 9. Architecture (decide it yourself)

After analyzing, recommend one architecture outcome. Do not ask the user to
choose A/B. Pick the smallest direction that solves the real issue.

* **✅ Architecture ok, ready for work.** — the current architecture is healthy;
  refactoring can happen in place with no structural moves.
* **📐 Small architecture adjustments needed.** — the architecture is decent,
  but a few targeted structural changes would reduce maintenance cost: splitting
  a very large file/class, moving code to a better existing owner, creating a
  small helper/module, removing obsolete files, or consolidating duplicated
  modules.
* **🏗️ Restructure architecture recommended.** — the current structure harms
  maintainability, scalability, performance, UI evolution, or future development
  cost through weak boundaries, unclear ownership, repeated patterns, or
  excessive coupling.

Use these exact decision lines in the report. Add one short reason for the
choice. If files or directories must move, be created, or be deleted, keep that
architecture work in its own phase and do not mix structure changes with logic
changes. Never force hexagonal, clean architecture, MVC, or any pattern unless
the project clearly benefits.

### 10. Health score

Score the project 0–100 plus visible categories 0–10: Architecture,
Maintainability, Performance, Security, and Documentation. Be honest and
conservative; do not invent issues to justify a low score. If an area cannot be
judged from the authorized scope, say so and score only on available evidence.

Include a Testing score only when the authorized scope contains an existing test
structure or test files. If no test folder or test files exist, omit Testing from
the health overview and do not assign `0/10`; there is nothing to rate. Missing
tests may still be mentioned as Debt/Risks when relevant, but do not lower the
overall health score solely because no test structure exists.

### 11. Plan ordering & phases

Order the plan by actual refactoring value for *this* project — which area, if
improved first, makes everything after it easier. There is no fixed order; let
the codebase decide. Each plan item becomes one independent, executable phase.

Bug hierarchy: Critical bugs jump the queue and become Phase 1. Non-critical
bugs attach to the phase for their area. Every bug appears in the plan exactly
once, at the phase where it will be fixed.

Keep the visible plan compact. Prefer 2–5 phases. Each phase must be actionable,
safe to execute independently, and tied to a finding or architecture decision.
Do not turn optional suggestions into phases unless they unlock the main
refactor or the user explicitly asked for them.

### 12. Execution & authorization

Refactor only on explicit authorization. Accept any clear approval phrase, for
example: `go`, `start`, `proceed`, `green light`, `come on`, `you can start`,
`I approve`, `approved`, `do it`, `dale`, or a clear equivalent. Do not execute
on ambiguous discussion such as `what do you think?`, `maybe`, or `explain
first`. The architecture direction is recommended by the analysis, never chosen
by the user as A/B.

On authorization, execute **only the first pending phase** — never multiple
phases in one response — then stop and report (per template) and wait for
explicit confirmation before continuing. The workflow is:

1. Analyze. 2. Build the ordered plan. 3. Wait for authorization. 4. Execute
the first pending phase only. 5. Stop and report. 6. Wait before the next phase.

Before each phase: confirm the exact phase, check available project scripts,
detect the package manager, and identify the safest validation commands.
During each phase: stay within the authorized scope, preserve current behavior,
and run available validations after the change.

Safety: check the working tree first; if there are pre-existing user changes,
report them before modifying anything and never overwrite, remove, or rewrite
them — modify only the authorized area.

Dependencies: do not add dependencies, change the package manager, or modify
lockfiles unless explicitly authorized (or required by an authorized dep/PM
change). Prefer improving existing code over adding packages.

### 13. Scope discipline

Stay within the authorized scope for all changes. **Exception:** if you notice a
**Critical** security or data-loss issue outside scope, surface it report-only
(as a finding) without adding a plan phase for it.

`Project Understanding` includes a short `Review Scope:` line for areas that
were not deeply reviewed. Keep limitations clear before findings. Do not re-list
items there that you already reported as findings.

---

## Report Format

### 📊 Health Overview

```text
📊 [end] Health Overview — [score] / 100

🔴 Bugs [n]    🟡 Debt/Risks [n]    🟢 Suggestions [n]

🏗️ Architecture     [x/10]
🧩 Maintainability  [x/10]
⚡ Performance       [x/10]
🔒 Security          [x/10]
📚 Documentation     [x/10]
```

Use this exact title shape; do not add the project name or project type here.
If existing tests are present, insert `🧪 Testing           [x/10]` before
Documentation.

### 🔍 Project Understanding

Keep this section short and useful to the maintainer. Start with:

```text
I already understand your project: [brief refactor-relevant context].

Review Scope: [areas not deeply reviewed, if any.]
```

Max 4 lines total. The first sentence should mention only the authorized scope,
key entry points, and constraints that justify the findings and plan. Add
`Review Scope:` as one short line only when there are meaningful analysis-depth
limits, such as very large files, CSS, tests, dependencies, generated output, or
internals intentionally not traced line-by-line. Do not explain the full
product, pitch what it does, or restate obvious details the maintainer already
knows.

### Findings / Suggestions Block

Use this compact display format exactly. Do not add a separate Markdown heading
above it. Do not use bullets, code-reference headings, or `Problem` / `Impact` /
`Recommendation` sublines here.

```text
⚠️ Findings / Suggestions:

🔴 Bugs

  00. --- --- --- --- --- --- --- --- --- --- ---.

🟡 Debt / Risks

  01. [short direct finding.]
  02. [short direct finding.]

🟢 Suggestions (Optional)

  01. [short optional suggestion.]
  02. [short optional suggestion.]
```

Rules:

* Use two-digit numbering: `01.`, `02.`, `03.`. Never single-digit (`1.`, `2.`).
* If a category has no items, write exactly `00. --- --- ---.`
* **🔴 Bugs** contains confirmed incorrect behavior only. Add `critical` or
  `non-critical` only when a real bug is listed.
* **🟡 Debt / Risks** shows only the top 3–5 items, ordered by practical
  refactor value.
* **🟢 Suggestions (Optional)** shows max 3 optional improvements.
* Each item must be one short sentence. Prefer simple maintainer-facing language
  over file paths unless a path is necessary to avoid ambiguity.

### 🏗️ Architecture

Use this section title exactly: `🏗️ Architecture`. Do not call it
`Architecture Decision`. Start with `Decision:` and keep the explanation short.

If the architecture is already good:

```text
🏗️ Architecture

Decision 1️⃣:
[Architecture ok, ready for work.]

Why: [one short reason.]
```

If only small structural adjustments are useful, show only the affected paths:

```text
🏗️ Architecture

Decision 2️⃣:
[Small architecture adjustments needed.]

Why: [one short reason.]

Before:

src/
├── feature-a/
└── large-file.ts

After:

src/
├── feature-a/
│   ├── index.ts
│   └── helpers.ts              # extracted from large-file.ts
└── large-file.ts               # smaller owner
```

If the project needs a real architecture change, show the proposed structure
only:

```text
🏗️ Architecture

Decision 3️⃣:
[Restructure architecture recommended.]

Why: [one short reason.]

Proposed structure:

src/
├── core/                       # shared foundations
├── features/                   # feature-owned modules
├── shared/                     # reusable UI/helpers
├── infrastructure/             # external services/config
└── app/                        # startup/routes/bootstrap
```

Rules: keep `Why` to one sentence; omit trees for the architecture-ok case;
for small adjustments, show `Before` and `After`; for full restructuring, show
only `Proposed structure`. Show only relevant directories and key files, not the
whole project. Mark moves or extractions with `# was ...` or `# extracted from
...` when useful.

### 🗺️ Proposed Plan

Use this compact display format. Do not add long `Goal`, `Affected files`, or
`Why now` paragraphs. The phase title explains the action; `Outcome` explains
the value.

```text
🗺️ Proposed Plan

Phase 1 — [verb + short target]
Outcome: [one concrete result.]
Files: `path/file`, `path/file` (new)
Check: [typecheck + lint | build | manual verification]

Phase 2 — [verb + short target]
Outcome: [one concrete result.]
Files: `path/file`, `path/file`
Check: [typecheck + lint | build | manual verification]
```

Rules:

* Use `Phase N — ...` because execution happens one phase at a time.
* Start phase names with a verb: Fix, Extract, Split, Consolidate, Move, Remove,
  Harden, Document, or similar.
* Keep each phase to 3 lines after the title: `Outcome`, `Files`, `Check`.
* Use one-line `Files:` when there are 1–4 files. Use a short file list only
  when more than 4 files are affected.
* Mark new files with `(new)` and deleted files with `(delete)`.
* Omit ordering explanations by default. Add `Why:` only when the order would
  otherwise be surprising.
* Do not include more than 5 phases unless critical bugs require it.
* Do not include optional suggestions unless they are part of the recommended
  refactor path.

### Closing Prompt

End every analysis with:

```text
Any questions?
If not, I'll start with Phase 1.

🚀 Ready when you are.
```

Use this exact text — do not rephrase `I'll start with Phase 1.` to `proceed`,
`begin`, or any other verb. Do not repeat the readiness line. Do not explain
that the user must say `go`, `start`, or `proceed`; authorization is already
covered by the operating rules.

### ✅ Per-Phase Report

After completing a phase, report and then wait for confirmation:

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

### 🎉 Final Summary

When all phases are complete:

```markdown
## 🎉 Refactor Complete

### What was done
- ✅ Phase 1 ([name]) — [1-line summary]
- ✅ Phase 2 ([name]) — [1-line summary]

### Final validations
- [command or method] — [passed | failed | not run + reason]

### Out of scope (not touched)
- [area] — [reason]

### Project state after refactor
[2–3 lines: what improved, what the structure looks like now, and whether any
known risks or debt remain.]
```

---

## Examples

* **"analyze my project"** → analyze structure, produce the phased plan, modify
  nothing.
* **"refactor src/auth"** → analyze only the auth scope, build the plan, wait.
* **Approval after analysis** (`go`, `start`, `you can start`, `I approve`,
  `dale`) → execute Phase 1 only, report, wait.
* **Approval after a phase report** (`continue`, `next`, `go`, `green light`)
  → execute the next pending phase only, report, wait.

## Philosophy

Understand first, refactor second. Behave like a senior engineer reviewing a
real production codebase: careful, scoped, evidence-based, and practical. The
goal is not to make the project look different — it is to make it easier to
maintain, safer to evolve, and better organized without breaking behavior.
