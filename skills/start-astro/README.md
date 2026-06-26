<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/github/icons/start-logo/start-astro.webp" width="150" />
</p>

<h1 align="center">[Start] / Astro Starter</h1>

<p align="center">
  <strong>Start Astro</strong> — The scalable Astro scaffolding skill
</p>

<p align="center">
  <a href="../../README.md">← Back to Start / Middle / [End]</a>
</p>

---

Scaffolds a new Astro project using the `minimal` template, overlaid with a clean, **scalable** architecture — ready to grow from a portfolio to a full app. The stuff you set up every single time you start an Astro project, done once, correctly.

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

## Install

```bash
npx skills add bastndev/skills --skill start-astro
```

## How It Works

1. **Detects** — Uses the current folder name as the project name. Never asks you to name it, never creates a separate sibling folder.
2. **Scaffolds** — Runs `bun create astro` with the `minimal` (empty) template to ensure zero boilerplate needs to be deleted.
3. **Builds** — Writes a scalable architecture (Layout, Header, Footer, pages, theme toggle, configs, aliases) into the project.
4. **Installs & Verifies** — Installs `@lucide/astro` and runs the production build to verify it works flawlessly before handing it over. Uses **`bun`** if available, otherwise falls back to **`npm`**.

## Guarantees

- **Single Source of Truth**: Project name and routes live exactly once in `consts.ts`.
- **Zero Boilerplate**: Uses the empty `minimal` template, never the `basic` one.
- **In-place Setup**: Operates in the current directory; never creates a throwaway or differently-named project folder.
- **Untouched Favicons**: Preserves the default Astro favicons (`public/favicon.svg`, `public/favicon.ico`).

## What You Get

```
src/
    ├── assets/               # Imported in code → optimized & hashed by Astro/Vite
    │   ├── images/
    │   └── icons/            #   custom inline SVGs (e.g. social/) imported as components
    │
    ├── components/           # Reusable pieces shared across pages
    │   ├── ui/               #   small primitives — ui/buttons/BackButton404.astro
    │   ├── Header.astro      #   logo + centered nav (from ROUTES) + theme toggle
    │   └── GXB.astro         #   ASCII hero + social-links row (one source for the art)
    │
    ├── sections/             # Page-level blocks (Hero, Footer, FeatureGrid…)
    │   └── Footer.astro      #   minimal footer (brand + year)
    │
    ├── layouts/
    │   └── Layout.astro      #   HTML shell: <head>, ClientRouter, no-flash theme
    │                         #   script, <Header />, <slot />, <Footer />
    │
    ├── content/              # Content Collection entries — one PLURAL folder
    │                         #   per collection (blog/, projects/…)
    │
    ├── pages/                # File-based routing
    │   ├── index.astro       #   Home
    │   ├── work/
    │   │   └── index.astro   #   Work → /work (folder per route, room to grow)
    │   ├── contact/
    │   │   └── index.astro   #   Contact → /contact
    │   ├── 404.astro         #   typing-animation 404, hides nav/footer, links home
    │   └── api/
    │       └── hello.ts      #   example endpoint → GET /api/hello
    │
    ├── lib/                  # Framework-agnostic helpers (no UI)
    │   └── utils.ts
    ├── types/               # Shared TypeScript types
    │   └── index.ts
    │
    ├── styles/
    │   └── global.css        #   design tokens (CSS vars: light + dark) + base
    │
    ├── content.config.ts     # Content Collections schema (Astro 7 location)
    ├── consts.ts             # SITE config + ROUTES registry — single source
    └── env.d.ts              # Typed import.meta.env

ARCHITECTURE.md · README.md · tsconfig.json (@/ alias)
```

A fully working site with a zero-dependency light/dark toggle, native View Transitions, a hero social-links row, an animated full-screen 404 (resilient with JS off), a gradient footer, SEO/Open Graph meta, accessibility defaults (skip link, focus rings, `prefers-reduced-motion`), `@/` path aliases, Content Collections ready, and an open backend door (`lib/` + `pages/api/`). Works with `bun` or `npm`.

---

→ Full spec & rules: [SKILL.md](./SKILL.md)

<div align="center">
  <sub>Built for developers who want to start their Astro projects with a robust foundation.</sub>
  <br><br>
  <sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="https://github.com/bastndev/skills/blob/main/LICENSE">MIT</a></sub>
</div>
