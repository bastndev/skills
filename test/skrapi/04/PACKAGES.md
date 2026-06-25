# Packages — NovaTech Landing

## dependencies

No hay dependencias de producción. Todo el código es JavaScript/TypeScript vanilla.

## devDependencies

| Paquete | Versión | Uso en este proyecto |
|---|---|---|
| `vite` | ^5.4.10 | Bundler y servidor de desarrollo. Compila TypeScript, sirve el `index.html` con HMR, y genera el build de producción (`dist/`). No tiene configuración personalizada — usa defaults. |
| `typescript` | ^5.6.3 | Compilador de TypeScript. Se ejecuta con `--noEmit` (solo type-checking, sin generar JS) en el script `build` y `typecheck`. No hay config de path aliases ni proyecto complejo. |

## Common needs check

| Necesidad | Estado |
|---|---|
| **Dark/light mode (theming)** | No implementado. El sitio es solo dark mode. Los design tokens en CSS custom properties (`:root`) permitirían añadir light mode fácilmente. |
| **State management** | No aplica — no hay framework ni estado complejo. Solo `currentLang` en una variable del closure. |
| **Forms & validation** | Validación manual en cliente (`main.ts:506-572`). Sin librería — regex para email, longitud mínima para mensaje, campos requeridos. Sin backend. |
| **Routing/navigation** | Anclajes HTML (`#section`) + smooth scroll manual. Sin librería de router. |
| **Animations** | Sistema propio con `IntersectionObserver` (data-aos), `requestAnimationFrame` (parallax, counters), y CSS keyframes. Sin librería externa (no usa AOS, GSAP, Framer Motion, etc.). |
| **Internationalization (i18n)** | Implementación propia: diccionario de traducciones en JS + atributo `data-i18n` en el HTML. Soporta EN y ES. Persiste preferencia en `localStorage`. |
| **Data fetching/caching** | No aplica — no hay llamadas a APIs ni fetch de datos. |
| **Testing** | No configurado. Sin framework (Jest, Vitest, Playwright, etc.), sin tests escritos, sin script `test`. |
| **Linting/formatting** | No configurado. Sin ESLint, sin Prettier, sin `lint` ni `format` script. |
