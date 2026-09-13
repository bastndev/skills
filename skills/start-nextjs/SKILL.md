---
name: start-nextjs
description: Scaffold a new Next.js App Router project with Bun, TypeScript, Tailwind CSS, shadcn/ui, Lucide icons, and next-themes. Use when starting, creating, or bootstrapping a Next.js website or "proyecto nextjs" from this minimal base in the current directory.
license: Complete terms in LICENSE.txt
metadata:
  author: bastndev
  version: "1.0.0"
---

# Next.js project scaffold

Create a focused Next.js base with application code under `src/`, shadcn components under `src/components/ui/shadcn/`, and a working light/dark theme. Use the official CLIs for framework and UI scaffolding; copy the custom files from `assets/template/`.

## Inputs and boundaries

- Use the current directory as the project root unless the user explicitly supplies another destination. Derive `PROJECT_NAME` from that directory's basename and preserve its visible spelling and casing. Do not ask for a name when one is already available.
- Inspect the destination before writing. Preserve unrelated files, editor settings, agent instructions, and skill-installation metadata. Stop before overwriting user-authored project files; this skill creates a new project, not a migration.
- Use Bun and keep `bun.lock`. Do not initialize Git, deploy, or add a publishing workflow unless requested.
- Default to TypeScript, App Router, Tailwind CSS, ESLint, Geist Sans/Mono, and Spanish document language and starter copy. Explicit user choices override these defaults.
- Keep the starter small: one home page and the theme control. Add routes, authentication, databases, stores, API handlers, and more shadcn components only when requested or needed by the actual project.

## Procedure

### 1. Create the project

Run in the destination directory:

```bash
bun create next-app@latest . --ts --tailwind --eslint --app --src-dir --import-alias '@/*' --use-bun --no-react-compiler --disable-git --yes
```

`--src-dir` creates `src/app` directly. Keep `public/`, `package.json`, `tsconfig.json`, and framework/tool configuration at the root; do not move every generated folder into `src/`.

If an option changes, inspect `bun create next-app@latest --help` and select the equivalent setup. Do not silently accept saved CLI preferences that change the requested stack. If the directory name is rejected or a real file conflict prevents scaffolding, explain the exact blocker instead of renaming the directory, deleting files, or creating a substitute project elsewhere.

### 2. Install icons and themes

```bash
bun add lucide-react next-themes
```

### 3. Initialize shadcn/ui

Initialize inside the project that was just created:

```bash
bunx --bun shadcn@latest init --defaults
```

Use the CLI's default UI preset unless the user supplied one. Keep CSS variables enabled and Lucide as the icon library. Do not pass a new project name or scaffold a second app. Inspect `init --help` if the installed CLI changes its options.

Before adding the button, merge these values into the generated root `components.json`, preserving its other settings:

```json
{
  "rsc": true,
  "tsx": true,
  "iconLibrary": "lucide",
  "tailwind": {
    "css": "src/app/globals.css",
    "cssVariables": true
  },
  "aliases": {
    "components": "@/components",
    "ui": "@/components/ui/shadcn",
    "utils": "@/lib/utils",
    "lib": "@/lib",
    "hooks": "@/hooks"
  }
}
```

Confirm `tsconfig.json` maps `@/*` to `./src/*`. Alias entries do not require empty directories. Preserve the utility generated in `src/lib/utils.ts`; newer presets may re-export `cn` from a package and import that package directly in components.

Some presets create a button during initialization. If `src/components/ui/button.tsx` already exists, relocate that fresh generated file to `src/components/ui/shadcn/button.tsx` and repair any imports before the next command. Do not leave two copies or overwrite an existing destination.

```bash
bunx --bun shadcn@latest add button --yes
```

Confirm the resulting file is `src/components/ui/shadcn/button.tsx` and its utility import resolves, whether it uses `@/lib/utils` or an installed `cn` package. If the CLI asks to overwrite the identical button supplied by initialization, keep the existing file. Let the CLI install the button's actual dependencies rather than maintaining a guessed dependency list.

### 4. Apply the bundled files

Resolve the directory containing this `SKILL.md` as `SKILL_DIR`. Copy every file from `SKILL_DIR/assets/template/` into the project root, replacing only the corresponding fresh scaffold files. The bundled layout preserves Geist Sans/Mono and provides the complete theme integration; the home page makes the toggle immediately usable.

Replace `{{PROJECT_NAME}}` in exactly these files:

- `src/consts.ts` — safely escape the value as a TypeScript string.
- `README.md` — visible project title.

Check that the placeholder is gone:

```bash
rg -n '\{\{PROJECT_NAME\}\}' src/consts.ts README.md
```

No matches is the expected result (`rg` exits with status 1). Preserve generated package metadata, dependency versions, configuration, favicons, and agent instructions. Do not overwrite `globals.css` with an Astro stylesheet or a handwritten replacement for shadcn's tokens.

### 5. Align global styles

Edit the existing `src/app/globals.css` in place:

- Keep Tailwind/shadcn imports, the class-based dark variant, semantic tokens, and base-layer rules.
- Set `--background: #fafafa` and `--foreground: #000000` in `:root`; set `--background: #101010` and `--foreground: #ffffff` in `.dark`. The body uses `bg-background text-foreground`, so the user's colors and shadcn's theme share one source.
- Map Tailwind's `--font-sans` and `--font-mono` to `var(--font-geist-sans)` and `var(--font-geist-mono)`. Remove a leftover scaffold `body { font-family: Arial, ... }` if it overrides Geist.
- Remove only leftover scaffold `prefers-color-scheme` color overrides that compete with the `.dark` class. Keep accessibility media queries and unrelated user CSS.
- Keep color changes immediate. The bundled button limits animation to the Sun/Moon transforms and disables that motion for `prefers-reduced-motion`.

### 6. Verify the generated project

```bash
bun run lint
bun run build
```

If the generated project has no lint script, use its installed ESLint CLI (`bunx --no-install eslint .`). Use the selected linter's generated command if the user chose another linter; do not install a second one. Do not use the removed `next lint` command.

Read failures, make focused corrections, and rerun the failed check. A dependency, registry, or font-download failure is not a passing build: report the blocker without silently replacing the requested fonts, changing versions, or disabling checks. On an interrupted setup, inspect completed files and resume the remaining steps; do not rerun initialization over modified files.

When a browser is available, briefly preview and verify:

- Fresh storage with both light and dark OS preferences; the first click switches to the opposite resolved theme.
- The explicit choice survives reload and overrides the OS preference.
- The button is reachable with Tab and works with Enter/Space, has an accessible name and visible focus, and respects reduced motion.
- The console has no hydration errors. Verify that the server-rendered page content remains visible before hydration.

Stop any preview started solely for verification. If browser checks cannot be performed, state that separately; a build does not prove interactive behavior. Run `git diff --check` when the project is a Git repository.

## Template ownership

```text
assets/template/
├── src/
│   ├── app/
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── components/
│   │   ├── theme-provider.tsx
│   │   └── theme-toggle.tsx
│   └── consts.ts
└── README.md
```

- The root layout owns metadata, fonts, global CSS, and the document shell. Keep it and the home page as Server Components.
- `theme-provider.tsx` and `theme-toggle.tsx` own client behavior. Pass server-rendered children through the provider; do not mark the whole app `"use client"`.
- `next-themes` owns persistence, system preference, and the initial theme script. Do not add a second storage implementation or wrap the entire page in a mounted-state guard.
- Use `resolvedTheme` in the click handler so `"system"` toggles correctly. Keep server and initial client markup stable: both decorative icons are rendered, their visibility follows CSS, and the accessible label is theme-independent.
- Limit `suppressHydrationWarning` to `<html>`, where `next-themes` changes attributes before hydration. Do not use it to conceal component mismatches.
- shadcn owns the generated button and utility; `components.json` owns where future UI components are installed. Do not bundle stale copies of these generated files.

## Completion report

Report the destination, project name, installed stack, `src/` structure, theme behavior, and actual validation results. Keep unperformed browser checks explicit. After the build succeeds, end with:

```text
Project created successfully 🎉
bun run dev
```

## Official references

Consult these when a CLI or integration differs from this procedure:

- [create-next-app options](https://nextjs.org/docs/app/api-reference/cli/create-next-app)
- [shadcn with Next.js](https://ui.shadcn.com/docs/installation/next) and [component aliases](https://ui.shadcn.com/docs/components-json)
- [shadcn theme integration](https://ui.shadcn.com/docs/dark-mode/next)
- [next-themes: system theme and hydration](https://github.com/pacocoursey/next-themes)
