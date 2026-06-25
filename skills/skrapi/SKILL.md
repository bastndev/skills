---
name: skrapi
description: Analyzes the architecture of any software project — web, mobile, browser extension, or npm package/library, in any JS/TS stack (Next.js, Astro, React Native, Expo, Lynx JS, Vite, etc.) or other languages if needed — and produces a folder of focused Markdown files covering architecture and packages/dependencies. Use whenever the user wants to understand or document an existing codebase; wants to study another project's structure for inspiration before applying ideas to their own (e.g. "estoy analizando este repo para aprender"); or asks which package handles something specific (dark/light mode, routing, state management, forms, i18n) and whether one exists. Trigger even without the word "architecture" — "ayúdame a entender este proyecto", "qué packages usa y para qué", "analiza la estructura de este repo" all qualify.
license: MIT
metadata:
  author: bastndev
  version: "1.0.0"
---

# Architecture Analyzer

## Why this skill exists

Reading an unfamiliar codebase is slow. The goal here isn't to produce one giant
file that nobody reads — it's to produce a handful of *focused* documents, each
answering one kind of question, so a human (or another AI session with no prior
context) can get oriented in minutes instead of hours.

This skill is deliberately stack-agnostic. The user might point it at a Next.js
app one day and a React Native + Lynx JS mobile app the next. Don't assume the
shape of the project — detect it first, then read the matching reference file
for what to look for.

## Step 0 — Ask which language to write the docs in

Before doing anything else, ask the user which language they want the output
files written in. Offer exactly three options, each with its flag emoji:
🇪🇸 **ES** (Spanish), 🇺🇸 **EN** (English), 🇨🇳 **ZH** (Chinese). If there's no
answer, don't block on it — default to **EN** and proceed.

## Step 1 — Actually look at the project, don't assume

Before writing anything, inspect the real files. Never describe a dependency's
purpose from its name alone — confirm it by checking where/how it's actually
imported and used in the code. A stale or guessed description is worse than no
description.

Useful signals to check, roughly in this order:

- `package.json` — `dependencies`, `devDependencies`, `scripts`, `type` (module
  vs commonjs), `exports`/`main`/`module`/`types` fields
- Framework config files: `next.config.*`, `astro.config.*`, `vite.config.*`,
  `remix.config.*`, `svelte.config.*`, `nuxt.config.*`
- Mobile signals: `app.json`/`app.config.js` (Expo), `ios/`/`android/` native
  folders, `lynx.config.*` or similar for Lynx JS
- Extension signals: `manifest.json` with a `manifest_version` field
- Monorepo signals: `turbo.json`, `nx.json`, `pnpm-workspace.yaml`, `lerna.json`
  — if present, there may be several projects to classify separately
- `tsconfig.json` (path aliases often reveal the intended module structure)
- AI-tooling signals: a `.claude/` folder (commands/skills/agents for Claude
  Code), an `.agents/` folder, or root files like `CLAUDE.md`/`AGENTS.md` —
  see Step 4's `SKILLS.md` for what to do with these
- The top 2 levels of the directory tree, ignoring `node_modules`, build output,
  and lockfiles

## Step 2 — Classify the project, then read the matching reference file

Based on what Step 1 turned up, pick the closest match and open the
corresponding file under `references/` **before** writing any output — it
tells you what's actually worth checking for that kind of project so you don't
default to generic boilerplate observations.

| If the project looks like...                          | Read              |
|---------------------------------------------------------|-------------------|
| A website/web app (Next.js, Astro, Vite, Remix, Nuxt...) | `references/web.md` |
| A mobile app (React Native, Expo, Lynx JS)             | `references/mobile.md` |
| A browser extension (has `manifest.json`)              | `references/extension.md` |
| An npm package/library/CLI meant to be consumed by other code | `references/library.md` |
| A monorepo with several of the above                  | Read each relevant reference file for the corresponding package/app inside |
| Something outside JS/TS entirely (Python, Go, Swift native, etc.) | No reference file needed — apply the same general structure below using your own judgment, and say so plainly in `ARCHITECTURE.md` so the user knows this is best-effort outside the skill's main focus |

## Step 3 — Decide on the output folder

Create **one folder named `SKRAPI`** holding everything this run produces.
Don't scatter the files loose next to the code, and don't rename this folder
per project — `SKRAPI` is this skill's fixed, recognizable folder name, the
same way a tool might always create a `.github/` or `.vscode/` folder.

- If the user already named a target location (e.g. `~/analices/`), create
  `SKRAPI/` inside it.
- Otherwise, default to creating `SKRAPI/` at the root of the analyzed
  project.
- For a monorepo, nest one subfolder per app/package you analyzed inside
  `SKRAPI/` instead of mixing everything into shared files.

## Step 4 — Write the files

Always produce these two:

- **`ARCHITECTURE.md`**
- **`PACKAGES.md`**

Add these only when they earn their place — don't pad the folder with empty
or near-duplicate files:

- **`STATE-MANAGEMENT.md`** — split this out only if state management is
  non-trivial (multiple stores, cross-island/cross-screen state, a notable
  custom solution) — otherwise a paragraph inside `ARCHITECTURE.md` is enough.
- **`STYLING.md`** — split out only if the styling approach is layered or
  unusual (e.g. a custom design-token system, multiple competing approaches
  found in the same repo) — otherwise covered briefly in `ARCHITECTURE.md`.
- **`RECOMMENDATIONS.md`** — only when the user has signaled they're studying
  this project to bring ideas back to *their own* project. If you don't
  already know their stack from the conversation, ask before writing this
  file — a recommendation is only useful when it's a concrete comparison
  against something real, not generic advice.
- **`SKILLS.md`** — only if the project has a `.claude/skills/` or
  `.agents/skills/` folder. If neither exists, this is simply not part of the
  project — don't create the file and don't mention its absence elsewhere.

Write every file in the language chosen in Step 0.

### `ARCHITECTURE.md`

Use this shape:

```markdown
# Architecture — <project name>

## Summary
3-4 sentences: what this project is, the main stack, and the one or two
architectural decisions that most define how it's built.

## Stack
Framework + version, language (JS/TS), runtime/rendering model.

## Directory structure
Annotated tree of the folders that matter (skip node_modules, dist, .git).
Each entry gets a one-line "what lives here and why".

## Rendering / execution model
Web: SSR vs SSG vs ISR vs CSR vs islands, and which adapter/target.
Mobile: native bridge model, JS engine, how screens mount.
Extension: background/content-script/popup relationship.
Library: entry points and what's actually exported.

## Routing / navigation
How routes or screens are defined and connected.

## Data flow & state
Where state lives, how data moves between pieces, what fetches what.

## Diagram
A Mermaid diagram of the main flow (request→render, or screen→screen nav,
or background↔content↔popup messaging — whatever fits the project type).

## Notable patterns
Things worth learning from.

## Things to question
Decisions that look like trade-offs, technical debt, or wouldn't generalize
well to a smaller project — flagged plainly, not just praise.
```

### `PACKAGES.md`

Split into `dependencies` and `devDependencies`. For each: version, and a
one-line description of what it does **in this project specifically** (verify
by checking actual usage, not the package's generic tagline).

Then close with a **"Common needs check"** section — this is the part users
most often want when they're comparing against their own project. Go through
this list and for each one say which package (if any) handles it, or that
there isn't one and how the project does it instead (custom code, a few lines
of CSS, manually, or not at all):

- Dark/light mode (theming)
- State management
- Forms & validation
- Routing/navigation
- Animations
- Internationalization (i18n)
- Data fetching/caching
- Testing
- Linting/formatting

Skip any item that's clearly inapplicable to the project type (e.g. dark mode
for a build-tool CLI) rather than forcing an entry.

### `RECOMMENDATIONS.md` (only when applicable)

For each idea worth borrowing: what it is, where to see it in this project,
why it'd help the user's own project specifically, and a short code sketch of
how to apply it — not just the abstract idea. Also call out anything that's
*not* worth copying (over-engineering, or a decision that only makes sense at
that project's scale/team size).

### `SKILLS.md` (only if `.claude/skills/` or `.agents/skills/` exists)

This file documents the custom skills available to AI tools in this repo —
nothing else. Don't summarize the root `AGENTS.md`/`CLAUDE.md` instruction
files anywhere in it; those are standing instructions for AI agents, not
something this file is for.

Keep it to exactly the list below — no overview paragraph before it, and
nothing after it. No "skills not used yet" section, no "how skills work"
explainer, no comparison to other AI tooling (Cursor, Copilot, etc.), no
"notable decisions" wrap-up. The list itself is the deliverable; resist the
pull to add framing text around it:

```markdown
## Skills (.claude/skills/)
<!-- or `## Skills (.agents/skills/)` — use whichever convention this
     project actually has -->

### 1. **skill-name**
What it specializes in (a few bullets if it covers multiple areas, plus a
file count if it has a non-trivial `references/`/`rules/` folder).
**Triggers**: when it activates.

### 2. **next-skill-name**
...
```

List every skill found, in the order they appear on disk — don't drop any,
and don't editorialize about which ones look unused or redundant unless the
user separately asks for that kind of review.

If the project also has `.claude/commands/` or `.claude/agents/` (or the
`.agents/` equivalents), add them as their own short sections right after the
skills list, in the same plain style — still no extra narrative:

```markdown
## Commands (.claude/commands/)
- `/command-name` — what it does

## Subagents (.claude/agents/)
- `agent-name` — what it specializes in
```

Only add one of these sections if that folder actually exists.

## Step 5 — Be honest about scale

For a huge codebase, completeness is the wrong goal. Say clearly in
`ARCHITECTURE.md` which folders/areas you focused on and which you
deliberately skipped, so the user knows the docs are a map, not a full
transcript.

## Step 6 — Closing summary

Once the files are written, give a short closing message — not a recap of
everything each file contains, since the user can just open the files for
that. The summary's only job is to confirm what exists and where, fast.

Use this shape (adapt the wording to the language chosen in Step 0):

```markdown
He creado `SKRAPI/` con <N> archivos:

1. `ARCHITECTURE.md` (<line count> líneas)
2. `PACKAGES.md` (<line count> líneas)
3. `SKILLS.md` (<line count> líneas)  <!-- only if it was created -->

Archivos creados con éxito 🎉
```

Just the file list with line counts and that closing line — no bullets
underneath each file describing its sections, no restating the skill's own
principles back to the user.