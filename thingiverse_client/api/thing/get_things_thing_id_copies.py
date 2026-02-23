from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_things_thing_id_copies_response_200_item import (
    GetThingsThingIdCopiesResponse200Item,
)
from ...models.get_things_thing_id_copies_response_401 import GetThingsThingIdCopiesResponse401
from ...models.get_things_thing_id_copies_response_403 import GetThingsThingIdCopiesResponse403
from ...models.get_things_thing_id_copies_response_404 import GetThingsThingIdCopiesResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    thing_id: int,
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/things/{thing_id}/copies".format(
            thing_id=quote(str(thing_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetThingsThingIdCopiesResponse401
    | GetThingsThingIdCopiesResponse403
    | GetThingsThingIdCopiesResponse404
    | list[GetThingsThingIdCopiesResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetThingsThingIdCopiesResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetThingsThingIdCopiesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetThingsThingIdCopiesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetThingsThingIdCopiesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetThingsThingIdCopiesResponse401
    | GetThingsThingIdCopiesResponse403
    | GetThingsThingIdCopiesResponse404
    | list[GetThingsThingIdCopiesResponse200Item]
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
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[
    GetThingsThingIdCopiesResponse401
    | GetThingsThingIdCopiesResponse403
    | GetThingsThingIdCopiesResponse404
    | list[GetThingsThingIdCopiesResponse200Item]
]:
    """Get copies/makes of a thing

    Args:
        thing_id (int):  Example: 1004996.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetThingsThingIdCopiesResponse401 | GetThingsThingIdCopiesResponse403 | GetThingsThingIdCopiesResponse404 | list[GetThingsThingIdCopiesResponse200Item]]
    """

    kwargs = _get_kwargs(
        thing_id=thing_id,
        page=page,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thing_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> (
    GetThingsThingIdCopiesResponse401
    | GetThingsThingIdCopiesResponse403
    | GetThingsThingIdCopiesResponse404
    | list[GetThingsThingIdCopiesResponse200Item]
    | None
):
    """Get copies/makes of a thing

    Args:
        thing_id (int):  Example: 1004996.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetThingsThingIdCopiesResponse401 | GetThingsThingIdCopiesResponse403 | GetThingsThingIdCopiesResponse404 | list[GetThingsThingIdCopiesResponse200Item]
    """

    return sync_detailed(
        thing_id=thing_id,
        client=client,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    thing_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[
    GetThingsThingIdCopiesResponse401
    | GetThingsThingIdCopiesResponse403
    | GetThingsThingIdCopiesResponse404
    | list[GetThingsThingIdCopiesResponse200Item]
]:
    """Get copies/makes of a thing

    Args:
        thing_id (int):  Example: 1004996.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetThingsThingIdCopiesResponse401 | GetThingsThingIdCopiesResponse403 | GetThingsThingIdCopiesResponse404 | list[GetThingsThingIdCopiesResponse200Item]]
    """

    kwargs = _get_kwargs(
        thing_id=thing_id,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thing_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> (
    GetThingsThingIdCopiesResponse401
    | GetThingsThingIdCopiesResponse403
    | GetThingsThingIdCopiesResponse404
    | list[GetThingsThingIdCopiesResponse200Item]
    | None
):
    """Get copies/makes of a thing

    Args:
        thing_id (int):  Example: 1004996.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetThingsThingIdCopiesResponse401 | GetThingsThingIdCopiesResponse403 | GetThingsThingIdCopiesResponse404 | list[GetThingsThingIdCopiesResponse200Item]
    """

    return (
        await asyncio_detailed(
            thing_id=thing_id,
            client=client,
            page=page,
            per_page=per_page,
        )
    ).parsed
