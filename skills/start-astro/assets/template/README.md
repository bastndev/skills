# {{PROJECT_NAME}}

A small, production-ready Astro base with accessible light/dark themes, client-side page transitions,
and a structure that grows only when the site needs it.

## What is included

- Astro 7 with static output.
- Pure Astro components and scoped CSS.
- A no-flash light/dark theme that survives client-side navigation.
- Header, centered GXB content, social links, footer, and 404 page.
- One route registry for navigation and active-link state.
- Lucide interface icons and local SVG brand icons.
- The `@/` alias for imports from `src/`.

Optional systems such as content collections, API routes, adapters, services, and stores are intentionally
absent. Add them when the real site requires them instead of maintaining empty scaffolding.

## Project structure

```text
src/
├── assets/icons/social/ # Local brand icons imported by GXB
├── components/          # GXB, Header, and reusable UI primitives
│   └── ui/buttons/      # BackButton404 and ThemeToggle
├── layouts/             # Document shell and global theme bootstrap
├── pages/               # File-based routes
├── sections/            # Page-level sections such as Footer
├── styles/global.css    # Theme tokens and true global foundations
├── consts.ts            # Site metadata and route registry
└── env.d.ts             # Astro environment types
```

See [ARCHITECTURE.md](./ARCHITECTURE.md) for ownership rules and extension recipes.

## Commands

| Command                | Action                                        |
| :--------------------- | :-------------------------------------------- |
| `bun install`          | Install dependencies                          |
| `bun run dev`          | Start Astro locally                           |
| `bun run build`        | Create the static production build in `dist/` |
| `bun run preview`      | Preview the production build                  |

## Customize the base

1. Change the site name and description in `src/consts.ts`.
2. Update the routes in the same file.
3. Replace the social URLs in `src/components/GXB.astro`.
4. Adjust shared theme colors in `src/styles/global.css`.
5. Replace each placeholder page with real sections as the site grows.

Astro documentation: <https://docs.astro.build>
