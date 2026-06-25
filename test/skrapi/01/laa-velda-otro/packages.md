# Packages — La Velada del Año VI

## Dependencies

### Framework & Core

- **astro** `6.4.7` — Framework principal, usado en modo SSR con islands architecture. Todas las páginas y componentes son `.astro` files.
- **@astrojs/vercel** `10.0.8` — Adapter para desplegar en Vercel como serverless functions. Configurado en `astro.config.mjs` como `adapter: vercel()`.
- **@astrojs/react** `5.0.7` — Integración de React, pero **no se usa en el código actual** (no hay archivos `.jsx`/`.tsx` en src). Instalado pero sin aprovechar.
- **@astrojs/sitemap** `3.7.3` — Genera `sitemap.xml` automáticamente desde las rutas. Configurado en `integrations: [sitemap()]`.

### Styling

- **tailwindcss** `4.3.0` — Sistema de utilidades CSS, toda la UI usa clases Tailwind.
- **@tailwindcss/vite** `4.3.0` — Plugin Vite para Tailwind 4, reemplaza el PostCSS plugin tradicional. Configurado en `vite.plugins`.
- **tailwind-animations** `1.0.1` — Presets de animaciones para Tailwind (fade-in, slide-up, etc.). Usado en componentes como Hero y Predictions.

### Database & Auth

- **@libsql/client** `0.17.3` — Cliente para Turso (LibSQL serverless DB). Usado en `lib/database.ts` para queries SQL de predicciones.
- **better-auth** `^1.6.15` — Sistema de autenticación con OAuth providers. Configurado en `lib/auth.ts` con Twitch y Google. Maneja sessions via middleware.

### UI & Interactivity

- **react** `19.2.6` + **react-dom** `19.2.6` — Instalados por la integración de React, pero no se usan activamente en el proyecto.
- **canvas-confetti** `1.9.4` — Efecto de confetti usado en `PredictionVoteController.astro` cuando el usuario completa todos los pronósticos.
- **@lucide/astro** `1.14.0` — Librería de iconos. Usado en componentes como `HeaderNav.astro` para iconos SVG (menu, close, etc.).

### Analytics & Monitoring

- **@vercel/analytics** `2.0.1` — Tracking de pageviews y eventos en Vercel Analytics. Inyectado en `Layout.astro`.

## DevDependencies

### TypeScript & Types

- **@typescript-eslint/parser** `8.59.3` — Parser TypeScript para ESLint. Configurado en `eslint.config.js`.
- **@types/react** `19.2.14` + **@types/react-dom** `19.2.3` + **@types/canvas-confetti** `1.9.0` — Type definitions para las libs de React y canvas-confetti.

### Linting & Formatting

- **eslint** `10.3.0` — Linter JavaScript/TypeScript. Script: `pnpm lint`.
- **eslint-plugin-astro** `1.7.0` — Reglas ESLint específicas para archivos `.astro`. Lee `AGENTS.md` para reglas custom del proyecto.
- **prettier** `3.8.3` — Formatter de código. Configurado con `.prettierrc`.
- **prettier-plugin-astro** `0.14.1` — Plugin para formatear archivos `.astro`.
- **prettier-plugin-tailwindcss** `0.8.0` — Ordena clases Tailwind automáticamente según orden recomendado.

### Build & Image Processing

- **sharp** `0.34.5` — Procesamiento de imágenes en build scripts (`scripts/generate-thumbnails.mjs`, `generate-blur-placeholders.mjs`). Redimensiona y optimiza webp.
- **png-to-ico** `3.0.1` — Convierte PNG a ICO. Usado en `scripts/generate-favicon.mjs`.
- **aws4fetch** `^1.0.20` — Cliente HTTP con signing AWS V4. Usado en `scripts/upload-to-r2.mjs` para subir assets a Cloudflare R2 (compatible con S3 API).

---

## Common needs check

### Dark/light mode (theming)
**No implementado.** La web usa un tema oscuro fijo definido en `src/styles/global.css`. No hay toggle ni detección de `prefers-color-scheme`. Todas las páginas son dark mode 100% del tiempo.

### State management
**No hay librería.** Todo el estado es server-side (`Astro.locals.user` via middleware) o DOM-local (variables en `<script>` tags de componentes). Ver `architecture.md` para detalles.

### Forms & validation
**No hay librería.** Las predicciones usan un `<form>` con `preventDefault()` + `fetch()` manual en `PredictionVoteController.astro`. No hay validación client-side más allá de checks básicos en el script.

### Routing/navigation
**File-based routing de Astro.** No necesita librería externa. Las rutas se definen con archivos en `src/pages/`. No usa `@astrojs/react-router` ni nada adicional.

### Animations
**tailwind-animations** `1.0.1` — Proporciona clases como `.animate-fade-in`, `.animate-slide-up`. Usado en Hero, Podcast section, Predictions. No hay Framer Motion ni GSAP.

### Internationalization (i18n)
**No implementado.** La web está 100% en español. No usa `astro:i18n` routing ni `@astrojs/i18n`. Los textos están hardcodeados en componentes y en `src/consts/*.ts`.

### Data fetching/caching
**Custom cache en memoria.** `src/lib/predictions.ts` implementa un cache manual con TTL de 30s usando un objeto global. El fetching es con `fetch()` directo a Turso (via `@libsql/client`). No usa React Query, SWR, ni TanStack Query (de hecho, React no se usa en modo hidratado).

### Testing
**No hay framework de testing.** Cero archivos `.test.ts` o `.spec.ts`. No usa Vitest, Jest, Playwright, ni Cypress. Los scripts en `scripts/` tienen nombres como `test-predictions.mjs` pero solo son scripts de validación manual, no tests automatizados.

### Linting/formatting
- **ESLint** `10.3.0` con `eslint-plugin-astro` — Linting de `.astro` files.
- **Prettier** `3.8.3` con plugins de Astro y Tailwind — Formatting automático.
- Scripts: `pnpm lint` (check), `pnpm lint:fix` (autofix).
