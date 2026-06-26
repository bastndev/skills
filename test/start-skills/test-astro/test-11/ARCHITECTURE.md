# Architecture — test-11

A simple but scalable Astro base. It starts as light as a portfolio, yet every
folder a growing project needs is already here — so you never restructure, you
only fill in. Pure Astro, a zero-dependency light/dark theme, native View
Transitions, Content Collections ready, and a backend door (`lib/` + `pages/api/`)
left open.

## File map

```
test-11/
│
├── public/                   # Served AS-IS at the site root — no processing
│   ├── favicon.svg           #   also reused, read-only, as the header logo
│   ├── favicon.ico
│   └── fonts/                #   self-hosted fonts (.woff2) — see fonts/README.md
│
├── src/
│   ├── assets/               # Imported in code → optimized & hashed by Astro/Vite
│   │   ├── images/
│   │   └── icons/            #   custom inline SVGs (e.g. social/) imported as components
│   │
│   ├── components/           # Reusable pieces shared across pages
│   │   ├── ui/               #   small primitives — ui/buttons/BackButton404.astro
│   │   ├── Header.astro      #   logo + centered nav (from ROUTES) + theme toggle
│   │   └── GXB.astro         #   ASCII hero + social-links row (one source for the art)
│   │
│   ├── sections/             # Page-level blocks (Hero, Footer, FeatureGrid…)
│   │   └── Footer.astro      #   minimal footer (brand + year)
│   │
│   ├── layouts/
│   │   └── Layout.astro      #   HTML shell: <head>, ClientRouter, no-flash theme
│   │                         #   script, <Header />, <slot />, <Footer />
│   │
│   ├── content/              # Content Collection entries — one PLURAL folder
│   │                         #   per collection (blog/, projects/…)
│   │
│   ├── pages/                # File-based routing
│   │   ├── index.astro       #   Home
│   │   ├── work/
│   │   │   └── index.astro   #   Work → /work (folder per route, room to grow)
│   │   ├── contact/
│   │   │   └── index.astro   #   Contact → /contact
│   │   ├── 404.astro         #   typing-animation 404, hides nav/footer, links home
│   │   └── api/
│   │       └── hello.ts      #   example endpoint → GET /api/hello
│   │
│   ├── lib/                  # Framework-agnostic helpers (no UI)
│   │   └── utils.ts
│   ├── types/               # Shared TypeScript types
│   │   └── index.ts
│   │
│   ├── styles/
│   │   └── global.css        #   design tokens (CSS vars: light + dark) + base
│   │
│   ├── content.config.ts     # Content Collections schema (Astro 7 location)
│   ├── consts.ts             # SITE config + ROUTES registry — single source
│   └── env.d.ts              # Typed import.meta.env
│
├── astro.config.mjs
├── tsconfig.json
├── package.json
├── ARCHITECTURE.md           # this file
└── README.md
```

## public/ vs src/assets/

Both hold static files; Astro treats them oppositely.

- **`public/`** — served verbatim at a fixed URL (`/favicon.svg`). No
  optimization, no hashing. Use for the favicon, `robots.txt`, OG images, and
  fonts referenced from CSS — anything that needs a stable, predictable URL.
- **`src/assets/`** — processed by Astro/Vite: compressed, converted
  (AVIF/WebP), and given a hashed filename for cache-busting. You `import` these
  in code.

The rule: **do you `import` it?** → `assets/`. **Do you point at a fixed URL?**
→ `public/`.

## Folder conventions

- **components/** — reused across pages. `ui/` holds tiny primitives; larger
  shared widgets sit at the root.
- **sections/** — a whole band of a page (hero, footer, feature grid). A page is
  mostly an assembly of sections.
- **lib/** — pure helpers with no UI (formatting, fetch wrappers, utilities).
- **types/** — shared `.ts` type definitions imported by both server and client.
- **services/ and stores/** — intentionally absent. Add `services/` when you talk
  to an external API, `stores/` when you need global client state. Grow by
  addition; don't ship empty folders.

## Imports (the `@` alias)

`@/` maps to `src/` (set in `tsconfig.json` → `compilerOptions.paths`). Import
with an absolute, refactor-proof path instead of brittle `../../` chains:

```ts
import Layout from '@/layouts/Layout.astro';
import { ROUTES } from '@/consts';
import { stripTrailingSlash } from '@/lib/utils';
```

Astro/Vite read the same alias from `tsconfig.json`, so it works in `.astro`,
`.ts`, and styles alike — no extra config.

## Icons

Two sources:

- **Lucide** (`@lucide/astro`) for standard line icons — used directly:
  ```astro
  import { Search } from '@lucide/astro';
  <Search />
  ```
- **Custom / brand icons** as raw `.svg` files in `src/assets/icons/`, imported
  either as components or as raw strings (`?raw`) for `set:html` (Astro 7 renders
  `*.svg` imports inline):
  ```astro
  import X from '@/assets/icons/social/x.svg';
  <X />
  ```
  Brand logos (X, GitHub, LinkedIn, Instagram, YouTube, TikTok, Facebook) live
  here because Lucide doesn't ship brand marks. The set is one consistent outline
  style, and each file's `viewBox` is tuned so they look the same size in the hero
  social row. Files are lowercase `kebab-case`, grouped in subfolders (`social/`,
  `theme/`, and add `ui/`, `payment/`, … as needed).

Both render inline and inherit `currentColor`, so size and color come from CSS —
they follow the light/dark theme for free:

```css
.icon { width: 24px; height: 24px; color: var(--color-nav-text); }
```

## Theme (light / dark)

- Every color is a CSS variable in `global.css`. Light values on `:root`; dark
  overrides under `[data-theme="dark"]`. Always use the variables, never raw hex,
  so your components follow the theme.
- An inline script in `Layout.astro`'s `<head>` sets `data-theme` from
  `localStorage` (falling back to OS preference) **before first paint** — no
  flash. It re-applies on `astro:after-swap` so View Transitions don't reset it.
- The toggle in `Header.astro` flips `data-theme` and re-binds on
  `astro:page-load`.

## Site name & the ROUTES registry

- The project name lives once in `SITE.name` (`consts.ts`). `Layout.astro`
  composes the `<title>` (`<page> · <SITE.name>`) and passes the brand to the
  header from it. **Rename the project in one place.**
- All top-level routes live once in `ROUTES` (`consts.ts`). `Header.astro` builds
  its nav from it and `404.astro` links home from it — add a route in one place
  and everything updates.
- `<ClientRouter />` (in `Layout.astro`) makes navigation SPA-style with a fade.
- `Header.astro` marks the active link by comparing `Astro.url.pathname`.

## Routing convention: plural index, singular detail

For any collection of things, follow the npm-style pattern (be consistent — never
mix the two for the same kind of thing):

```
/projects                  →  src/pages/projects/index.astro   (PLURAL — lists all)
/project/my-thing          →  src/pages/project/[slug].astro    (SINGULAR — one detail)
src/content/projects/*.md  →  the data (PLURAL — it holds many)
```

The detail page reads from the **plural** collection; the folder name and the
public URL don't have to match. Slugs are always lowercase `kebab-case`.

Only index routes go in the `ROUTES` registry — detail routes are generated from
the collection, not hand-listed.

## Content Collections

- Schemas are defined in `src/content.config.ts` (collections named in plural).
- Entries live in `src/content/<collection>/`.
- Pages read them with `getCollection()` / `getStaticPaths()`.

## Backend (lib/ + pages/api/)

The structure is ready for a backend, but the project ships **static (SSG)** — no
adapter, nothing to configure. `pages/api/` endpoints work prerendered (see
`api/hello.ts`).

When you need dynamic server logic (auth, a database, runtime API routes):
1. add an adapter (`@astrojs/vercel`, `@astrojs/node`, …),
2. set `output: 'server'` (or `'hybrid'`) in `astro.config.mjs`,
3. opt routes into SSR with `export const prerender = false`.

Until then, don't add the adapter — it's config you don't need yet.

## Recipes

**Add a page**
1. Create `src/pages/<name>.astro` (wrap `Layout`, drop in your content).
2. Add `{ href: '/<name>', label: '<Name>' }` to `ROUTES` in `consts.ts`.

**Add a collection (e.g. projects)**
1. Define the `projects` schema in `src/content.config.ts`.
2. Add entries under `src/content/projects/`.
3. List at `src/pages/projects/index.astro`; detail at
   `src/pages/project/[slug].astro` reading the `projects` collection.

## Commands

```bash
bun run dev      # local dev server with HMR
bun run build    # production build into dist/
bun run preview  # serve the production build locally
```
