"""Unit tests for the collection API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.collection import (
    delete_collections_collection_id,
    delete_collections_collection_id_thing_thing_id,
    get_collections,
    get_collections_collection_id,
    get_collections_collection_id_things,
    get_collections_thing_id_by_thing_id,
    patch_collections_collection_id,
    post_collections,
    post_collections_collection_id_like,
    post_collections_collection_id_move_thing_id,
    post_collections_collection_id_thing_thing_id,
    post_collections_collection_id_watch,
)


def test_delete_collections_collection_id_kwargs() -> None:
    kwargs = delete_collections_collection_id._get_kwargs(collection_id=42)
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/collections/42/"


def test_delete_collections_collection_id_thing_thing_id_kwargs() -> None:
    kwargs = delete_collections_collection_id_thing_thing_id._get_kwargs(
        collection_id=42, thing_id=42
    )
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/collections/42/thing/42"


def test_get_collections_kwargs() -> None:
    kwargs = get_collections._get_kwargs()
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/collections/"


def test_get_collections_collection_id_kwargs() -> None:
    kwargs = get_collections_collection_id._get_kwargs(collection_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/collections/42/"


def test_get_collections_collection_id_things_kwargs() -> None:
    kwargs = get_collections_collection_id_things._get_kwargs(collection_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/collections/42/things"


def test_get_collections_thing_id_by_thing_id_kwargs() -> None:
    kwargs = get_collections_thing_id_by_thing_id._get_kwargs(thing_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/collections/42/by-thing-id"


def test_patch_collections_collection_id_kwargs() -> None:
    kwargs = patch_collections_collection_id._get_kwargs(collection_id=42)
    assert kwargs["method"] == "patch"
    assert kwargs["url"] == "/collections/42/"


def test_post_collections_kwargs() -> None:
    kwargs = post_collections._get_kwargs()
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/collections/"


def test_post_collections_collection_id_like_kwargs() -> None:
    kwargs = post_collections_collection_id_like._get_kwargs(collection_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/collections/42/like"


def test_post_collections_collection_id_move_thing_id_kwargs() -> None:
    kwargs = post_collections_collection_id_move_thing_id._get_kwargs(collection_id=42, thing_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/collections/42/move/42"


def test_post_collections_collection_id_thing_thing_id_kwargs() -> None:
    kwargs = post_collections_collection_id_thing_thing_id._get_kwargs(
        collection_id=42, thing_id=42
    )
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/collections/42/thing/42"


def test_post_collections_collection_id_watch_kwargs() -> None:
    kwargs = post_collections_collection_id_watch._get_kwargs(collection_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/collections/42/watch"


def test_get_collections_collection_id_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(204, content=b""))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = get_collections_collection_id.sync_detailed(collection_id=42, client=client)
    assert response.status_code == 204
    assert response.content is not None
