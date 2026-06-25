# Packages — astro-test

## dependencies
- astro `^6.3.6`: framework principal que compila `src/pages/index.astro`, sirve el dev server y produce el sitio estático final.
- fixnow `^2.0.4`: está instalado en `package.json`, pero no hay referencias en `src/` ni en la configuración actual; por ahora parece una dependencia no utilizada.

## Common needs check
- Dark/light mode (theming): no hay soporte específico; la app usa un único tema definido con variables CSS en `index.astro`.
- State management: no hay librería; el estado vive en un arreglo local dentro del frontmatter.
- Forms & validation: no hay formularios ni validación.
- Routing/navigation: no hay router de paquete; Astro maneja el routing por archivos y la navegación interna usa anclas HTML.
- Animations: no hay biblioteca; sólo transiciones CSS simples en tarjetas y botones.
- Internationalization (i18n): no hay paquete de i18n ni estructura de traducción.
- Data fetching/caching: no hay cliente de fetch ni caché; los datos son locales y estáticos.
- Testing: no hay framework de pruebas instalado.
- Linting/formatting: no hay ESLint ni Prettier configurados en el repositorio actual.
