<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/logo.webp" width="180" />
</p>

<h1 align="center">Inicio / Medio / Fin</h1>

<p align="center">
  <a href="https://github.com/bastndev/skills/blob/main/README.md">English 🇺🇸</a> | 
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

## Las Tres Fases

| Fase | Propósito | Capacidades Clave | Ejemplos de Skills | Estado |
| --- | --- | --- | --- | --- |
| **Start** | Inicialización y scaffolding | Crear estructuras listas para producción, inicializar frameworks, aplicar configuraciones y mejores prácticas desde el primer commit. | `start-nextjs`, `start-vite`... | Planeado |
| **Middle** | Mejora continua y pulido | Mejorar UI/UX, endurecer la seguridad, aumentar el rendimiento, limpiar la lógica, eliminar código muerto. | Optimizadores (TBD) | Planeado |
| **End** | Auditoría, diagnóstico y refactorización | Análisis completo de arquitectura. Plan en fases priorizado y ejecutado **solo con aprobación explícita**. Mantiene el comportamiento original. | `refactor-project` | ✅ Disponible |

## Skills Disponibles

| Skill | Descripción |
| --- | --- |
| **[end](../../skills/end/README.md)** | **`refactor-project`** — Entiende tu proyecto de principio a fin. Entrega un diagnóstico claro con referencias concretas. Recomienda la dirección de arquitectura adecuada y construye un plan de ejecución ordenado. Cada cambio ocurre de forma aislada. Tú mantienes el control.<br><br>→ [Documentación completa y ejemplos](../../skills/end/README.md) |

> **Nota:** Cada skill incluye su propio README detallado. La página raíz ofrece una visión general; revisa `../../skills/<skill>/README.md` para ver su uso detallado, ejemplos de reportes y garantías.

## Instalación

```bash
# Instalar el skill End (refactor-project)
npx skills add bastndev/skills --skill end
```

Las skills adicionales (una vez lanzadas) se instalan de la misma manera:

```bash
npx skills add bastndev/skills --skill start-nextjs
```

## Cómo funciona el Skill End

1. **Primero análisis** — Mapea los puntos de entrada y entiende el proyecto. **No se modifica ningún archivo.**
2. **Reporte estructurado** — Hallazgos claros en cuatro categorías (Bugs Confirmados con severidad, Riesgos, Oportunidades de Refactorización, Deuda Técnica) + una recomendación de arquitectura y un plan ordenado. Todos los elementos incluyen referencias concretas a archivos y líneas.
3. **Tú autorizas cada fase** — Se ejecuta **exactamente una fase** a la vez. Después de cada fase obtienes un resumen preciso de los cambios, las validaciones realizadas y la lista de las fases restantes.
4. **Control total y seguridad** — Nunca crea pruebas si el proyecto no tenía ninguna. Nunca añade dependencias ni cambia el gestor de paquetes sin permiso. Respeta tu trabajo no confirmado y siempre preserva el comportamiento actual a menos que solucione un bug justificado.

Para ver el flujo de trabajo completo, los formatos exactos de los reportes (incluyendo los bloques de cierre requeridos), las reglas de decisión de arquitectura y todas las garantías de seguridad, lee la documentación dedicada del skill:

→ **[End – Refactor Project](../../skills/end/README.md)**

La especificación interna completa se encuentra en [skills/end/SKILL.md](../../skills/end/SKILL.md).

## Hoja de Ruta

- **Skills Start** — Scaffolding de proyectos en un solo comando para los stacks más populares (Next.js, Vite, FastAPI, etc.)
- **Skills Middle** — Mejoradores enfocados bajo demanda (rendimiento, seguridad, UX, eliminación de código muerto, etc.)
- **Expansiones End** — Más entornos de ejecución, modos de refactorización especializados adicionales y utilidades.

Cada skill tendrá su propia documentación dedicada (como el actual [End – Refactor Project](../../skills/end/README.md)).

---

<br>

<div align="center">
  <p align="center">
  <sub>Construido para desarrolladores que quieren que sus agentes de IA actúen con la disciplina de un ingeniero senior.</sub>
</p>

_If you find any bugs or have feedback, feel free to [open an issue](https://github.com/bastndev/skills/issues/new)._

<sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a></sub>

</div>
