"""Generate API reference documentation pages for mkdocs-gen-files.

This script runs during `mkdocs build` (via the gen-files plugin) and
produces one Markdown page per API endpoint group, plus a set of model
pages grouped by resource, so the generated docs stay in sync with the
code automatically.
"""

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

# ── Endpoint pages (one per API sub-package) ──────────────────────────
NICE_NAMES = {
    "app": "App",
    "banner": "Banner",
    "category": "Category",
    "changelog": "Changelog",
    "collection": "Collection",
    "comment": "Comment",
    "deprecated": "Deprecated",
    "email": "Email",
    "event": "Event",
    "file": "File",
    "group": "Group",
    "group_topic": "Group Topic",
    "home_banner": "Home Banner",
    "make": "Make",
    "message": "Message",
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

groups = sorted(d.name for d in API_DIR.iterdir() if d.is_dir() and d.name != "__pycache__")

for group in groups:
    nice = NICE_NAMES.get(group, group.replace("_", " ").title())
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

model_files = sorted(p.stem for p in MODELS_DIR.glob("*.py") if p.stem != "__init__")


def _classify(name: str) -> str:
    for prefix in sorted(RESOURCE_PREFIXES, key=len, reverse=True):
        if name.startswith(prefix):
            return prefix
    return "other"


groups_map: dict[str, list[str]] = {}
for m in model_files:
    bucket = _classify(m)
    groups_map.setdefault(bucket, []).append(m)

MODEL_NICE = {
    "thing": "Thing",
    "user": "User",
    "tag": "Tag",
    "copy": "Copy",
    "collection": "Collection",
    "comment": "Comment",
    "group": "Group",
    "category": "Category",
    "file": "File",
    "make": "Make",
    "search": "Search",
    "subscription": "Subscription",
    "banner": "Banner",
    "app": "App",
    "changelog": "Changelog",
    "email": "Email",
    "event": "Event",
    "home_banner": "Home Banner",
    "message": "Message",
    "printer": "Printer",
    "program": "Program",
    "sitewidenotification": "Sitewide Notification",
    "verified": "Verified",
    "other": "Other",
}

for bucket in sorted(groups_map):
    nice = MODEL_NICE.get(bucket, bucket.replace("_", " ").title())
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
