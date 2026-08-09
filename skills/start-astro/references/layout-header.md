# Layout + Header + Footer (the shell)

Copy-paste ready, byte-for-byte. These files wrap every page. They import from the `@/` alias and pull the project name from `SITE` (`@/consts`) — **nothing here hardcodes the project name.** `Layout.astro` runs the no-flash theme script and Astro's `<ClientRouter />`; `Header.astro` is a three-zone bar (brand / centered nav / reusable theme toggle); `ThemeToggle.astro` owns the button, icons, and interaction; `Footer.astro` is one centered line.

> **Critical scoping note:** the footer CSS and the theme-toggle **icon visibility** CSS do **not** live in scoped component `<style>` blocks — they are in `global.css` (see `references/global-css.md`). Both depend on first-paint or `<html data-theme>` behavior. The toggle button's layout, colors, focus state, and script stay encapsulated in `ThemeToggle.astro`.

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
  /** Hide the Header + Footer for full-screen pages (e.g. 404). Defaults to false. */
  hideNavAndFooter?: boolean;
}

const { title, projectName = SITE.name, hideNavAndFooter = false } = Astro.props;
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
    {!hideNavAndFooter && <Header projectName={projectName} />}
    <main transition:animate="fade">
      <slot />
    </main>
    {!hideNavAndFooter && <Footer />}
  </body>
</html>
```

- The page composes its own `<title>` from `SITE.name`, so pages pass only `title="Home"` — no project name in any page.
- `transition:animate="fade"` on `<main>` gives the soft cross-fade between pages. `<Header />` and `<Footer />` sit outside `<main>`, so they don't refade on navigation.
- **`hideNavAndFooter`** lets a page render full-screen with no chrome — `404.astro` sets it so the typing animation owns the whole viewport. Both `<Header />` and `<Footer />` are guarded with `{!hideNavAndFooter && …}`; `<main>` (flex:1 in `global.css`) then fills the screen.
- **Why the no-flash script is inline and re-runs on `astro:after-swap`:** it must run synchronously before first paint (or dark-mode reloads flash light). With `<ClientRouter />`, each navigation swaps in server HTML that has no `data-theme`, so Astro strips the attribute and the page flips to light — `astro:after-swap` fires after the new DOM is in place but before paint, restoring the theme with zero flash. The listener is on `document` (persists across swaps), so registering once is enough.

## `src/components/Header.astro`

Nav is built from `ROUTES` (`@/consts`), the active link is computed with `stripTrailingSlash` (`@/lib/utils`), and the reusable toggle is imported from `ui/buttons/ThemeToggle.astro`.

```astro
---
import { ROUTES } from '@/consts';
import { stripTrailingSlash } from '@/lib/utils';
import ThemeToggle from '@/components/ui/buttons/ThemeToggle.astro';

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

    <ThemeToggle />
  </nav>
</header>

<style>
  .site-header {
    background: var(--color-bg);
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
    color: #4a4a4a;
    text-decoration: none;
  }
  :global([data-theme='dark']) .brand {
    color: #b0b0b0;
  }
  .brand:hover {
    color: #111111;
  }
  :global([data-theme='dark']) .brand:hover {
    color: #ffffff;
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
    color: #4a4a4a;
    text-decoration: none;
    font-size: 0.95rem;
    padding: 0.25rem 0;
  }
  :global([data-theme='dark']) .nav-link {
    color: #b0b0b0;
  }
  .nav-link.active,
  .nav-link:hover {
    color: #111111;
  }
  :global([data-theme='dark']) .nav-link.active,
  :global([data-theme='dark']) .nav-link:hover {
    color: #ffffff;
  }
</style>
```

- The brand mark reuses `public/favicon.svg` via a CSS `mask` painted with `currentColor`, so it tracks the theme. **Read-only — leave `public/favicon.svg`/`.ico` exactly as `bun create astro` ships them.** (The `mask` uses only the shape, so any fill/colors inside the SVG are ignored — it renders as a single-color silhouette.)
- `projectName` flows from `Layout` (default `SITE.name`) → `Header`. No hardcoded site name, no reliance on `Astro.site`.

## `src/components/ui/buttons/ThemeToggle.astro`

The theme control is a reusable UI primitive rather than header-owned markup. It uses Lucide's `Sun` and `Moon`, supports multiple instances on one page, and guards each button with `data-bound` so View Transitions never register duplicate listeners.

```astro
---
import { Sun, Moon } from '@lucide/astro';

// Day/night theme toggle. Drop in anywhere — multiple instances on the same
// page (e.g. desktop Header + mobile Main) coexist
// safely: the script binds via class selector and guards each button with
// `data-bound` so it never wires twice. The sun/moon swap depends on
// `[data-theme]` on <html>, an ancestor scoped styles can't reach — its
// visibility rules live in `global.css` keyed off `.theme-toggle-*` classes.
---

<button class="theme-toggle" type="button" aria-label="Toggle light and dark theme">
  <Sun class="theme-toggle-icon theme-toggle-sun" aria-hidden="true" />
  <Moon class="theme-toggle-icon theme-toggle-moon" aria-hidden="true" />
</button>

<style>
  .theme-toggle {
    justify-self: end;
    background: none;
    border: 1px solid var(--color-border);
    border-radius: 10px;
    width: 36px;
    height: 36px;
    display: grid;
    place-items: center;
    cursor: pointer;
    color: #4a4a4a;
  }
  :global([data-theme='dark']) .theme-toggle {
    color: #b0b0b0;
  }
  .theme-toggle:focus-visible {
    outline: 2px solid #111111;
    outline-offset: 2px;
  }
  :global([data-theme='dark']) .theme-toggle:focus-visible {
    outline-color: #ffffff;
  }
</style>

<script is:inline>
  function initThemeToggles() {
    document.querySelectorAll('.theme-toggle').forEach((btn) => {
      if (btn.dataset.bound) return;
      btn.dataset.bound = 'true';
      btn.addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-theme');
        const next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('theme', next);
      });
    });
  }
  initThemeToggles();
  document.addEventListener('astro:page-load', initThemeToggles);
</script>
```

- **Why a class selector:** reusable components cannot assume their button ID is unique. Binding every `.theme-toggle` allows the same primitive in a desktop header and a mobile surface.
- **Why `astro:page-load`:** `<ClientRouter />` swaps component DOM on navigation while bundled scripts run once. Rebinding on page load keeps the new button alive; `data-bound` prevents duplicate listeners.
- The sun/moon visibility rules remain global because they depend on `[data-theme]` on `<html>`. Everything else remains scoped to the component.

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
