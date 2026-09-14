<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/github/icons/start-logo/start-next.webp" width="150" />
</p>

<h1 align="center">[Start] / Next.js Starter</h1>

<p align="center">
  <strong>Start Next.js</strong> — A focused App Router starter with Bun, five routes, and persistent light/dark themes
</p>

<p align="center">
  <a href="../../README.md">← Back to Start / Middle / [End]</a>
</p>

---

Creates a Next.js App Router project in the current directory with TypeScript, Tailwind CSS, ESLint, Geist, and Lucide icons. It applies the prepared template’s five routes, responsive workspace shell, social links, metadata, keyboard skip link, and accessible theme control.

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

1. **Detects** — Uses the current folder as the project root and its basename as the visible project name.
2. **Scaffolds** — Runs `create-next-app` with Bun, App Router, TypeScript, Tailwind CSS, ESLint, and `src/`.
3. **Applies** — Copies the bundled source, route groups, configuration, documentation, favicon, and public mark.
4. **Installs** — Adds Lucide as the only dependency beyond the generated Next.js stack.
5. **Verifies** — Runs lint, generated-route type checking, and a production build, then checks interaction in a browser when available.

## What You Get

```text
src/
├── app/
│   ├── (workspace)/
│   │   ├── page.tsx             # /
│   │   ├── work/page.tsx        # /work
│   │   ├── contact/page.tsx     # /contact
│   │   └── layout.tsx           # shared Header + Footer
│   ├── (auth)/
│   │   ├── login/page.tsx       # /login placeholder
│   │   └── register/page.tsx    # /register placeholder
│   ├── globals.css
│   └── layout.tsx
├── components/
│   ├── icons/social-media.tsx
│   ├── ui/{Header,Footer,GXB}.tsx
│   └── ThemeToggle.tsx
└── consts.ts

ARCHITECTURE.md · README.md · tsconfig.json · bun.lock
```

The route groups organize shared layouts without changing URLs or adding access control. Login and Register are intentionally plain UI placeholders; the starter does not claim to include authentication or a database.

## Theme and Structure

- **Dark by default** — A valid explicit light/dark choice is restored before paint and persisted in `localStorage`.
- **Storage fallback** — Theme switching still works for the current document if browser storage is unavailable.
- **Stable hydration** — Both icons stay rendered and CSS follows `data-theme`; the expected root attribute difference is suppressed only on `<html>`.
- **Accessible controls** — The toggle has contextual text, native keyboard behavior, visible focus, and reduced-motion support. Every route has a heading and the same skip-link target.
- **Clear ownership** — The root layout owns document concerns, the workspace layout owns Header and Footer, `consts.ts` owns metadata and navigation, and `GXB.tsx` owns social links.
- **Focused globals** — Theme tokens and document rules live in `globals.css`; component-specific Tailwind styling remains with each component.

The reusable source of truth lives in `assets/template/`. Framework package versions and routine configuration still come from `create-next-app`, which keeps the generated project current.

---

→ Full spec & rules: [SKILL.md](./SKILL.md)

<div align="center">
  <sub>Built for developers who want a focused Next.js foundation with room to grow.</sub>
  <br><br>
  <sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="./LICENSE.txt">Apache-2.0</a></sub>
</div>
