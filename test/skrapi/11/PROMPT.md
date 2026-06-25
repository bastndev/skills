# Prompts — astro-test

## 🏗️ Arquitectura

Este proyecto es un sitio web estático minimalista con Astro usando SSG puro, sin frameworks de componentes ni adaptador de despliegue — toda la lógica vive en un solo archivo `.astro` con datos hardcodeados y CSS vanilla tokenizado.

```
Implement a minimal static site using Astro with SSG mode (no adapter configured). Create a single-page layout where all data lives in the frontmatter of the .astro file, styled with CSS custom properties for design tokens (colors, spacing, radii). Use CSS Grid for responsive layout with breakpoints, and scoped CSS within the component. No external CSS frameworks, no React/Vue/Svelte islands, no Content Collections — keep everything in native Astro syntax with a clean bento-grid card pattern.
```

## 📦 Packages

El proyecto usa Astro 6.3.6 como framework principal con Bun como gestor de paquetes, y tiene 2 dependencias — una de ellas (`fixnow`) no está siendo utilizada en el código.

```
bun add astro
```

<br>

```
bun add fixnow
```

## 🤖 Skills

Este proyecto tiene 6 skills instalados en carpetas `.agents/skills/` y `.claude/skills/`, incluyendo skrapi como analizador de arquitectura.

<br>

⯈ **auth0-quickstart**
```
npx skills add https://github.com/auth0/agent-skills --skill auth0-quickstart
```

<br>

⯈ **bun**
```
npx skills add https://github.com/midudev/autoskills --skill bun
```

<br>

⯈ **gpt-image-2**
```
npx skills add https://github.com/doany-ai/skills --skill gpt-image-2
```

<br>

⯈ **improve-codebase-architecture**
```
npx skills add https://github.com/mattpocock/skills --skill improve-codebase-architecture
```

<br>

⯈ **skrapi**
```
npx skills add https://github.com/bastndev/skills --skill skrapi
```

<br>

⯈ **vercel-react-best-practices**
```
npx skills add https://github.com/vercel-labs/agent-skills --skill vercel-react-best-practices
```
