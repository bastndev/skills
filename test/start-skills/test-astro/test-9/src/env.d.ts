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
