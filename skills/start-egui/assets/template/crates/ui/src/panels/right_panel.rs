//! Right panel: details about the selection (properties, inspector, outline…).

use eframe::egui;

pub fn show(ui: &mut egui::Ui, selected: Option<&str>) {
    ui.heading("Right panel");
    ui.separator();

    match selected {
        Some(item) => ui.label(format!("Selected: {item}")),
        None => ui.weak("Nothing selected"),
    };
}
