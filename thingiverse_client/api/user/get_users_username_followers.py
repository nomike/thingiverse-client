from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_users_username_followers_response_401 import GetUsersUsernameFollowersResponse401
from ...models.get_users_username_followers_response_403 import GetUsersUsernameFollowersResponse403
from ...models.get_users_username_followers_response_404 import GetUsersUsernameFollowersResponse404
from ...models.user_summary_schema_2 import UserSummarySchema2
from ...types import Response


def _get_kwargs(
    username: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/{username}/followers".format(
            username=quote(str(username), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetUsersUsernameFollowersResponse401
    | GetUsersUsernameFollowersResponse403
    | GetUsersUsernameFollowersResponse404
    | list[UserSummarySchema2]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UserSummarySchema2.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetUsersUsernameFollowersResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetUsersUsernameFollowersResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetUsersUsernameFollowersResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetUsersUsernameFollowersResponse401
    | GetUsersUsernameFollowersResponse403
    | GetUsersUsernameFollowersResponse404
    | list[UserSummarySchema2]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetUsersUsernameFollowersResponse401
    | GetUsersUsernameFollowersResponse403
    | GetUsersUsernameFollowersResponse404
    | list[UserSummarySchema2]
]:
    """Get followers

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersUsernameFollowersResponse401 | GetUsersUsernameFollowersResponse403 | GetUsersUsernameFollowersResponse404 | list[UserSummarySchema2]]
    """

    kwargs = _get_kwargs(
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetUsersUsernameFollowersResponse401
    | GetUsersUsernameFollowersResponse403
    | GetUsersUsernameFollowersResponse404
    | list[UserSummarySchema2]
    | None
):
    """Get followers

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersUsernameFollowersResponse401 | GetUsersUsernameFollowersResponse403 | GetUsersUsernameFollowersResponse404 | list[UserSummarySchema2]
    """

    return sync_detailed(
        username=username,
        client=client,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetUsersUsernameFollowersResponse401
    | GetUsersUsernameFollowersResponse403
    | GetUsersUsernameFollowersResponse404
    | list[UserSummarySchema2]
]:
    """Get followers

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersUsernameFollowersResponse401 | GetUsersUsernameFollowersResponse403 | GetUsersUsernameFollowersResponse404 | list[UserSummarySchema2]]
    """

    kwargs = _get_kwargs(
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetUsersUsernameFollowersResponse401
    | GetUsersUsernameFollowersResponse403
    | GetUsersUsernameFollowersResponse404
    | list[UserSummarySchema2]
    | None
):
    """Get followers

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersUsernameFollowersResponse401 | GetUsersUsernameFollowersResponse403 | GetUsersUsernameFollowersResponse404 | list[UserSummarySchema2]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
        )
    ).parsed
