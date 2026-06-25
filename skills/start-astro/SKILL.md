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

   - `PROJECT_NAME` — **the user already created and named their folder before invoking this skill.** Detect it automatically from the current working directory (`pwd` / the basename of the folder Claude is operating in) and use it as-is — **never ask the user to name the project, and never request a name in chat.** The folder's existing name (e.g. `TEST1`) is the project name, exactly as the user typed it (preserve its original casing — don't lowercase/slugify it).
   - `DIR` — always `.` (the current directory). This skill scaffolds **into** the folder the user is already standing in; it does not create a new sibling folder and does not rename anything.
   - `PAGES` — default `Home, Work, About, Contact` (the standard set this skill ships). Only deviate if the user explicitly asks for different sections.

2. **Scaffold via the official CLI, into the current folder** — the user already made and is standing inside their project folder (e.g. `TEST1`), so this always targets `.`, never a new named folder:
   ```bash
   bun create astro@latest . -- --template minimal --no-install --no-git --skip-houston
   ```
   - `.` → scaffold into the current directory; this skill never creates a new folder or renames the existing one.
   - `--template minimal` → the empty template (see rationale above).
   - `--no-install` → this skill controls the install step explicitly (next step), keeps output readable.
   - `--no-git` → don't assume the user wants a fresh git repo; skip unless asked.
   - `--skip-houston` → skip the mascot/animation prompt, keep it non-interactive.
   - If any flag is rejected by the installed `create-astro` version, fall back to running it without flags and answer the interactive prompts yourself: `dir` → `.` (current folder), `template` → minimal/empty, decline TypeScript strictness prompts with the default, decline git init, decline install.
   - If `create-astro` warns that the directory isn't empty (it may contain `.git`, an editor config, etc. — fine), proceed; only stop and ask if it refuses outright because of conflicting files.

3. **Read the reference files** before writing any code — they contain the exact, ready-to-paste implementation:
   - `references/theme-toggle.md` — the 15 CSS variables (light + dark), the toggle button, and the vanilla JS (rebinds the toggle on `astro:page-load` **and** re-applies the theme on `astro:after-swap`, so both survive View Transitions per the gotchas below).
   - `references/layout-header.md` — `Layout.astro` (imports `ClientRouter`, the theme script, global CSS) + `Header.astro` (nav with Home/Work/About/Contact + the toggle button).
   - `references/project-structure.md` — final file tree and what minimal content goes in each of the 4 pages.

4. **Write the files** into the current folder exactly as given in the references — these are copy-paste ready, not something to regenerate from scratch:
   - `src/layouts/Layout.astro`
   - `src/components/Header.astro`
   - `src/styles/global.css`
   - `src/pages/index.astro` (Home)
   - `src/pages/work.astro`
   - `src/pages/about.astro`
   - `src/pages/contact.astro`

5. **Install + verify** (already in the project folder, no `cd` needed):
   ```bash
   bun install
   bun run build      # must exit 0 — catches broken imports/typos before the user ever opens the editor
   ```
   Do not report success until `bun run build` passes. If it fails, read the error, fix the file, rebuild — don't hand back a broken project.

6. **Do not run `bun run dev`** in the background unless the user asks to preview it — this skill's job is to hand back a ready project, not to occupy a long-running terminal.

---

## Gotchas checklist (verify before declaring done)

- [ ] Project name was detected from the current folder's name — never asked the user, never invented a separate name
- [ ] Used `minimal` template, not `basic` — no boilerplate to clean up
- [ ] Theme toggle script runs on `astro:page-load`, not only on initial `DOMContentLoaded` — otherwise it breaks after the first View Transition (bundled module scripts only execute once; see `references/theme-toggle.md`)
- [ ] Inline "no-flash" script in `<head>` reads the saved theme **before** first paint (no light-flash on dark-mode reload) **and re-applies it on `astro:after-swap`** — without the after-swap re-apply, navigating between pages strips `<html data-theme>` (the incoming server HTML has none) and the site flips dark→light on every nav click
- [ ] `<ClientRouter />` imported from `astro:transitions` and placed in `Layout.astro`'s `<head>`
- [ ] All 4 pages (Home/Work/About/Contact) use the same `Layout.astro` + `Header.astro`
- [ ] Home page (`index.astro`) is the centered ASCII-logo hero (`<pre aria-hidden>` + welcome line), not a plain `<h1>Home</h1>`
- [ ] `bun install` and `bun run build` both pass before reporting done
- [ ] Zero runtime dependencies added for the theme toggle (CSS vars + vanilla JS only — no package installed for this)
