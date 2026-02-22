"""Unit tests for the banner API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.banner import get_banner, get_banner_0_page_ad
from thingiverse_client.models.get_banner_0_page_ad_location import GetBanner0PageAdLocation
from thingiverse_client.models.get_banner_location import GetBannerLocation


def test_get_banner_kwargs() -> None:
    kwargs = get_banner._get_kwargs(location=GetBannerLocation.HOME)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/banner"
    assert kwargs["params"]["location"] == "home"


def test_get_banner_0_page_ad_kwargs() -> None:
    kwargs = get_banner_0_page_ad._get_kwargs(location=GetBanner0PageAdLocation.EXPLORE)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/banner/0/page-ad"
    assert kwargs["params"]["location"] == "explore"


def test_get_banner_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(200, json={"id": 1}))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = get_banner.sync_detailed(location=GetBannerLocation.HOME, client=client)
    assert response.status_code == 200
    assert response.content is not None
