# Layout + Header

Copy-paste ready. `Layout.astro` wraps every page, imports the theme CSS, the no-flash script, and Astro's native `<ClientRouter />` for smooth fade transitions between pages. `Header.astro` holds the nav (Home/Work/About/Contact) + the theme toggle button.

## `src/layouts/Layout.astro`

```astro
---
import { ClientRouter } from 'astro:transitions';
import Header from '../components/Header.astro';
import '../styles/theme.css';

interface Props {
  title: string;
}

const { title } = Astro.props;
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
        const saved = localStorage.getItem('theme');
        const theme = saved || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
        document.documentElement.setAttribute('data-theme', theme);
      })();
    </script>
  </head>
  <body>
    <Header />
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
const navItems = [
  { href: '/', label: 'Home' },
  { href: '/work', label: 'Work' },
  { href: '/about', label: 'About' },
  { href: '/contact', label: 'Contact' },
];

const currentPath = Astro.url.pathname;
---

<header class="site-header">
  <nav class="nav">
    <a href="/" class="brand">{Astro.site?.hostname ?? 'Astro Site'}</a>

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
    border-bottom: 1px solid var(--color-border);
  }
  .nav {
    max-width: 960px;
    margin: 0 auto;
    padding: 1rem 1.5rem;
    display: flex;
    align-items: center;
    gap: 1.5rem;
  }
  .brand {
    font-weight: 700;
    color: var(--color-nav-text);
    text-decoration: none;
    margin-right: auto;
  }
  .nav-links {
    display: flex;
    gap: 1.25rem;
    list-style: none;
    margin: 0;
    padding: 0;
  }
  .nav-link {
    color: var(--color-nav-text);
    text-decoration: none;
    font-size: 0.95rem;
    padding: 0.25rem 0;
    border-bottom: 2px solid transparent;
  }
  .nav-link.active {
    color: var(--color-nav-text-active);
    border-bottom-color: var(--color-nav-text-active);
  }
  .nav-link:hover {
    color: var(--color-nav-text-active);
  }

  #theme-toggle {
    background: none;
    border: 1px solid var(--color-border);
    border-radius: 999px;
    width: 36px;
    height: 36px;
    display: grid;
    place-items: center;
    cursor: pointer;
    color: var(--color-nav-text);
    flex-shrink: 0;
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

- `currentPath === item.href` highlights the active section in the nav. Works correctly with View Transitions because `Astro.url.pathname` is re-evaluated server-side on every navigation (Astro re-renders the component, it isn't a client-side SPA route guess).
- `class:list` is Astro's built-in conditional-class helper — no extra package needed.
- If the user later wants the brand name to be a literal site name instead of `Astro.site?.hostname`, just hardcode the string — `Astro.site` is `undefined` unless `site` is set in `astro.config.mjs`, so confirm with the user or default to a plain string like the project name to avoid an empty brand link.
