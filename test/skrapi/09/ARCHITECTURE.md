# Architecture — astro-test

## Resumen
Aplicación web minimalista construida con Astro 6.3.6 y TypeScript. Es un starter ultra-simple que muestra una tienda de móviles con diseño bento en una única página sin componentes separados, todo el código está contenido en un solo archivo `.astro` con estilos CSS inline.

## Stack
- **Framework:** Astro 6.3.6
- **Lenguaje:** TypeScript (configuración strict)
- **Runtime:** Node.js >=22.12.0
- **Package Manager:** Bun (lockfile: bun.lock)
- **Modelo de renderizado:** SSG (Static Site Generation) por defecto

## Estructura de directorios
```
/
├── public/               # Assets estáticos (favicon.ico, favicon.svg)
├── src/
│   └── pages/           # Páginas basadas en routing del filesystem
│       └── index.astro  # Única página: tienda de móviles con diseño bento
├── .astro/              # Archivos generados por Astro (types, settings)
├── .agents/skills/      # Skills para AI agents (auth0, gpt-image-2, improve-codebase-architecture, skrapi)
├── .claude/skills/      # Skills para Claude (vercel-react-best-practices, bun)
├── astro.config.mjs     # Configuración de Astro (vacía, usa defaults)
├── tsconfig.json        # Configuración TypeScript (extends astro/tsconfigs/strict)
├── package.json         # Dependencias: astro + fixnow
└── bun.lock             # Lockfile de Bun
```

## Rendering / execution model
- **Modo:** SSG (Static Site Generation) por defecto
- **Output:** HTML estático generado en `dist/` durante el build
- **Páginas:** File-based routing, cada archivo en `src/pages/` se convierte en una ruta
- **Único endpoint:** `/` (index.astro)

## Routing / navigation
- **Sistema:** File-based routing de Astro
- **Rutas:** Solo `/` (página principal)
- **Navegación interna:** Links HTML estándar con hash (`#shop`, `#about`) dentro de la misma página

## Data flow & state
- **Datos:** Array estático de teléfonos definido directamente en el frontmatter de `index.astro`
- **Estado:** No hay manejo de estado reactivo, todo es estático
- **Fetch:** No hay llamadas a APIs externas
- **Imágenes:** URLs de Unsplash hardcodeadas en el array de productos

## Diagram
```mermaid
graph LR
    A[index.astro] --> B[Build Time]
    B --> C[Static HTML]
    C --> D[/dist/index.html]
    E[phones array] --> A
    F[CSS inline] --> A
```

## Patrones notables
1. **Single-file component:** Todo (lógica, markup, estilos) está en un solo archivo `.astro`
2. **CSS Variables:** Sistema de diseño centralizado con custom properties CSS
3. **Bento Grid:** Layout responsivo usando CSS Grid con breakpoints
4. **No JavaScript runtime:** Página completamente estática, cero JS en el cliente
5. **Design tokens:** Valores de espaciado, colores y radios definidos como CSS variables

## Cosas a cuestionar
1. **Sin componentes reutilizables:** Todo el código está en un solo archivo. Para escalar, sería mejor extraer `<ProductCard>`, `<Header>`, etc.
2. **Datos hardcodeados:** El array de teléfonos está inline. En una app real, estos datos vendrían de un CMS o API.
3. **Sin sistema de estilos:** CSS está inline en el archivo. Considerar extraer a archivos `.css` separados o usar un preprocesador.
4. **Dependencia fixnow no usada:** El proyecto incluye `fixnow@^2.0.4` pero no se importa ni usa en ningún lugar del código.
5. **Skills desconectadas del código:** Hay 6 skills instaladas (auth0, arquitectura, gpt-image, etc.) pero el código actual no hace uso de ellas.
