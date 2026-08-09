# Global styles — `src/styles/global.css`

Copy-paste ready, byte-for-byte. This is the one global, render-blocking stylesheet imported by `Layout.astro`. Keep it focused on the shared theme tokens, document layout, footer, and the theme-toggle icon swap. Component-specific colors and interaction styles stay with their components.

**Two things live here on purpose — do not move them into scoped component `<style>` blocks:**

1. **The footer styles** (`.site-footer`, `.footer-line`). As scoped styles they can flash left-aligned for a frame before the centering attaches; the global render-blocking sheet styles them before first paint.
2. **The theme-toggle icon swap** (`.theme-toggle-sun` / `.theme-toggle-moon` and the `[data-theme='dark']` overrides). The visible icon is chosen by `[data-theme]` on `<html>`, an ancestor Astro's component scoping cannot target. The button's own appearance still belongs in `ThemeToggle.astro`.

Also keep `html { scrollbar-gutter: stable }`: it reserves scrollbar space so centered content does not shift sideways between pages that do and do not scroll.

```css
:root {
  --color-bg: #fafaf8;
  --color-text: #161616;
  --color-border: #e7e5df;
}

[data-theme="dark"] {
  --color-bg: #111111;
  --color-text: #f5f5f5;
  --color-border: #2a2a2a;
}

* {
  transition: background-color 0.25s ease, color 0.25s ease, border-color 0.25s ease;
}

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

main {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.site-footer {
  border-top: 1px solid;
  border-image: linear-gradient(
      to right,
      transparent,
      var(--color-border) 40%,
      var(--color-border) 60%,
      transparent
    ) 1;
  background: var(--color-bg);
}

.footer-line {
  margin: 0;
  padding: 1.25rem 1.5rem;
  text-align: center;
  color: #555;
  font-size: 0.9rem;
  cursor: default;
}

.theme-toggle-sun,
.theme-toggle-moon {
  grid-area: 1 / 1;
  width: 20px;
  height: 20px;
}

.theme-toggle-sun {
  display: none;
}

.theme-toggle-moon {
  display: block;
}

[data-theme='dark'] .theme-toggle-sun {
  display: block;
}

[data-theme='dark'] .theme-toggle-moon {
  display: none;
}
```

## Usage note

Use the three shared variables for page background, text, and borders. Keep colors that belong to one component in that component's scoped styles, with a `:global([data-theme='dark'])` override when needed. This keeps the global stylesheet small without weakening theme support.
