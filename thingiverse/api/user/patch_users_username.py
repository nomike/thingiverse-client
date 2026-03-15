from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_users_username_body import PatchUsersUsernameBody
from ...models.patch_users_username_response_401 import PatchUsersUsernameResponse401
from ...models.patch_users_username_response_403 import PatchUsersUsernameResponse403
from ...models.patch_users_username_response_404 import PatchUsersUsernameResponse404
from ...models.user_schema import UserSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    username: str,
    *,
    body: PatchUsersUsernameBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/users/{username}".format(
            username=quote(str(username), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchUsersUsernameResponse401
    | PatchUsersUsernameResponse403
    | PatchUsersUsernameResponse404
    | UserSchema
    | None
):
    if response.status_code == 200:
        response_200 = UserSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PatchUsersUsernameResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchUsersUsernameResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchUsersUsernameResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchUsersUsernameResponse401
    | PatchUsersUsernameResponse403
    | PatchUsersUsernameResponse404
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
    body: PatchUsersUsernameBody | Unset = UNSET,
) -> Response[
    PatchUsersUsernameResponse401
    | PatchUsersUsernameResponse403
    | PatchUsersUsernameResponse404
    | UserSchema
]:
    """Update the user's profile

    Args:
        username (str):  Example: thingiverse.
        body (PatchUsersUsernameBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchUsersUsernameResponse401 | PatchUsersUsernameResponse403 | PatchUsersUsernameResponse404 | UserSchema]
    """

    kwargs = _get_kwargs(
        username=username,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: AuthenticatedClient,
    body: PatchUsersUsernameBody | Unset = UNSET,
) -> (
    PatchUsersUsernameResponse401
    | PatchUsersUsernameResponse403
    | PatchUsersUsernameResponse404
    | UserSchema
    | None
):
    """Update the user's profile

    Args:
        username (str):  Example: thingiverse.
        body (PatchUsersUsernameBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchUsersUsernameResponse401 | PatchUsersUsernameResponse403 | PatchUsersUsernameResponse404 | UserSchema
    """

    return sync_detailed(
        username=username,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    body: PatchUsersUsernameBody | Unset = UNSET,
) -> Response[
    PatchUsersUsernameResponse401
    | PatchUsersUsernameResponse403
    | PatchUsersUsernameResponse404
    | UserSchema
]:
    """Update the user's profile

    Args:
        username (str):  Example: thingiverse.
        body (PatchUsersUsernameBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchUsersUsernameResponse401 | PatchUsersUsernameResponse403 | PatchUsersUsernameResponse404 | UserSchema]
    """

    kwargs = _get_kwargs(
        username=username,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient,
    body: PatchUsersUsernameBody | Unset = UNSET,
) -> (
    PatchUsersUsernameResponse401
    | PatchUsersUsernameResponse403
    | PatchUsersUsernameResponse404
    | UserSchema
    | None
):
    """Update the user's profile

    Args:
        username (str):  Example: thingiverse.
        body (PatchUsersUsernameBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchUsersUsernameResponse401 | PatchUsersUsernameResponse403 | PatchUsersUsernameResponse404 | UserSchema
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            body=body,
        )
    ).parsed
