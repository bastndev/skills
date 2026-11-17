# App icon

`app-icon.svg` is the only file you edit. Everything else in this folder is generated from it.

## Change the icon

1. Change the colour under `TILE COLOUR` in `app-icon.svg`,
   or replace `app-icon.svg` with your own square SVG (512×512 works best).
2. Run `scripts/install-desktop.sh`. It renders `hicolor/` and `app-icon.png` (via
   `scripts/app-icon.sh`) and installs them, so the dock shows the new icon. Restart the app.

## Files

| File | What it is | Used by |
|---|---|---|
| `app-icon.svg` | The master | You |
| `app-icon.png` | 256 px render | Window icon, embedded by `apps/*/src/main.rs` (X11, Windows) |
| `hicolor/<size>/apps/<app id>.png`, `hicolor/scalable/apps/<app id>.svg` | Linux icon theme | Dock, app menu, `.deb` |

The `<app id>` is `MACHINE_NAME` from `crates/brand`. `scripts/install-desktop.sh` uses it for the
`.desktop` file name and its `Icon=` line, so they always match.

Original artwork, MIT like the rest of the project.
