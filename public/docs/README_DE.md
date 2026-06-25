<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/logo.webp" width="180" />
</p>

<h1 align="center">[Start] / Mitte / [Ende]</h1>

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
  Starten Sie neue Projekte mit Zuversicht. Verfeinern und härten Sie diese iterativ, während sie wachsen. Führen Sie tiefgreifende, sichere Refactorings durch, wenn sich die Architektur weiterentwickeln muss.
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

## Die drei Phasen

| Phase | Zweck | Schlüsselfähigkeiten | Beispiel-Skills | Status |
| ---------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------ |
| **Start** | Ein Projekt beginnen — neues erstellen oder aus einem bestehenden lernen | Erstellen Sie produktionsreife Strukturen und Konfigurationen ab Commit #1. Oder analysieren Sie die Architektur & Pakete einer bestehenden Codebasis und dokumentieren Sie diese, um funktionierende Muster in Ihrem Projekt wiederzuverwenden. | `start-package`, `skrapi`       | ㅤㅤ✅ |
| **Middle** (Mitte)| Kontinuierliche Verbesserung & Feinschliff | Verbessern Sie UI/UX, härten Sie die Sicherheit, steigern Sie die Leistung, bereinigen Sie die Logik und entfernen Sie toten Code während der aktiven Entwicklung. | Gezielte Verbesserer (TBD) | Geplant |
| **End** (Ende)| Audit, Diagnose & sicheres Refactoring | Vollständige Architektur- & Qualitätsanalyse. Kategorisierte Erkenntnisse mit Belegen auf Dateiebene. Priorisierter, phasenweiser Plan, der **nur mit expliziter Genehmigung** ausgeführt wird. Verhaltensbewahrend. Multi-Runtime-Unterstützung. | `end` | ㅤㅤ✅ |

## Verfügbare Skills

Aufgelistet in der natürlichen Reihenfolge, in der Sie sie benötigen — **Start** (Starten) Sie etwas Neues (oder studieren Sie eine bestehende Codebasis als Inspiration), verfeinern Sie es in der **Middle** (Mitte) und härten Sie es am **End** (Ende).

| Skill | Beschreibung |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[start-package](../../skills/start-package/README.md)** | _Start_ — Erstellt ein veröffentlichbares **duales ESM + CJS** TypeScript-Paket mit gebündelten Typdeklarationen, einem Zero-Config `tsup`-Build und auf `5.x` fixiertem TypeScript, sodass es sowohl im CLI als auch im Editor sauber kompiliert. Generiert `package.json`, `tsconfig.json`, tsup-Konfiguration, einen Smoke-Test und `.vscode`-Einstellungen und führt dann Installation, Build und Überprüfung durch.<br><br>→ [Vollständige Dokumentation](../../skills/start-package/README.md) |
| **[skrapi](../../skills/skrapi/README.md)**               | _Start_ — Richten Sie es auf ein Projekt, das Sie bewundern, und es bildet ab, wie diese Codebasis aufgebaut ist, in einem festen `SKRAPI/`-Ordner mit fokussiertem Markdown — Architektur, Abhängigkeiten und einfügefertige Prompts — damit Sie die für Ihr eigenes Projekt passenden Muster übernehmen können, bevor Sie beginnen. Funktioniert mit jedem Stack (Web, Mobile, Erweiterung, Bibliothek, Monorepo); jede Beschreibung wird an echtem Code verifiziert, niemals nur anhand eines Paketnamens erraten. Mehrsprachige Ausgabe (🇪🇸 ES · 🇺🇸 EN · 🇨🇳 ZH).<br><br>→ [Vollständige Dokumentation](../../skills/skrapi/README.md) |
| **[end](../../skills/end/README.md)**                     | _End_ (Ende) — Versteht Ihr Projekt von A bis Z. Liefert eine klare Diagnose (bestätigte Bugs, Risiken, Chancen, technische Schulden) mit konkreten Referenzen, empfiehlt die richtige Architekturrichtung für _diese_ Codebasis und erstellt einen geordneten Ausführungsplan. Jede Änderung erfolgt in einer isolierten, überprüfbaren Phase — sie wird nur fortgesetzt, wenn Sie `go`, `start` oder `proceed` sagen, und während der Analyse werden keine Dateien berührt.<br><br>→ [Vollständige Dokumentation & Beispiele](../../skills/end/README.md) |

> **Hinweis:** Jeder Skill verfügt über eine eigene detaillierte README. Die Startseite gibt einen Überblick; vertiefen Sie sich in `./skills/<skill>/README.md` für genaue Nutzung, Berichtbeispiele und Garantien.

## Installation

Jeder Skill wird auf die gleiche Weise installiert — wählen Sie den aus, den Sie benötigen:

```bash
npx skills add bastndev/skills --skill start-package   # Start — TS-npm-Paket erstellen
npx skills add bastndev/skills --skill skrapi          # Start — Jede Codebasis studieren & dokumentieren
npx skills add bastndev/skills --skill end             # End   — Audit & sicheres Refactoring
```

## Wie der "End" Skill funktioniert

`end` ist der ausgereifteste Skill der Suite. Hier ist sein durchgehender Workflow:

1. **Zuerst Analyse** — Kartografiert Einstiegspunkte und versteht das Projekt. **Es werden null Dateien modifiziert.**
2. **Strukturierter Bericht** — Klare Erkenntnisse kategorisiert in Bugs (mit Schweregrad), Schulden/Risiken und Vorschläge, plus eine bewertete Gesundheitsübersicht, eine Architekturempfehlung und ein geordneter Plan — alles unterstützt durch konkrete Datei- + Zeilenreferenzen.
3. **Sie autorisieren jede Phase** — Er führt **genau eine Phase** auf einmal aus. Nach jeder Phase erhalten Sie eine genaue Zusammenfassung der Änderungen, durchgeführten Validierungen und die Liste der verbleibenden Phasen.
4. **Volle Kontrolle & Sicherheit** — Erstellt niemals Tests, wenn das Projekt keine hatte. Fügt niemals ohne Erlaubnis Abhängigkeiten hinzu oder wechselt den Paketmanager. Respektiert Ihre nicht committete Arbeit und bewahrt immer das aktuelle Verhalten, es sei denn, ein gerechtfertigter Bug wird behoben.

Lesen Sie die dedizierte Skill-Dokumentation für den vollständigen Workflow, genaue Berichtsformate (einschließlich der erforderlichen Abschlussblöcke), Architektur-Entscheidungsregeln und alle Sicherheitsgarantien:

→ **[End – Refactor Project](../../skills/end/README.md)**

Die vollständige interne Spezifikation finden Sie in [skills/end/SKILL.md](../../skills/end/SKILL.md).

## Roadmap

- **Start** — `start-package` (Gerüstbau) und `skrapi` (Studium einer bestehenden Codebasis) sind heute verfügbar; weitere `start-*`-Scaffolder sind in Arbeit.
- **Middle** — fokussierte, On-Demand-Verbesserer (Leistung, Sicherheit, UX, Entfernung von totem Code) sind geplant.
- **End** — `end` ist heute verfügbar; weitere Runtimes, zusätzliche spezialisierte Refactoring-Modi und Dienstprogramme sind geplant.

Jeder Skill verfügt über seine eigene dedizierte Dokumentation (wie das aktuelle [End – Refactor Project](../../skills/end/README.md)).

---

<br>

<div align="center">
  <p align="center">
  <sub>Gebaut für Entwickler, die möchten, dass ihre KI-Agenten mit der Disziplin eines Senior-Engineers handeln.</sub>
</p>

_Wenn Sie Fehler finden oder Feedback haben, können Sie gerne ein [Issue eröffnen](https://github.com/bastndev/skills/issues/new)._

<sub>Hergestellt in 🇵🇪 von <a href="https://gohit.xyz">Gohit X</a> · Lizenziert unter <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a></sub>

</div>
