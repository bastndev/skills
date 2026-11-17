#!/usr/bin/env bash
# Renders assets/app-icon/app-icon.svg into the Linux icon sizes (assets/app-icon/hicolor/)
# and the window icon (assets/app-icon/app-icon.png).
# Run it after changing the icon:  scripts/app-icon.sh
#
# Uses the first renderer it finds: rsvg-convert (apt install librsvg2-bin), resvg, inkscape,
# ImageMagick, or gdk-pixbuf-thumbnailer (present on GNOME desktops).
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
dir="$root/assets/app-icon"
svg="$dir/app-icon.svg"
# The file name is the app id, read from crates/brand so the name stays in one place.
id="$(sed -n 's/^pub const MACHINE_NAME: &str = "\(.*\)";/\1/p' "$root/crates/brand/src/lib.rs")"
sizes=(16 32 48 64 128 256 512)

render() { # render <size> <out.png>
    local s="$1" out="$2"
    if command -v rsvg-convert >/dev/null; then
        rsvg-convert -w "$s" -h "$s" "$svg" -o "$out"
    elif command -v resvg >/dev/null; then
        resvg -w "$s" -h "$s" "$svg" "$out"
    elif command -v inkscape >/dev/null; then
        inkscape "$svg" -w "$s" -h "$s" -o "$out" 2>/dev/null
    elif command -v magick >/dev/null; then
        magick -background none -density 384 "$svg" -resize "${s}x${s}" "$out"
    elif command -v gdk-pixbuf-thumbnailer >/dev/null; then
        gdk-pixbuf-thumbnailer -s "$s" "$svg" "$out"
    else
        echo "No SVG renderer found. Install one: sudo apt install librsvg2-bin" >&2
        exit 1
    fi
}

rm -rf "$dir/hicolor"
for s in "${sizes[@]}"; do
    mkdir -p "$dir/hicolor/${s}x${s}/apps"
    render "$s" "$dir/hicolor/${s}x${s}/apps/$id.png"
done
mkdir -p "$dir/hicolor/scalable/apps"
cp "$svg" "$dir/hicolor/scalable/apps/$id.svg"
# Window icon embedded by apps/*/src/main.rs (name-free, so a rename doesn't touch the code).
cp "$dir/hicolor/256x256/apps/$id.png" "$dir/app-icon.png"
echo "Icons written to assets/app-icon/hicolor/ ($id.png, ${sizes[*]} px, plus scalable)"
