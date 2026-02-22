"""Unit tests for the deprecated API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.deprecated import (
    get_featured,
    get_files_file_id_finalize,
    get_newest,
    get_popular,
    post_files_0_finalize_files,
    post_files_file_id_finalize,
)


def test_get_featured_kwargs() -> None:
    kwargs = get_featured._get_kwargs()
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/featured"


def test_get_files_file_id_finalize_kwargs() -> None:
    kwargs = get_files_file_id_finalize._get_kwargs(file_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/files/42/finalize"


def test_get_newest_kwargs() -> None:
    kwargs = get_newest._get_kwargs()
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/newest"


def test_get_popular_kwargs() -> None:
    kwargs = get_popular._get_kwargs()
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/popular"


def test_post_files_0_finalize_files_kwargs() -> None:
    kwargs = post_files_0_finalize_files._get_kwargs()
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/files/0/FinalizeFiles"


def test_post_files_file_id_finalize_kwargs() -> None:
    kwargs = post_files_file_id_finalize._get_kwargs(file_id=42)
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/files/42/finalize"


def test_get_files_file_id_finalize_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(200, json={"id": 42}))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = get_files_file_id_finalize.sync_detailed(file_id=42, client=client)
    assert response.status_code == 200
    assert response.content is not None
