// Content Collections config. In Astro 7 this lives at the src root as
// `content.config.ts` (not the older `src/content/config.ts`).
//
// Define collections here, named in PLURAL — a collection holds many entries.
// Entries live in `src/content/<collection>/`. Pages read them with
// getCollection() / getStaticPaths(). See ARCHITECTURE.md → "Content Collections".
//
// Example — uncomment and adapt:
//
// import { defineCollection, z } from 'astro:content';
// import { glob } from 'astro/loaders';
//
// const projects = defineCollection({
//   loader: glob({ pattern: '**/*.md', base: './src/content/projects' }),
//   schema: z.object({
//     title: z.string(),
//     description: z.string(),
//     repoUrl: z.string().url().optional(),
//   }),
// });
//
// export const collections = { projects };

export const collections = {};
