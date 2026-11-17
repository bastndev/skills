# Windows packaging

Not built yet. This folder will hold what turns the program into a Windows installer.

## Developing on Windows

Nothing from this folder is needed. `cargo run` shows the window title from `crates/brand` and the
taskbar icon from `assets/app-icon/app-icon.png` (set in `apps/*/src/main.rs`).

## What goes here when Windows is shipped

- **Installer** (`.msi` with WiX, or `.exe` with Inno Setup): copies the program and creates the
  Start-menu shortcut. The shortcut's name is the app name people see; fill it from `crates/brand`.
- **Packaging script** (`package.ps1`): builds in release mode and runs the installer tool.
- **`.exe` icon:** Explorer shows the icon stored inside the `.exe`. That needs an `app-icon.ico`
  (rendered from `assets/app-icon/app-icon.svg`) and a `build.rs` in the app that embeds it.
- **Signing** (optional): without a code-signing certificate, Windows SmartScreen warns on first run.

Build and test it on Windows (a GitHub Actions `windows-latest` runner works).
