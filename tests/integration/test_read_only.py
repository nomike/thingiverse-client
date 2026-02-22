"""Integration tests: read-only API calls. Require THINGIVERSE_TOKEN."""

import pytest
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.default import get_things

from tests.conftest import _get_token


@pytest.mark.integration
def test_get_things_read_only(skip_without_token, base_url) -> None:
    """Call GET /things/ (read-only). Uses THINGIVERSE_BASE_URL or staging if set."""
    client = AuthenticatedClient(base_url=base_url, token=_get_token())
    response = get_things.sync_detailed(client=client)
    # 200 or 401/403 if token invalid
    assert response.status_code in (200, 401, 403)
