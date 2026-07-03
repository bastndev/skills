---
name: middle
description: "Focused, on-demand project improver for active development. Improves ONE dimension at a time — performance, security, UI/UX, structure, cleanup (dead code), or code quality — within a given path. Analyzes through that single lens, scores the focus 0–10, proposes a compact phased plan, and executes only with explicit approval. Use for targeted improvements like 'harden security in src/api', 'speed up this page', 'clean dead code', 'polish the UI'. Invoke with /middle <focus> (@path)"
license: Complete terms in LICENSE.txt
metadata:
  author: bastndev
  version: "2.0.0"
---

# Improve / [Middle]

A focused improvement skill for projects in active development. Unlike a full
audit, it improves **one dimension at a time** — the one the user asks for —
inside the scope they point at. Small surface, fast diagnosis, surgical changes,
explicit approval before any edit.

`middle` sits between scaffolding (**Start**) and full refactoring (**End**):
the project already exists and works; the goal is to raise one specific quality
bar without touching anything else.

## Invocation

```
/middle <focus> (@path)

/middle performance (@src/api)
/middle security
/middle 3 (@components/)
/middle
```

* Accept the focus by **name, alias, or menu number**.
* **No focus given** → print the Focus Menu, ask which one, and wait. Do not
  guess a focus or analyze anything yet.
* **No path given** → infer the smallest relevant source scope from the
  project's entry points (`package.json`, then `pyproject.toml` → `Cargo.toml`
  → `go.mod` → `*.csproj`). Never scan the whole repository blindly.
* **Two or more focuses requested** → run only the first; after its final
  summary, offer to run the next one.

### Focus Menu

```text
🎯 [middle] What do you want to improve?

1. ⚡ performance   — speed, efficiency, wasted work
2. 🔒 security      — input handling, secrets, unsafe patterns
3. 🎨 ui-ux         — states, accessibility, consistency, feedback
4. 🏗️ structure     — file/module organization within the scope
5. 🧹 cleanup       — dead code, duplication, leftovers
6. 🧩 quality       — naming, complexity, error handling

Reply with a number or name (optionally add a @path).
```

Aliases: `perf` → performance · `sec` → security · `ui`, `ux`, `design` →
ui-ux · `arch`, `architecture` → structure · `dead-code`, `clean` → cleanup ·
`maintainability`, `refactor-lite` → quality.

---

## Operating Rules

### 1. One lens only

Analyze the scope **through the chosen focus only**. Do not report, score, or
plan anything outside the focus.

* **Exception:** a **critical** security or data-loss issue noticed outside the
  focus is surfaced in one line, report-only (`⚠️ Out of focus:`), never as a
  plan phase.
* Everything else out of focus is silently ignored — no "while I was here"
  findings, no bonus advice.

### 2. Scope & where to look

* The given path is the authorized scope. Files outside it may be **read** only
  to understand imports, entry points, config, or runtime behavior — never
  modified.
* Ignore by default: `node_modules/`, `dist/`, `build/`, `.next/`, `out/`,
  `coverage/`, `.cache/`, `.git/`, generated and minified files. Config
  dotfiles may be inspected when relevant to the focus.
* For scopes with many files, read entry points, the largest files, and
  representative files per directory — not everything. Note skipped areas in
  one `Scope note:` line.

### 3. Read-only during analysis

Do not modify, move, create, or delete any file while analyzing. Changes happen
only in approved phases.

### 4. Evidence or silence

Every finding must be backed by inspected code: file path, and
function/component/module name or line range when possible. No vague findings
("slow code", "insecure app"). Never present a risk or assumption as a
confirmed problem. If the focus looks healthy, say so and stop — do not invent
work.

### 5. Preserve behavior

Improvements must not change observable behavior unless the finding **is** the
incorrect behavior (e.g., an injection vulnerability, a broken UI state). When
a change is behavior-altering by design, mark it in the plan with
`(behavior change)`.

### 6. Tests & dependencies

* If the project has no test structure, do not create test folders, files, or
  suites in any language. Validate with the safest available method: build,
  typecheck, lint, manual verification of the affected flow.
* Do not add dependencies, change the package manager, or modify lockfiles
  unless explicitly authorized. Prefer improving existing code over adding
  packages.

### 7. Working-tree safety

Check the working tree first; if there are pre-existing user changes, mention
them before modifying anything and never overwrite or rewrite them.

---

## Focus Lenses

What to actively look for per focus. Check only what applies to the stack; skip
what doesn't exist in the scope.

### ⚡ performance

Repeated or unnecessary work · N+1 queries and request waterfalls · blocking
I/O on hot paths · inefficient loops and algorithms on real data sizes ·
missing caching or memoization **where it measurably matters** · unreleased
resources (listeners, handles, subscriptions) · oversized imports/bundles and
assets · unnecessary re-renders (UI frameworks) · work done at startup that
could be lazy.

Do not micro-optimize cold paths. Every performance finding must name the cost
(what is wasted, how often it runs).

### 🔒 security

Hardcoded secrets, tokens, or credentials · unvalidated/unsanitized input ·
injection surfaces (SQL, command, path, XSS) · unsafe `eval`/dynamic code ·
missing authorization checks on protected operations · sensitive data in logs
or error messages · permissive CORS, insecure cookies, missing critical
headers · unverified downloads or unsafe deserialization.

Confirmed exploitable issues are **critical** and always become Phase 1.

### 🎨 ui-ux

Missing loading / error / empty states · no feedback on user actions ·
accessibility: labels, alt text, focus handling, keyboard navigation, contrast,
semantic HTML · inconsistent spacing, typography, or component patterns ·
unresponsive or overflowing layouts · dead-end flows (no way back, no retry).

Respect the existing design language — align to it, do not restyle the app.

### 🏗️ structure

Oversized files with too many responsibilities · code living in the wrong
module · weak or leaky boundaries · circular dependencies · duplicated modules
· obsolete files. Scoped to the target path — this is **not** a whole-project
restructure (that is the `end` skill's job).

Report the structural direction with one of these decision blocks:

```text
Decision 1️⃣: Structure ok, nothing to move.
Why: [one short reason.]
```

```text
Decision 2️⃣: Small adjustments inside the scope.
Why: [one short reason.]

Before:                          After:

src/                             src/
├── feature-a/                   ├── feature-a/
└── large-file.ts                │   ├── index.ts
                                 │   └── helpers.ts   # extracted from large-file.ts
                                 └── large-file.ts    # smaller owner
```

If the real fix requires restructuring **beyond the scope**, say so honestly
and recommend running the `end` skill instead of forcing a partial move.

### 🧹 cleanup

Dead code and unreachable branches · unused exports, imports, variables, and
dependencies · duplicated logic worth consolidating · commented-out code
blocks · leftover debug logs and TODO corpses · obsolete files and assets.

Deleting is the point — but verify nothing references the code before removing
it (including dynamic references, config entries, and public API surface).

### 🧩 quality

Misleading or inconsistent naming · deep nesting and high complexity · empty
`catch` blocks, swallowed errors, unhandled promises · magic values that need
names · copy-paste variation of the same logic · inconsistent patterns for the
same task within the scope.

---

## Report Format

The analysis output has four parts, in this order, always compact.

### 1. Header + focus score

```text
🎯 [middle] ⚡ Performance — @src/api — 6/10
```

Score **only the chosen focus**, 0–10, honest and conservative: 9–10 nearly
nothing to do · 7–8 solid, minor gains · 5–6 clear improvements available ·
3–4 focus is hurting the project · 0–2 urgent. Do not score other dimensions.
Record this as the **baseline** for the final summary.

### 2. Understanding

Max 2 lines: what the scope does and anything that shaped the analysis.
Add `Scope note:` only if meaningful areas were skipped.

### 3. Findings

```text
⚠️ Findings:

🔴 Critical

  00. .--- --- --- --- --- --- -_- --- --- --- --- --- ---.

🟡 Improvements

  01. [short direct finding.]
  02. [short direct finding.]

🟢 Polish (Optional)

  01. [short optional item.]
```

* **🔴 Critical** — the focus is actively hurting users or the project now
  (exploitable vulnerability, real slowdown, broken UI state).
* **🟡 Improvements** — recommended in-focus gains; top 3–5 only, ordered by
  value.
* **🟢 Polish** — optional extras, max 3.
* Two-digit numbering (`01.`). Empty category → exactly
  `00. .--- --- --- --- --- --- -_- --- --- --- --- --- ---.`
* One short sentence per item, plain maintainer language; add a path only when
  needed to disambiguate.
* For the `structure` focus, insert the decision block between Findings and
  the Plan.

### 4. Plan + closing

```text
🗺️ Plan

Phase 1 — [verb + short target]
Outcome: [one concrete result.]
Files: `path/file`, `path/file`
Check: [typecheck + lint | build | manual verification]
```

* **1–3 phases** by default, 5 max — each phase maps to a specific finding.
  This is targeted improvement, not a project overhaul; if the work honestly
  needs more than 5 phases, say the scope is too big for `middle` and suggest
  narrowing the path or running `end`.
* Critical findings jump the queue and become Phase 1.
* Phase names start with a verb and name the target: ✅ `Cache repeated user
  lookups in session.ts` ❌ `Improve performance`.
* Do not turn 🟢 Polish items into phases unless the user asks.
* Mark new files `(new)`, deletions `(delete)`, behavior-altering fixes
  `(behavior change)`.

End every analysis with exactly:

```text
Any questions?
If not, I'll start with Phase 1.

🚀 Ready when you are.
```

If the focus is healthy (no 🔴, no 🟡), skip the plan and close with:

```text
✅ [focus] looks solid here — nothing worth changing.
```

---

## Execution

Execute only on explicit approval: `go`, `start`, `proceed`, `dale`, `do it`,
`approved`, or a clear equivalent. Ambiguous replies (`what do you think?`,
`maybe`) are discussion, not authorization.

On approval, execute **only the first pending phase**, then stop and report:

```text
✅ Phase N complete — [phase name]

Changed files:
- `path/file` — what changed and why

Validations:
- [command or method] — [passed | failed | not run + reason]

Remaining:
- Phase N+1 — [name]

Continue with Phase N+1?
```

Wait for confirmation between phases. For the **last phase**, skip the
per-phase report and go straight to the final summary. Before each phase:
detect the package manager, pick the safest validation commands, and stay
inside the authorized scope. Run the validations after every change and report
failures honestly.

### Final Summary

```text
## [Focus] Improved 🎉

⚡ Performance  6/10 → 8/10   ▲ +2

### What was done
- ✅ Phase 1 ([name]) — [1-line summary] ([impact metric])
- ✅ Phase 2 ([name]) — [1-line summary] ([impact metric])

Would you like the 🟢 polish items too?
```

Re-score the focus with the same rubric; only resolved findings may raise the
score, and open 🟡 items keep counting against it. Show `▲ +0` honestly if
nothing improved. Ask the polish question only when 🟢 items exist; if the user
accepts, implement simple ones directly and plan complex ones as phases; if
they decline, close with exactly `Improvement Complete 🎉`.

---

## Philosophy

One focus, one scope, one clear win at a time. `middle` behaves like a senior
engineer doing a focused pass during active development: it sharpens the one
thing you asked about, proves the gain, and leaves everything else exactly as
it found it. For whole-project diagnosis and deep refactoring, use `end`.
