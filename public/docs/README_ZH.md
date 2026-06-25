<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/logo.webp" width="180" />
</p>

<h1 align="center">[开始] / 中期 / [结束]</h1>

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
  充满信心地启动新项目。在它们成长时不断迭代和加固。当架构需要演进时，执行深入、安全的重构。
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

## 三个阶段

| 阶段 | 目的 | 核心能力 | 示例技能 | 状态 |
| ---------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------ |
| **Start** (开始)| 启动项目 — 搭建新项目，或从现有项目中学习 | 从第一次提交开始创建生产就绪的结构和配置。或者分析现有代码库的架构和包并生成文档，以便在您自己的项目中复用有效的模式。 | `start-package`, `skrapi`       | ㅤㅤ✅ |
| **Middle** (中期)| 持续改进与打磨 | 在积极开发期间增强 UI/UX、加固安全性、提升性能、清理逻辑以及消除死代码。 | 目标增强工具 (待定) | 计划中 |
| **End** (结束)| 审计、诊断与安全重构 | 全面的架构和质量分析。包含文件级证据的分类发现。在**明确批准**后执行的优先级分阶段计划。保持行为一致。支持多运行时。 | `end` | ㅤㅤ✅ |

## 可用技能

按照您自然使用的顺序列出 — **Start** (开始) 一个新项目（或研究现有的代码库以获取灵感），在 **Middle** (中期) 进行打磨，并在 **End** (结束) 时进行加固。

| 技能 | 描述 |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[start-package](../../skills/start-package/README.md)** | _Start_ (开始) — 搭建一个可发布的 **双重 ESM + CJS** TypeScript 包，包含捆绑的类型声明、零配置的 `tsup` 构建，并将 TypeScript 固定在 `5.x` 版本，以便在 CLI 和编辑器中都能干净地构建。生成 `package.json`、`tsconfig.json`、tsup 配置、冒烟测试和 `.vscode` 设置，然后安装、构建并验证。<br><br>→ [完整文档](../../skills/start-package/README.md) |
| **[skrapi](../../skills/skrapi/README.md)**               | _Start_ (开始) — 将它指向您欣赏的项目，它会将该代码库的构建方式映射到一个固定的 `SKRAPI/` 文件夹，其中包含重点突出的 Markdown — 架构、依赖关系和可直接粘贴的提示（prompts） — 以便在开始之前借用适合您自己项目的模式。支持任何技术栈（web、移动、扩展、库、monorepo）；每个描述都经过真实代码验证，绝不从包名中猜测。多语言输出 (🇪🇸 ES · 🇺🇸 EN · 🇨🇳 ZH)。<br><br>→ [完整文档](../../skills/skrapi/README.md) |
| **[end](../../skills/end/README.md)**                     | _End_ (结束) — 端到端地理解您的项目。提供清晰的诊断（确认的错误、风险、机会、技术债务）并附有具体参考，为*该*代码库推荐正确的架构方向，并构建有序的执行计划。每一项变更都在孤立且可审查的阶段发生 — 只有在您说 `go`、`start` 或 `proceed` 时才会继续，且分析期间不会修改任何文件。<br><br>→ [完整文档和示例](../../skills/end/README.md) |

> **注意：** 每个技能都自带详细的 README。根页面提供高层次的概述；深入阅读 `./skills/<skill>/README.md` 以了解深入用法、报告示例和保障措施。

## 安装

每个技能的安装方式都一样 — 选择您需要的：

```bash
npx skills add bastndev/skills --skill start-package   # Start (开始) — 搭建 TS npm 包
npx skills add bastndev/skills --skill skrapi          # Start (开始) — 研究和记录任何代码库
npx skills add bastndev/skills --skill end             # End (结束) — 审计和安全重构
```

## "End" 技能如何运作

`end` 是套件中最成熟的技能。以下是其端到端的完整工作流程：

1. **分析优先** — 映射入口点并理解项目。**不修改任何文件。**
2. **结构化报告** — 分类清晰的发现，包括错误（含严重程度）、债务/风险和建议，外加评分健康概览、架构推荐和有序计划 — 所有这些都由具体的文件和行参考支持。
3. **您授权每个阶段** — 它每次**仅执行一个阶段**。每个阶段后，您将获得变更的精确摘要、执行的验证以及剩余阶段的列表。
4. **完全控制与安全** — 如果项目没有测试，则绝不创建测试。未经允许绝不添加依赖项或更改包管理器。尊重您未提交的工作，除非修复合理的错误，否则始终保留当前行为。

有关完整的工作流程、确切的报告格式（包括必需的结束块）、架构决策规则以及所有安全保障，请阅读专门的技能文档：

→ **[End – 重构项目](../../skills/end/README.md)**

完整的内部规范位于 [skills/end/SKILL.md](../../skills/end/SKILL.md)。

## 路线图

- **Start** (开始) — `start-package` (搭建) 和 `skrapi` (研究现有代码库) 现已发布；更多 `start-*` 搭建工具即将推出。
- **Middle** (中期) — 计划推出重点的按需改进工具（性能、安全性、UX、死代码消除）。
- **End** (结束) — `end` 现已发布；计划支持更多运行时、更多专门的重构模式和实用工具。

每个技能都会提供其专属文档（如当前的 [End – 重构项目](../../skills/end/README.md)）。

---

<br>

<div align="center">
  <p align="center">
  <sub>为那些希望其 AI 代理像资深工程师一样严谨行事的开发者打造。</sub>
</p>

_如果您发现任何错误或有反馈意见，请随时 [开启 Issue](https://github.com/bastndev/skills/issues/new)。_

<sub>在 🇵🇪 由 <a href="https://gohit.xyz">Gohit X</a> 制作 · 基于 <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a> 协议授权</sub>

</div>
