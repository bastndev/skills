//! Bottom bar: app name and version on the left, the update button on the right.

use eframe::egui;

/// Draws the bar. Returns `true` when "Check for updates" was clicked.
pub fn show(ui: &mut egui::Ui) -> bool {
    ui.horizontal_centered(|ui| {
        ui.label(format!("{} {}", {{CRATE_PREFIX}}_brand::DISPLAY_NAME, {{CRATE_PREFIX}}_brand::VERSION));

        ui.with_layout(egui::Layout::right_to_left(egui::Align::Center), |ui| {
            ui.small_button("Check for updates").clicked()
        })
        .inner
    })
    .inner
}
