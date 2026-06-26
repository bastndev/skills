<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/logo.webp" width="180" />
</p>

<h1 align="center">[Início] / Meio / [Fim]</h1>

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
  Inicie novos projetos com confiança. Refine-os e fortaleça-os iterativamente à medida que crescem. Realize refatorações profundas e seguras quando a arquitetura precisar evoluir.
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

## As Três Fases

| Fase | Propósito | Principais Recursos | Exemplos de Skills | Status |
| ---------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------ |
| **Start** (Início) | Iniciar um projeto — estruturar um novo ou aprender com um existente | Crie estruturas e configurações prontas para produção a partir do commit #1. Ou analise a arquitetura e os pacotes de uma base de código existente e documente-a, para que você possa reutilizar os padrões que funcionam em seu próprio projeto. | `start-package`, `start-astro`, `skrapi`       | ㅤㅤ✅ |
| **Middle** (Meio) | Melhoria contínua e polimento | Melhore a UI/UX, reforce a segurança, aumente o desempenho, limpe a lógica e elimine código morto durante o desenvolvimento ativo. | Aprimoradores focados (A definir) | Planejado |
| **End** (Fim) | Auditoria, diagnóstico e refatoração segura | Análise completa de arquitetura e qualidade. Descobertas categorizadas com evidências no nível do arquivo. Plano em fases priorizado e executado **apenas com aprovação explícita**. Preserva o comportamento. Suporte a múltiplos runtimes. | `end` | ㅤㅤ✅ |

## Skills Disponíveis

Listados na ordem natural em que você os usaria — **Start** (Inicie) algo novo (ou estude uma base de código existente como inspiração), refine-o no **Middle** (Meio) e fortaleça-o no **End** (Fim).

| Skill | Descrição |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[start-package](../../skills/start-package/README.md)** | _Start_ (Início) — Estrutura um pacote TypeScript **dual ESM + CJS** publicável com declarações de tipo empacotadas, um build `tsup` sem configuração e o TypeScript fixado na versão `5.x` para que seja compilado de forma limpa tanto na CLI quanto no editor. Gera `package.json`, `tsconfig.json`, configuração do tsup, um teste de fumaça e configurações `.vscode`, e em seguida instala, compila e verifica.<br><br>→ [Documentação completa](../../skills/start-package/README.md) |
| **[start-astro](../../skills/start-astro/README.md)** | _Start_ (Início) — Estrutura um novo projeto Astro usando o template `minimal`, sobreposto com uma arquitetura limpa e **escalável** — pronto para crescer de um portfólio para um aplicativo completo. Configura imediatamente um layout compartilhado, cabeçalho, rodapé, páginas, alternador de tema claro/escuro, View Transitions nativas, alias de caminho e Coleções de Conteúdo (Content Collections).<br><br>→ [Documentação completa](../../skills/start-astro/README.md) |
| **[skrapi](../../skills/skrapi/README.md)**               | _Start_ (Início) — Aponte-o para um projeto que você admira e ele mapeará como essa base de código é construída em uma pasta `SKRAPI/` fixa de Markdown focado — arquitetura, dependências e prompts prontos para colar — para que você possa emprestar os padrões que se adequam ao seu próprio projeto antes de começar. Funciona em qualquer stack (web, mobile, extensão, biblioteca, monorepo); toda descrição é verificada com código real, nunca adivinhada pelo nome de um pacote. Saída multilíngue (🇪🇸 ES · 🇺🇸 EN · 🇨🇳 ZH).<br><br>→ [Documentação completa](../../skills/skrapi/README.md) |
| **[end](../../skills/end/README.md)**                     | _End_ (Fim) — Entende seu projeto de ponta a ponta. Fornece um diagnóstico claro (bugs confirmados, riscos, oportunidades, dívida técnica) com referências concretas, recomenda a direção de arquitetura correta para _esta_ base de código e constrói um plano de execução ordenado. Cada alteração ocorre em uma fase isolada e revisável — ela só prossegue quando você diz `go`, `start` ou `proceed`, e nenhum arquivo é tocado durante a análise.<br><br>→ [Documentação completa e exemplos](../../skills/end/README.md) |

> **Nota:** Cada skill vem com seu próprio README detalhado. A página raiz dá uma visão geral de alto nível; mergulhe em `./skills/<skill>/README.md` para um uso profundo, exemplos de relatórios e garantias.

## Instalação

Cada skill é instalada da mesma forma — escolha a que você precisa:

```bash
npx skills add bastndev/skills --skill start-package   # Start (Início) — estrutura um pacote TS npm
npx skills add bastndev/skills --skill start-astro     # Start (Início) — estrutura um projeto Astro
npx skills add bastndev/skills --skill skrapi          # Start (Início) — estuda e documenta qualquer base de código
npx skills add bastndev/skills --skill end             # End (Fim) — audita e refatora com segurança
```

## Como a Skill "End" funciona

`end` é a skill mais madura da suíte. Veja seu fluxo de trabalho de ponta a ponta:

1. **Análise primeiro** — Mapeia os pontos de entrada e entende o projeto. **Nenhum arquivo é modificado.**
2. **Relatório estruturado** — Descobertas claras categorizadas em Bugs (com severidade), Dívidas/Riscos e Sugestões, além de uma visão geral de saúde pontuada, uma recomendação de arquitetura e um plano ordenado — tudo apoiado por referências concretas de arquivos e linhas.
3. **Você autoriza cada fase** — Executa **exatamente uma fase** por vez. Após cada fase, você obtém um resumo preciso das mudanças, validações realizadas e a lista de fases restantes.
4. **Controle total e segurança** — Nunca cria testes se o projeto não tiver nenhum. Nunca adiciona dependências ou altera o gerenciador de pacotes sem permissão. Respeita o seu trabalho não comitado (uncommitted) e sempre preserva o comportamento atual, a menos que corrija um bug justificado.

Para conhecer o fluxo de trabalho completo, os formatos exatos de relatórios (incluyendo os blocos de fechamento necessários), as regras de decisão de arquitetura e todas as garantias de segurança, leia a documentação dedicada da skill:

→ **[End – Refatorar Projeto](../../skills/end/README.md)**

A especificação interna completa encontra-se em [skills/end/SKILL.md](../../skills/end/SKILL.md).

## Roteiro

- **Start** (Início) — `start-package` (estruturação), `start-astro` (estruturador Astro) e `skrapi` (estudo de uma base de código existente) já estão disponíveis; mais ferramentas de estruturação `start-*` estão a caminho.
- **Middle** (Meio) — aprimoradores focados sob demanda (desempenho, segurança, UX, remoção de código morto) estão planejados.
- **End** (Fim) — `end` já está disponível; mais ambientes de execução, modos adicionais de refatoração especializados e utilitários estão planejados.

Cada skill vem com sua própria documentação dedicada (como o atual [End – Refatorar Projeto](../../skills/end/README.md)).

---

<br>

<div align="center">
  <p align="center">
  <sub>Construído para desenvolvedores que desejam que seus agentes de IA ajam com a disciplina de um engenheiro sênior.</sub>
</p>

_Se você encontrar algum bug ou tiver comentários, sinta-se à vontade para [abrir uma issue](https://github.com/bastndev/skills/issues/new)._

<sub>Feito no 🇵🇪 por <a href="https://gohit.xyz">Gohit X</a> · Licenciado sob <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a></sub>

</div>
