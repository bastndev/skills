# Layout + Header

Copy-paste ready. `Layout.astro` wraps every page, imports the global CSS, runs the no-flash theme script (which **re-applies on `astro:after-swap`** so the theme survives navigation), and pulls in Astro's native `<ClientRouter />` for smooth fade transitions between pages. `Header.astro` is a three-zone bar: the logo + project name on the left, the centered nav (Home/Work/Contact), and the theme toggle on the right.

## `src/layouts/Layout.astro`

```astro
---
import { ClientRouter } from 'astro:transitions';
import Header from '../components/Header.astro';
import '../styles/global.css';

interface Props {
  title: string;
  projectName: string;
}

const { title, projectName } = Astro.props;
---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title}</title>
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
  </body>
</html>
```

> `transition:animate="fade"` on `<main>` is what gives the soft cross-fade when navigating between pages. `<Header />` sits outside `<main>` and is unaffected by transitions, so it doesn't blink/refade on every navigation.

## `src/components/Header.astro`

```astro
---
interface Props {
  projectName: string;
}

const { projectName } = Astro.props;

const navItems = [
  { href: '/', label: 'Home' },
  { href: '/work', label: 'Work' },
  { href: '/contact', label: 'Contact' },
];

// Normalise trailing slashes so the active link matches in both `bun run dev`
// (path is `/work`) and the static build/preview (path is `/work/`).
const stripSlash = (p: string) => (p !== '/' && p.endsWith('/') ? p.slice(0, -1) : p);
const currentPath = stripSlash(Astro.url.pathname);
---

<header class="site-header">
  <nav class="nav">
    <a href="/" class="brand">
      <span class="brand-logo" aria-hidden="true"></span>
      <span class="brand-name">{projectName}</span>
    </a>

    <ul class="nav-links">
      {navItems.map((item) => (
        <li>
          <a
            href={item.href}
            class:list={['nav-link', { active: currentPath === item.href }]}
          >
            {item.label}
          </a>
        </li>
      ))}
    </ul>

    <button id="theme-toggle" type="button" aria-label="Toggle light and dark theme">
      <svg id="icon-sun" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="4" />
        <path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41" />
      </svg>
      <svg id="icon-moon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" />
      </svg>
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
  #icon-sun, #icon-moon { grid-area: 1 / 1; }
  #icon-sun { display: none; }
  #icon-moon { display: block; }
  [data-theme='dark'] #icon-sun { display: block; }
  [data-theme='dark'] #icon-moon { display: none; }
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

## Notes

- `currentPath === item.href` highlights the active section in the nav. `Astro.url.pathname` is re-evaluated server-side on every navigation (Astro re-renders the component, it isn't a client-side SPA route guess), and `stripSlash` normalises trailing slashes so the match holds in both `dev` (`/work`) and the static build (`/work/`) — otherwise non-home links never highlight in production.
- `class:list` is Astro's built-in conditional-class helper — no extra package needed.
- The brand mark reuses `public/favicon.svg` via a CSS `mask`, painted with `currentColor`, so it tracks the in-app theme toggle. **This is read-only — the scaffold must leave `public/favicon.svg` and `public/favicon.ico` exactly as `bun create astro` ships them (the Astro default), and must not delete the `.ico`.** If the user later wants to rebrand, they can swap `public/favicon.svg` themselves and both the favicon and the header logo update at once. (Because `mask` uses only the shape, any fill/colors inside the SVG are ignored — it renders as a single-color silhouette.)
- `projectName` flows from `Layout.astro`'s `title`/`projectName` props down into `Header.astro` — both ultimately come from `{{PROJECT_NAME}}` (detected automatically from the current folder's name; see `project-structure.md`). No hardcoded site name and no reliance on `Astro.site` (which is `undefined` unless `site` is explicitly set in `astro.config.mjs`).
