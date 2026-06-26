# Project structure, pages & root files

`{{PROJECT_NAME}}` is detected automatically from the current folder's name — the user already created and named it before invoking this skill (e.g. a folder called `TEST1` means `{{PROJECT_NAME}} = TEST1`, preserving its exact casing). Never ask for a name; never invent one. The skill writes files **into the current directory**, not a new sibling folder.

**The project name is name-free everywhere except three files** (`consts.ts`, `README.md`, `ARCHITECTURE.md`). The pages do **not** embed the name — they pass only a page title to `Layout`, which composes `<page> · <SITE.name>` itself. So `{{PROJECT_NAME}}` does **not** appear in any page below.

Final file tree after this skill runs (on top of the `minimal` template's `bun create astro` output):

```
{{PROJECT_NAME}}/                    ← the user's existing folder — never renamed
├── public/
│   ├── favicon.svg                 ← bun create astro default — DO NOT touch (also the header logo, read-only)
│   ├── favicon.ico                 ← bun create astro default — DO NOT touch / delete
│   └── fonts/
│       └── README.md               ← from this file
├── src/
│   ├── assets/
│   │   ├── images/.gitkeep         ← from this file
│   │   └── icons/
│   │       ├── social/*.svg        ← 11 brand icons, from references/icons.md
│   │       └── theme/{sun,moon}.svg ← toggle icons, from references/icons.md
│   ├── components/
│   │   ├── ui/.gitkeep             ← from this file
│   │   ├── Header.astro            ← from references/layout-header.md
│   │   └── GXB.astro               ← from this file (byte-for-byte)
│   ├── sections/
│   │   └── Footer.astro            ← from references/layout-header.md
│   ├── layouts/
│   │   └── Layout.astro            ← from references/layout-header.md
│   ├── content/.gitkeep            ← from this file
│   ├── pages/
│   │   ├── index.astro             ← Home (this file)
│   │   ├── work.astro              ← Work (this file)
│   │   ├── contact.astro           ← Contact (this file)
│   │   ├── 404.astro               ← this file
│   │   └── api/
│   │       └── hello.ts            ← from references/config-data-backend.md
│   ├── lib/utils.ts                ← from references/config-data-backend.md
│   ├── types/index.ts              ← from references/config-data-backend.md
│   ├── styles/global.css           ← from references/global-css.md
│   ├── consts.ts                   ← from references/config-data-backend.md
│   ├── content.config.ts           ← from references/config-data-backend.md
│   └── env.d.ts                    ← from references/config-data-backend.md
├── ARCHITECTURE.md                 ← from references/architecture.md
├── README.md                       ← from this file (overwrite the scaffold default)
├── .prettierignore                 ← from this file
├── astro.config.mjs                ← created by bun create astro, leave as-is
├── package.json                    ← created by bun create astro (+ bun add @lucide/astro)
└── tsconfig.json                   ← OVERWRITE — from references/config-data-backend.md
```

Each page is intentionally minimal: it wraps `Layout` and drops in the shared `GXB` hero with a one-line tagline. The ASCII art lives **only** in `GXB.astro`.

## `src/components/GXB.astro` (write byte-for-byte — do not edit the art)

The hero shown on **every** page: the ASCII-art logo + a per-page tagline (the `text` prop). The art lives here and nowhere else. The `<pre>` is `aria-hidden` because the art is decorative; screen readers get the tagline. (To rebrand later, edit the `logo` constant — e.g. generate new art at [patorjk.com/software/taag](https://patorjk.com/software/taag/) with the "ANSI Shadow" font.)

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
import Layout from '@/layouts/Layout.astro';
import GXB from '@/components/GXB.astro';
---

<Layout title="Home">
  <GXB text="Welcome — the starting point of your new Astro project." />
</Layout>
```

## `src/pages/work.astro`

```astro
---
import Layout from '@/layouts/Layout.astro';
import GXB from '@/components/GXB.astro';
---

<Layout title="Work">
  <GXB text="Work — a place to showcase your projects." />
</Layout>
```

## `src/pages/contact.astro`

```astro
---
import Layout from '@/layouts/Layout.astro';
import GXB from '@/components/GXB.astro';
---

<Layout title="Contact">
  <GXB text="Contact — get in touch or drop your details here." />
</Layout>
```

## `src/pages/404.astro`

Reuses `GXB` (never duplicate the art) and links home from the `ROUTES` registry.

```astro
---
import Layout from '@/layouts/Layout.astro';
import GXB from '@/components/GXB.astro';
import { ROUTES } from '@/consts';

// Link home from the routes registry — never hard-code "/" here.
const home = ROUTES[0];
---

<Layout title="404">
  <GXB text="404 — this page wandered off." />
  <p class="back">
    <a href={home.href}>← Back to {home.label}</a>
  </p>
</Layout>

<style>
  .back {
    text-align: center;
    margin: 0 0 3rem;
  }
  .back a {
    color: var(--color-link);
    text-decoration: none;
    font-size: 1rem;
  }
  .back a:hover {
    color: var(--color-link-hover);
  }
</style>
```

## `README.md` (overwrite the scaffold default — substitute `{{PROJECT_NAME}}` in the title)

````markdown
# {{PROJECT_NAME}}

A simple but scalable Astro base — ready to grow from a portfolio to a full app.
Pure Astro (no UI framework), a zero-dependency light/dark theme, native View
Transitions, Content Collections wired up, and an open backend door.

## Features

- ⚡ **Astro 7**, static-first (SSG) — add an adapter only when you actually need a server.
- 🌗 **Light/dark theme** — CSS variables + a no-flash inline script that survives View Transitions. Zero runtime deps.
- 🔀 **View Transitions** — SPA-style fades between pages.
- 🧭 **Connected routes** — the nav and the 404 page both read one `ROUTES` registry in `src/consts.ts`.
- 🎨 **Icons** — [`@lucide/astro`](https://lucide.dev) for line icons; custom/brand SVGs in `src/assets/icons/`.
- 📦 **Content Collections** ready (`src/content.config.ts`).
- 🏷️ **`@/` path alias** → `src/` (no `../../` chains).
- 🧱 **Scalable structure** — `components/`, `sections/`, `lib/`, `types/`, `content/`, `pages/api/`.

See **[ARCHITECTURE.md](./ARCHITECTURE.md)** for the full layout, conventions, and recipes.

## Project structure

```text
src/
├── assets/icons/      # custom + brand SVGs (social/, theme/)
├── components/        # reusable UI (Header, GXB, ui/)
├── sections/          # page-level blocks (Footer, …)
├── layouts/           # Layout.astro — the HTML shell every page wraps in
├── content/           # Content Collection entries
├── pages/             # file-based routes (+ api/, 404.astro)
├── lib/               # framework-agnostic helpers
├── types/             # shared TypeScript types
├── styles/            # global.css — design tokens (light + dark)
├── consts.ts          # SITE config + ROUTES registry
└── content.config.ts  # Content Collection schemas
```

## Commands

All commands are run from the project root:

| Command           | Action                                       |
| :---------------- | :------------------------------------------- |
| `bun install`     | Install dependencies                         |
| `bun run dev`     | Start the dev server at `localhost:4321`     |
| `bun run build`   | Build the production site to `./dist/`       |
| `bun run preview` | Preview the production build locally         |

## Getting started

1. Set your name, description, and URL in `src/consts.ts` (`SITE`).
2. Add or rename routes in `ROUTES` (same file) — the nav and the 404 page follow automatically.
3. Tweak colors in `src/styles/global.css` (CSS variables, light + dark).
4. Build pages in `src/pages/`, page sections in `src/sections/`, helpers in `src/lib/`.

## Learn more

Astro documentation: <https://docs.astro.build>
````

## `.prettierignore` (project root)

Skips generated output and keeps `public/` (incl. the default favicon) untouched by formatting.

```
# Build output & generated files
dist/
.astro/

# Lockfile
bun.lock

# Static assets — keep public/ (incl. the default Astro favicon) untouched
public/
```

## `public/fonts/README.md`

```markdown
# Fonts

Drop self-hosted font files (`.woff2`) in this folder. They're served as-is at a
stable URL (`/fonts/your-font.woff2`), so reference them from
`src/styles/global.css`:

\```css
@font-face {
  font-family: 'Your Font';
  src: url('/fonts/your-font.woff2') format('woff2');
  font-weight: 400;
  font-display: swap;
}

body {
  font-family: 'Your Font', system-ui, sans-serif;
}
\```

**Why `public/fonts/` and not `src/assets/`?** Fonts need a stable, predictable
URL for `@font-face`. Files in `public/` are served untouched; files in
`src/assets/` get hashed filenames meant to be imported in code.
```

## `.gitkeep` placeholders (keep intentional-but-empty folders in version control)

Write a `.gitkeep` to each of these three folders. Content is a single comment line:

- `src/assets/images/.gitkeep`
  ```
  # Imported, optimized images live here. Purpose documented in ARCHITECTURE.md.
  ```
- `src/components/ui/.gitkeep`
  ```
  # Small reusable UI primitives (Button, Badge, Card…). See ARCHITECTURE.md.
  ```
- `src/content/.gitkeep`
  ```
  # Content Collection entries live here, one PLURAL folder per collection
  # (e.g. content/projects/, content/blog/). Schemas are in src/content.config.ts.
  ```

## Adding more pages later

1. Create `src/pages/{name}.astro` — import `Layout` + `GXB`, then `<GXB text="…" />`. Pass only a page title: `<Layout title="{Name}">`.
2. Add `{ href: '/{name}', label: '{Name}' }` to the `ROUTES` array in `src/consts.ts`.

The nav (Header), the 404 link, the title, and the theme all follow automatically — no other file changes.
