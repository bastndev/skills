# Packages — astro-test

## dependencies

| Package | Version | What it does in this project |
|---------|---------|------------------------------|
| `astro` | ^6.3.6 | Core framework — compiles `.astro` files, runs the dev server, and builds the static site output |
| `fixnow` | ^2.0.4 | A text spell-correction/normalization library. Listed as a dependency but **not imported anywhere** in the source code |

## devDependencies

None declared.

---

## Common needs check

- **Dark/light mode (theming)** — Not implemented. The site uses a single light palette defined via CSS custom properties in `:root`. There is no `prefers-color-scheme` media query or toggle mechanism.
- **State management** — Not needed. All data is a static array in the `.astro` frontmatter; there is no runtime state.
- **Forms & validation** — Not present. The "Add to cart" button is a plain `<button>` with no form, no handler, and no validation.
- **Routing/navigation** — Handled by Astro's file-based routing. Only one route (`/`) exists; in-page navigation uses anchor links.
- **Animations** — CSS `transition` on `.bento-card` (transform + box-shadow on hover). No JS animation library.
- **Internationalization (i18n)** — Not present. The page is English-only (`<html lang="en">`).
- **Data fetching/caching** — Not present. Product data is hardcoded in the frontmatter array.
- **Testing** — Not configured. No test runner, no test files.
- **Linting/formatting** — Not configured. No ESLint, no Prettier, no formatter script.
