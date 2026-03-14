from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.comment_schema import CommentSchema
from ...models.post_comments_body import PostCommentsBody
from ...models.post_comments_response_400 import PostCommentsResponse400
from ...models.post_comments_response_401 import PostCommentsResponse401
from ...models.post_comments_response_403 import PostCommentsResponse403
from ...models.post_comments_response_404 import PostCommentsResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostCommentsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/comments/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CommentSchema
    | PostCommentsResponse400
    | PostCommentsResponse401
    | PostCommentsResponse403
    | PostCommentsResponse404
    | None
):
    if response.status_code == 200:
        response_200 = CommentSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostCommentsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostCommentsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostCommentsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostCommentsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CommentSchema
    | PostCommentsResponse400
    | PostCommentsResponse401
    | PostCommentsResponse403
    | PostCommentsResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostCommentsBody | Unset = UNSET,
) -> Response[
    CommentSchema
    | PostCommentsResponse400
    | PostCommentsResponse401
    | PostCommentsResponse403
    | PostCommentsResponse404
]:
    """Reply to a comment

    Args:
        body (PostCommentsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommentSchema | PostCommentsResponse400 | PostCommentsResponse401 | PostCommentsResponse403 | PostCommentsResponse404]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostCommentsBody | Unset = UNSET,
) -> (
    CommentSchema
    | PostCommentsResponse400
    | PostCommentsResponse401
    | PostCommentsResponse403
    | PostCommentsResponse404
    | None
):
    """Reply to a comment

    Args:
        body (PostCommentsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommentSchema | PostCommentsResponse400 | PostCommentsResponse401 | PostCommentsResponse403 | PostCommentsResponse404
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostCommentsBody | Unset = UNSET,
) -> Response[
    CommentSchema
    | PostCommentsResponse400
    | PostCommentsResponse401
    | PostCommentsResponse403
    | PostCommentsResponse404
]:
    """Reply to a comment

    Args:
        body (PostCommentsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommentSchema | PostCommentsResponse400 | PostCommentsResponse401 | PostCommentsResponse403 | PostCommentsResponse404]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostCommentsBody | Unset = UNSET,
) -> (
    CommentSchema
    | PostCommentsResponse400
    | PostCommentsResponse401
    | PostCommentsResponse403
    | PostCommentsResponse404
    | None
):
    """Reply to a comment

    Args:
        body (PostCommentsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommentSchema | PostCommentsResponse400 | PostCommentsResponse401 | PostCommentsResponse403 | PostCommentsResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
