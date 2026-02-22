from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.comment_schema import CommentSchema
from ...models.get_comments_comment_id_replies_response_401 import (
    GetCommentsCommentIdRepliesResponse401,
)
from ...models.get_comments_comment_id_replies_response_403 import (
    GetCommentsCommentIdRepliesResponse403,
)
from ...models.get_comments_comment_id_replies_response_404 import (
    GetCommentsCommentIdRepliesResponse404,
)
from ...types import Response


def _get_kwargs(
    comment_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/comments/{comment_id}/replies".format(
            comment_id=quote(str(comment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetCommentsCommentIdRepliesResponse401
    | GetCommentsCommentIdRepliesResponse403
    | GetCommentsCommentIdRepliesResponse404
    | list[CommentSchema]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CommentSchema.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetCommentsCommentIdRepliesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetCommentsCommentIdRepliesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetCommentsCommentIdRepliesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetCommentsCommentIdRepliesResponse401
    | GetCommentsCommentIdRepliesResponse403
    | GetCommentsCommentIdRepliesResponse404
    | list[CommentSchema]
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
) -> Response[
    GetCommentsCommentIdRepliesResponse401
    | GetCommentsCommentIdRepliesResponse403
    | GetCommentsCommentIdRepliesResponse404
    | list[CommentSchema]
]:
    """Get replies of a certain comment

    Args:
        comment_id (int):  Example: 285620.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCommentsCommentIdRepliesResponse401 | GetCommentsCommentIdRepliesResponse403 | GetCommentsCommentIdRepliesResponse404 | list[CommentSchema]]
    """

    kwargs = _get_kwargs(
        comment_id=comment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    comment_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    GetCommentsCommentIdRepliesResponse401
    | GetCommentsCommentIdRepliesResponse403
    | GetCommentsCommentIdRepliesResponse404
    | list[CommentSchema]
    | None
):
    """Get replies of a certain comment

    Args:
        comment_id (int):  Example: 285620.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCommentsCommentIdRepliesResponse401 | GetCommentsCommentIdRepliesResponse403 | GetCommentsCommentIdRepliesResponse404 | list[CommentSchema]
    """

    return sync_detailed(
        comment_id=comment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    comment_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetCommentsCommentIdRepliesResponse401
    | GetCommentsCommentIdRepliesResponse403
    | GetCommentsCommentIdRepliesResponse404
    | list[CommentSchema]
]:
    """Get replies of a certain comment

    Args:
        comment_id (int):  Example: 285620.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCommentsCommentIdRepliesResponse401 | GetCommentsCommentIdRepliesResponse403 | GetCommentsCommentIdRepliesResponse404 | list[CommentSchema]]
    """

    kwargs = _get_kwargs(
        comment_id=comment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    comment_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    GetCommentsCommentIdRepliesResponse401
    | GetCommentsCommentIdRepliesResponse403
    | GetCommentsCommentIdRepliesResponse404
    | list[CommentSchema]
    | None
):
    """Get replies of a certain comment

    Args:
        comment_id (int):  Example: 285620.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCommentsCommentIdRepliesResponse401 | GetCommentsCommentIdRepliesResponse403 | GetCommentsCommentIdRepliesResponse404 | list[CommentSchema]
    """

    return (
        await asyncio_detailed(
            comment_id=comment_id,
            client=client,
        )
    ).parsed
