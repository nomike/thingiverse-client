from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_verified_response_401 import GetVerifiedResponse401
from ...models.get_verified_response_403 import GetVerifiedResponse403
from ...models.get_verified_response_404 import GetVerifiedResponse404
from ...models.verified_schema import VerifiedSchema
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/verified",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetVerifiedResponse401
    | GetVerifiedResponse403
    | GetVerifiedResponse404
    | list[VerifiedSchema]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = VerifiedSchema.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetVerifiedResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetVerifiedResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetVerifiedResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetVerifiedResponse401 | GetVerifiedResponse403 | GetVerifiedResponse404 | list[VerifiedSchema]
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
    GetVerifiedResponse401 | GetVerifiedResponse403 | GetVerifiedResponse404 | list[VerifiedSchema]
]:
    """Get the latest things verified

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVerifiedResponse401 | GetVerifiedResponse403 | GetVerifiedResponse404 | list[VerifiedSchema]]
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
    GetVerifiedResponse401
    | GetVerifiedResponse403
    | GetVerifiedResponse404
    | list[VerifiedSchema]
    | None
):
    """Get the latest things verified

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVerifiedResponse401 | GetVerifiedResponse403 | GetVerifiedResponse404 | list[VerifiedSchema]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    GetVerifiedResponse401 | GetVerifiedResponse403 | GetVerifiedResponse404 | list[VerifiedSchema]
]:
    """Get the latest things verified

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVerifiedResponse401 | GetVerifiedResponse403 | GetVerifiedResponse404 | list[VerifiedSchema]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> (
    GetVerifiedResponse401
    | GetVerifiedResponse403
    | GetVerifiedResponse404
    | list[VerifiedSchema]
    | None
):
    """Get the latest things verified

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVerifiedResponse401 | GetVerifiedResponse403 | GetVerifiedResponse404 | list[VerifiedSchema]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
