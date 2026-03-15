from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_files_file_id_download_response_401 import GetFilesFileIdDownloadResponse401
from ...models.get_files_file_id_download_response_403 import GetFilesFileIdDownloadResponse403
from ...models.get_files_file_id_download_response_404 import GetFilesFileIdDownloadResponse404
from ...types import Response


def _get_kwargs(
    file_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/files/{file_id}/download".format(
            file_id=quote(str(file_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetFilesFileIdDownloadResponse401
    | GetFilesFileIdDownloadResponse403
    | GetFilesFileIdDownloadResponse404
    | None
):
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = GetFilesFileIdDownloadResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetFilesFileIdDownloadResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetFilesFileIdDownloadResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetFilesFileIdDownloadResponse401
    | GetFilesFileIdDownloadResponse403
    | GetFilesFileIdDownloadResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    Any
    | GetFilesFileIdDownloadResponse401
    | GetFilesFileIdDownloadResponse403
    | GetFilesFileIdDownloadResponse404
]:
    """Get tracked download URL

     Redirects to the requested file and adds an entry to the user's download history for use with the
    GET /users/{$username}/downloads endpoint, as opposed to the public url which is anonymous.

    Args:
        file_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFilesFileIdDownloadResponse401 | GetFilesFileIdDownloadResponse403 | GetFilesFileIdDownloadResponse404]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    Any
    | GetFilesFileIdDownloadResponse401
    | GetFilesFileIdDownloadResponse403
    | GetFilesFileIdDownloadResponse404
    | None
):
    """Get tracked download URL

     Redirects to the requested file and adds an entry to the user's download history for use with the
    GET /users/{$username}/downloads endpoint, as opposed to the public url which is anonymous.

    Args:
        file_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFilesFileIdDownloadResponse401 | GetFilesFileIdDownloadResponse403 | GetFilesFileIdDownloadResponse404
    """

    return sync_detailed(
        file_id=file_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    file_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    Any
    | GetFilesFileIdDownloadResponse401
    | GetFilesFileIdDownloadResponse403
    | GetFilesFileIdDownloadResponse404
]:
    """Get tracked download URL

     Redirects to the requested file and adds an entry to the user's download history for use with the
    GET /users/{$username}/downloads endpoint, as opposed to the public url which is anonymous.

    Args:
        file_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFilesFileIdDownloadResponse401 | GetFilesFileIdDownloadResponse403 | GetFilesFileIdDownloadResponse404]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    Any
    | GetFilesFileIdDownloadResponse401
    | GetFilesFileIdDownloadResponse403
    | GetFilesFileIdDownloadResponse404
    | None
):
    """Get tracked download URL

     Redirects to the requested file and adds an entry to the user's download history for use with the
    GET /users/{$username}/downloads endpoint, as opposed to the public url which is anonymous.

    Args:
        file_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFilesFileIdDownloadResponse401 | GetFilesFileIdDownloadResponse403 | GetFilesFileIdDownloadResponse404
    """

    return (
        await asyncio_detailed(
            file_id=file_id,
            client=client,
        )
    ).parsed
