"""Unit tests for the printer API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.printer import get_printers_0_brands, get_printers_0_models


def test_get_printers_0_brands_kwargs() -> None:
    kwargs = get_printers_0_brands._get_kwargs(include_user_defined=True)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/printers/0/brands"


def test_get_printers_0_models_kwargs() -> None:
    kwargs = get_printers_0_models._get_kwargs(include_user_defined=True, brand="test-value")
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/printers/0/models"


def test_get_printers_0_brands_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(204, content=b""))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = get_printers_0_brands.sync_detailed(include_user_defined=True, client=client)
    assert response.status_code == 204
    assert response.content is not None
