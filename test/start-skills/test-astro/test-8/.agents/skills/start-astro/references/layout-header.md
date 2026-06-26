# Layout + Header + Footer (the shell)

Copy-paste ready, byte-for-byte. These three wrap every page. They import from the `@/` alias and pull the project name from `SITE` (`@/consts`) — **nothing here hardcodes the project name.** `Layout.astro` runs the no-flash theme script and Astro's `<ClientRouter />`; `Header.astro` is a three-zone bar (brand / centered nav / theme toggle); `Footer.astro` is one centered line.

> **Critical scoping note:** the footer's CSS and the theme-toggle icon CSS do **not** live in these components' scoped `<style>` blocks — they're in `global.css` (see `references/global-css.md`). Both depend on `[data-theme]` on `<html>`, an ancestor that a component's scoped styles can't target. Scope them and the toggle icon freezes on the moon and the footer flashes left-aligned on load.

## `src/layouts/Layout.astro`

```astro
---
import { ClientRouter } from 'astro:transitions';
import Header from '@/components/Header.astro';
import Footer from '@/sections/Footer.astro';
import { SITE } from '@/consts';
import '@/styles/global.css';

interface Props {
  /** Page name, e.g. "Home". Composed into `<name> · <SITE.name>`. Omit for the bare site name. */
  title?: string;
  /** Brand text in the header. Defaults to the site name from consts.ts. */
  projectName?: string;
}

const { title, projectName = SITE.name } = Astro.props;
const fullTitle = title ? `${title} · ${SITE.name}` : SITE.name;
---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content={SITE.description} />
    <title>{fullTitle}</title>
    <ClientRouter />
    <script is:inline>
      (function () {
        function applyTheme() {
          const saved = localStorage.getItem('theme');
          const theme = saved || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
          document.documentElement.setAttribute('data-theme', theme);
        }
        applyTheme();
        // Re-apply after every View Transition swap (fires before paint).
        // Without this, navigating between pages resets <html data-theme> to
        // the server HTML (which has no theme) and the site flips back to light.
        document.addEventListener('astro:after-swap', applyTheme);
      })();
    </script>
  </head>
  <body>
    <Header projectName={projectName} />
    <main transition:animate="fade">
      <slot />
    </main>
    <Footer />
  </body>
</html>
```

- The page composes its own `<title>` from `SITE.name`, so pages pass only `title="Home"` — no project name in any page.
- `transition:animate="fade"` on `<main>` gives the soft cross-fade between pages. `<Header />` and `<Footer />` sit outside `<main>`, so they don't refade on navigation.
- **Why the no-flash script is inline and re-runs on `astro:after-swap`:** it must run synchronously before first paint (or dark-mode reloads flash light). With `<ClientRouter />`, each navigation swaps in server HTML that has no `data-theme`, so Astro strips the attribute and the page flips to light — `astro:after-swap` fires after the new DOM is in place but before paint, restoring the theme with zero flash. The listener is on `document` (persists across swaps), so registering once is enough.

## `src/components/Header.astro`

Nav is built from `ROUTES` (`@/consts`); the active link is computed with `stripTrailingSlash` (`@/lib/utils`); the toggle uses the imported sun/moon SVG components.

```astro
---
import { ROUTES } from '@/consts';
import { stripTrailingSlash } from '@/lib/utils';
import Sun from '@/assets/icons/theme/sun.svg';
import Moon from '@/assets/icons/theme/moon.svg';

interface Props {
  projectName: string;
}

const { projectName } = Astro.props;

// Nav is built from the shared ROUTES registry (src/consts.ts). Active-link state
// compares the current path to each route; trailing slashes are normalised so it
// matches in both `bun run dev` (`/work`) and the static build/preview (`/work/`).
const currentPath = stripTrailingSlash(Astro.url.pathname);
---

<header class="site-header">
  <nav class="nav">
    <a href="/" class="brand">
      <span class="brand-logo" aria-hidden="true"></span>
      <span class="brand-name">{projectName}</span>
    </a>

    <ul class="nav-links">
      {ROUTES.map((route) => (
        <li>
          <a
            href={route.href}
            class:list={['nav-link', { active: currentPath === route.href }]}
          >
            {route.label}
          </a>
        </li>
      ))}
    </ul>

    <button id="theme-toggle" type="button" aria-label="Toggle light and dark theme">
      <Sun id="icon-sun" aria-hidden="true" />
      <Moon id="icon-moon" aria-hidden="true" />
    </button>
  </nav>
</header>

<style>
  .site-header {
    background: var(--color-nav-bg);
  }
  .nav {
    max-width: 1200px;
    margin: 0 auto;
    padding: 1rem 1.5rem;
    /* three zones: brand (left) · nav (true-centered) · toggle (right).
       1fr/auto/1fr keeps the nav centered on the page no matter how wide the
       brand or toggle are. */
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    align-items: center;
    gap: 1.5rem;
  }
  .brand {
    justify-self: start;
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    font-weight: 700;
    color: var(--color-nav-text);
    text-decoration: none;
  }
  .brand:hover {
    color: var(--color-nav-text-active);
  }
  /* Reuses /public/favicon.svg (read-only) as a mask, then paints it with the
     brand's currentColor — so the logo follows the in-app theme toggle. This
     only *references* the file; the scaffold never modifies or replaces it. */
  .brand-logo {
    width: 26px;
    height: 26px;
    flex-shrink: 0;
    background-color: currentColor;
    -webkit-mask: url(/favicon.svg) center / contain no-repeat;
    mask: url(/favicon.svg) center / contain no-repeat;
  }
  .nav-links {
    justify-self: center;
    display: flex;
    gap: 1.5rem;
    list-style: none;
    margin: 0;
    padding: 0;
  }
  /* No underlines/lines: links sit muted-gray and brighten to white (or near-black
     in light mode) when active or hovered. The active state is colour-only. */
  .nav-link {
    color: var(--color-nav-text);
    text-decoration: none;
    font-size: 0.95rem;
    padding: 0.25rem 0;
  }
  .nav-link.active,
  .nav-link:hover {
    color: var(--color-nav-text-active);
  }

  #theme-toggle {
    justify-self: end;
    background: none;
    border: 1px solid var(--color-border);
    border-radius: 10px; /* square with generously rounded corners (not a circle) */
    width: 36px;
    height: 36px;
    display: grid;
    place-items: center;
    cursor: pointer;
    color: var(--color-nav-text);
  }
  #theme-toggle:focus-visible {
    outline: 2px solid var(--color-focus-ring);
    outline-offset: 2px;
  }
  /* The sun/moon swap (display chosen by [data-theme] on <html>) lives in
     global.css — a scoped style can't target the <html> ancestor, which is why
     the icon previously stayed stuck on the moon in dark mode. */
</style>

<script is:inline>
  function initThemeToggle() {
    const btn = document.getElementById('theme-toggle');
    if (!btn || btn.dataset.bound) return;
    btn.dataset.bound = 'true';

    btn.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
    });
  }

  initThemeToggle();
  document.addEventListener('astro:page-load', initThemeToggle);
</script>
```

- **Why `astro:page-load`:** `<ClientRouter />` swaps the DOM (including `#theme-toggle`) on each navigation, but bundled module scripts only run once. Without re-binding the click handler on `astro:page-load`, the button goes dead after the first navigation. The `data-bound` guard avoids double-binding on the initial load (where both `initThemeToggle()` and `astro:page-load` fire).
- The brand mark reuses `public/favicon.svg` via a CSS `mask` painted with `currentColor`, so it tracks the theme. **Read-only — leave `public/favicon.svg`/`.ico` exactly as `bun create astro` ships them.** (The `mask` uses only the shape, so any fill/colors inside the SVG are ignored — it renders as a single-color silhouette.)
- `projectName` flows from `Layout` (default `SITE.name`) → `Header`. No hardcoded site name, no reliance on `Astro.site`.

## `src/sections/Footer.astro`

One centered line, `{SITE.name} © {year}`. Its styles live in `global.css` (see the critical scoping note above).

```astro
---
// Minimal site footer: the project name + the current year. Shown on every page
// via Layout.astro. The name comes from SITE so it follows the single source of
// truth (rename once in consts.ts). Its styles live in global.css (a
// render-blocking, global stylesheet) instead of a scoped <style> here — so the
// centered line is applied before first paint and never flashes left-aligned.
import { SITE } from '@/consts';

const year = new Date().getFullYear();
---

<footer class="site-footer">
  <p class="footer-line">{SITE.name} © {year}</p>
</footer>
```
