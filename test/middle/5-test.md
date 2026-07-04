# Editor and local workspace state
.vscode/**
.vscode-test/**
.gitignore
.vscodeignore
.yarnrc

# Exclude src/ except webview runtime assets (HTML/CSS/images); removing negations → panels render blank.
src/**
!src/shared/
!src/shared/**/
!src/shared/**/*.html
!src/shared/**/*.css
!src/shared/**/*.svg
!src/shared/**/*.png
!src/shared/**/*.webp
!src/my-skills/
!src/my-skills/**/
!src/my-skills/**/*.html
!src/my-skills/**/*.css
!src/my-skills/**/*.svg
!src/my-skills/**/*.png
!src/my-skills/**/*.webp

# Smart + Skills reads SKILL.md from src/my-plus/ at runtime (smart-service.ts → RULES_ASSET_SEGMENTS); .md only, .ts stays out.
!src/my-plus/**/*.md

# Repo-only assets (screenshots, GIFs ~13 MB) — not loaded by the extension
public/**

# Tests and generated development maps
**/__test__/**
**/__tests__/**
**/*.test.*
**/*.spec.*
**/*.ts
**/*.map

# Build, lint, typecheck, and package-manager inputs
.prettierignore
bun.lock
esbuild.js
**/eslint.config.mjs
**/tsconfig.json

# Native debug symbols — trims ~53 MB of node-pty .pdb files
**/*.pdb

# fixnow ships 8 language dicts (~11 MB); keep en/es/pt/ru only — see src/my-cli/shared/prompt/languages.ts
node_modules/fixnow/dictionaries/ar/**
node_modules/fixnow/dictionaries/de/**
node_modules/fixnow/dictionaries/fr/**
node_modules/fixnow/dictionaries/vi/**

# Project notes and contributor-only documentation
AGENTS.md
ARCHITECTURE.md
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
NOTES.md
vsc-extension-quickstart.md

# Agent/context caches and graph analysis output
.agents/**
.claude/**
.codex/**

# Local package artifacts
*.vsix
