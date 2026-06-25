# Paquetes — astro-test

## Dependencies

| Paquete | Versión | Descripción en este proyecto |
|---------|---------|------------------------------|
| `astro` | ^6.3.6 | Framework principal — genera el sitio estático con SSG, enrutamiento por archivos, y CSS scoped por componente |
| `fixnow` | ^2.0.4 | Spell checker multilingüe con sugerencias. **No se usa en ningún archivo del proyecto** — dead weight en dependencies |

## devDependencies

No hay devDependencies configuradas en este proyecto.

---

## Comprobación de necesidades comunes

| Necesidad | Paquete / Solución |
|-----------|---------------------|
| Dark/light mode (theming) | No implementado — solo esquema de colores claro definido en custom properties |
| State management | No aplica — sitio estático sin estado dinámico |
| Formularios y validación | No hay formularios funcionales |
| Enrutamiento/navegación | Astro file-based routing (una sola ruta: `/`) |
| Animaciones | CSS transitions (180ms ease) para hover en cards y botones |
| Internacionalización (i18n) | No implementado |
| Obtención de datos/caché | No aplica — datos hardcodeados en frontmatter |
| Testing | No configurado — sin framework de testing |
| Linting/formatting | No configurado — sin ESLint ni Prettier |
