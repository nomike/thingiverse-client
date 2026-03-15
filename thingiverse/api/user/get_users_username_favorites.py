from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_users_username_favorites_response_200_item import (
    GetUsersUsernameFavoritesResponse200Item,
)
from ...models.get_users_username_favorites_response_401 import GetUsersUsernameFavoritesResponse401
from ...models.get_users_username_favorites_response_403 import GetUsersUsernameFavoritesResponse403
from ...models.get_users_username_favorites_response_404 import GetUsersUsernameFavoritesResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    username: str,
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/{username}/favorites".format(
            username=quote(str(username), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetUsersUsernameFavoritesResponse401
    | GetUsersUsernameFavoritesResponse403
    | GetUsersUsernameFavoritesResponse404
    | list[GetUsersUsernameFavoritesResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetUsersUsernameFavoritesResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetUsersUsernameFavoritesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetUsersUsernameFavoritesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetUsersUsernameFavoritesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetUsersUsernameFavoritesResponse401
    | GetUsersUsernameFavoritesResponse403
    | GetUsersUsernameFavoritesResponse404
    | list[GetUsersUsernameFavoritesResponse200Item]
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
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[
    GetUsersUsernameFavoritesResponse401
    | GetUsersUsernameFavoritesResponse403
    | GetUsersUsernameFavoritesResponse404
    | list[GetUsersUsernameFavoritesResponse200Item]
]:
    """Get favorites by user

     If an authenticated user is requesting their own list of favorites, If the user doesn't exist,
    result is 404 Not Found

    Args:
        username (str):  Example: thingiverse.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersUsernameFavoritesResponse401 | GetUsersUsernameFavoritesResponse403 | GetUsersUsernameFavoritesResponse404 | list[GetUsersUsernameFavoritesResponse200Item]]
    """

    kwargs = _get_kwargs(
        username=username,
        page=page,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> (
    GetUsersUsernameFavoritesResponse401
    | GetUsersUsernameFavoritesResponse403
    | GetUsersUsernameFavoritesResponse404
    | list[GetUsersUsernameFavoritesResponse200Item]
    | None
):
    """Get favorites by user

     If an authenticated user is requesting their own list of favorites, If the user doesn't exist,
    result is 404 Not Found

    Args:
        username (str):  Example: thingiverse.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersUsernameFavoritesResponse401 | GetUsersUsernameFavoritesResponse403 | GetUsersUsernameFavoritesResponse404 | list[GetUsersUsernameFavoritesResponse200Item]
    """

    return sync_detailed(
        username=username,
        client=client,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[
    GetUsersUsernameFavoritesResponse401
    | GetUsersUsernameFavoritesResponse403
    | GetUsersUsernameFavoritesResponse404
    | list[GetUsersUsernameFavoritesResponse200Item]
]:
    """Get favorites by user

     If an authenticated user is requesting their own list of favorites, If the user doesn't exist,
    result is 404 Not Found

    Args:
        username (str):  Example: thingiverse.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersUsernameFavoritesResponse401 | GetUsersUsernameFavoritesResponse403 | GetUsersUsernameFavoritesResponse404 | list[GetUsersUsernameFavoritesResponse200Item]]
    """

    kwargs = _get_kwargs(
        username=username,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> (
    GetUsersUsernameFavoritesResponse401
    | GetUsersUsernameFavoritesResponse403
    | GetUsersUsernameFavoritesResponse404
    | list[GetUsersUsernameFavoritesResponse200Item]
    | None
):
    """Get favorites by user

     If an authenticated user is requesting their own list of favorites, If the user doesn't exist,
    result is 404 Not Found

    Args:
        username (str):  Example: thingiverse.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersUsernameFavoritesResponse401 | GetUsersUsernameFavoritesResponse403 | GetUsersUsernameFavoritesResponse404 | list[GetUsersUsernameFavoritesResponse200Item]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            page=page,
            per_page=per_page,
        )
    ).parsed
