from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_schema import FileSchema
from ...models.post_files_file_id_finalize_response_401 import PostFilesFileIdFinalizeResponse401
from ...models.post_files_file_id_finalize_response_403 import PostFilesFileIdFinalizeResponse403
from ...models.post_files_file_id_finalize_response_404 import PostFilesFileIdFinalizeResponse404
from ...types import Response


def _get_kwargs(
    file_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/files/{file_id}/finalize".format(
            file_id=quote(str(file_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FileSchema
    | PostFilesFileIdFinalizeResponse401
    | PostFilesFileIdFinalizeResponse403
    | PostFilesFileIdFinalizeResponse404
    | None
):
    if response.status_code == 200:
        response_200 = FileSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostFilesFileIdFinalizeResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostFilesFileIdFinalizeResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostFilesFileIdFinalizeResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FileSchema
    | PostFilesFileIdFinalizeResponse401
    | PostFilesFileIdFinalizeResponse403
    | PostFilesFileIdFinalizeResponse404
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
    FileSchema
    | PostFilesFileIdFinalizeResponse401
    | PostFilesFileIdFinalizeResponse403
    | PostFilesFileIdFinalizeResponse404
]:
    """Finalize an uploaded file. DEPRECATED, use FinalizeFiles endpoint instead

    Args:
        file_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileSchema | PostFilesFileIdFinalizeResponse401 | PostFilesFileIdFinalizeResponse403 | PostFilesFileIdFinalizeResponse404]
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
    | PostFilesFileIdFinalizeResponse401
    | PostFilesFileIdFinalizeResponse403
    | PostFilesFileIdFinalizeResponse404
    | None
):
    """Finalize an uploaded file. DEPRECATED, use FinalizeFiles endpoint instead

    Args:
        file_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileSchema | PostFilesFileIdFinalizeResponse401 | PostFilesFileIdFinalizeResponse403 | PostFilesFileIdFinalizeResponse404
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
    FileSchema
    | PostFilesFileIdFinalizeResponse401
    | PostFilesFileIdFinalizeResponse403
    | PostFilesFileIdFinalizeResponse404
]:
    """Finalize an uploaded file. DEPRECATED, use FinalizeFiles endpoint instead

    Args:
        file_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileSchema | PostFilesFileIdFinalizeResponse401 | PostFilesFileIdFinalizeResponse403 | PostFilesFileIdFinalizeResponse404]
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
    | PostFilesFileIdFinalizeResponse401
    | PostFilesFileIdFinalizeResponse403
    | PostFilesFileIdFinalizeResponse404
    | None
):
    """Finalize an uploaded file. DEPRECATED, use FinalizeFiles endpoint instead

    Args:
        file_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileSchema | PostFilesFileIdFinalizeResponse401 | PostFilesFileIdFinalizeResponse403 | PostFilesFileIdFinalizeResponse404
    """

    return (
        await asyncio_detailed(
            file_id=file_id,
            client=client,
        )
    ).parsed
