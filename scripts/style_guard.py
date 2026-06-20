#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
terms = (
    ''.join(chr(n) for n in (54620, 44397)),
    ''.join(chr(n) for n in (44397, 45236)),
)
files = [
    path
    for path in root.rglob('*')
    if path.is_file() and path.suffix.lower() in {'.md', '.json', '.csv'}
]
errors = []
for path in sorted(files):
    for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        for term in terms:
            if term in line:
                errors.append((path.relative_to(root), number))
if errors:
    for path, number in errors:
        print(f'{path}:{number}')
    sys.exit(1)
print('style guard passed')
