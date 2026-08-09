<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/github/icons/start-logo/start-astro.webp" width="150" />
</p>

<h1 align="center">[Start] / Astro Starter</h1>

<p align="center">
  <strong>Start Astro</strong> — A focused Astro scaffold that grows only when the site needs it
</p>

<p align="center">
  <a href="../../README.md">← Back to Start / Middle / [End]</a>
</p>

---

Scaffolds a new Astro 7 project from the `minimal` template and overlays a small, production-ready architecture. It includes the shared shell, accessible theme behavior, core pages, local icons, and documentation a real starter uses—without pre-creating APIs, content systems, helpers, types, or empty folders for hypothetical future work.

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

1. **Detects** — Uses the current folder name as the project name and works in place.
2. **Scaffolds** — Runs Astro's empty `minimal` template without initializing Git or installing twice.
3. **Overlays** — Copies the known-good template bundled with the skill, including the local `gxb.otf` font.
4. **Customizes** — Writes the project name only to `SITE.name` and the README title.
5. **Verifies** — Installs `@lucide/astro` and requires `bun run build` to pass before handoff.

## Guarantees

- **Focused by default**: Includes only files the working starter uses.
- **Clear ownership**: Global CSS contains document-wide foundations; component styles stay scoped beside their markup.
- **Single source of truth**: Site identity and primary routes live in `src/consts.ts`.
- **Accessible interaction**: Keyboard focus, synchronized theme ARIA state, reduced-motion handling, and semantic 404 markup are built in.
- **Reliable navigation**: The theme survives View Transitions without duplicate listeners, and active routes tolerate trailing slashes.
- **In-place setup**: Never creates a throwaway or differently named project folder.
- **Preserved scaffold files**: Leaves generated package metadata, Astro config, agent guidance, editor settings, and favicons alone.

## What You Get

```text
public/
└── fonts/gxb.otf
src/
├── assets/icons/social/       # 7 local outline brand icons
├── components/
│   ├── ui/buttons/            # BackButton404 + ThemeToggle
│   ├── GXB.astro              # ASCII hero + tagline + social links
│   └── Header.astro           # brand + active nav + theme control
├── layouts/Layout.astro       # metadata + ClientRouter + theme bootstrap
├── pages/
│   ├── index.astro
│   ├── work/index.astro
│   ├── contact/index.astro
│   └── 404.astro
├── sections/Footer.astro
├── styles/global.css
├── consts.ts                  # SITE + ROUTES
└── env.d.ts

ARCHITECTURE.md · README.md · .prettierignore · tsconfig.json
```

The base intentionally omits Content Collections, API routes, adapters, services, stores, shared library/type folders, and empty placeholders. `ARCHITECTURE.md` explains when each capability has earned a place in the project.

---

→ Full spec & rules: [SKILL.md](./SKILL.md)

<div align="center">
  <sub>Built for developers who want a strong Astro foundation without speculative architecture.</sub>
  <br><br>
  <sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="https://github.com/bastndev/skills/blob/main/LICENSE">MIT</a></sub>
</div>
