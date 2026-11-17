//! Left panel: a list to pick from. Becomes files, layers, tracks… depending on the app.

use eframe::egui;

const ITEMS: &[&str] = &["First item", "Second item", "Third item", "Fourth item"];

#[derive(Default)]
pub struct LeftPanel {
    /// Index into `ITEMS` of the selected item, if any.
    selected: Option<usize>,
}

impl LeftPanel {
    pub fn show(&mut self, ui: &mut egui::Ui) {
        ui.heading("Left panel");
        ui.separator();

        egui::ScrollArea::vertical().auto_shrink(false).show(ui, |ui| {
            for (index, item) in ITEMS.iter().enumerate() {
                if ui.selectable_label(self.selected == Some(index), *item).clicked() {
                    self.selected = Some(index);
                }
            }
        });
    }

    pub fn selected(&self) -> Option<&'static str> {
        self.selected.map(|index| ITEMS[index])
    }
}
