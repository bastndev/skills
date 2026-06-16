<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/logo.webp" width="180" />
</p>

<h1 align="center">Начало / Середина / Конец</h1>

<p align="center">
  <a href="https://github.com/bastndev/skills/blob/main/README.md">English 🇺🇸</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_ES.md">Español 🇪🇸</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_ZH.md">中文 🇨🇳</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_DE.md">Deutsch 🇩🇪</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_FR.md">Français 🇫🇷</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_JA.md">日本語 🇯🇵</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_KO.md">한국어 🇰🇷</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_PT.md">Português 🇧🇷</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_VI.md">Tiếng Việt 🇻🇳</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_HI.md">हिन्दी 🇮🇳</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_AR.md">العربية 🇸🇦</a>
</p>

<br>

<p align="center">
  Уверенно запускайте новые проекты. Итеративно улучшайте и укрепляйте их по мере роста. Выполняйте глубокий и безопасный рефакторинг, когда архитектуре необходимо развиваться.
</p>

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

## Три Фазы

| Фаза | Цель | Ключевые возможности | Примеры навыков | Статус |
| --- | --- | --- | --- | --- |
| **Start** | Инициализация проекта | Создание структур папок, готовых к продакшену, инициализация фреймворков, применение лучших практик с первого коммита. | `start-nextjs`... | Запланировано |
| **Middle** | Непрерывное улучшение | Улучшение UI/UX, повышение безопасности, производительности, очистка логики. | TBD | Запланировано |
| **End** | Аудит и рефакторинг | Полный анализ архитектуры. План по этапам выполняется **только с явного одобрения**. | `refactor-project` | ✅ Доступно |

## Доступные навыки

| Навык | Описание |
| --- | --- |
| **[end](../../skills/end/README.md)** | **`refactor-project`** — Понимает ваш проект от начала до конца. Предоставляет четкий диагноз с конкретными ссылками. Рекомендует правильное направление архитектуры. Вы сохраняете полный контроль.<br><br>→ [Полная документация и примеры](../../skills/end/README.md) |

> **Примечание:** У каждого skill есть свой подробный README. На главной странице представлен общий обзор; загляните в `../../skills/<skill>/README.md` для подробного использования, примеров отчетов и гарантий.

## Установка

```bash
# Добавить текущий навык (End / refactor-project)
npx skills add bastndev/skills --skill end
```

Будущие навыки будут устанавливаться так же:

```bash
npx skills add bastndev/skills --skill start-nextjs
```

## Как работает Skill End

1. **Сначала анализ** — Картирует точки входа и понимает проект. **Никакие файлы не изменяются.**
2. **Структурированный отчет** — Ясные выводы по четырем категориям (Подтвержденные ошибки с серьезностью, Риски, Возможности рефакторинга, Технический долг) + рекомендация по архитектуре и упорядоченный план. Все пункты включают конкретные ссылки на файлы и строки.
3. **Вы авторизуете каждую фазу** — Выполняет **ровно одну фазу** за раз. После каждой фазы вы получаете точную сводку изменений, выполненных проверок и список оставшихся фаз.
4. **Полный контроль и безопасность** — Никогда не создает тесты, если их не было в проекте. Никогда не добавляет зависимости и не изменяет менеджер пакетов без разрешения. Уважает вашу незакоммиченную работу и всегда сохраняет текущее поведение, если только не исправляет обоснованную ошибку.

Для полного рабочего процесса, точных форматов отчетов, правил принятия архитектурных решений и всех гарантий безопасности прочитайте специальную документацию по skill:

→ **[End – Refactor Project](../../skills/end/README.md)**

Полная внутренняя спецификация находится в [skills/end/SKILL.md](../../skills/end/SKILL.md).

## Дорожная карта

- **Skills Start** — Скаффолдинг проектов одной командой для популярных стеков (Next.js, Vite, FastAPI и т.д.)
- **Skills Middle** — Целевые улучшатели по запросу (производительность, безопасность, UX, удаление мертвого кода и т.д.)
- **Расширения End** — Больше сред выполнения, дополнительные специализированные режимы рефакторинга и утилиты.

У каждого skill будет своя специальная документация (как текущий [End – Refactor Project](../../skills/end/README.md)).

---

<br>

<div align="center">
  <p align="center">
  <sub>Создано для разработчиков, которые хотят, чтобы их ИИ-агенты действовали с дисциплиной старшего инженера.</sub>
</p>

_If you find any bugs or have feedback, feel free to [open an issue](https://github.com/bastndev/skills/issues/new)._

<sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a></sub>

</div>
