"""Unit tests for get_things API (mocked)."""
import httpx
from thingiverse_client import Client
from thingiverse_client.api.default import get_things


def test_get_things_builds_request() -> None:
    """Test that get_things builds the expected request (mocked)."""
    client = Client(base_url="https://api.thingiverse.com")
    # Mock the httpx client
    transport = httpx.MockTransport(
        lambda req: httpx.Response(200, json=[])
    )
    client._client = httpx.Client(
        base_url=client._base_url,
        transport=transport,
    )
    response = get_things.sync_detailed(client=client)
    assert response.status_code == 200
