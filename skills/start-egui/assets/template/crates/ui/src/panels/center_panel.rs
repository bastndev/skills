//! Center panel: the app's main view (an editor, a canvas, a timeline…).

use eframe::egui;

pub fn show(ui: &mut egui::Ui, selected: Option<&str>) {
    let text = match selected {
        Some(item) => format!("{item} is open"),
        None => "Pick an item on the left".to_owned(),
    };
    ui.centered_and_justified(|ui| ui.heading(text));
}
