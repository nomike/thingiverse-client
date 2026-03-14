from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_users_username_search_term_response_200 import (
    GetUsersUsernameSearchTermResponse200,
)
from ...models.get_users_username_search_term_response_401 import (
    GetUsersUsernameSearchTermResponse401,
)
from ...models.get_users_username_search_term_response_403 import (
    GetUsersUsernameSearchTermResponse403,
)
from ...models.get_users_username_search_term_response_404 import (
    GetUsersUsernameSearchTermResponse404,
)
from ...types import Response


def _get_kwargs(
    username: str,
    term: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/{username}/search/{term}".format(
            username=quote(str(username), safe=""),
            term=quote(str(term), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetUsersUsernameSearchTermResponse200
    | GetUsersUsernameSearchTermResponse401
    | GetUsersUsernameSearchTermResponse403
    | GetUsersUsernameSearchTermResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetUsersUsernameSearchTermResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetUsersUsernameSearchTermResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetUsersUsernameSearchTermResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetUsersUsernameSearchTermResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetUsersUsernameSearchTermResponse200
    | GetUsersUsernameSearchTermResponse401
    | GetUsersUsernameSearchTermResponse403
    | GetUsersUsernameSearchTermResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    term: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetUsersUsernameSearchTermResponse200
    | GetUsersUsernameSearchTermResponse401
    | GetUsersUsernameSearchTermResponse403
    | GetUsersUsernameSearchTermResponse404
]:
    """Search data by user

    Args:
        username (str):  Example: thingiverse.
        term (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersUsernameSearchTermResponse200 | GetUsersUsernameSearchTermResponse401 | GetUsersUsernameSearchTermResponse403 | GetUsersUsernameSearchTermResponse404]
    """

    kwargs = _get_kwargs(
        username=username,
        term=term,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    term: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetUsersUsernameSearchTermResponse200
    | GetUsersUsernameSearchTermResponse401
    | GetUsersUsernameSearchTermResponse403
    | GetUsersUsernameSearchTermResponse404
    | None
):
    """Search data by user

    Args:
        username (str):  Example: thingiverse.
        term (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersUsernameSearchTermResponse200 | GetUsersUsernameSearchTermResponse401 | GetUsersUsernameSearchTermResponse403 | GetUsersUsernameSearchTermResponse404
    """

    return sync_detailed(
        username=username,
        term=term,
        client=client,
    ).parsed


async def asyncio_detailed(
    username: str,
    term: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetUsersUsernameSearchTermResponse200
    | GetUsersUsernameSearchTermResponse401
    | GetUsersUsernameSearchTermResponse403
    | GetUsersUsernameSearchTermResponse404
]:
    """Search data by user

    Args:
        username (str):  Example: thingiverse.
        term (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersUsernameSearchTermResponse200 | GetUsersUsernameSearchTermResponse401 | GetUsersUsernameSearchTermResponse403 | GetUsersUsernameSearchTermResponse404]
    """

    kwargs = _get_kwargs(
        username=username,
        term=term,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    term: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetUsersUsernameSearchTermResponse200
    | GetUsersUsernameSearchTermResponse401
    | GetUsersUsernameSearchTermResponse403
    | GetUsersUsernameSearchTermResponse404
    | None
):
    """Search data by user

    Args:
        username (str):  Example: thingiverse.
        term (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersUsernameSearchTermResponse200 | GetUsersUsernameSearchTermResponse401 | GetUsersUsernameSearchTermResponse403 | GetUsersUsernameSearchTermResponse404
    """

    return (
        await asyncio_detailed(
            username=username,
            term=term,
            client=client,
        )
    ).parsed
