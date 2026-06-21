# Handoff workflow

## 문서 우선순위

모델별 작업에서는 다음 순서를 사용합니다.

1. `AGENTS.md`
2. `requirements/model-XX.md` — 존재하는 경우 최우선 모델 정의
3. `rules/공통_편집규칙.md`
4. `handoff/README.md`
5. 단계별 프롬프트
6. `templates/handoff_template.md`
7. 기존 handoff 원고

기존 handoff가 requirements와 충돌하거나 필수 사례를 빠뜨렸다면 기존 handoff를 유효본으로 보지 않습니다.

## 작업 순서

`requirements → business → research → draft → review → final`

## 요구사항 변경과 재생성

`requirements/model-XX.md`가 새로 생기거나 내용이 변경되면 해당 모델의 기존 분석·조사·초안·검증·최종 완료 표시는 무효입니다.

재생성 절차:

1. `status/model-status.csv`의 상태를 `재생성대기`로 바꿉니다.
2. 분석완료·조사완료·초안완료·검증완료·최종완료 표시를 비웁니다.
3. requirements를 기준으로 business를 같은 경로에서 다시 작성합니다.
4. requirements 검사를 통과한 뒤에만 분석완료로 바꿉니다.
5. requirements와 새 business를 기준으로 research를 다시 작성합니다.
6. requirements 검사를 통과한 뒤에만 조사완료로 바꿉니다.
7. draft·review·final도 requirements를 필수 입력으로 읽습니다.

기존 business·research 파일은 재생성 전 참고자료일 뿐이며, 상태가 `재생성대기`인 동안 다음 단계의 근거 원고로 사용하지 않습니다.

## Business

`handoff/business/model-XX.md`

필수 입력:

- `requirements/model-XX.md` — 존재하는 경우
- `rules/공통_편집규칙.md`
- `prompts/01_사업성_분석.md`
- `templates/handoff_template.md`

실제 구매자, 유입 경로, 판매 방식, 결제, 정산, 비용, 확정 입금, 반복 가능성, 중단 기준을 분석합니다. requirements의 필수 사례마다 역할 분담·수익 흐름·숨은 변수·실패 신호·공식 검증 과제를 연결합니다.

저장 뒤 다음 검사를 실행합니다.

`python scripts/check_business_handoff.py handoff/business/model-XX.md`

`python scripts/check_model_requirements.py business XX`

두 검사 중 하나라도 실패하면 분석완료로 처리하지 않습니다.

## Research

`handoff/research/model-XX.md`

필수 입력:

- `requirements/model-XX.md` — 존재하는 경우
- 새로 생성된 `handoff/business/model-XX.md`
- `prompts/02_공식자료_조사.md`
- `templates/handoff_template.md`

공식 문서가 확인한 사실과 계약·계정 화면·사업자 인터뷰로 확인할 사항을 분리합니다. 사용자 제공 운영 관찰이 공식 문서에서 바로 확인되지 않아도 삭제하지 않고 확인 상태를 표시합니다.

저장 뒤 다음 검사를 실행합니다.

`python scripts/check_model_requirements.py research XX`

검사 실패 시 조사완료로 처리하지 않습니다.

`handoff/research/model-XX.md`는 draft·review·final 단계의 근거 문서입니다. 내용이 낡았으면 삭제하지 말고 같은 경로에서 갱신합니다.

## Draft

`handoff/draft/model-XX.md`

requirements, business, research를 모두 읽습니다. 조사 문구를 그대로 복사하지 않고 독자가 실행할 수 있는 원고로 재구성합니다. requirements의 핵심 사례와 역할 분담은 삭제하지 않습니다.

저장 뒤 다음 검사를 실행합니다.

`python scripts/check_model_requirements.py draft XX`

## Review

`handoff/review/model-XX.md`

requirements, business, research, draft를 함께 검토합니다. requirements의 필수 사례가 누락되거나 일반적인 플랫폼 설명으로 대체됐으면 치명적 오류로 분류합니다.

`python scripts/check_model_requirements.py review XX`

## Final

`final/model-XX.md`

requirements와 네 단계 handoff를 모두 읽고 통합합니다.

`python scripts/check_model_requirements.py final XX`

모든 단계는 최신 GitHub `main`을 다시 확인하고 작업 완료 후 `status/model-status.csv`를 갱신합니다.
