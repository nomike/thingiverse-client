#!/usr/bin/env python3
"""
Apply all upstream-spec fixes to the bundled OpenAPI file so the generator succeeds.
Run after Redocly bundle; used when (re)creating openapi/bundled.patch.

Fixes applied:
1. Add missing response description for any 200 with content.
2. Add items: {} to any schema with type: array and no items/prefixItems.
3. Set required: true for all parameters with in: path.
4. Path/param fixes: /comments/ POST has no path params; /copies/.../images/... only copy_id/image_id;
   /events/0/read-all -> /events/{id}/read-all.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Need pyyaml: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


def _ensure_response_descriptions(spec: dict) -> int:
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
                    response["description"] = "Success"
                    count += 1
    return count


def _add_array_items(obj: object) -> int:
    """Recursively add items: {} to any type: array without items/prefixItems. Returns count."""
    count = 0
    if isinstance(obj, dict):
        if obj.get("type") == "array" and "items" not in obj and "prefixItems" not in obj:
            obj["items"] = {"type": "object"}
            count += 1
        for v in obj.values():
            count += _add_array_items(v)
    elif isinstance(obj, list):
        for i in obj:
            count += _add_array_items(i)
    return count


def _require_path_params(spec: dict) -> int:
    count = 0
    paths = spec.get("paths") or {}
    for _path_key, path_item in paths.items():
        if not isinstance(path_item, dict):
            continue
        for _method, op in path_item.items():
            if _method not in (
                "get",
                "post",
                "put",
                "patch",
                "delete",
                "head",
                "options",
                "parameters",
                "servers",
                "summary",
                "description",
                "tags",
                "security",
                "requestBody",
                "responses",
                "callbacks",
                "deprecated",
                "externalDocs",
            ):
                continue
            if not isinstance(op, dict):
                continue
            params = op.get("parameters")
            if not isinstance(params, list):
                continue
            for p in params:
                if isinstance(p, dict) and p.get("in") == "path" and not p.get("required"):
                    p["required"] = True
                    count += 1
        # Top-level path parameters
        params = path_item.get("parameters")
        if isinstance(params, list):
            for p in params:
                if isinstance(p, dict) and p.get("in") == "path" and not p.get("required"):
                    p["required"] = True
                    count += 1
    return count


def _path_param_names(path_str: str) -> set[str]:
    """Extract {name} placeholders from path string."""
    return set(re.findall(r"\{([^}]+)\}", path_str))


def _fix_path_templating(spec: dict) -> int:
    paths = spec.get("paths")
    if not isinstance(paths, dict):
        return 0
    changes = 0

    # /events/0/read-all -> /events/{id}/read-all so param "id" matches
    if "/events/0/read-all" in paths:
        paths["/events/{id}/read-all"] = paths.pop("/events/0/read-all")
        changes += 1

    # POST /comments/ must not have path parameters (path has no {comment_id})
    comments = paths.get("/comments/")
    if isinstance(comments, dict):
        post_op = comments.get("post")
        if isinstance(post_op, dict):
            params = post_op.get("parameters")
            if isinstance(params, list):

                def is_path_param(param):
                    if not isinstance(param, dict):
                        return False
                    if param.get("in") == "path":
                        return True
                    ref = param.get("$ref", "")
                    return "commentIdPathParam" in ref

                new_params = [p for p in params if not is_path_param(p)]
                if len(new_params) != len(params):
                    post_op["parameters"] = new_params
                    changes += 1

    # PATCH /copies/{copy_id}/images/{image_id}: only path params copy_id and image_id
    copy_images_path = "/copies/{copy_id}/images/{image_id}"
    if copy_images_path in paths:
        patch_op = paths[copy_images_path].get("patch")
        if isinstance(patch_op, dict):
            params = patch_op.get("parameters")
            if isinstance(params, list):
                path_param_names = {"copy_id", "image_id"}
                new_params = [
                    p
                    for p in params
                    if isinstance(p, dict)
                    and p.get("in") == "path"
                    and p.get("name") in path_param_names
                ]
                new_params += [
                    p for p in params if not (isinstance(p, dict) and p.get("in") == "path")
                ]
                if len(new_params) != len(params):
                    patch_op["parameters"] = new_params
                    changes += 1

    # Any param with in: path whose name is not in the path template -> move to query
    for path_str, path_item in list(paths.items()):
        if not isinstance(path_item, dict):
            continue
        valid_path_params = _path_param_names(path_str)
        for _method, op in path_item.items():
            if _method not in ("get", "post", "put", "patch", "delete", "head", "options"):
                continue
            if not isinstance(op, dict):
                continue
            params = op.get("parameters")
            if not isinstance(params, list):
                continue
            for p in params:
                if (
                    isinstance(p, dict)
                    and p.get("in") == "path"
                    and p.get("name") not in valid_path_params
                ):
                    p["in"] = "query"
                    changes += 1

    return changes


def _fix_duplicate_image_summary_sizes(spec: dict) -> int:
    """Extract the image_summary 'sizes' item schema into a named component and $ref it so the generator sees one schema instead of two duplicates."""
    components = spec.get("components") or {}
    schemas = components.get("schemas") or {}
    if not isinstance(schemas, dict):
        return 0
    changes = 0
    image_summary = schemas.get("image_summary_schema")
    if not isinstance(image_summary, dict):
        return 0
    props = image_summary.get("properties") or {}
    sizes = props.get("sizes") if isinstance(props, dict) else None
    if not isinstance(sizes, dict):
        return 0
    items = sizes.get("items")
    if (
        not isinstance(items, dict)
        or items.get("type") != "object"
        or "ImageSummarySizesItem" in schemas
    ):
        return 0
    # Extract to a named schema so both ImageSummary and image_summary_schema use the same ref
    schemas["ImageSummarySizesItem"] = dict(items)
    sizes["items"] = {"$ref": "#/components/schemas/ImageSummarySizesItem"}
    changes += 1
    return changes


def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "openapi/bundled.yaml")
    if not path.exists():
        print(f"Error: {path} not found", file=sys.stderr)
        return 1
    text = path.read_text(encoding="utf-8")
    spec = yaml.safe_load(text)
    if not isinstance(spec, dict):
        print("Error: bundled spec is not a dict", file=sys.stderr)
        return 1

    n_desc = _ensure_response_descriptions(spec)
    n_array = _add_array_items(spec)
    n_req = _require_path_params(spec)
    n_path = _fix_path_templating(spec)
    n_sizes = _fix_duplicate_image_summary_sizes(spec)

    path.write_text(
        yaml.dump(spec, default_flow_style=False, allow_unicode=True),
        encoding="utf-8",
    )
    print(
        f"Patched {path}: {n_desc} description(s), {n_array} array items, {n_req} path required, {n_path} path fix(es), {n_sizes} image-summary title(s)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
