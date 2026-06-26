---
name: start-astro
description: Scaffold a new Astro project (minimal template) with a ready-to-use, scalable architecture — a shared Layout + Header (logo + centered nav) + Footer, a zero-dependency light/dark theme toggle, native Astro View Transitions, a `@/`→`src/` path alias, a SITE + ROUTES single-source-of-truth config, icons (`@lucide/astro` + custom brand SVGs), Content Collections wired up, a 404 page, and an open backend door (`lib/` + `pages/api/`). Use when starting, creating, or bootstrapping a new Astro site/project/"proyecto astro" from scratch, or when the user wants a base/starter ready to grow from a portfolio to a full app. Generates the project via `bun create astro@latest` (minimal/empty template), writes the full structure, installs deps (incl. @lucide/astro), and verifies the production build.
license: Complete terms in LICENSE.txt
metadata:
  author: bastndev
  version: "2.0.0"
---

# start-astro

Scaffolds a publishable, **scalable Astro base**: the clean `minimal` template, then a hand-written architecture on top — Layout + Header + Footer + 4 pages (incl. 404) + light/dark toggle + View Transitions + `@/` alias + SITE/ROUTES config + icons + Content Collections + a backend door. The stuff you set up every single time you start an Astro project, done once, correctly. It starts as light as a portfolio, but every folder a growing app needs is already there — so you never restructure, you only fill in.

## When to use

The user wants to start a new Astro project: "create/scaffold/bootstrap a new astro project", "set up an astro site", "necesito un proyecto de astro listo", or they have an empty folder and want a base with theme switching, navigation, icons, and a scalable structure already working.

---

## Why `minimal`, not `basic`

`bun create astro@latest` offers four templates. This skill always picks **"Use minimal (empty) template"**, not "A basic, helpful starter project (recommended)".

**Why:** the "basic" template ships its own boilerplate page, default styles, and an Astro logo/welcome component that would all need to be located and deleted before this architecture can go in cleanly. That's an extra, error-prone step that also drifts depending on whatever Astro bundled in that release. `minimal` gives an empty `src/pages/index.astro` and nothing else — everything this skill adds is therefore exactly what's in `references/`, no leftover files, no guessing what to delete.

---

## Architecture at a glance

```
src/
├── assets/icons/{social,theme}/   custom + brand SVGs (imported as components)
├── components/{ui/,Header,GXB}    reusable UI
├── sections/Footer.astro          page-level blocks
├── layouts/Layout.astro           HTML shell (ClientRouter + no-flash theme + Header + Footer)
├── content/                       Content Collection entries (empty, ready)
├── pages/{index,work/index,contact/index,404,api/hello}
├── lib/utils.ts · types/index.ts
├── styles/global.css              design tokens (light + dark) + footer + toggle CSS
├── consts.ts                      SITE + ROUTES (single source of truth)
└── content.config.ts · env.d.ts
ARCHITECTURE.md · README.md · .prettierignore · tsconfig.json (@/ alias)
```

The whole base is built on **one principle: a single source of truth.** The project name lives once in `SITE.name` (`src/consts.ts`); the tab title, header brand, and footer all derive from it. The top-level routes live once in `ROUTES`; the header nav and the 404 page both read it. So the project name and routes are written in exactly one file each — everything else is name-free.

---

## Procedure

1. **Gather inputs:**

   - `PROJECT_NAME` — **the user already created and named their folder before invoking this skill.** Detect it automatically from the current working directory (`pwd` / the basename of the folder Claude is operating in) and use it as-is — **never ask the user to name the project, and never request a name in chat.** The folder's existing name (e.g. `TEST1`) is the project name, exactly as the user typed it (preserve its original casing — don't lowercase/slugify it).
   - `DIR` — always `.` (the current directory). This skill scaffolds **into** the folder the user is already standing in; it does not create a new sibling folder and does not rename anything.
   - `PAGES` — default `Home, Work, Contact` (the standard set this skill ships). Only deviate if the user explicitly asks for different sections.

2. **Scaffold via the official CLI, into the current folder** — the user already made and is standing inside their project folder (e.g. `TEST1`), so this always targets `.`, never a new named folder:
   ```bash
   bun create astro@latest . -- --template minimal --no-install --no-git --skip-houston
   ```
   - `.` → scaffold into the current directory; this skill never creates a new folder or renames the existing one.
   - **Never create a separate, temporary, or differently-named project folder** (e.g. `test-project1`, `astro-scaffold`, a `/tmp` copy, a sibling dir) to scaffold or "test" in and then move/delete. There is exactly **one** project and it is the current folder. Run every command — scaffold, install, build — directly here.
   - `--template minimal` → the empty template (see rationale above).
   - `--no-install` → this skill controls the install step explicitly (next steps), keeps output readable.
   - `--no-git` → don't assume the user wants a fresh git repo; skip unless asked.
   - `--skip-houston` → skip the mascot/animation prompt, keep it non-interactive.
   - If any flag is rejected by the installed `create-astro` version, fall back to running it without flags and answer the interactive prompts yourself: `dir` → `.`, `template` → minimal/empty, decline git init, decline install.
   - If `create-astro` warns that the directory isn't empty (it may contain `.git`, an editor config, etc. — fine), proceed; only stop and ask if it refuses outright because of conflicting files.

3. **Read ALL reference files before writing anything** — they contain the exact, byte-for-byte content to write (these are copy-paste ready, not something to regenerate from scratch):
   - `references/architecture.md` — the doc to copy to the project root as `ARCHITECTURE.md` (substituting `{{PROJECT_NAME}}`).
   - `references/project-structure.md` — final file tree, `GXB.astro` (the ASCII hero — **byte-for-byte**), the 3 pages, `404.astro`, `README.md`, `.prettierignore`, `public/fonts/README.md`, and the 3 `.gitkeep` placeholders.
   - `references/layout-header.md` — `Layout.astro`, `Header.astro`, `Footer.astro` (the shell trio) + the no-flash and toggle scripts, with the View-Transitions gotchas.
   - `references/global-css.md` — the full `src/styles/global.css` (design tokens + base layout + footer + theme-toggle icon CSS) and **why the footer/toggle CSS must live here, not scoped**.
   - `references/config-data-backend.md` — `tsconfig.json` (the `@/` alias), `consts.ts`, `types/index.ts`, `lib/utils.ts`, `env.d.ts`, `content.config.ts`, `pages/api/hello.ts`.
   - `references/icons.md` — installing `@lucide/astro` and the custom SVG set (`assets/icons/social/` + `assets/icons/theme/`), every file byte-for-byte.

4. **Write the files** into the current folder exactly as given in the references.

   **Overwrite** these files that `bun create astro` generated:
   - `tsconfig.json` (the `@/`→`src/*` alias version — no React JSX, no `baseUrl`)
   - `src/pages/index.astro`
   - `README.md`

   **Create** everything else:
   - `src/layouts/Layout.astro`, `src/components/Header.astro`, `src/sections/Footer.astro`
   - `src/components/GXB.astro` (**byte-for-byte from the reference — do not edit the ASCII art**)
   - `src/styles/global.css`
   - `src/pages/work/index.astro`, `src/pages/contact/index.astro`, `src/pages/404.astro`, `src/pages/api/hello.ts` (Work and Contact each live in their own folder as `index.astro` — `pages/work/index.astro` → `/work` — so a route can grow sub-pages later without a move; Home and 404 stay flat at the `pages/` root)
   - `src/consts.ts`, `src/types/index.ts`, `src/lib/utils.ts`, `src/env.d.ts`, `src/content.config.ts`
   - `src/assets/icons/social/*.svg` (11 files) and `src/assets/icons/theme/{sun,moon}.svg`
   - `ARCHITECTURE.md` (project root, **uppercase**)
   - `public/fonts/README.md`
   - `.gitkeep` in `src/assets/images/`, `src/components/ui/`, `src/content/` (so the empty-but-intentional folders survive version control)

   **Substitute `{{PROJECT_NAME}}` in exactly three files** — everywhere else is name-free (the name flows from `SITE.name`):
   - `src/consts.ts` → `SITE.name`
   - `README.md` → the `# {{PROJECT_NAME}}` title
   - `ARCHITECTURE.md` → the `# Architecture — {{PROJECT_NAME}}` title and the `{{PROJECT_NAME}}/` tree root

   **Leave `public/` favicons alone.** Do **not** create, replace, or delete `public/favicon.svg` or `public/favicon.ico` — `bun create astro` ships them (the Astro defaults). The header logo only *references* `favicon.svg` read-only (via a CSS mask); never overwrite the favicon and never delete the `.ico`. You only *add* `public/fonts/README.md`.

   **Leave `astro.config.mjs` as generated** (`export default defineConfig({})`) — the base ships static-first with no adapter.

5. **Install + verify** (already in the project folder, no `cd` needed):
   ```bash
   bun install
   bun add @lucide/astro
   bun run build      # must exit 0 — catches broken imports/typos before the user opens the editor
   ```
   `@lucide/astro` is the **only** runtime dependency this skill adds (the theme toggle and custom icons need zero packages). The peer-dependency warning Lucide prints about the Astro version is harmless. Do not report success until `bun run build` passes. If it fails, read the error, fix the file, rebuild — don't hand back a broken project. **Verify in place** — build *this* project; never spin up a separate throwaway project to test against.

6. **Do not run `bun run dev`** in the background unless the user asks to preview it — this skill's job is to hand back a ready project, not to occupy a long-running terminal.

7. **Report what was scaffolded** once the build passes — print this summary (substitute the real project name), ending with the success line and the run hint:

   ```
   Project {{PROJECT_NAME}} is ready. Here's what was scaffolded:

   src/
   ├── assets/icons/
   │   ├── social/            ← 11 brand SVGs (twitter, github, discord, …)
   │   └── theme/             ← sun.svg + moon.svg (the toggle icons)
   ├── components/
   │   ├── ui/                ← primitives folder (empty, ready)
   │   ├── Header.astro       ← logo + centered nav (from ROUTES) + theme toggle
   │   └── GXB.astro          ← centered ASCII hero + per-page tagline
   ├── sections/Footer.astro  ← {SITE.name} © year
   ├── layouts/Layout.astro   ← shell: ClientRouter + no-flash theme + Header + Footer
   ├── content/               ← Content Collection entries (empty, ready)
   ├── pages/
   │   ├── index.astro · work/index.astro · contact/index.astro
   │   ├── 404.astro          ← themed, links home via ROUTES
   │   └── api/hello.ts       ← example endpoint (the backend door)
   ├── lib/utils.ts · types/index.ts
   ├── styles/global.css      ← design tokens (light + dark) + footer + toggle CSS
   ├── consts.ts              ← SITE + ROUTES (single source of truth)
   └── content.config.ts · env.d.ts
   ARCHITECTURE.md · README.md · .prettierignore · tsconfig.json (@/ alias)

   What's included:
   - Astro 7 with minimal template (no boilerplate), static-first
   - Light/dark theme toggle (CSS vars + vanilla JS, zero deps) + no-flash + View Transitions
   - @/ → src/ path alias (clean imports, no ../../ chains)
   - SITE + ROUTES single source of truth — rename / add routes in one place
   - Icons: @lucide/astro (line icons) + custom brand SVGs that inherit currentColor
   - Content Collections ready; backend door (lib/ + pages/api/)
   - bun run build passed cleanly

   Project created successfully 🎉
   bun run dev
   ```

---

## Gotchas checklist (verify before declaring done)

- [ ] Project name detected from the current folder's name — never asked the user, never invented a separate name
- [ ] `{{PROJECT_NAME}}` substituted in **only** `consts.ts`, `README.md`, `ARCHITECTURE.md` — pages/Layout/Header/Footer are name-free (the name flows from `SITE.name`); the footer is `{SITE.name} © year`, never a hardcoded mark
- [ ] Used `minimal` template, not `basic` — no boilerplate to clean up
- [ ] `tsconfig.json` overwritten with the `@/`→`src/*` alias (extends `astro/tsconfigs/strict`; **no** `baseUrl`, **no** React `jsx`/`jsxImportSource`)
- [ ] **Footer CSS and theme-toggle icon CSS live in `global.css`, NOT in a scoped `<style>`.** They depend on `[data-theme]` on `<html>`, an ancestor a component's scoped styles can't target — scope them and the toggle icon freezes (stuck on the moon) and the footer flashes left-aligned on load
- [ ] Theme-toggle icons are imported SVG components (`@/assets/icons/theme/{sun,moon}.svg`) rendered as `<Sun id="icon-sun" aria-hidden="true" />` / `<Moon id="icon-moon" aria-hidden="true" />`
- [ ] Theme toggle script runs on `astro:page-load` (not only initial load) and the no-flash `<head>` script re-applies on `astro:after-swap` — both required so theme + toggle survive View Transitions
- [ ] `<ClientRouter />` imported from `astro:transitions` and placed in `Layout.astro`'s `<head>`
- [ ] `GXB.astro` written **byte-for-byte** from the reference — the ASCII art is not edited, renamed, or moved (404.astro reuses it)
- [ ] `@lucide/astro` installed (`bun add`); it's the only runtime dep added
- [ ] Custom SVGs are valid files (kebab-case, `currentColor`) in `assets/icons/social/` + `assets/icons/theme/`
- [ ] `public/favicon.svg` and `public/favicon.ico` are the **untouched Astro defaults**; only `public/fonts/README.md` is added to `public/`
- [ ] `.gitkeep` written to `src/assets/images/`, `src/components/ui/`, `src/content/`
- [ ] `ARCHITECTURE.md` (uppercase), `README.md`, `.prettierignore` at the project root
- [ ] `bun install` + `bun run build` both pass before reporting done
