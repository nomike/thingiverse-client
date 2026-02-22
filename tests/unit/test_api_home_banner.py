"""Unit tests for the home_banner API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.home_banner import get_homebanner


def test_get_homebanner_kwargs() -> None:
    kwargs = get_homebanner._get_kwargs()
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/homebanner"


def test_get_homebanner_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(200, json={"id": 42}))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = get_homebanner.sync_detailed(client=client)
    assert response.status_code == 200
    assert response.content is not None
