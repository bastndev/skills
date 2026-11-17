# {{DISPLAY_NAME}} — Notes

Commands you type by hand. Run them from the project folder.

## Run

```sh
cargo run
```

Update the dock name and icon (Linux, after changing either; then restart the app):

```sh
scripts/install-desktop.sh
```

## Before committing

All three must pass:

```sh
cargo fmt
cargo clippy --all-targets -- -D warnings
cargo test
```

Optimised build, closer to what users get (slower to compile):

```sh
cargo run --release
```

## Change the name or the icon

| What | Where |
|---|---|
| Name | `DISPLAY_NAME` in `crates/brand/src/lib.rs` |
| Icon | `assets/app-icon/app-icon.svg` (square, 512×512) |
| Version | `version` under `[workspace.package]` in `Cargo.toml` |

Then update the dock and restart the app:

```sh
# Linux: renders the icon and updates the dock name + icon
scripts/install-desktop.sh

# Windows / macOS: only after changing the icon (the name needs nothing)
scripts/app-icon.sh
```

> On Linux, `cargo run` alone does not update the dock: it reads its own copy, which only
> `scripts/install-desktop.sh` refreshes. If the old icon stays, log out and back in once.

## Remove the app from the dock (Linux)

```sh
scripts/install-desktop.sh --remove
```