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
  새로운 프로젝트를 자신감 있게 시작하세요. 성장함에 따라 반복적으로 개선하고 강화합니다. 아키텍처가 발전해야 할 때 깊고 안전한 리팩토링을 수행합니다.
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

## 세 가지 단계

| 단계 | 목적 | 주요 기능 | 스킬 예시 | 상태 |
| ---------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------ |
| **Start** | 프로젝트 시작 — 새로 만들거나 기존 프로젝트에서 배우기 | 커밋 #1부터 프로덕션 준비가 된 구조와 설정을 만듭니다. 또는 기존 코드베이스의 아키텍처와 패키지를 분석하여 문서화하고, 자체 프로젝트에서 재사용할 수 있는 것을 파악합니다. | `start-package`, `start-astro`, `skrapi` | ㅤㅤ✅ |
| **Middle** | 지속적 개선 및 다듬기 | 프로젝트를 평가합니다 (0–100 건강 개요), 그 다음 **한번에 하나의 차원**을 개선합니다 — 성능, UI/UX, 정리 (파일 순서 + 코멘트 위생), 보안, 구조, 정리, 또는 코드 품질 — `go`를 입력할 때만 실행되는 집중 계획으로. | `middle` | ㅤㅤ✅ |
| **End** | 감사, 진단 및 안전한 리팩토링 | 전체 아키텍처 및 품질 분석. 파일 수준의 증거와 함께 분류된 발견 사항. **명시적 승인으로만** 실행되는 우선순위 지정된 단계별 계획. 동작 보존. 멀티 런타임 지원. | `end` | ㅤㅤ✅ |

## 사용 가능한 스킬

자연스러운 순서대로 나열 — **Start**로 새로운 것을 시작 (또는 영감을 위해 기존 코드베이스 연구), **Middle**에서 개선하고, **End**에서 강화합니다.

| 스킬 | 설명 |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[start-package](./skills/start-package/README.md)** | _Start_ — 번들된 타입 선언, 제로-config `tsup` 빌드, CLI와 편집기 모두에서 깔끔하게 빌드되도록 `5.x`로 고정된 TypeScript를 갖춘 출 가능한 **듀얼 ESM + CJS** TypeScript 패키지를 스캐폴딩합니다. `package.json`, `tsconfig.json`, tsup 설정, 스모크 테스트, `.vscode` 설정을 생성한 후 설치, 빌드, 검증합니다.<br><br>→ [전체 문서](./skills/start-package/README.md) |
| **[start-astro](./skills/start-astro/README.md)** | _Start_ — `minimal` 템플릿을 사용하여 새로운 Astro 프로젝트를 스캐폴딩하고, 깔끔하고 **확장 가능한** 아키텍처를 오버레이 — 포트폴리오에서 전체 앱으로 성장할 준비가 됩니다. 공유 레이아웃, 헤더, 푸터, 페이지, 라이트/다크 테마 전환, 네이티브 View Transitions, 경로 별칭, Content Collections을 바로 사용할 수 있도록 설정합니다.<br><br>→ [전체 문서](./skills/start-astro/README.md) |
| **[skrapi](./skills/skrapi/README.md)** | _Start_ — 좋아하는 프로젝트를 가리키면 해당 코드베이스가 고정된 `SKRAPI/` 폴더에 어떻게 구축되어 있는지 매핑 — 아키텍처, 의존성, 붙여넣기 가능한 프롬프트 — 시작 전에 자체 프로젝트에 맞는 패턴을 빌릴 수 있습니다. 모든 스택 (웹, 모바일, 확장 프로그램, 라이브러리, 모노레포)에서 작동; 모든 설명은 실제 코드를 대조하여 검증되며 패키지 이름으로 추측되지 않습니다. 다국어 출력 (🇪🇸 ES · 🇺🇸 EN · 🇨🇳 ZH).<br><br>→ [전체 문서](./skills/skrapi/README.md) |
| **[middle](./skills/middle/README.md)** | _Middle_ — 활발한 개발을 위한 번호 매긴 온디맨드 개선 도구. `0`은 프로젝트나 폴더를 0–100 건강 개요로 평가하고 가장 약한 영역을 지적; `1–7`은 각각 하나의 차원 (⚡ 성능 · 🎨 UI/UX · 🗂️ 정리 · 🔒 보안 · 🏗️ 구조 · 🧹 정리 · 🧩 품질)을 평가하고, 증거 기반 발견을 보고하며, 수정 계획을 제안 — `go`를 입력할 때만 단계별로 실행.<br><br>→ [전체 문서](./skills/middle/README.md) |
| **[end](./skills/end/README.md)** | _End_ — 프로젝트를 처음부터 끝까지 이해합니다. 명확한 진단 (확인된 버그, 위험, 기회, 기술 부채)을 구체적인 참조와 함께 제공하고, _이_ 코드베이스에 적합한 아키텍처 방향을 권장하며, 순서가 지정된 실행 계획을 구축합니다. 모든 변경은 격리되고 검토 가능한 단계에서 발생 — `go`, `start`, `proceed`를 입력할 때만 진행되며 분석 중에는 파일이 건드려지지 않습니다.<br><br>→ [전체 문서 및 예시](./skills/end/README.md) |
| **[l10n-sync](./skills/l10n-sync/README.md)** | _Utility_ — 엄격하고 토큰 효율적인 로컬라이제이션 스킬. 완전한 파일 재번역 없이 영어 진실 소스와 번역된 자산을 동기화합니다. 11개 언어에 걸쳐 불변 요소 (코드, HTML)와 정확한 구조가 보존됨을 보장합니다.<br><br>→ [전체 문서](./skills/l10n-sync/README.md) |

> **참고:** 각 스킬에는 자체 상세 README가 포함되어 있습니다. 루트 페이지는 높은 수준의 개요를 제공합니다. 자세한 사용법, 보고서 예시, 보증은 `./skills/<skill>/README.md`를 참조하세요.

## 설치

각 스킬은 같은 방식으로 설치됩니다 — 필요한 것을 선택하세요:

```bash
npx skills add bastndev/skills --skill start-package   # Start  — scaffold a TS npm package
npx skills add bastndev/skills --skill start-astro     # Start  — scaffold an Astro project
npx skills add bastndev/skills --skill skrapi          # Start  — study & document any codebase
npx skills add bastndev/skills --skill middle          # Middle — score & improve one dimension
npx skills add bastndev/skills --skill end             # End    — audit & safely refactor
npx skills add bastndev/skills --skill l10n-sync       # Utility — sync localized assets safely
```

## End 스킬의 작동 방식

`end`는 스위트에서 가장 성숙한 스킬입니다. 전체 워크플로우를 소개합니다:

1. **먼저 분석** — 진입점을 매핑하고 프로젝트를 이해합니다. **파일이 수정되지 않습니다.**
2. **구조화된 보고서** — 심각도별 버그, 부채/위험, 제안으로 분류된 명확한 발견 사항과 함께 점수화된 건강 개요, 아키텍처 권장 사항, 순서 지정된 계획 — 모두 구체적인 파일+행 참조로 뒷받침됩니다.
3. **각 단계를 승인** — **정확히 하나의 단계**를 한 번에 실행합니다. 각 단계 후 변경 사항, 수행된 검증, 남은 단계 목록의 정확한 요약을 받습니다.
4. **완전한 제어 및 안전** — 프로젝트에 테스트가 없으면 생성하지 않습니다. 허가 없이 의존성을 추가하거나 패키지 관리자를 변경하지 않습니다. 커밋되지 않은 작업을 존중하고 정당한 버그를 수정하는 경우를 제외하고 항상 현재 동작을 보존합니다.

전체 워크플로우, 정확한 보고서 형식 (필수 마감 블록 포함), 아키텍처 의사 결정 규칙 및 모든 안전 보증에 대해서는 전용 스킬 문서를 읽으세요:

→ **[End – Refactor Project](./skills/end/README.md)**

전체 내부 사양은 [skills/end/SKILL.md](./skills/end/SKILL.md)에 있습니다.

## 로드맵

- **Start** — `start-package` (스캐폴드), `start-astro` (Astro 스캐폴드), `skrapi` (기존 코드베이스 연구)가 오늘 출시; 더 많은 `start-*` 스캐폴더가 준비 중.
- **Middle** — `middle`이 오늘 출시 (건강 개요 + 6개 번호 매긴 초점 개선 도구); 더 깊은 차원별 도구가 계획되어 있습니다.
- **End** — `end`가 오늘 출시; 추가 런타임, 추가 전문 리팩토링 모드, 유틸리티가 계획되어 있습니다.
- **Utility** — `l10n-sync`가 오늘 출시. 엄격하고 토큰 효율적인 워크스페이스 로컬라이제이션용.

각 스킬에는 자체 전용 문서가 포함되어 있습니다 (현재 [End – Refactor Project](./skills/end/README.md)처럼).

---

<br>

<div align="center">
  <p align="center">
  <sub>시니어 엔지니어의 규율로 AI 에이전트가 행동하기를 원하는 개발자를 위해 구축되었습니다.</sub>
</p>

_버그를 발견하거나 피드백이 있으시면 [issue를 열어주세요](https://github.com/bastndev/skills/issues/new)._

<sub>🇵🇪에서 <a href="https://gohit.xyz">Gohit X</a>가 제작 · <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a> 라이선스</sub>

</div>
