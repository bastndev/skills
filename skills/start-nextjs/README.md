<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/github/icons/start-logo/start-next.webp" width="150" />
</p>

<h1 align="center">[Start] / Next.js Starter</h1>

<p align="center">
  <strong>Start Next.js</strong> — A focused Next.js scaffold with Bun, shadcn/ui, and light/dark themes
</p>

<p align="center">
  <a href="../../README.md">← Back to Start / Middle / [End]</a>
</p>

---

Creates a new Next.js App Router project in the current directory, with TypeScript, Tailwind CSS, ESLint, and all application code under `src/`. Adds Lucide icons, a shadcn button, and a working theme toggle while keeping the starting structure small.

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

## Install

```bash
npx skills add bastndev/skills --skill start-nextjs
```

## How It Works

1. **Detects** — Uses the current folder as the project root and its name as the visible project title.
2. **Scaffolds** — Runs `create-next-app` with Bun and `--src-dir`, so no manual move from `app/` is needed.
3. **Configures** — Initializes shadcn/ui and sets its output alias before adding the button under `src/components/ui/shadcn/`.
4. **Adds themes** — Copies the bundled provider, toggle, root layout, and minimal home page. Keeps Geist Sans/Mono and the requested light/dark palette.
5. **Verifies** — Runs lint and a production build; checks theme interaction in a browser when available and reports any unchecked behavior.

## What You Get

```text
src/
├── app/
│   ├── globals.css
│   ├── layout.tsx
│   └── page.tsx
├── components/
│   ├── ui/shadcn/button.tsx
│   ├── theme-provider.tsx
│   └── theme-toggle.tsx
├── lib/utils.ts
└── consts.ts

components.json · bun.lock · README.md
```

Next.js also supplies the framework configuration, public assets, and favicon. These stay in their generated locations. The CLI manages dependencies for the selected shadcn preset and button.

## Theme and Structure

- **System preference first**: Uses `next-themes` with `defaultTheme="system"`; explicit choices persist across reloads.
- **Correct first click**: Toggles using the resolved light/dark appearance, including when the stored preference is `system`.
- **Stable hydration**: Both decorative icons use CSS visibility; the button has a stable accessible name. Only the provider and toggle need client boundaries.
- **Accessible control**: Native button behavior, keyboard focus, Sun/Moon transforms, and reduced-motion support.
- **One palette**: `#fafafa`/black in light mode and `#101010`/white in dark mode, defined through shadcn's semantic tokens.
- **Small base**: One page, Spanish copy, shared site identity, and no speculative API, auth, store, or service folders.

The reusable custom files live in `assets/template/`. Next.js and shadcn generate the framework files and UI primitive so the skill does not ship stale dependency metadata or a frozen copy of the button.

---

→ Full spec & rules: [SKILL.md](./SKILL.md)

<div align="center">
  <sub>Built for developers who want a focused Next.js foundation with room to grow.</sub>
  <br><br>
  <sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="./LICENSE.txt">Apache-2.0</a></sub>
</div>
