# Fonts

Drop self-hosted font files (`.woff2`) in this folder. They're served as-is at a
stable URL (`/fonts/your-font.woff2`), so reference them from
`src/styles/global.css`:

```css
@font-face {
  font-family: 'Your Font';
  src: url('/fonts/your-font.woff2') format('woff2');
  font-weight: 400;
  font-display: swap;
}

body {
  font-family: 'Your Font', system-ui, sans-serif;
}
```

**Why `public/fonts/` and not `src/assets/`?** Fonts need a stable, predictable
URL for `@font-face`. Files in `public/` are served untouched; files in
`src/assets/` get hashed filenames meant to be imported in code.
