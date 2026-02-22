"""Unit tests for the search API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.search import (
    get_search_tag_tag,
    get_search_term_autocomplete,
    get_search_term_typecollections,
    get_search_term_typemakes,
    get_search_term_typethings,
    get_search_term_typeusers,
)


def test_get_search_tag_tag_kwargs() -> None:
    kwargs = get_search_tag_tag._get_kwargs(tag="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/search/test-value/tag"


def test_get_search_term_autocomplete_kwargs() -> None:
    kwargs = get_search_term_autocomplete._get_kwargs(term="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/search/test-value/autocomplete"


def test_get_search_term_typecollections_kwargs() -> None:
    kwargs = get_search_term_typecollections._get_kwargs(term="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/search/test-value/?type=collections"


def test_get_search_term_typemakes_kwargs() -> None:
    kwargs = get_search_term_typemakes._get_kwargs(term="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/search/test-value/?type=makes"


def test_get_search_term_typethings_kwargs() -> None:
    kwargs = get_search_term_typethings._get_kwargs(term="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/search/test-value/?type=things"


def test_get_search_term_typeusers_kwargs() -> None:
    kwargs = get_search_term_typeusers._get_kwargs(term="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/search/test-value/?type=users"


def test_get_search_tag_tag_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(200, json={"id": 42}))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = get_search_tag_tag.sync_detailed(tag="test", client=client)
    assert response.status_code == 200
    assert response.content is not None
