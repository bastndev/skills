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
  Lancez de nouveaux projets en toute confiance. Affinez et renforcez-les de manière itérative à mesure qu'ils grandissent. Effectuez des refactorisations profondes et sûres lorsque l'architecture doit évoluer.
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

## Les trois phases

| Phase | Objectif | Capacités clés | Compétences d'exemple | Statut |
| ---------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------ |
| **Start** | Démarrer un projet — créer un nouveau projet ou apprendre d'un existant | Créez des structures et configurations prêtes pour la production dès le commit #1. Ou analysez l'architecture et les packages d'un codebase existant et documentez-le, pour réutiliser ce qui fonctionne dans votre propre projet. | `start-package`, `start-astro`, `skrapi` | ㅤㅤ✅ |
| **Middle** | Amélioration continue et perfectionnement | Évaluez le projet (aperçu santé de 0–100), puis améliorez **une dimension à la fois** — performance, UI/UX, propreté (ordre des fichiers + hygiène des commentaires), sécurité, structure, nettoyage ou qualité du code — avec un plan ciblé exécuté uniquement lorsque vous tapez `go`. | `middle` | ㅤㅤ✅ |
| **End** | Audit, diagnostic et refactorisation sûre | Analyse complète de l'architecture et de la qualité. Résultats classés avec preuves au niveau fichier. Plan par phases priorisé exécuté **uniquement avec approbation explicite**. Préservation du comportement. Support multi-runtime. | `end` | ㅤㅤ✅ |

## Compétences disponibles

Listées dans l'ordre naturel où vous auriez besoin d'elles — **Commencez** quelque chose de nouveau (ou étudiez un codebase existant pour inspiration), affinez-le au **Milieu**, et renforcez-le à la **Fin**.

| Compétence | Description |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[start-package](./skills/start-package/README.md)** | _Start_ — Génère un package TypeScript **double ESM + CJS** publiable avec déclarations de types regroupées, une compilation `tsup` sans configuration et TypeScript fixé à `5.x` pour compiler proprement en CLI et dans l'éditeur. Génère `package.json`, `tsconfig.json`, la configuration tsup, un test de fumée et les paramètres `.vscode`, puis installe, compile et vérifie.<br><br>→ [Documentation complète](./skills/start-package/README.md) |
| **[start-astro](./skills/start-astro/README.md)** | _Start_ — Génère un nouveau projet Astro en utilisant le template `minimal`, superposé avec une architecture propre et **évolutive** — prêt à passer d'un portfolio à une application complète. Configure un layout partagé, header, footer, pages, bascule thème clair/sombre, View Transitions natives, alias de chemin et Content Collections prêts à l'emploi.<br><br>→ [Documentation complète](./skills/start-astro/README.md) |
| **[skrapi](./skills/skrapi/README.md)** | _Start_ — Pointez-le vers un projet que vous admirez et il cartographie comment ce codebase est construit dans un dossier fixe `SKRAPI/` de Markdown ciblé — architecture, dépendances et prompts prêts à coller — pour que vous puissiez emprunter les modèles qui correspondent à votre propre projet avant de commencer. Fonctionne sur n'importe quel stack (web, mobile, extension, librairie, monorepo) ; chaque description est vérifiée contre le vrai code, jamais devinée par nom de package. Sortie multilingue (🇪🇸 ES · 🇺🇸 EN · 🇨🇳 ZH).<br><br>→ [Documentation complète](./skills/skrapi/README.md) |
| **[middle](./skills/middle/README.md)** | _Middle_ — Améliorateurs numérotés à la demande pour le développement actif. `0` évalue votre projet ou dossier avec un aperçu santé de 0–100 et pointe la zone la plus faible ; `1–7` qualifie chacun une dimension (⚡ performance · 🎨 ui-ux · 🗂️ propreté · 🔒 sécurité · 🏗️ structure · 🧹 nettoyage · 🧩 qualité), rapporte des constatations étayées et propose un plan de correction — exécuté phase par phase uniquement quand vous tapez `go`.<br><br>→ [Documentation complète](./skills/middle/README.md) |
| **[end](./skills/end/README.md)** | _End_ — Comprend votre projet de bout en bout. Fournit un diagnostic clair (bugs confirmés, risques, opportunités, dette technique) avec des références concrètes, recommande la bonne direction architecturale pour _ce_ codebase et construit un plan d'exécution ordonné. Chaque changement se produit dans une phase isolée et révisable — il ne procède que quand vous tapez `go`, `start` ou `proceed`, et aucun fichier n'est touché pendant l'analyse.<br><br>→ [Documentation complète et exemples](./skills/end/README.md) |
| **[l10n-sync](./skills/l10n-sync/README.md)** | _Utility_ — La compétence de localisation disciplinée et économe en tokens. Synchronise les assets traduits avec la source anglaise sans retraduction complète. Garantit les invariants (code, HTML) et structures exactes préservées dans 11 langues.<br><br>→ [Documentation complète](./skills/l10n-sync/README.md) |

> **Note :** Chaque compétence est livrée avec son propre README détaillé. La page racine donne l'aperçu de haut niveau ; plongez dans `./skills/<skill>/README.md` pour une utilisation approfondie, des exemples de rapports et des garanties.

## Installation

Chaque compétence s'installe de la même manière — choisissez celle dont vous avez besoin :

```bash
npx skills add bastndev/skills --skill start-package   # Start  — scaffold a TS npm package
npx skills add bastndev/skills --skill start-astro     # Start  — scaffold an Astro project
npx skills add bastndev/skills --skill skrapi          # Start  — study & document any codebase
npx skills add bastndev/skills --skill middle          # Middle — score & improve one dimension
npx skills add bastndev/skills --skill end             # End    — audit & safely refactor
npx skills add bastndev/skills --skill l10n-sync       # Utility — sync localized assets safely
```

## Comment fonctionne la compétence End

`end` est la compétence la plus mature de la suite. Voici son flux de travail de bout en bout :

1. **Analyse d'abord** — Cartographie les points d'entrée et comprend le projet. **Aucun fichier n'est modifié.**
2. **Rapport structuré** — Constatations claires classées en Bugs (avec gravité), Dette/Risques et Suggestions, plus un aperçu santé noté, une recommandation architecturale et un plan ordonné — le tout étayé par des références concrètes fichier + ligne.
3. **Vous autorisez chaque phase** — Il exécute **exactement une phase** à la fois. Après chaque phase, vous obtenez un résumé précis des changements, validations effectuées et la liste des phases restantes.
4. **Contrôle total et sécurité** — Ne crée jamais de tests si le projet n'en avait pas. N'ajoute jamais de dépendances ni ne change le gestionnaire de paquets sans permission. Respecte votre travail non commit et préserve toujours le comportement actuel sauf pour corriger un bug justifié.

Pour le flux complet, les formats de rapports exacts (y compris les blocs de clôture requis), les règles de décision architecturale et toutes les garanties de sécurité, lisez la documentation dédiée à la compétence :

→ **[End – Refactor Project](./skills/end/README.md)**

La spécification interne complète se trouve dans [skills/end/SKILL.md](./skills/end/SKILL.md).

## Feuille de route

- **Start** — `start-package` (scaffold), `start-astro` (scaffold Astro) et `skrapi` (étudier un codebase existant) sont disponibles aujourd'hui ; plus de générateurs `start-*` sont en route.
- **Middle** — `middle` est disponible aujourd'hui (aperçu santé + six améliorateurs numérotés) ; des outils plus profonds par dimension sont prévus.
- **End** — `end` est disponible aujourd'hui ; plus de runtimes, modes de refactorisation spécialisés supplémentaires et utilitaires sont prévus.
- **Utility** — `l10n-sync` est disponible aujourd'hui pour une localisation disciplinée et économe en tokens.

Chaque compétence est livrée avec sa propre documentation dédiée (comme l'actuel [End – Refactor Project](./skills/end/README.md)).

---

<br>

<div align="center">
  <p align="center">
  <sub>Conçu pour les développeurs qui veulent que leurs agents IA agissent avec la discipline d'un ingénieur senior.</sub>
</p>

_Si vous trouvez des bugs ou avez des commentaires, n'hésitez pas à [ouvrir un issue](https://github.com/bastndev/skills/issues/new)._

<sub>Fait en 🇵🇪 par <a href="https://gohit.xyz">Gohit X</a> · Licencié sous <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a></sub>

</div>
