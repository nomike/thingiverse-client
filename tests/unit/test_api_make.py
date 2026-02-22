"""Unit tests for the make API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.make import (
    delete_copies_copy_id,
    delete_copies_copy_id_images_image_id,
    delete_copies_copy_id_likes,
    get_copies,
    get_copies_copy_id,
    get_copies_copy_id_comments,
    get_copies_copy_id_images,
    get_copies_copy_id_root_comments,
    get_copies_copy_id_threaded_comments,
    get_copiesreturncomplete,
    patch_copies_copy_id,
    patch_copies_copy_id_images_image_id,
    post_copies_copy_id_comments,
    post_copies_copy_id_images,
    post_copies_copy_id_likes,
    post_copies_copy_id_restore,
    post_copies_copy_id_toggle_watch,
)


def test_delete_copies_copy_id_kwargs() -> None:
    kwargs = delete_copies_copy_id._get_kwargs(copy_id=42)
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/copies/42/"


def test_delete_copies_copy_id_images_image_id_kwargs() -> None:
    kwargs = delete_copies_copy_id_images_image_id._get_kwargs(copy_id=42, image_id=42)
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/copies/42/images/42"


def test_delete_copies_copy_id_likes_kwargs() -> None:
    kwargs = delete_copies_copy_id_likes._get_kwargs(copy_id=42)
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/copies/42/likes"


def test_get_copies_kwargs() -> None:
    kwargs = get_copies._get_kwargs()
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/copies/"


def test_get_copies_copy_id_kwargs() -> None:
    kwargs = get_copies_copy_id._get_kwargs(copy_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/copies/42/"


def test_get_copies_copy_id_comments_kwargs() -> None:
    kwargs = get_copies_copy_id_comments._get_kwargs(copy_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/copies/42/comments"


def test_get_copies_copy_id_images_kwargs() -> None:
    kwargs = get_copies_copy_id_images._get_kwargs(copy_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/copies/42/images"


def test_get_copies_copy_id_root_comments_kwargs() -> None:
    kwargs = get_copies_copy_id_root_comments._get_kwargs(copy_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/copies/42/root-comments"


def test_get_copies_copy_id_threaded_comments_kwargs() -> None:
    kwargs = get_copies_copy_id_threaded_comments._get_kwargs(copy_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/copies/42/threaded-comments"


def test_get_copiesreturncomplete_kwargs() -> None:
    kwargs = get_copiesreturncomplete._get_kwargs()
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/copies?return=complete"


def test_patch_copies_copy_id_kwargs() -> None:
    kwargs = patch_copies_copy_id._get_kwargs(copy_id=42)
    assert kwargs["method"] == "patch"
    assert kwargs["url"] == "/copies/42/"


def test_patch_copies_copy_id_images_image_id_kwargs() -> None:
    kwargs = patch_copies_copy_id_images_image_id._get_kwargs(copy_id=42, image_id=42)
    assert kwargs["method"] == "patch"
    assert kwargs["url"] == "/copies/42/images/42"


def test_post_copies_copy_id_comments_kwargs() -> None:
    kwargs = post_copies_copy_id_comments._get_kwargs(copy_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/copies/42/comments"


def test_post_copies_copy_id_images_kwargs() -> None:
    kwargs = post_copies_copy_id_images._get_kwargs(copy_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/copies/42/images"


def test_post_copies_copy_id_likes_kwargs() -> None:
    kwargs = post_copies_copy_id_likes._get_kwargs(copy_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/copies/42/likes"


def test_post_copies_copy_id_restore_kwargs() -> None:
    kwargs = post_copies_copy_id_restore._get_kwargs(copy_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/copies/42/restore"


def test_post_copies_copy_id_toggle_watch_kwargs() -> None:
    kwargs = post_copies_copy_id_toggle_watch._get_kwargs(copy_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/copies/42/toggle-watch"


def test_get_copies_copy_id_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(200, json={"id": 42}))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = get_copies_copy_id.sync_detailed(copy_id=42, client=client)
    assert response.status_code == 200
    assert response.content is not None
