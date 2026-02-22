"""Unit tests for the tag API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.tag import (
    get_tags,
    get_tags_0_popular,
    get_tags_tag,
    get_tags_tag_search_tags,
    get_tags_tag_things,
)


def test_get_tags_kwargs() -> None:
    kwargs = get_tags._get_kwargs()
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/tags/"


def test_get_tags_0_popular_kwargs() -> None:
    kwargs = get_tags_0_popular._get_kwargs()
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/tags/0/popular"


def test_get_tags_tag_kwargs() -> None:
    kwargs = get_tags_tag._get_kwargs(tag="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/tags/test-value/"


def test_get_tags_tag_search_tags_kwargs() -> None:
    kwargs = get_tags_tag_search_tags._get_kwargs(tag="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/tags/test-value/search-tags"


def test_get_tags_tag_things_kwargs() -> None:
    kwargs = get_tags_tag_things._get_kwargs(tag="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/tags/test-value/things"


def test_get_tags_tag_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(200, json={"id": 42}))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = get_tags_tag.sync_detailed(tag="test", client=client)
    assert response.status_code == 200
    assert response.content is not None
