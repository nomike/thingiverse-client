from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_users_username_followers_response_200 import (
    PostUsersUsernameFollowersResponse200,
)
from ...models.post_users_username_followers_response_401 import (
    PostUsersUsernameFollowersResponse401,
)
from ...models.post_users_username_followers_response_403 import (
    PostUsersUsernameFollowersResponse403,
)
from ...models.post_users_username_followers_response_404 import (
    PostUsersUsernameFollowersResponse404,
)
from ...types import Response


def _get_kwargs(
    username: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users/{username}/followers".format(
            username=quote(str(username), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostUsersUsernameFollowersResponse200
    | PostUsersUsernameFollowersResponse401
    | PostUsersUsernameFollowersResponse403
    | PostUsersUsernameFollowersResponse404
    | None
):
    if response.status_code == 200:
        response_200 = PostUsersUsernameFollowersResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostUsersUsernameFollowersResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostUsersUsernameFollowersResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostUsersUsernameFollowersResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostUsersUsernameFollowersResponse200
    | PostUsersUsernameFollowersResponse401
    | PostUsersUsernameFollowersResponse403
    | PostUsersUsernameFollowersResponse404
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
    PostUsersUsernameFollowersResponse200
    | PostUsersUsernameFollowersResponse401
    | PostUsersUsernameFollowersResponse403
    | PostUsersUsernameFollowersResponse404
]:
    """Follow an user

     Must use the POST method Result will be 404 Not Found if the user doesn't exist. Result will be 400
    Bad Request if the user is trying to follow itself.

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostUsersUsernameFollowersResponse200 | PostUsersUsernameFollowersResponse401 | PostUsersUsernameFollowersResponse403 | PostUsersUsernameFollowersResponse404]
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
    PostUsersUsernameFollowersResponse200
    | PostUsersUsernameFollowersResponse401
    | PostUsersUsernameFollowersResponse403
    | PostUsersUsernameFollowersResponse404
    | None
):
    """Follow an user

     Must use the POST method Result will be 404 Not Found if the user doesn't exist. Result will be 400
    Bad Request if the user is trying to follow itself.

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostUsersUsernameFollowersResponse200 | PostUsersUsernameFollowersResponse401 | PostUsersUsernameFollowersResponse403 | PostUsersUsernameFollowersResponse404
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
    PostUsersUsernameFollowersResponse200
    | PostUsersUsernameFollowersResponse401
    | PostUsersUsernameFollowersResponse403
    | PostUsersUsernameFollowersResponse404
]:
    """Follow an user

     Must use the POST method Result will be 404 Not Found if the user doesn't exist. Result will be 400
    Bad Request if the user is trying to follow itself.

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostUsersUsernameFollowersResponse200 | PostUsersUsernameFollowersResponse401 | PostUsersUsernameFollowersResponse403 | PostUsersUsernameFollowersResponse404]
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
    PostUsersUsernameFollowersResponse200
    | PostUsersUsernameFollowersResponse401
    | PostUsersUsernameFollowersResponse403
    | PostUsersUsernameFollowersResponse404
    | None
):
    """Follow an user

     Must use the POST method Result will be 404 Not Found if the user doesn't exist. Result will be 400
    Bad Request if the user is trying to follow itself.

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostUsersUsernameFollowersResponse200 | PostUsersUsernameFollowersResponse401 | PostUsersUsernameFollowersResponse403 | PostUsersUsernameFollowersResponse404
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
        )
    ).parsed
