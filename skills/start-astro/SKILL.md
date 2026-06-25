---
name: start-astro
description: Scaffold a new Astro project (minimal template) with a ready-to-use Basic architecture — header navigation (Home/Work/About/Contact), light/dark theme toggle (zero deps, CSS vars + vanilla JS), and native Astro View Transitions for smooth page-to-page fades. Use when starting, creating, or bootstrapping a new Astro site/project/"proyecto astro" from scratch, or when the user wants a base/starter with theme switching and a header already wired up. Generates the project via `bun create astro@latest` with the minimal/empty template, then writes the layout, header, theme CSS/script, and all four pages, installs, and verifies the dev build.
license: Complete terms in LICENSE.txt
metadata:
  author: bastndev
  version: "1.0.0"
---

# start-astro

Scaffolds a publishable **Astro Basic** starter: clean `minimal` template as the base, then a hand-written **Layout + Header + 4 pages + light/dark toggle + View Transitions** on top — the stuff you configure every single time you start an Astro project, done once, correctly.

## When to use

The user wants to start a new Astro project: "create/scaffold/bootstrap a new astro project", "set up an astro site", "necesito un proyecto de astro listo", or they have an empty folder and want the base files with theme switching and navigation already working.

---

## Why `minimal`, not `basic`

`bun create astro@latest` offers four templates. This skill always picks **"Use minimal (empty) template"**, not "A basic, helpful starter project (recommended)".

**Why:** the "basic" template ships its own boilerplate page, default styles, and an Astro logo/welcome component that would all need to be located and deleted before our Header/Layout/theme code can go in cleanly. That's an extra, error-prone step that also drifts depending on whatever Astro bundled in that release. `minimal` gives an empty `src/pages/index.astro` and nothing else — everything this skill adds is therefore exactly what's in `references/`, no leftover files, no guessing what to delete.

---

## Procedure

1. **Gather inputs:**

   - `PROJECT_NAME` / `DIR` — **always let the user choose.** Look for a name already given in the same message that triggered the skill, in any of these forms (English or Spanish, case-insensitive):
     - `name project is: X`, `project name: X`, `project name is X`
     - `nombre del proyecto: X`, `el proyecto se llama X`, `llamalo X`, `nombre: X`
     - A bare folder-looking token the user clearly intends as the name (e.g. "crea **new-proyect-01**", "scaffold **portfolio-site**")

     If a name is found this way, use it directly as both `DIR` (target folder) and `PROJECT_NAME` (used in page titles) — **do not ask**, just confirm briefly in your reply (e.g. "Creando el proyecto **new-proyect-01**...").

     If no name appears anywhere in the request, **ask the user** what they want to call it before scaffolding anything — e.g. "¿Cómo quieres llamar al proyecto? (este nombre se usa como carpeta y en el título de las páginas)". Don't invent a placeholder name and don't default to something like `my-astro-app` silently — the folder name is the one thing this skill never assumes.

   - `PAGES` — default `Home, Work, About, Contact` (the standard set this skill ships). Only deviate if the user explicitly asks for different sections.

2. **Scaffold via the official CLI** — run it non-interactively with flags so it doesn't hang waiting on prompts:
   ```bash
   bun create astro@latest {{DIR}} -- --template minimal --no-install --no-git --skip-houston
   ```
   - `--template minimal` → the empty template (see rationale above).
   - `--no-install` → this skill controls the install step explicitly (next step), keeps output readable.
   - `--no-git` → don't assume the user wants a fresh git repo; skip unless asked.
   - `--skip-houston` → skip the mascot/animation prompt, keep it non-interactive.
   - If any flag is rejected by the installed `create-astro` version, fall back to running it without flags and answer the interactive prompts yourself with the values above (`dir` → `{{DIR}}`, `template` → minimal/empty, decline TypeScript strictness prompts with the default, decline git init, decline install).

3. **Read the reference files** before writing any code — they contain the exact, ready-to-paste implementation:
   - `references/theme-toggle.md` — the 15 CSS variables (light + dark), the toggle button, and the vanilla JS (handles `astro:page-load` so it survives View Transitions per the gotcha below).
   - `references/layout-header.md` — `Layout.astro` (imports `ClientRouter`, the theme script, global CSS) + `Header.astro` (nav with Home/Work/About/Contact + the toggle button).
   - `references/project-structure.md` — final file tree and what minimal content goes in each of the 4 pages.

4. **Write the files** into `{{DIR}}` exactly as given in the references — these are copy-paste ready, not something to regenerate from scratch:
   - `src/layouts/Layout.astro`
   - `src/components/Header.astro`
   - `src/styles/theme.css`
   - `src/pages/index.astro` (Home)
   - `src/pages/work.astro`
   - `src/pages/about.astro`
   - `src/pages/contact.astro`

5. **Install + verify:**
   ```bash
   cd {{DIR}}
   bun install
   bun run build      # must exit 0 — catches broken imports/typos before the user ever opens the editor
   ```
   Do not report success until `bun run build` passes. If it fails, read the error, fix the file, rebuild — don't hand back a broken project.

6. **Do not run `bun run dev`** in the background unless the user asks to preview it — this skill's job is to hand back a ready project, not to occupy a long-running terminal.

---

## Gotchas checklist (verify before declaring done)

- [ ] Project name came from the user's message or was explicitly asked — never silently defaulted/invented
- [ ] Used `minimal` template, not `basic` — no boilerplate to clean up
- [ ] Theme toggle script runs on `astro:page-load`, not only on initial `DOMContentLoaded` — otherwise it breaks after the first View Transition (bundled module scripts only execute once; see `references/theme-toggle.md`)
- [ ] Inline "no-flash" script in `<head>` reads the saved theme **before** first paint, so there's no light-flash on dark-mode reload
- [ ] `<ClientRouter />` imported from `astro:transitions` and placed in `Layout.astro`'s `<head>`
- [ ] All 4 pages (Home/Work/About/Contact) use the same `Layout.astro` + `Header.astro`
- [ ] `bun install` and `bun run build` both pass before reporting done
- [ ] Zero runtime dependencies added for the theme toggle (CSS vars + vanilla JS only — no package installed for this)
