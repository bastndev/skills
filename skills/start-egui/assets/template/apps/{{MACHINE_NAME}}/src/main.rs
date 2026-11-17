//! Starts the window. No UI code and no logic here: drawing lives in `crates/ui`.

use eframe::egui;

/// Window icon, rendered by `scripts/app-icon.sh`. Shown on Windows, macOS and X11; on Wayland the
/// desktop takes the icon from the `.desktop` file that matches the app id instead.
const ICON_PNG: &[u8] = include_bytes!("../../../assets/app-icon/app-icon.png");

fn main() -> eframe::Result {
    let mut viewport = egui::ViewportBuilder::default()
        .with_title({{CRATE_PREFIX}}_brand::DISPLAY_NAME)
        // Must match the installed .desktop file name (<app id>.desktop), or the Linux dock shows
        // this raw id and a generic icon.
        .with_app_id({{CRATE_PREFIX}}_brand::MACHINE_NAME)
        .with_inner_size([1200.0, 760.0])
        .with_min_inner_size([640.0, 400.0]);
    if let Ok(icon) = eframe::icon_data::from_png_bytes(ICON_PNG) {
        viewport = viewport.with_icon(icon);
    }

    eframe::run_native(
        {{CRATE_PREFIX}}_brand::DISPLAY_NAME,
        eframe::NativeOptions {
            viewport,
            ..Default::default()
        },
        Box::new(|_cc| Ok(Box::new({{CRATE_PREFIX}}_ui::App::default()))),
    )
}
