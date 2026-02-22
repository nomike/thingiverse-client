"""Unit tests for the program API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.program import get_programs_0_all


def test_get_programs_0_all_kwargs() -> None:
    kwargs = get_programs_0_all._get_kwargs()
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/programs/0/all"


def test_get_programs_0_all_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(200, json={"id": 42}))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = get_programs_0_all.sync_detailed(client=client)
    assert response.status_code == 200
    assert response.content is not None
