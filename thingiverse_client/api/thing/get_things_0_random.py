from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_things_0_random_response_200_item import GetThings0RandomResponse200Item
from ...models.get_things_0_random_response_401 import GetThings0RandomResponse401
from ...models.get_things_0_random_response_403 import GetThings0RandomResponse403
from ...models.get_things_0_random_response_404 import GetThings0RandomResponse404
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/things/0/random",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetThings0RandomResponse401
    | GetThings0RandomResponse403
    | GetThings0RandomResponse404
    | list[GetThings0RandomResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetThings0RandomResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetThings0RandomResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetThings0RandomResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetThings0RandomResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetThings0RandomResponse401
    | GetThings0RandomResponse403
    | GetThings0RandomResponse404
    | list[GetThings0RandomResponse200Item]
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
) -> Response[
    GetThings0RandomResponse401
    | GetThings0RandomResponse403
    | GetThings0RandomResponse404
    | list[GetThings0RandomResponse200Item]
]:
    """Get 5 random things with minimal 1000 likes

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetThings0RandomResponse401 | GetThings0RandomResponse403 | GetThings0RandomResponse404 | list[GetThings0RandomResponse200Item]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> (
    GetThings0RandomResponse401
    | GetThings0RandomResponse403
    | GetThings0RandomResponse404
    | list[GetThings0RandomResponse200Item]
    | None
):
    """Get 5 random things with minimal 1000 likes

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetThings0RandomResponse401 | GetThings0RandomResponse403 | GetThings0RandomResponse404 | list[GetThings0RandomResponse200Item]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    GetThings0RandomResponse401
    | GetThings0RandomResponse403
    | GetThings0RandomResponse404
    | list[GetThings0RandomResponse200Item]
]:
    """Get 5 random things with minimal 1000 likes

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetThings0RandomResponse401 | GetThings0RandomResponse403 | GetThings0RandomResponse404 | list[GetThings0RandomResponse200Item]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> (
    GetThings0RandomResponse401
    | GetThings0RandomResponse403
    | GetThings0RandomResponse404
    | list[GetThings0RandomResponse200Item]
    | None
):
    """Get 5 random things with minimal 1000 likes

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetThings0RandomResponse401 | GetThings0RandomResponse403 | GetThings0RandomResponse404 | list[GetThings0RandomResponse200Item]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
