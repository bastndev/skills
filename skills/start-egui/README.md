<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/github/icons/start-logo/start-egui.webp" width="150" />
</p>

<h1 align="center">[Start] / rust-egui-starter</h1>

<p align="center">
  <strong>Start egui</strong> — Scaffold a native Rust desktop app with egui, built to grow
</p>

<p align="center">
  <a href="../../README.md">← Back to Start / Middle / [End]</a>
</p>

---

Scaffolds a native desktop app in **Rust** with **egui/eframe 0.37**, laid out the way large
production egui apps are: one Cargo workspace with programs in `apps/` and single-purpose
libraries in `crates/`, strict layers, and the product name in exactly one place. It opens a
neutral UI shell you can turn into an IDE, a photo editor, a video editor or any other tool.

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

## Install

```bash
npx skills add bastndev/skills --skill start-egui
```

## What you get

```
your-app/
├── Cargo.toml              # workspace: shared version, dependencies, lints, build profiles
├── apps/your-app/          # the program: main.rs only opens the window
├── crates/
│   ├── brand/              # name, repository, version: the only place the name is written
│   └── ui/                 # everything on screen
│       └── src/
│           ├── lib.rs      # the App and the panel layout
│           ├── panels/     # left_panel, center_panel, right_panel, status_bar
│           └── update_dialog.rs
├── assets/app-icon/        # app-icon.svg (the one you edit) + rendered sizes
├── packaging/              # linux/app.desktop.in (dock name + icon); macos/, windows/ for later
├── scripts/                # app-icon.sh (render the icon), install-desktop.sh (Linux dock)
├── .cargo/  .config/  .github/workflows/   # ready for later
├── NOTES.md                # commands you type by hand: run, checks, change name/icon
├── AGENTS.md  CLAUDE.md    # rules for AI assistants, including egui 0.37 notes
├── ARCHITECTURE.md         # project tree + layer rules
├── rust-toolchain.toml  rustfmt.toml  clippy.toml
└── README.md  LICENSE  .gitignore  .gitattributes
```

`cargo run` opens a window with:

- a **left panel** with a list you can click,
- a **main view** that shows what you picked,
- a **right panel** with details,
- a **status bar** with the app name and version,
- a **Check for updates** button that opens an update dialog (placeholder data, ready for real logic).

The side panels resize by dragging. The window has its own icon (a blue `>_` tile) that you
replace by editing one SVG. On Linux, `scripts/install-desktop.sh` makes the dock show the app's
name and icon instead of a generic gear.

## How it works

1. A short survey asks for the display name, machine name, crate prefix, GitHub repo,
   description and author. Every field has a default.
2. The template is copied into the current folder and the placeholders are filled in.
3. `cargo build`, `cargo fmt --check`, `cargo clippy -- -D warnings` and `cargo test` must all pass,
   then a short smoke run checks that the window opens.

It never pushes, tags, publishes or installs system packages.

## Requirements

- Rust (via [rustup](https://rustup.rs)) 1.95 or newer.
- Linux, Windows or macOS. Verified on Ubuntu 24.04 (Wayland) without extra system packages.

## License

Apache-2.0, see [LICENSE.txt](LICENSE.txt). Projects you create with it are MIT.
