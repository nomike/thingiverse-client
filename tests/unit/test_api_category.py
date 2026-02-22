"""Unit tests for the category API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.category import (
    get_categories,
    get_categories_slug,
    get_categories_slug_things,
    get_categoriesreturncomplete,
)


def test_get_categories_kwargs() -> None:
    kwargs = get_categories._get_kwargs()
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/categories"


def test_get_categories_slug_kwargs() -> None:
    kwargs = get_categories_slug._get_kwargs(slug="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/categories/test-value"


def test_get_categories_slug_things_kwargs() -> None:
    kwargs = get_categories_slug_things._get_kwargs(slug="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/categories/test-value/things"


def test_get_categoriesreturncomplete_kwargs() -> None:
    kwargs = get_categoriesreturncomplete._get_kwargs()
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/categories?return=complete"


def test_get_categories_slug_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(200, json={"id": 42}))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = get_categories_slug.sync_detailed(slug="test", client=client)
    assert response.status_code == 200
    assert response.content is not None
