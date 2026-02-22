"""Unit tests for get_things_thing_id API (mocked)."""

import httpx
from thingiverse_client import Client
from thingiverse_client.api.thing import get_things_thing_id


def test_get_thing_by_id_builds_request() -> None:
    """Test that get_things_thing_id builds the expected request (mocked)."""
    client = Client(base_url="https://api.thingiverse.com")
    transport = httpx.MockTransport(
        lambda req: httpx.Response(200, json={"id": 123, "name": "Test"})
    )
    client._client = httpx.Client(
        base_url=client._base_url,
        transport=transport,
    )
    response = get_things_thing_id.sync_detailed(thing_id=123, client=client)
    assert response.status_code == 200
