from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_subscriptions_0_analytics_response_200 import (
    GetSubscriptions0AnalyticsResponse200,
)
from ...models.get_subscriptions_0_analytics_response_401 import (
    GetSubscriptions0AnalyticsResponse401,
)
from ...models.get_subscriptions_0_analytics_response_403 import (
    GetSubscriptions0AnalyticsResponse403,
)
from ...models.get_subscriptions_0_analytics_response_404 import (
    GetSubscriptions0AnalyticsResponse404,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/subscriptions/0/analytics",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSubscriptions0AnalyticsResponse200
    | GetSubscriptions0AnalyticsResponse401
    | GetSubscriptions0AnalyticsResponse403
    | GetSubscriptions0AnalyticsResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetSubscriptions0AnalyticsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetSubscriptions0AnalyticsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetSubscriptions0AnalyticsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSubscriptions0AnalyticsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSubscriptions0AnalyticsResponse200
    | GetSubscriptions0AnalyticsResponse401
    | GetSubscriptions0AnalyticsResponse403
    | GetSubscriptions0AnalyticsResponse404
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
    GetSubscriptions0AnalyticsResponse200
    | GetSubscriptions0AnalyticsResponse401
    | GetSubscriptions0AnalyticsResponse403
    | GetSubscriptions0AnalyticsResponse404
]:
    """Get activity analytics from the last 30 Days of a certain user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSubscriptions0AnalyticsResponse200 | GetSubscriptions0AnalyticsResponse401 | GetSubscriptions0AnalyticsResponse403 | GetSubscriptions0AnalyticsResponse404]
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
    GetSubscriptions0AnalyticsResponse200
    | GetSubscriptions0AnalyticsResponse401
    | GetSubscriptions0AnalyticsResponse403
    | GetSubscriptions0AnalyticsResponse404
    | None
):
    """Get activity analytics from the last 30 Days of a certain user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSubscriptions0AnalyticsResponse200 | GetSubscriptions0AnalyticsResponse401 | GetSubscriptions0AnalyticsResponse403 | GetSubscriptions0AnalyticsResponse404
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    GetSubscriptions0AnalyticsResponse200
    | GetSubscriptions0AnalyticsResponse401
    | GetSubscriptions0AnalyticsResponse403
    | GetSubscriptions0AnalyticsResponse404
]:
    """Get activity analytics from the last 30 Days of a certain user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSubscriptions0AnalyticsResponse200 | GetSubscriptions0AnalyticsResponse401 | GetSubscriptions0AnalyticsResponse403 | GetSubscriptions0AnalyticsResponse404]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> (
    GetSubscriptions0AnalyticsResponse200
    | GetSubscriptions0AnalyticsResponse401
    | GetSubscriptions0AnalyticsResponse403
    | GetSubscriptions0AnalyticsResponse404
    | None
):
    """Get activity analytics from the last 30 Days of a certain user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSubscriptions0AnalyticsResponse200 | GetSubscriptions0AnalyticsResponse401 | GetSubscriptions0AnalyticsResponse403 | GetSubscriptions0AnalyticsResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
