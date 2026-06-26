# Config, data & backend

Copy-paste ready, byte-for-byte. These wire up the `@/` path alias, the single-source-of-truth data (`consts.ts` + `types/`), a helper (`lib/`), typed env, Content Collections, and the example API route.

## `tsconfig.json` (OVERWRITE the scaffold's version)

Modern TypeScript: `paths` works **without** `baseUrl`. No React JSX settings (this base is pure Astro). Astro/Vite read this same alias, so `@/` works in `.astro`, `.ts`, and styles.

```json
{
  "extends": "astro/tsconfigs/strict",
  "include": [".astro/types.d.ts", "**/*"],
  "exclude": ["dist"],
  "compilerOptions": {
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
```

## `package.json`

Leave the file `bun create astro` generated as-is; **add the one runtime dependency** with `bun add @lucide/astro` (do not hand-edit `package.json`). After install it looks like:

```json
"dependencies": {
  "@lucide/astro": "^1.21.0",
  "astro": "^7.0.3"
}
```

## `src/types/index.ts`

```ts
// Shared TypeScript types. Import from here across the app: `import type { Route } from '../types'`.

/** A top-level navigation route, used by the ROUTES registry in `consts.ts`. */
export interface Route {
  href: string;
  label: string;
}

/** Site-wide configuration (name, description, canonical URL). */
export interface SiteConfig {
  name: string;
  description: string;
  url: string;
}
```

## `src/consts.ts` (substitute `{{PROJECT_NAME}}` in `SITE.name`)

The single source of truth. `SITE.name` is the **only** place the project name is written in code; the tab title, header brand, and footer all derive from it.

```ts
import type { Route, SiteConfig } from '@/types';

// Single source of truth for the site's name. Rename the project here once and
// the browser tab, the header brand, and the footer all follow.
export const SITE: SiteConfig = {
  name: '{{PROJECT_NAME}}',
  description: 'A simple, scalable Astro base — ready to grow from a portfolio to a full app.',
  url: 'https://example.com',
};

// The "connected routes" registry. Header builds its nav from this, and 404.astro
// links home from it — add a top-level page in ONE place and both update.
//
// Detail routes (e.g. /project/[slug]) are generated from Content Collections,
// not hand-listed here. See ARCHITECTURE.md → "Routing convention".
export const ROUTES: Route[] = [
  { href: '/', label: 'Home' },
  { href: '/work', label: 'Work' },
  { href: '/contact', label: 'Contact' },
];
```

## `src/lib/utils.ts`

```ts
// Framework-agnostic helpers. No UI, no Astro-specific imports — pure functions
// that any page, component, or endpoint can reuse.

/**
 * Normalise trailing slashes so paths compare equal in dev (`/work`) and in the
 * static build/preview (`/work/`). Root (`/`) is left untouched.
 */
export function stripTrailingSlash(path: string): string {
  return path !== '/' && path.endsWith('/') ? path.slice(0, -1) : path;
}
```

## `src/env.d.ts`

```ts
/// <reference types="astro/client" />

// Type your environment variables here for autocomplete + safety on
// `import.meta.env`. Astro exposes `PUBLIC_`-prefixed vars to the client;
// everything else stays server-only.
interface ImportMetaEnv {
  // readonly PUBLIC_SITE_URL: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
```

## `src/content.config.ts`

Astro 7 puts the Content Collections config at the src root (not `src/content/config.ts`). Ships with no active collections — an empty object is valid — plus a commented example.

```ts
// Content Collections config. In Astro 7 this lives at the src root as
// `content.config.ts` (not the older `src/content/config.ts`).
//
// Define collections here, named in PLURAL — a collection holds many entries.
// Entries live in `src/content/<collection>/`. Pages read them with
// getCollection() / getStaticPaths(). See ARCHITECTURE.md → "Content Collections".
//
// Example — uncomment and adapt:
//
// import { defineCollection, z } from 'astro:content';
// import { glob } from 'astro/loaders';
//
// const projects = defineCollection({
//   loader: glob({ pattern: '**/*.md', base: './src/content/projects' }),
//   schema: z.object({
//     title: z.string(),
//     description: z.string(),
//     repoUrl: z.string().url().optional(),
//   }),
// });
//
// export const collections = { projects };

export const collections = {};
```

## `src/pages/api/hello.ts`

The "backend door" — a working endpoint in the default static build. Keeps the project static-first; the comment tells the user exactly how to go dynamic later.

```ts
import type { APIRoute } from 'astro';

// Example backend endpoint → GET /api/hello.
//
// The backend door is open: this works in the default STATIC build (the response
// is prerendered at build time). For runtime/dynamic server logic — auth, a
// database, request-time responses — add an adapter (@astrojs/vercel,
// @astrojs/node, …), set `output: 'server'` in astro.config.mjs, and add
// `export const prerender = false` to the routes that need it.
export const GET: APIRoute = () => {
  return new Response(JSON.stringify({ status: 'ok' }), {
    headers: { 'Content-Type': 'application/json' },
  });
};
```
