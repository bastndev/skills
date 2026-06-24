# Mobile projects — what to check

Covers React Native (bare), Expo, and Lynx JS (ByteDance's cross-platform
engine). If you're unsure how a specific Lynx JS convention works, it's a
newer framework — say so plainly rather than guessing, and a quick web search
of its docs is reasonable if available.

## Framework & tooling
- **Bare React Native** vs **Expo** (check for `app.json`/`app.config.js`,
  `expo` in dependencies) vs **Lynx JS**.
- Expo specifically: managed vs bare workflow, which Expo SDK version, which
  `expo-*` modules are used and for what.

## Navigation
React Navigation (stack/tab/drawer config) vs Expo Router (file-based) vs a
custom solution. How screens are organized and how params are passed between
them.

## Native code
Check `ios/` and `android/` folders for custom native modules or
configuration beyond the default template — this is often where the real
complexity lives and is easy to miss if you only read JS files.

## State management
Redux/Redux Toolkit, Zustand, MobX, Context, or a custom store — and whether
it's global or scoped per-screen.

## Styling
`StyleSheet.create`, NativeWind/Tailwind, styled-components, or inline
styles. Note any shared theme/design-token file.

## Platform-specific code
`.ios.js`/`.android.js` file splits, `Platform.select`/`Platform.OS` checks —
worth noting where and why platform branching happens.

## Build & distribution
EAS Build (Expo), Fastlane, manual Gradle/CocoaPods config — and whether
there's CI wired to it.
