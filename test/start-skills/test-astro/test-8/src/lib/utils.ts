// Framework-agnostic helpers. No UI, no Astro-specific imports — pure functions
// that any page, component, or endpoint can reuse.

/**
 * Normalise trailing slashes so paths compare equal in dev (`/work`) and in the
 * static build/preview (`/work/`). Root (`/`) is left untouched.
 */
export function stripTrailingSlash(path: string): string {
  return path !== '/' && path.endsWith('/') ? path.slice(0, -1) : path;
}
