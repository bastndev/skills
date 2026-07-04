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
  Starten Sie neue Projekte mit Zuversicht. Verfeinern und festigen Sie sie iterativ, während sie wachsen. Führen Sie tiefe, sichere Refactorings durch, wenn sich die Architektur weiterentwickeln muss.
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

| Phase | Zweck | Hauptfunktionen | Beispiel-Skills | Status |
| ---------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------ |
| **Start** | Ein Projekt beginnen — neu starten oder von einem bestehenden lernen | Erstellen Sie ab Commit #1 produktionsreife Strukturen und Konfigurationen. Oder analysieren Sie die Architektur & Pakete eines bestehenden Codebasis und dokumentieren Sie diese, damit Sie das Funktionierende in Ihrem eigenen Projekt wiederverwenden können. | `start-package`, `start-astro`, `skrapi` | ㅤㅤ✅ |
| **Middle** | Kontinuierliche Verbesserung & Veredelung | Bewerten Sie das Projekt (0–100 Gesundheitsüberblick), dann verbessern Sie **eine Dimension nach der anderen** — Leistung, UI/UX, Aufgeräumtheit (Dateireihenfolge + Kommentar-Hygiene), Sicherheit, Struktur, Bereinigung oder Codequalität — mit einem fokussierten Plan, der nur bei Eingabe von `go` ausgeführt wird. | `middle` | ㅤㅤ✅ |
| **End** | Audit, Diagnose & sicheres Refactoring | Vollständige Architektur- & Qualitätsanalyse. Klassifizierte Ergebnisse mit dateispezifischen Belegen. Priorisierter Phasenplan, der **nur mit ausdrücklicher Genehmigung** ausgeführt wird. Verhaltenserhaltend. Multi-Runtime-Unterstützung. | `end` | ㅤㅤ✅ |

## Verfügbare Skills

In der natürlichen Reihenfolge, in der Sie sie brauchen — **Starten** Sie etwas Neues (oder studieren Sie eine bestehende Codebasis als Inspiration), verfeinern Sie es in der **Mitte** und festigen Sie es am **Ende**.

| Skill | Beschreibung |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[start-package](./skills/start-package/README.md)** | _Start_ — Erstellt ein veröffentlichbares **duales ESM + CJS** TypeScript-Paket mit gebündelten Typlarkearungen, einem konfigurationsfreien `tsup`-Build und TypeScript auf `5.x` fixiert, damit es sowohl in der CLI als auch im Editor sauber erstellt wird. Generiert `package.json`, `tsconfig.json`, tsup-Konfiguration, einen Rauchtest und `.vscode`-Einstellungen, installiert dann, baut und verifiziert.<br><br>→ [Vollständige Dokumentation](./skills/start-package/README.md) |
| **[start-astro](./skills/start-astro/README.md)** | _Start_ — Erstellt ein neues Astro-Projekt mit der `minimal`-Vorlage, ergänzt um eine saubere, **skalierbare** Architektur — bereit zum Wachstum von einem Portfolio zu einer vollständigen App. Richtet ein gemeinsames Layout, Header, Footer, Seiten, Hell/Dunkel-Thema-Umschaltung, native View Transitions, Pfad-Alias und Content Collections out of the box ein.<br><br>→ [Vollständige Dokumentation](./skills/start-astro/README.md) |
| **[skrapi](./skills/skrapi/README.md)** | _Start_ — Richten Sie es auf ein Projekt, das Sie bewundern, und es kartiert, wie dieser Code in einen festen `SKRAPI/`-Ordner aus fokussiertem Markdown gebaut ist — Architektur, Abhängigkeiten und kopierfertige Prompts — damit Sie die Muster übernehmen können, die zu Ihrem Projekt passen, bevor Sie beginnen. Funktioniert mit jedem Stack (Web, Mobile, Erweiterung, Bibliothek, Monorepo); jede Beschreibung wird anhand des echten Codes überprüft, nie geraten. Mehrsprachige Ausgabe (🇪🇸 ES · 🇺🇸 EN · 🇨🇳 ZH).<br><br>→ [Vollständige Dokumentation](./skills/skrapi/README.md) |
| **[middle](./skills/middle/README.md)** | _Middle_ — Nummerierte, bedarfsorientierte Verbesserer für aktive Entwicklung. `0` bewertet Ihr Projekt oder Ihren Ordner mit einem 0–100 Gesundheitsüberblick und zeigt auf den schwächsten Bereich; `1–7` qualifizieren jeweils eine Dimension (⚡ Leistung · 🎨 UI/UX · 🗂️ Aufgeräumtheit · 🔒 Sicherheit · 🏗️ Struktur · 🧹 Bereinigung · 🧩 Qualität), berichten evidenzgestützte Ergebnisse und schlagen einen Korrekturplan vor — Phase für Phase nur bei Eingabe von `go` ausgeführt.<br><br>→ [Vollständige Dokumentation](./skills/middle/README.md) |
| **[end](./skills/end/README.md)** | _End_ — Versteht Ihr Projekt von Anfang bis Ende. Liefert eine klare Diagnose (bestätigte Bugs, Risiken, Möglichkeiten, technische Schulden) mit konkreten Referenzen, empfiehlt die richtige Architekturrichtung für _diese_ Codebasis und erstellt einen geordneten Ausführungsplan. Jede Änderung erfolgt in einer isolierten, überprüfbaren Phase — sie wird nur bei Eingabe von `go`, `start` oder `proceed` ausgeführt, und keine Dateien werden während der Analyse berührt.<br><br>→ [Vollständige Dokumentation & Beispiele](./skills/end/README.md) |
| **[l10n-sync](./skills/l10n-sync/README.md)** | _Utility_ — Der disziplinierte, token-effiziente Lokalisierungsskill. Synchronisierte übersetzte Assets mit der englischen Quelle der Wahrheit ohne vollständige Neuübersetzung. Stellt sicher, dass Invarianten (Code, HTML) und exakte Strukturen über 11 Sprachen erhalten bleiben.<br><br>→ [Vollständige Dokumentation](./skills/l10n-sync/README.md) |

> **Hinweis:** Jeder Skill wird mit einer eigenen detaillierten README ausgeliefert. Die Hauptseite gibt den Überblick; tauchen Sie in `./skills/<skill>/README.md` für tiefe Nutzung, Berichtsbeispiele und Garantien ein.

## Installation

Jeder Skill wird auf dieselbe Weise installiert — wählen Sie den, den Sie brauchen:

```bash
npx skills add bastndev/skills --skill start-package   # Start  — scaffold a TS npm package
npx skills add bastndev/skills --skill start-astro     # Start  — scaffold an Astro project
npx skills add bastndev/skills --skill skrapi          # Start  — study & document any codebase
npx skills add bastndev/skills --skill middle          # Middle — score & improve one dimension
npx skills add bastndev/skills --skill end             # End    — audit & safely refactor
npx skills add bastndev/skills --skill l10n-sync       # Utility — sync localized assets safely
```

## So funktioniert der End-Skill

`end` ist der reifste Skill in der Suite. Hier sein Workflow von Anfang bis Ende:

1. **Zuerst Analyse** — Kartiert Einstiegspunkte und versteht das Projekt. **Keine Dateien werden geändert.**
2. **Strukturierter Bericht** — Klare Ergebnisse, klassifiziert in Bugs (mit Schweregrad), Schulden/Risiken und Vorschläge, plus ein bewerteter Gesundheitsüberblick, eine Architektur-Empfehlung und ein geordneter Plan — alle untermauert durch konkrete Datei + Zeilen-Referenzen.
3. **Sie genehmigen jede Phase** — Es wird **genau eine Phase** gleichzeitig ausgeführt. Nach jeder Phase erhalten Sie eine präzise Zusammenfassung der Änderungen, durchgeführte Validierungen und die Liste der verbleibenden Phasen.
4. **Volle Kontrolle & Sicherheit** — Erstellt nie Tests, wenn das Projekt keine hatte. Fügt keine Abhängigkeiten hinzu oder ändert den Paketmanager ohne Genehmigung. Respektiert Ihre uncommitted Arbeit und bewahrt immer das aktuelle Verhalten, es sei denn, ein gerechtfertigter Bug wird behoben.

Den vollständigen Workflow, exakte Berichtsformate (einschließlich der erforderlichen Abschlussblöcke), Architektur-Entscheidungsregeln und alle Sicherheitsgarantien finden Sie in der speziellen Skill-Dokumentation:

→ **[End – Refactor Project](./skills/end/README.md)**

Die vollständige interne Spezifikation findet sich in [skills/end/SKILL.md](./skills/end/SKILL.md).

## Roadmap

- **Start** — `start-package` (Scaffold), `start-astro` (Astro-Scaffold) und `skrapi` (bestehende Codebasis studieren) sind heute verfügbar; weitere `start-*`-Generatoren sind auf dem Weg.
- **Middle** — `middle` ist heute verfügbar (Gesundheitsüberblick + sechs nummerierte Fokus-Verbesserer); tiefere pro-Fokus-Werkzeuge sind geplant.
- **End** — `end` ist heute verfügbar; weitere Laufzeiten, zusätzliche spezialisierte Refactoring-Modi und Utilities sind geplant.
- **Utility** — `l10n-sync` ist heute für disziplinierte, token-effiziente Workspace-Lokalisierung verfügbar.

Jeder Skill wird mit eigener Dokumentation ausgeliefert (wie das aktuelle [End – Refactor Project](./skills/end/README.md)).

---

<br>

<div align="center">
  <p align="center">
  <sub>Entwickelt für Entwickler, die wollen, dass ihre KI-Agenten mit der Disziplin eines Senior Engineers handeln.</sub>
</p>

_Wenn Sie Fehler finden oder Feedback haben, zögern Sie nicht, ein [Issue zu eröffnen](https://github.com/bastndev/skills/issues/new)._

<sub>Hergestellt in 🇵🇪 von <a href="https://gohit.xyz">Gohit X</a> · Lizenziert unter <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a></sub>

</div>
