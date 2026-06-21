#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
VALID_STAGES = {"business", "research", "draft", "review", "final"}


def fail(message: str, code: int = 1) -> None:
    print(message)
    raise SystemExit(code)


def normalize_model(value: str) -> str:
    try:
        return f"{int(value):02d}"
    except ValueError:
        fail(f"invalid model number: {value}", 2)


def read_required_terms(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    in_section = False
    terms: list[str] = []

    for line in lines:
        stripped = line.strip()
        if stripped == "## 필수 포함 검사":
            in_section = True
            continue
        if in_section and stripped.startswith("## "):
            break
        if in_section and stripped.startswith("- "):
            term = stripped[2:].strip().strip("`")
            if term:
                terms.append(term)

    if not terms:
        fail(f"no required terms found in {path.relative_to(ROOT)}", 2)
    return terms


def main() -> None:
    if len(sys.argv) != 3:
        fail("usage: check_model_requirements.py <business|research|draft|review|final> <model-number>", 2)

    stage = sys.argv[1]
    if stage not in VALID_STAGES:
        fail(f"invalid stage: {stage}", 2)

    model = normalize_model(sys.argv[2])
    requirements = ROOT / "requirements" / f"model-{model}.md"

    if not requirements.is_file():
        print(f"no model requirements: model-{model}; skipped")
        return

    if stage == "final":
        target = ROOT / "final" / f"model-{model}.md"
    else:
        target = ROOT / "handoff" / stage / f"model-{model}.md"

    if not target.is_file():
        fail(f"missing target file: {target.relative_to(ROOT)}", 2)

    text = target.read_text(encoding="utf-8")
    terms = read_required_terms(requirements)
    missing = [term for term in terms if term not in text]

    if missing:
        print(f"model requirements check failed: {target.relative_to(ROOT)}")
        for term in missing:
            print(f"missing: {term}")
        raise SystemExit(1)

    print(f"model requirements check passed: {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
