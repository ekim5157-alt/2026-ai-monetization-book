# 2026 AI 수익화 전체 지도

『2026 AI 수익화 전체 지도』 집필·검증·Sanity 패키지 생성을 위한 단일 저장소입니다.

이 저장소는 공식자료 조사, 사업성 분석, 초보자 실행 원고, 품질 검증, 최종 승인 원고와 Sanity 단일 패키지 JSON을 관리합니다. 로컬에서 Codex로 작업하더라도 GitHub의 최신 커밋을 단일 기준으로 봅니다.

## 작업 원칙

- 한 번에 한 모델만 최종 편집합니다.
- 조사·분석·초안은 그대로 복사하지 않고 총괄 편집실에서 재구성합니다.
- 가격, 무료 한도, 상업 이용, 수익화 자격, 지급 조건은 공식 출처로 검증합니다.
- 조회수·클릭·예약·주문과 확정 수익·실제 입금을 구분합니다.
- 승인 전 원고는 `sanity/`에 반영하지 않습니다.
- 기존 파일을 수정할 때 같은 경로의 파일을 갱신하고, 불필요한 사본을 만들지 않습니다.

## 디렉터리

- `handoff/research/` — 공식자료 조사 결과
- `handoff/business/` — 사업성 및 숨은 병목 분석
- `handoff/draft/` — 초보자 실행 원고
- `review/` — 비판적 품질 검증 결과
- `final/` — 모델별 승인 완성 원고
- `sanity/` — 승인된 모델의 완성 Sanity 패키지 JSON
- `sources/` — 공식 출처와 확인 기록
- `glossary/` — 책 전체 약어·전문용어 최초 등장 관리
- `templates/` — 모델별 작업 템플릿

## 기본 작업 흐름

1. `handoff/research/`에 공식자료 조사 결과 저장
2. `handoff/business/`에 사업성 분석 저장
3. `handoff/draft/`에 초보자 실행 원고 저장
4. 총괄 편집실에서 세 문서를 통합
5. `review/`의 검증 결과 반영
6. 승인된 완성본을 `final/`에 저장
7. 승인된 완성본만 `sanity/`에 반영

## 파일명 규칙

모델 번호는 두 자리로 고정합니다.

```text
handoff/research/research_01_model-slug.md
handoff/business/business_01_model-slug.md
handoff/draft/draft_01_model-slug.md
review/review_01_model-slug.md
final/final_01_model-slug.md
sanity/sanity-content-model-01-model-slug-complete-v1.json
```

책의 고정 모델명 중 5번은 `구글 SEO 블로그·애드센스(워드프레스)`, 12번은 `각종 어필리에이트`로 사용합니다.
