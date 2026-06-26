<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/logo.webp" width="180" />
</p>

<h1 align="center">[시작] / 중간 / [끝]</h1>

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
  자신감을 가지고 새 프로젝트를 시작하세요. 프로젝트가 성장함에 따라 반복적으로 개선하고 강화하십시오. 아키텍처가 진화해야 할 때 깊고 안전한 리팩토링을 수행하십시오.
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

| 단계 | 목적 | 주요 기능 | 예시 스킬 | 상태 |
| ---------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------ |
| **Start** (시작) | 프로젝트 시작 — 새로 스캐폴딩하거나 기존 프로젝트에서 학습 | 커밋 #1부터 프로덕션 준비가 된 구조와 설정을 만듭니다. 또는 기존 코드베이스의 아키텍처 및 패키지를 분석하고 문서화하여 작동하는 패턴을 자신의 프로젝트에서 재사용할 수 있습니다. | `start-package`, `start-astro`, `skrapi`       | ㅤㅤ✅ |
| **Middle** (중간) | 지속적인 개선 및 다듬기 | 활발한 개발 중에 UI/UX 향상, 보안 강화, 성능 향상, 로직 정리 및 데드 코드 제거를 수행합니다. | 대상 강화 도구 (미정) | 계획됨 |
| **End** (끝) | 감사, 진단 및 안전한 리팩토링 | 전체 아키텍처 및 품질 분석. 파일 수준의 증거가 있는 분류된 조사 결과. **명시적 승인이 있을 때만** 실행되는 우선순위가 지정된 단계별 계획. 동작 유지. 다중 런타임 지원. | `end` | ㅤㅤ✅ |

## 사용 가능한 스킬

자연스럽게 손이 가는 순서대로 나열됨 — 새로운 것을 **Start** (시작) 하고 (또는 영감을 얻기 위해 기존 코드베이스를 연구하고), **Middle** (중간) 에 다듬고, **End** (끝) 에 강화합니다.

| 스킬 | 설명 |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[start-package](../../skills/start-package/README.md)** | _Start_ (시작) — 번들형 타입 선언, 설정이 필요 없는 `tsup` 빌드, CLI와 에디터 모두에서 깔끔하게 빌드되도록 `5.x`로 고정된 TypeScript를 포함하여 게시 가능한 **이중 ESM + CJS** TypeScript 패키지를 스캐폴딩합니다. `package.json`, `tsconfig.json`, tsup 설정, 스모크 테스트 및 `.vscode` 설정을 생성한 다음 설치, 빌드 및 검증을 수행합니다.<br><br>→ [전체 문서](../../skills/start-package/README.md) |
| **[start-astro](../../skills/start-astro/README.md)** | _Start_ (시작) — `minimal` 템플릿을 사용하여 새로운 Astro 프로젝트를 스캐폴딩하고, 깔끔하고 **확장 가능한** 아키텍처를 오버레이합니다. 포트폴리오에서 완전한 앱으로 성장할 준비가 되어 있습니다. 공유 레이아웃, 헤더, 푸터, 페이지, 라이트/다크 테마 토글, 네이티브 View Transitions, 경로 별칭 및 콘텐츠 컬렉션(Content Collections)을 기본적으로 설정합니다.<br><br>→ [전체 문서](../../skills/start-astro/README.md) |
| **[skrapi](../../skills/skrapi/README.md)**               | _Start_ (시작) — 감탄하는 프로젝트를 가리키면 해당 코드베이스가 어떻게 구축되어 있는지 집중된 Markdown(아키텍처, 종속성, 붙여넣기 준비가 된 프롬프트)의 고정된 `SKRAPI/` 폴더에 매핑하여 시작하기 전에 자신의 프로젝트에 맞는 패턴을 빌릴 수 있도록 합니다. 모든 스택(웹, 모바일, 확장 프로그램, 라이브러리, 모노레포)에서 작동하며 모든 설명은 실제 코드에 대해 검증되며 패키지 이름에서 추측하지 않습니다. 다국어 출력 (🇪🇸 ES · 🇺🇸 EN · 🇨🇳 ZH).<br><br>→ [전체 문서](../../skills/skrapi/README.md) |
| **[end](../../skills/end/README.md)**                     | _End_ (끝) — 프로젝트를 종단 간 이해합니다. 구체적인 참조와 함께 명확한 진단(확인된 버그, 위험, 기회, 기술 부채)을 제공하고 _이_ 코드베이스에 맞는 올바른 아키텍처 방향을 추천하며 정렬된 실행 계획을 구축합니다. 모든 변경은 격리되고 검토 가능한 단계에서 발생합니다 — `go`, `start` 또는 `proceed`라고 말할 때만 진행되며 분석 중에는 파일이 수정되지 않습니다.<br><br>→ [전체 문서 및 예시](../../skills/end/README.md) |

> **참고:** 각 스킬은 고유한 상세 README와 함께 제공됩니다. 루트 페이지는 높은 수준의 개요를 제공합니다. 깊이 있는 사용법, 보고서 예시 및 보증 사항에 대해서는 `./skills/<skill>/README.md`를 자세히 살펴보십시오.

## 설치

모든 스킬은 동일한 방식으로 설치됩니다 — 필요한 것을 선택하십시오:

```bash
npx skills add bastndev/skills --skill start-package   # Start (시작) — TS npm 패키지 스캐폴딩
npx skills add bastndev/skills --skill start-astro     # Start (시작) — Astro 프로젝트 구축
npx skills add bastndev/skills --skill skrapi          # Start (시작) — 모든 코드베이스 연구 및 문서화
npx skills add bastndev/skills --skill end             # End (끝) — 감사 및 안전하게 리팩토링
```

## "End" 스킬의 작동 방식

`end`는 제품군에서 가장 성숙한 스킬입니다. 종단 간 워크플로우는 다음과 같습니다.

1. **분석 먼저** — 진입점을 매핑하고 프로젝트를 이해합니다. **파일은 하나도 수정되지 않습니다.**
2. **구조화된 보고서** — 버그(심각도 포함), 부채/위험 및 제안으로 분류된 명확한 조사 결과와 점수가 매겨진 상태 개요, 아키텍처 권장 사항 및 정렬된 계획 — 이 모든 것은 구체적인 파일 + 줄 참조로 뒷받침됩니다.
3. **사용자가 각 단계를 승인합니다** — 한 번에 **정확히 하나의 단계** 만 실행합니다. 각 단계 후에는 변경 사항, 수행된 검증 및 남은 단계 목록에 대한 정확한 요약을 받게 됩니다.
4. **완전한 제어 및 안전성** — 프로젝트에 테스트가 없었다면 절대 테스트를 만들지 않습니다. 허가 없이 종속성을 추가하거나 패키지 관리자를 변경하지 않습니다. 커밋되지 않은 작업을 존중하고 정당한 버그를 수정하지 않는 한 항상 현재 동작을 유지합니다.

전체 워크플로우, 정확한 보고서 형식(필수 종료 블록 포함), 아키텍처 결정 규칙 및 모든 안전 보증에 대해서는 전용 스킬 문서를 읽어보십시오:

→ **[End – 프로젝트 리팩토링](../../skills/end/README.md)**

전체 내부 사양은 [skills/end/SKILL.md](../../skills/end/SKILL.md) 에 있습니다.

## 로드맵

- **Start** (시작) — `start-package` (스캐폴딩), `start-astro` (Astro 구축) 및 `skrapi` (기존 코드베이스 연구) 가 오늘 출시되었습니다. 더 많은 `start-*` 스캐폴더가 준비 중입니다.
- **Middle** (중간) — 집중적이고 온디맨드 방식의 개선 도구(성능, 보안, UX, 데드 코드 제거)가 계획되어 있습니다.
- **End** (끝) — `end`가 오늘 출시되었습니다. 더 많은 런타임, 추가 전문 리팩토링 모드 및 유틸리티가 계획되어 있습니다.

각 스킬은 고유한 전용 문서와 함께 제공됩니다 (현재의 [End – 프로젝트 리팩토링](../../skills/end/README.md) 참조).

---

<br>

<div align="center">
  <p align="center">
  <sub>AI 에이전트가 수석 엔지니어의 규율을 가지고 행동하기를 원하는 개발자를 위해 구축되었습니다.</sub>
</p>

_버그를 발견하거나 피드백이 있으시면 언제든지 [이슈를 열어주세요](https://github.com/bastndev/skills/issues/new)._

<sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a> 라이선스 적용</sub>

</div>
