# Paquetes — novatech-landing

## Dependencies

No hay dependencies. El proyecto no tiene dependencias de runtime.

## devDependencies

| Paquete | Versión | Uso en este proyecto |
|---------|---------|---------------------|
| `typescript` | ^5.6.3 | Compilación y type-checking de TypeScript (`tsc --noEmit`) |
| `vite` | ^5.4.10 | Bundler y dev server. Sirve `index.html` como punto de entrada, procesa `src/main.ts` como ES module |

## Common needs check

| Necesidad | ¿Qué lo maneja? |
|-----------|------------------|
| Dark/light mode (theming) | No implementado. El sitio tiene un solo tema oscuro (colores hardcodeados en CSS variables). No hay toggle ni detección de prefers-color-scheme. |
| State management | No aplica. No hay framework de componentes ni estado compartido. El único estado es el idioma actual en localStorage. |
| Forms & validation | Implementación manual en `src/main.ts:506-572`. Validación client-side con regex para email, longitud mínima para mensaje. Sin librería de forms. |
| Routing/navigation | Smooth scroll manual con `window.scrollTo()` en `src/main.ts:377-393`. Sin router library. |
| Animations | Implementación propia con IntersectionObserver (`src/main.ts:439-450`). Animaciones CSS keyframes en `style.css`. Sin librería de animaciones. |
| Internationalization (i18n) | Sistema manual: objeto `translations` con EN/ES en `src/main.ts:12-289`, función `setLanguage()` que recorre `data-i18n` attributes. Sin librería i18n. |
| Data fetching/caching | No aplica. No hay llamadas a APIs ni fetching de datos. Todo el contenido está estático en el HTML. |
| Testing | No configurado. Directorio `__test__/` existe pero sin runner ni configuración de tests. |
| Linting/formatting | No configurado. No hay ESLint, Prettier, ni scripts de lint/format en package.json. |
