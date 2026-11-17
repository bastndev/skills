# AGENTS.md

Rules for AI assistants working in this repository. `ARCHITECTURE.md` has the project tree and the full layer table.

## What this is

{{DISPLAY_NAME}}: {{DESCRIPTION}} A desktop app written in Rust with **egui/eframe 0.37**.

## Commands

- Run: `cargo run`
- A change is done only when all of these pass:
  `cargo fmt --check`, `cargo clippy --all-targets -- -D warnings`, `cargo test`

## Rules

- **Layers** (see `ARCHITECTURE.md`): egui only in `crates/ui` and `apps/`. Logic crates
  never draw.
- **The name lives in `crates/brand`.** Never hard-code the product name, repo or version elsewhere.
- **Never block the window.** Slow work (network, disk) goes on a background thread; call
  `ctx.request_repaint()` when the result arrives.
- **Few dependencies.** Justify every new crate; prefer `default-features = false`. Declare it once
  in the root `Cargo.toml` under `[workspace.dependencies]`.
- **Don't create empty crates.** A crate is created in the step that needs it.

## egui 0.37 notes

- The app implements `eframe::App::ui(&mut self, ui: &mut egui::Ui, frame)`, not `update`.
- Panels: `egui::Panel::left("id")` / `right` / `top` / `bottom`, with `.default_size()`,
  `.min_size()`, `.exact_size()`, `.resizable()`, then `.show(ui, |ui| ...)`. Add edge panels
  **before** `egui::CentralPanel`. Panels can be nested inside another panel with the same `.show(ui, ..)`.
- `egui::Id::new` is deprecated: use `egui::Id::unique(..)`.
- Dialogs: `egui::Modal::new(id).show(ctx, ..)`; `should_close()` is true on Escape or a click outside.
- When unsure, read the source in `~/.cargo/registry/src/*/egui-0.37.0/` instead of guessing.

## Working with the owner

- Keep each change small; say which files to look at and what to run.
- Ask before anything public or hard to undo: `git push`, tags, releases, installing system packages.
- Reference projects are for ideas only. Never copy their code, names, icons or art.
