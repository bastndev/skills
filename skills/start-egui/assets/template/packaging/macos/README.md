# macOS packaging

Not built yet. This folder will hold what turns the program into a macOS app.

## Developing on macOS

Nothing from this folder is needed. `cargo run` shows the window title from `crates/brand` and the
Dock icon from `assets/app-icon/app-icon.png` (set in `apps/*/src/main.rs`). The Dock and menu bar
show the program's file name (the machine name) until the app is bundled.

## What goes here when macOS is shipped

- **`Info.plist.in`**: a template, like `packaging/linux/app.desktop.in`, filled from
  `crates/brand`. It sets the name in the Dock and menu bar (`CFBundleName`), the bundle id, the
  version and the icon file.
- **Packaging script** (`package.sh`): builds in release mode and assembles
  `<Name>.app/Contents/{Info.plist, MacOS/<binary>, Resources/app-icon.icns}`, then a `.dmg`.
- **`app-icon.icns`**: rendered from `assets/app-icon/app-icon.svg` (`iconutil` ships with macOS).
- **Signing and notarization** (optional): without an Apple Developer account, macOS blocks the
  first open until the user allows it in System Settings.

Build and test it on a Mac (a GitHub Actions `macos-latest` runner works).
