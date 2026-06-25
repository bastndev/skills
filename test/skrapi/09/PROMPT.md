# Prompts — astro-test

## 🏗️ Architecture

Este proyecto usa una arquitectura **single-file component** donde toda la lógica, markup y estilos viven en un único archivo `.astro`. Es un patrón común en proyectos de demostración o MVPs ultra-simples, pero no escala bien cuando el proyecto crece.

```
You are building a minimal Astro static site generator project with TypeScript. Follow these architectural decisions:

1. Use file-based routing: each file in src/pages/ becomes a route
2. Keep components as single .astro files until you have reusable patterns
3. Define design tokens as CSS custom properties in :root
4. Use SSG (static site generation) by default — output pure HTML with zero client-side JS unless explicitly needed
5. Structure data as static arrays in the frontmatter section (--- ... ---) of .astro files
6. Use CSS Grid for responsive layouts with mobile-first breakpoints
7. Inline styles in <style> tags within .astro files for small projects
8. Store static assets like icons and images in the public/ directory
9. Use semantic HTML and proper heading hierarchy
10. Prefer progressive enhancement: start with working HTML, add interactivity only when needed

When the project grows beyond a single page, extract reusable components to src/components/ and consider adding a content layer with Astro Content Collections or an external CMS.
```

## 📦 Packages

Este proyecto usa Astro como framework principal y Bun como package manager. Solo tiene dos dependencias: `astro` (framework) y `fixnow` (no utilizado actualmente).

```
npm i astro
```

<br>

```
npm i fixnow
```
<br>

```
npm i fixnow
```

## 🤖 Skills

Este proyecto tiene 6 skills instaladas: 4 en `.agents/skills/` (auth0-quickstart, gpt-image-2, improve-codebase-architecture, skrapi) y 2 en `.claude/skills/` (bun, vercel-react-best-practices).

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
