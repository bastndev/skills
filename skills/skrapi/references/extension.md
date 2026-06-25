# Browser extensions — what to check

Identified by a `manifest.json` with a `manifest_version` field.

## Manifest
`manifest_version` (2 vs 3 — this changes a lot about what's possible),
`permissions` vs `host_permissions`, declared entry points.

## Background context
Manifest V3: service worker (non-persistent, can't hold long-lived state in
memory without `chrome.storage`). Manifest V2: persistent background page.
Note which, since it explains a lot of the message-passing code.

## Content scripts
Which pages they're injected into (`matches`), isolated world vs main world,
what they actually do (DOM manipulation, scraping, injecting UI).

## Popup / options / side panel UI
How it's built — plain HTML/JS, or a full framework (React/Vue/Svelte)
bundled in.

## Messaging
How background, content scripts, and popup talk to each other —
`chrome.runtime.sendMessage`, ports, or a wrapper library.

## Storage
`chrome.storage.local`/`sync`, IndexedDB, or just in-memory (and therefore
lost when the service worker sleeps).

## Build tooling
Webpack, Vite, or a purpose-built extension bundler (e.g. CRXJS) — and how
multiple entry points (background/content/popup) map to the manifest.
