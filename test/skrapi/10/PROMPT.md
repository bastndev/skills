# Prompts — astro-test

## 🏗️ Arquitectura

Este proyecto sigue una arquitectura de sitio estático (SSG) con Astro, sin adaptadores ni backend. Todo el contenido se genera en build-time con componentes single-file (HTML + JS + CSS en el mismo archivo `.astro`), usando CSS variables para el sistema de diseño y datos hardcodeados en el frontmatter.

```
Create an Astro project with static site generation (SSG), no adapter or backend. Use single-file components where HTML, JavaScript frontmatter, and scoped CSS coexist in .astro files. Implement a design system using CSS custom properties (variables) for spacing, colors, and typography. Store page data as static arrays directly in the component's frontmatter. Configure TypeScript with strict mode, use Bun as the package manager, and set the minimum Node.js version to 22.12.0 in package.json engines. Keep the project minimal with no additional integrations or frameworks—just Astro core for build-time rendering.
```

## 📦 Packages

Este proyecto usa Astro como framework principal y Bun como package manager. Solo tiene dos dependencias: `astro` (framework) y `fixnow` (no utilizado actualmente).

```
bun add astro
```

<br>

```
bun add fixnow
```

## 🤖 Skills

El proyecto tiene 6 skills instalados para herramientas de AI: auth0-quickstart (integración Auth0), bun (documentación de Bun), gpt-image-2 (generación de imágenes), improve-codebase-architecture (análisis arquitectónico), skrapi (documentación automática de arquitectura), y vercel-react-best-practices (optimización React/Next.js).

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
