# Global styles — `src/styles/global.css`

Copy-paste ready, byte-for-byte. This is the one global, render-blocking stylesheet (imported in `Layout.astro`). It holds: the design tokens (CSS variables, light on `:root` + dark on `[data-theme="dark"]`), the base `html`/`body`/`main` layout, the footer styles, and the theme-toggle icon swap.

**Two things live here on purpose — do not move them into scoped component `<style>` blocks:**

1. **The footer styles** (`.site-footer`, `.footer-line`). As a scoped style they flashed left-aligned for a frame on load before the centering attached; in this global (render-blocking) sheet the centered line is styled before first paint.
2. **The theme-toggle icon swap** (`#icon-sun` / `#icon-moon` + the `[data-theme='dark']` overrides). The visible icon is chosen by `[data-theme]` on `<html>` — an **ancestor** that Astro's component scoping can't target (it would scope `[data-theme='dark']` to require the component's marker, which `<html>` doesn't have). Scoped, the rule never matches and the icon freezes on the moon in dark mode. Global, it works.

Also note `html { scrollbar-gutter: stable }` — it reserves the scrollbar space on every page so centered content (the footer, the hero) doesn't shift sideways between a page that scrolls and one that doesn't.

```css
:root {
  /* backgrounds */
  --color-bg: #fafaf8;
  --color-bg-elevated: #ffffff;
  --color-bg-subtle: #f4f3ef;

  /* borders */
  --color-border: #e7e5df;

  /* text */
  --color-text: #161616;
  --color-text-muted: #6b6b6b;

  /* premium accent */
  --color-accent: #2d2d2d;
  --color-accent-hover: #111111;
  --color-on-accent: #ffffff;

  /* navigation */
  --color-nav-bg: rgba(250, 250, 248, 0.8);
  --color-nav-text: #4a4a4a;
  --color-nav-text-active: #111111;

  /* effects */
  --color-shadow: rgba(0, 0, 0, 0.04);
  --color-focus-ring: rgba(0, 0, 0, 0.12);

  --color-link: #222222;
  --color-link-hover: #000000;

  --transition-theme:
    background-color 0.25s ease,
    color 0.25s ease,
    border-color 0.25s ease;
}

[data-theme="dark"] {
  --color-bg: #111111;
  --color-bg-elevated: #171717;
  --color-bg-subtle: #1f1f1f;

  --color-border: #2a2a2a;

  --color-text: #f5f5f5;
  --color-text-muted: #9b9b9b;

  --color-accent: #f5f5f5;
  --color-accent-hover: #ffffff;
  --color-on-accent: #111111;

  --color-nav-bg: rgba(17, 17, 17, 0.8);
  --color-nav-text: #b0b0b0;
  --color-nav-text-active: #ffffff;

  --color-shadow: rgba(0, 0, 0, 0.35);
  --color-focus-ring: rgba(255, 255, 255, 0.12);

  --color-link: #ffffff;
  --color-link-hover: #d9d9d9;
}

* {
  transition: var(--transition-theme);
}

/* Always reserve space for the vertical scrollbar so navigating between a page
   that scrolls and one that doesn't never shifts centered content sideways. */
html {
  scrollbar-gutter: stable;
}

body {
  background: var(--color-bg);
  color: var(--color-text);
  margin: 0;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
}

/* <main> fills the height left below the header. Full-height pages (the centered
   Home hero) then size to exactly that space via flex:1 instead of a hard-coded
   `100vh - header` guess — which is what caused a scrollbar on Home only. Short
   pages (Work/Contact) just leave empty space below their content. */
main {
  flex: 1;
  display: flex;
  flex-direction: column;
}

/* Footer — kept here (global, render-blocking) rather than scoped in
   Footer.astro so the centered line is styled before first paint and never
   flashes left-aligned on load. */
.site-footer {
  border-top: 1px solid var(--color-border);
  background: var(--color-nav-bg);
}
.footer-line {
  margin: 0;
  padding: 1.25rem 1.5rem;
  text-align: center;
  color: #555; /* as grey/dim as possible, same in both themes */
  font-size: 0.9rem;
  cursor: default; /* keep the normal arrow on hover, not the text I-beam */
}

/* Theme-toggle icons (Header). Kept global because the visible icon is chosen by
   the [data-theme] attribute on <html> — an ancestor a component's scoped styles
   can't reach, which is why the icon previously stayed stuck on the moon. */
#icon-sun,
#icon-moon {
  grid-area: 1 / 1;
  width: 20px;
  height: 20px;
}
#icon-sun {
  display: none;
}
#icon-moon {
  display: block;
}
[data-theme='dark'] #icon-sun {
  display: block;
}
[data-theme='dark'] #icon-moon {
  display: none;
}
```

## Usage note

All page content should use the CSS variables (`var(--color-text)`, etc.) instead of hardcoded colors, so it automatically respects whichever theme is active.
