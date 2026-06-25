## Skills (.agents/skills/)

### 1. **auth0-quickstart**
- Detecta el stack del proyecto y guía la configuración de autenticación con Auth0.
- Incluye flujos para login en apps web y móviles.
**Triggers**: cuando se añade autenticación o inicio de sesión a una app.

### 2. **gpt-image-2**
- Genera y edita imágenes con OpenAI GPT Image 2 en RunComfy.
- Está orientado a prompts con texto incrustado, logos, tipografía y ediciones con preservación de composición.
**Triggers**: cuando se pide generar o editar imágenes con GPT Image 2, ChatGPT Images 2 o Image 2.

### 3. **improve-codebase-architecture**
- Busca oportunidades de refactor para profundizar módulos y mejorar testabilidad y navegabilidad para IA.
- Trae documentación de apoyo en varios archivos auxiliares, además de la skill principal.
**Triggers**: cuando se quiere mejorar arquitectura, consolidar módulos acoplados o descubrir refactors de mayor leverage.

### 4. **skrapi**
- Analiza la arquitectura de un repositorio y produce documentación enfocada en Markdown.
- Incluye referencias por tipo de proyecto en `references/`.
**Triggers**: cuando se quiere entender, documentar o comparar la estructura de un código base.

## Skills (.claude/skills/)

### 1. **bun**
- Uso de Bun para ejecutar scripts, instalar dependencias, compilar y probar proyectos JavaScript/TypeScript.
- Encaja con este repo porque usa `bun.lock` y un workspace de Astro en JavaScript/TypeScript.
**Triggers**: cuando se necesita build, test, install o ejecución rápida de código JS/TS.

### 2. **vercel-react-best-practices**
- Conjunto de guías de rendimiento para React y Next.js, con foco en waterfalls, bundles, render y data fetching.
- Trae un paquete amplio de reglas para revisión y refactor de componentes y páginas React/Next.
**Triggers**: cuando se escribe, revisa o optimiza código React o Next.js.
