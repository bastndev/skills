# Components — La Velada del Año VI

## Overview

El proyecto tiene 23 componentes Astro en `src/components/`, 9 secciones en `src/sections/`, y 1 layout en `src/layouts/`. Todos son componentes Astro puros (`.astro`) — no hay React/Vue/Svelte. La interactividad client-side se maneja con `<script>` tags inline que ejecutan TypeScript/JavaScript vanilla.

---

## Layout

### `Layout.astro`
Layout base usado por todas las páginas. Contiene `<html>`, `<head>`, `<body>`, y slots para contenido. Inyecta:
- Meta tags SEO (og:image, twitter:card, description, canonical)
- Structured data JSON-LD (variable según página)
- `@vercel/analytics` script
- `src/styles/global.css` (Tailwind)
- Font preloads (Outfit variable font)

Props: `title`, `description`, `preload`, `image`, `canonical`, `schemaOrg`, `noIndex`

---

## Sections (src/sections/)

Componentes grandes que forman secciones completas de páginas, usados principalmente en `index.astro`.

### `Header.astro`
Navegación principal del sitio. Sticky header con logo, links a `/boxeadores`, `/combates`, `/artistas`, `/pronosticos`. Botón de menú móvil. Incluye `HeaderNav.astro` component.

### `Hero.astro`
Hero section de la homepage con:
- Background image responsive (avif/webp, 3 tamaños)
- Logo de La Velada VI
- Fecha y ubicación del evento
- Botón CTA "Ver boxeadores" → `/boxeadores`
- `BoxerSelector.astro` embebido (el grid interactivo de boxeadores)

### `Podcast.astro`
Sección que muestra episodios recientes del podcast usando **Content Collection** `podcast`. Fetcha datos del RSS de YouTube via el loader en `content.config.ts`. Carousel horizontal con thumbnails de videos (avif/webp optimizadas). Link a canal de YouTube.

### `Videos.astro`
Galería de videos de entrenamientos y pesajes. Grid responsive con thumbnails + play button overlay. Videos embebidos en modals (probablemente, por el tamaño del componente).

### `Sponsors.astro`
Grid de logos de sponsors (Coca-Cola, Spotify, Revolut, McDonald's, etc.). SVGs importados desde `src/assets/sponsors/`. Incluye banners de Revolut y Alsa como webp images.

### `Map.astro`
Mapa interactivo de ubicación del evento (Estadio La Cartuja, Sevilla). Probablemente usa un iframe de Google Maps o similar + info de dirección y cómo llegar.

### `Schedules.astro`
Horarios del evento. Lista de combates con hora de inicio de cada uno. Data desde `src/consts/battles.ts` + `EVENT_HOUR` de `event.ts`.

### `FAQ.astro`
Sección de preguntas frecuentes. Data desde `src/consts/home-faq.ts`. Accordion expandible (script para toggle de open/close).

### `Footer.astro`
Footer del sitio con links a redes sociales, copyright, link a GitHub del proyecto. Logos SVG de redes desde `src/assets/svg/`.

---

## Prediction System (src/components/)

8 componentes que forman el sistema de pronósticos de combates.

### `PredictionVoteController.astro` (24KB)
**Controlador principal** del sistema de predicciones. Maneja:
- Estado de votos del usuario (lee config desde `<script type="application/json">`)
- POST a `/api/predictions` cuando el usuario vota
- Actualización de UI con nuevos porcentajes tras votar
- Animación de "reacción" visual (avatar + confetti con `canvas-confetti` al completar todas las predicciones)
- Announcer para lectores de pantalla (aria-live)

Props: `isLoggedIn`, `userVotes`, `user`

### `PredictionOption.astro` (12KB)
Una opción votable en un combate (un boxeador). Muestra:
- Foto del boxeador
- Nombre, país (flag), peso
- Barra de progreso con % de votos
- Estado selected/hover
- Botón de voto (disabled si no está loggeado)

Interactividad: click para votar, hover effects, animaciones de transición.

### `PredictionFight.astro`
Contenedor de un combate en la página de pronósticos. Renderiza 2 `PredictionOption` (uno por boxeador). Incluye título del combate y separador "VS".

### `PredictionShareController.astro`
Controlador para compartir predicciones. Botón "Compartir" que abre `PredictionShareModal`. Genera una imagen OG dinámica con las predicciones del usuario (via `lib/share-image.ts`).

### `PredictionShareModal.astro` (26KB)
Modal que muestra al hacer clic en "Compartir". Contiene:
- Preview de la imagen de share
- Botones para copiar link, compartir en Twitter/X, descargar imagen
- Close button
- Lógica de apertura/cierre via script

### `PredictionStats.astro`
Muestra estadísticas globales de predicciones (total de votos, predicción más popular, etc.). Recibe data de predicciones como prop.

### `PredictionHero.astro`
Hero mini de la página `/pronosticos`. Título + descripción de la sección.

### `PredictionsBackground.astro`
Fondo decorativo animado para la página de pronósticos. Probablemente un gradiente o pattern SVG.

---

## Boxer Components (src/components/)

6 componentes relacionados con boxeadores.

### `BoxerSelector.astro` (66KB — el más grande)
**Grid interactivo de 20 boxeadores** (10 parejas) en la homepage. Layout responsive:
- Mobile: 4 cols × 5 filas
- Tablet: 8 cols × 3 filas  
- Desktop: 10 cols × 2 filas

Features:
- Posicionamiento simétrico de parejas (espejo horizontal)
- Hover: resalta al boxeador + su rival
- Click: navega a `/boxeadores/[id]`
- Imágenes optimizadas (avif/webp, 2 resoluciones por boxeador)
- Mirrors horizontal de algunos boxeadores (`MIRRORED_BOXER_IDS`: clersss, alondrissa) para que "miren" al rival

Script de ~1000 líneas con event listeners y manipulación de clases CSS.

### `BoxerGallery.astro` (9KB)
Galería de fotos de un boxeador. Carousel horizontal con thumbnails. Usado en páginas individuales de boxeador (`/boxeadores/[id]`).

### `BoxerWorkoutVideos.astro` (14KB)
Sección de videos de entrenamientos de un boxeador. Similar a `Videos.astro` pero filtrado por boxeador. Grid de thumbnails + play overlay.

### `BoxerHeroStatsCard.astro`
Card con estadísticas de un boxeador en su página individual (altura, peso, alcance, record de peleas). Data desde `src/consts/boxers.ts`.

### `BoxerSocials.astro`
Links a redes sociales de un boxeador (Instagram, TikTok, YouTube, Twitch, X). Iconos SVG + links externos.

### `BoxerWinsBadge.astro` (7KB)
Badge decorativo que muestra el número de victorias de un boxeador. Animación de entrada.

---

## Combat Components (src/components/combat/)

5 componentes para páginas de combates individuales (`/combate/[id]`).

### `CombatHero.astro` (11KB)
Hero de página de combate. Muestra:
- Nombres de los 2 boxeadores
- Fotos hero-size
- "VS" animado
- Fecha y hora del combate
- Botón CTA "Hacer pronóstico" → `/pronosticos`

### `CombatStatsSection.astro` (11KB)
Comparación lado a lado de stats de ambos boxeadores (peso, altura, alcance, récord). Tabla responsive.

### `CombatHeroVideo.astro`
Video hero del combate (probablemente promo o face-to-face). Thumbnail + play button overlay, abre video embebido.

### `CombatFaceToFaceVideoSection.astro` (6KB)
Sección de video face-to-face (pesaje o confrontación pre-combate). Similar a `CombatHeroVideo` pero en una sección separada de la página.

### `CombatPredictionsSection.astro`
Wrapper para mostrar predicciones en página de combate. Embebe componentes del Prediction System.

---

## Shared UI Components (src/components/)

Componentes pequeños y reutilizables.

### `CombatCard.astro` (9KB)
Card de combate para la página `/combates`. Muestra:
- Thumbnails de ambos boxeadores
- Nombres
- "VS" separator
- Link a `/combate/[id]`

Hover effects y animaciones.

### `AuthButton.astro` (4KB)
Botón de login/logout con OAuth (Twitch/Google). Muestra estado del usuario (avatar + nombre si está loggeado). Usado en header y página de pronósticos.

Script: maneja clicks, redirect a `/api/auth/[provider]`, logout.

### `HeaderNav.astro` (5KB)
Componente de navegación móvil (menú hamburguesa). Slide-in panel con links. Usado dentro de `Header.astro`.

### `CountryFlag.astro`
Renderiza un emoji de bandera dado un código de país (ISO 3166-1 alpha-2). Usado en cards de boxeadores.

Props: `country` (string, e.g. "ES", "MX", "AR")

### `SectionTitle.astro`
Título de sección estilizado. Tipografía grande + animación de fade-in.

Props: `title` (string)

### `SectionHeader.astro`
Header de sección con título + subtítulo opcional. Usado en `Podcast.astro`, `Videos.astro`.

Props: `title`, `subtitle?`

### `SectionDivider.astro`
Separador visual entre secciones (línea decorativa o espacio).

### `ThumbnailPlaceholder.astro`
Placeholder para thumbnails de video mientras cargan. Skeleton loader con gradiente animado.

---

## Notes on Component Size

- **BoxerSelector.astro** (66KB): El componente más grande, contiene toda la lógica de interacción del grid. Candidato a split en subcomponentes.
- **PredictionShareModal.astro** (26KB): Modal complejo con múltiples métodos de compartir. Podría extraerse lógica a `lib/`.
- **PredictionVoteController.astro** (24KB): Controlador de estado complejo. Un signal library simplificaría este código.
- **BoxerWorkoutVideos.astro** (14KB): Grid de videos con lazy loading. Bastante denso.

El resto de componentes son <10KB, tamaño razonable.

---

## Patterns Observed

1. **No client-side framework**: Todo es Astro components con `<script>` tags. Los scripts usan `$ / $$` (custom wrappers de `querySelector`) en lugar de `document.querySelector` directamente (regla de `AGENTS.md`).

2. **Props typing**: Todos los componentes definen un `interface Props` en el frontmatter con TypeScript types.

3. **Image optimization**: Todas las imágenes usan `<picture>` con sources avif/webp y fallback. URLs desde `cdn.infolavelada.com` (R2). No usa `astro:assets` (las imágenes se optimizan en build scripts, no en runtime).

4. **Accessibility**: Uso consistente de `aria-label`, `aria-live`, `role="status"`, `<sr-only>` classes para lectores de pantalla. Buttons semánticos (`<button type="button">`), links con descriptive text.

5. **Data from consts**: Casi todos los componentes importan data desde `src/consts/*.ts` en lugar de props. Los datos del evento están centralizados ahí.

6. **No slot composition**: Los componentes no usan `<slot>` de Astro frecuentemente. La mayoría reciben data via props y renderizan todo internamente. Solo `Layout.astro` y algunos wrappers usan slots.
