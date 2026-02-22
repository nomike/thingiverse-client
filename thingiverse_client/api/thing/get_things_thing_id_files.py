from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_schema import FileSchema
from ...models.get_things_thing_id_files_response_401 import GetThingsThingIdFilesResponse401
from ...models.get_things_thing_id_files_response_403 import GetThingsThingIdFilesResponse403
from ...models.get_things_thing_id_files_response_404 import GetThingsThingIdFilesResponse404
from ...types import UNSET, Response


def _get_kwargs(
    thing_id: int,
    *,
    file_id: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["file_id"] = file_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/things/{thing_id}/files".format(
            thing_id=quote(str(thing_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetThingsThingIdFilesResponse401
    | GetThingsThingIdFilesResponse403
    | GetThingsThingIdFilesResponse404
    | list[FileSchema]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FileSchema.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetThingsThingIdFilesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetThingsThingIdFilesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetThingsThingIdFilesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetThingsThingIdFilesResponse401
    | GetThingsThingIdFilesResponse403
    | GetThingsThingIdFilesResponse404
    | list[FileSchema]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    thing_id: int,
    *,
    client: AuthenticatedClient,
    file_id: int,
) -> Response[
    GetThingsThingIdFilesResponse401
    | GetThingsThingIdFilesResponse403
    | GetThingsThingIdFilesResponse404
    | list[FileSchema]
]:
    """Get files by thing

     Get a list of files associated with a thing or

    Args:
        thing_id (int):  Example: 1004996.
        file_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetThingsThingIdFilesResponse401 | GetThingsThingIdFilesResponse403 | GetThingsThingIdFilesResponse404 | list[FileSchema]]
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
    *,
    client: AuthenticatedClient,
    file_id: int,
) -> (
    GetThingsThingIdFilesResponse401
    | GetThingsThingIdFilesResponse403
    | GetThingsThingIdFilesResponse404
    | list[FileSchema]
    | None
):
    """Get files by thing

     Get a list of files associated with a thing or

    Args:
        thing_id (int):  Example: 1004996.
        file_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetThingsThingIdFilesResponse401 | GetThingsThingIdFilesResponse403 | GetThingsThingIdFilesResponse404 | list[FileSchema]
    """

    return sync_detailed(
        thing_id=thing_id,
        client=client,
        file_id=file_id,
    ).parsed


async def asyncio_detailed(
    thing_id: int,
    *,
    client: AuthenticatedClient,
    file_id: int,
) -> Response[
    GetThingsThingIdFilesResponse401
    | GetThingsThingIdFilesResponse403
    | GetThingsThingIdFilesResponse404
    | list[FileSchema]
]:
    """Get files by thing

     Get a list of files associated with a thing or

    Args:
        thing_id (int):  Example: 1004996.
        file_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetThingsThingIdFilesResponse401 | GetThingsThingIdFilesResponse403 | GetThingsThingIdFilesResponse404 | list[FileSchema]]
    """

    kwargs = _get_kwargs(
        thing_id=thing_id,
        file_id=file_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thing_id: int,
    *,
    client: AuthenticatedClient,
    file_id: int,
) -> (
    GetThingsThingIdFilesResponse401
    | GetThingsThingIdFilesResponse403
    | GetThingsThingIdFilesResponse404
    | list[FileSchema]
    | None
):
    """Get files by thing

     Get a list of files associated with a thing or

    Args:
        thing_id (int):  Example: 1004996.
        file_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetThingsThingIdFilesResponse401 | GetThingsThingIdFilesResponse403 | GetThingsThingIdFilesResponse404 | list[FileSchema]
    """

    return (
        await asyncio_detailed(
            thing_id=thing_id,
            client=client,
            file_id=file_id,
        )
    ).parsed
