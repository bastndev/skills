<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/logo.webp" width="180" />
</p>

<h1 align="center">[Début] / Milieu / [Fin]</h1>

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
  Démarrez de nouveaux projets en toute confiance. Affinez-les et renforcez-les itérativement au fur et à mesure de leur croissance. Effectuez un refactoring profond et sûr lorsque l'architecture doit évoluer.
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

## Les Trois Phases

| Phase | Objectif | Capacités Clés | Exemples de Skills | Statut |
| ---------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------ |
| **Start** (Début) | Commencer un projet — structurer un nouveau ou apprendre d'un existant | Créez des structures et des configurations prêtes pour la production dès le commit #1. Ou analysez l'architecture et les paquets d'une base de code existante et documentez-la, afin de pouvoir réutiliser ce qui fonctionne dans votre propre projet. | `start-package`, `skrapi`       | ㅤㅤ✅ |
| **Middle** (Milieu) | Amélioration continue et perfectionnement | Améliorez l'UI/UX, renforcez la sécurité, augmentez les performances, nettoyez la logique et éliminez le code mort pendant le développement actif. | Améliorateurs ciblés (À venir) | Prévu |
| **End** (Fin) | Audit, diagnostic et refactoring sûr | Analyse complète de l'architecture et de la qualité. Découvertes catégorisées avec des preuves au niveau des fichiers. Plan priorisé en phases exécuté **uniquement avec une approbation explicite**. Préserve le comportement. Prise en charge de plusieurs environnements d'exécution. | `end` | ㅤㅤ✅ |

## Skills Disponibles

Listées dans l'ordre naturel dans lequel vous les utiliseriez — **Start** (Démarrez) quelque chose de nouveau (ou étudiez une base de code existante pour vous en inspirer), affinez-le au **Middle** (Milieu) et renforcez-le à la **End** (Fin).

| Skill | Description |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[start-package](../../skills/start-package/README.md)** | _Start_ (Début) — Structure un paquet TypeScript **double ESM + CJS** publiable avec des déclarations de type groupées, une compilation `tsup` sans configuration et TypeScript fixé à la version `5.x` pour qu'il se compile proprement à la fois dans la CLI et dans l'éditeur. Génère `package.json`, `tsconfig.json`, la configuration tsup, un test de fumée et les paramètres `.vscode`, puis installe, compile et vérifie.<br><br>→ [Documentation complète](../../skills/start-package/README.md) |
| **[skrapi](../../skills/skrapi/README.md)**               | _Start_ (Début) — Pointez-le sur un projet que vous admirez et il mappera la façon dont cette base de code est construite dans un dossier `SKRAPI/` fixe de Markdown ciblé — architecture, dépendances et invites (prompts) prêtes à être collées — afin que vous puissiez emprunter les modèles qui correspondent à votre propre projet avant de commencer. Fonctionne sur n'importe quelle stack (web, mobile, extension, bibliothèque, monorepo); chaque description est vérifiée par rapport au code réel, jamais devinée à partir du nom d'un paquet. Sortie multilingue (🇪🇸 ES · 🇺🇸 EN · 🇨🇳 ZH).<br><br>→ [Documentation complète](../../skills/skrapi/README.md) |
| **[end](../../skills/end/README.md)**                     | _End_ (Fin) — Comprend votre projet de bout en bout. Fournit un diagnostic clair (bugs confirmés, risques, opportunités, dette technique) avec des références concrètes, recommande la bonne direction architecturale pour _cette_ base de code et construit un plan d'exécution ordonné. Chaque changement se produit dans une phase isolée et révisable — il ne se poursuit que lorsque vous dites `go`, `start` ou `proceed`, et aucun fichier n'est touché pendant l'analyse.<br><br>→ [Documentation complète et exemples](../../skills/end/README.md) |

> **Remarque :** Chaque skill est livrée avec son propre README détaillé. La page racine donne un aperçu de haut niveau ; plongez dans `./skills/<skill>/README.md` pour une utilisation approfondie, des exemples de rapports et des garanties.

## Installation

Chaque skill s'installe de la même manière — choisissez celle dont vous avez besoin :

```bash
npx skills add bastndev/skills --skill start-package   # Start (Début) — structurer un paquet TS npm
npx skills add bastndev/skills --skill skrapi          # Start (Début) — étudier et documenter n'importe quelle base de code
npx skills add bastndev/skills --skill end             # End (Fin) — auditer et refactoriser en toute sécurité
```

## Comment fonctionne la Skill "End"

`end` est la skill la plus mature de la suite. Voici son flux de travail de bout en bout :

1. **Analyse d'abord** — Cartographie les points d'entrée et comprend le projet. **Zéro fichier n'est modifié.**
2. **Rapport structuré** — Des découvertes claires catégorisées en Bugs (avec gravité), Dettes/Risques et Suggestions, plus un aperçu de santé noté, une recommandation d'architecture et un plan ordonné — le tout soutenu par des références concrètes de fichiers et de lignes.
3. **Vous autorisez chaque phase** — Il exécute **exactement une phase** à la fois. Après chaque phase, vous obtenez un résumé précis des modifications, des validations effectuées et de la liste des phases restantes.
4. **Contrôle total et sécurité** — Ne crée jamais de tests si le projet n'en avait pas. N'ajoute jamais de dépendances et ne change jamais de gestionnaire de paquets sans autorisation. Respecte votre travail non validé (uncommitted) et préserve toujours le comportement actuel, sauf s'il corrige un bug justifié.

Pour connaître le flux de travail complet, les formats de rapport exacts (y compris les blocs de clôture requis), les règles de décision d'architecture et toutes les garanties de sécurité, lisez la documentation dédiée de la skill :

→ **[End – Refactoriser le Projet](../../skills/end/README.md)**

La spécification interne complète se trouve dans [skills/end/SKILL.md](../../skills/end/SKILL.md).

## Feuille de route

- **Start** (Début) — `start-package` (structuration) et `skrapi` (étude d'une base de code existante) sont disponibles dès aujourd'hui ; d'autres outils de structuration `start-*` sont en route.
- **Middle** (Milieu) — des améliorateurs ciblés à la demande (performances, sécurité, UX, suppression du code mort) sont prévus.
- **End** (Fin) — `end` est disponible dès aujourd'hui ; d'autres environnements d'exécution, des modes de refactoring spécialisés supplémentaires et des utilitaires sont prévus.

Chaque skill est livrée avec sa propre documentation dédiée (comme l'actuel [End – Refactoriser le Projet](../../skills/end/README.md)).

---

<br>

<div align="center">
  <p align="center">
  <sub>Construit pour les développeurs qui veulent que leurs agents d'IA agissent avec la discipline d'un ingénieur senior.</sub>
</p>

_Si vous trouvez des bugs ou si vous avez des commentaires, n'hésitez pas à [ouvrir un ticket](https://github.com/bastndev/skills/issues/new)._

<sub>Fait au 🇵🇪 par <a href="https://gohit.xyz">Gohit X</a> · Sous licence <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a></sub>

</div>
