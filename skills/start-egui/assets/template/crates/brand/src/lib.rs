//! The product's name, identifiers and version.
//! This is the only place in the code where the name is written.

/// Shown to people: window title, dock and app menu, About, update dialog.
/// After changing it, run `scripts/install-desktop.sh` so the Linux dock shows it too.
pub const DISPLAY_NAME: &str = "{{DISPLAY_NAME}}";

/// Used by machines: binary, package and .desktop file name.
pub const MACHINE_NAME: &str = "{{MACHINE_NAME}}";

/// Where releases are published, as `owner/repo` on GitHub.
pub const GITHUB_REPO: &str = "{{GITHUB_REPO}}";

/// The version from the workspace `Cargo.toml`, filled in at compile time.
pub const VERSION: &str = env!("CARGO_PKG_VERSION");
