# Project structure & pages

`{{PROJECT_NAME}}` is detected automatically from the current folder's name — the user already created and named it before invoking this skill (e.g. a folder called `TEST1` means `{{PROJECT_NAME}} = TEST1`, preserving its exact casing). Never ask the user for a name; never invent one. The skill scaffolds and writes files **into the current directory**, not into a newly-created sibling folder.

Every page passes `{{PROJECT_NAME}}` to `Layout.astro` twice: once inside the `title` string (for the browser tab) and once as the `projectName` prop (which `Layout.astro` forwards to `Header.astro` for the brand link). Substitute the real value everywhere `{{PROJECT_NAME}}` appears below — both occurrences on each page.

Final file tree after this skill runs (on top of the `minimal` template's `bun create astro` output), written directly into the current folder:

```
{{PROJECT_NAME}}/                 ← the user's existing folder (e.g. TEST1) — already created, never renamed
├── src/
│   ├── components/
│   │   ├── Header.astro        ← from references/layout-header.md
│   │   └── GXB.astro           ← from this file (shared ASCII logo + per-page tagline)
│   ├── layouts/
│   │   └── Layout.astro        ← from references/layout-header.md
│   ├── styles/
│   │   └── global.css          ← from references/theme-toggle.md
│   └── pages/
│       ├── index.astro         ← Home
│       ├── work.astro          ← Work
│       └── contact.astro       ← Contact
├── public/                     ← bun create astro defaults — DO NOT touch
│   ├── favicon.svg             ← leave untouched (also reused, read-only, as the header logo)
│   └── favicon.ico             ← leave untouched (never delete)
├── ARCHITECTURE.md             ← from references/architecture.md
├── .prettierignore             ← from this file
├── astro.config.mjs            ← created by `bun create astro`, leave as-is
├── package.json                ← created by `bun create astro`, leave as-is
└── tsconfig.json               ← created by `bun create astro`, leave as-is
```

Each page is intentionally minimal: it wraps `Layout` and drops in the shared `GXB` component, passing one line of text. The ASCII logo lives **only** in `GXB.astro`, so every page shows the same centered hero and the only thing that changes per page is the tagline. The user fills in real content afterward.

## `src/components/GXB.astro`

The hero shown on **every** page: the ASCII-art logo + a per-page tagline (the `text` prop). The art lives here and nowhere else — edit the `logo` constant to change it, or delete this one component to drop the hero from the whole site. The `<pre>` is `aria-hidden` because the art is decorative; screen readers get the tagline. Swap the art for your own (e.g. generated at [patorjk.com/software/taag](https://patorjk.com/software/taag/) with the "ANSI Shadow" font).

```astro
---
interface Props {
  text: string;
}

const { text } = Astro.props;

// ASCII-art logo — the single source for the art used on every page. Edit or
// delete it here to change/remove it site-wide. The first line starts with a
// leading space; keep it, it aligns the glyphs.
const logo = ` ██████╗ ██╗  ██╗██████╗
██╔════╝ ╚██╗██╔╝██╔══██╗
██║  ███╗ ╚███╔╝ ██████╔╝
██║   ██║ ██╔██╗ ██╔══██╗
╚██████╔╝██╔╝ ██╗██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═════╝ `;
---

<section class="hero">
  <pre class="hero-logo" aria-hidden="true">{logo}</pre>
  <p class="hero-text">{text}</p>
</section>

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

## `src/pages/index.astro` (Home)

```astro
---
import Layout from '../layouts/Layout.astro';
import GXB from '../components/GXB.astro';
---

<Layout title={`Home · {{PROJECT_NAME}}`} projectName="{{PROJECT_NAME}}">
  <GXB text="Welcome — the starting point of your new Astro project." />
</Layout>
```

## `src/pages/work.astro`

```astro
---
import Layout from '../layouts/Layout.astro';
import GXB from '../components/GXB.astro';
---

<Layout title={`Work · {{PROJECT_NAME}}`} projectName="{{PROJECT_NAME}}">
  <GXB text="Work — a place to showcase your projects." />
</Layout>
```

## `src/pages/contact.astro`

```astro
---
import Layout from '../layouts/Layout.astro';
import GXB from '../components/GXB.astro';
---

<Layout title={`Contact · {{PROJECT_NAME}}`} projectName="{{PROJECT_NAME}}">
  <GXB text="Contact — get in touch or drop your details here." />
</Layout>
```

## `.prettierignore`

Written to the project root so Prettier (editor-on-save or CLI) skips generated output and, importantly, **never reformats the default favicon** or anything else in `public/`.

```
# Build output & generated files
dist/
.astro/

# Lockfile
bun.lock

# Static assets — keep public/ (incl. the default Astro favicon) untouched
public/
```

## Verification commands (run from the project root — no `cd` needed, already there)

```bash
bun install
bun run build
```

`bun run build` must exit 0. It type-checks the `.astro` files and confirms every page imports `Layout.astro` correctly, every nav link resolves to a real page, and `global.css` has no syntax errors — catches the most common mistakes (typo'd import path, missing closing tag) before the user ever opens the dev server.

## Adding more pages later

To add another page, the pattern is always:
1. Create `src/pages/{name}.astro` following the same shape as the pages above — import `Layout` + `GXB`, then `<GXB text="{Label} — short description." />`.
2. Add `{ href: '/{name}', label: '{Label}' }` to the `navItems` array in `src/components/Header.astro`.

No other file needs to change — the hero/ASCII art, active-link highlighting, and theme toggle all live in `GXB.astro`/`Header.astro`/`Layout.astro`, which every page already imports.
