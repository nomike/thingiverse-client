from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_apps_0_approvedandpublished_response_401 import (
    GetApps0ApprovedandpublishedResponse401,
)
from ...models.get_apps_0_approvedandpublished_response_403 import (
    GetApps0ApprovedandpublishedResponse403,
)
from ...models.get_apps_0_approvedandpublished_response_404 import (
    GetApps0ApprovedandpublishedResponse404,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/apps/0/approvedandpublished",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetApps0ApprovedandpublishedResponse401
    | GetApps0ApprovedandpublishedResponse403
    | GetApps0ApprovedandpublishedResponse404
    | list[Any]
    | None
):
    if response.status_code == 200:
        response_200 = cast(list[Any], response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetApps0ApprovedandpublishedResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetApps0ApprovedandpublishedResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetApps0ApprovedandpublishedResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetApps0ApprovedandpublishedResponse401
    | GetApps0ApprovedandpublishedResponse403
    | GetApps0ApprovedandpublishedResponse404
    | list[Any]
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
    GetApps0ApprovedandpublishedResponse401
    | GetApps0ApprovedandpublishedResponse403
    | GetApps0ApprovedandpublishedResponse404
    | list[Any]
]:
    """Get all approved and published apps

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApps0ApprovedandpublishedResponse401 | GetApps0ApprovedandpublishedResponse403 | GetApps0ApprovedandpublishedResponse404 | list[Any]]
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
    GetApps0ApprovedandpublishedResponse401
    | GetApps0ApprovedandpublishedResponse403
    | GetApps0ApprovedandpublishedResponse404
    | list[Any]
    | None
):
    """Get all approved and published apps

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApps0ApprovedandpublishedResponse401 | GetApps0ApprovedandpublishedResponse403 | GetApps0ApprovedandpublishedResponse404 | list[Any]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    GetApps0ApprovedandpublishedResponse401
    | GetApps0ApprovedandpublishedResponse403
    | GetApps0ApprovedandpublishedResponse404
    | list[Any]
]:
    """Get all approved and published apps

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApps0ApprovedandpublishedResponse401 | GetApps0ApprovedandpublishedResponse403 | GetApps0ApprovedandpublishedResponse404 | list[Any]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> (
    GetApps0ApprovedandpublishedResponse401
    | GetApps0ApprovedandpublishedResponse403
    | GetApps0ApprovedandpublishedResponse404
    | list[Any]
    | None
):
    """Get all approved and published apps

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApps0ApprovedandpublishedResponse401 | GetApps0ApprovedandpublishedResponse403 | GetApps0ApprovedandpublishedResponse404 | list[Any]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
