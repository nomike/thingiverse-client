"""Unit tests for the thing_ops API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.thing_ops import (
    post_thingops_ids_copy,
    post_thingops_ids_move,
    post_thingops_ids_remove,
)


def test_post_thingops_ids_copy_kwargs() -> None:
    kwargs = post_thingops_ids_copy._get_kwargs(ids="test-value")
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/thingops/test-value/copy"


def test_post_thingops_ids_move_kwargs() -> None:
    kwargs = post_thingops_ids_move._get_kwargs(ids="test-value")
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/thingops/test-value/move"


def test_post_thingops_ids_remove_kwargs() -> None:
    kwargs = post_thingops_ids_remove._get_kwargs(ids="test-value")
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/thingops/test-value/remove"


def test_post_thingops_ids_copy_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(200, json={}))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = post_thingops_ids_copy.sync_detailed(ids="test", client=client)
    assert response.status_code == 200
    assert response.content is not None
