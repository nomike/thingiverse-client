"""Unit tests for the thing API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.thing import (
    delete_things_thing_id,
    delete_things_thing_id_collections,
    delete_things_thing_id_files_file_id,
    delete_things_thing_id_images_image_id,
    delete_things_thing_id_likes,
    get_things_0_random,
    get_things_thing_id,
    get_things_thing_id_ancestors,
    get_things_thing_id_categories,
    get_things_thing_id_comments,
    get_things_thing_id_copies,
    get_things_thing_id_derivatives,
    get_things_thing_id_files,
    get_things_thing_id_files_file_id,
    get_things_thing_id_images,
    get_things_thing_id_images_image_id,
    get_things_thing_id_likes,
    get_things_thing_id_prints,
    get_things_thing_id_root_comments,
    get_things_thing_id_tags,
    get_things_thing_id_threaded_comments,
    patch_things_thing_id,
    patch_things_thing_id_images_image_id,
    post_things,
    post_things_thing_id_comments,
    post_things_thing_id_copies,
    post_things_thing_id_likes,
    post_things_thing_id_publish,
    post_things_thing_id_toggle_watch,
)


def test_delete_things_thing_id_kwargs() -> None:
    kwargs = delete_things_thing_id._get_kwargs(thing_id=42)
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/things/42"


def test_delete_things_thing_id_collections_kwargs() -> None:
    kwargs = delete_things_thing_id_collections._get_kwargs(thing_id=42)
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/things/42/collections"


def test_delete_things_thing_id_files_file_id_kwargs() -> None:
    kwargs = delete_things_thing_id_files_file_id._get_kwargs(thing_id=42, file_id=42)
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/things/42/files/42"


def test_delete_things_thing_id_images_image_id_kwargs() -> None:
    kwargs = delete_things_thing_id_images_image_id._get_kwargs(thing_id=42, image_id=42)
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/things/42/images/42"


def test_delete_things_thing_id_likes_kwargs() -> None:
    kwargs = delete_things_thing_id_likes._get_kwargs(thing_id=42)
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/things/42/likes"


def test_get_things_0_random_kwargs() -> None:
    kwargs = get_things_0_random._get_kwargs()
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/things/0/random"


def test_get_things_thing_id_kwargs() -> None:
    kwargs = get_things_thing_id._get_kwargs(thing_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/things/42"


def test_get_things_thing_id_ancestors_kwargs() -> None:
    kwargs = get_things_thing_id_ancestors._get_kwargs(thing_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/things/42/ancestors"


def test_get_things_thing_id_categories_kwargs() -> None:
    kwargs = get_things_thing_id_categories._get_kwargs(thing_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/things/42/categories"


def test_get_things_thing_id_comments_kwargs() -> None:
    kwargs = get_things_thing_id_comments._get_kwargs(thing_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/things/42/comments"


def test_get_things_thing_id_copies_kwargs() -> None:
    kwargs = get_things_thing_id_copies._get_kwargs(thing_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/things/42/copies"


def test_get_things_thing_id_derivatives_kwargs() -> None:
    kwargs = get_things_thing_id_derivatives._get_kwargs(thing_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/things/42/derivatives"


def test_get_things_thing_id_files_kwargs() -> None:
    kwargs = get_things_thing_id_files._get_kwargs(thing_id=42, file_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/things/42/files"


def test_get_things_thing_id_files_file_id_kwargs() -> None:
    kwargs = get_things_thing_id_files_file_id._get_kwargs(thing_id=42, file_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/things/42/files/42"


def test_get_things_thing_id_images_kwargs() -> None:
    kwargs = get_things_thing_id_images._get_kwargs(
        thing_id=42, size="test-value", type_="test-value"
    )
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/things/42/images"


def test_get_things_thing_id_images_image_id_kwargs() -> None:
    kwargs = get_things_thing_id_images_image_id._get_kwargs(
        thing_id=42, image_id=42, size="test-value", type_="test-value"
    )
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/things/42/images/42"


def test_get_things_thing_id_likes_kwargs() -> None:
    kwargs = get_things_thing_id_likes._get_kwargs(thing_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/things/42/likes"


def test_get_things_thing_id_prints_kwargs() -> None:
    kwargs = get_things_thing_id_prints._get_kwargs(thing_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/things/42/prints"


def test_get_things_thing_id_root_comments_kwargs() -> None:
    kwargs = get_things_thing_id_root_comments._get_kwargs(thing_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/things/42/root-comments"


def test_get_things_thing_id_tags_kwargs() -> None:
    kwargs = get_things_thing_id_tags._get_kwargs(thing_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/things/42/tags"


def test_get_things_thing_id_threaded_comments_kwargs() -> None:
    kwargs = get_things_thing_id_threaded_comments._get_kwargs(thing_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/things/42/threaded-comments"


def test_patch_things_thing_id_kwargs() -> None:
    kwargs = patch_things_thing_id._get_kwargs(thing_id=42)
    assert kwargs["method"] == "patch"
    assert kwargs["url"] == "/things/42"


def test_patch_things_thing_id_images_image_id_kwargs() -> None:
    kwargs = patch_things_thing_id_images_image_id._get_kwargs(thing_id=42, image_id=42)
    assert kwargs["method"] == "patch"
    assert kwargs["url"] == "/things/42/images/42"


def test_post_things_kwargs() -> None:
    kwargs = post_things._get_kwargs()
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/things/"


def test_post_things_thing_id_comments_kwargs() -> None:
    kwargs = post_things_thing_id_comments._get_kwargs(thing_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/things/42/comments"


def test_post_things_thing_id_copies_kwargs() -> None:
    kwargs = post_things_thing_id_copies._get_kwargs(thing_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/things/42/copies"


def test_post_things_thing_id_likes_kwargs() -> None:
    kwargs = post_things_thing_id_likes._get_kwargs(thing_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/things/42/likes"


def test_post_things_thing_id_publish_kwargs() -> None:
    kwargs = post_things_thing_id_publish._get_kwargs(thing_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/things/42/publish"


def test_post_things_thing_id_toggle_watch_kwargs() -> None:
    kwargs = post_things_thing_id_toggle_watch._get_kwargs(thing_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/things/42/toggle-watch"


def test_get_things_thing_id_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(204, content=b""))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = get_things_thing_id.sync_detailed(thing_id=42, client=client)
    assert response.status_code == 204
    assert response.content is not None
