from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_subscriptions_0_dashboard_response_200 import (
    GetSubscriptions0DashboardResponse200,
)
from ...models.get_subscriptions_0_dashboard_response_401 import (
    GetSubscriptions0DashboardResponse401,
)
from ...models.get_subscriptions_0_dashboard_response_403 import (
    GetSubscriptions0DashboardResponse403,
)
from ...models.get_subscriptions_0_dashboard_response_404 import (
    GetSubscriptions0DashboardResponse404,
)
from ...models.get_subscriptions_0_dashboard_type import GetSubscriptions0DashboardType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: GetSubscriptions0DashboardType,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_type_ = type_.value
    params["type"] = json_type_

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/subscriptions/0/dashboard",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSubscriptions0DashboardResponse200
    | GetSubscriptions0DashboardResponse401
    | GetSubscriptions0DashboardResponse403
    | GetSubscriptions0DashboardResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetSubscriptions0DashboardResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetSubscriptions0DashboardResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetSubscriptions0DashboardResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSubscriptions0DashboardResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSubscriptions0DashboardResponse200
    | GetSubscriptions0DashboardResponse401
    | GetSubscriptions0DashboardResponse403
    | GetSubscriptions0DashboardResponse404
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
    type_: GetSubscriptions0DashboardType,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[
    GetSubscriptions0DashboardResponse200
    | GetSubscriptions0DashboardResponse401
    | GetSubscriptions0DashboardResponse403
    | GetSubscriptions0DashboardResponse404
]:
    """Get activities of User in Dashboard page

    Args:
        type_ (GetSubscriptions0DashboardType):
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSubscriptions0DashboardResponse200 | GetSubscriptions0DashboardResponse401 | GetSubscriptions0DashboardResponse403 | GetSubscriptions0DashboardResponse404]
    """

    kwargs = _get_kwargs(
        type_=type_,
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
    type_: GetSubscriptions0DashboardType,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> (
    GetSubscriptions0DashboardResponse200
    | GetSubscriptions0DashboardResponse401
    | GetSubscriptions0DashboardResponse403
    | GetSubscriptions0DashboardResponse404
    | None
):
    """Get activities of User in Dashboard page

    Args:
        type_ (GetSubscriptions0DashboardType):
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSubscriptions0DashboardResponse200 | GetSubscriptions0DashboardResponse401 | GetSubscriptions0DashboardResponse403 | GetSubscriptions0DashboardResponse404
    """

    return sync_detailed(
        client=client,
        type_=type_,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    type_: GetSubscriptions0DashboardType,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[
    GetSubscriptions0DashboardResponse200
    | GetSubscriptions0DashboardResponse401
    | GetSubscriptions0DashboardResponse403
    | GetSubscriptions0DashboardResponse404
]:
    """Get activities of User in Dashboard page

    Args:
        type_ (GetSubscriptions0DashboardType):
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSubscriptions0DashboardResponse200 | GetSubscriptions0DashboardResponse401 | GetSubscriptions0DashboardResponse403 | GetSubscriptions0DashboardResponse404]
    """

    kwargs = _get_kwargs(
        type_=type_,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    type_: GetSubscriptions0DashboardType,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> (
    GetSubscriptions0DashboardResponse200
    | GetSubscriptions0DashboardResponse401
    | GetSubscriptions0DashboardResponse403
    | GetSubscriptions0DashboardResponse404
    | None
):
    """Get activities of User in Dashboard page

    Args:
        type_ (GetSubscriptions0DashboardType):
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSubscriptions0DashboardResponse200 | GetSubscriptions0DashboardResponse401 | GetSubscriptions0DashboardResponse403 | GetSubscriptions0DashboardResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            page=page,
            per_page=per_page,
        )
    ).parsed
