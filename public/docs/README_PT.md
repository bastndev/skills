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
  Inicie novos projetos com confiança. Refine e fortaleça iterativamente à medida que crescem. Realize refatorações profundas e seguras quando a arquitetura precisar evoluir.
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

## As três fases

| Fase | Propósito | Capacidades-chave | Skills de exemplo | Status |
| ---------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------ |
| **Start** | Iniciar um projeto — criar um novo ou aprender de um existente | Crie estruturas e configurações prontas para produção desde o commit #1. Ou analise a arquitetura e pacotes de um codebase existente e documente o que funciona, para reutilizar no seu próprio projeto. | `start-package`, `start-astro`, `skrapi` | ㅤㅤ✅ |
| **Middle** | Melhoria contínua e acabamento | Avalie o projeto (visão geral de saúde 0–100), então melhore **uma dimensão por vez** — desempenho, UI/UX, organização (ordem de arquivos + higiene de comentários), segurança, estrutura, limpeza ou qualidade de código — com um plano focado executado apenas quando você digitar `go`. | `middle` | ㅤㅤ✅ |
| **End** | Auditoria, diagnóstico e refatoração segura | Análise completa de arquitetura e qualidade. Constatações categorizadas com evidências no nível de arquivo. Plano por fases priorizado executado **apenas com aprovação explícita**. Preservação de comportamento. Suporte multi-runtime. | `end` | ㅤㅤ✅ |

## Skills disponíveis

Listadas na ordem natural em que você as usaria — **Comece** algo novo (ou estude um codebase existente para inspiração), refine no **Meio**, e fortaleça no **Fim**.

| Skill | Descrição |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[start-package](./skills/start-package/README.md)** | _Start_ — Gera um pacote TypeScript **dual ESM + CJS** publicável com declarações de tipo empacotadas, uma compilação `tsup` sem configuração e TypeScript fixado em `5.x` para compilar limpo tanto no CLI quanto no editor. Gera `package.json`, `tsconfig.json`, configuração do tsup, um teste de fumaça e configurações `.vscode`, depois instala, compila e verifica.<br><br>→ [Documentação completa](./skills/start-package/README.md) |
| **[start-astro](./skills/start-astro/README.md)** | _Start_ — Gera um novo projeto Astro usando o template `minimal`, sobreposto com uma arquitetura limpa e **escalável** — pronto para crescer de um portfólio para um app completo. Configura um layout compartilhado, header, footer, páginas, alternância de tema claro/escuro, View Transitions nativas, alias de caminho e Content Collections prontos para uso.<br><br>→ [Documentação completa](./skills/start-astro/README.md) |
| **[skrapi](./skills/skrapi/README.md)** | _Start_ — Aponte para um projeto que você admira e ele mapeia como esse codebase é construído em uma pasta fixa `SKRAPI/` de Markdown focado — arquitetura, dependências e prompts prontos para colar — para que você possa pegar os padrões que se encaixam no seu projeto antes de começar. Funciona em qualquer stack (web, mobile, extensão, biblioteca, monorepo); cada descrição é verificada contra o código real, nunca adivinhada pelo nome do pacote. Saída multilíngue (🇪🇸 ES · 🇺🇸 EN · 🇨🇳 ZH).<br><br>→ [Documentação completa](./skills/skrapi/README.md) |
| **[middle](./skills/middle/README.md)** | _Middle_ — Melhoradores numerados sob demanda para desenvolvimento ativo. `0` avalia seu projeto ou pasta com uma visão geral de saúde 0–100 e aponta a área mais fraca; `1–7` qualifica cada um uma dimensão (⚡ desempenho · 🎨 ui-ux · 🗂️ organização · 🔒 segurança · 🏗️ estrutura · 🧹 limpeza · 🧩 qualidade), relata constatações baseadas em evidências e propõe um plano de correção — executado fase por fase apenas quando você digita `go`.<br><br>→ [Documentação completa](./skills/middle/README.md) |
| **[end](./skills/end/README.md)** | _End_ — Entende seu projeto de ponta a ponta. Fornece um diagnóstico claro (bugs confirmados, riscos, oportunidades, dívida técnica) com referências concretas, recomenda a direção arquitetônica correta para _este_ codebase e constrói um plano de execução ordenado. Cada mudança acontece em uma fase isolada e revisável — só prossegue quando você digita `go`, `start` ou `proceed`, e nenhum arquivo é tocado durante a análise.<br><br>→ [Documentação completa e exemplos](./skills/end/README.md) |
| **[l10n-sync](./skills/l10n-sync/README.md)** | _Utility_ — A skill disciplinada e eficiente em tokens para localização. Sincroniza assets traduzidos com a fonte inglesa sem retradução de arquivo completo. Garante invariantes (código, HTML) e estruturas exatas preservadas em 11 idiomas.<br><br>→ [Documentação completa](./skills/l10n-sync/README.md) |

> **Nota:** Cada skill vem com seu próprio README detalhado. A página raiz fornece a visão geral de alto nível; aprofunde-se em `./skills/<skill>/README.md` para uso detalhado, exemplos de relatórios e garantias.

## Instalação

Cada skill é instalada da mesma maneira — escolha a que você precisa:

```bash
npx skills add bastndev/skills --skill start-package   # Start  — scaffold a TS npm package
npx skills add bastndev/skills --skill start-astro     # Start  — scaffold an Astro project
npx skills add bastndev/skills --skill skrapi          # Start  — study & document any codebase
npx skills add bastndev/skills --skill middle          # Middle — score & improve one dimension
npx skills add bastndev/skills --skill end             # End    — audit & safely refactor
npx skills add bastndev/skills --skill l10n-sync       # Utility — sync localized assets safely
```

## Como a skill End funciona

`end` é a skill mais madura da suíte. Aqui está seu fluxo de trabalho completo:

1. **Análise primeiro** — Mapeia pontos de entrada e entende o projeto. **Nenhum arquivo é modificado.**
2. **Relatório estruturado** — Constatações claras categorizadas em Bugs (com severidade), Dívida/Riscos e Sugestões, mais uma visão geral de saúde pontuada, uma recomendação arquitetônica e um plano ordenado — todos apoiados por referências concretas de arquivo + linha.
3. **Você autoriza cada fase** — Executa **exatamente uma fase** por vez. Após cada fase, você recebe um resumo preciso das mudanças, validações realizadas e a lista de fases restantes.
4. **Controle total e segurança** — Nunca cria testes se o projeto não tinha. Nunca adiciona dependências ou muda o gerenciador de pacotes sem permissão. Respeita seu trabalho não commitado e sempre preserva o comportamento atual, a menos que corrija um bug justificado.

Para o fluxo completo, formatos exatos de relatório (incluindo os blocos de fechamento obrigatórios), regras de decisão arquitetônica e todas as garantias de segurança, leia a documentação dedicada da skill:

→ **[End – Refactor Project](./skills/end/README.md)**

A especificação interna completa está em [skills/end/SKILL.md](./skills/end/SKILL.md).

## Roteiro

- **Start** — `start-package` (scaffold), `start-astro` (scaffold Astro) e `skrapi` (estudar um codebase existente) disponíveis hoje; mais geradores `start-*` estão a caminho.
- **Middle** — `middle` disponível hoje (visão geral de saúde + seis melhoradores numerados); ferramentas mais profundas por dimensão estão planejadas.
- **End** — `end` disponível hoje; mais runtimes, modos de refatoração especializados adicionais e utilitários estão planejados.
- **Utility** — `l10n-sync` disponível hoje para localização disciplinada e eficiente em tokens.

Cada skill vem com sua própria documentação dedicada (como o atual [End – Refactor Project](./skills/end/README.md)).

---

<br>

<div align="center">
  <p align="center">
  <sub>Feito para desenvolvedores que querem que seus agentes de IA atuem com a disciplina de um engenheiro sênior.</sub>
</p>

_Se você encontrar bugs ou tiver feedback, sinta-se à vontade para [abrir um issue](https://github.com/bastndev/skills/issues/new)._

<sub>Feito em 🇵🇪 por <a href="https://gohit.xyz">Gohit X</a> · Licenciado sob <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a></sub>

</div>
