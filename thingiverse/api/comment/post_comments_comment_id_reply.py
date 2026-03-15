from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.comment_schema import CommentSchema
from ...models.post_comments_comment_id_reply_body import PostCommentsCommentIdReplyBody
from ...models.post_comments_comment_id_reply_response_400 import (
    PostCommentsCommentIdReplyResponse400,
)
from ...models.post_comments_comment_id_reply_response_401 import (
    PostCommentsCommentIdReplyResponse401,
)
from ...models.post_comments_comment_id_reply_response_403 import (
    PostCommentsCommentIdReplyResponse403,
)
from ...models.post_comments_comment_id_reply_response_404 import (
    PostCommentsCommentIdReplyResponse404,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    comment_id: int,
    *,
    body: PostCommentsCommentIdReplyBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/comments/{comment_id}/reply".format(
            comment_id=quote(str(comment_id), safe=""),
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
    CommentSchema
    | PostCommentsCommentIdReplyResponse400
    | PostCommentsCommentIdReplyResponse401
    | PostCommentsCommentIdReplyResponse403
    | PostCommentsCommentIdReplyResponse404
    | None
):
    if response.status_code == 200:
        response_200 = CommentSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostCommentsCommentIdReplyResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostCommentsCommentIdReplyResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostCommentsCommentIdReplyResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostCommentsCommentIdReplyResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CommentSchema
    | PostCommentsCommentIdReplyResponse400
    | PostCommentsCommentIdReplyResponse401
    | PostCommentsCommentIdReplyResponse403
    | PostCommentsCommentIdReplyResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: PostCommentsCommentIdReplyBody | Unset = UNSET,
) -> Response[
    CommentSchema
    | PostCommentsCommentIdReplyResponse400
    | PostCommentsCommentIdReplyResponse401
    | PostCommentsCommentIdReplyResponse403
    | PostCommentsCommentIdReplyResponse404
]:
    """Reply to a comment

    Args:
        comment_id (int):  Example: 285620.
        body (PostCommentsCommentIdReplyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommentSchema | PostCommentsCommentIdReplyResponse400 | PostCommentsCommentIdReplyResponse401 | PostCommentsCommentIdReplyResponse403 | PostCommentsCommentIdReplyResponse404]
    """

    kwargs = _get_kwargs(
        comment_id=comment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: PostCommentsCommentIdReplyBody | Unset = UNSET,
) -> (
    CommentSchema
    | PostCommentsCommentIdReplyResponse400
    | PostCommentsCommentIdReplyResponse401
    | PostCommentsCommentIdReplyResponse403
    | PostCommentsCommentIdReplyResponse404
    | None
):
    """Reply to a comment

    Args:
        comment_id (int):  Example: 285620.
        body (PostCommentsCommentIdReplyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommentSchema | PostCommentsCommentIdReplyResponse400 | PostCommentsCommentIdReplyResponse401 | PostCommentsCommentIdReplyResponse403 | PostCommentsCommentIdReplyResponse404
    """

    return sync_detailed(
        comment_id=comment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: PostCommentsCommentIdReplyBody | Unset = UNSET,
) -> Response[
    CommentSchema
    | PostCommentsCommentIdReplyResponse400
    | PostCommentsCommentIdReplyResponse401
    | PostCommentsCommentIdReplyResponse403
    | PostCommentsCommentIdReplyResponse404
]:
    """Reply to a comment

    Args:
        comment_id (int):  Example: 285620.
        body (PostCommentsCommentIdReplyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommentSchema | PostCommentsCommentIdReplyResponse400 | PostCommentsCommentIdReplyResponse401 | PostCommentsCommentIdReplyResponse403 | PostCommentsCommentIdReplyResponse404]
    """

    kwargs = _get_kwargs(
        comment_id=comment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: PostCommentsCommentIdReplyBody | Unset = UNSET,
) -> (
    CommentSchema
    | PostCommentsCommentIdReplyResponse400
    | PostCommentsCommentIdReplyResponse401
    | PostCommentsCommentIdReplyResponse403
    | PostCommentsCommentIdReplyResponse404
    | None
):
    """Reply to a comment

    Args:
        comment_id (int):  Example: 285620.
        body (PostCommentsCommentIdReplyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommentSchema | PostCommentsCommentIdReplyResponse400 | PostCommentsCommentIdReplyResponse401 | PostCommentsCommentIdReplyResponse403 | PostCommentsCommentIdReplyResponse404
    """

    return (
        await asyncio_detailed(
            comment_id=comment_id,
            client=client,
            body=body,
        )
    ).parsed
