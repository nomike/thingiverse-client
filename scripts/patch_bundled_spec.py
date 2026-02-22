#!/usr/bin/env python3
"""
Legacy: patch the bundled OpenAPI spec by adding missing response descriptions.
Superseded by applying openapi/bundled.patch in generate_client.sh.
Kept for reference; use add_response_descriptions_in_place.py when (re)creating
the patch to avoid reordering the YAML.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Need pyyaml: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

DEFAULT_BUNDLED = "openapi/bundled.yaml"
DEFAULT_DESCRIPTION = "Success"


def patch_response_descriptions(spec: dict) -> int:
    """
    Add a default description to any response object that has content but no
    description (required by OpenAPI 3.0). Modifies spec in place.
    Returns the number of response objects patched.
    """
    count = 0
    paths = spec.get("paths") or {}
    for _path_key, path_item in paths.items():
        if not isinstance(path_item, dict):
            continue
        for method in ("get", "post", "put", "patch", "delete", "head", "options"):
            op = path_item.get(method)
            if not isinstance(op, dict):
                continue
            responses = op.get("responses")
            if not isinstance(responses, dict):
                continue
            for _code, response in responses.items():
                if not isinstance(response, dict):
                    continue
                if "content" in response and not response.get("description"):
                    response["description"] = DEFAULT_DESCRIPTION
                    count += 1
    return count


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Patch bundled OpenAPI spec for generator compatibility"
    )
    parser.add_argument(
        "bundled",
        type=Path,
        nargs="?",
        default=Path(DEFAULT_BUNDLED),
        help=f"Path to bundled spec (default: {DEFAULT_BUNDLED})",
    )
    args = parser.parse_args()
    path = args.bundled.resolve()
    if not path.exists():
        print(f"Error: {path} not found", file=sys.stderr)
        return 1
    text = path.read_text(encoding="utf-8")
    try:
        spec = yaml.safe_load(text)
    except Exception as e:
        print(f"Error: failed to parse YAML: {e}", file=sys.stderr)
        return 1
    if not isinstance(spec, dict):
        print("Error: bundled spec is not a dict", file=sys.stderr)
        return 1
    n = patch_response_descriptions(spec)
    if n:
        path.write_text(
            yaml.dump(spec, default_flow_style=False, allow_unicode=True), encoding="utf-8"
        )
        print(f"Patched {n} response(s) with missing description in {path}")
    else:
        print("No response descriptions to patch.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
