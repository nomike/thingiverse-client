#!/usr/bin/env python3
"""
Download the full Thingiverse OpenAPI spec (root + all $ref'd files) into openapi/.

Usage:
    python scripts/fetch_openapi_spec.py [--output-dir openapi]

The Thingiverse docs URL may be behind Cloudflare. If fetch fails, try running from
a browser-authenticated environment or with a realistic User-Agent. See README.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from urllib.parse import urljoin

try:
    import httpx
    import yaml
except ImportError:
    print("Need httpx and pyyaml: pip install httpx pyyaml", file=sys.stderr)
    sys.exit(1)

BASE_URL = "https://www.thingiverse.com/swagger/docs/"
ROOT_SPEC = "openapi.yaml"

# User-Agent that may help with some CDNs
USER_AGENT = "Mozilla/5.0 (compatible; Thingiverse-SDK-Fetcher/1.0; +https://github.com/placeholder/thingiverse-api)"


def normalize_ref(current_dir: str, ref: str) -> str:
    """Resolve ref relative to current_dir; return path relative to spec root (no leading /)."""
    parts = (Path(current_dir) / ref).parts
    resolved = []
    for p in parts:
        if p == "..":
            if resolved:
                resolved.pop()
        elif p != "." and p:
            resolved.append(p)
    return "/".join(resolved)


def find_refs(obj: object, current_dir: str) -> set[str]:
    """Recursively find all $ref paths that look like local files. Returns paths relative to spec root."""
    refs: set[str] = set()
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "$ref" and isinstance(v, str):
                ref = v.split("#")[0].strip()
                if ref and not ref.startswith("http"):
                    rel = normalize_ref(current_dir, ref)
                    if rel:
                        refs.add(rel)
            else:
                refs |= find_refs(v, current_dir)
    elif isinstance(obj, list):
        for item in obj:
            refs |= find_refs(item, current_dir)
    return refs


def fetch_text(client: httpx.Client, url: str) -> str:
    r = client.get(url, follow_redirects=True)
    r.raise_for_status()
    return r.text


def fetch_and_save(
    client: httpx.Client,
    base_url: str,
    relative_path: str,
    out_dir: Path,
) -> set[str]:
    """Fetch one file, save it, parse for refs, return new refs found (relative to spec root)."""
    url = urljoin(base_url, relative_path)
    text = fetch_text(client, url)
    out_path = out_dir / relative_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    print(f"  {relative_path}", flush=True)
    try:
        data = yaml.safe_load(text)
    except Exception:
        return set()
    current_dir = str(Path(relative_path).parent) if "/" in relative_path else "."
    return find_refs(data, current_dir)


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch Thingiverse OpenAPI spec into openapi/")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("openapi"),
        help="Output directory (default: openapi)",
    )
    parser.add_argument(
        "--base-url",
        default=BASE_URL,
        help=f"Base URL for spec (default: {BASE_URL})",
    )
    args = parser.parse_args()
    out_dir = args.output_dir.resolve()
    base_url = args.base_url.rstrip("/") + "/"
    out_dir.mkdir(parents=True, exist_ok=True)

    headers = {"User-Agent": USER_AGENT}
    to_fetch = {ROOT_SPEC}
    fetched: set[str] = set()

    with httpx.Client(headers=headers, timeout=30.0) as client:
        while to_fetch:
            next_batch = set()
            for rel in to_fetch:
                if rel in fetched:
                    continue
                fetched.add(rel)
                try:
                    new_refs = fetch_and_save(client, base_url, rel, out_dir)
                    for ref in new_refs:
                        if ref not in fetched:
                            next_batch.add(ref)
                except httpx.HTTPStatusError as e:
                    print(f"  ERROR {rel}: {e.response.status_code}", file=sys.stderr)
                except Exception as e:
                    print(f"  ERROR {rel}: {e}", file=sys.stderr)
            to_fetch = next_batch

    print(f"Fetched {len(fetched)} file(s) into {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
