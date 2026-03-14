from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_things_thing_id_root_comments_response_200_item import (
    GetThingsThingIdRootCommentsResponse200Item,
)
from ...models.get_things_thing_id_root_comments_response_401 import (
    GetThingsThingIdRootCommentsResponse401,
)
from ...models.get_things_thing_id_root_comments_response_403 import (
    GetThingsThingIdRootCommentsResponse403,
)
from ...models.get_things_thing_id_root_comments_response_404 import (
    GetThingsThingIdRootCommentsResponse404,
)
from ...types import Response


def _get_kwargs(
    thing_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/things/{thing_id}/root-comments".format(
            thing_id=quote(str(thing_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetThingsThingIdRootCommentsResponse401
    | GetThingsThingIdRootCommentsResponse403
    | GetThingsThingIdRootCommentsResponse404
    | list[GetThingsThingIdRootCommentsResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetThingsThingIdRootCommentsResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetThingsThingIdRootCommentsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetThingsThingIdRootCommentsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetThingsThingIdRootCommentsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetThingsThingIdRootCommentsResponse401
    | GetThingsThingIdRootCommentsResponse403
    | GetThingsThingIdRootCommentsResponse404
    | list[GetThingsThingIdRootCommentsResponse200Item]
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
    GetThingsThingIdRootCommentsResponse401
    | GetThingsThingIdRootCommentsResponse403
    | GetThingsThingIdRootCommentsResponse404
    | list[GetThingsThingIdRootCommentsResponse200Item]
]:
    """Get an unthreaded paginated list of root comment objects

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetThingsThingIdRootCommentsResponse401 | GetThingsThingIdRootCommentsResponse403 | GetThingsThingIdRootCommentsResponse404 | list[GetThingsThingIdRootCommentsResponse200Item]]
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
    GetThingsThingIdRootCommentsResponse401
    | GetThingsThingIdRootCommentsResponse403
    | GetThingsThingIdRootCommentsResponse404
    | list[GetThingsThingIdRootCommentsResponse200Item]
    | None
):
    """Get an unthreaded paginated list of root comment objects

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetThingsThingIdRootCommentsResponse401 | GetThingsThingIdRootCommentsResponse403 | GetThingsThingIdRootCommentsResponse404 | list[GetThingsThingIdRootCommentsResponse200Item]
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
    GetThingsThingIdRootCommentsResponse401
    | GetThingsThingIdRootCommentsResponse403
    | GetThingsThingIdRootCommentsResponse404
    | list[GetThingsThingIdRootCommentsResponse200Item]
]:
    """Get an unthreaded paginated list of root comment objects

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetThingsThingIdRootCommentsResponse401 | GetThingsThingIdRootCommentsResponse403 | GetThingsThingIdRootCommentsResponse404 | list[GetThingsThingIdRootCommentsResponse200Item]]
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
    GetThingsThingIdRootCommentsResponse401
    | GetThingsThingIdRootCommentsResponse403
    | GetThingsThingIdRootCommentsResponse404
    | list[GetThingsThingIdRootCommentsResponse200Item]
    | None
):
    """Get an unthreaded paginated list of root comment objects

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetThingsThingIdRootCommentsResponse401 | GetThingsThingIdRootCommentsResponse403 | GetThingsThingIdRootCommentsResponse404 | list[GetThingsThingIdRootCommentsResponse200Item]
    """

    return (
        await asyncio_detailed(
            thing_id=thing_id,
            client=client,
        )
    ).parsed
