# 2026 AI 수익화 전체 지도

『2026 AI 수익화 전체 지도』 집필·검증·Sanity 패키지 생성을 위한 단일 저장소입니다.

이 저장소는 사업성 분석, 공식자료 조사, 초보자 실행 원고, 품질 검증, 최종 승인 원고와 Sanity 패키지 JSON을 관리합니다. 로컬에서 Codex로 작업하더라도 GitHub의 최신 커밋을 단일 기준으로 봅니다.

## 작업 원칙

- 한 번에 한 모델만 최종 편집합니다.
- 작업 시작 순서는 `business → research → draft → review → final`입니다.
- 사업성 분석이 먼저 실제 병목과 검증 질문을 제시합니다.
- 공식자료 조사는 사업성 분석의 주장과 조사 체크리스트를 공식 문서로 검증합니다.
- 초보자 원고는 사업성 분석과 공식자료 조사 결과를 모두 읽고 작성합니다.
- 품질 검증은 세 문서와 초안을 함께 검토합니다.
- 최종 편집은 검증 결과까지 반영해 완성본을 만듭니다.
- 가격, 무료 한도, 상업 이용, 수익화 자격, 지급 조건은 공식 출처로 검증합니다.
- 조회수·클릭·예약·주문과 확정 수익·실제 입금을 구분합니다.
- 승인 전 원고는 `sanity-packages/`에 반영하지 않습니다.
- 기존 파일을 수정할 때 같은 경로의 파일을 갱신하고, 불필요한 사본을 만들지 않습니다.

## 디렉터리

- `prompts/` — 에이전트별 작업 프롬프트
- `rules/` — 공통 편집 규칙
- `handoff/business/` — 사업성 및 숨은 병목 분석
- `handoff/research/` — 사업성 분석을 기반으로 한 공식자료 검증
- `handoff/draft/` — 초보자 실행 원고
- `handoff/review/` — 비판적 품질 검증 결과
- `final/` — 모델별 승인 완성 원고
- `sanity-packages/` — 승인된 모델의 완성 Sanity 패키지 JSON
- `status/` — 모델별 진행 상태
- `templates/` — 공통 작업 템플릿

## 기본 작업 흐름

1. `handoff/business/model-XX.md`에 사업성 분석과 조사 체크리스트 저장
2. `handoff/research/model-XX.md`에 공식자료 검증 결과 저장
3. `handoff/draft/model-XX.md`에 초보자 실행 원고 저장
4. `handoff/review/model-XX.md`에 품질 검증 결과 저장
5. 검증 결과를 반영한 승인본을 `final/model-XX.md`에 저장
6. 최종 승인 후에만 `sanity-packages/sanity-content-model-XX.json` 생성

## 단계별 입력 관계

- `business` — 사전 handoff 없이 시장 구조와 실제 병목을 분석
- `research` — 해당 모델의 `business` 파일을 먼저 읽고 검증 과제를 공식자료로 확인
- `draft` — 해당 모델의 `business`와 `research` 파일을 모두 읽고 작성
- `review` — 해당 모델의 `business`, `research`, `draft` 파일을 함께 검토
- `final` — 네 개의 handoff 파일을 읽고 통합·수정해 승인본 작성

## 파일명 규칙

모델 번호는 두 자리로 고정합니다.

```text
handoff/business/model-01.md
handoff/research/model-01.md
handoff/draft/model-01.md
handoff/review/model-01.md
final/model-01.md
sanity-packages/sanity-content-model-01.json
status/model-status.csv
```

책의 고정 모델명 중 5번은 `구글 SEO 블로그·애드센스(워드프레스)`, 12번은 `각종 어필리에이트`로 사용합니다.
