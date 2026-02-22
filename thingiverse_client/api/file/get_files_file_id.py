from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_schema import FileSchema
from ...models.get_files_file_id_response_401 import GetFilesFileIdResponse401
from ...models.get_files_file_id_response_403 import GetFilesFileIdResponse403
from ...models.get_files_file_id_response_404 import GetFilesFileIdResponse404
from ...types import Response


def _get_kwargs(
    file_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/files/{file_id}/".format(
            file_id=quote(str(file_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FileSchema
    | GetFilesFileIdResponse401
    | GetFilesFileIdResponse403
    | GetFilesFileIdResponse404
    | None
):
    if response.status_code == 200:
        response_200 = FileSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetFilesFileIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetFilesFileIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetFilesFileIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FileSchema | GetFilesFileIdResponse401 | GetFilesFileIdResponse403 | GetFilesFileIdResponse404
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
    FileSchema | GetFilesFileIdResponse401 | GetFilesFileIdResponse403 | GetFilesFileIdResponse404
]:
    """Get info about a file by id

     Get basic information about how to access a file. For relevant files, a thumbnail image or three.js
    json file may be available.

    Args:
        file_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileSchema | GetFilesFileIdResponse401 | GetFilesFileIdResponse403 | GetFilesFileIdResponse404]
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
    FileSchema
    | GetFilesFileIdResponse401
    | GetFilesFileIdResponse403
    | GetFilesFileIdResponse404
    | None
):
    """Get info about a file by id

     Get basic information about how to access a file. For relevant files, a thumbnail image or three.js
    json file may be available.

    Args:
        file_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileSchema | GetFilesFileIdResponse401 | GetFilesFileIdResponse403 | GetFilesFileIdResponse404
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
    FileSchema | GetFilesFileIdResponse401 | GetFilesFileIdResponse403 | GetFilesFileIdResponse404
]:
    """Get info about a file by id

     Get basic information about how to access a file. For relevant files, a thumbnail image or three.js
    json file may be available.

    Args:
        file_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileSchema | GetFilesFileIdResponse401 | GetFilesFileIdResponse403 | GetFilesFileIdResponse404]
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
    FileSchema
    | GetFilesFileIdResponse401
    | GetFilesFileIdResponse403
    | GetFilesFileIdResponse404
    | None
):
    """Get info about a file by id

     Get basic information about how to access a file. For relevant files, a thumbnail image or three.js
    json file may be available.

    Args:
        file_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileSchema | GetFilesFileIdResponse401 | GetFilesFileIdResponse403 | GetFilesFileIdResponse404
    """

    return (
        await asyncio_detailed(
            file_id=file_id,
            client=client,
        )
    ).parsed
