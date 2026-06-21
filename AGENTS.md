# AGENTS.md

모든 단계는 `rules/공통_편집규칙.md`와 `handoff/README.md`를 따른다.

## GitHub 최신 상태 우선 원칙

이 프로젝트는 사용자, Codex, 다른 에이전트가 동시에 수정할 수 있다. 에이전트는 이전 대화, 과거 커밋, 기억, 방금 전 읽은 내용만으로 현재 저장소 상태를 추정하지 않는다.

- 모든 작업을 시작하기 전에 GitHub `main`의 최신 파일을 먼저 읽는다.
- 파일·폴더의 존재 여부는 대화 맥락이 아니라 GitHub에서 직접 확인한다.
- 수정 직전에 대상 파일을 다시 읽고 최신 blob SHA를 확인한다.
- 이전에 읽어 둔 SHA와 내용을 재사용하지 않는다.
- 여러 파일을 순차 수정할 때도 각 파일마다 쓰기 직전에 최신 상태를 다시 확인한다.
- 커밋 뒤에는 같은 경로를 다시 열어 실제 반영 여부와 최종 내용을 검증한다.
- 상태표의 완료 여부와 handoff 파일 존재 여부가 다르면 둘 다 다시 확인하고, 어느 한쪽만 보고 판단하지 않는다.
- GitHub 확인 없이 “파일이 없다”, “작업이 완료됐다”, “현재 구조는 이렇다”고 단정하지 않는다.

## 사용자 지시 우선 및 덮어쓰기 판단

- 동시 변경 가능성이나 덮어쓰기 가능성은 작업을 축소·보류·회피할 사유가 아니다.
- 사용자가 수정하라고 지시한 파일과 범위는 최신 GitHub 상태를 확인한 뒤 그대로 반영한다.
- 어떤 변경을 덮어쓸지, 보존할지, 다시 적용할지는 사용자가 판단한다.
- 에이전트는 덮어쓰기 우려를 이유로 일부 파일만 수정하거나 임시 파일로 우회하거나 작업을 중단하지 않는다.
- SHA 충돌이 발생하면 최신 파일을 다시 읽고 사용자의 최근 지시를 기준으로 수정 내용을 다시 적용한다.
- 기술적으로 실행할 수 없는 경우가 아니면 사용자에게 판단을 되돌리지 않는다.

## 모델별 요구사항 우선 원칙

- 작업 대상에 `requirements/model-XX.md`가 있으면 모든 단계가 반드시 먼저 읽는다.
- `requirements/model-XX.md`는 기존 business·research·draft·review·final보다 우선하는 모델 정의다.
- 기존 handoff가 요구사항과 충돌하거나 필수 사례를 빠뜨렸으면 기존 완료 상태를 신뢰하지 않고 같은 경로에서 다시 생성한다.
- 공식 문서에서 바로 확인되지 않는 사용자 제공 운영 관찰은 삭제하지 않는다. `계약 확인 필요`, `사업자 인터뷰 필요`, `사용자 제공 운영 관찰`, `편집 판단` 중 하나로 분류한다.
- requirements가 변경되면 해당 모델의 기존 분석·조사·초안·검증·최종 완료 표시는 무효다.
- business와 research는 `python scripts/check_model_requirements.py <단계> <모델번호>` 검사를 통과해야 완료 처리할 수 있다.

에이전트는 사용자의 명시 지시 없이 자동 동기화, 자동 pull, 자동 push, 자동 삭제 정리를 실행하지 않는다. GitHub와 로컬 작업물의 동기화는 사용자가 요청한 범위에서만 수행한다.

`handoff/research/model-XX.md` 파일은 중간 원본이다. 임시 파일 정리, cleanup, probe 제거 작업에서 삭제하지 않는다.

business 단계는 반드시 `prompts/01_사업성_분석.md`를 먼저 읽는다.

`handoff/business/model-XX.md` 작성 후 다음 검사를 모두 통과해야 한다.

`python scripts/check_business_handoff.py handoff/business/model-XX.md`

`python scripts/check_model_requirements.py business XX`

research 단계는 반드시 `prompts/02_공식자료_조사.md`, `requirements/model-XX.md`, `handoff/business/model-XX.md`를 읽고 다음 검사를 통과해야 한다.

`python scripts/check_model_requirements.py research XX`

검사 실패 시 결과 저장, 상태 갱신, 다음 단계 전달을 하지 않는다.
