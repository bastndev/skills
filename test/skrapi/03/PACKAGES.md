# Packages — NovaTech Landing

## dependencies

No hay dependencias de producción. Este proyecto no usa librerías externas en runtime.

## devDependencies

| Package | Versión | Uso en este proyecto |
|---|---|---|
| `typescript` | ^5.6.3 | Compilación de TypeScript a JavaScript. Configurado con `strict: false` y `module: ESNext`. |
| `vite` | ^5.4.10 | Build tool y servidor de desarrollo. Configuración por defecto (sin `vite.config.*`). |

## Common needs check

| Necesidad | ¿Cómo se resuelve? |
|---|---|
| **Dark/light mode (theming)** | No implementado. Solo existe un tema oscuro (colores definidos en CSS variables). |
| **State management** | No aplica. El estado es trivial: idioma actual en `localStorage` y variables locales. |
| **Forms & validation** | Validación manual en `main.ts:506-573`. Sin librería externa — regex para email, min-length para mensaje, campos requeridos. |
| **Routing/navigation** | No aplica. Página estática de una sola vista con scroll suave a anclajes. |
| **Animations** | Implementación custom con IntersectionObserver. Sin librería externa (no usa AOS, GSAP, ni Framer Motion). |
| **Internationalization (i18n)** | Sistema manual: objeto `translations` con idiomas EN/ES, atributos `data-i18n`, función `setLanguage()`. |
| **Data fetching/caching** | No aplica. No hay peticiones a APIs ni fetching de datos. |
| **Testing** | No configurado. Existe `src/__test__/` pero está vacío. No hay framework de testing ni script de test. |
| **Linting/formatting** | No configurado. No hay ESLint, Prettier, ni scripts de lint/format. |
