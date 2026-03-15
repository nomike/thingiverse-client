from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_users_username_response_401 import GetUsersUsernameResponse401
from ...models.get_users_username_response_403 import GetUsersUsernameResponse403
from ...models.get_users_username_response_404 import GetUsersUsernameResponse404
from ...models.user_schema import UserSchema
from ...types import Response


def _get_kwargs(
    username: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/{username}".format(
            username=quote(str(username), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetUsersUsernameResponse401
    | GetUsersUsernameResponse403
    | GetUsersUsernameResponse404
    | UserSchema
    | None
):
    if response.status_code == 200:
        response_200 = UserSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetUsersUsernameResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetUsersUsernameResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetUsersUsernameResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetUsersUsernameResponse401
    | GetUsersUsernameResponse403
    | GetUsersUsernameResponse404
    | UserSchema
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
    GetUsersUsernameResponse401
    | GetUsersUsernameResponse403
    | GetUsersUsernameResponse404
    | UserSchema
]:
    """Get the specified user

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersUsernameResponse401 | GetUsersUsernameResponse403 | GetUsersUsernameResponse404 | UserSchema]
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
    GetUsersUsernameResponse401
    | GetUsersUsernameResponse403
    | GetUsersUsernameResponse404
    | UserSchema
    | None
):
    """Get the specified user

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersUsernameResponse401 | GetUsersUsernameResponse403 | GetUsersUsernameResponse404 | UserSchema
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
    GetUsersUsernameResponse401
    | GetUsersUsernameResponse403
    | GetUsersUsernameResponse404
    | UserSchema
]:
    """Get the specified user

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersUsernameResponse401 | GetUsersUsernameResponse403 | GetUsersUsernameResponse404 | UserSchema]
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
    GetUsersUsernameResponse401
    | GetUsersUsernameResponse403
    | GetUsersUsernameResponse404
    | UserSchema
    | None
):
    """Get the specified user

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersUsernameResponse401 | GetUsersUsernameResponse403 | GetUsersUsernameResponse404 | UserSchema
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
        )
    ).parsed
