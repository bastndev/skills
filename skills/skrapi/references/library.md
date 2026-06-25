# npm packages / libraries / CLIs — what to check

A project meant to be consumed by *other* code (or run as a CLI), rather than
shipped as an app itself.

## Entry points & exports
`main`, `module`, `exports`, `types` fields in `package.json`. The `exports`
map especially — it defines the actual public surface, which can differ from
what the source tree implies.

## Module formats
CJS only, ESM only, or dual-publish — and how that's built (conditional
exports, separate build outputs).

## Build tooling
tsup, rollup, esbuild, or Vite's library mode — and what the output looks
like (single bundle vs preserved file structure).

## Dependencies vs peerDependencies
What the package bundles itself vs what it expects the consumer to already
have installed (common for things expecting React, etc., as a peer).

## Public API surface
What's actually exported from the main entry — this is usually a small
fraction of the source tree. Worth listing explicitly since it's the part
consumers care about.

## Testing & types
Test runner used, and whether `.d.ts` files are hand-written or generated.

## Monorepo tooling (if applicable)
Changesets/semantic-release for versioning, Turborepo/Nx for task running —
worth a quick mention of how releases happen.
