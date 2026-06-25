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
  see Step 4's `SKILLS.md` for what to do with these. Also check for a
  `skills-lock.json` at the project root — when present, it maps installed
  skill names to their real source repos, used later in `PROMPT.md`'s
  Skills section.
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

Always produce these three:

- **`ARCHITECTURE.md`**
- **`PACKAGES.md`**
- **`PROMPT.md`** — write this one last, since it pulls from the other two.

Add these only when they earn their place — don't pad the folder with empty
or near-duplicate files:

- **`STATE-MANAGEMENT.md`** — split this out only if state management is
  non-trivial (multiple stores, cross-island/cross-screen state, a notable
  custom solution) — otherwise a paragraph inside `ARCHITECTURE.md` is enough.
- **`STYLING.md`** — split out only if the styling approach is layered or
  unusual (e.g. a custom design-token system, multiple competing approaches
  found in the same repo) — otherwise covered briefly in `ARCHITECTURE.md`.
- **`SKILLS.md`** — only if the project has a `.claude/skills/` or
  `.agents/skills/` folder **and** it contains at least one skill besides
  `skrapi` itself. If `skrapi` is the only skill found there, skip this file
  entirely — a file whose only content is "this project has skrapi" isn't
  useful information, since the user already knows that. If there's at least
  one other skill alongside it, create the file normally and include `skrapi`
  in the list too, like any other skill found.

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

### `PROMPT.md`

Always create this one, written last since it pulls from `ARCHITECTURE.md`,
`PACKAGES.md`, and — when it exists — `SKILLS.md`. All three sections
(Architecture, Packages, Skills) always appear in `PROMPT.md` — this is
independent from whether the `SKILLS.md` *file* itself gets created (that
file stays conditional, per Step 4 above). When `SKILLS.md` wasn't created
this run, the Skills section here still appears, just with the no-skills
message instead of real skill install commands — see rules below.

```markdown
# Prompts — <project name>

## 🏗️ Architecture

<1-2 sentences, in the language chosen in Step 0: name the actual pattern
found — DDD, hexagonal, clean architecture, islands architecture, etc. If
the project rolled its own approach instead of a named one, describe it
plainly rather than forcing it into a label that doesn't fit.>

```
<a single self-contained prompt asking the reader's own AI agent to
implement this same pattern in their project, grounded in the real
structure/decisions from ARCHITECTURE.md — always written in English, no
matter what language the rest of this file is in>
```

## 📦 Packages

<1-2 sentences, in the language chosen in Step 0: name the project's main
framework, the detected package manager, how many dependencies it has,
and call out any that PACKAGES.md flagged as not actually used in the
code — don't just describe what the packages are for in the abstract.>

```
npm i package-example
```

<br>

```
npm i package-example
```
<!-- one fenced block per package; `<br>` goes BETWEEN blocks only, never
before the first one or after the last one — see rules below for which
install verb to use, source, ordering, and the empty-state message -->

## 🤖 Skills

<1-2 sentences, in the language chosen in Step 0, naming the skill(s)
found — or, if there are none, saying plainly that this project has no
custom skills installed.>

<br>

⯈ **skill-example**
```
npx skills add https://github.com/owner-example/repo-example --skill skill-example
```

<br>

⯈ **skill-example**
```
skill-example
```

<br>
<!-- one labeled+fenced pair per skill, each preceded by its own `<br>` —
including before the first pair — see rules below for which form each
block takes, ordering, and the empty-state message -->

Rules for the **📦 Packages** blocks specifically:

- One fenced code block per package — never combine multiple packages into
  a single block or a single multi-package command. Each block contains
  exactly one line: the install command for the detected package manager
  plus the package's real name from `package.json` (not the placeholder
  `package-example` shown above).
- Put a `<br>` on its own line **between** consecutive package blocks
  only — never before the first block, never after the last one. This is
  what creates visible separation between packages when rendered, without
  adding stray whitespace at either end of the section. Don't add `<br>`
  anywhere else in this file (Architecture blocks don't get one).
- Detect which package manager the project actually uses by checking for
  its lockfile at the project root: `bun.lockb` or `bun.lock` → Bun,
  `yarn.lock` → Yarn, `pnpm-lock.yaml` → pnpm, `package-lock.json` → npm.
  Use that manager's real install verb for every package block in this
  project: `bun add <package-name>`, `yarn add <package-name>`,
  `pnpm add <package-name>`, or `npm i <package-name>`. All package blocks
  for a given project use the same detected manager — never mix verbs
  within one `PROMPT.md`.
- If no lockfile is found, default to `npm i <package-name>`.
- Never add a dev-install flag (`-D`/`--save-dev`/`-d`) to any of these
  commands, even when falling back to `devDependencies` below.
- Source and list **every** package found in `dependencies`, in the order
  they appear in `package.json` — not a curated highlight subset. Include
  a dependency here even if `PACKAGES.md` noted its usage wasn't clearly
  detected in the code; being listed in `dependencies` is enough.
- Only fall back to listing `devDependencies` (same one-block-per-package,
  same plain install-verb format, no dev flag) when `dependencies` is
  completely empty.
- If both `dependencies` and `devDependencies` are empty, skip the fenced
  blocks entirely and write a single line instead:
  `>- This project doesn't have any package installed 🚫`

Rules for the **🤖 Skills** blocks specifically:

- One labeled fenced block per skill found — never combine multiple skills
  into a single block or a single multi-skill command, mirroring how
  Packages handles multiple packages.
- Each skill gets a `⯈ **<skill-name>**` line directly above its fenced
  block (no blank line between the label and the block), using the
  skill's real name.
- Put a `<br>` on its own line before every labeled skill block, including
  before the first one — this is what creates visible separation between
  skills when rendered. Don't add `<br>` anywhere else in this file
  (Architecture and Packages blocks don't get one).
- For each skill, look for a `skills-lock.json` file at the project root.
  If it exists, check whether the skill's name is a key in its `skills`
  object.
  - If the skill is found there: read its `source` field (an
    `owner/repo` string) and write
    `npx skills add https://github.com/<source> --skill <skill-name>`,
    using the real values from the lock file (not the placeholders shown
    above). The `https://github.com/` prefix is always used here,
    regardless of `sourceType`.
  - If `skills-lock.json` doesn't exist, or exists but has no entry for
    that skill's name: fall back to a block containing only the skill's
    name on its own line, exactly as it appears in `.claude/skills/` or
    `.agents/skills/` (e.g. `skrapi`) — nothing else, no invented URL, no
    git-remote lookup, no guessed repo. The `⯈ **<skill-name>**` label
    above it still applies the same way.
- List every skill found this run (the same set documented in `SKILLS.md`,
  including `skrapi` itself when it's listed there), in the same order
  they appear on disk.
- If no skills were found (no `SKILLS.md` this run), don't omit the
  section — instead write a single line in the fenced block, in English,
  with no `⯈` label and no leading `<br>`:
  `>- This project doesn't have any skill installed 🚫`
  The 1-2 sentence explanation above the block should say the same thing
  in the language chosen in Step 0.

Rule that applies to **all fenced prompt blocks** (Architecture, Packages,
and Skills): the text *inside* the triple backticks is always written in
English, regardless of the language chosen in Step 0 — including both the
real install commands and either empty-state message. The 1-2 sentence
explanation around each block is what stays in the user's chosen language,
not the contents of the block itself.

Keep all blocks paste-ready as-is and don't blend them: the Architecture
block is text meant for an AI agent to read; each Packages and each
Skills block is a literal command or bare name to copy-paste — no
commentary inside any fenced block.

### `SKILLS.md` (only if there's at least one skill besides `skrapi` itself)

This file documents the custom skills available to AI tools in this repo —
nothing else. Don't summarize the root `AGENTS.md`/`CLAUDE.md` instruction
files anywhere in it; those are standing instructions for AI agents, not
something this file is for.

If `skrapi` is the only skill present in `.claude/skills/` or
`.agents/skills/`, don't create this file at all — skip it silently, same as
when no skills folder exists. Once there's at least one other skill, create
the file and include `skrapi` in the list along with the rest — it's fine to
describe what `skrapi` itself does at that point, the same way any other
skill entry gets described.

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

Write this message entirely in the language chosen in Step 0 — including
the intro line and the closing line, not just the surrounding prose. Use
the matching shape below for whichever language was chosen (translate
naturally rather than transliterating word-for-word if none of these
exact wordings fit the conversation's tone):

**If ES was chosen:**
```markdown
He creado `SKRAPI/` con <N> archivos:

1. `ARCHITECTURE.md` (<line count> líneas)
2. `PACKAGES.md` (<line count> líneas)
3. `PROMPT.md` (<line count> líneas)
4. `SKILLS.md` (<line count> líneas)  <!-- only if it was created -->

Archivos creados con éxito 🎉
```

**If EN was chosen:**
```markdown
I've created `SKRAPI/` with <N> files:

1. `ARCHITECTURE.md` (<line count> lines)
2. `PACKAGES.md` (<line count> lines)
3. `PROMPT.md` (<line count> lines)
4. `SKILLS.md` (<line count> lines)  <!-- only if it was created -->

Files created successfully 🎉
```

**If ZH was chosen:**
```markdown
我已创建 `SKRAPI/`，共 <N> 个文件：

1. `ARCHITECTURE.md`（<line count> 行）
2. `PACKAGES.md`（<line count> 行）
3. `PROMPT.md`（<line count> 行）
4. `SKILLS.md`（<line count> 行）  <!-- only if it was created -->

文件创建成功 🎉
```

Just the file list with line counts and that closing line — no bullets
underneath each file describing its sections, no restating the skill's own
principles back to the user.
