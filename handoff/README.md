# Handoff workflow

## 문서 우선순위

다음 문서만 공식 운영 기준으로 사용합니다.

1. `AGENTS.md`
2. `rules/공통_편집규칙.md`
3. `handoff/README.md`
4. `templates/handoff_template.md`

`handoff/business/README.md`, `handoff/research/README.md`, `handoff/draft/README.md`, `handoff/review/README.md`는 폐기된 안내문입니다. 에이전트는 이 파일들을 읽거나 인용하지 않습니다.

작업 순서:

`business → research → draft → review → final`

## Business

`handoff/business/model-XX.md`

실제 구매자, 유입 경로, 판매 방식, 결제, 정산, 비용, 확정 입금, 반복 가능성, 중단 기준을 분석합니다. 마지막에는 다음 단계가 공식자료로 검증할 조사 체크리스트를 둡니다.

## Research

`handoff/research/model-XX.md`

먼저 business 파일을 읽습니다. 현장 자료로 시장동향과 운영 감각을 파악하고, 가격·자격·수수료·지급 조건·상업 이용은 공식 문서로 최종 검증합니다. 미국식 모델은 실제 환경에서 대응되는 경로가 확인될 때만 실행안으로 인정합니다.

`handoff/research/model-XX.md` 파일은 draft, review, final 단계의 근거 문서입니다. 임시 산출물, probe 파일, cleanup 파일을 정리할 때 함께 삭제하지 않습니다. 내용이 낡았으면 삭제하지 말고 같은 경로에서 갱신합니다.

## Draft

`handoff/draft/model-XX.md`

business와 research 파일을 모두 읽습니다. 긴 자료를 평탄화하지 않고 `관찰 → 숨은 변수 → 작동 메커니즘 → 실행 판단 → 실패·전환 신호`로 재구성합니다.

## Review

`handoff/review/model-XX.md`

business, research, draft를 함께 검토합니다. 실제 구매자와 수익 경로가 불명확하거나, 미국식 단가·전환율·구독 구조를 그대로 옮겼거나, 긴 자료를 일반론으로 줄였으면 치명적 오류로 분류합니다.

모든 단계는 `rules/공통_편집규칙.md`와 `templates/handoff_template.md`를 따릅니다. 작업 완료 후 `status/model-status.csv`를 갱신합니다.
