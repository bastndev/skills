# Architecture — {{PROJECT_NAME}}

A minimal Astro starter: one shared layout, a header with a logo + centered nav, a
reusable hero, a zero-dependency light/dark theme, and native View Transitions.

## File map

```
src/
├── layouts/
│   └── Layout.astro      — the HTML shell every page wraps in: <head>, the
│                           <ClientRouter /> (View Transitions), the no-flash
│                           theme script, and <Header />.
├── components/
│   ├── Header.astro      — logo (a CSS mask of /public/favicon.svg) + centered
│   │                       nav (Home / Work / Contact) + the light/dark toggle.
│   └── Hero.astro        — centered ASCII logo + a per-page tagline (`text` prop).
│                           The ASCII art lives here and nowhere else.
├── styles/
│   └── global.css        — design tokens as CSS variables (light on :root, dark
│                           under [data-theme="dark"]) + the base body/main layout.
└── pages/
    ├── index.astro       — Home
    ├── work.astro        — Work
    └── contact.astro     — Contact
                            each page = <Layout><Hero text="…" /></Layout>

public/
├── favicon.svg           — default Astro favicon (also reused as the header logo)
└── favicon.ico           — default Astro favicon
```

## Theme (light / dark)

- Every color is a CSS variable in `global.css`. Light values sit on `:root`; dark
  values override them under `[data-theme="dark"]`. Use the variables (never raw
  hex) in your own components so they follow the theme automatically.
- An inline script in `Layout.astro`'s `<head>` sets `data-theme` from
  `localStorage` (falling back to the OS preference) **before first paint**, so the
  page never flashes the wrong theme on load.
- The toggle button in `Header.astro` flips `data-theme` and saves the choice.
- Because View Transitions swap the DOM in place, the theme is re-applied on
  `astro:after-swap` and the toggle re-binds on `astro:page-load` — without those,
  navigating would reset the theme and kill the button.

## Navigation

- `<ClientRouter />` (in `Layout.astro`) turns page changes into SPA-style swaps
  with a fade (`transition:animate="fade"` on `<main>`).
- `Header.astro` highlights the active link by comparing `Astro.url.pathname` to
  each item's `href` (re-evaluated server-side on every navigation).

## Adding a page

1. Create `src/pages/<name>.astro`:

   ```astro
   ---
   import Layout from '../layouts/Layout.astro';
   import Hero from '../components/Hero.astro';
   ---

   <Layout title={`<Name> · {{PROJECT_NAME}}`} projectName="{{PROJECT_NAME}}">
     <Hero text="<Name> — a short description." />
   </Layout>
   ```

2. Add `{ href: '/<name>', label: '<Name>' }` to `navItems` in `Header.astro`.

## Commands

```bash
bun run dev      # local dev server with HMR
bun run build    # production build into dist/
bun run preview  # serve the production build locally
```
