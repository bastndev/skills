# Web projects — what to check

Covers Next.js, Astro, Vite (+React/Vue/Svelte), Remix, Nuxt, SvelteKit, or
plain bundler-based sites. Not every item applies to every framework — use
judgment.

## Rendering strategy
This is usually the single most defining architectural fact about a web
project. Find it in config, don't guess from the framework name alone:

- **Next.js**: App Router vs Pages Router (check for `app/` vs `pages/`).
  Server Components vs Client Components (`"use client"` directives). API
  routes / route handlers. `output` mode if set (`export`, `standalone`).
- **Astro**: `output` in `astro.config.*` (`static`, `server`, `hybrid`), and
  the `adapter`. Islands architecture — which components are islands, which
  `client:*` directive each uses (`load`, `idle`, `visible`, `only`) and
  whether that choice makes sense. Content Collections — are they used, and
  what do the Zod schemas look like.
- **Remix/Nuxt/SvelteKit**: loaders/actions or equivalent data-loading
  convention, file-based routing conventions specific to that framework.
- **Vite (no meta-framework)**: it's just a build tool here — the
  "architecture" is whatever app code does, not Vite itself.

## Routing
File-based vs explicitly configured. Dynamic segments. Any middleware.

## Styling approach
Tailwind, CSS Modules, styled-components/Emotion, vanilla CSS with custom
properties, or a mix. If there's a design-token system, that's worth its own
mention.

## State / data flow across components
Within a single framework's component tree this is usually straightforward,
but cross-island (Astro) or cross-route (SPA) state is worth flagging:
nanostores, Zustand, Redux, Context, signals, or just URL/query params as
state.

## Data fetching
`fetch` inside loaders/`getServerSideProps`/server components, React
Query/SWR/TanStack Query, a GraphQL client, or direct calls scattered through
components (worth flagging if so).

## Integrations / plugins
Astro integrations (`@astrojs/react`, `@astrojs/tailwind`, etc.) or
Next.js/Vite plugins — list what's installed and what it's actually doing in
this project, not its generic description.

## Build/deploy target
Adapter or output target (Vercel, Netlify, Node server, static export,
Cloudflare, etc.) — this often explains other decisions in the codebase.
