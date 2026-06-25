# Prompts — astro-test

## 🏗️ Architecture

This project uses Astro's islands architecture in its simplest form: fully static generation (SSG) with no islands activated, no client-side JS, and all content rendered at build time from a single `.astro` page.

```
I have an Astro project that I want to build as a fully static site with no JavaScript sent to the browser. It uses Astro 6 with TypeScript in strict mode. There is a single page at src/pages/index.astro that renders a product grid from a hardcoded data array in the frontmatter. The astro.config.mjs has no adapter and no integrations configured — just a bare defineConfig({}). Please help me extend this pattern: add a second page, move the product data to a Content Collection with a Zod schema, and keep the output fully static with no client: directives.
```

## 📦 Packages

This project has two runtime dependencies: `astro` (the framework) and `fixnow` (a text correction library that is currently unused in the source code).

```
npm i astro
```
```
npm i fixnow
```

## 🤖 Skills

This project has 6 custom skills installed across `.agents/skills/` and `.claude/skills/`, covering architecture analysis, image generation, authentication, React best practices, and Bun tooling.

<br>

⯈ **skrapi**
```
npx skills add https://github.com/bastndev/skills --skill skrapi
```

<br>


```
npx skills add https://github.com/mattpocock/skills --skill improve-codebase-architecture
```

<br>

```
npx skills add https://github.com/doany-ai/skills --skill gpt-image-2
```

<br>

```
npx skills add https://github.com/auth0/agent-skills --skill auth0-quickstart
```

<br>

```
npx skills add https://github.com/vercel-labs/agent-skills --skill vercel-react-best-practices
```

<br>

```
npx skills add https://github.com/midudev/autoskills --skill bun
```

<br>
