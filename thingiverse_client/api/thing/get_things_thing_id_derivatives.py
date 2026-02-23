from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_things_thing_id_derivatives_response_401 import (
    GetThingsThingIdDerivativesResponse401,
)
from ...models.get_things_thing_id_derivatives_response_403 import (
    GetThingsThingIdDerivativesResponse403,
)
from ...models.get_things_thing_id_derivatives_response_404 import (
    GetThingsThingIdDerivativesResponse404,
)
from ...models.thing_schema import ThingSchema
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
        "url": "/things/{thing_id}/derivatives".format(
            thing_id=quote(str(thing_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetThingsThingIdDerivativesResponse401
    | GetThingsThingIdDerivativesResponse403
    | GetThingsThingIdDerivativesResponse404
    | list[ThingSchema]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ThingSchema.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetThingsThingIdDerivativesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetThingsThingIdDerivativesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetThingsThingIdDerivativesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetThingsThingIdDerivativesResponse401
    | GetThingsThingIdDerivativesResponse403
    | GetThingsThingIdDerivativesResponse404
    | list[ThingSchema]
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
    GetThingsThingIdDerivativesResponse401
    | GetThingsThingIdDerivativesResponse403
    | GetThingsThingIdDerivativesResponse404
    | list[ThingSchema]
]:
    """Get a list of thing derivatives

    Args:
        thing_id (int):  Example: 1004996.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetThingsThingIdDerivativesResponse401 | GetThingsThingIdDerivativesResponse403 | GetThingsThingIdDerivativesResponse404 | list[ThingSchema]]
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
    GetThingsThingIdDerivativesResponse401
    | GetThingsThingIdDerivativesResponse403
    | GetThingsThingIdDerivativesResponse404
    | list[ThingSchema]
    | None
):
    """Get a list of thing derivatives

    Args:
        thing_id (int):  Example: 1004996.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetThingsThingIdDerivativesResponse401 | GetThingsThingIdDerivativesResponse403 | GetThingsThingIdDerivativesResponse404 | list[ThingSchema]
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
    GetThingsThingIdDerivativesResponse401
    | GetThingsThingIdDerivativesResponse403
    | GetThingsThingIdDerivativesResponse404
    | list[ThingSchema]
]:
    """Get a list of thing derivatives

    Args:
        thing_id (int):  Example: 1004996.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetThingsThingIdDerivativesResponse401 | GetThingsThingIdDerivativesResponse403 | GetThingsThingIdDerivativesResponse404 | list[ThingSchema]]
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
    GetThingsThingIdDerivativesResponse401
    | GetThingsThingIdDerivativesResponse403
    | GetThingsThingIdDerivativesResponse404
    | list[ThingSchema]
    | None
):
    """Get a list of thing derivatives

    Args:
        thing_id (int):  Example: 1004996.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetThingsThingIdDerivativesResponse401 | GetThingsThingIdDerivativesResponse403 | GetThingsThingIdDerivativesResponse404 | list[ThingSchema]
    """

    return (
        await asyncio_detailed(
            thing_id=thing_id,
            client=client,
            page=page,
            per_page=per_page,
        )
    ).parsed
