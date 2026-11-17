#!/usr/bin/env bash
# Renders assets/app-icon/app-icon.svg into the Linux icon sizes (assets/app-icon/hicolor/)
# and the window icon (assets/app-icon/app-icon.png).
# Run it after changing the icon:  scripts/app-icon.sh
#
# Uses the first renderer it finds: rsvg-convert (apt install librsvg2-bin), resvg, inkscape,
# ImageMagick, or gdk-pixbuf-thumbnailer (present on GNOME desktops). Without one, or if a
# size fails to render, the icons already in the folder are left untouched.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
dir="$root/assets/app-icon"
svg="$dir/app-icon.svg"
# The file name is the app id, read from crates/brand so the name stays in one place.
id="$(sed -n 's/^pub const MACHINE_NAME: &str = "\(.*\)";/\1/p' "$root/crates/brand/src/lib.rs")"
sizes=(16 32 48 64 128 256 512)

renderer=""
for candidate in rsvg-convert resvg inkscape magick gdk-pixbuf-thumbnailer; do
    if command -v "$candidate" >/dev/null; then
        renderer="$candidate"
        break
    fi
done
if [ -z "$renderer" ]; then
    echo "No SVG renderer found, so the icons were left as they are." \
        "Install one: sudo apt install librsvg2-bin" >&2
    exit 1
fi

render() { # render <size> <out.png>
    local s="$1" out="$2"
    case "$renderer" in
        rsvg-convert) rsvg-convert -w "$s" -h "$s" "$svg" -o "$out" ;;
        resvg) resvg -w "$s" -h "$s" "$svg" "$out" ;;
        inkscape) inkscape "$svg" -w "$s" -h "$s" -o "$out" 2>/dev/null ;;
        magick) magick -background none -density 384 "$svg" -resize "${s}x${s}" "$out" ;;
        gdk-pixbuf-thumbnailer) gdk-pixbuf-thumbnailer -s "$s" "$svg" "$out" ;;
    esac
    if [ ! -s "$out" ]; then
        echo "$renderer did not render the ${s}px icon, so the icons were left as they are." >&2
        exit 1
    fi
}

# Render into a temporary folder; replace the icons only once every size worked.
tmp="$(mktemp -d "$dir/.render.XXXXXX")"
trap 'rm -rf "$tmp"' EXIT
for s in "${sizes[@]}"; do
    mkdir -p "$tmp/hicolor/${s}x${s}/apps"
    render "$s" "$tmp/hicolor/${s}x${s}/apps/$id.png"
done
mkdir -p "$tmp/hicolor/scalable/apps"
cp "$svg" "$tmp/hicolor/scalable/apps/$id.svg"

rm -rf "$dir/hicolor"
mv "$tmp/hicolor" "$dir/hicolor"
# Window icon embedded by apps/*/src/main.rs (name-free, so a rename doesn't touch the code).
cp "$dir/hicolor/256x256/apps/$id.png" "$dir/app-icon.png"
echo "Icons written to assets/app-icon/hicolor/ ($id.png, ${sizes[*]} px, plus scalable) with $renderer"
