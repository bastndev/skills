# {{DISPLAY_NAME}}

{{DESCRIPTION}}

Stack: Rust + [egui](https://github.com/emilk/egui) / eframe 0.37.

## Run

```sh
cargo run
```

The first build downloads and compiles egui and takes a few minutes; later builds take seconds.

## Check before committing

```sh
cargo fmt --check
cargo clippy --all-targets -- -D warnings
cargo test
```

## Layout

Programs live in `apps/`, libraries in `crates/`. See [ARCHITECTURE.md](ARCHITECTURE.md) for the
full project tree and the layer rules.

## Where the name appears

Renaming the product means changing these, and nothing else:

- `crates/brand/src/lib.rs`: display name, machine name, GitHub repository
- `apps/{{MACHINE_NAME}}/`: the folder name and `name` in its `Cargo.toml`
- `Cargo.toml`: `repository`
- `README.md`, `AGENTS.md`, `ARCHITECTURE.md`, `LICENSE`

## License

MIT, see [LICENSE](LICENSE).
