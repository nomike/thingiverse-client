"""Generate API reference documentation pages for mkdocs-gen-files.

This script runs during `mkdocs build` (via the gen-files plugin) and
produces one Markdown page per API endpoint group, plus a set of model
pages grouped by resource, so the generated docs stay in sync with the
code automatically.
"""

import re
from pathlib import Path

import mkdocs_gen_files

PACKAGE = Path("thingiverse_client")
API_DIR = PACKAGE / "api"
MODELS_DIR = PACKAGE / "models"

# All generated files live under api/ in the virtual docs tree.
# The SUMMARY.md for literate-nav also lives at api/SUMMARY.md,
# so nav paths must be relative to api/.
nav = mkdocs_gen_files.Nav()

# ── Client page ───────────────────────────────────────────────────────
nav["Client"] = "client.md"

with mkdocs_gen_files.open("api/client.md", "w") as f:
    f.write(
        "# Client\n\n"
        "::: thingiverse_client\n"
        "    options:\n"
        "      show_root_heading: true\n"
        "      members:\n"
        "        - Client\n"
        "        - AuthenticatedClient\n"
        "        - BASE_URL_PRODUCTION\n"
        "        - BASE_URL_STAGING\n"
    )

# ── Display names shared by endpoints and models ─────────────────────
_DISPLAY_NAMES = {
    "app": "App",
    "banner": "Banner",
    "category": "Category",
    "changelog": "Changelog",
    "collection": "Collection",
    "comment": "Comment",
    "copy": "Copy",
    "deprecated": "Deprecated",
    "email": "Email",
    "event": "Event",
    "file": "File",
    "group": "Group",
    "group_topic": "Group Topic",
    "home_banner": "Home Banner",
    "make": "Make",
    "message": "Message",
    "other": "Other",
    "printer": "Printer",
    "program": "Program",
    "search": "Search",
    "sitewidenotification": "Sitewide Notification",
    "subscription": "Subscription",
    "tag": "Tag",
    "thing": "Thing",
    "thing_ops": "Thing Ops",
    "user": "User",
    "verified": "Verified",
}


def _nice(key: str) -> str:
    return _DISPLAY_NAMES.get(key, key.replace("_", " ").title())


# ── Endpoint pages (one per API sub-package) ──────────────────────────
groups = sorted(d.name for d in API_DIR.iterdir() if d.is_dir() and d.name != "__pycache__")

for group in groups:
    nice = _nice(group)
    nav["Endpoints", nice] = f"endpoints/{group}.md"

    with mkdocs_gen_files.open(f"api/endpoints/{group}.md", "w") as f:
        f.write(
            f"# {nice}\n\n"
            f"::: thingiverse_client.api.{group}\n"
            "    options:\n"
            "      show_root_heading: true\n"
            "      show_submodules: true\n"
        )

# ── Model pages (grouped by resource to keep page sizes reasonable) ───
RESOURCE_PREFIXES = [
    "thing",
    "user",
    "tag",
    "copy",
    "collection",
    "comment",
    "group",
    "category",
    "file",
    "make",
    "search",
    "subscription",
    "banner",
    "app",
    "changelog",
    "email",
    "event",
    "home_banner",
    "message",
    "printer",
    "program",
    "sitewidenotification",
    "verified",
]

_HTTP_VERB_RE = re.compile(r"^(get|post|put|patch|delete|head|options)_")

_PLURAL_SEGMENT_TO_RESOURCE = {
    "apps": "app",
    "banner": "banner",
    "categories": "category",
    "categoriesreturncomplete": "category",
    "collections": "collection",
    "comments": "comment",
    "copies": "copy",
    "copiesreturncomplete": "copy",
    "email": "email",
    "events": "event",
    "featured": "thing",
    "files": "file",
    "groups": "group",
    "grouptopics": "group_topic",
    "homebanner": "home_banner",
    "messages": "message",
    "newest": "thing",
    "popular": "thing",
    "printers": "printer",
    "programs": "program",
    "search": "search",
    "sitewidenotification": "sitewidenotification",
    "subscriptions": "subscription",
    "tags": "tag",
    "thingops": "thing_ops",
    "things": "thing",
    "users": "user",
    "verified": "verified",
}

model_files = sorted(p.stem for p in MODELS_DIR.glob("*.py") if p.stem != "__init__")


def _classify(name: str) -> str:
    stripped = _HTTP_VERB_RE.sub("", name)
    if stripped != name:
        first_seg = stripped.split("_")[0]
        resource = _PLURAL_SEGMENT_TO_RESOURCE.get(first_seg)
        if resource:
            return resource
    for prefix in sorted(RESOURCE_PREFIXES, key=len, reverse=True):
        if name.startswith(prefix):
            return prefix
    return "other"


groups_map: dict[str, list[str]] = {}
for m in model_files:
    bucket = _classify(m)
    groups_map.setdefault(bucket, []).append(m)

for bucket in sorted(groups_map):
    nice = _nice(bucket)
    nav["Models", nice] = f"models/{bucket}.md"

    members = groups_map[bucket]
    with mkdocs_gen_files.open(f"api/models/{bucket}.md", "w") as f:
        f.write(f"# {nice} Models\n\n")
        for member in members:
            f.write(
                f"::: thingiverse_client.models.{member}\n"
                "    options:\n"
                "      show_root_heading: true\n"
                "      show_source: false\n\n"
            )

# ── Write the literate-nav SUMMARY ────────────────────────────────────
with mkdocs_gen_files.open("api/SUMMARY.md", "w") as f:
    f.writelines(nav.build_literate_nav())
