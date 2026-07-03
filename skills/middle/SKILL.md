---
name: middle
description: "Interactive project analysis skill. Option 1: scored health overview (0-100) with emoji table across Architecture, Maintainability, Performance, Security, Documentation plus Bug/Debt/Suggestion counts. Option 2: architecture analysis with structural decisions. Invoke with /skill analyze (@path) <1|2>"
license: Complete terms in LICENSE.txt
metadata:
  author: bastndev
  version: "1.0.0"
---

# Analyze / [Middle]

Interactive project analysis skill. Call it with a target path and an option number:

```
/skill analyze (@src/) 1
/skill analyze (@src/) 2
```

---

## Option 1 — Health Overview (Scored 0–100)

Analyze the target, score it from 1–100 across these dimensions, and display the result:

```
📊 [end] Health Overview — 74 / 100

🔴 Bugs 1    🟡 Debt/Risks 3    🟢 Suggestions 2

🏗️ Architecture     7/10
🧩 Maintainability  6/10
⚡ Performance       8/10
🔒 Security          5/10
📚 Documentation     7/10
```

A scored overview, findings sorted into Bugs / Debt / Suggestions, one architecture decision, and a phased plan — executed one phase at a time on your `go`.

### Reading the Score

The overall score is a **0–100** thermometer:

| Score | Meaning |
| ----- | ------- |
| **0–40** | 🚨 Critical — hard to maintain, risky to change |
| **40–60** | 🔴 Heavy debt — significant refactoring recommended |
| **60–70** | 🟡 Needs improvement — works, but address debt before production |
| **70–80** | 🟢 Production-ready — solid, maintainable code |
| **80–90** | ⭐ Excellent — clean architecture, praise-worthy |
| **90–100** | 🏆 Outstanding — reference-grade codebase |

---

## Option 2 — Architecture Analysis

Analyze the target's structure and output the appropriate architecture decision format.

### Decision 1 — Architecture OK

```
🏗️ Architecture

Decision 1️⃣:
Architecture ok, ready for work.

Why: [one short reason.]
```

### Decision 2 — Small adjustments needed

Show only the affected paths:

```
🏗️ Architecture

Decision 2️⃣:
Small architecture adjustments needed.

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

### Decision 3 — Restructure recommended

Show the proposed structure only:

```
🏗️ Architecture

Decision 3️⃣:
Restructure architecture recommended.

Why: [one short reason.]

Proposed structure:

src/
├── core/                       # shared foundations
├── features/                   # feature-owned modules
├── shared/                     # reusable UI/helpers
├── infrastructure/             # external services/config
└── app/                        # startup/routes/bootstrap
```
