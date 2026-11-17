<h1 align="center">[WidgetX] / UI widgets</h1>

<p align="center">
  <strong>WidgetX</strong> — Small pieces that make an interface feel finished
</p>

<p align="center">
  <a href="../../README.md">← Back to Start / Middle / [End]</a>
</p>

---

Adds **one small UI widget in one style** to a project you already have — web, web app, or desktop. Two short questions (which widget, which style), then a few lines of dependency-free code written the way your project already writes its UI. It is not a component library: it installs only what you picked.

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

## Install

```bash
npx skills add bastndev/skills --skill widgetx
```

## Usage

```
/widgetx <widget> <style> (@path)

/widgetx                              # widget menu, then style menu
/widgetx 1                            # skeleton → style menu
/widgetx skeleton 2                   # skeleton in the sync style
/widgetx skeleton text (@src/ui/InstallStatus.tsx)
```

Natural language works too: _"add a skeleton to the skills list"_, _"make the 'Installing…' text shimmer"_.

## Widgets

| #   | Widget          | What it is                                             | Styles                     |
| --- | --------------- | ------------------------------------------------------ | -------------------------- |
| 1   | 🦴 **skeleton** | Loading placeholders: shimmering text or gray blocks   | text · sync · pulse · wave |

More widgets are on the way.

### 🦴 skeleton

```
Which skeleton style?

1. text
   a light sweeps across the text itself ("Installing…")
2. sync
   gray blocks, one shared light crossing all of them
3. pulse
   gray blocks fading in and out together
4. wave
   gray blocks fading one after another, top to bottom
5. type your own answer

↑↓ select  enter confirm  esc dismiss
```

| Style     | Pick it when                                                                    |
| --------- | ------------------------------------------------------------------------------- |
| **text**  | There is a status line and no layout to imitate: "Installing…", a busy button   |
| **sync**  | The shape of the content is known (list, card, table) — the default for blocks  |
| **pulse** | Many placeholders, small elements, or low-power devices — the cheapest to draw  |
| **wave**  | A vertical list where the eye should travel down the rows                       |

## How It Works

1. **Pick** — choose the widget, then the style, from a selectable list: arrow keys and Enter, no typing. CLIs without a question tool get the same menus as text (reply with a number or name).
2. **Look** — it reads your project first: stack, styling system, theme, where shared UI lives, and whether you already have that widget.
3. **Install** — adds only the chosen style, in your conventions. Point it at a file (`@path`) and it also wires the widget into that loading state.
4. **Report** — a compact block: files touched, a usage snippet, what to tune, which checks ran.

## What You Get

```
🧩 widgetx — skeleton › sync installed

Stack:  Next.js · Tailwind v4 · dark/light via data-theme
Files:  + src/styles/skeleton.css        (new)
        ~ src/app/globals.css            (1 import line)
        ~ src/components/SkillList.tsx   (loading state wired)

Use it:
  <div class="wx-skeleton wx-skeleton-sync" style="width: 60%"></div>

Tune:   --wx-skeleton-base · --wx-skeleton-shine · 1.8s cycle
Checks: typecheck ✅ · lint ✅ · visual check not performed
```

## Guarantees

- Zero dependencies added
- Only the style you picked — no extra variants, no demo pages
- Light and dark themes work with no setup (colors derive from your text color)
- Respects `prefers-reduced-motion` and ships with accessibility markup
- Existing files change only to register or wire the widget
- Never duplicates a widget your project already has
- Uncommitted work is never overwritten

---

→ Full spec & rules: [SKILL.md](./SKILL.md) · Skeleton reference: [references/skeleton.md](./references/skeleton.md)

<div align="center">
  <sub>Built for developers who want their AI agents to act with the discipline of a senior engineer.</sub>
  <br><br>
  <sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="https://github.com/bastndev/skills/blob/main/LICENSE">MIT</a></sub>
</div>
