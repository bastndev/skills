# test-12

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
