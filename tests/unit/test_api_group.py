"""Unit tests for the group API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.group import (
    delete_groups_group_id,
    delete_groups_group_id_forum_forum_id,
    delete_groups_group_id_members,
    delete_groups_group_id_things_thing_id,
    get_groups,
    get_groups_group_id,
    get_groups_group_id_forum_by_slug_forum_slug,
    get_groups_group_id_forum_topics_forum_id,
    get_groups_group_id_group_forums,
    get_groups_group_id_group_topics,
    get_groups_group_id_members,
    get_groups_group_id_things,
    patch_groups_group_id,
    post_groups,
    post_groups_group_id_group_forums,
    post_groups_group_id_group_topics_forum_slug,
    post_groups_group_id_image,
    post_groups_group_id_members,
    post_groups_group_id_things_thing_id,
    post_groups_group_id_update_group_forum_forum_id,
)


def test_delete_groups_group_id_kwargs() -> None:
    kwargs = delete_groups_group_id._get_kwargs(group_id=42)
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/groups/42"


def test_delete_groups_group_id_forum_forum_id_kwargs() -> None:
    kwargs = delete_groups_group_id_forum_forum_id._get_kwargs(group_id=42, forum_id=42)
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/groups/42/forum/42"


def test_delete_groups_group_id_members_kwargs() -> None:
    kwargs = delete_groups_group_id_members._get_kwargs(group_id=42)
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/groups/42/members"


def test_delete_groups_group_id_things_thing_id_kwargs() -> None:
    kwargs = delete_groups_group_id_things_thing_id._get_kwargs(group_id=42, thing_id=42)
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/groups/42/things/42"


def test_get_groups_kwargs() -> None:
    kwargs = get_groups._get_kwargs()
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/groups/"


def test_get_groups_group_id_kwargs() -> None:
    kwargs = get_groups_group_id._get_kwargs(group_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/groups/42"


def test_get_groups_group_id_forum_by_slug_forum_slug_kwargs() -> None:
    kwargs = get_groups_group_id_forum_by_slug_forum_slug._get_kwargs(
        group_id=42, forum_slug="test-value"
    )
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/groups/42/forum-by-slug/test-value"


def test_get_groups_group_id_forum_topics_forum_id_kwargs() -> None:
    kwargs = get_groups_group_id_forum_topics_forum_id._get_kwargs(group_id=42, forum_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/groups/42/forum-topics/42"


def test_get_groups_group_id_group_forums_kwargs() -> None:
    kwargs = get_groups_group_id_group_forums._get_kwargs(group_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/groups/42/group-forums"


def test_get_groups_group_id_group_topics_kwargs() -> None:
    kwargs = get_groups_group_id_group_topics._get_kwargs(
        group_id=42, filter_="test-value", sort="test-value"
    )
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/groups/42/group-topics"


def test_get_groups_group_id_members_kwargs() -> None:
    kwargs = get_groups_group_id_members._get_kwargs(group_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/groups/42/members"


def test_get_groups_group_id_things_kwargs() -> None:
    kwargs = get_groups_group_id_things._get_kwargs(group_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/groups/42/things"


def test_patch_groups_group_id_kwargs() -> None:
    kwargs = patch_groups_group_id._get_kwargs(group_id=42)
    assert kwargs["method"] == "patch"
    assert kwargs["url"] == "/groups/42"


def test_post_groups_kwargs() -> None:
    kwargs = post_groups._get_kwargs()
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/groups/"


def test_post_groups_group_id_group_forums_kwargs() -> None:
    kwargs = post_groups_group_id_group_forums._get_kwargs(group_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/groups/42/group-forums"


def test_post_groups_group_id_group_topics_forum_slug_kwargs() -> None:
    kwargs = post_groups_group_id_group_topics_forum_slug._get_kwargs(
        group_id=42, forum_slug="test-value"
    )
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/groups/42/group-topics/test-value"


def test_post_groups_group_id_image_kwargs() -> None:
    kwargs = post_groups_group_id_image._get_kwargs(group_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/groups/42/image"


def test_post_groups_group_id_members_kwargs() -> None:
    kwargs = post_groups_group_id_members._get_kwargs(group_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/groups/42/members"


def test_post_groups_group_id_things_thing_id_kwargs() -> None:
    kwargs = post_groups_group_id_things_thing_id._get_kwargs(group_id=42, thing_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/groups/42/things/42"


def test_post_groups_group_id_update_group_forum_forum_id_kwargs() -> None:
    kwargs = post_groups_group_id_update_group_forum_forum_id._get_kwargs(group_id=42, forum_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/groups/42/update-group-forum/42"


def test_get_groups_group_id_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(200, json={"id": 42}))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = get_groups_group_id.sync_detailed(group_id=42, client=client)
    assert response.status_code == 200
    assert response.content is not None
