---
name: middle
description: "Focused, on-demand project improver for active development. Option 0 scores the project or folder with a 0–100 health overview (Architecture, Maintainability, Performance, Security, Documentation), report-only. Options 1–6 improve ONE dimension at a time — performance (1), UI/UX (2), security (3), structure (4), cleanup/dead code (5), code quality (6) — scoring the focus 0–100, proposing a correction plan, and executing only with explicit approval. Use for 'score my project', 'harden security in src/api', 'speed up this page', 'clean dead code'. Invoke with /middle <0-6|focus> (@path)"
license: Complete terms in LICENSE.txt
metadata:
  author: bastndev
  version: "2.1.2"
---

# Improve / [Middle]

A focused improvement skill for projects in active development. Unlike a full
audit, it improves **one dimension at a time** — the one the user asks for —
inside the scope they point at. Option 0 first scores the whole scope so the
user knows where to aim. Small surface, fast diagnosis, surgical changes,
explicit approval before any edit.

`middle` sits between scaffolding (**Start**) and full refactoring (**End**):
the project already exists and works; the goal is to raise one specific quality
bar without touching anything else.

## Invocation

```
/middle <option|focus> (@path)

/middle 0                    # health overview of the inferred scope
/middle (@src/) 0            # health overview of src/ only
/middle (@src/) 1            # performance improvement in src/
/middle security             # names and aliases also work
/middle
```

* Accept the option by **menu number, name, or alias**. Path and number may
  come in either order (`/middle src 0` = `/middle 0 (@src/)`).
* **Natural language works too** — a request that clearly names one dimension
  maps straight to its focus without showing the menu: "make this page faster"
  → 1 · "polish the UI of the gallery" → 2 · "harden security in src/api" →
  3 (@src/api) · "clean the dead code" → 5.
* **No option given, or ambiguous request** ("improve my project") → print the
  Menu, ask which one, and wait. Do not guess an option or analyze anything
  yet. Same for an invalid option (`/middle 9`, unknown name).
* **Option lost in transport** — some IDE wrappers rewrite the prompt and drop
  arguments, delivering only a path or file. Treat that as "no option given":
  show the Menu with a `Scope detected:` line and wait.
* **No path given** → analyze the general project, discovering scope the same
  way the `end` skill does: find `package.json` and follow its entry points.
  If absent, look in order and adapt to the runtime: `pyproject.toml` →
  `Cargo.toml` → `go.mod` → `*.csproj`. If none exist, inspect root-level
  files first, infer the runtime, then choose the smallest relevant source
  scope. In a monorepo, analyze only the workspace tied to the request. Never
  scan the entire repository blindly.
* **Two or more focuses requested** → run only the first; after its final
  summary, offer to run the next one.

### Menu

```text
🎯 [middle] What do you want?

0. 📊 overview      — score the whole scope (statistics only)

1. ⚡ performance   — speed, efficiency, wasted work
2. 🎨 ui-ux         — states, accessibility, consistency, feedback
3. 🔒 security      — input handling, secrets, unsafe patterns
4. 🏗️ structure     — file/module organization within the scope
5. 🧹 cleanup       — dead code, duplication, leftovers
6. 🧩 quality       — naming, complexity, error handling

Reply with a number or name (optionally add a @path).
```

If a path or file already arrived with the request, append one line to the
menu — `Scope detected: src/style.css — [very short description]` — and reuse
that scope when the user replies with just a number.

Aliases: `overview`, `health`, `score` → 0 · `perf` → performance · `ui`,
`ux`, `design` → ui-ux · `sec` → security · `arch`, `architecture` →
structure · `dead-code`, `clean` → cleanup · `maintainability`,
`refactor-lite` → quality.

**The contract of every number:** option `0` delivers statistics only — score
and findings, no plan, no edits. Every focus option `1–6` behaves identically
to the others: it qualifies that one dimension (score + counts), reports
evidence-backed findings, and proposes a correction plan with the solution —
executed phase by phase only when the user says `go`.

**Workflow:** 1. Resolve option + scope. 2. Analyze (read-only). 3. Report —
score, findings, plan. 4. Wait for `go`. 5. Execute one phase, report, wait.
6. Final summary with before → after. Option 0 stops at step 3.

---

## Option 0 — 📊 Health Overview (report-only)

Score the target scope across all dimensions and deliver a diagnosis. **No
plan, no edits** — option 0 never modifies files and never proposes phases;
its job is to tell the user where the project stands and which focus (1–6) is
worth running next.

```text
📊 my-project Health Overview — 74 / 100

🔴 Bugs 1    🟡 Debt/Risks 3    🟢 Suggestions 2

🏗️ Architecture     7/10
🧩 Maintainability  6/10
⚡ Performance       8/10
🔒 Security          5/10
📚 Documentation     7/10
```

`my-project` is a placeholder — replace it with the analyzed project's real
name, written **without square brackets**: the manifest name (`package.json`
`name`, `Cargo.toml` `[package].name`, etc.) or, if none, the root folder
name. The skill is global; nothing about it is tied to any one project. Keep the rest of
the title shape exact. If existing tests are present, insert
`🧪 Testing [x/10]` before Documentation; if no test structure exists, omit
the bar entirely (never `0/10`).

After the block, add:

1. **Understanding** — max 2 lines: what the scope is and anything that shaped
   the analysis. Add `Scope note:` only if meaningful areas were skipped.
2. **Findings** — the same compact block as focus runs (see Report Format),
   but with option-0 labels: `🔴 Bugs` (confirmed incorrect behavior only,
   marked `critical` / `non-critical`) · `🟡 Debt / Risks` (top 3–5) ·
   `🟢 Suggestions (Optional)` (max 3).
3. **Next step** — close by pointing at the weakest bar and its focus number:

```text
Weakest bar: 🔒 Security 5/10 — run `/middle (@src/) 3` to improve it.
```

Bar → focus mapping: ⚡ Performance → 1 · 🔒 Security → 3 · 🏗️ Architecture →
4 (structure) · 🧩 Maintainability → 6 (quality). If 📚 Documentation is the
weakest, mention it as debt (no dedicated focus; the `end` skill covers docs).

### Scoring the overview

Score 0–100 overall plus each category 0–10. Be honest and conservative; do
not invent issues to justify a low score, and say when an area cannot be
judged from the scope. Calibrate: greenfield/no debt 85–92 · maintained
production codebase 62–80 · legacy with known debt 40–62. Never score above 80
with 3+ Debt/Risk items, or above 90 with any.

| Score | Meaning |
| ----- | ------- |
| **0–40** | 🚨 Critical — hard to maintain, risky to change |
| **40–60** | 🔴 Heavy debt — significant refactoring recommended |
| **60–70** | 🟡 Needs improvement — works, but address debt before production |
| **70–80** | 🟢 Production-ready — solid, maintainable code |
| **80–90** | ⭐ Excellent — clean architecture, praise-worthy |
| **90–100** | 🏆 Outstanding — reference-grade codebase |

---

## Operating Rules

### 1. One lens only

These rules govern both option 0 and focus runs; option 0 additionally never
plans or edits. For focus runs (1–6), analyze the scope **through the chosen
focus only**. Do not report, score, or plan anything outside the focus.

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
work. Two precision rules:

* **Cite line numbers only when verified** by reading the file in this
  session; otherwise name the element, function, or section instead. A wrong
  line number is worse than none.
* **Measure once, reuse everywhere.** Sizes, counts, and totals must be
  consistent across the whole report — never two different figures for the
  same thing (e.g., "75 MB of assets" in one section and "46 MB" in another).

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

### 8. Speak the user's language

Write the Understanding, findings, plan outcomes, and explanations in the
language the user is using (Spanish request → Spanish report). The fixed
structure never translates: emoji, section titles, category labels
(`Critical` / `Improvements` / `Polish`), phase line keys (`Outcome`, `Files`,
`Check`), and the closing lines stay exactly as defined.

---

## Focus Lenses

What to actively look for per focus. Check only what applies to the stack; skip
what doesn't exist in the scope.

### 1 — ⚡ performance

Repeated or unnecessary work · N+1 queries and request waterfalls · blocking
I/O on hot paths · inefficient loops and algorithms on real data sizes ·
missing caching or memoization **where it measurably matters** · unreleased
resources (listeners, handles, subscriptions) · oversized imports/bundles and
assets · unnecessary re-renders (UI frameworks) · work done at startup that
could be lazy.

Do not micro-optimize cold paths. Every performance finding must name the cost
(what is wasted, how often it runs). Verify default runtime/browser behavior
before labeling something critical — e.g., `<audio controls>` preloads only
metadata by default, not the full file; an unlinked script never executes.

### 2 — 🎨 ui-ux

Missing loading / error / empty states · no feedback on user actions ·
accessibility: labels, alt text, focus handling, keyboard navigation, contrast,
semantic HTML · inconsistent spacing, typography, or component patterns ·
unresponsive or overflowing layouts · dead-end flows (no way back, no retry).

Respect the existing design language — align to it, do not restyle the app.

### 3 — 🔒 security

Hardcoded secrets, tokens, or credentials · unvalidated/unsanitized input ·
injection surfaces (SQL, command, path, XSS) · unsafe `eval`/dynamic code ·
missing authorization checks on protected operations · sensitive data in logs
or error messages · permissive CORS, insecure cookies, missing critical
headers · unverified downloads or unsafe deserialization.

Confirmed exploitable issues are **critical** and always become Phase 1.

### 4 — 🏗️ structure

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

### 5 — 🧹 cleanup

Dead code and unreachable branches · unused exports, imports, variables, and
dependencies · duplicated logic worth consolidating · commented-out code
blocks · leftover debug logs and TODO corpses · obsolete files and assets.

Deleting is the point — but verify nothing references the code before removing
it (including dynamic references, config entries, and public API surface).

### 6 — 🧩 quality

Misleading or inconsistent naming · deep nesting and high complexity · empty
`catch` blocks, swallowed errors, unhandled promises · magic values that need
names · copy-paste variation of the same logic · inconsistent patterns for the
same task within the scope.

---

## Report Format (focus runs 1–6)

The analysis output has four parts, in this order, always compact. A
horizontal separator line (`────…`) between parts is optional and welcome —
it applies to option 0's report too.

### 1. Header + focus score

Same visual shape as option 0's overview, but with **only the chosen focus**:

```text
📊 my-project 🎨 UI/UX Overview — 46 / 100

🔴 Critical 1    🟡 Improvements 4    🟢 Polish 2
```

The project name follows the same rule as option 0 (manifest name, else root
folder name, no square brackets). The counts row uses the focus categories (Critical /
Improvements / Polish), not option 0's Bugs / Debt / Suggestions. Score the
focus **0–100** on the same thermometer as option 0, honest and conservative:
90–100 nearly nothing to do · 70–89 solid, minor gains · 50–69 clear
improvements available · 30–49 the focus is hurting the project · 0–29 urgent.
Do not score or display other dimensions. Record this as the **baseline** for
the final summary. If option 0 already ran in this session, keep the focus
score coherent with its category bar (bar × 10 as the starting point); deviate
only when deeper reading justifies it, and say why in the Understanding.

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
      ↳ `path/file` — [exact location + one evidence detail.]
  02. [short direct finding.]

🟢 Polish (Optional)

  01. [short optional item.]
```

* **Always two-digit numbering**: `01.`, `02.`, `03.` — never `1.`, `2.`.
  Empty category → exactly
  `00. .--- --- --- --- --- --- -_- --- --- --- --- --- ---.`
* **🔴 Critical** — the focus is actively hurting users or the project now
  (exploitable vulnerability, real slowdown, broken UI state).
* **🟡 Improvements** — recommended in-focus gains; top 3–5 only, ordered by
  value.
* **🟢 Polish** — optional extras, max 3.
* Each item is **one short sentence** in plain maintainer language, optionally
  followed by a single indented `↳` evidence line with the exact path and
  location. Never more than two lines per item; put deeper detail in the plan,
  not the findings.
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
* Every phase must be executable **now** — no conditional or speculative
  phases ("only if components are added later"). If a fix depends on a future
  decision, it is a 🟢 Polish note, not a phase.
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
`maybe`) are discussion, not authorization. Two edge cases:

* Approval bundled with the invocation (`/middle 1 go`) does **not** skip the
  report — analyze, present the report, and wait anyway.
* `go` after option 0 → there is nothing to execute; ask which focus (1–6) to
  run.

On approval, execute **only the first pending phase**, then stop and report:

```text
✅ Phase N complete — [phase name]

Changed files:
- `path/file` — what changed and why

Validations:
- [command or method] — [passed | failed | not run + reason]

Impact: [one metric, e.g. nav usable at 375 px · -420 lines · 0 hardcoded secrets]

Remaining:
- Phase N+1 — [name]

Continue with Phase N+1?
```

Wait for confirmation between phases. For the **last phase**, skip the
per-phase report and go straight to the final summary. Before each phase:
detect the package manager, pick the safest validation commands, and stay
inside the authorized scope. Run the validations after every change and report
failures honestly. For move, extract, or delete phases (structure, cleanup),
confirm the relocated code is logic-identical and deleted code is truly
unreferenced before reporting the phase complete.

### Final Summary

```text
## [Focus] Improved 🎉

🎨 UI/UX  46 / 100 → 78 / 100   ▲ +32

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

## Examples

* `/middle 0` → health overview of the whole project. Statistics only, ends
  with the weakest-bar pointer.
* `/middle (@src/api) 3` → security qualification + findings + plan for
  `src/api`; waits for `go`.
* **"make the gallery page faster"** → focus 1 on that page's scope directly,
  no menu.
* **"improve my project"** → ambiguous; show the Menu and wait.
* **`go` after a focus report** → execute Phase 1 only, report, wait.
* **`go` after option 0** → nothing to execute; ask which focus to run.
* **Focus looks healthy** → `✅ [focus] looks solid here — nothing worth
  changing.` and stop.

---

## Philosophy

One focus, one scope, one clear win at a time. `middle` behaves like a senior
engineer doing a focused pass during active development: it sharpens the one
thing you asked about, proves the gain, and leaves everything else exactly as
it found it. For whole-project diagnosis and deep refactoring, use `end`.
