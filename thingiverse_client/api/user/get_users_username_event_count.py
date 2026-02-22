from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_users_username_event_count_response_200 import (
    GetUsersUsernameEventCountResponse200,
)
from ...models.get_users_username_event_count_response_401 import (
    GetUsersUsernameEventCountResponse401,
)
from ...models.get_users_username_event_count_response_403 import (
    GetUsersUsernameEventCountResponse403,
)
from ...models.get_users_username_event_count_response_404 import (
    GetUsersUsernameEventCountResponse404,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    username: str,
    *,
    timestamp: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["timestamp"] = timestamp

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/{username}/event-count".format(
            username=quote(str(username), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetUsersUsernameEventCountResponse200
    | GetUsersUsernameEventCountResponse401
    | GetUsersUsernameEventCountResponse403
    | GetUsersUsernameEventCountResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetUsersUsernameEventCountResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetUsersUsernameEventCountResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetUsersUsernameEventCountResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetUsersUsernameEventCountResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetUsersUsernameEventCountResponse200
    | GetUsersUsernameEventCountResponse401
    | GetUsersUsernameEventCountResponse403
    | GetUsersUsernameEventCountResponse404
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
    timestamp: str | Unset = UNSET,
) -> Response[
    GetUsersUsernameEventCountResponse200
    | GetUsersUsernameEventCountResponse401
    | GetUsersUsernameEventCountResponse403
    | GetUsersUsernameEventCountResponse404
]:
    """Get the count of events for user since the timestamp sent

    Args:
        username (str):  Example: thingiverse.
        timestamp (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersUsernameEventCountResponse200 | GetUsersUsernameEventCountResponse401 | GetUsersUsernameEventCountResponse403 | GetUsersUsernameEventCountResponse404]
    """

    kwargs = _get_kwargs(
        username=username,
        timestamp=timestamp,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: AuthenticatedClient,
    timestamp: str | Unset = UNSET,
) -> (
    GetUsersUsernameEventCountResponse200
    | GetUsersUsernameEventCountResponse401
    | GetUsersUsernameEventCountResponse403
    | GetUsersUsernameEventCountResponse404
    | None
):
    """Get the count of events for user since the timestamp sent

    Args:
        username (str):  Example: thingiverse.
        timestamp (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersUsernameEventCountResponse200 | GetUsersUsernameEventCountResponse401 | GetUsersUsernameEventCountResponse403 | GetUsersUsernameEventCountResponse404
    """

    return sync_detailed(
        username=username,
        client=client,
        timestamp=timestamp,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    timestamp: str | Unset = UNSET,
) -> Response[
    GetUsersUsernameEventCountResponse200
    | GetUsersUsernameEventCountResponse401
    | GetUsersUsernameEventCountResponse403
    | GetUsersUsernameEventCountResponse404
]:
    """Get the count of events for user since the timestamp sent

    Args:
        username (str):  Example: thingiverse.
        timestamp (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersUsernameEventCountResponse200 | GetUsersUsernameEventCountResponse401 | GetUsersUsernameEventCountResponse403 | GetUsersUsernameEventCountResponse404]
    """

    kwargs = _get_kwargs(
        username=username,
        timestamp=timestamp,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient,
    timestamp: str | Unset = UNSET,
) -> (
    GetUsersUsernameEventCountResponse200
    | GetUsersUsernameEventCountResponse401
    | GetUsersUsernameEventCountResponse403
    | GetUsersUsernameEventCountResponse404
    | None
):
    """Get the count of events for user since the timestamp sent

    Args:
        username (str):  Example: thingiverse.
        timestamp (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersUsernameEventCountResponse200 | GetUsersUsernameEventCountResponse401 | GetUsersUsernameEventCountResponse403 | GetUsersUsernameEventCountResponse404
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            timestamp=timestamp,
        )
    ).parsed
