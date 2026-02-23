from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_things_thing_id_tags_response_200_item import GetThingsThingIdTagsResponse200Item
from ...models.get_things_thing_id_tags_response_401 import GetThingsThingIdTagsResponse401
from ...models.get_things_thing_id_tags_response_403 import GetThingsThingIdTagsResponse403
from ...models.get_things_thing_id_tags_response_404 import GetThingsThingIdTagsResponse404
from ...types import Response


def _get_kwargs(
    thing_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/things/{thing_id}/tags".format(
            thing_id=quote(str(thing_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetThingsThingIdTagsResponse401
    | GetThingsThingIdTagsResponse403
    | GetThingsThingIdTagsResponse404
    | list[GetThingsThingIdTagsResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetThingsThingIdTagsResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetThingsThingIdTagsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetThingsThingIdTagsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetThingsThingIdTagsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetThingsThingIdTagsResponse401
    | GetThingsThingIdTagsResponse403
    | GetThingsThingIdTagsResponse404
    | list[GetThingsThingIdTagsResponse200Item]
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
) -> Response[
    GetThingsThingIdTagsResponse401
    | GetThingsThingIdTagsResponse403
    | GetThingsThingIdTagsResponse404
    | list[GetThingsThingIdTagsResponse200Item]
]:
    """Get tags on this thing

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetThingsThingIdTagsResponse401 | GetThingsThingIdTagsResponse403 | GetThingsThingIdTagsResponse404 | list[GetThingsThingIdTagsResponse200Item]]
    """

    kwargs = _get_kwargs(
        thing_id=thing_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thing_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    GetThingsThingIdTagsResponse401
    | GetThingsThingIdTagsResponse403
    | GetThingsThingIdTagsResponse404
    | list[GetThingsThingIdTagsResponse200Item]
    | None
):
    """Get tags on this thing

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetThingsThingIdTagsResponse401 | GetThingsThingIdTagsResponse403 | GetThingsThingIdTagsResponse404 | list[GetThingsThingIdTagsResponse200Item]
    """

    return sync_detailed(
        thing_id=thing_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    thing_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetThingsThingIdTagsResponse401
    | GetThingsThingIdTagsResponse403
    | GetThingsThingIdTagsResponse404
    | list[GetThingsThingIdTagsResponse200Item]
]:
    """Get tags on this thing

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetThingsThingIdTagsResponse401 | GetThingsThingIdTagsResponse403 | GetThingsThingIdTagsResponse404 | list[GetThingsThingIdTagsResponse200Item]]
    """

    kwargs = _get_kwargs(
        thing_id=thing_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thing_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    GetThingsThingIdTagsResponse401
    | GetThingsThingIdTagsResponse403
    | GetThingsThingIdTagsResponse404
    | list[GetThingsThingIdTagsResponse200Item]
    | None
):
    """Get tags on this thing

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetThingsThingIdTagsResponse401 | GetThingsThingIdTagsResponse403 | GetThingsThingIdTagsResponse404 | list[GetThingsThingIdTagsResponse200Item]
    """

    return (
        await asyncio_detailed(
            thing_id=thing_id,
            client=client,
        )
    ).parsed
