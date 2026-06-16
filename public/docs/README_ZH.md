<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/logo.webp" width="180" />
</p>

<h1 align="center">开始 / 中间 / 结束</h1>

<p align="center">
  <a href="https://github.com/bastndev/skills/blob/main/README.md">English 🇺🇸</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_ES.md">Español 🇪🇸</a> | 
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
  充满信心地启动新项目。在它们成长时不断优化和加固。在架构需要演进时进行深度且安全的重构。
</p>

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

## 三个阶段

| 阶段 | 目的 | 核心能力 | 技能示例 | 状态 |
| --- | --- | --- | --- | --- |
| **Start (开始)** | 项目初始化和脚手架 | 创建生产就绪的文件夹结构，初始化框架，从第一次提交开始应用最佳实践配置。 | `start-nextjs`, `start-vite`... | 计划中 |
| **Middle (中间)** | 持续改进和打磨 | 在活跃开发期间增强 UI/UX，加强安全，提升性能，清理逻辑，消除死代码。 | 针对性优化器 (待定) | 计划中 |
| **End (结束)** | 审计，诊断和安全重构 | 全面的架构和质量分析。优先级分阶段计划，**仅在明确批准下**执行。保留原有行为。 | `refactor-project` | ✅ 可用 |

## 可用技能

| 技能 | 描述 |
| --- | --- |
| **[end](../../skills/end/README.md)** | **`refactor-project`** — 深入了解你的项目。提供清晰的诊断和具体参考。推荐正确的架构方向并构建有序的执行计划。所有更改在隔离阶段进行，你拥有完全控制权。<br><br>→ [完整文档与示例](../../skills/end/README.md) |

> **注意：** 每个 skill 都有自己的详细 README。根页面提供高级概述；深入了解 `../../skills/<skill>/README.md` 以获取深入用法、报告示例和保证。

## 安装

```bash
# 安装 End skill (refactor-project)
npx skills add bastndev/skills --skill end
```

其他 skills（发布后）以相同方式安装：

```bash
npx skills add bastndev/skills --skill start-nextjs
```

## End Skill 如何工作

1. **首先分析** — 映射入口点并理解项目。**不修改任何文件。**
2. **结构化报告** — 在四个类别（带有严重性的已确认 Bug、风险、重构机会、技术债务）中提供清晰的发现 + 架构建议和有序的计划。所有项目都包括具体的文件和行参考。
3. **您授权每个阶段** — 它每次**仅执行一个阶段**。在每个阶段之后，您会获得关于更改的精确摘要、执行的验证以及剩余阶段的列表。
4. **完全控制和安全** — 如果项目没有测试，则绝不创建测试。未经许可绝不添加依赖项或更改包管理器。尊重您未提交的工作，并始终保留当前行为，除非修复合理的 bug。

有关完整工作流程、确切的报告格式（包括必需的闭包块）、架构决策规则以及所有安全保证，请阅读专用的 skill 文档：

→ **[End – Refactor Project](../../skills/end/README.md)**

完整的内部规范位于 [skills/end/SKILL.md](../../skills/end/SKILL.md)。

## 路线图

- **Start 技能** — 流行技术栈（Next.js、Vite、FastAPI 等）的单命令项目脚手架。
- **Middle 技能** — 重点关注按需改进（性能、安全、UX、死代码消除等）。
- **End 扩展** — 更多运行时、额外的专用重构模式和实用程序。

每个 skill 都有自己的专用文档（如当前的 [End – Refactor Project](../../skills/end/README.md)）。

---

<br>

<div align="center">
  <p align="center">
  <sub>专为希望其 AI 代理具备高级工程师纪律的开发者而构建。</sub>
</p>

_If you find any bugs or have feedback, feel free to [open an issue](https://github.com/bastndev/skills/issues/new)._

<sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a></sub>

</div>
