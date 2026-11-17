//! Starts the window. No UI code and no logic here: drawing lives in `crates/ui`.

use eframe::egui;

fn main() -> eframe::Result {
    let options = eframe::NativeOptions {
        viewport: egui::ViewportBuilder::default()
            .with_title({{CRATE_PREFIX}}_brand::DISPLAY_NAME)
            .with_app_id({{CRATE_PREFIX}}_brand::MACHINE_NAME)
            .with_inner_size([1200.0, 760.0])
            .with_min_inner_size([640.0, 400.0]),
        ..Default::default()
    };

    eframe::run_native(
        {{CRATE_PREFIX}}_brand::DISPLAY_NAME,
        options,
        Box::new(|_cc| Ok(Box::new({{CRATE_PREFIX}}_ui::App::default()))),
    )
}
