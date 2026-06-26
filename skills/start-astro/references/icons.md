# Icons — Lucide + custom brand/theme SVGs

Two sources, no React anywhere:

- **Lucide** (`@lucide/astro`) for standard line icons. Install with `bun add @lucide/astro` (the only runtime dep this skill adds). Use directly: `import { Search } from '@lucide/astro'` → `<Search />`.
- **Custom icons** as raw `.svg` files under `src/assets/icons/`, imported either as **components** (Astro 7 renders `*.svg` imports inline) or as **raw strings** (`?raw`) injected with `set:html`. Brand logos live here because **Lucide ships no brand marks**.

Write the files below exactly. Filenames are lowercase `kebab-case`. Every icon is one consistent **outline (stroke) style** on a 24×24 grid using `currentColor`, so CSS controls color (they follow the theme) and the set reads as one family.

**The social set is exactly 7 icons** — `x`, `github`, `linkedin`, `instagram`, `youtube`, `tiktok`, `facebook`. It was deliberately trimmed and unified: earlier mismatched brand marks (a *solid-fill* GitHub, plus Discord, Threads, SoundCloud, and a separate `github-thin`) were removed so the row reads as one consistent outline family, and `twitter` is now `x`.

**Optical balancing via `viewBox`.** Each glyph fills its 24×24 box by a different amount, so at the same pixel size some look bigger than others. Each icon's `viewBox` is nudged (zoomed in or out) to equalize the *apparent* size — the row looks uniform with no per-icon CSS. Keep these exact values:

| icon      | viewBox        | why                                         |
| :-------- | :------------- | :------------------------------------------ |
| x         | `-1 -1 26 26`  | zoom out — the X reaches into the corners   |
| github    | `0 0 24 24`    | standard                                    |
| linkedin  | `1 1 22 22`    | slight zoom in                              |
| instagram | `2 2 20 20`    | zoom in — the rounded square is small       |
| youtube   | `1 1 22 22`    | slight zoom in                              |
| tiktok    | `1 1 22 22`    | slight zoom in                              |
| facebook  | `0 0 24 24`    | standard                                    |

Usage — two ways:

```astro
---
// As a component (single icon, e.g. the theme toggle):
import Sun from '@/assets/icons/theme/sun.svg';
// As a raw string for set:html (the hero social row — see GXB.astro):
import xIcon from '@/assets/icons/social/x.svg?raw';
import { Search } from '@lucide/astro';
---
<Sun class="icon" />
<a href="https://x.com/yourusername" set:html={xIcon} />
<Search class="icon" />
```

> The theme toggle (`Header.astro`) imports `theme/sun.svg` + `theme/moon.svg` and renders them as `<Sun id="icon-sun" aria-hidden="true" />` / `<Moon id="icon-moon" aria-hidden="true" />`; their show/hide swap is in `global.css` (see `references/global-css.md`). The hero (`GXB.astro`) imports the 7 social icons with `?raw` and injects them with `set:html` (see `references/project-structure.md`).

---

## `src/assets/icons/theme/sun.svg`

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path stroke="none" d="M0 0h24v24H0z" fill="none" />
  <path d="M12 12m-4 0a4 4 0 1 0 8 0a4 4 0 1 0 -8 0" />
  <path d="M3 12h1m8 -9v1m8 8h1m-9 8v1m-6.4 -15.4l.7 .7m12.1 -.7l-.7 .7m0 11.4l.7 .7m-12.1 -.7l-.7 .7" />
</svg>
```

## `src/assets/icons/theme/moon.svg`

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path stroke="none" d="M0 0h24v24H0z" fill="none" />
  <path d="M12 3c.132 0 .263 0 .393 0a7.5 7.5 0 0 0 7.92 12.446a9 9 0 1 1 -8.313 -12.454z" />
</svg>
```

---

## `src/assets/icons/social/x.svg`

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="-1 -1 26 26" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path stroke="none" d="M0 0h24v24H0z" fill="none" />
  <path d="M4 4l11.733 16h4.267l-11.733 -16z" />
  <path d="M4 20l6.768 -6.768m2.46 -2.46l6.772 -6.772" />
</svg>
```

## `src/assets/icons/social/github.svg`

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path stroke="none" d="M0 0h24v24H0z" fill="none" />
  <path d="M9 19c-4.3 1.4 -4.3 -2.5 -6 -3m12 5v-3.5c0 -1 .1 -1.4 -.5 -2c2.8 -.3 5.5 -1.4 5.5 -6a4.6 4.6 0 0 0 -1.3 -3.2a4.2 4.2 0 0 0 -.1 -3.2s-1.1 -.3 -3.5 1.3a12.3 12.3 0 0 0 -6.2 0c-2.4 -1.6 -3.5 -1.3 -3.5 -1.3a4.2 4.2 0 0 0 -.1 3.2a4.6 4.6 0 0 0 -1.3 3.2c0 4.6 2.7 5.7 5.5 6c-.6 .6 -.6 1.2 -.5 2v3.5" />
</svg>
```

## `src/assets/icons/social/linkedin.svg`

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="1 1 22 22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path stroke="none" d="M0 0h24v24H0z" fill="none" />
  <path d="M8 11v5" />
  <path d="M8 8v.01" />
  <path d="M12 16v-5" />
  <path d="M16 16v-3a2 2 0 1 0 -4 0" />
  <path d="M3 7a4 4 0 0 1 4 -4h10a4 4 0 0 1 4 4v10a4 4 0 0 1 -4 4h-10a4 4 0 0 1 -4 -4z" />
</svg>
```

## `src/assets/icons/social/instagram.svg`

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="2 2 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path stroke="none" d="M0 0h24v24H0z" fill="none" />
  <path d="M4 8a4 4 0 0 1 4 -4h8a4 4 0 0 1 4 4v8a4 4 0 0 1 -4 4h-8a4 4 0 0 1 -4 -4z" />
  <path d="M9 12a3 3 0 1 0 6 0a3 3 0 0 0 -6 0" />
  <path d="M16.5 7.5v.01" />
</svg>
```

## `src/assets/icons/social/youtube.svg`

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="1 1 22 22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path stroke="none" d="M0 0h24v24H0z" fill="none" />
  <path d="M2 8a4 4 0 0 1 4 -4h12a4 4 0 0 1 4 4v8a4 4 0 0 1 -4 4h-12a4 4 0 0 1 -4 -4v-8z" />
  <path d="M10 9l5 3l-5 3z" />
</svg>
```

## `src/assets/icons/social/tiktok.svg`

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="1 1 22 22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path stroke="none" d="M0 0h24v24H0z" fill="none" />
  <path d="M21 7.917v4.034a9.948 9.948 0 0 1 -5 -1.951v4.5a6.5 6.5 0 1 1 -8 -6.326v4.326a2.5 2.5 0 1 0 4 2v-11.5h4.083a6.005 6.005 0 0 0 4.917 4.917z" />
</svg>
```

## `src/assets/icons/social/facebook.svg`

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path stroke="none" d="M0 0h24v24H0z" fill="none" />
  <path d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3" />
</svg>
```
