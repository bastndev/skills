# Prompts — astro-test

## 🏗️ Architecture
Este proyecto no sigue una arquitectura con nombre; es un sitio estático de Astro con una sola ruta, datos locales en el frontmatter y estilos CSS embebidos. La decisión dominante es mantener toda la presentación en un único archivo de página, sin islas, sin stores y sin fetch en tiempo de ejecución.

```english
Implement the same architecture in my project: an Astro site with file-based routing, a single static page that keeps its data in page frontmatter, and vanilla CSS with custom properties embedded alongside the page. Avoid introducing client-side state, a router library, or hydration unless a new requirement truly needs it.
```

## 📦 Packages
Estas dependencias cubren el framework principal del sitio y una librería instalada que ahora mismo no se usa en el código fuente. No hay paquetes de desarrollo adicionales instalados.

```english
npm i astro
```
```english
npm i fixnow
```

## 🧠 Skills
Este proyecto tiene skills personalizadas en `.agents/skills/` y `.claude/skills/`: Auth0, generación de imágenes con GPT Image 2, análisis de arquitectura, Bun y buenas prácticas de rendimiento para React/Next. Si amplías autenticación, imágenes, arquitectura o toolchain, vale la pena activar la skill correspondiente.

```english
Review the available skills in this repository and set up whichever ones fit my next change: auth0-quickstart for authentication, gpt-image-2 for image generation or editing, improve-codebase-architecture for refactors, skrapi for repository architecture docs, bun for JS/TS workflows, and vercel-react-best-practices for React or Next.js performance work.
```
