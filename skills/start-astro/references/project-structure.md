# Project structure & pages

Final file tree after this skill runs (on top of the `minimal` template's `bun create astro` output):

```
{{DIR}}/
├── src/
│   ├── components/
│   │   └── Header.astro        ← from references/layout-header.md
│   ├── layouts/
│   │   └── Layout.astro        ← from references/layout-header.md
│   ├── styles/
│   │   └── theme.css           ← from references/theme-toggle.md
│   └── pages/
│       ├── index.astro         ← Home
│       ├── work.astro          ← Work
│       ├── about.astro         ← About
│       └── contact.astro       ← Contact
├── public/                     ← created by `bun create astro` (favicon etc.)
├── astro.config.mjs            ← created by `bun create astro`, leave as-is
├── package.json                ← created by `bun create astro`, leave as-is
└── tsconfig.json                ← created by `bun create astro`, leave as-is
```

Each page is intentionally minimal — just enough content to prove the Layout/Header/theme/transitions work end to end. The user fills in real content afterward.

## `src/pages/index.astro`

```astro
---
import Layout from '../layouts/Layout.astro';
---

<Layout title="Home">
  <section class="page">
    <h1>Home</h1>
    <p>Welcome — this is the starting point of the site.</p>
  </section>
</Layout>

<style>
  .page {
    max-width: 960px;
    margin: 0 auto;
    padding: 3rem 1.5rem;
  }
  .page h1 {
    color: var(--color-text);
  }
  .page p {
    color: var(--color-text-muted);
  }
</style>
```

## `src/pages/work.astro`

```astro
---
import Layout from '../layouts/Layout.astro';
---

<Layout title="Work">
  <section class="page">
    <h1>Work</h1>
    <p>A place to showcase projects.</p>
  </section>
</Layout>

<style>
  .page {
    max-width: 960px;
    margin: 0 auto;
    padding: 3rem 1.5rem;
  }
  .page h1 {
    color: var(--color-text);
  }
  .page p {
    color: var(--color-text-muted);
  }
</style>
```

## `src/pages/about.astro`

```astro
---
import Layout from '../layouts/Layout.astro';
---

<Layout title="About">
  <section class="page">
    <h1>About</h1>
    <p>A short bio or company description goes here.</p>
  </section>
</Layout>

<style>
  .page {
    max-width: 960px;
    margin: 0 auto;
    padding: 3rem 1.5rem;
  }
  .page h1 {
    color: var(--color-text);
  }
  .page p {
    color: var(--color-text-muted);
  }
</style>
```

## `src/pages/contact.astro`

```astro
---
import Layout from '../layouts/Layout.astro';
---

<Layout title="Contact">
  <section class="page">
    <h1>Contact</h1>
    <p>Get in touch — add a form or contact details here.</p>
  </section>
</Layout>

<style>
  .page {
    max-width: 960px;
    margin: 0 auto;
    padding: 3rem 1.5rem;
  }
  .page h1 {
    color: var(--color-text);
  }
  .page p {
    color: var(--color-text-muted);
  }
</style>
```

## Verification commands (run from `{{DIR}}`)

```bash
bun install
bun run build
```

`bun run build` must exit 0. It type-checks the `.astro` files and confirms every page imports `Layout.astro` correctly, every nav link resolves to a real page, and `theme.css` has no syntax errors — catches the most common mistakes (typo'd import path, missing closing tag) before the user ever opens the dev server.

## Adding more pages later

To add a 5th page, the pattern is always:
1. Create `src/pages/{name}.astro` following the same shape as the 4 above.
2. Add `{ href: '/{name}', label: '{Label}' }` to the `navItems` array in `src/components/Header.astro`.

No other file needs to change — the active-link highlighting and the theme toggle work automatically because they live in `Header.astro`/`Layout.astro`, which every page already imports.
