#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
terms = (
    ''.join(chr(n) for n in (54620, 44397)),
    ''.join(chr(n) for n in (44397, 45236)),
)

if len(sys.argv) > 1:
    files = [root / sys.argv[1]]
else:
    files = sorted(root.glob('handoff/business/model-*.md'))

errors = []
for path in files:
    if not path.is_file():
        print(f'missing file: {path.relative_to(root)}')
        sys.exit(2)
    for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if any(term in line for term in terms):
            errors.append((path.relative_to(root), number))

if errors:
    print('business handoff wording check failed')
    for path, number in errors:
        print(f'{path}:{number}')
    sys.exit(1)

print('business handoff wording check passed')
