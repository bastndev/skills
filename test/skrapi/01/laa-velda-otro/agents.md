# Agents — La Velada del Año VI

## Overview

Este proyecto está configurado para trabajar con **Kiro CLI**, un sistema de AI coding agents. La carpeta `.agents/` contiene 13 skills personalizados que guían el comportamiento de los agentes al trabajar en este codebase.

---

## Root Instructions (AGENTS.md)

El archivo `AGENTS.md` en la raíz del proyecto define reglas globales para cualquier agente que trabaje en el código:

### Key Rules

1. **No auto-linting**: Los agentes NO deben correr ESLint automáticamente después de cada cambio pequeño.

2. **No auto-TypeScript checks**: No correr `pnpm exec tsc` o `astro check` automáticamente — solo cuando el usuario lo pida explícitamente o al preparar una verificación final.

3. **Prefer editor diagnostics**: Usar `ReadLints` (diagnostics del LSP) para feedback rápido en archivos modificados, en lugar de correr linters completos.

4. **Run lints on demand**: Solo ejecutar `pnpm lint` o validaciones amplias cuando:
   - El usuario lo pida
   - Se prepare una verificación final para un cambio riesgoso
   - Los diagnostics no sean suficientes

5. **DOM selector abstraction**: **NUNCA** usar `document.querySelector` o `document.querySelectorAll` directamente. Siempre importar y usar las utilities `$` y `$$` desde `@/lib/dom-selector`:
   ```ts
   import { $, $$} from '@/lib/dom-selector'
   ```

### Pull Request Guidelines

- **One change per PR**: Un PR debe enfocarse en un solo componente o sección.
- **Template**: Seguir el template en `.github/pull_request_template.md`.
- **Screenshots requeridos**: Para cambios visuales, incluir screenshots de mobile + desktop.
- **Breaking changes**: Listar explícitamente o declarar "None".

---

## Skills (.agents/skills/)

El proyecto tiene 13 skills que especializan al agente en diferentes áreas del desarrollo. Cada skill es un folder con un `SKILL.md` que contiene:
- `name`: Nombre del skill
- `description`: Cuándo activarlo y qué hace
- Contenido: Guías, patrones, referencias, reglas

### List of Skills

#### 1. **astro-framework**
Framework specialist para Astro. Cubre:
- Islands architecture
- Content Layer API (loaders, glob, file)
- Server islands (`server:defer`)
- SSR adapters
- View transitions
- Sessions (server-side user state)
- `astro:env` (typed environment variables)
- i18n routing
- Actions
- Client hydration directives

Contiene 10 archivos `.rule.md` en `rules/` y 11 referencias en `references/`.

**Triggers**: Cuando se trabaja con componentes Astro, configuración, content collections, o routing.

#### 2. **astro** (legacy)
Skill más simple de Astro, probablemente deprecado en favor de `astro-framework`. Solo 1 archivo `SKILL.md` básico.

#### 3. **tailwind-css-patterns**
Patrones y best practices de Tailwind CSS. Incluye:
- Layout patterns (grid, flexbox, responsive)
- Component patterns (buttons, cards, forms)
- Animations
- Performance optimization
- Accessibility con Tailwind
- Configuration tips

8 archivos de referencia en `references/` (performance, responsive-design, animations, etc.).

**Triggers**: Styling, responsive design, animaciones, optimización de clases CSS.

#### 4. **accessibility**
Guías de accesibilidad web (a11y). Cubre:
- WCAG 2.1 guidelines
- ARIA patterns
- Keyboard navigation
- Screen reader support
- Semantic HTML

2 referencias: `WCAG.md` y `A11Y-PATTERNS.md`.

**Triggers**: Mejoras de accesibilidad, auditoría a11y, soporte de lectores de pantalla.

#### 5. **seo**
Optimización para motores de búsqueda. Incluye:
- Meta tags (og, twitter cards)
- Structured data (JSON-LD)
- Sitemap generation
- Canonical URLs
- Performance SEO

**Triggers**: Mejoras de SEO, indexación, structured data.

#### 6. **frontend-design**
Principios de diseño frontend (UX/UI). Guías de:
- Layout composition
- Typography
- Color systems
- Spacing and rhythm
- Visual hierarchy

**Triggers**: Diseño visual, mejoras de UI, layout.

#### 7. **typescript-advanced-types**
Patrones avanzados de TypeScript:
- Mapped types
- Conditional types
- Template literal types
- Utility types
- Type guards
- Discriminated unions

**Triggers**: Problemas de tipos complejos, generics, type safety.

#### 8. **nodejs-best-practices**
Best practices de Node.js backend:
- Error handling
- Security patterns
- Performance optimization
- Module patterns
- Async patterns

**Triggers**: Código Node.js, scripts de build, API endpoints.

#### 9. **nodejs-backend-patterns**
Patrones arquitectónicos de backend Node.js:
- Layered architecture
- Dependency injection
- Repository pattern
- Service layer patterns

Contiene `references/advanced-patterns.md`.

**Triggers**: Arquitectura de backend, refactoring de servicios.

#### 10. **deploy-to-vercel**
Guía de deployment a Vercel:
- Configuration (`vercel.json`)
- Environment variables
- Build optimization
- Edge functions
- Analytics

Contiene `resources/` con ejemplos y un `Archive.zip`.

**Triggers**: Deployment, configuración de Vercel, troubleshooting de builds.

#### 11. **scrapp** (Architecture Analyzer)
El skill que estás usando ahora mismo. Analiza arquitectura de proyectos y genera documentación en Markdown.

Contiene 4 referencias en `references/`:
- `web.md` — Para proyectos web (Next, Astro, Vite, etc.)
- `mobile.md` — Para apps React Native/Expo
- `extension.md` — Para browser extensions
- `library.md` — Para npm packages/libraries

**Triggers**: "Analiza este proyecto", "ayúdame a entender la estructura", "qué packages usa para X".

---

## Skills Not Used Yet

Aunque hay 13 skills, el proyecto actual **no usa todos activamente**:

- **React integration** (`@astrojs/react`) está instalado pero no se usa (no hay archivos `.jsx`/`.tsx`).
- **i18n routing** del skill `astro-framework` no está implementado (todo en español).
- **View transitions** de Astro no están configuradas (navegación tradicional).
- **Server islands** (`server:defer`) no se usan.

Los skills están disponibles para futuras features o refactors.

---

## How Skills Work

Cuando un agente de Kiro CLI trabaja en este proyecto:

1. Lee `AGENTS.md` para reglas globales.
2. Detecta el contexto de la tarea (e.g., "estoy modificando un componente Astro").
3. Activa los skills relevantes (e.g., `astro-framework`, `tailwind-css-patterns`, `accessibility`).
4. Usa las referencias y reglas de esos skills para tomar decisiones (e.g., "usar `client:idle` en lugar de `client:load` para este componente").
5. Sigue los patterns documentados en los skills en lugar de adivinar o usar prácticas genéricas.

---

## Maintaining Skills

- **Location**: `.agents/skills/[skill-name]/SKILL.md`
- **Format**: Markdown con frontmatter YAML (name, description, metadata)
- **Updates**: Cuando el proyecto adopta nuevos patrones, actualizar el skill correspondiente para que futuros agentes sigan la convención.

**Example**: Si el proyecto empieza a usar `nanostores` para state management, actualizar `astro-framework/SKILL.md` con un section sobre cómo y cuándo usarlo.

---

## Comparison to Other AI Tooling

Este setup es similar pero no idéntico a:

- **Cursor `.cursorrules`**: Cursor usa archivos `.cursorrules` en la raíz. Este proyecto tiene `.cursor/` folder pero las reglas principales están en `AGENTS.md` y `.agents/skills/`.
- **Claude `.claude/`**: Claude Code (Anthropic) usa `.claude/commands/`, `.claude/skills/`, `.claude/agents/`. Este proyecto usa la convención `.agents/skills/` de Kiro CLI.
- **GitHub Copilot**: Copilot no tiene sistema de skills; solo usa comentarios inline. Este proyecto tiene skills estructurados que son más explícitos.

---

## Notable Decisions

1. **No client-side linting during dev**: Hace el workflow del agente más rápido. Solo se valida cuando el usuario lo pide o antes de commit.

2. **DOM selector abstraction enforced**: La regla de usar `$ / $$` en lugar de `querySelector` directo asegura consistencia y facilita futuros refactors (e.g., cambiar a un sistema de scoped queries).

3. **Skill-based vs prompt-based**: En lugar de darle al agente un prompt largo cada vez, los skills se activan contextualmente. Reduce repetición y asegura consistencia entre sesiones.
