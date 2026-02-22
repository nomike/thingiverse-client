from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_homebanner_response_401 import GetHomebannerResponse401
from ...models.get_homebanner_response_403 import GetHomebannerResponse403
from ...models.get_homebanner_response_404 import GetHomebannerResponse404
from ...models.homebanner_schema import HomebannerSchema
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/homebanner",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetHomebannerResponse401
    | GetHomebannerResponse403
    | GetHomebannerResponse404
    | HomebannerSchema
    | None
):
    if response.status_code == 200:
        response_200 = HomebannerSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetHomebannerResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetHomebannerResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetHomebannerResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetHomebannerResponse401
    | GetHomebannerResponse403
    | GetHomebannerResponse404
    | HomebannerSchema
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
    GetHomebannerResponse401
    | GetHomebannerResponse403
    | GetHomebannerResponse404
    | HomebannerSchema
]:
    """Get the banner on the home page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetHomebannerResponse401 | GetHomebannerResponse403 | GetHomebannerResponse404 | HomebannerSchema]
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
    GetHomebannerResponse401
    | GetHomebannerResponse403
    | GetHomebannerResponse404
    | HomebannerSchema
    | None
):
    """Get the banner on the home page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetHomebannerResponse401 | GetHomebannerResponse403 | GetHomebannerResponse404 | HomebannerSchema
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    GetHomebannerResponse401
    | GetHomebannerResponse403
    | GetHomebannerResponse404
    | HomebannerSchema
]:
    """Get the banner on the home page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetHomebannerResponse401 | GetHomebannerResponse403 | GetHomebannerResponse404 | HomebannerSchema]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> (
    GetHomebannerResponse401
    | GetHomebannerResponse403
    | GetHomebannerResponse404
    | HomebannerSchema
    | None
):
    """Get the banner on the home page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetHomebannerResponse401 | GetHomebannerResponse403 | GetHomebannerResponse404 | HomebannerSchema
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
