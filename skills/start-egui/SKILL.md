---
name: start-egui
description: Scaffold a Rust desktop app with egui/eframe 0.37 as a layered Cargo workspace (apps/ + crates/). Creates brand constants, an app icon with Linux dock integration, a resizable three-panel UI shell with a status bar and an update-dialog placeholder, shared lints, toolchain and formatting config, and AGENTS.md rules. Use when starting, creating, or bootstrapping a new Rust desktop app, egui or eframe project, or native GUI (an IDE, a photo or video editor, a tool) in the current directory.
license: Complete terms in LICENSE.txt
metadata:
  author: bastndev
  version: "1.3.0"
---

# Rust + egui desktop app scaffold

Create a native desktop app from the files in `assets/template/`. The result runs with `cargo run`
and shows a neutral UI shell (left list, main view, right details, status bar with the version,
and a fake update dialog) that becomes an IDE, a photo editor, a video editor or any other app.

Keep the generated project small and keep its layer rules intact: they are the point of this base.

Two scripts in this skill's `scripts/` folder do the mechanical work, so every run is fast and the
same. Below, `<skill>` is the folder holding this `SKILL.md` (installed with `npx skills add`, it
is `.agents/skills/start-egui`).

- Run every command from the project root: the current working directory. Never create a child
  directory named after the project.
- Run the scripts with `bash <skill>/scripts/<name>.sh`, so they work whatever the installer did
  to file permissions. Do not copy, rename or fill in template files by hand.
- Between steps, write one short line at most. The person sees the full result in the final table.

## 1. Setup survey

1. Run `bash <skill>/scripts/scaffold.sh --defaults`. It writes nothing. It prints each value's
   default as `KEY=VALUE`, an `INVALID=` line for a default that breaks a rule, and a `FOLDER=` line:
   - `FOLDER=ok`, or `FOLDER=ok, replaces: …` (a `README.md`, `LICENSE` or `.gitignore` left by
     GitHub's "Initial commit"): go on.
   - `FOLDER=stop` (a `Cargo.toml`, `apps/` or `crates/` exists) or `FOLDER=ask` (other files
     would be overwritten): stop, show the line and ask. Go on only if the person agrees, and then
     add `--overwrite` in step 2.
2. Show the seven values as a table (`Field | Value`), then ask **one** question: "Create the
   project with these values?", with the options **Yes, create it** (recommended) and **Change
   values**. A field with an `INVALID=` line must be changed first.
3. Only after **Change values**: ask which fields to change and their new values, as free text.
   The rules, which `scaffold.sh` checks again:
   - `DISPLAY_NAME`: shown to people (window title, dock, dialogs). Default: the folder's name in
     Title Case, with `-` and `_` as spaces (`photo-lab` → `Photo Lab`).
   - `MACHINE_NAME`: binary, package and app id. Must match `^[a-z][a-z0-9-]*$`. Default: the
     folder's name, lowercased, with every character outside `a-z 0-9 -` turned into `-`.
   - `CRATE_PREFIX`: prefix for internal crates (`<prefix>-brand`, `<prefix>-ui`). Default `app`.
     Must match `^[a-z][a-z0-9]*$` (no `-`: it is also used as `<prefix>_brand` in Rust code).
     Internal crates are deliberately not named after the product, so a rename touches few files.
   - `GITHUB_REPO`: `owner/repo`. Default: from `git remote get-url origin` when it is a GitHub
     URL; otherwise `bastndev/<MACHINE_NAME>`.
   - `DESCRIPTION`: one sentence ending with a period (added when missing).
   - `AUTHOR`: for `LICENSE`. `YEAR`: the current year.

   `DISPLAY_NAME` and `DESCRIPTION` end up inside Rust and TOML strings, so they cannot contain
   `"` or `\`. `MACHINE_NAME` must differ from `<prefix>-brand` and `<prefix>-ui`.

## 2. Scaffold

Run `bash <skill>/scripts/scaffold.sh`, with one option per changed value, for example
`--display-name "Photo Lab" --description "Edits photos."`. The options are `--display-name`,
`--machine-name`, `--crate-prefix`, `--github-repo`, `--description`, `--author` and `--year`;
a value left out uses its default. With every default accepted, run it with no options.

It copies every template file (dotfiles included), names the app folder and the icons after
`MACHINE_NAME`, fills in every placeholder, makes `scripts/*.sh` executable and checks that no
placeholder is left. It never touches files that are not in the template (`.git/`, notes). It
leaves `@DISPLAY_NAME@` and `@APP_ID@` in `packaging/linux/app.desktop.in`: the project's scripts
fill them.

It ends with `scaffold: ok` and the values it used, as `KEY=VALUE`, plus `REPLACED=` when it
replaced files. Use those values in the final table. Exit code `1` means a value is invalid: ask
for a new one. Exit code `2` means the folder needs the person's decision: see step 1.

## 3. Build

Say first that the first build compiles about 285 crates and takes 3 to 4 minutes, once per
project folder (later builds take seconds). Run `cargo build` with a timeout of at least
10 minutes, and keep the time from its `Finished … in <time>` line.

If it fails because a Linux system library is missing, report the exact error and **ask before
installing any system package**. (Verified on Ubuntu 24.04, Wayland: no system packages were
needed.)

## 4. Check and clean up

Run `bash <skill>/scripts/finish.sh`. It prints one line per step and stops at the first failure:
`cargo fmt` (real names change line lengths) then `cargo fmt --check`,
`cargo clippy --all-targets -- -D warnings`, `cargo test`, `cargo build`, a smoke run (the window
must still be open after 5 seconds; skipped without a display) and `git diff --check` in a Git
repository. When every step passes, it deletes the installer's `.agents/` and `skills-lock.json`,
as the very last change to the folder. Its last line is `RESULT ok`, or `RESULT failed: <step>`
after the error.

- `RESULT failed`: fix the cause with the smallest change and run `finish.sh` again. Never report
  success without `RESULT ok`.
- `cleanup skipped`: `.agents/` holds other skills too. Ask before deleting it with
  `rm -rf .agents skills-lock.json`.
- Do not commit unless asked.

## 5. Final message

Reply with only this table and the line under it: the values printed after `scaffold: ok`, and
the build time from step 3.

| Field | Value | Status |
|---|---|---|
| DISPLAY_NAME | Photo Lab | ✅ |
| MACHINE_NAME | photo-lab | ✅ |
| CRATE_PREFIX | app | ✅ |
| GITHUB_REPO | bastndev/photo-lab | ✅ |
| DESCRIPTION | A desktop app built with Rust and egui. | ✅ |
| AUTHOR | Gohit X (bastndev) | ✅ |
| YEAR | 2026 | ✅ |
| Build | cargo build · 3m 33s | ✅ |
| Checks | fmt · clippy · test · window opens | ✅ |

🎉 The project was created successfully.

- The window check was skipped (no display): write `fmt · clippy · test (window: no display)`.
- `scaffold.sh` printed `REPLACED=`: add the row `Replaced | <files> | ✅`.
- A step still fails: mark its row ❌ with the short error, and in place of the 🎉 line write one
  line saying what is needed. Never write the 🎉 line without `RESULT ok`.

## Boundaries

- Never push, tag, publish a release, or install system packages unless the user separately asks.
- Do not add dependencies beyond `eframe`. Each new crate is the user's decision.
- Do not create CI workflows, package builders (`.deb`, `.msi`, `.dmg`) or real update logic: not
  part of this base. `packaging/macos` and `packaging/windows` hold only a README until each is
  built and tested on its own system.
- Do not create empty crates. `xtask/` is added when a build helper needs it.
- Keep `eframe = "0.37"`. Do not move to a newer egui unless the user asks: its API changes between
  minor versions and this template is verified against 0.37.0 only.

## What the base guarantees

- One Cargo workspace: programs in `apps/`, libraries in `crates/`. Version, edition, minimum Rust
  (`1.95`, egui 0.37's minimum), license and repository are declared once in the root `Cargo.toml`.
- Layers: `brand` (L0, no dependencies) → `ui` (L3, the only crate using egui) → the app (L4).
  `ARCHITECTURE.md` shows the project tree and where logic crates (L1/L2) go when needed.
- The product name is written only in `crates/brand`.
- App icon: `assets/app-icon/app-icon.svg` is the master; `scripts/app-icon.sh` renders the window
  icon (`app-icon.png`, embedded by `main.rs`) and the Linux `hicolor/` sizes, and leaves the
  existing icons untouched when no renderer is installed. On Linux, `scripts/install-desktop.sh`
  fills `packaging/linux/app.desktop.in` from `crates/brand` and installs it with the icons for
  the current user, so the dock shows the real name and icon. `MACHINE_NAME` is the app id that
  ties them together.
- Dev builds compile dependencies optimised (`opt-level = 2`) so the UI is smooth under `cargo run`.
- Shared lints (`[workspace.lints]`: `unsafe_code` forbidden, `dbg!`/`todo!` warned) and
  `clippy.toml`, `rustfmt.toml` (120 columns), `rust-toolchain.toml` (`stable` + rustfmt + clippy).
- `AGENTS.md` (+ `CLAUDE.md` pointing to it) gives AI assistants the rules and egui 0.37 notes.
- `.config/` and `.github/workflows/` exist, kept by a `.gitkeep` (Git doesn't track empty folders); `.cargo/config.toml` holds commented examples.
- The update dialog takes its data as a parameter, so real update logic plugs in without redrawing it.

## Growing the app

Tell the user how, when they ask:

- **Rename the panels** after what the app shows (`left_panel.rs` → `layers.rs`, …).
- **A new feature** = a logic crate in `crates/` (no egui, with tests) + a panel or widget in
  `crates/ui` + one line in the app to connect them.
- **Add a crate:** `cargo new --vcs none --lib --name <prefix>-<name> crates/<name>`. Check that its
  `Cargo.toml` inherits `rust-version.workspace = true` and has `[lints] workspace = true`; add
  either if missing. Declare it in `[workspace.dependencies]`.
- **Change the icon:** edit or replace `assets/app-icon/app-icon.svg` (512×512), then
  `scripts/install-desktop.sh` on Linux, or `scripts/app-icon.sh` elsewhere. The renderer is the
  first found of `rsvg-convert`, `resvg`, `inkscape`, `magick`, `gdk-pixbuf-thumbnailer`.
- **Never block the window:** slow work on a background thread + a channel;
  `ctx.request_repaint()` when the result arrives.

## egui 0.37 pitfalls

- `eframe::App` is implemented with `fn ui(&mut self, ui: &mut egui::Ui, frame)`. Older tutorials
  use `update(&mut self, ctx, frame)`, which no longer exists.
- Panels are `egui::Panel::left/right/top/bottom("id")` with `.default_size()`, `.min_size()`,
  `.exact_size()`, `.resizable()`, then `.show(ui, ..)`. Edge panels go **before** `CentralPanel`.
  Panels nest inside another panel with the same `.show(ui, ..)`.
- `egui::Id::new` is deprecated (an error under `-D warnings`): use `egui::Id::unique(..)`.
- Dialogs: `egui::Modal::new(id).show(ctx, ..)`; `.should_close()` covers Escape and outside clicks.
- When unsure, read `~/.cargo/registry/src/*/egui-0.37.0/` rather than guessing.
- Pinning an exact Rust version in `rust-toolchain.toml` makes rustup download a second copy of the
  compiler even when it matches the installed `stable`; the template uses `stable` on purpose.
