"""Unit tests for the file API group."""

import httpx
from thingiverse_client import AuthenticatedClient
from thingiverse_client.api.file import (
    get_files_file_id,
    get_files_file_id_download,
    post_files_0_upload_file,
)


def test_get_files_file_id_kwargs() -> None:
    kwargs = get_files_file_id._get_kwargs(file_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/files/42/"


def test_get_files_file_id_download_kwargs() -> None:
    kwargs = get_files_file_id_download._get_kwargs(file_id=42)
    assert kwargs["method"] == "get"
    assert kwargs["url"] == "/files/42/download"


def test_post_files_0_upload_file_kwargs() -> None:
    kwargs = post_files_0_upload_file._get_kwargs()
    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/files/0/uploadFile"


def test_get_files_file_id_sync_detailed() -> None:
    """Round-trip test: sync_detailed with mock transport."""
    client = AuthenticatedClient(base_url="https://api.thingiverse.com", token="test")
    transport = httpx.MockTransport(lambda req: httpx.Response(200, json={"id": 42}))
    client._client = httpx.Client(base_url=client._base_url, transport=transport)
    response = get_files_file_id.sync_detailed(file_id=42, client=client)
    assert response.status_code == 200
    assert response.content is not None
