# Architecture

This base favors clear ownership over pre-created folders. A file or abstraction should exist because the
current site uses it, not because a future site might use it.

## Ownership

### `src/styles/global.css`

Keep only rules that genuinely affect the entire document:

- light and dark semantic color tokens;
- `box-sizing`;
- document scrollbar behavior;
- body typography, background, and text color.

Do not place component selectors here. Astro component styles are scoped automatically, so GXB, Header,
ThemeToggle, Footer, and page-specific rules stay beside their markup.

### `src/layouts/`

Layouts own the HTML document, metadata, global imports, page-shell geometry, client routing, and scripts
that must run before first paint. `Layout.astro` is the only place that imports `global.css`.

### `src/components/`

Components are reusable UI with a focused public API. Shared widgets such as GXB and Header live at the
root. Small primitives are grouped by kind under `ui/`, such as `ui/buttons/`.

### `src/sections/`

Sections are complete page bands such as a hero, footer, feature grid, or testimonials block. Their markup,
responsive behavior, and visual styling live together.

### `src/pages/`

Pages define routes and compose layouts and components. Top-level routes use `<route>/index.astro`, keeping
each route in its own folder.

## Theme

`Layout.astro` chooses a saved `light` or `dark` theme before paint and falls back to the operating-system
preference. `components/ui/buttons/ThemeToggle.astro` owns the interactive control and persists explicit
choices.

Global theme tokens are semantic and intentionally small:

- `--color-bg`
- `--color-text`
- `--color-border`
- `--color-scrollbar`

Component-only values stay local. Add a new global token only when multiple components share the same
meaning, not merely the same hex value.

## Scrollbar

The standard property takes exactly two colors:

```css
scrollbar-color: <thumb-color> <track-color>;
```

This base uses a visible themed thumb and a transparent track on `html`. A thumb appears only when the
document actually overflows.

## Routes

Astro creates public routes from files in `src/pages/`. `ROUTES` in `src/consts.ts` is not a second router;
it is the small registry used to render the primary navigation. Keep it synchronized with navigable top-level
pages. The 404 page verifies that the registry still contains `/`.

## Assets

- Put imported images and SVGs in `src/assets/` so Astro and Vite can process them.
- Put files in `public/` only when they require a stable, literal URL, such as favicons or `robots.txt`.
- Do not keep documentation or placeholders in `public/`; every file there is copied to production.

## Add capabilities when needed

### Content collections

Create `src/content.config.ts` and the corresponding content directory when the first real collection is
introduced. Follow Astro's content collection guide for the current loader and schema APIs.

### API or server rendering

Static endpoints can be added under `src/pages/api/`. Add an adapter and server output only when runtime
logic is required; an empty API example is not part of the base.

### Shared logic and types

Create `src/lib/` when logic has multiple consumers or deserves independent testing. Create `src/types/`
when types are genuinely shared across modules. Keep one-use helpers and interfaces beside their consumer.

## Code conventions

- Use `@/` imports across source files.
- Prefer semantic HTML before adding ARIA.
- Use scoped, low-specificity component styles.
- Order CSS by layout, box model, visual appearance, typography, then interaction.
- Respect `prefers-reduced-motion` for nonessential animation.
- Run `bun run build` before handing off changes.
