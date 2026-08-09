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
export interface Route {
  href: string;
  label: string;
}

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

export const SITE: SiteConfig = {
  name: '{{PROJECT_NAME}}',
  description: 'A simple, scalable Astro base — ready to grow from a portfolio to a full app.',
  url: 'https://example.com',
};

export const ROUTES: Route[] = [
  { href: '/', label: 'Home' },
  { href: '/work', label: 'Work' },
  { href: '/contact', label: 'Contact' },
];
```

## `src/lib/utils.ts`

```ts
export function stripTrailingSlash(path: string): string {
  return path !== '/' && path.endsWith('/') ? path.slice(0, -1) : path;
}
```

## `src/env.d.ts`

```ts
/// <reference types="astro/client" />

interface ImportMetaEnv {
  // Example: readonly PUBLIC_SITE_URL: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
```

## `src/content.config.ts`

Astro 7 puts the Content Collections config at the src root (not `src/content/config.ts`). It ships with no active collections; the recipe lives in `ARCHITECTURE.md` instead of as a large commented block in the source file.

```ts
export const collections = {};
```

## `src/pages/api/hello.ts`

The "backend door" — a working endpoint in the default static build. Runtime-server guidance stays in `ARCHITECTURE.md`, keeping the endpoint itself focused.

```ts
import type { APIRoute } from 'astro';

export const GET: APIRoute = () => {
  return new Response(JSON.stringify({ status: 'ok' }), {
    headers: { 'Content-Type': 'application/json' },
  });
};
```
