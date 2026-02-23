from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_users_username_response_200 import DeleteUsersUsernameResponse200
from ...models.delete_users_username_response_401 import DeleteUsersUsernameResponse401
from ...models.delete_users_username_response_403 import DeleteUsersUsernameResponse403
from ...models.delete_users_username_response_404 import DeleteUsersUsernameResponse404
from ...types import Response


def _get_kwargs(
    username: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/users/{username}".format(
            username=quote(str(username), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteUsersUsernameResponse200
    | DeleteUsersUsernameResponse401
    | DeleteUsersUsernameResponse403
    | DeleteUsersUsernameResponse404
    | None
):
    if response.status_code == 200:
        response_200 = DeleteUsersUsernameResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = DeleteUsersUsernameResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteUsersUsernameResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteUsersUsernameResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteUsersUsernameResponse200
    | DeleteUsersUsernameResponse401
    | DeleteUsersUsernameResponse403
    | DeleteUsersUsernameResponse404
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
    DeleteUsersUsernameResponse200
    | DeleteUsersUsernameResponse401
    | DeleteUsersUsernameResponse403
    | DeleteUsersUsernameResponse404
]:
    """Soft delete a user's account

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteUsersUsernameResponse200 | DeleteUsersUsernameResponse401 | DeleteUsersUsernameResponse403 | DeleteUsersUsernameResponse404]
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
    DeleteUsersUsernameResponse200
    | DeleteUsersUsernameResponse401
    | DeleteUsersUsernameResponse403
    | DeleteUsersUsernameResponse404
    | None
):
    """Soft delete a user's account

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteUsersUsernameResponse200 | DeleteUsersUsernameResponse401 | DeleteUsersUsernameResponse403 | DeleteUsersUsernameResponse404
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
    DeleteUsersUsernameResponse200
    | DeleteUsersUsernameResponse401
    | DeleteUsersUsernameResponse403
    | DeleteUsersUsernameResponse404
]:
    """Soft delete a user's account

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteUsersUsernameResponse200 | DeleteUsersUsernameResponse401 | DeleteUsersUsernameResponse403 | DeleteUsersUsernameResponse404]
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
    DeleteUsersUsernameResponse200
    | DeleteUsersUsernameResponse401
    | DeleteUsersUsernameResponse403
    | DeleteUsersUsernameResponse404
    | None
):
    """Soft delete a user's account

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteUsersUsernameResponse200 | DeleteUsersUsernameResponse401 | DeleteUsersUsernameResponse403 | DeleteUsersUsernameResponse404
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
        )
    ).parsed
