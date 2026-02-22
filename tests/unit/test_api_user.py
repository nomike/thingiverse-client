"""Unit tests for the user API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.user import (
    delete_users_username,
    delete_users_username_followers,
    get_users_username,
    get_users_username_all_collected_things,
    get_users_username_collections,
    get_users_username_copies,
    get_users_username_downloads,
    get_users_username_event_count,
    get_users_username_favorites,
    get_users_username_followers,
    get_users_username_following,
    get_users_username_likes,
    get_users_username_likesids,
    get_users_username_recommended_tags,
    get_users_username_recommended_things,
    get_users_username_search_term,
    get_users_username_stats_by_day_start_date_end_date,
    get_users_username_stats_by_thing_start_date_end_date,
    get_users_username_things,
    get_users_username_unread_message_count,
    patch_users_username,
    post_users_username_avatar_image,
    post_users_username_cover_image,
    post_users_username_followers,
)


def test_delete_users_username_kwargs() -> None:
    kwargs = delete_users_username._get_kwargs(username="test-value")
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/users/test-value"


def test_delete_users_username_followers_kwargs() -> None:
    kwargs = delete_users_username_followers._get_kwargs(username="test-value")
    assert kwargs["method"] == "delete"
    assert kwargs["url"] == "/users/test-value/followers"


def test_get_users_username_kwargs() -> None:
    kwargs = get_users_username._get_kwargs(username="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/users/test-value"


def test_get_users_username_all_collected_things_kwargs() -> None:
    kwargs = get_users_username_all_collected_things._get_kwargs(username="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/users/test-value/all-collected-things"


def test_get_users_username_collections_kwargs() -> None:
    kwargs = get_users_username_collections._get_kwargs(username="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/users/test-value/collections"


def test_get_users_username_copies_kwargs() -> None:
    kwargs = get_users_username_copies._get_kwargs(username="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/users/test-value/copies"


def test_get_users_username_downloads_kwargs() -> None:
    kwargs = get_users_username_downloads._get_kwargs(username="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/users/test-value/downloads"


def test_get_users_username_event_count_kwargs() -> None:
    kwargs = get_users_username_event_count._get_kwargs(username="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/users/test-value/event-count"


def test_get_users_username_favorites_kwargs() -> None:
    kwargs = get_users_username_favorites._get_kwargs(username="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/users/test-value/favorites"


def test_get_users_username_followers_kwargs() -> None:
    kwargs = get_users_username_followers._get_kwargs(username="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/users/test-value/followers"


def test_get_users_username_following_kwargs() -> None:
    kwargs = get_users_username_following._get_kwargs(username="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/users/test-value/following"


def test_get_users_username_likes_kwargs() -> None:
    kwargs = get_users_username_likes._get_kwargs(username="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/users/test-value/likes"


def test_get_users_username_likesids_kwargs() -> None:
    kwargs = get_users_username_likesids._get_kwargs(username="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/users/test-value/likesids"


def test_get_users_username_recommended_tags_kwargs() -> None:
    kwargs = get_users_username_recommended_tags._get_kwargs(username="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/users/test-value/recommended-tags"


def test_get_users_username_recommended_things_kwargs() -> None:
    kwargs = get_users_username_recommended_things._get_kwargs(username="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/users/test-value/recommended-things"


def test_get_users_username_search_term_kwargs() -> None:
    kwargs = get_users_username_search_term._get_kwargs(username="test-value", term="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/users/test-value/search/test-value"


def test_get_users_username_stats_by_day_start_date_end_date_kwargs() -> None:
    kwargs = get_users_username_stats_by_day_start_date_end_date._get_kwargs(
        username="test-value", start_date="test-value", end_date="test-value"
    )
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/users/test-value/stats-by-day/test-value/test-value"


def test_get_users_username_stats_by_thing_start_date_end_date_kwargs() -> None:
    kwargs = get_users_username_stats_by_thing_start_date_end_date._get_kwargs(
        username="test-value", start_date="test-value", end_date="test-value"
    )
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/users/test-value/stats-by-thing/test-value/test-value"


def test_get_users_username_things_kwargs() -> None:
    kwargs = get_users_username_things._get_kwargs(username="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/users/test-value/things"


def test_get_users_username_unread_message_count_kwargs() -> None:
    kwargs = get_users_username_unread_message_count._get_kwargs(username="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/users/test-value/unread-message-count"


def test_patch_users_username_kwargs() -> None:
    kwargs = patch_users_username._get_kwargs(username="test-value")
    assert kwargs["method"] == "patch"
    assert kwargs["url"] == "/users/test-value"


def test_post_users_username_avatar_image_kwargs() -> None:
    kwargs = post_users_username_avatar_image._get_kwargs(username="test-value")
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/users/test-value/avatar-image"


def test_post_users_username_cover_image_kwargs() -> None:
    kwargs = post_users_username_cover_image._get_kwargs(username="test-value")
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/users/test-value/cover-image"


def test_post_users_username_followers_kwargs() -> None:
    kwargs = post_users_username_followers._get_kwargs(username="test-value")
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/users/test-value/followers"


def test_get_users_username_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(204, content=b""))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = get_users_username.sync_detailed(username="test", client=client)
    assert response.status_code == 204
    assert response.content is not None
