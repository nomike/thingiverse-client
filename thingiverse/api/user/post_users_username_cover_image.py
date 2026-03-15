from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_users_username_cover_image_body import PostUsersUsernameCoverImageBody
from ...models.post_users_username_cover_image_response_200 import (
    PostUsersUsernameCoverImageResponse200,
)
from ...models.post_users_username_cover_image_response_401 import (
    PostUsersUsernameCoverImageResponse401,
)
from ...models.post_users_username_cover_image_response_403 import (
    PostUsersUsernameCoverImageResponse403,
)
from ...models.post_users_username_cover_image_response_404 import (
    PostUsersUsernameCoverImageResponse404,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    username: str,
    *,
    body: PostUsersUsernameCoverImageBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users/{username}/cover-image".format(
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
    PostUsersUsernameCoverImageResponse200
    | PostUsersUsernameCoverImageResponse401
    | PostUsersUsernameCoverImageResponse403
    | PostUsersUsernameCoverImageResponse404
    | None
):
    if response.status_code == 200:
        response_200 = PostUsersUsernameCoverImageResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostUsersUsernameCoverImageResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostUsersUsernameCoverImageResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostUsersUsernameCoverImageResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostUsersUsernameCoverImageResponse200
    | PostUsersUsernameCoverImageResponse401
    | PostUsersUsernameCoverImageResponse403
    | PostUsersUsernameCoverImageResponse404
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
    body: PostUsersUsernameCoverImageBody | Unset = UNSET,
) -> Response[
    PostUsersUsernameCoverImageResponse200
    | PostUsersUsernameCoverImageResponse401
    | PostUsersUsernameCoverImageResponse403
    | PostUsersUsernameCoverImageResponse404
]:
    """Update the cover image

     Must use the POST method

    Args:
        username (str):  Example: thingiverse.
        body (PostUsersUsernameCoverImageBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostUsersUsernameCoverImageResponse200 | PostUsersUsernameCoverImageResponse401 | PostUsersUsernameCoverImageResponse403 | PostUsersUsernameCoverImageResponse404]
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
    body: PostUsersUsernameCoverImageBody | Unset = UNSET,
) -> (
    PostUsersUsernameCoverImageResponse200
    | PostUsersUsernameCoverImageResponse401
    | PostUsersUsernameCoverImageResponse403
    | PostUsersUsernameCoverImageResponse404
    | None
):
    """Update the cover image

     Must use the POST method

    Args:
        username (str):  Example: thingiverse.
        body (PostUsersUsernameCoverImageBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostUsersUsernameCoverImageResponse200 | PostUsersUsernameCoverImageResponse401 | PostUsersUsernameCoverImageResponse403 | PostUsersUsernameCoverImageResponse404
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
    body: PostUsersUsernameCoverImageBody | Unset = UNSET,
) -> Response[
    PostUsersUsernameCoverImageResponse200
    | PostUsersUsernameCoverImageResponse401
    | PostUsersUsernameCoverImageResponse403
    | PostUsersUsernameCoverImageResponse404
]:
    """Update the cover image

     Must use the POST method

    Args:
        username (str):  Example: thingiverse.
        body (PostUsersUsernameCoverImageBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostUsersUsernameCoverImageResponse200 | PostUsersUsernameCoverImageResponse401 | PostUsersUsernameCoverImageResponse403 | PostUsersUsernameCoverImageResponse404]
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
    body: PostUsersUsernameCoverImageBody | Unset = UNSET,
) -> (
    PostUsersUsernameCoverImageResponse200
    | PostUsersUsernameCoverImageResponse401
    | PostUsersUsernameCoverImageResponse403
    | PostUsersUsernameCoverImageResponse404
    | None
):
    """Update the cover image

     Must use the POST method

    Args:
        username (str):  Example: thingiverse.
        body (PostUsersUsernameCoverImageBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostUsersUsernameCoverImageResponse200 | PostUsersUsernameCoverImageResponse401 | PostUsersUsernameCoverImageResponse403 | PostUsersUsernameCoverImageResponse404
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            body=body,
        )
    ).parsed
