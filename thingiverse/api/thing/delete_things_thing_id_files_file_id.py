from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_things_thing_id_files_file_id_response_200 import (
    DeleteThingsThingIdFilesFileIdResponse200,
)
from ...models.delete_things_thing_id_files_file_id_response_401 import (
    DeleteThingsThingIdFilesFileIdResponse401,
)
from ...models.delete_things_thing_id_files_file_id_response_403 import (
    DeleteThingsThingIdFilesFileIdResponse403,
)
from ...models.delete_things_thing_id_files_file_id_response_404 import (
    DeleteThingsThingIdFilesFileIdResponse404,
)
from ...types import Response


def _get_kwargs(
    thing_id: int,
    file_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/things/{thing_id}/files/{file_id}".format(
            thing_id=quote(str(thing_id), safe=""),
            file_id=quote(str(file_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteThingsThingIdFilesFileIdResponse200
    | DeleteThingsThingIdFilesFileIdResponse401
    | DeleteThingsThingIdFilesFileIdResponse403
    | DeleteThingsThingIdFilesFileIdResponse404
    | None
):
    if response.status_code == 200:
        response_200 = DeleteThingsThingIdFilesFileIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = DeleteThingsThingIdFilesFileIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteThingsThingIdFilesFileIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteThingsThingIdFilesFileIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteThingsThingIdFilesFileIdResponse200
    | DeleteThingsThingIdFilesFileIdResponse401
    | DeleteThingsThingIdFilesFileIdResponse403
    | DeleteThingsThingIdFilesFileIdResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    thing_id: int,
    file_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    DeleteThingsThingIdFilesFileIdResponse200
    | DeleteThingsThingIdFilesFileIdResponse401
    | DeleteThingsThingIdFilesFileIdResponse403
    | DeleteThingsThingIdFilesFileIdResponse404
]:
    """Delete a file from a thing

     This cannot be undone.

    Args:
        thing_id (int):  Example: 1004996.
        file_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteThingsThingIdFilesFileIdResponse200 | DeleteThingsThingIdFilesFileIdResponse401 | DeleteThingsThingIdFilesFileIdResponse403 | DeleteThingsThingIdFilesFileIdResponse404]
    """

    kwargs = _get_kwargs(
        thing_id=thing_id,
        file_id=file_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thing_id: int,
    file_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    DeleteThingsThingIdFilesFileIdResponse200
    | DeleteThingsThingIdFilesFileIdResponse401
    | DeleteThingsThingIdFilesFileIdResponse403
    | DeleteThingsThingIdFilesFileIdResponse404
    | None
):
    """Delete a file from a thing

     This cannot be undone.

    Args:
        thing_id (int):  Example: 1004996.
        file_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteThingsThingIdFilesFileIdResponse200 | DeleteThingsThingIdFilesFileIdResponse401 | DeleteThingsThingIdFilesFileIdResponse403 | DeleteThingsThingIdFilesFileIdResponse404
    """

    return sync_detailed(
        thing_id=thing_id,
        file_id=file_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    thing_id: int,
    file_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    DeleteThingsThingIdFilesFileIdResponse200
    | DeleteThingsThingIdFilesFileIdResponse401
    | DeleteThingsThingIdFilesFileIdResponse403
    | DeleteThingsThingIdFilesFileIdResponse404
]:
    """Delete a file from a thing

     This cannot be undone.

    Args:
        thing_id (int):  Example: 1004996.
        file_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteThingsThingIdFilesFileIdResponse200 | DeleteThingsThingIdFilesFileIdResponse401 | DeleteThingsThingIdFilesFileIdResponse403 | DeleteThingsThingIdFilesFileIdResponse404]
    """

    kwargs = _get_kwargs(
        thing_id=thing_id,
        file_id=file_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thing_id: int,
    file_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    DeleteThingsThingIdFilesFileIdResponse200
    | DeleteThingsThingIdFilesFileIdResponse401
    | DeleteThingsThingIdFilesFileIdResponse403
    | DeleteThingsThingIdFilesFileIdResponse404
    | None
):
    """Delete a file from a thing

     This cannot be undone.

    Args:
        thing_id (int):  Example: 1004996.
        file_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteThingsThingIdFilesFileIdResponse200 | DeleteThingsThingIdFilesFileIdResponse401 | DeleteThingsThingIdFilesFileIdResponse403 | DeleteThingsThingIdFilesFileIdResponse404
    """

    return (
        await asyncio_detailed(
            thing_id=thing_id,
            file_id=file_id,
            client=client,
        )
    ).parsed
