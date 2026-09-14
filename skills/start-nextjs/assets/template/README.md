# {{PROJECT_NAME}}

A small Next.js App Router starter using Bun, TypeScript, Tailwind CSS 4, Geist, and Lucide icons. Includes five example routes, a responsive header and footer, social links, and a light/dark toggle.

The pages are examples to replace as your project grows. Login and Register are placeholders; no authentication service or database is included.

## Run locally

```bash
bun install
bun run dev
```

Open [http://localhost:3000](http://localhost:3000).

## Check the project

```bash
bun run lint
bun run typecheck
bun run build
```

`typecheck` generates Next.js route types before checking TypeScript, so it also works before the first development run. To serve the production build, run `bun run start`.

## Customize

- Edit `src/consts.ts` for the site name, description, document language, and navigation. Social URLs live in `src/components/ui/GXB.tsx`; replace the included author URLs for your project.
- Replace the example content in `src/app/`. The `(workspace)` and `(auth)` folders organize layouts without changing URLs or protecting routes.
- Replace the sample ASCII logo in `src/components/ui/GXB.tsx`, `public/vercel.svg`, and `src/app/favicon.ico` when adding your branding.
- Keep theme tokens and document styles in `src/app/globals.css`; keep component styles with their components.

The theme defaults to dark and remembers an explicit choice in `localStorage`. A small script in the root layout restores it before the first paint. If storage is unavailable, switching still works for the current document. System theme detection is not enabled.

Each page has a main landmark and a heading. Workspace headings use `sr-only` to keep the minimal design while remaining available to screen readers. Replace them with visible headings when your page design needs one. The keyboard skip link targets `main-content` on every page.

Scrolling uses the browser default. Component transitions respect reduced-motion preferences.

See [ARCHITECTURE.md](ARCHITECTURE.md) for the file structure and extension points.
