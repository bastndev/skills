<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/logo.webp" width="180" />
</p>

<h1 align="center">시작 / 중간 / 끝</h1>

<p align="center">
  <a href="https://github.com/bastndev/skills/blob/main/README.md">English 🇺🇸</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_ES.md">Español 🇪🇸</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_ZH.md">中文 🇨🇳</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_DE.md">Deutsch 🇩🇪</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_FR.md">Français 🇫🇷</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_JA.md">日本語 🇯🇵</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_PT.md">Português 🇧🇷</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_RU.md">Русский 🇷🇺</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_VI.md">Tiếng Việt 🇻🇳</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_HI.md">हिन्दी 🇮🇳</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_AR.md">العربية 🇸🇦</a>
</p>

<br>

<p align="center">
  자신 있게 새 프로젝트를 부트스트랩하세요. 프로젝트가 성장함에 따라 반복적으로 다듬고 강화하세요. 아키텍처가 진화해야 할 때 깊고 안전한 리팩터링을 수행하세요.
</p>

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

## 세 가지 단계

| 단계 | 목적 | 주요 기능 | 예시 스킬 | 상태 |
| --- | --- | --- | --- | --- |
| **Start** | 프로젝트 초기화 | 프로덕션 준비 폴더 구조 생성, 프레임워크 초기화, 첫 커밋부터 모범 사례 적용. | `start-nextjs`... | 계획됨 |
| **Middle** | 지속적인 개선 | UI/UX 향상, 보안 강화, 성능 향상, 로직 정리, 데드 코드 제거. | TBD | 계획됨 |
| **End** | 감사, 진단 및 리팩터링 | 전체 아키텍처 및 품질 분석. **명시적인 승인 하에** 실행되는 우선순위가 지정된 단계별 계획. | `refactor-project` | ✅ 사용 가능 |

## 사용 가능한 스킬

| 스킬 | 설명 |
| --- | --- |
| **[end](../../skills/end/README.md)** | **`refactor-project`** — 프로젝트의 처음부터 끝까지 이해합니다. 구체적인 참조와 함께 명확한 진단을 제공합니다. 올바른 아키텍처 방향을 권장하고 질서 있는 실행 계획을 구축합니다. 모든 권한은 여러분에게 있습니다.<br><br>→ [전체 문서 및 예제](../../skills/end/README.md) |

> **참고:** 각 스킬에는 자체적인 자세한 README가 제공됩니다. 루트 페이지는 개요를 제공합니다. 심층적인 사용법, 보고서 예시 및 보증에 대해서는 `../../skills/<skill>/README.md`를 참조하세요.

## 설치

```bash
# 현재 스킬 추가 (End / refactor-project)
npx skills add bastndev/skills --skill end
```

향후 스킬도 동일한 방식으로 설치할 수 있습니다:

```bash
npx skills add bastndev/skills --skill start-nextjs
```

## End 스킬의 작동 방식

1. **분석 우선** — 진입점을 매핑하고 프로젝트를 이해합니다. **파일은 수정되지 않습니다.**
2. **구조화된 보고서** — 4가지 범주(심각도가 있는 확인된 버그, 위험, 리팩토링 기회, 기술 부채)의 명확한 결과 + 아키텍처 권장 사항 및 정렬된 계획. 모든 항목에는 구체적인 파일 및 줄 참조가 포함됩니다.
3. **각 단계를 승인합니다** — 한 번에 **정확히 한 단계**만 실행합니다. 각 단계 후에는 변경 사항의 정확한 요약, 수행된 검증 및 남은 단계 목록을 받게 됩니다.
4. **완벽한 제어 및 안전성** — 프로젝트에 테스트가 없는 경우 테스트를 만들지 않습니다. 허가 없이 종속성을 추가하거나 패키지 관리자를 변경하지 않습니다. 커밋되지 않은 작업을 존중하며 정당한 버그를 수정하지 않는 한 항상 현재 동작을 유지합니다.

전체 워크플로, 정확한 보고서 형식, 아키텍처 결정 규칙 및 모든 안전 보증에 대해서는 전용 스킬 문서를 읽어보세요:

→ **[End – Refactor Project](../../skills/end/README.md)**

전체 내부 사양은 [skills/end/SKILL.md](../../skills/end/SKILL.md)에 있습니다.

## 로드맵

- **Start 스킬** — 인기 스택(Next.js, Vite, FastAPI 등)을 위한 단일 명령 프로젝트 스캐폴딩.
- **Middle 스킬** — 온디맨드 집중 개선(성능, 보안, UX, 데드 코드 제거 등).
- **End 확장** — 더 많은 런타임, 추가 전용 리팩토링 모드 및 유틸리티.

각 스킬에는 고유한 전용 문서가 있습니다(현재의 [End – Refactor Project](../../skills/end/README.md) 참조).

---

<br>

<div align="center">
  <p align="center">
  <sub>AI 에이전트가 시니어 엔지니어의 규율에 따라 행동하기를 원하는 개발자를 위해 구축되었습니다.</sub>
</p>

_If you find any bugs or have feedback, feel free to [open an issue](https://github.com/bastndev/skills/issues/new)._

<sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a></sub>

</div>
