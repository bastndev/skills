<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/github/icons/start-logo/start-astro.webp" width="150" />
</p>

<h1 align="center">[Start] / Astro Starter</h1>

<p align="center">
  <strong>Start Astro</strong> — Scaffold a minimal Astro project with theme toggle and View Transitions
</p>

<p align="center">
  <a href="../../README.md">← Back to Start / Middle / [End]</a>
</p>

---

Scaffolds a new Astro project using the `minimal` template, overlaid with a clean, **scalable** architecture — ready to grow from a portfolio to a full app. It sets up a shared layout, a header (logo + centered nav) and footer, four pages (incl. a themed 404), a zero-dependency light/dark theme toggle, native View Transitions, a `@/` path alias, a `SITE` + `ROUTES` single-source-of-truth config, icons (Lucide + custom brand SVGs), and Content Collections — right out of the box.

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

## Install

```bash
npx skills add bastndev/skills --skill start-astro
```

## Features

- **Minimal Base** — The empty `minimal` Astro template, no boilerplate to clean up. Static-first.
- **Layout + Header + Footer** — A shared shell wrapping every page.
- **Pages** — `Home`, `Work`, `Contact`, plus a themed `404`.
- **Theme Toggle** — Zero-dependency light/dark switch (CSS variables + vanilla JS) with no-flash + View Transitions support.
- **Single Source of Truth** — `SITE` + `ROUTES` in `consts.ts`: rename the project or add a route in one place.
- **`@/` Path Alias** — Clean imports from `src/`, no `../../` chains.
- **Icons** — [`@lucide/astro`](https://lucide.dev) line icons + a custom brand SVG set that inherits `currentColor`.
- **Content Collections** — Wired up (`content.config.ts`) and ready for blog/docs/projects.
- **Backend Door** — `lib/` + `pages/api/` ready; add an adapter only when you need a server.

---

→ Full spec & rules: [SKILL.md](./SKILL.md)

<div align="center">
  <sub>Built for developers who want to start their Astro projects with a robust foundation.</sub>
  <br><br>
  <sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="https://github.com/bastndev/skills/blob/main/LICENSE">MIT</a></sub>
</div>
