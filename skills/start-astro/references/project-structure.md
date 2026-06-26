# Project structure, pages & root files

`{{PROJECT_NAME}}` is detected automatically from the current folder's name — the user already created and named it before invoking this skill (e.g. a folder called `TEST1` means `{{PROJECT_NAME}} = TEST1`, preserving its exact casing). Never ask for a name; never invent one. The skill writes files **into the current directory**, not a new sibling folder.

**The project name is name-free everywhere except three files** (`consts.ts`, `README.md`, `ARCHITECTURE.md`). The pages do **not** embed the name — they pass only a page title to `Layout`, which composes `<page> · <SITE.name>` itself. So `{{PROJECT_NAME}}` does **not** appear in any page below.

Final file tree after this skill runs (on top of the `minimal` template's `bun create astro` output):

```
{{PROJECT_NAME}}/                    ← the user's existing folder — never renamed
├── public/
│   ├── favicon.svg                 ← bun create astro default — DO NOT touch (also the header logo, read-only)
│   ├── favicon.ico                 ← bun create astro default — DO NOT touch / delete
│   └── fonts/
│       └── README.md               ← from this file
├── src/
│   ├── assets/
│   │   ├── images/.gitkeep         ← from this file
│   │   └── icons/
│   │       ├── social/*.svg        ← 7 brand icons (x, github, linkedin, …), from references/icons.md
│   │       └── theme/{sun,moon}.svg ← toggle icons, from references/icons.md
│   ├── components/
│   │   ├── ui/
│   │   │   ├── .gitkeep            ← from this file
│   │   │   └── buttons/
│   │   │       └── BackButton404.astro ← from this file (used by 404.astro)
│   │   ├── Header.astro            ← from references/layout-header.md
│   │   └── GXB.astro               ← from this file (ASCII art byte-for-byte + social row)
│   ├── sections/
│   │   └── Footer.astro            ← from references/layout-header.md
│   ├── layouts/
│   │   └── Layout.astro            ← from references/layout-header.md
│   ├── content/.gitkeep            ← from this file
│   ├── pages/
│   │   ├── index.astro             ← Home (this file)
│   │   ├── work/index.astro        ← Work → /work (this file)
│   │   ├── contact/index.astro     ← Contact → /contact (this file)
│   │   ├── 404.astro               ← typing animation + BackButton404, hides nav/footer (this file)
│   │   └── api/
│   │       └── hello.ts            ← from references/config-data-backend.md
│   ├── lib/utils.ts                ← from references/config-data-backend.md
│   ├── types/index.ts              ← from references/config-data-backend.md
│   ├── styles/global.css           ← from references/global-css.md
│   ├── consts.ts                   ← from references/config-data-backend.md
│   ├── content.config.ts           ← from references/config-data-backend.md
│   └── env.d.ts                    ← from references/config-data-backend.md
├── ARCHITECTURE.md                 ← from references/architecture.md
├── README.md                       ← from this file (overwrite the scaffold default)
├── .prettierignore                 ← from this file
├── .npmrc                          ← from this file (npm peer-deps fix; inert under bun)
├── astro.config.mjs                ← created by bun create astro, leave as-is
├── package.json                    ← created by bun create astro (+ bun add @lucide/astro)
└── tsconfig.json                   ← OVERWRITE — from references/config-data-backend.md
```

Each page is intentionally minimal: it wraps `Layout` and drops in the shared `GXB` hero with a one-line tagline. The ASCII art lives **only** in `GXB.astro`.

**Work and Contact each live in their own folder as `index.astro`** (`src/pages/work/index.astro` → `/work`, `src/pages/contact/index.astro` → `/contact`). Astro maps a folder's `index.astro` to the folder's path, so the URLs stay `/work` and `/contact` and `ROUTES` is unchanged — but each route now owns a folder it can grow into (sub-pages, co-located page-only parts) without a later move. Home and 404 stay flat at the `pages/` root.

## `src/components/GXB.astro` (ASCII art byte-for-byte — edit the social handles)

The hero shown on **every** page: the ASCII-art logo + a per-page tagline (the `text` prop) + a row of social links. The art lives here and nowhere else; the `<pre>` is `aria-hidden` because the art is decorative, so screen readers get the tagline. The social icons are imported with `?raw` and injected with `set:html` so they inherit `currentColor` and follow the theme. (To rebrand later, edit the `logo` constant — e.g. generate new art at [patorjk.com/software/taag](https://patorjk.com/software/taag/) with the "ANSI Shadow" font.)

**Write the ASCII art byte-for-byte.** The `socials` array ships with default handles — **edit each `href` to your own** (or trim the list). These links are *not* derived from `{{PROJECT_NAME}}`; this array is the single place a project's social links live.

```astro
---
import xIcon from "@/assets/icons/social/x.svg?raw";
import githubIcon from "@/assets/icons/social/github.svg?raw";
import linkedinIcon from "@/assets/icons/social/linkedin.svg?raw";
import instagramIcon from "@/assets/icons/social/instagram.svg?raw";
import youtubeIcon from "@/assets/icons/social/youtube.svg?raw";
import tiktokIcon from "@/assets/icons/social/tiktok.svg?raw";
import facebookIcon from "@/assets/icons/social/facebook.svg?raw";

interface Props {
  text: string;
}

const { text } = Astro.props;

// Social links shown under the hero tagline on every page. This array is the ONE
// place a project's socials live — edit each href to your own handle (or trim the
// list). Icons are imported ?raw and injected with set:html so they inherit
// currentColor and follow the theme.
const socials = [
  { href: "https://x.com/intent/follow?screen_name=gohitx", icon: xIcon, label: "X (Twitter)" },
  { href: "https://github.com/gohitx", icon: githubIcon, label: "GitHub" },
  { href: "https://linkedin.com/in/gohitx", icon: linkedinIcon, label: "LinkedIn" },
  { href: "https://instagram.com/gohitx", icon: instagramIcon, label: "Instagram" },
  { href: "https://www.youtube.com/@gohitx?sub_confirmation=1", icon: youtubeIcon, label: "YouTube" },
  { href: "https://tiktok.com/@gohitx", icon: tiktokIcon, label: "TikTok" },
  { href: "https://facebook.com/gohitx", icon: facebookIcon, label: "Facebook" },
];

// ASCII-art logo — the single source for the art used on every page. Edit or
// delete it here to change/remove it site-wide. The first line starts with a
// leading space; keep it, it aligns the glyphs.
const logo = ` ██████╗ ██╗  ██╗██████╗
██╔════╝ ╚██╗██╔╝██╔══██╗
██║  ███╗ ╚███╔╝ ██████╔╝
██║   ██║ ██╔██╗ ██╔══██╗
╚██████╔╝██╔╝ ██╗██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═════╝ `;
---

<section class="hero">
  <pre class="hero-logo" aria-hidden="true">{logo}</pre>
  <p class="hero-text">{text}</p>
  <div class="hero-socials">
    {
      socials.map((social) => (
        <a
          href={social.href}
          target="_blank"
          rel="noopener noreferrer"
          aria-label={social.label}
          set:html={social.icon}
        />
      ))
    }
  </div>
</section>

<style>
  .hero {
    flex: 1; /* fill <main> (see global.css) so the hero centers without a
                hard-coded height — that guess was overflowing into a scrollbar */
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    gap: 1.5rem;
    padding: 2rem 1.5rem;
  }
  .hero-logo {
    margin: 0;
    max-width: 100%;
    color: var(--color-accent);
    font-family: ui-monospace, 'Cascadia Code', 'JetBrains Mono', 'Fira Code', Menlo, Consolas, monospace;
    font-size: clamp(0.45rem, 2.2vw, 0.95rem);
    line-height: 1.1;
    white-space: pre;
  }
  .hero-text {
    margin: 0;
    color: var(--color-text-muted);
    font-size: 1.05rem;
  }
  .hero-socials {
    display: flex;
    gap: 2rem;
    margin-top: 0.5rem;
    align-items: center;
    justify-content: center;
  }
  .hero-socials a {
    color: var(--color-text-muted);
    transition:
      color 0.2s ease,
      transform 0.2s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 24px;
  }
  .hero-socials a:hover {
    color: var(--color-text);
    transform: translateY(-2px);
  }
  .hero-socials a :global(svg) {
    width: 100%;
    height: 100%;
  }
</style>
```

## `src/pages/index.astro` (Home)

```astro
---
import Layout from '@/layouts/Layout.astro';
import GXB from '@/components/GXB.astro';
---

<Layout title="Home">
  <GXB text="Welcome — the starting point of your new Astro project." />
</Layout>
```

## `src/pages/work/index.astro`

```astro
---
import Layout from '@/layouts/Layout.astro';
import GXB from '@/components/GXB.astro';
---

<Layout title="Work">
  <GXB text="Work — a place to showcase your projects." />
</Layout>
```

## `src/pages/contact/index.astro`

```astro
---
import Layout from '@/layouts/Layout.astro';
import GXB from '@/components/GXB.astro';
---

<Layout title="Contact">
  <GXB text="Contact — get in touch or drop your details here." />
</Layout>
```

## `src/pages/404.astro`

A full-screen not-found page: a monospace **typing animation** ("404, page not found.") with a blinking cursor, plus a themed back button. It passes `hideNavAndFooter={true}` so the Header and Footer are hidden (see `references/layout-header.md`), and links home from the `ROUTES` registry (never hard-code `/`). The title stays **name-free** (`title="404"`) so `Layout` composes `404 · <SITE.name>`.

**The message is server-rendered** inside `.typing-text`, so it's present for crawlers and with JavaScript disabled; the script clears and re-types it only as a progressive enhancement, and skips the animation entirely under `prefers-reduced-motion` (leaving the static text). The cursor is `aria-hidden` (decorative), and because the text is real DOM, screen readers announce it.

```astro
---
import Layout from '@/layouts/Layout.astro';
import BackButton404 from '@/components/ui/buttons/BackButton404.astro';
import { ROUTES } from '@/consts';

// Link home from the routes registry — never hard-code "/" here.
const home = ROUTES[0];
---

<Layout title="404" hideNavAndFooter={true}>
  <section class="not-found">
    <p class="typed"><span class="typing-text">404, page not found.</span><span class="cursor" aria-hidden="true"></span></p>
    <BackButton404 href={home.href} text={home.label} />
  </section>
</Layout>

<style>
  /* Full-screen centered: <main> is flex:1 (global.css) and the header/footer are
     hidden on this page, so .not-found fills the viewport. */
  .not-found {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    gap: 1.5rem;
    padding: 2rem 1.5rem;
  }
  .typed {
    margin: 0;
    font-family: ui-monospace, 'Cascadia Code', 'JetBrains Mono', 'Fira Code', Menlo, Consolas, monospace;
    font-size: 1.25rem;
    color: var(--color-text);
  }
  /* Blinking terminal cursor — a deliberate orange accent kept the same in both
     themes (like the footer line), not a theme variable. */
  .cursor {
    display: inline-block;
    width: 10px;
    height: 1.15em;
    margin-left: 2px;
    background-color: #f84f00;
    vertical-align: text-bottom;
    animation: blink 0.7s infinite;
  }
  @keyframes blink {
    0%, 49% { opacity: 1; }
    50%, 100% { opacity: 0; }
  }
</style>

<script>
  const SPEED_MS = 100;

  function initTyping() {
    const el = document.querySelector('.typing-text');
    if (!el || el.dataset.typed) return; // guard the initial double-run + later re-runs
    const full = el.textContent ?? ''; // message is server-rendered (so it's there with JS off)
    el.dataset.typed = 'true';

    // Honour reduced-motion: keep the already-visible text, skip the animation.
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    el.textContent = '';
    let i = 0;
    (function type() {
      if (i < full.length) {
        el.textContent += full.charAt(i++);
        setTimeout(type, SPEED_MS);
      }
    })();
  }

  // Run on first load and after every View-Transition navigation, mirroring the
  // theme-toggle pattern in Header.astro.
  initTyping();
  document.addEventListener('astro:page-load', initTyping);
</script>
```

## `src/components/ui/buttons/BackButton404.astro`

The themed "← Home" button used by `404.astro` — the first real `ui/` primitive, living under `ui/buttons/`. Accent-filled, rounded, lifts on hover. Reusable for any "go back" link (`href` + `text` props).

```astro
---
interface Props {
  href: string;
  text: string;
}

const { href, text } = Astro.props;
---

<a href={href} class="back-btn">
  ← {text}
</a>

<style>
  .back-btn {
    display: inline-block;
    margin-top: 1.5rem;
    padding: 0.5rem 1.25rem;
    font-size: 0.95rem;
    color: var(--color-on-accent);
    background-color: var(--color-accent);
    text-decoration: none;
    border-radius: 15px;
    transition:
      background-color 0.2s ease,
      transform 0.2s ease;
    font-family: inherit;
  }
  .back-btn:hover {
    background-color: var(--color-accent-hover);
    transform: translateY(-2px);
  }
</style>
```

## `README.md` (overwrite the scaffold default — substitute `{{PROJECT_NAME}}` in the title)

````markdown
# {{PROJECT_NAME}}

A simple but scalable Astro base — ready to grow from a portfolio to a full app.
Pure Astro (no UI framework), a zero-dependency light/dark theme, native View
Transitions, Content Collections wired up, and an open backend door.

## Features

- ⚡ **Astro 7**, static-first (SSG) — add an adapter only when you actually need a server.
- 🌗 **Light/dark theme** — CSS variables + a no-flash inline script that survives View Transitions. Zero runtime deps.
- 🔀 **View Transitions** — SPA-style fades between pages.
- 🧭 **Connected routes** — the nav and the 404 page both read one `ROUTES` registry in `src/consts.ts`.
- 🎨 **Icons** — [`@lucide/astro`](https://lucide.dev) for line icons; custom/brand SVGs in `src/assets/icons/`.
- 📦 **Content Collections** ready (`src/content.config.ts`).
- 🔎 **SEO ready** — canonical + Open Graph/Twitter tags composed from one `SITE` config (per-page `description`/`image` overrides).
- ♿ **Accessible** — skip-to-content link, `aria-current`, visible focus rings, and `prefers-reduced-motion` support.
- 🏷️ **`@/` path alias** → `src/` (no `../../` chains).
- 🧱 **Scalable structure** — `components/`, `sections/`, `lib/`, `types/`, `content/`, `pages/api/`.

See **[ARCHITECTURE.md](./ARCHITECTURE.md)** for the full layout, conventions, and recipes.

## Project structure

```text
src/
├── assets/icons/      # custom + brand SVGs (social/, theme/)
├── components/        # reusable UI (Header, GXB, ui/)
├── sections/          # page-level blocks (Footer, …)
├── layouts/           # Layout.astro — the HTML shell every page wraps in
├── content/           # Content Collection entries
├── pages/             # file-based routes (+ api/, 404.astro)
├── lib/               # framework-agnostic helpers
├── types/             # shared TypeScript types
├── styles/            # global.css — design tokens (light + dark)
├── consts.ts          # SITE config + ROUTES registry
└── content.config.ts  # Content Collection schemas
```

## Commands

All commands are run from the project root:

| Command           | Action                                       |
| :---------------- | :------------------------------------------- |
| `bun install`     | Install dependencies                         |
| `bun run dev`     | Start the dev server at `localhost:4321`     |
| `bun run build`   | Build the production site to `./dist/`       |
| `bun run preview` | Preview the production build locally         |

> Using **npm** (or pnpm/yarn)? Swap `bun` for your manager: `npm install`, `npm run dev`, `npm run build`.

## Getting started

1. Set your name, description, and URL in `src/consts.ts` (`SITE`).
2. Add or rename routes in `ROUTES` (same file) — the nav and the 404 page follow automatically.
3. Tweak colors in `src/styles/global.css` (CSS variables, light + dark).
4. Build pages in `src/pages/`, page sections in `src/sections/`, helpers in `src/lib/`.

## Learn more

Astro documentation: <https://docs.astro.build>
````

## `.prettierignore` (project root)

Skips generated output and keeps `public/` (incl. the default favicon) untouched by formatting.

```
# Build output & generated files
dist/
.astro/

# Lockfiles
bun.lock
package-lock.json

# Static assets — keep public/ (incl. the default Astro favicon) untouched
public/
```

## `.npmrc` (project root)

Makes the project install with **npm** as cleanly as with bun. `@lucide/astro` hasn't yet widened its `peerDependencies` to include Astro 7, so npm — which, unlike bun, treats a peer-range mismatch as a hard `ERESOLVE` error — would otherwise refuse `npm install`, both for the initial setup *and* for anyone who later clones the repo. `legacy-peer-deps=true` restores the install. It's inert under bun, so it ships unconditionally. Safe to delete once `@lucide/astro` lists Astro 7 as a peer.

```
# @lucide/astro hasn't widened its peer range to Astro 7 yet, so npm (unlike bun)
# hard-errors on install. This keeps `npm install` working — for setup and for
# anyone who clones the project. Safe to remove once @lucide/astro lists Astro 7.
legacy-peer-deps=true
```

## `public/fonts/README.md`

```markdown
# Fonts

Drop self-hosted font files (`.woff2`) in this folder. They're served as-is at a
stable URL (`/fonts/your-font.woff2`), so reference them from
`src/styles/global.css`:

\```css
@font-face {
  font-family: 'Your Font';
  src: url('/fonts/your-font.woff2') format('woff2');
  font-weight: 400;
  font-display: swap;
}

body {
  font-family: 'Your Font', system-ui, sans-serif;
}
\```

**Why `public/fonts/` and not `src/assets/`?** Fonts need a stable, predictable
URL for `@font-face`. Files in `public/` are served untouched; files in
`src/assets/` get hashed filenames meant to be imported in code.
```

## `.gitkeep` placeholders (keep intentional-but-empty folders in version control)

Write a `.gitkeep` to each of these three folders. Content is a single comment line:

- `src/assets/images/.gitkeep`
  ```
  # Imported, optimized images live here. Purpose documented in ARCHITECTURE.md.
  ```
- `src/components/ui/.gitkeep`
  ```
  # Small reusable UI primitives (Button, Badge, Card…). See ARCHITECTURE.md.
  ```
- `src/content/.gitkeep`
  ```
  # Content Collection entries live here, one PLURAL folder per collection
  # (e.g. content/projects/, content/blog/). Schemas are in src/content.config.ts.
  ```

## Adding more pages later

1. Create `src/pages/{name}/index.astro` (a folder per route, mirroring Work/Contact) — import `Layout` + `GXB`, then `<GXB text="…" />`. Pass only a page title: `<Layout title="{Name}">`. (A flat `src/pages/{name}.astro` resolves to the same `/{name}` URL if you don't need the folder yet.)
2. Add `{ href: '/{name}', label: '{Name}' }` to the `ROUTES` array in `src/consts.ts`.

The nav (Header), the 404 link, the title, and the theme all follow automatically — no other file changes.
