# 🏗️ {{DISPLAY_NAME}} — Architecture

{{DESCRIPTION}} Stack: Rust + **egui/eframe 0.37**.

## 📁 Project structure

```sh
{{MACHINE_NAME}}/
├── .cargo/
│   └── config.toml                  # Cargo settings for this project (empty until needed)
├── .config/                         # Settings for extra tools (nextest, typos…) — empty for now
├── .github/
│   └── workflows/                   # CI and release pipelines — empty for now
├── apps/                            # Programs you run and ship
│   └── {{MACHINE_NAME}}/
│       ├── Cargo.toml               # The program's package
│       └── src/main.rs              # Opens the window. No UI code, no logic
├── crates/                          # Libraries that do the work, one job each
│   ├── brand/
│   │   └── src/lib.rs               # Name, repo, version — the only place the name is written
│   └── ui/                          # Everything on screen (the only crate using egui)
│       └── src/
│           ├── lib.rs               # The App: state + panel layout
│           ├── panels/
│           │   ├── left_panel.rs    # Left: a list to pick from
│           │   ├── center_panel.rs  # Middle: the main view
│           │   ├── right_panel.rs   # Right: details of the selection
│           │   └── status_bar.rs    # Bottom: name, version, "Check for updates"
│           └── update_dialog.rs     # Update dialog; takes its data as a parameter
├── assets/                          # Icons, fonts, images the app ships with
│   └── app-icon/                    # The app icon — see its README.md
│       ├── app-icon.svg             # The master: the only icon file you edit
│       ├── app-icon.png             # Generated: window icon (embedded by main.rs)
│       └── hicolor/                 # Generated: Linux icon sizes, named after the app id
├── packaging/                       # Turns the program into what users install, one folder per OS
│   ├── linux/
│   │   └── app.desktop.in           # Dock/menu entry template; name and id filled from brand
│   ├── macos/README.md              # Not built yet: what goes here (.app, .dmg)
│   └── windows/README.md            # Not built yet: what goes here (installer, .exe icon)
├── scripts/                         # Developer shell helpers
│   ├── app-icon.sh                  # Renders app-icon.svg into app-icon.png and hicolor/
│   └── install-desktop.sh           # Registers the dev build: name + icon in the dock (--remove)
├── target/                          # Build output (gitignored)
├── .gitattributes                   # Line endings: LF everywhere
├── .gitignore
├── AGENTS.md                        # Rules for AI assistants
├── ARCHITECTURE.md                  # This file
├── CLAUDE.md                        # Points Claude Code to AGENTS.md
├── Cargo.lock                       # Exact dependency versions (committed)
├── Cargo.toml                       # Workspace: version, shared deps, lints, build profiles
├── clippy.toml                      # Code-checker settings
├── LICENSE                          # MIT
├── NOTES.md                         # Commands you type by hand: run, checks, name/icon
├── README.md
├── rust-toolchain.toml              # Rust compiler: stable + rustfmt + clippy
└── rustfmt.toml                     # Code style: 120 columns
```

## 🧱 Layers

A crate may depend only on crates in **lower** layers.

| Layer | Crates | Role | egui? |
|---|---|---|---|
| L0 | `brand` | Name, repo, version. No dependencies | No |
| L1 | one crate per feature's logic (e.g. `update`, `project`, `settings`) | Pure logic; tested without a window | **No** |
| L2 | later, e.g. `engine` | Combines L1 into the open session; owns the command list | **No** |
| L3 | `ui` | Draws state; turns clicks and keys into calls to lower layers | Yes |
| L4 | `apps/{{MACHINE_NAME}}` | Starts everything | Yes |

A new feature means a new crate. A new program you install means a new app.

## 📏 Rules

1. **egui only in L3 and L4.** Logic crates return data or send messages; they never draw.
2. **L1 crates don't depend on each other** unless there is a clear reason.
3. **One crate, one job.** If its description needs "and", split it.
4. **`main.rs` stays small:** read arguments, build the state, open the window.
5. **Internal crates are named `{{CRATE_PREFIX}}-*`**, not after the product, so a rename touches few files.
6. **Shared dependencies are declared once** in the root `Cargo.toml`; crates write `name.workspace = true`.
7. **A new feature** = an L1 crate (with tests) + a panel in `ui` + one line in the app.
8. **Never block the window.** Slow work runs on a background thread and reports back.
9. **The app id ties the desktop together.** `MACHINE_NAME` is the Wayland app id, the `.desktop`
   file name and the icon file name. If they differ, the dock shows the raw id and a generic icon.
