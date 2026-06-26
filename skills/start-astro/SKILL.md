---
name: start-astro
description: Scaffold a new Astro project (minimal template) with a ready-to-use, scalable architecture — a shared Layout + Header (logo + centered nav) + Footer, a zero-dependency light/dark theme toggle, native Astro View Transitions, a `@/`→`src/` path alias, a SITE + ROUTES single-source-of-truth config, icons (`@lucide/astro` + a unified 7-icon custom brand set) shown in a hero social-links row, Content Collections wired up, an animated full-screen 404 page (typing effect), SEO/Open Graph meta, accessibility defaults (skip-link, focus rings, reduced-motion), and an open backend door (`lib/` + `pages/api/`). Use when starting, creating, or bootstrapping a new Astro site/project/"proyecto astro" from scratch, or when the user wants a base/starter ready to grow from a portfolio to a full app. Generates the project via `bun create astro@latest` (or `npm create astro@latest`; minimal/empty template), writes the full structure, installs deps (incl. @lucide/astro), and verifies the production build.
license: Complete terms in LICENSE.txt
metadata:
  author: bastndev
  version: "2.2.0"
---

# start-astro

Scaffolds a publishable, **scalable Astro base**: the clean `minimal` template, then a hand-written architecture on top — Layout + Header + Footer + 4 pages (incl. 404) + light/dark toggle + View Transitions + `@/` alias + SITE/ROUTES config + icons + Content Collections + a backend door. The stuff you set up every single time you start an Astro project, done once, correctly. It starts as light as a portfolio, but every folder a growing app needs is already there — so you never restructure, you only fill in.

## When to use

The user wants to start a new Astro project: "create/scaffold/bootstrap a new astro project", "set up an astro site", "necesito un proyecto de astro listo", or they have an empty folder and want a base with theme switching, navigation, icons, and a scalable structure already working.

---

## Why `minimal`, not `basic`

The `create astro` CLI (`bun`/`npm create astro@latest`) offers four templates. This skill always picks **"Use minimal (empty) template"**, not "A basic, helpful starter project (recommended)".

**Why:** the "basic" template ships its own boilerplate page, default styles, and an Astro logo/welcome component that would all need to be located and deleted before this architecture can go in cleanly. That's an extra, error-prone step that also drifts depending on whatever Astro bundled in that release. `minimal` gives an empty `src/pages/index.astro` and nothing else — everything this skill adds is therefore exactly what's in `references/`, no leftover files, no guessing what to delete.

---

## Architecture at a glance

```
src/
├── assets/icons/{social,theme}/   7 brand SVGs + sun/moon (components / ?raw)
├── components/{ui/buttons/,Header,GXB}  reusable UI (GXB = ASCII hero + social row; BackButton404)
├── sections/Footer.astro          page-level blocks (gradient top border)
├── layouts/Layout.astro           HTML shell (ClientRouter + no-flash theme + Header + Footer + hideNavAndFooter)
├── content/                       Content Collection entries (empty, ready)
├── pages/{index,work/index,contact/index,404,api/hello}
├── lib/utils.ts · types/index.ts
├── styles/global.css              design tokens (light + dark) + gradient footer + toggle CSS
├── consts.ts                      SITE + ROUTES (single source of truth)
└── content.config.ts · env.d.ts
ARCHITECTURE.md · README.md · .prettierignore · .npmrc · tsconfig.json (@/ alias)
```

The whole base is built on **one principle: a single source of truth.** The project name lives once in `SITE.name` (`src/consts.ts`); the tab title, header brand, and footer all derive from it. The top-level routes live once in `ROUTES`; the header nav and the 404 page both read it. So the project name and routes are written in exactly one file each — everything else is name-free.

---

## Procedure

1. **Gather inputs:**

   - `PROJECT_NAME` — **the user already created and named their folder before invoking this skill.** Detect it automatically from the current working directory (`pwd` / the basename of the folder Claude is operating in) and use it as-is — **never ask the user to name the project, and never request a name in chat.** The folder's existing name (e.g. `TEST1`) is the project name, exactly as the user typed it (preserve its original casing — don't lowercase/slugify it).
   - `DIR` — always `.` (the current directory). This skill scaffolds **into** the folder the user is already standing in; it does not create a new sibling folder and does not rename anything.
   - `PAGES` — default `Home, Work, Contact` (the standard set this skill ships). Only deviate if the user explicitly asks for different sections.

2. **Pick the package manager, then scaffold via the official CLI into the current folder.** Prefer **`bun`** if it's installed (`command -v bun`); otherwise fall back to **`npm`**. Use the *same* manager for every command in this skill (scaffold, install, add, build). The user already made and is standing inside their project folder (e.g. `TEST1`), so this always targets `.`, never a new named folder:
   ```bash
   # bun (preferred):
   bun create astro@latest . -- --template minimal --no-install --no-git --skip-houston
   # npm (fallback — only if bun is not installed):
   npm create astro@latest . -- --template minimal --no-install --no-git --skip-houston
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
   - `references/project-structure.md` — final file tree, `GXB.astro` (the ASCII hero — **art byte-for-byte** — plus the social-links row), the 3 pages, the animated `404.astro` + `ui/buttons/BackButton404.astro`, `README.md`, `.prettierignore`, `public/fonts/README.md`, and the 3 `.gitkeep` placeholders.
   - `references/layout-header.md` — `Layout.astro` (incl. the `hideNavAndFooter` prop), `Header.astro`, `Footer.astro` (the shell trio) + the no-flash and toggle scripts, with the View-Transitions gotchas.
   - `references/global-css.md` — the full `src/styles/global.css` (design tokens + base layout + the gradient footer + theme-toggle icon CSS) and **why the footer/toggle CSS must live here, not scoped**.
   - `references/config-data-backend.md` — `tsconfig.json` (the `@/` alias), `consts.ts`, `types/index.ts`, `lib/utils.ts`, `env.d.ts`, `content.config.ts`, `pages/api/hello.ts`.
   - `references/icons.md` — installing `@lucide/astro` and the custom SVG set: the **7** social icons (`assets/icons/social/`) + the theme icons (`assets/icons/theme/`), every file byte-for-byte.

4. **Write the files** into the current folder exactly as given in the references.

   **Overwrite** these files that `bun create astro` generated:
   - `tsconfig.json` (the `@/`→`src/*` alias version — no React JSX, no `baseUrl`)
   - `src/pages/index.astro`
   - `README.md`

   **Create** everything else:
   - `src/layouts/Layout.astro` (incl. the `hideNavAndFooter` prop), `src/components/Header.astro`, `src/sections/Footer.astro`
   - `src/components/GXB.astro` (**ASCII art byte-for-byte — do not edit it; the hero also renders a social-links row whose `socials` handles you may edit**)
   - `src/components/ui/buttons/BackButton404.astro` (the themed back button the 404 uses)
   - `src/styles/global.css`
   - `src/pages/work/index.astro`, `src/pages/contact/index.astro`, `src/pages/404.astro` (the typing-animation page — passes `hideNavAndFooter`), `src/pages/api/hello.ts` (Work and Contact each live in their own folder as `index.astro` — `pages/work/index.astro` → `/work` — so a route can grow sub-pages later without a move; Home and 404 stay flat at the `pages/` root)
   - `src/consts.ts`, `src/types/index.ts`, `src/lib/utils.ts`, `src/env.d.ts`, `src/content.config.ts`
   - `src/assets/icons/social/*.svg` (7 files: x, github, linkedin, instagram, youtube, tiktok, facebook) and `src/assets/icons/theme/{sun,moon}.svg`
   - `ARCHITECTURE.md` (project root, **uppercase**)
   - `public/fonts/README.md`
   - `.npmrc` (project root — `legacy-peer-deps=true` so `npm install` works despite Lucide's lagging Astro-7 peer range; inert under bun — see `references/project-structure.md`)
   - `.gitkeep` in `src/assets/images/`, `src/components/ui/`, `src/content/` (so the empty-but-intentional folders survive version control)

   **Substitute `{{PROJECT_NAME}}` in exactly three files** — everywhere else is name-free (the name flows from `SITE.name`):
   - `src/consts.ts` → `SITE.name`
   - `README.md` → the `# {{PROJECT_NAME}}` title
   - `ARCHITECTURE.md` → the `# Architecture — {{PROJECT_NAME}}` title and the `{{PROJECT_NAME}}/` tree root

   The `socials` array in `GXB.astro` is **not** a `{{PROJECT_NAME}}` slot — it ships with default handles; leave them as shipped unless the user gives their own.

   **Leave `public/` favicons alone.** Do **not** create, replace, or delete `public/favicon.svg` or `public/favicon.ico` — `bun create astro` ships them (the Astro defaults). The header logo only *references* `favicon.svg` read-only (via a CSS mask); never overwrite the favicon and never delete the `.ico`. You only *add* `public/fonts/README.md`.

   **Leave `astro.config.mjs` as generated** (`export default defineConfig({})`) — the base ships static-first with no adapter.

5. **Install + verify** (already in the project folder, no `cd` needed) — with the **same package manager** chosen in step 2:
   ```bash
   # bun (preferred):
   bun install
   bun add @lucide/astro
   bun run build      # must exit 0 — catches broken imports/typos before the user opens the editor

   # npm (fallback):
   npm install
   npm install @lucide/astro
   npm run build
   ```
   `@lucide/astro` is the **only** runtime dependency this skill adds (the theme toggle and custom icons need zero packages). Lucide's peer range doesn't list Astro 7 yet: **bun** prints a harmless warning and proceeds; **npm** would hard-error (`ERESOLVE`), which is exactly why the skill writes `.npmrc` (`legacy-peer-deps=true`) in step 4 — with it in place, `npm install @lucide/astro` (and any later `npm install` by someone who clones the project) just works. Do not report success until the production build (`bun run build` / `npm run build`) passes. If it fails, read the error, fix the file, rebuild — don't hand back a broken project. **Verify in place** — build *this* project; never spin up a separate throwaway project to test against.

6. **Do not run `bun run dev`** in the background unless the user asks to preview it — this skill's job is to hand back a ready project, not to occupy a long-running terminal.

7. **Report what was scaffolded** once the build passes — print this summary (substitute the real project name), ending with the success line and the run hint:

   ```
   Project {{PROJECT_NAME}} is ready. Here's what was scaffolded:

   src/
   ├── assets/icons/
   │   ├── social/            ← 7 brand SVGs (x, github, linkedin, instagram, …)
   │   └── theme/             ← sun.svg + moon.svg (the toggle icons)
   ├── components/
   │   ├── ui/buttons/        ← BackButton404.astro (used by the 404)
   │   ├── Header.astro       ← logo + centered nav (from ROUTES) + theme toggle
   │   └── GXB.astro          ← ASCII hero + tagline + social-links row
   ├── sections/Footer.astro  ← {SITE.name} © year (gradient top border)
   ├── layouts/Layout.astro   ← shell: ClientRouter + no-flash theme + SEO/OG meta + Header + Footer + hideNavAndFooter
   ├── content/               ← Content Collection entries (empty, ready)
   ├── pages/
   │   ├── index.astro · work/index.astro · contact/index.astro
   │   ├── 404.astro          ← typing animation, hides nav/footer, links home
   │   └── api/hello.ts       ← example endpoint (the backend door)
   ├── lib/utils.ts · types/index.ts
   ├── styles/global.css      ← design tokens (light + dark) + gradient footer + toggle CSS
   ├── consts.ts              ← SITE + ROUTES (single source of truth)
   └── content.config.ts · env.d.ts
   ARCHITECTURE.md · README.md · .prettierignore · .npmrc · tsconfig.json (@/ alias)

   What's included:
   - Astro 7 with minimal template (no boilerplate), static-first
   - Light/dark theme toggle (CSS vars + vanilla JS, zero deps) + no-flash + View Transitions
   - @/ → src/ path alias (clean imports, no ../../ chains)
   - SITE + ROUTES single source of truth — rename / add routes in one place
   - Hero social-links row (7 brand icons) + animated full-screen 404 (typing effect)
   - Icons: @lucide/astro (line icons) + a unified 7-icon brand set (outline, currentColor)
   - Gradient ("degraded") footer border
   - SEO-ready <head>: canonical + Open Graph/Twitter cards (per-page description/image overrides)
   - Accessible by default: skip link, aria-current, focus rings, prefers-reduced-motion; 404 works with JS off
   - Content Collections ready; backend door (lib/ + pages/api/)
   - Built with bun (or npm) — production build passed cleanly

   Project created successfully 🎉
   bun run dev      # (or: npm run dev)
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
- [ ] `GXB.astro`: the **ASCII art is byte-for-byte** (not edited, renamed, or moved); the hero also renders a **social-links row** — 7 icons imported with `?raw` + injected via `set:html`, handles in the `socials` array
- [ ] `404.astro` is the typing-animation page: imports `BackButton404` (`components/ui/buttons/`), passes `hideNavAndFooter={true}` (Header + Footer hidden), keeps a **name-free** `title="404"`, and links home from `ROUTES[0]`
- [ ] `Layout.astro` exposes `hideNavAndFooter?: boolean`; `<Header />` and `<Footer />` are guarded with `{!hideNavAndFooter && …}`
- [ ] Footer's top border is the **gradient** (`border-image: linear-gradient(...)`, transparent→border→transparent), not a solid rule — and it lives in `global.css`
- [ ] `@lucide/astro` installed (`bun add` / `npm install`); it's the only runtime dep added
- [ ] Social set is exactly **7** outline SVGs — `x, github, linkedin, instagram, youtube, tiktok, facebook` (`twitter`→`x`; no discord/threads/soundcloud) — each `currentColor`, kebab-case, with the tuned `viewBox` from `references/icons.md`
- [ ] `public/favicon.svg` and `public/favicon.ico` are the **untouched Astro defaults**; only `public/fonts/README.md` is added to `public/`
- [ ] `.gitkeep` written to `src/assets/images/`, `src/components/ui/`, `src/content/`
- [ ] `ARCHITECTURE.md` (uppercase), `README.md`, `.prettierignore` at the project root
- [ ] Same package manager used throughout — `bun` if available, else `npm` (`npm install`, `npm install @lucide/astro`, `npm run build`)
- [ ] `.npmrc` (`legacy-peer-deps=true`) written at the project root — it's what lets npm install `@lucide/astro` despite Lucide's lagging Astro-7 peer range (bun only warns); inert under bun
- [ ] `Layout.astro` emits SEO/social tags — canonical `<link>` + Open Graph/Twitter from `SITE` + page props (`description`, optional `image`); `SITE.url` drives the absolute URLs
- [ ] Accessibility defaults present: skip-to-content link (`.skip-link` → `#main-content`), `aria-current="page"` on the active nav link, a global `:focus-visible` ring, and a `prefers-reduced-motion` reset in `global.css`
- [ ] 404 message is **server-rendered** in `.typing-text` (works with JS off); the script re-types it as enhancement and skips the animation under reduced-motion
- [ ] install + production build both pass (with the chosen manager) before reporting done
