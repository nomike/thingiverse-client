from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_users_username_likesids_response_401 import GetUsersUsernameLikesidsResponse401
from ...models.get_users_username_likesids_response_403 import GetUsersUsernameLikesidsResponse403
from ...models.get_users_username_likesids_response_404 import GetUsersUsernameLikesidsResponse404
from ...types import Response


def _get_kwargs(
    username: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/{username}/likesids".format(
            username=quote(str(username), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetUsersUsernameLikesidsResponse401
    | GetUsersUsernameLikesidsResponse403
    | GetUsersUsernameLikesidsResponse404
    | list[int]
    | None
):
    if response.status_code == 200:
        response_200 = cast(list[int], response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetUsersUsernameLikesidsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetUsersUsernameLikesidsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetUsersUsernameLikesidsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetUsersUsernameLikesidsResponse401
    | GetUsersUsernameLikesidsResponse403
    | GetUsersUsernameLikesidsResponse404
    | list[int]
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
    GetUsersUsernameLikesidsResponse401
    | GetUsersUsernameLikesidsResponse403
    | GetUsersUsernameLikesidsResponse404
    | list[int]
]:
    """Get all things id's like by user

     If the user doesn't exist, result is 404 Not Found

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersUsernameLikesidsResponse401 | GetUsersUsernameLikesidsResponse403 | GetUsersUsernameLikesidsResponse404 | list[int]]
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
    GetUsersUsernameLikesidsResponse401
    | GetUsersUsernameLikesidsResponse403
    | GetUsersUsernameLikesidsResponse404
    | list[int]
    | None
):
    """Get all things id's like by user

     If the user doesn't exist, result is 404 Not Found

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersUsernameLikesidsResponse401 | GetUsersUsernameLikesidsResponse403 | GetUsersUsernameLikesidsResponse404 | list[int]
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
    GetUsersUsernameLikesidsResponse401
    | GetUsersUsernameLikesidsResponse403
    | GetUsersUsernameLikesidsResponse404
    | list[int]
]:
    """Get all things id's like by user

     If the user doesn't exist, result is 404 Not Found

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersUsernameLikesidsResponse401 | GetUsersUsernameLikesidsResponse403 | GetUsersUsernameLikesidsResponse404 | list[int]]
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
    GetUsersUsernameLikesidsResponse401
    | GetUsersUsernameLikesidsResponse403
    | GetUsersUsernameLikesidsResponse404
    | list[int]
    | None
):
    """Get all things id's like by user

     If the user doesn't exist, result is 404 Not Found

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersUsernameLikesidsResponse401 | GetUsersUsernameLikesidsResponse403 | GetUsersUsernameLikesidsResponse404 | list[int]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
        )
    ).parsed
