#!/usr/bin/env bash
# Registers the app with the desktop for your user only (no sudo), so the dock and the
# Activities view show the name and icon from the project while you develop with `cargo run`.
#
#   scripts/install-desktop.sh            install, or refresh after changing the name or icon
#   scripts/install-desktop.sh --remove   undo
#
# The .deb does the same system-wide; this is only for development.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
brand() { sed -n "s/^pub const $1: &str = \"\(.*\)\";/\1/p" "$root/crates/brand/src/lib.rs"; }
id="$(brand MACHINE_NAME)"
name="$(brand DISPLAY_NAME)"
apps="${XDG_DATA_HOME:-$HOME/.local/share}/applications"
icons="${XDG_DATA_HOME:-$HOME/.local/share}/icons/hicolor"

remove_icons() { find "$icons" -path "*/apps/$id.*" -delete 2>/dev/null || true; }

refresh() {
    # GNOME rescans an icon folder only when the folder's timestamp changes; overwriting a file
    # doesn't change it, so touch the theme folder to make the dock pick up the new icon.
    touch "$icons"
    # Only refresh an icon cache that already exists; without one, GTK reads the folders directly.
    if [ -f "$icons/icon-theme.cache" ]; then gtk-update-icon-cache -q -t -f "$icons" || true; fi
    update-desktop-database -q "$apps" 2>/dev/null || true
}

if [ "${1:-}" = "--remove" ]; then
    rm -f "$apps/$id.desktop"
    remove_icons
    refresh
    echo "Removed $id from the desktop."
    exit 0
fi

# Icons: render from app-icon.svg, then replace the installed copies. Without an SVG renderer,
# app-icon.sh says so and the icons already in the project are installed instead.
if ! bash "$root/scripts/app-icon.sh" >/dev/null; then
    echo "Installing the icons already in assets/app-icon/hicolor/ instead." >&2
fi
mkdir -p "$icons"
remove_icons
cp -r "$root/assets/app-icon/hicolor/." "$icons/"

# Desktop entry: fill in the name and id, and point Exec at the dev build instead of /usr/bin.
esc() { printf '%s' "$1" | sed 's/[&|\\]/\\&/g'; }
# The Exec path is quoted, so a project folder with spaces works. Inside the quotes the Desktop
# Entry spec wants \ " ` $ after a backslash, written twice because the file format unescapes
# once first, and % written as %%.
exec_path() {
    printf '"%s"' "$(printf '%s' "$1" | sed -e 's/\\/\\\\\\\\/g' -e 's/["`$]/\\\\&/g' -e 's/%/%%/g')"
}
mkdir -p "$apps"
sed -e '/^#/d' \
    -e "s|^Exec=@APP_ID@|Exec=$(esc "$(exec_path "$root/target/debug/$id")")|" \
    -e "s|@APP_ID@|$(esc "$id")|g" \
    -e "s|@DISPLAY_NAME@|$(esc "$name")|g" \
    "$root/packaging/linux/app.desktop.in" >"$apps/$id.desktop"

refresh
echo "Installed \"$name\" ($id) for $USER. Restart the app to see it."
