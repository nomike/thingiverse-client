"""Unit tests for the app API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.app import get_apps_0_approvedandpublished, get_apps_id


def test_get_apps_0_approvedandpublished_kwargs() -> None:
    kwargs = get_apps_0_approvedandpublished._get_kwargs()
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/apps/0/approvedandpublished"


def test_get_apps_id_kwargs() -> None:
    kwargs = get_apps_id._get_kwargs(id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/apps/42"


def test_get_apps_id_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(200, json={"id": 42}))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = get_apps_id.sync_detailed(id=42, client=client)
    assert response.status_code == 200
    assert response.content is not None
