# AGENTS.md

모든 단계는 `rules/공통_편집규칙.md`와 `handoff/README.md`를 따른다.

`handoff/research/model-XX.md` 파일은 중간 원본이다. 임시 파일 정리, cleanup, probe 제거 작업에서 삭제하지 않는다.

business 단계는 반드시 `prompts/01_사업성_분석.md`를 먼저 읽는다.

`handoff/business/model-XX.md` 작성 후 다음 검사를 통과해야 한다.

`python scripts/check_business_handoff.py handoff/business/model-XX.md`

검사 실패 시 결과 저장, 상태 갱신, 커밋을 하지 않는다.
