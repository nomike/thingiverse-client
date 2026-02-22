"""Unit tests for the verified API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.verified import get_verified


def test_get_verified_kwargs() -> None:
    kwargs = get_verified._get_kwargs()
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/verified"


def test_get_verified_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(204, content=b""))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = get_verified.sync_detailed(client=client)
    assert response.status_code == 204
    assert response.content is not None
