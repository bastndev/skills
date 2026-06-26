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
