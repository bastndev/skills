---
name: start-egui
description: Scaffold a Rust desktop app with egui/eframe 0.37 as a layered Cargo workspace (apps/ + crates/). Creates brand constants, an app icon with Linux dock integration, a resizable three-panel UI shell with a status bar and an update-dialog placeholder, shared lints, toolchain and formatting config, and AGENTS.md rules. Use when starting, creating, or bootstrapping a new Rust desktop app, egui or eframe project, or native GUI (an IDE, a photo or video editor, a tool) in the current directory.
license: Complete terms in LICENSE.txt
metadata:
  author: bastndev
  version: "1.2.0"
---

# Rust + egui desktop app scaffold

Create a native desktop app from the files in `assets/template/`. The result runs with `cargo run`
and shows a neutral UI shell (left list, main view, right details, status bar with the version,
and a fake update dialog) that becomes an IDE, a photo editor, a video editor or any other app.

Keep the generated project small and keep its layer rules intact: they are the point of this base.

## Setup survey

Before writing files, show one compact setup survey. Use text-entry fields; do not present values
as choice/select options. Prefill each field with its default when the interface supports
editable defaults. Otherwise show the default in the prompt and let an empty response accept it.

- `DISPLAY_NAME`: shown to people (window title, dialogs). Default: the current folder's basename
  in Title Case, with `-` and `_` turned into spaces (`photo-lab` → `Photo Lab`).
- `MACHINE_NAME`: binary, package and app id. Default: the folder basename, lowercased, with every
  character outside `a-z 0-9 -` turned into `-`. Must match `^[a-z][a-z0-9-]*$`.
- `CRATE_PREFIX`: prefix for internal crates (`<prefix>-brand`, `<prefix>-ui`). Default `app`.
  Must match `^[a-z][a-z0-9]*$` (no `-`: it is also used as `<prefix>_brand` in Rust code).
  Internal crates are deliberately not named after the product, so a rename touches few files.
- `GITHUB_REPO`: `owner/repo`. Default: parsed from `git remote get-url origin` when it is a
  GitHub URL; otherwise `bastndev/{{MACHINE_NAME}}`.
- `DESCRIPTION`: one sentence ending with a period. Default
  `A desktop app built with Rust and egui.`
- `AUTHOR`: for `LICENSE`. Default `Gohit X (bastndev)`.
- `YEAR`: current year.

`DISPLAY_NAME` and `DESCRIPTION` end up inside Rust and TOML string literals: reject `"` and `\`.
`MACHINE_NAME` must differ from `{{CRATE_PREFIX}}-brand` and `{{CRATE_PREFIX}}-ui`.

## Scaffold procedure

1. Use the current working directory as the project root. Never create a child directory named
   after the project.
2. Inspect the directory before writing. If a `Cargo.toml`, `apps/` or `crates/` already exists,
   stop and ask. Preserve unrelated files (`.git/`, notes); the skill installer's `.agents/` and
   `skills-lock.json` are removed at the end (step 11). A `README.md`,
   `LICENSE` or `.gitignore` left by GitHub's "Initial commit" may be replaced; say so in the
   report. Ask before overwriting anything else.
3. Copy every file from `assets/template/`, including dotfiles and dot-folders (`.cargo/`, `.config/`, `.github/`,
   `.gitignore`, `.gitattributes`), into the project root. Then make the scripts executable,
   whatever the copy did to permissions:

   ```bash
   chmod +x scripts/*.sh
   ```

   Without this, running `scripts/install-desktop.sh` fails with "exists but is not an
   executable file" (fish) or "Permission denied" (bash).
4. Rename every path containing `{{MACHINE_NAME}}` to use `<MACHINE_NAME>`: the folder
   `apps/{{MACHINE_NAME}}` and the icons `assets/app-icon/hicolor/*/apps/{{MACHINE_NAME}}.*`.
5. Replace `{{DISPLAY_NAME}}`, `{{MACHINE_NAME}}`, `{{CRATE_PREFIX}}`, `{{GITHUB_REPO}}`,
   `{{DESCRIPTION}}`, `{{AUTHOR}}` and `{{YEAR}}` in every text file. Skip binary files (`*.png`).
   Leave `@DISPLAY_NAME@` and `@APP_ID@` in `packaging/linux/app.desktop.in`: the scripts fill them.
6. Confirm no placeholder remains, in file contents or in names:

   ```bash
   grep -rn '{{[A-Z_]*}}' . --exclude-dir=target --exclude-dir=.git
   find . -name '*{{*' -not -path './.git/*'
   ```

7. Build: `cargo build`. The first build downloads and compiles about 400 crates and takes several
   minutes; say so before starting. If it fails because a Linux system library is missing, report
   the exact error and **ask before installing any system package**. (Verified on Ubuntu 24.04,
   Wayland: no system packages were needed.)
8. Run `cargo fmt` (real names change line lengths), then all of these. Do not report success
   unless every one passes:

   ```bash
   cargo fmt --check
   cargo clippy --all-targets -- -D warnings
   cargo test
   ```

9. Smoke run, only when a display is available: `timeout 5 cargo run`. Exit code `124` means the
   window stayed open until the timeout, which is the expected result. A panic or any other exit
   code is a failure. Without a display, skip this and say so.
10. Run `git diff --check` when the root is a Git repository. Do not commit unless asked.
11. Clean up, as the very last change to the folder: delete the files the skill installer left in
    the project root, so only the project remains.

    ```bash
    rm -rf .agents skills-lock.json
    ```

    Only if `.agents/skills/` holds other skills besides `start-egui`, ask before deleting.
12. Report: the files created, anything replaced, the check results, and the next steps for the
    person, in this order, as in the **Run** section of `NOTES.md`:
    1. On Linux, `scripts/install-desktop.sh` first, so the dock shows the app's name and icon
       instead of the raw id and a generic icon (it writes only to `~/.local/share`; `--remove`
       undoes it). Again after changing `DISPLAY_NAME` or the icon. Run it yourself only if they ask.
    2. `cargo run`.

    Point to `NOTES.md` for the commands they will type by hand.

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
  icon (`app-icon.png`, embedded by `main.rs`) and the Linux `hicolor/` sizes. On Linux,
  `scripts/install-desktop.sh` fills `packaging/linux/app.desktop.in` from `crates/brand` and
  installs it with the icons for the current user, so the dock shows the real name and icon.
  `MACHINE_NAME` is the app id that ties them together.
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
