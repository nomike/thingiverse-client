"""Unit tests for the group_topic API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.group_topic import (
    delete_grouptopics_grouptopic_id,
    delete_grouptopics_grouptopic_id_pin,
    delete_grouptopics_grouptopic_id_watch,
    get_grouptopics_grouptopic_id,
    get_grouptopics_grouptopic_id_comments,
    get_grouptopics_grouptopic_id_forumtopics_comments,
    get_grouptopics_grouptopic_id_root_comments,
    patch_grouptopics_grouptopic_id,
    post_grouptopics_grouptopic_id_comments,
    post_grouptopics_grouptopic_id_pin,
    post_grouptopics_grouptopic_id_update,
    post_grouptopics_grouptopic_id_watch,
)


def test_delete_grouptopics_grouptopic_id_kwargs() -> None:
    kwargs = delete_grouptopics_grouptopic_id._get_kwargs(grouptopic_id=42)
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/grouptopics/42/"


def test_delete_grouptopics_grouptopic_id_pin_kwargs() -> None:
    kwargs = delete_grouptopics_grouptopic_id_pin._get_kwargs(grouptopic_id=42)
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/grouptopics/42/pin"


def test_delete_grouptopics_grouptopic_id_watch_kwargs() -> None:
    kwargs = delete_grouptopics_grouptopic_id_watch._get_kwargs(grouptopic_id=42)
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/grouptopics/42/watch"


def test_get_grouptopics_grouptopic_id_kwargs() -> None:
    kwargs = get_grouptopics_grouptopic_id._get_kwargs(grouptopic_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/grouptopics/42/"


def test_get_grouptopics_grouptopic_id_comments_kwargs() -> None:
    kwargs = get_grouptopics_grouptopic_id_comments._get_kwargs(grouptopic_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/grouptopics/42/comments"


def test_get_grouptopics_grouptopic_id_forumtopics_comments_kwargs() -> None:
    kwargs = get_grouptopics_grouptopic_id_forumtopics_comments._get_kwargs(grouptopic_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/grouptopics/42/forumtopics-comments"


def test_get_grouptopics_grouptopic_id_root_comments_kwargs() -> None:
    kwargs = get_grouptopics_grouptopic_id_root_comments._get_kwargs(grouptopic_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/grouptopics/42/root-comments"


def test_patch_grouptopics_grouptopic_id_kwargs() -> None:
    kwargs = patch_grouptopics_grouptopic_id._get_kwargs(grouptopic_id=42)
    assert kwargs["method"] == "patch"
    assert kwargs["url"] == "/grouptopics/42/"


def test_post_grouptopics_grouptopic_id_comments_kwargs() -> None:
    kwargs = post_grouptopics_grouptopic_id_comments._get_kwargs(grouptopic_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/grouptopics/42/comments"


def test_post_grouptopics_grouptopic_id_pin_kwargs() -> None:
    kwargs = post_grouptopics_grouptopic_id_pin._get_kwargs(grouptopic_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/grouptopics/42/pin"


def test_post_grouptopics_grouptopic_id_update_kwargs() -> None:
    kwargs = post_grouptopics_grouptopic_id_update._get_kwargs(grouptopic_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/grouptopics/42/update"


def test_post_grouptopics_grouptopic_id_watch_kwargs() -> None:
    kwargs = post_grouptopics_grouptopic_id_watch._get_kwargs(grouptopic_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/grouptopics/42/watch"


def test_get_grouptopics_grouptopic_id_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(200, json={"id": 42}))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = get_grouptopics_grouptopic_id.sync_detailed(grouptopic_id=42, client=client)
    assert response.status_code == 200
    assert response.content is not None
