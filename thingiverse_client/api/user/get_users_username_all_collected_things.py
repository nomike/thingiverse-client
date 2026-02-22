from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_users_username_all_collected_things_response_200 import (
    GetUsersUsernameAllCollectedThingsResponse200,
)
from ...models.get_users_username_all_collected_things_response_401 import (
    GetUsersUsernameAllCollectedThingsResponse401,
)
from ...models.get_users_username_all_collected_things_response_403 import (
    GetUsersUsernameAllCollectedThingsResponse403,
)
from ...models.get_users_username_all_collected_things_response_404 import (
    GetUsersUsernameAllCollectedThingsResponse404,
)
from ...types import Response


def _get_kwargs(
    username: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/{username}/all-collected-things".format(
            username=quote(str(username), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetUsersUsernameAllCollectedThingsResponse200
    | GetUsersUsernameAllCollectedThingsResponse401
    | GetUsersUsernameAllCollectedThingsResponse403
    | GetUsersUsernameAllCollectedThingsResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetUsersUsernameAllCollectedThingsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetUsersUsernameAllCollectedThingsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetUsersUsernameAllCollectedThingsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetUsersUsernameAllCollectedThingsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetUsersUsernameAllCollectedThingsResponse200
    | GetUsersUsernameAllCollectedThingsResponse401
    | GetUsersUsernameAllCollectedThingsResponse403
    | GetUsersUsernameAllCollectedThingsResponse404
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
    GetUsersUsernameAllCollectedThingsResponse200
    | GetUsersUsernameAllCollectedThingsResponse401
    | GetUsersUsernameAllCollectedThingsResponse403
    | GetUsersUsernameAllCollectedThingsResponse404
]:
    """Get latest downloaded things by user

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersUsernameAllCollectedThingsResponse200 | GetUsersUsernameAllCollectedThingsResponse401 | GetUsersUsernameAllCollectedThingsResponse403 | GetUsersUsernameAllCollectedThingsResponse404]
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
    GetUsersUsernameAllCollectedThingsResponse200
    | GetUsersUsernameAllCollectedThingsResponse401
    | GetUsersUsernameAllCollectedThingsResponse403
    | GetUsersUsernameAllCollectedThingsResponse404
    | None
):
    """Get latest downloaded things by user

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersUsernameAllCollectedThingsResponse200 | GetUsersUsernameAllCollectedThingsResponse401 | GetUsersUsernameAllCollectedThingsResponse403 | GetUsersUsernameAllCollectedThingsResponse404
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
    GetUsersUsernameAllCollectedThingsResponse200
    | GetUsersUsernameAllCollectedThingsResponse401
    | GetUsersUsernameAllCollectedThingsResponse403
    | GetUsersUsernameAllCollectedThingsResponse404
]:
    """Get latest downloaded things by user

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersUsernameAllCollectedThingsResponse200 | GetUsersUsernameAllCollectedThingsResponse401 | GetUsersUsernameAllCollectedThingsResponse403 | GetUsersUsernameAllCollectedThingsResponse404]
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
    GetUsersUsernameAllCollectedThingsResponse200
    | GetUsersUsernameAllCollectedThingsResponse401
    | GetUsersUsernameAllCollectedThingsResponse403
    | GetUsersUsernameAllCollectedThingsResponse404
    | None
):
    """Get latest downloaded things by user

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersUsernameAllCollectedThingsResponse200 | GetUsersUsernameAllCollectedThingsResponse401 | GetUsersUsernameAllCollectedThingsResponse403 | GetUsersUsernameAllCollectedThingsResponse404
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
        )
    ).parsed
