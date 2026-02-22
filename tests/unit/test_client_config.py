"""Unit tests for client and staging/production URL constants."""

from thingiverse_client import (
    BASE_URL_PRODUCTION,
    BASE_URL_STAGING,
    AuthenticatedClient,
    Client,
)


def test_base_url_constants() -> None:
    assert BASE_URL_PRODUCTION == "https://api.thingiverse.com"
    assert BASE_URL_STAGING == "https://api-staging.thingiverse.com"


def test_client_accepts_base_url() -> None:
    client = Client(base_url=BASE_URL_STAGING)
    assert client._base_url == BASE_URL_STAGING
    http_client = client.get_httpx_client()
    assert BASE_URL_STAGING in str(http_client.base_url)


def test_authenticated_client_accepts_base_url() -> None:
    client = AuthenticatedClient(base_url=BASE_URL_STAGING, token="test-token")
    assert client._base_url == BASE_URL_STAGING
