//! Everything that is drawn on screen lives in this crate.

mod panels;
mod update_dialog;

use eframe::egui;
use panels::{center_panel, left_panel::LeftPanel, right_panel, status_bar};
use update_dialog::{UpdateChoice, UpdateOffer};

/// The whole app's state. It lives as long as the window is open.
#[derive(Default)]
pub struct App {
    left: LeftPanel,
    /// `Some` while the update dialog is open.
    update_offer: Option<UpdateOffer>,
}

impl eframe::App for App {
    /// Called every frame: egui redraws the whole window from the state above.
    fn ui(&mut self, ui: &mut egui::Ui, _frame: &mut eframe::Frame) {
        // Edge panels first, the central panel last: it takes the space that is left.
        egui::Panel::bottom("status_bar").exact_size(26.0).show(ui, |ui| {
            if status_bar::show(ui) {
                self.update_offer = Some(UpdateOffer::fake());
            }
        });

        egui::Panel::left("left_panel")
            .resizable(true)
            .default_size(240.0)
            .min_size(160.0)
            .show(ui, |ui| self.left.show(ui));

        let selected = self.left.selected();

        egui::Panel::right("right_panel")
            .resizable(true)
            .default_size(240.0)
            .min_size(160.0)
            .show(ui, |ui| right_panel::show(ui, selected));

        egui::CentralPanel::default().show(ui, |ui| center_panel::show(ui, selected));

        if let Some(offer) = &self.update_offer
            && let Some(choice) = update_dialog::show(ui.ctx(), offer)
        {
            // The real update logic plugs in here; for now both buttons just close the dialog.
            match choice {
                UpdateChoice::Later | UpdateChoice::UpdateAndRestart => self.update_offer = None,
            }
        }
    }
}
