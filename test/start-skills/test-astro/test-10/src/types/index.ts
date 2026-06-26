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
