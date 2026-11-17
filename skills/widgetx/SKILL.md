---
name: widgetx
description: "Adds one small, polished UI widget to an existing project (web, web app, desktop, mobile), fitted to its stack and theme, with zero new dependencies. Asks two short questions — which widget, then which style — and installs it. Ships today: skeleton loading placeholders in four styles — text (a light sweeps across the text), sync (gray blocks sharing one light), pulse (blocks fading together), wave (blocks fading in cascade). Use for 'add a skeleton', 'loading placeholder', 'shimmer text', 'show something while this loads'. Invoke with /widgetx <widget> <style> (@path)"
license: Complete terms in LICENSE.txt
metadata:
  author: bastndev
  version: "1.0.0"
---

# WidgetX / UI widgets

Small pieces that make an interface feel finished. Each run installs **one
widget in one style** into a project that already exists: a few lines of
dependency-free code, written the way that project already writes its UI.

`widgetx` is not a component library and never becomes one inside the user's
project. It adds only what was picked, nothing "for later".

## Invocation

```
/widgetx <widget> <style> (@path)

/widgetx                              # widget menu, then style menu
/widgetx 1                            # skeleton → style menu
/widgetx skeleton 2                   # skeleton in the sync style
/widgetx skeleton text (@src/ui/InstallStatus.tsx)
```

* Accept widget and style by **menu number or name**. The first value is the
  widget, the second is the style; a path may come anywhere.
* **Natural language works too.** A request that clearly names a widget skips
  Menu 1 ("add a skeleton to the skills list" → skeleton). A request that also
  names a style skips Menu 2 ("make the 'Installing…' text shimmer" → skeleton,
  text). Never guess a style that was not named.
* **Nothing given, or an unknown value** → print the menu for the missing
  choice and wait. Do not inspect the project or write anything yet.
* **Arguments lost in transport** — some IDE wrappers drop arguments and
  deliver only a path. Treat that as "nothing chosen": show Menu 1 with a
  `Target detected:` line and wait.
* **Two widgets or two styles requested** → install the first; after its
  report, offer the next.

### Menu 1 — widget

Always shown when no widget was named, even while the list has one entry:

```text
🧩 [widgetx] Which widget?

1. 🦴 skeleton — loading placeholders: shimmering text or gray blocks

Reply with a number or name (optionally add a @path).
```

If a path already arrived, append `Target detected: src/ui/List.tsx — [very
short description]` and reuse it when the user replies with just a number.

### Menu 2 — style

Each widget owns its style menu. Once the widget is known, read its reference
file from the registry below and print that file's **Style menu** block
exactly as written, then wait.

### Widget registry

| #   | Widget      | Reference                | Styles                       |
| --- | ----------- | ------------------------ | ---------------------------- |
| 1   | 🦴 skeleton | `references/skeleton.md` | text · sync · pulse · wave   |

The reference file is the source of truth for that widget: its style menu,
motion spec, reference code, and stack notes. Read the whole file before
writing any code. Do not rebuild a widget from memory.

**Workflow:** 1. Resolve the widget (Menu 1). 2. Read its reference and
resolve the style (Menu 2). 3. Inspect the project, read-only. 4. Install.
5. Verify. 6. Report.

---

## Operating Rules

### 1. Look before writing

Before creating anything, read enough of the project to answer:

* **Stack** — framework and language (plain HTML, React, Vue, Svelte, Astro,
  a webview, egui, React Native, Flutter…), from the manifest and entry points.
* **Styling system** — global CSS, Tailwind (and its major version), CSS
  Modules, scoped styles, CSS-in-JS, or a native theme struct.
* **Theme** — color tokens or variables, and how light/dark is switched.
* **Home for shared UI** — where small shared components and shared styles
  already live.
* **An existing equivalent** — search for the widget under its common names
  before adding it. If the project already has one, do not add a second: say
  where it is and offer to restyle or extend it instead.

Ignore `node_modules/`, build output, and generated files.

### 2. Fit the project, not the reference

The reference gives a motion spec and reference code. The project decides the
rest: file location, file naming, component shape, class naming, and color
tokens. Keep the reference's `wx-` names only when the project has no
convention of its own. Keep the spec values (durations, easing, color
strengths) unless the user asks to change them — they are what makes every
style look right.

On a stack the reference has no code for, port the spec with that stack's own
animation tools. Say in the report that it is a port.

### 3. Additive and minimal

* Create new files for the widget. Touch existing files only to register it
  (one import or one `@import` line) and to wire it into a target the user
  pointed at.
* Install only the chosen style. No extra variants, no demo page, no
  storybook entry, no tests unless the project tests its UI components and
  the user wants one.
* **Zero dependencies.** Never install a package for a widget. If the project
  already uses an animation library, the widget still does not need it.
* Never overwrite uncommitted work. If a file to be edited has local changes,
  keep them and edit around them.

### 4. Target or no target

* **A target was given** (file, component, or a clear description such as
  "the skills list") → install the widget, then use it there.
* **No target** → install the widget and show a usage snippet in the report.
  Do not pick a screen to change on the user's behalf.
* Never invent behavior. If the target has no loading state to hang the
  widget on, say so and show exactly where one would go; add it only when the
  user asked for the widget to work end to end.

### 5. Accessibility and motion are part of the widget

Every widget ships with its reduced-motion behavior and its accessibility
markup, as defined in its reference. They are not optional extras and are
never removed to save lines.

### 6. Verify honestly

Run the checks the project already has (typecheck, lint, build) when the
change touches code they cover. Do not add tooling. When a browser or preview
tool is available, look at the widget running; when it is not, say
`visual check not performed` — a passing build does not prove an animation
looks right.

---

## Report Format

Close every run with this compact block. Replace every value with the real
one; drop the `~` lines that do not apply.

```text
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

After the block, add at most two lines when they matter: a port note (rule 2),
or one thing the user must do by hand. No walkthrough of the code.

## Final checks

- [ ] Both choices came from the user (menu answer or explicit words).
- [ ] The widget's reference file was read in full before writing.
- [ ] No equivalent widget already existed in the project.
- [ ] Only the chosen style was installed, in the project's own conventions.
- [ ] No dependency was added.
- [ ] Reduced-motion handling and accessibility markup are in place.
- [ ] Existing files changed only to register or wire the widget.
- [ ] The report states which checks ran and whether it was seen running.
