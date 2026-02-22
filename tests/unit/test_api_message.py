"""Unit tests for the message API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.message import post_messages


def test_post_messages_kwargs() -> None:
    kwargs = post_messages._get_kwargs()
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/messages"


def test_post_messages_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(200, json={}))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = post_messages.sync_detailed(client=client)
    assert response.status_code == 200
    assert response.content is not None
