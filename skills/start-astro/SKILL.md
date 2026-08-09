---
name: start-astro
description: Scaffold a focused, production-ready Astro 7 project from the minimal template. Use when starting, creating, or bootstrapping a new Astro site or "proyecto astro" in the current directory. Installs a pure-Astro layout with Header, Footer, Home/Work/Contact pages, an accessible animated 404, no-flash light/dark themes, View Transitions, a `@/` path alias, SITE and ROUTES configuration, Lucide UI icons, seven local brand icons, and the bundled gxb font, then verifies the production build. Keeps optional content collections, API routes, adapters, services, stores, shared libraries, and speculative folders out until the project actually needs them.
license: Complete terms in LICENSE.txt
metadata:
  author: bastndev
  version: "2.1.0"
---

# Astro project scaffold

Create a small Astro base from the files in `assets/template/`. Favor clear ownership and add capabilities only when the site needs them.

## Inputs and boundaries

- Derive `PROJECT_NAME` from the basename of the current working directory. Preserve its original spelling and casing. Never ask for a name.
- Use the current directory as the project root. Never create a sibling, child, temporary, or throwaway project.
- Ship the standard Home, Work, and Contact routes unless the user explicitly requests different pages.
- Treat `assets/template/` as the source of truth. Do not recreate its files from memory or redesign the base while scaffolding.
- Preserve unrelated files and skill-installation metadata already present in the directory. Stop before overwriting user-authored project files that are not from a fresh Astro scaffold.

## Procedure

1. Inspect the current directory and derive `PROJECT_NAME`.
2. Scaffold Astro's empty template directly into the current directory:

   ```bash
   bun create astro@latest . -- --template minimal --no-install --no-git --skip-houston
   ```

   If the installed CLI rejects a flag, run it interactively and select the current directory, the minimal/empty template, no dependency installation, and no Git initialization. Existing installer metadata or editor files are not conflicts; stop only when the CLI refuses because a real project file would be overwritten.

3. Resolve the directory containing this `SKILL.md` as `SKILL_DIR`. Copy every file from `SKILL_DIR/assets/template/`, including `.prettierignore`, into the project root. Overwrite the minimal scaffold's `README.md`, `tsconfig.json`, and `src/pages/index.astro` with the bundled versions.
4. Replace `{{PROJECT_NAME}}` in exactly these two files:

   - `README.md` — visible project title.
   - `src/consts.ts` — `SITE.name`, safely escaped as a TypeScript string while preserving the displayed name.

   Confirm the placeholder is gone:

   ```bash
   rg -n '\{\{PROJECT_NAME\}\}' README.md src/consts.ts
   ```

5. Leave these scaffold-generated files as generated: `.gitignore`, `.vscode/`, `AGENTS.md`, `CLAUDE.md`, `astro.config.mjs`, `package.json`, `public/favicon.svg`, and `public/favicon.ico`. Do not hand-edit package metadata. The template adds only `public/fonts/gxb.otf` under `public/`.
6. Install and verify in place:

   ```bash
   bun install
   bun add @lucide/astro
   bun run build
   ```

   `@lucide/astro` is the only dependency added beyond Astro. Do not report success until the build exits with status 0. Read any error, fix the generated project, and rerun the build.
7. When the project root is a Git repository, run `git diff --check`. Do not start `bun run dev` unless the user asks for a preview.

## Template inventory

```text
assets/template/
├── public/fonts/gxb.otf
├── src/
│   ├── assets/icons/social/       # x, github, linkedin, instagram, youtube, tiktok, facebook
│   ├── components/
│   │   ├── ui/buttons/            # BackButton404 + ThemeToggle
│   │   ├── GXB.astro              # ASCII hero, tagline, and social links
│   │   └── Header.astro           # brand, active navigation, and theme control
│   ├── layouts/Layout.astro       # metadata, ClientRouter, theme bootstrap, page shell
│   ├── pages/                     # Home, Work, Contact, and 404
│   ├── sections/Footer.astro
│   ├── styles/global.css
│   ├── consts.ts
│   └── env.d.ts
├── .prettierignore
├── ARCHITECTURE.md
├── README.md
└── tsconfig.json
```

Copy the binary font from the asset; never attempt to reconstruct or transcribe it.

## Architecture guarantees

- Keep global CSS limited to the font face, semantic theme tokens, box sizing, scrollbar colors, and document typography/background. Keep component selectors beside their Astro markup.
- Keep the project name in `SITE.name`; Layout, Header, and Footer derive it from there.
- Keep top-level navigation in `ROUTES`. Header renders it and computes active links; the 404 page finds `/` and fails clearly if the home route is missing.
- Apply the saved theme before first paint, fall back to the operating-system preference, tolerate unavailable storage, and restore it during View Transitions without duplicate listeners.
- Keep the toggle accessible with synchronized `aria-label` and `aria-pressed`, multiple-instance safety, and visible keyboard focus.
- Respect `prefers-reduced-motion` in the 404 typing effect. Use semantic heading markup and hide the decorative cursor from assistive technology.
- Preserve the seven local outline brand SVGs and their tuned view boxes. Keep social profile URLs centralized in `GXB.astro`.
- Preserve `public/favicon.svg` and `public/favicon.ico`; Header uses the SVG as a theme-aware CSS mask.
- Keep Astro static-first. Do not add an adapter or server output.

## Deliberately absent

Do not create empty or example-only systems for future use:

- `src/content.config.ts` or `src/content/`
- `src/pages/api/`
- `src/lib/`, `src/types/`, `src/services/`, or `src/stores/`
- empty image folders or `.gitkeep` placeholders
- sample API endpoints, placeholder font documentation, React, Tailwind, or another UI framework

`ARCHITECTURE.md` explains when to introduce content collections, API/server rendering, shared logic, or shared types.

## Completion report

After `bun run build` passes, report the detected project name, the focused structure created, `@lucide/astro` and the bundled font, theme/View Transition behavior, the intentionally omitted speculative systems, and the successful build. End with:

```text
Project created successfully 🎉
bun run dev
```

## Final checks

- [ ] Scaffolded the minimal template in the current directory only.
- [ ] Copied the complete bundled template, including `.prettierignore` and `public/fonts/gxb.otf`.
- [ ] Replaced `{{PROJECT_NAME}}` only in `README.md` and `src/consts.ts`.
- [ ] Preserved generated package metadata, config, instructions, editor files, and favicons.
- [ ] Kept component styles scoped and global CSS focused.
- [ ] Did not reintroduce speculative folders, APIs, collections, helpers, or placeholder files.
- [ ] Installed only `@lucide/astro` beyond Astro.
- [ ] `bun run build` passed in the real project.
