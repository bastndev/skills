<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/logo.webp" width="180" />
</p>

<h1 align="center">[Start] / Middle / [End]</h1>

<p align="center">
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_ES.md">Español 🇪🇸</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_ZH.md">中文 🇨🇳</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_DE.md">Deutsch 🇩🇪</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_FR.md">Français 🇫🇷</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_JA.md">日本語 🇯🇵</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_KO.md">한국어 🇰🇷</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_PT.md">Português 🇧🇷</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_RU.md">Русский 🇷🇺</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_VI.md">Tiếng Việt 🇻🇳</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_HI.md">हिन्दी 🇮🇳</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_AR.md">العربية 🇸🇦</a><span>...</span>
</p>

<br>

<p align="center">
  Inicia nuevos proyectos con confianza. Refina y afianza iterativamente a medida que crecen. Realiza refactorizaciones profundas y seguras cuando la arquitectura necesite evolucionar.
</p>

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

```
npx skills add bastndev/skills
```

<br>

## Las tres fases

| Fase | Propósito | Capacidades clave | Habilidades de ejemplo | Estado |
| ---------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------ |
| **Start** | Iniciar un proyecto — crear uno nuevo o aprender de uno existente | Crea estructuras y configuraciones listas para producción desde el commit #1. O analiza la arquitectura y paquetes de un codebase existente y documenta lo que funciona, para poder reutilizarlo en tu propio proyecto. | `start-package`, `start-astro`, `skrapi` | ㅤㅤ✅ |
| **Middle** | Mejora continua y pulido | Evalúa el proyecto (resumen de salud de 0–100), luego mejora **una dimensión a la vez** — rendimiento, UI/UX, orden (orden de archivos + higiene de comentarios), seguridad, estructura, limpieza o calidad de código — con un plan enfocado que se ejecuta solo al escribir `go`. | `middle` | ㅤㅤ✅ |
| **End** | Auditoría, diagnóstico y refactorización segura | Análisis completo de arquitectura y calidad. Hallazgos categorizados con evidencia a nivel de archivo. Plan por fases priorizado ejecutado **solo con aprobación explícita**. Preservación de comportamiento. Soporte multi-runtime. | `end` | ㅤㅤ✅ |

## Habilidades disponibles

Listadas en el orden natural en que las necesitarías — **Empieza** algo nuevo (o estudia un codebase existente como inspiración), refínalo en el **Medio**, y afiánzalo en el **Final**.

| Habilidad | Descripción |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[start-package](./skills/start-package/README.md)** | _Start_ — Genera un paquete TypeScript **dual ESM + CJS** publicable con declaraciones de tipo empaquetadas, una compilación `tsup` sin configuración y TypeScript fijado en `5.x` para que compile limpiamente tanto en CLI como en editor. Genera `package.json`, `tsconfig.json`, configuración de tsup, una prueba de humo y configuraciones `.vscode`, luego instala, compila y verifica.<br><br>→ [Documentación completa](./skills/start-package/README.md) |
| **[start-astro](./skills/start-astro/README.md)** | _Start_ — Genera un nuevo proyecto Astro usando la plantilla `minimal`, superpuesto con una arquitectura limpia y **escalable** — listo para crecer desde un portafolio hasta una app completa. Configura un layout compartido, header, footer, páginas, toggle de tema claro/oscuro, View Transitions nativas, alias de ruta y Content Collections listas para usar.<br><br>→ [Documentación completa](./skills/start-astro/README.md) |
| **[skrapi](./skills/skrapi/README.md)** | _Start_ — Apúntalo a un proyecto que admiras y mapea cómo está construido ese codebase en una carpeta fija `SKRAPI/` de Markdown enfocado — arquitectura, dependencias y prompts listos para copiar — para que puedas tomar los patrones que encajen en tu propio proyecto antes de comenzar. Funciona en cualquier stack (web, móvil, extensión, librería, monorepo); cada descripción está verificada contra el código real, nunca adivinada por nombre de paquete. Salida multilingüe (🇪🇸 ES · 🇺🇸 EN · 🇨🇳 ZH).<br><br>→ [Documentación completa](./skills/skrapi/README.md) |
| **[middle](./skills/middle/README.md)** | _Middle_ — Mejoradores numerados bajo demanda para desarrollo activo. `0` evalúa tu proyecto o carpeta con un resumen de salud de 0–100 y señala el área más débil; `1–7` califica cada uno una dimensión (⚡ rendimiento · 🎨 ui-ux · 🗂️ orden · 🔒 seguridad · 🏗️ estructura · 🧹 limpieza · 🧩 calidad), reporta hallazgos respaldados por evidencia y propone un plan de corrección — ejecutado fase por fase solo cuando dices `go`.<br><br>→ [Documentación completa](./skills/middle/README.md) |
| **[end](./skills/end/README.md)** | _End_ — Entiende tu proyecto de principio a fin. Entrega un diagnóstico claro (bugs confirmados, riesgos, oportunidades, deuda técnica) con referencias concretas, recomienda la dirección arquitectónica correcta para _este_ codebase y construye un plan de ejecución ordenado. Cada cambio ocurre en una fase aislada y revisable — solo procede cuando dices `go`, `start` o `proceed`, y no se tocan archivos durante el análisis.<br><br>→ [Documentación completa y ejemplos](./skills/end/README.md) |
| **[l10n-sync](./skills/l10n-sync/README.md)** | _Utility_ — La habilidad disciplinada y eficiente en tokens para localización. Sincroniza assets traducidos con la fuente inglesa sin retraducir archivos completos. Garantiza invariantes (código, HTML) y estructuras exactas preservadas en 11 idiomas.<br><br>→ [Documentación completa](./skills/l10n-sync/README.md) |

> **Nota:** Cada habilidad incluye su propio README detallado. La página raíz ofrece la visión general de alto nivel; profundiza en `./skills/<skill>/README.md` para uso detallado, ejemplos de reportes y garantías.

## Instalación

Cada habilidad se instala de la misma manera — elige la que necesitas:

```bash
npx skills add bastndev/skills --skill start-package   # Start  — scaffold a TS npm package
npx skills add bastndev/skills --skill start-astro     # Start  — scaffold an Astro project
npx skills add bastndev/skills --skill skrapi          # Start  — study & document any codebase
npx skills add bastndev/skills --skill middle          # Middle — score & improve one dimension
npx skills add bastndev/skills --skill end             # End    — audit & safely refactor
npx skills add bastndev/skills --skill l10n-sync       # Utility — sync localized assets safely
```

## Cómo funciona la habilidad End

`end` es la habilidad más madura de la suite. Aquí está su flujo de trabajo completo:

1. **Análisis primero** — Mapea puntos de entrada y entiende el proyecto. **No se modifica ningún archivo.**
2. **Reporte estructurado** — Hallazgos claros categorizados en Bugs (con severidad), Deuda/Riesgos y Sugerencias, más un resumen de salud puntuado, una recomendación arquitectónica y un plan ordenado — todos respaldados por referencias concretas de archivo + línea.
3. **Tú autorizas cada fase** — Ejecuta **exactamente una fase** a la vez. Después de cada fase obtienes un resumen preciso de cambios, validaciones realizadas y la lista de fases restantes.
4. **Control total y seguridad** — Nunca crea tests si el proyecto no tenía. Nunca agrega dependencias o cambia el gestor de paquetes sin permiso. Respeta tu trabajo sin commit y siempre preserva el comportamiento actual salvo que corrija un bug justificado.

Para el flujo completo, formatos exactos de reporte (incluyendo los bloques de cierre requeridos), reglas de decisión arquitectónica y todas las garantías de seguridad, lee la documentación dedicada de la habilidad:

→ **[End – Refactor Project](./skills/end/README.md)**

La especificación interna completa está en [skills/end/SKILL.md](./skills/end/SKILL.md).

## Hoja de ruta

- **Start** — `start-package` (scaffold), `start-astro` (scaffold de Astro) y `skrapi` (estudiar un codebase existente) están disponibles hoy; más generadores `start-*` están en camino.
- **Middle** — `middle` está disponible hoy (resumen de salud + seis mejoradores numerados); herramientas más profundas por dimensión están planeadas.
- **End** — `end` está disponible hoy; más runtimes, modos de refactorización especializados adicionales y utilidades están planeadas.
- **Utility** — `l10n-sync` está disponible hoy para localización disciplinada y eficiente en tokens.

Cada habilidad incluye su propia documentación dedicada (como el actual [End – Refactor Project](./skills/end/README.md)).

---

<br>

<div align="center">
  <p align="center">
  <sub>Creado para desarrolladores que quieren que sus agentes de IA actúen con la disciplina de un ingeniero senior.</sub>
</p>

_Si encuentras errores o tienes feedback, no dudes en [abrir un issue](https://github.com/bastndev/skills/issues/new)._

<sub>Hecho en 🇵🇪 por <a href="https://gohit.xyz">Gohit X</a> · Licenciado bajo <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a></sub>

</div>
