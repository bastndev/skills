# Project structure & pages

`{{PROJECT_NAME}}` is detected automatically from the current folder's name — the user already created and named it before invoking this skill (e.g. a folder called `TEST1` means `{{PROJECT_NAME}} = TEST1`, preserving its exact casing). Never ask the user for a name; never invent one. The skill scaffolds and writes files **into the current directory**, not into a newly-created sibling folder.

Every page passes `{{PROJECT_NAME}}` to `Layout.astro` twice: once inside the `title` string (for the browser tab) and once as the `projectName` prop (which `Layout.astro` forwards to `Header.astro` for the brand link). Substitute the real value everywhere `{{PROJECT_NAME}}` appears below — both occurrences on each page.

Final file tree after this skill runs (on top of the `minimal` template's `bun create astro` output), written directly into the current folder:

```
{{PROJECT_NAME}}/                 ← the user's existing folder (e.g. TEST1) — already created, never renamed
├── src/
│   ├── components/
│   │   └── Header.astro        ← from references/layout-header.md
│   ├── layouts/
│   │   └── Layout.astro        ← from references/layout-header.md
│   ├── styles/
│   │   └── global.css          ← from references/theme-toggle.md
│   └── pages/
│       ├── index.astro         ← Home
│       ├── work.astro          ← Work
│       └── contact.astro       ← Contact
├── public/                     ← created by `bun create astro` (favicon etc.)
├── astro.config.mjs            ← created by `bun create astro`, leave as-is
├── package.json                ← created by `bun create astro`, leave as-is
└── tsconfig.json                ← created by `bun create astro`, leave as-is
```

Each page is intentionally minimal — just enough content to prove the Layout/Header/theme/transitions work end to end. The user fills in real content afterward.

## `src/pages/index.astro`

The Home page is a **centered hero**: an ASCII-art logo rendered in a `<pre>`, with the welcome line directly beneath it. The logo string lives in the frontmatter so the markup stays clean — swap it for the project's own ASCII (e.g. generated at [patorjk.com/software/taag](https://patorjk.com/software/taag/) with the "ANSI Shadow" font) to rebrand. The `<pre>` is `aria-hidden` because the art is decorative; screen readers get the heading-less welcome text instead.

```astro
---
import Layout from '../layouts/Layout.astro';

// Decorative ASCII logo for the Home hero. Replace with your own art.
// First line begins with a single leading space — keep it, it aligns the glyphs.
const logo = ` ██████╗ ██╗  ██╗██████╗
██╔════╝ ╚██╗██╔╝██╔══██╗
██║  ███╗ ╚███╔╝ ██████╔╝
██║   ██║ ██╔██╗ ██╔══██╗
╚██████╔╝██╔╝ ██╗██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═════╝ `;
---

<Layout title={`Home · {{PROJECT_NAME}}`} projectName="{{PROJECT_NAME}}">
  <section class="hero">
    <pre class="hero-logo" aria-hidden="true">{logo}</pre>
    <p class="hero-text">Welcome — this is the starting point of the site.</p>
  </section>
</Layout>

<style>
  .hero {
    flex: 1; /* fill <main> (see global.css) so the hero centers without a
                hard-coded height — that guess was overflowing into a scrollbar */
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    gap: 1.5rem;
    padding: 2rem 1.5rem;
  }
  .hero-logo {
    margin: 0;
    max-width: 100%;
    color: var(--color-accent);
    font-family: ui-monospace, 'Cascadia Code', 'JetBrains Mono', 'Fira Code', Menlo, Consolas, monospace;
    font-size: clamp(0.45rem, 2.2vw, 0.95rem);
    line-height: 1.1;
    white-space: pre;
  }
  .hero-text {
    margin: 0;
    color: var(--color-text-muted);
    font-size: 1.05rem;
  }
</style>
```

## `src/pages/work.astro`

```astro
---
import Layout from '../layouts/Layout.astro';
---

<Layout title={`Work · {{PROJECT_NAME}}`} projectName="{{PROJECT_NAME}}">
  <section class="page">
    <h1>Work</h1>
    <p>A place to showcase projects.</p>
  </section>
</Layout>

<style>
  .page {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 3rem 1.5rem;
    box-sizing: border-box;
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

<Layout title={`Contact · {{PROJECT_NAME}}`} projectName="{{PROJECT_NAME}}">
  <section class="page">
    <h1>Contact</h1>
    <p>Get in touch — add a form or contact details here.</p>
  </section>
</Layout>

<style>
  .page {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 3rem 1.5rem;
    box-sizing: border-box;
  }
  .page h1 {
    color: var(--color-text);
  }
  .page p {
    color: var(--color-text-muted);
  }
</style>
```

## Verification commands (run from the project root — no `cd` needed, already there)

```bash
bun install
bun run build
```

`bun run build` must exit 0. It type-checks the `.astro` files and confirms every page imports `Layout.astro` correctly, every nav link resolves to a real page, and `global.css` has no syntax errors — catches the most common mistakes (typo'd import path, missing closing tag) before the user ever opens the dev server.

## Adding more pages later

To add another page, the pattern is always:
1. Create `src/pages/{name}.astro` following the same shape as the pages above.
2. Add `{ href: '/{name}', label: '{Label}' }` to the `navItems` array in `src/components/Header.astro`.

No other file needs to change — the active-link highlighting and the theme toggle work automatically because they live in `Header.astro`/`Layout.astro`, which every page already imports.
