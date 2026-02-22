#!/usr/bin/env python3
"""List all designs for Thingiverse user 'nomike' and fetch the first design.

Requires THINGIVERSE_TOKEN in the environment.
Usage: python scripts/list_user_designs.py
"""

import json
import os
import sys

from thingiverse_client import BASE_URL_PRODUCTION, AuthenticatedClient
from thingiverse_client.api.thing import get_things_thing_id
from thingiverse_client.api.user import get_users_username_things


def main() -> None:
    token = os.environ.get("THINGIVERSE_TOKEN")
    if not token:
        print("Error: THINGIVERSE_TOKEN must be set", file=sys.stderr)
        sys.exit(1)

    base_url = os.environ.get("THINGIVERSE_BASE_URL", "").strip() or BASE_URL_PRODUCTION
    username = "nomike"

    client = AuthenticatedClient(base_url=base_url, token=token)

    resp = get_users_username_things.sync_detailed(username=username, client=client, per_page=100)
    if resp.status_code != 200:
        print(f"Error listing designs: {resp.status_code} {resp.content}", file=sys.stderr)
        sys.exit(1)

    designs = json.loads(resp.content)
    print(f"User '{username}' has {len(designs)} design(s)\n")

    if not designs:
        print("No designs to show.")
        return

    for i, d in enumerate(designs, 1):
        print(f"  {i}. id={d.get('id')} name={d.get('name', '?')}")

    first_id = designs[0]["id"]
    print(f"\nFetching first design (id={first_id})...\n")

    detail_resp = get_things_thing_id.sync_detailed(thing_id=first_id, client=client)
    if detail_resp.status_code != 200:
        print(f"Error fetching thing: {detail_resp.status_code}", file=sys.stderr)
        sys.exit(1)

    first_design = json.loads(detail_resp.content)
    print("First design:")
    print(json.dumps(first_design, indent=2, default=str))


if __name__ == "__main__":
    main()
