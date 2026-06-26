<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/logo.webp" width="180" />
</p>

<h1 align="center">[Inicio] / Medio / [Fin]</h1>

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
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_AR.md">العربية 🇸🇦</a>
</p>

<br>

<p align="center">
  Inicia nuevos proyectos con confianza. Refínalos y fortalécelos iterativamente a medida que crecen. Realiza refactorizaciones profundas y seguras cuando la arquitectura necesite evolucionar.
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

## Las Tres Fases

| Fase | Propósito | Capacidades Clave | Ejemplos de Skills | Estado |
| ---------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------ |
| **Start** (Inicio)| Iniciar un proyecto — estructurar uno nuevo, o aprender de uno existente | Crea estructuras y configuraciones listas para producción desde el commit #1. O analiza la arquitectura y los paquetes de una base de código existente y la documenta, para que puedas reutilizar lo que funciona en tu propio proyecto. | `start-package`, `start-astro`, `skrapi`       | ㅤㅤ✅ |
| **Middle** (Medio)| Mejora continua y pulido | Mejora UI/UX, refuerza la seguridad, aumenta el rendimiento, limpia la lógica y elimina código muerto durante el desarrollo activo. | Optimizadores específicos (Por definir) | Planeado |
| **End** (Fin)| Auditoría, diagnóstico y refactorización segura | Análisis completo de arquitectura y calidad. Hallazgos categorizados con evidencia a nivel de archivo. Plan por fases priorizado ejecutado **solo con aprobación explícita**. Preserva el comportamiento. Soporte multi-entorno. | `end` | ㅤㅤ✅ |

## Skills Disponibles

Listados en el orden natural en el que los utilizarías: **Start** (Inicia) algo nuevo (o estudia una base de código existente como inspiración), refínalo en el **Middle** (Medio), y fortalécelo al **End** (Fin).

| Skill | Descripción |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[start-package](../../skills/start-package/README.md)** | _Start_ (Inicio) — Estructura un paquete de TypeScript **dual ESM + CJS** publicable con declaraciones de tipo empaquetadas, una compilación de `tsup` sin configuración y TypeScript fijado en `5.x` para que compile limpiamente tanto en CLI como en el editor. Genera `package.json`, `tsconfig.json`, la configuración de tsup, una prueba de humo y la configuración de `.vscode`, luego instala, compila y verifica.<br><br>→ [Documentación completa](../../skills/start-package/README.md) |
| **[start-astro](../../skills/start-astro/README.md)** | _Start_ (Inicio) — Estructura un nuevo proyecto Astro usando la plantilla `minimal`, superpuesta con una arquitectura limpia y **escalable** — lista para crecer desde un portafolio hasta una aplicación completa. Configura un layout compartido, encabezado, pie de página, páginas, cambio de tema claro/oscuro, View Transitions nativas, alias de ruta y Colecciones de Contenido (Content Collections) listos para usar.<br><br>→ [Documentación completa](../../skills/start-astro/README.md) |
| **[skrapi](../../skills/skrapi/README.md)**               | _Start_ (Inicio) — Apúntalo a un proyecto que admires y mapeará cómo está construida esa base de código en una carpeta `SKRAPI/` fija de Markdown enfocado — arquitectura, dependencias y prompts listos para pegar — para que puedas tomar prestados los patrones que se adapten a tu propio proyecto antes de comenzar. Funciona en cualquier stack (web, móvil, extensión, librería, monorepo); cada descripción se verifica con código real, nunca se adivina por el nombre del paquete. Salida multilingüe (🇪🇸 ES · 🇺🇸 EN · 🇨🇳 ZH).<br><br>→ [Documentación completa](../../skills/skrapi/README.md) |
| **[end](../../skills/end/README.md)**                     | _End_ (Fin) — Entiende tu proyecto de principio a fin. Entrega un diagnóstico claro (errores confirmados, riesgos, oportunidades, deuda técnica) con referencias concretas, recomienda la dirección de arquitectura correcta para _esta_ base de código y construye un plan de ejecución ordenado. Cada cambio ocurre en una fase aislada y revisable — solo avanza cuando dices `go`, `start` o `proceed`, y no se toca ningún archivo durante el análisis.<br><br>→ [Documentación completa y ejemplos](../../skills/end/README.md) |

> **Nota:** Cada skill viene con su propio README detallado. La página raíz da una visión general de alto nivel; adéntrate en `./skills/<skill>/README.md` para un uso profundo, ejemplos de informes y garantías.

## Instalación

Cada skill se instala de la misma manera — elige la que necesites:

```bash
npx skills add bastndev/skills --skill start-package   # Start (Inicio) — estructura un paquete TS npm
npx skills add bastndev/skills --skill start-astro     # Start (Inicio) — estructura un proyecto Astro
npx skills add bastndev/skills --skill skrapi          # Start (Inicio) — estudia y documenta cualquier base de código
npx skills add bastndev/skills --skill end             # End (Fin) — audita y refactoriza de forma segura
```

## Cómo funciona la Skill "End"

`end` es la skill más madura de la suite. Así es como funciona su flujo de principio a fin:

1. **Análisis primero** — Mapea los puntos de entrada y entiende el proyecto. **No se modifica ningún archivo.**
2. **Informe estructurado** — Hallazgos claros categorizados en Errores (con severidad), Deuda/Riesgos y Sugerencias, además de una visión general de salud puntuada, una recomendación de arquitectura y un plan ordenado — todo respaldado con referencias concretas a archivos y líneas.
3. **Autorizas cada fase** — Ejecuta **exactamente una fase** a la vez. Después de cada fase obtienes un resumen preciso de los cambios, validaciones realizadas y la lista de fases restantes.
4. **Control total y seguridad** — Nunca crea pruebas si el proyecto no tenía ninguna. Nunca agrega dependencias o cambia el gestor de paquetes sin permiso. Respeta tu trabajo no consolidado (uncommitted) y siempre preserva el comportamiento actual a menos que arregle un error justificado.

Para conocer el flujo completo, formatos de informe exactos (incluyendo los bloques de cierre requeridos), reglas de decisión de arquitectura y todas las garantías de seguridad, lee la documentación dedicada de la skill:

→ **[End – Refactorizar Proyecto](../../skills/end/README.md)**

La especificación interna completa se encuentra en [skills/end/SKILL.md](../../skills/end/SKILL.md).

## Hoja de Ruta

- **Start** (Inicio) — `start-package` (estructurador), `start-astro` (estructurador de Astro) y `skrapi` (estudia una base de código existente) ya están disponibles; hay más estructuradores `start-*` en camino.
- **Middle** (Medio) — están planeados mejoradores enfocados bajo demanda (rendimiento, seguridad, UX, eliminación de código muerto).
- **End** (Fin) — `end` ya está disponible; están planeados más entornos de ejecución, modos adicionales de refactorización especializados y utilidades.

Cada skill viene con su propia documentación dedicada (como el actual [End – Refactorizar Proyecto](../../skills/end/README.md)).

---

<br>

<div align="center">
  <p align="center">
  <sub>Construido para desarrolladores que quieren que sus agentes de IA actúen con la disciplina de un ingeniero senior.</sub>
</p>

_Si encuentras algún error o tienes comentarios, no dudes en [abrir un issue](https://github.com/bastndev/skills/issues/new)._

<sub>Hecho en 🇵🇪 por <a href="https://gohit.xyz">Gohit X</a> · Licenciado bajo <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a></sub>

</div>
