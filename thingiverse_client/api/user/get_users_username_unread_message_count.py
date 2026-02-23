from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_users_username_unread_message_count_response_200 import (
    GetUsersUsernameUnreadMessageCountResponse200,
)
from ...models.get_users_username_unread_message_count_response_401 import (
    GetUsersUsernameUnreadMessageCountResponse401,
)
from ...models.get_users_username_unread_message_count_response_403 import (
    GetUsersUsernameUnreadMessageCountResponse403,
)
from ...models.get_users_username_unread_message_count_response_404 import (
    GetUsersUsernameUnreadMessageCountResponse404,
)
from ...types import Response


def _get_kwargs(
    username: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/{username}/unread-message-count".format(
            username=quote(str(username), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetUsersUsernameUnreadMessageCountResponse200
    | GetUsersUsernameUnreadMessageCountResponse401
    | GetUsersUsernameUnreadMessageCountResponse403
    | GetUsersUsernameUnreadMessageCountResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetUsersUsernameUnreadMessageCountResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetUsersUsernameUnreadMessageCountResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetUsersUsernameUnreadMessageCountResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetUsersUsernameUnreadMessageCountResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetUsersUsernameUnreadMessageCountResponse200
    | GetUsersUsernameUnreadMessageCountResponse401
    | GetUsersUsernameUnreadMessageCountResponse403
    | GetUsersUsernameUnreadMessageCountResponse404
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
    GetUsersUsernameUnreadMessageCountResponse200
    | GetUsersUsernameUnreadMessageCountResponse401
    | GetUsersUsernameUnreadMessageCountResponse403
    | GetUsersUsernameUnreadMessageCountResponse404
]:
    """Get the count of messages for user

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersUsernameUnreadMessageCountResponse200 | GetUsersUsernameUnreadMessageCountResponse401 | GetUsersUsernameUnreadMessageCountResponse403 | GetUsersUsernameUnreadMessageCountResponse404]
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
    GetUsersUsernameUnreadMessageCountResponse200
    | GetUsersUsernameUnreadMessageCountResponse401
    | GetUsersUsernameUnreadMessageCountResponse403
    | GetUsersUsernameUnreadMessageCountResponse404
    | None
):
    """Get the count of messages for user

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersUsernameUnreadMessageCountResponse200 | GetUsersUsernameUnreadMessageCountResponse401 | GetUsersUsernameUnreadMessageCountResponse403 | GetUsersUsernameUnreadMessageCountResponse404
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
    GetUsersUsernameUnreadMessageCountResponse200
    | GetUsersUsernameUnreadMessageCountResponse401
    | GetUsersUsernameUnreadMessageCountResponse403
    | GetUsersUsernameUnreadMessageCountResponse404
]:
    """Get the count of messages for user

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersUsernameUnreadMessageCountResponse200 | GetUsersUsernameUnreadMessageCountResponse401 | GetUsersUsernameUnreadMessageCountResponse403 | GetUsersUsernameUnreadMessageCountResponse404]
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
    GetUsersUsernameUnreadMessageCountResponse200
    | GetUsersUsernameUnreadMessageCountResponse401
    | GetUsersUsernameUnreadMessageCountResponse403
    | GetUsersUsernameUnreadMessageCountResponse404
    | None
):
    """Get the count of messages for user

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersUsernameUnreadMessageCountResponse200 | GetUsersUsernameUnreadMessageCountResponse401 | GetUsersUsernameUnreadMessageCountResponse403 | GetUsersUsernameUnreadMessageCountResponse404
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
        )
    ).parsed
