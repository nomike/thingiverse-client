#!/usr/bin/env python3
"""
Insert "description: Success" after '200': when the next key is "content:"
(no description present). Preserves file structure and key order.
Used only when creating/updating openapi/bundled.patch.
"""

import re
import sys
from pathlib import Path


def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "openapi/bundled.yaml")
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    out: list[str] = []
    i = 0
    added = 0
    # Match line like "        '200':" or '        "200":' (response key)
    response_200 = re.compile(r"^(\s+)['\"]200['\"]\s*:\s*$")
    # Indentation for the next line (description/content)
    content_key = re.compile(r"^(\s+)content\s*:\s*$")
    description_key = re.compile(r"^(\s+)description\s*:")

    while i < len(lines):
        line = lines[i]
        out.append(line)
        m = response_200.match(line)
        if m:
            base_indent = m.group(1)
            # Look at next line(s) - if we see content: before description:, insert description
            j = i + 1
            seen_description = False
            content_indent = None
            while j < len(lines):
                next_line = lines[j]
                cm = content_key.match(next_line)
                if cm:
                    content_indent = cm.group(1)
                    break
                if description_key.match(next_line):
                    seen_description = True
                    break
                # Next key at same or less indent - stop
                if next_line.strip():
                    ni = len(next_line) - len(next_line.lstrip())
                    if ni <= len(base_indent):
                        break
                j += 1
            if content_indent is not None and not seen_description:
                out.append(content_indent + "description: Success\n")
                added += 1
        i += 1

    path.write_text("".join(out), encoding="utf-8")
    print(f"Added {added} response description(s) to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
