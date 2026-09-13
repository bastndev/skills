# {{PROJECT_NAME}}

Next.js App Router with Bun, TypeScript, Tailwind CSS, shadcn/ui, Lucide, and next-themes.

## Development

```bash
bun install
bun run dev
```

## Validation

```bash
bun run lint
bun run build
```

## Structure

```text
src/
├── app/                         # Routes, root layout, metadata, and global CSS
├── components/
│   ├── ui/shadcn/button.tsx     # Generated shadcn button
│   ├── theme-provider.tsx      # next-themes client boundary
│   └── theme-toggle.tsx        # Accessible light/dark control
├── lib/utils.ts                # shadcn class-name utility
└── consts.ts                   # Site name and description
```

Keep application code in `src/`; `public/` and framework configuration stay at the root. Update site identity in `src/consts.ts`. The initial page uses Spanish copy and `lang="es"`; change them together for another language.

The theme follows the operating system until an explicit choice is saved. Its colors live in `src/app/globals.css`. Geist Sans and Mono are loaded through `next/font/google`, which needs network access when building an uncached project.

To add another UI component:

```bash
bunx --bun shadcn@latest add input
```

`components.json` directs generated UI components to `src/components/ui/shadcn/`. Keep pages and layouts as Server Components; use client boundaries for interactive controls. Add shared logic, routes, or services when the app needs them.
