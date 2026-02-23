from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_popular_response_401 import GetPopularResponse401
from ...models.get_popular_response_403 import GetPopularResponse403
from ...models.get_popular_response_404 import GetPopularResponse404
from ...models.short_thing_schema import ShortThingSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
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
        "url": "/popular",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetPopularResponse401
    | GetPopularResponse403
    | GetPopularResponse404
    | list[ShortThingSchema]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ShortThingSchema.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetPopularResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetPopularResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetPopularResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetPopularResponse401 | GetPopularResponse403 | GetPopularResponse404 | list[ShortThingSchema]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[
    GetPopularResponse401 | GetPopularResponse403 | GetPopularResponse404 | list[ShortThingSchema]
]:
    """Get the most popular things

     You can use `GET /search` with the `sort=popular` parameter now.

    Args:
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPopularResponse401 | GetPopularResponse403 | GetPopularResponse404 | list[ShortThingSchema]]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> (
    GetPopularResponse401
    | GetPopularResponse403
    | GetPopularResponse404
    | list[ShortThingSchema]
    | None
):
    """Get the most popular things

     You can use `GET /search` with the `sort=popular` parameter now.

    Args:
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPopularResponse401 | GetPopularResponse403 | GetPopularResponse404 | list[ShortThingSchema]
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[
    GetPopularResponse401 | GetPopularResponse403 | GetPopularResponse404 | list[ShortThingSchema]
]:
    """Get the most popular things

     You can use `GET /search` with the `sort=popular` parameter now.

    Args:
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPopularResponse401 | GetPopularResponse403 | GetPopularResponse404 | list[ShortThingSchema]]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> (
    GetPopularResponse401
    | GetPopularResponse403
    | GetPopularResponse404
    | list[ShortThingSchema]
    | None
):
    """Get the most popular things

     You can use `GET /search` with the `sort=popular` parameter now.

    Args:
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPopularResponse401 | GetPopularResponse403 | GetPopularResponse404 | list[ShortThingSchema]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
        )
    ).parsed
