from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_copies_copy_id_likes_response_200 import PostCopiesCopyIdLikesResponse200
from ...models.post_copies_copy_id_likes_response_400 import PostCopiesCopyIdLikesResponse400
from ...models.post_copies_copy_id_likes_response_401 import PostCopiesCopyIdLikesResponse401
from ...models.post_copies_copy_id_likes_response_403 import PostCopiesCopyIdLikesResponse403
from ...models.post_copies_copy_id_likes_response_404 import PostCopiesCopyIdLikesResponse404
from ...types import Response


def _get_kwargs(
    copy_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/copies/{copy_id}/likes".format(
            copy_id=quote(str(copy_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostCopiesCopyIdLikesResponse200
    | PostCopiesCopyIdLikesResponse400
    | PostCopiesCopyIdLikesResponse401
    | PostCopiesCopyIdLikesResponse403
    | PostCopiesCopyIdLikesResponse404
    | None
):
    if response.status_code == 200:
        response_200 = PostCopiesCopyIdLikesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostCopiesCopyIdLikesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostCopiesCopyIdLikesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostCopiesCopyIdLikesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostCopiesCopyIdLikesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostCopiesCopyIdLikesResponse200
    | PostCopiesCopyIdLikesResponse400
    | PostCopiesCopyIdLikesResponse401
    | PostCopiesCopyIdLikesResponse403
    | PostCopiesCopyIdLikesResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    copy_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    PostCopiesCopyIdLikesResponse200
    | PostCopiesCopyIdLikesResponse400
    | PostCopiesCopyIdLikesResponse401
    | PostCopiesCopyIdLikesResponse403
    | PostCopiesCopyIdLikesResponse404
]:
    """Like a copy

     Must use the POST method Result will be 404 Not Found if the copy doesn't exist. Result will be 400
    Bad Request if the user is trying to like their own copy.

    Args:
        copy_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCopiesCopyIdLikesResponse200 | PostCopiesCopyIdLikesResponse400 | PostCopiesCopyIdLikesResponse401 | PostCopiesCopyIdLikesResponse403 | PostCopiesCopyIdLikesResponse404]
    """

    kwargs = _get_kwargs(
        copy_id=copy_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    copy_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    PostCopiesCopyIdLikesResponse200
    | PostCopiesCopyIdLikesResponse400
    | PostCopiesCopyIdLikesResponse401
    | PostCopiesCopyIdLikesResponse403
    | PostCopiesCopyIdLikesResponse404
    | None
):
    """Like a copy

     Must use the POST method Result will be 404 Not Found if the copy doesn't exist. Result will be 400
    Bad Request if the user is trying to like their own copy.

    Args:
        copy_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCopiesCopyIdLikesResponse200 | PostCopiesCopyIdLikesResponse400 | PostCopiesCopyIdLikesResponse401 | PostCopiesCopyIdLikesResponse403 | PostCopiesCopyIdLikesResponse404
    """

    return sync_detailed(
        copy_id=copy_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    copy_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    PostCopiesCopyIdLikesResponse200
    | PostCopiesCopyIdLikesResponse400
    | PostCopiesCopyIdLikesResponse401
    | PostCopiesCopyIdLikesResponse403
    | PostCopiesCopyIdLikesResponse404
]:
    """Like a copy

     Must use the POST method Result will be 404 Not Found if the copy doesn't exist. Result will be 400
    Bad Request if the user is trying to like their own copy.

    Args:
        copy_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCopiesCopyIdLikesResponse200 | PostCopiesCopyIdLikesResponse400 | PostCopiesCopyIdLikesResponse401 | PostCopiesCopyIdLikesResponse403 | PostCopiesCopyIdLikesResponse404]
    """

    kwargs = _get_kwargs(
        copy_id=copy_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    copy_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    PostCopiesCopyIdLikesResponse200
    | PostCopiesCopyIdLikesResponse400
    | PostCopiesCopyIdLikesResponse401
    | PostCopiesCopyIdLikesResponse403
    | PostCopiesCopyIdLikesResponse404
    | None
):
    """Like a copy

     Must use the POST method Result will be 404 Not Found if the copy doesn't exist. Result will be 400
    Bad Request if the user is trying to like their own copy.

    Args:
        copy_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCopiesCopyIdLikesResponse200 | PostCopiesCopyIdLikesResponse400 | PostCopiesCopyIdLikesResponse401 | PostCopiesCopyIdLikesResponse403 | PostCopiesCopyIdLikesResponse404
    """

    return (
        await asyncio_detailed(
            copy_id=copy_id,
            client=client,
        )
    ).parsed
