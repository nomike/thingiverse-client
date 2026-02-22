"""Integration tests: read-only API calls. Require THINGIVERSE_TOKEN."""

import pytest
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.thing import get_things_thing_id

from tests.conftest import _get_token


@pytest.mark.integration
def test_get_thing_by_id_read_only(skip_without_token, base_url) -> None:
    """Call GET /things/{thing_id} (read-only). Uses THINGIVERSE_BASE_URL or staging if set."""
    client = AuthenticatedClient(base_url=base_url, token=_get_token())
    response = get_things_thing_id.sync_detailed(thing_id=763622, client=client)
    assert response.status_code in (200, 401, 403)
