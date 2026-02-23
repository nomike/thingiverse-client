from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_users_username_stats_by_day_start_date_end_date_response_200_item import (
    GetUsersUsernameStatsByDayStartDateEndDateResponse200Item,
)
from ...models.get_users_username_stats_by_day_start_date_end_date_response_401 import (
    GetUsersUsernameStatsByDayStartDateEndDateResponse401,
)
from ...models.get_users_username_stats_by_day_start_date_end_date_response_404 import (
    GetUsersUsernameStatsByDayStartDateEndDateResponse404,
)
from ...types import Response


def _get_kwargs(
    username: str,
    start_date: str,
    end_date: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/{username}/stats-by-day/{start_date}/{end_date}".format(
            username=quote(str(username), safe=""),
            start_date=quote(str(start_date), safe=""),
            end_date=quote(str(end_date), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetUsersUsernameStatsByDayStartDateEndDateResponse401
    | GetUsersUsernameStatsByDayStartDateEndDateResponse404
    | list[GetUsersUsernameStatsByDayStartDateEndDateResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetUsersUsernameStatsByDayStartDateEndDateResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetUsersUsernameStatsByDayStartDateEndDateResponse401.from_dict(
            response.json()
        )

        return response_401

    if response.status_code == 404:
        response_404 = GetUsersUsernameStatsByDayStartDateEndDateResponse404.from_dict(
            response.json()
        )

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetUsersUsernameStatsByDayStartDateEndDateResponse401
    | GetUsersUsernameStatsByDayStartDateEndDateResponse404
    | list[GetUsersUsernameStatsByDayStartDateEndDateResponse200Item]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    start_date: str,
    end_date: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetUsersUsernameStatsByDayStartDateEndDateResponse401
    | GetUsersUsernameStatsByDayStartDateEndDateResponse404
    | list[GetUsersUsernameStatsByDayStartDateEndDateResponse200Item]
]:
    """Get user's analytics of viewing and downloading things per day

    Args:
        username (str):  Example: thingiverse.
        start_date (str):  Example: 2023-03-28.
        end_date (str):  Example: 2023-04-27.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersUsernameStatsByDayStartDateEndDateResponse401 | GetUsersUsernameStatsByDayStartDateEndDateResponse404 | list[GetUsersUsernameStatsByDayStartDateEndDateResponse200Item]]
    """

    kwargs = _get_kwargs(
        username=username,
        start_date=start_date,
        end_date=end_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    start_date: str,
    end_date: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetUsersUsernameStatsByDayStartDateEndDateResponse401
    | GetUsersUsernameStatsByDayStartDateEndDateResponse404
    | list[GetUsersUsernameStatsByDayStartDateEndDateResponse200Item]
    | None
):
    """Get user's analytics of viewing and downloading things per day

    Args:
        username (str):  Example: thingiverse.
        start_date (str):  Example: 2023-03-28.
        end_date (str):  Example: 2023-04-27.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersUsernameStatsByDayStartDateEndDateResponse401 | GetUsersUsernameStatsByDayStartDateEndDateResponse404 | list[GetUsersUsernameStatsByDayStartDateEndDateResponse200Item]
    """

    return sync_detailed(
        username=username,
        start_date=start_date,
        end_date=end_date,
        client=client,
    ).parsed


async def asyncio_detailed(
    username: str,
    start_date: str,
    end_date: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetUsersUsernameStatsByDayStartDateEndDateResponse401
    | GetUsersUsernameStatsByDayStartDateEndDateResponse404
    | list[GetUsersUsernameStatsByDayStartDateEndDateResponse200Item]
]:
    """Get user's analytics of viewing and downloading things per day

    Args:
        username (str):  Example: thingiverse.
        start_date (str):  Example: 2023-03-28.
        end_date (str):  Example: 2023-04-27.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersUsernameStatsByDayStartDateEndDateResponse401 | GetUsersUsernameStatsByDayStartDateEndDateResponse404 | list[GetUsersUsernameStatsByDayStartDateEndDateResponse200Item]]
    """

    kwargs = _get_kwargs(
        username=username,
        start_date=start_date,
        end_date=end_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    start_date: str,
    end_date: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetUsersUsernameStatsByDayStartDateEndDateResponse401
    | GetUsersUsernameStatsByDayStartDateEndDateResponse404
    | list[GetUsersUsernameStatsByDayStartDateEndDateResponse200Item]
    | None
):
    """Get user's analytics of viewing and downloading things per day

    Args:
        username (str):  Example: thingiverse.
        start_date (str):  Example: 2023-03-28.
        end_date (str):  Example: 2023-04-27.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersUsernameStatsByDayStartDateEndDateResponse401 | GetUsersUsernameStatsByDayStartDateEndDateResponse404 | list[GetUsersUsernameStatsByDayStartDateEndDateResponse200Item]
    """

    return (
        await asyncio_detailed(
            username=username,
            start_date=start_date,
            end_date=end_date,
            client=client,
        )
    ).parsed
