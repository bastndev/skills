# Packages — astro-test

## dependencies

### astro · ^6.3.6
Framework web para construir sitios estáticos y renderizados en el servidor. Se usa como base del proyecto para el sistema de routing file-based, compilación de componentes `.astro`, y generación de HTML estático.

### fixnow · ^2.0.4
Herramienta de corrección tipográfica automática para múltiples idiomas. **No se detectó uso real en el código actual** — está listado como dependencia pero no hay imports ni referencias en los archivos del proyecto.

---

## devDependencies

*(Este proyecto no tiene devDependencies)*

---

## Verificación de necesidades comunes

### Dark/light mode (theming)
**No implementado.** El proyecto usa un único tema claro definido en CSS variables (`:root`). No hay detección de `prefers-color-scheme` ni toggle manual de tema.

### State management
**No necesario.** Al ser una página completamente estática sin interactividad del lado del cliente, no hay estado reactivo que gestionar. Los datos (array de teléfonos) son estáticos y se procesan en build time.

### Forms & validation
**No implementado.** No hay formularios en el proyecto. El botón "Add to cart" es un `<button>` sin funcionalidad asociada.

### Routing/navigation
**File-based routing de Astro.** El framework maneja el routing automáticamente basándose en la estructura de archivos en `src/pages/`. La navegación interna usa hash links estándar (`#shop`, `#about`).

### Animations
**Transiciones CSS básicas.** Se usan `transition` en `.bento-card:hover` (transform, box-shadow) y botones (background-color, color). No hay animaciones complejas ni librería dedicada.

### Internationalization (i18n)
**No implementado.** El sitio está hardcodeado en inglés (`lang="en"`). No hay soporte para múltiples idiomas ni detección de locale.

### Data fetching/caching
**No aplica.** No hay llamadas a APIs ni fetch de datos dinámicos. Los datos (productos) están hardcodeados en el componente. Las imágenes se cargan de Unsplash vía URLs directas.

### Testing
**No configurado.** No hay test runner, archivos de test, ni scripts de testing en `package.json`. No se detectaron frameworks como Vitest, Jest o Playwright.

### Linting/formatting
**No configurado.** No hay ESLint, Prettier, ni otros linters/formatters. No existen archivos de configuración (`.eslintrc`, `.prettierrc`) ni scripts de lint/format en `package.json`.
