# Arquitectura — novatech-landing

## Resumen

Landing page de una empresa de desarrollo de apps móviles enfocada en Latinoamérica. Es un sitio de una sola página (SPA) construido con Vite y TypeScript vanilla, sin framework de componentes. La arquitectura se define por tres decisiones clave: CSS puro con custom properties para todo el diseño, un sistema de internacionalización (i18n) manual con atributos `data-i18n`, y animaciones basadas en IntersectionObserver sin librerías externas.

## Stack

- **Bundler**: Vite 5.4 (configuración por defecto, sin `vite.config.*`)
- **Lenguaje**: TypeScript 5.6 (strict mode deshabilitado)
- **Framework**: Ninguno — JavaScript vanilla con patrón IIFE
- **Estilos**: CSS puro con custom properties (1737 líneas)
- **Runtime**: Navegador moderno (target ES2020)

## Estructura de directorios

```
novatech-landing/
├── index.html          — Punto de entrada HTML (396 líneas), secciones: hero, services, about, process, contact, footer
├── src/
│   ├── main.ts         — Toda la lógica JS (673 líneas, IIFE): i18n, navegación, formularios, animaciones
│   ├── style.css       — Estilos completos del sitio (1737 líneas)
│   ├── shared/         — Directorio vacío (sin uso)
│   └── __test__/       — Archivos de prueba (karla.ts, sarita.ts)
├── assets/screenshot/  — Capturas de pantalla
├── dist/               — Build output (ignorado por git)
├── .agents/skills/     — Skills de IA (solo skrapi)
└── .f1/                — Project map generado por F1
```

## Modelo de renderización / ejecución

**CSR (Client-Side Rendering)** puro. Vite sirve el `index.html` estático y carga `src/main.ts` como ES module. No hay SSR, SSG, ISR, ni server-side de ningún tipo. Todo el contenido se renderiza en el navegador después de que el JS carga.

## Navegación / Routing

Sin router. El sitio es una sola página con secciones identificadas por IDs (`#hero`, `#services`, `#about`, `#process`, `#contact`). La navegación entre secciones se hace con smooth scroll programático (offset de 80px para la navbar fija). El menú móvil se togglea con clases CSS.

## Flujo de datos y estado

- **Estado global**: Ninguno. No hay store ni estado compartido entre componentes.
- **Idioma**: Guardado en `localStorage` (`novatech-lang`). El objeto `translations` en `main.ts` contiene todas las cadenas para EN y ES. La función `setLanguage()` recorre el DOM buscando atributos `data-i18n` y reemplaza el contenido de texto.
- **Formulario de contacto**: Validación 100% client-side. No hay envío real al servidor — solo muestra feedback visual de éxito/error tras la validación.
- **Preferencia de idioma**: Persistida en localStorage, cargada al init.

## Diagrama

```mermaid
flowchart TD
    A[index.html] --> B[src/main.ts]
    B --> C{init()}
    C --> D[setLanguage - carga idioma de localStorage]
    C --> E[Event Listeners - scroll, click, form]
    D --> F[DOM traversal: data-i18n attributes]
    E --> G[IntersectionObserver - counter animation]
    E --> H[IntersectionObserver - AOS animations]
    E --> I[Scroll handler - navbar style + parallax]
    E --> J[Form validation - client-side only]
    B --> K[src/style.css]
    K --> L[Custom Properties - design tokens]
    K --> M[CSS Grid - responsive layouts]
    K --> N[CSS Animations - float, shimmer, bounce]
```

## Patrones notables

- **i18n manual sin framework**: Sistema de traducciones inline con objetos anidados y atributos `data-i18n`. Simple pero efectivo para dos idiomas. La función `t(path)` resuelve rutas como `'form.errors.name'` contra el objeto de traducciones.
- **Animaciones sin librerías**: Implementación propia de AOS (Animate On Scroll) usando IntersectionObserver. Parallax suave con requestAnimationFrame y throttle manual (`ticking` flag).
- **Accesibilidad**: Skip link, `aria-label`, `aria-expanded`, `aria-invalid`, `role="alert"` en errores de formulario, `prefers-reduced-motion` respetado.
- **Glass morphism extensivo**: Uso consistente de `backdrop-filter: blur()` y colores semitransparentes para efectos de vidrio en navbar, cards, badges y formulario.
- **CSS como design system completo**: Variables CSS para colores, gradientes, tipografía, spacing, efectos y status (error/warning/success/info). Todo el sistema de diseño vive en `:root`.
- **Responsive sin framework**: Media queries manuales en 980px y 768px. Grid-based layouts que colapsan a columna única en móvil.

## Cosas a cuestionar

- **`src/shared/` está vacío**: Directorio creado pero sin uso — posible deuda técnica o plans abandonados.
- **Archivos duplicados**: `add.css` y `global.css` no están referenciados en `index.html`. `README copy.md` y `README copy 2.md` son duplicados.
- **Sin validación de formulario en servidor**: El formulario de contacto solo valida client-side y no envía datos a ningún backend. Es puramente cosmético.
- **TODO en main.ts (línea 455)**: Comentario `// TODO: create a new function aquí` sugiere trabajo pendiente.
- **Comentario incompleto en línea 456**: `% tis is a new commmit here` parece un commit message accidental pegado en el código.
- **Sin configuración de Vite**: Usa defaults — funciona pero no hay optimizaciones específicas del proyecto (aliases, base path, build options).
- **Sin tests configurados**: El directorio `__test__/` existe pero no hay runner de tests ni configuración de testing.
- **`strict: false` en tsconfig**: TypeScript no valida tipos estrictamente, lo que reduce la seguridad de tipos.
