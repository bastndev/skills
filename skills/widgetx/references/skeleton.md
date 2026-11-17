# 🦴 skeleton

Loading placeholders. A skeleton tells the user "content is coming, and it
will go here" without a spinner and without the page jumping when it arrives.

## Style menu

Ask it as a select question (see "How to ask" in `SKILL.md`):

* Header: `style`
* Question: `Which skeleton style?`
* Options, in this order:

| Label                | Description                                           |
| -------------------- | ----------------------------------------------------- |
| `text`               | a light sweeps across the text itself ("Installing…") |
| `sync`               | gray blocks, one shared light crossing all of them    |
| `pulse`              | gray blocks fading in and out together                |
| `wave (recommended)` | gray blocks fading one after another, top to bottom   |

Keep `(recommended)` in the `wave` label exactly as written; it is the most
used style. It is a hint only: never pick it on the user's behalf.

Text fallback — only when no question tool exists. Print this block exactly,
then wait for the answer:

```text
🦴 [widgetx › skeleton] Which style?

1. ✨ text   — a light sweeps across the text itself ("Installing…")
2. 🔄 sync   — gray blocks, one shared light crossing all of them
3. 💓 pulse  — gray blocks fading in and out together
4. 🌊 wave   — gray blocks fading one after another, top to bottom (recommended)

Reply with a number or name.
```

Aliases: `shimmer`, `shimmer-text`, `shine` → text · `synced`, `blocks`,
`normal`, `classic` → sync · `breathe`, `fade` → pulse · `cascade`,
`stagger` → wave.

If the user asks which to pick:

| Style | Pick it when                                                                 |
| ----- | ---------------------------------------------------------------------------- |
| text  | There is a status line and no layout to imitate: "Installing…", "Thinking…", a busy button. |
| sync  | The shape of the content is known (list, card, table). The default for blocks. |
| pulse | Many placeholders, small elements, or low-power devices. The cheapest to draw. |
| wave  | A vertical list where the eye should travel down the rows.                    |

`text` and a block style combine well: a shimmering "Loading skills…" line
above a block list. That is still two installs; do the one that was asked.

## Rules for every style

* **Only while loading.** The skeleton exists between "request started" and
  "content ready". Remove it (or its class) the moment content arrives; never
  leave an animation running on finished UI.
* **Same size as the real thing.** Block skeletons copy the final layout:
  same row height, gaps, and rough widths as the content they stand in for,
  so nothing shifts when it loads. Vary line widths a little (55% / 68% /
  60%) and make the last line of a paragraph shorter; identical bars look
  like a rendering bug.
* **Colors come from the text color.** The reference code derives every tone
  from `currentColor`, so it is correct in light and dark themes with no
  setup. Replace the two tokens with project theme tokens only when the
  project already has matching ones (a "muted" or "surface" tone).
* **Animate cheap properties only**: `background-position` and `opacity`.
  Never width, height, margin, or anything that moves layout.
* **Reduced motion.** Under `prefers-reduced-motion: reduce` the placeholder
  stays, the animation stops. The reference code includes this block; it
  must stay last so it wins.
* **Accessibility.**
  * Blocks are decoration: each block, or their wrapper, gets
    `aria-hidden="true"`.
  * The region being loaded gets `aria-busy="true"` while loading.
  * Each loading region has exactly one text for assistive tech, in an
    element with `role="status"`: either visible ("Loading skills…") or
    hidden with the project's existing visually-hidden utility. Do not add
    such a utility just for this; a visible line is fine.
  * Shimmering text stays real text, so it is read normally. Put
    `role="status"` on it when it reports progress.

## Shared keyframes

Both are needed by more than one style. Install only the ones the chosen
style uses.

```css
@keyframes wx-sweep {
  from { background-position: 100% 0; }
  to   { background-position: -100% 0; }
}

@keyframes wx-pulse {
  50% { opacity: 0.4; }
}
```

`wx-sweep` is seamless because the gradient is twice as wide as its area and
repeats: the light crosses during the first half of the cycle and rests
during the second.

## 1 · text

The text dims to 45% of its own color and a band of full color travels across
it, left to right, every 2 seconds.

```css
.wx-shimmer-text {
  --wx-text-dim: color-mix(in srgb, currentColor 45%, transparent);
  display: inline-block;
  background: linear-gradient(90deg, var(--wx-text-dim) 35%, currentColor 50%, var(--wx-text-dim) 65%) 100% 0 / 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: wx-sweep 2s linear infinite;
}

@media (prefers-reduced-motion: reduce) {
  .wx-shimmer-text { animation: none; background: none; -webkit-text-fill-color: currentColor; }
}
```

```html
<p role="status"><span class="wx-shimmer-text">Installing opencode 2.3.0…</span></p>
```

* `-webkit-text-fill-color` is used instead of `color: transparent` on
  purpose: `color` stays intact, so `currentColor` still means the text's
  real color. Do not "simplify" it.
* Wrap only the text. Emoji and icon fonts inside the span turn invisible;
  keep icons outside it. SVG icons that use `currentColor` are unaffected.
* Put the class on the smallest element that holds the words, not on a
  container that has its own background.
* Needs: keyframes `wx-sweep`.

## 2 · sync

Gray blocks with a soft light crossing them every 1.8 seconds. The light is
anchored to the window, not to each block, so it reads as **one** light
passing over the whole layout: a block on the left lights up before a block
on the right.

```css
.wx-skeleton {
  --wx-skeleton-base: color-mix(in srgb, currentColor 11%, transparent);
  --wx-skeleton-shine: color-mix(in srgb, currentColor 12%, transparent);
  display: block;
  height: 0.75rem;
  border-radius: 4px;
  background-color: var(--wx-skeleton-base);
}

.wx-skeleton-sync {
  background-image: linear-gradient(100deg, transparent 40%, var(--wx-skeleton-shine) 50%, transparent 60%);
  background-size: 200% 100%;
  background-attachment: fixed;
  animation: wx-sweep 1.8s linear infinite;
}

@media (prefers-reduced-motion: reduce) {
  .wx-skeleton { animation: none; background-image: none; }
}
```

```html
<section aria-busy="true">
  <p role="status">Loading skills…</p>
  <div aria-hidden="true">
    <div class="row">
      <span class="wx-skeleton wx-skeleton-sync" style="width: 1.5rem"></span>
      <span class="wx-skeleton wx-skeleton-sync" style="width: 55%"></span>
    </div>
    <!-- more rows, same shape as the real rows -->
  </div>
</section>
```

Size each block with whatever the project uses for sizing (utility classes,
inline style, a prop). A circle is `border-radius: 50%` with equal width and
height.

* `background-attachment: fixed` is what makes the light shared. Where the
  browser cannot honor it (an ancestor with `transform`, and some mobile
  browsers), every block quietly gets its own sweep instead, still on the
  same beat. That fallback is fine; do not add workarounds for it.
* **Optional — fading tail.** For a long list, fade the placeholder rows out
  toward the bottom by putting this class on the wrapper of the rows:

  ```css
  .wx-skeleton-fade {
    -webkit-mask-image: linear-gradient(to bottom, #000 30%, transparent);
    mask-image: linear-gradient(to bottom, #000 30%, transparent);
  }
  ```

  Add it when the target is a list of six or more rows, or when asked.
* **Optional — late arrivals.** Blocks rendered at the same moment are in
  phase automatically. If the app adds skeleton blocks at different moments
  and the drift is visible, align them all to one clock after mounting:

  ```js
  for (const animation of document.getAnimations()) {
    if (animation.animationName?.startsWith("wx-")) animation.startTime = 0;
  }
  ```

  Add this only when that case really exists in the project.
* Needs: keyframes `wx-sweep`.

## 3 · pulse

The same gray blocks, with no light: they all fade to 40% and back together
every 1.6 seconds. Only `opacity` changes, so it is the lightest style to
draw.

```css
/* .wx-skeleton base rule from "2 · sync" goes here, unchanged */

.wx-skeleton-pulse {
  animation: wx-pulse 1.6s ease-in-out infinite;
}

@media (prefers-reduced-motion: reduce) {
  .wx-skeleton { animation: none; }
}
```

```html
<span class="wx-skeleton wx-skeleton-pulse" style="width: 60%" aria-hidden="true"></span>
```

* The unused `--wx-skeleton-shine` token may be dropped from the base rule.
* Needs: keyframes `wx-pulse`.

## 4 · wave

`pulse`, but each row starts 120 ms after the one above it, so the fade
travels down the list.

```css
/* .wx-skeleton base rule from "2 · sync" goes here, unchanged */

.wx-skeleton-wave {
  animation: wx-pulse 1.6s ease-in-out infinite;
  animation-delay: calc(var(--wx-i, 0) * 120ms);
}

@media (prefers-reduced-motion: reduce) {
  .wx-skeleton { animation: none; }
}
```

```html
<div class="row">
  <span class="wx-skeleton wx-skeleton-wave" style="--wx-i: 0; width: 55%"></span>
</div>
<div class="row">
  <span class="wx-skeleton wx-skeleton-wave" style="--wx-i: 1; width: 68%"></span>
</div>
```

* `--wx-i` is the row index, starting at 0. All blocks **in the same row
  share the same index**; the step is per row, not per block.
* In a component, set `--wx-i` from the loop index. In static HTML, write it
  by hand or with `:nth-child()` rules.
* Needs: keyframes `wx-pulse`.

## Fitting the stack

**Global CSS (any web framework).** Put the widget in one shared stylesheet:
a new file next to the project's other shared styles, imported once where
global styles are loaded. The widget is used across screens, so it does not
belong inside one component's scoped styles.

**Tailwind.** Keep the reference classes; do not rebuild the animation out of
utilities or theme config. Add the rules to the global stylesheet inside
`@layer components { … }` (keyframes at the top level of the file) so sizing
utilities can override the defaults: `class="wx-skeleton wx-skeleton-sync h-4
w-32 rounded-full"`. Keep the reduced-motion block in the same layer, last.

**Component frameworks** (React, Vue, Svelte, Astro, Solid…). Add a wrapper
component only when the project already keeps small UI components in a shared
folder; follow the naming and prop style found there. Otherwise the classes
alone are the widget. A wrapper stays this small:

```tsx
type SkeletonProps = { width?: string; height?: string; className?: string };

export function Skeleton({ width, height, className = "" }: SkeletonProps) {
  return (
    <span
      aria-hidden="true"
      className={`wx-skeleton wx-skeleton-sync ${className}`}
      style={{ width, height }}
    />
  );
}
```

**Scoped styles and CSS Modules.** Keyframe names are rewritten per file.
Keep the keyframes and the classes that use them in the same file, or use the
global stylesheet as above.

**Webviews and embedded panels** (editor extensions, Electron, Tauri). Same
CSS. The window is the panel, so `sync` sweeps across the panel. Use the
host's theme variables for the two tokens only if the project already styles
with them.

**Older browser targets.** `color-mix()` needs Chrome 111, Firefox 113, or
Safari 16.2. If the project's stated targets are older, replace each
`color-mix(...)` with a fixed translucent color per theme (for example
`rgb(128 128 128 / 0.16)`), and say so in the report.

**Not CSS** (egui, React Native, Flutter, SwiftUI, Compose, terminal UIs…).
Port the spec below with the platform's own drawing and animation tools.

| Style | Cycle            | What changes                                                                 |
| ----- | ---------------- | ---------------------------------------------------------------------------- |
| text  | 2 s, linear      | Text at 45% alpha; a full-color band, 60% of the text width with soft edges, crosses left → right during the first half of the cycle. |
| sync  | 1.8 s, linear    | Block = text color at 11% alpha. A band adding 12% alpha, 40% of the window width, crosses the **window** left → right during the first half of the cycle; each block draws the part that is over it. |
| pulse | 1.6 s, ease-in-out | Block opacity 1 → 0.4 → 1.                                                   |
| wave  | 1.6 s, ease-in-out | As pulse, each row delayed 120 ms more than the row above.                   |

* Drive every placeholder from **one shared clock** (app or frame time), not
  from the moment each one was created. `phase = (time % cycle) / cycle`.
  That is what keeps them in sync.
* Request repaints only while a skeleton is on screen, and stop when loading
  ends. In immediate-mode UIs (egui: `ctx.input(|i| i.time)` for the clock,
  `ctx.request_repaint()` while visible) a forgotten repaint loop burns CPU
  forever.
* Where text cannot take a gradient fill, color the text per character from
  each character's distance to the band.
* Honor the platform's reduce-motion setting when it exposes one: draw the
  static placeholder.

## Before reporting

- [ ] Only the chosen style's rules and the keyframes it needs were added.
- [ ] The reduced-motion block is present and comes last.
- [ ] Blocks are hidden from assistive tech; the region has one status text.
- [ ] Placeholders match the real content's size, and disappear when it loads.
- [ ] Nothing animates layout.
