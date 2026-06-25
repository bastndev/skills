# Paquetes — astro-test

## dependencies

**astro** — ^6.3.6  
Framework principal del proyecto. Proporciona el compilador `.astro`, el sistema de routing basado en archivos, el bundler Vite integrado, y la generación de sitios estáticos. En este proyecto se usa en modo SSG puro sin adaptadores ni integraciones adicionales.

**fixnow** — ^2.0.4  
Corrector ortográfico multiidioma con diccionarios embebidos y cero dependencias en runtime. **Nota**: No se detecta ningún uso real en el código fuente de `src/` — posiblemente agregado para uso futuro o es una dependencia residual que debería eliminarse.

---

## devDependencies

_Este proyecto no tiene devDependencies._

---

## Verificación de necesidades comunes

**Dark/light mode (theming)**  
No implementado. El sitio usa un esquema de colores fijo definido con CSS variables en `:root` (gris/zinc palette). No hay toggle ni detección de preferencia del sistema.

**Gestión de estado**  
No aplica. El sitio es completamente estático sin interactividad client-side. Los datos de productos están hardcodeados en el archivo `.astro`.

**Formularios y validación**  
No implementado. No hay formularios en el sitio — los botones "Add to cart" son elementos `<button>` sin funcionalidad asociada.

**Routing/navegación**  
Manejado nativamente por Astro con routing basado en archivos. La navegación interna usa hash links (`#shop`, `#about`) dentro de la misma página — no hay navegación entre múltiples rutas.

**Animaciones**  
CSS nativo únicamente. Transiciones simples en hover (`transform`, `box-shadow`) definidas con `transition` en `.bento-card`. No hay librería de animaciones (Framer Motion, GSAP, etc.).

**Internacionalización (i18n)**  
No implementado. El sitio está completamente en inglés sin soporte multi-idioma.

**Data fetching/caching**  
No aplica. Sin llamadas a APIs, sin fetch, sin endpoints dinámicos. Todo el contenido es estático en build-time.

**Testing**  
No configurado. Sin dependencias de testing (Vitest, Jest, Playwright), sin scripts `test` en `package.json`.

**Linting/formatting**  
No configurado. Sin ESLint, sin Prettier, sin scripts `lint` o `format` en `package.json`.
