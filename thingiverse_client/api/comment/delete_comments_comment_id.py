from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_comments_comment_id_response_200 import DeleteCommentsCommentIdResponse200
from ...models.delete_comments_comment_id_response_401 import DeleteCommentsCommentIdResponse401
from ...models.delete_comments_comment_id_response_403 import DeleteCommentsCommentIdResponse403
from ...models.delete_comments_comment_id_response_404 import DeleteCommentsCommentIdResponse404
from ...types import Response


def _get_kwargs(
    comment_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/comments/{comment_id}/".format(
            comment_id=quote(str(comment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteCommentsCommentIdResponse200
    | DeleteCommentsCommentIdResponse401
    | DeleteCommentsCommentIdResponse403
    | DeleteCommentsCommentIdResponse404
    | None
):
    if response.status_code == 200:
        response_200 = DeleteCommentsCommentIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = DeleteCommentsCommentIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteCommentsCommentIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteCommentsCommentIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteCommentsCommentIdResponse200
    | DeleteCommentsCommentIdResponse401
    | DeleteCommentsCommentIdResponse403
    | DeleteCommentsCommentIdResponse404
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
    DeleteCommentsCommentIdResponse200
    | DeleteCommentsCommentIdResponse401
    | DeleteCommentsCommentIdResponse403
    | DeleteCommentsCommentIdResponse404
]:
    """Softdelete a comment

    Args:
        comment_id (int):  Example: 285620.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteCommentsCommentIdResponse200 | DeleteCommentsCommentIdResponse401 | DeleteCommentsCommentIdResponse403 | DeleteCommentsCommentIdResponse404]
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
    DeleteCommentsCommentIdResponse200
    | DeleteCommentsCommentIdResponse401
    | DeleteCommentsCommentIdResponse403
    | DeleteCommentsCommentIdResponse404
    | None
):
    """Softdelete a comment

    Args:
        comment_id (int):  Example: 285620.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteCommentsCommentIdResponse200 | DeleteCommentsCommentIdResponse401 | DeleteCommentsCommentIdResponse403 | DeleteCommentsCommentIdResponse404
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
    DeleteCommentsCommentIdResponse200
    | DeleteCommentsCommentIdResponse401
    | DeleteCommentsCommentIdResponse403
    | DeleteCommentsCommentIdResponse404
]:
    """Softdelete a comment

    Args:
        comment_id (int):  Example: 285620.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteCommentsCommentIdResponse200 | DeleteCommentsCommentIdResponse401 | DeleteCommentsCommentIdResponse403 | DeleteCommentsCommentIdResponse404]
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
    DeleteCommentsCommentIdResponse200
    | DeleteCommentsCommentIdResponse401
    | DeleteCommentsCommentIdResponse403
    | DeleteCommentsCommentIdResponse404
    | None
):
    """Softdelete a comment

    Args:
        comment_id (int):  Example: 285620.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteCommentsCommentIdResponse200 | DeleteCommentsCommentIdResponse401 | DeleteCommentsCommentIdResponse403 | DeleteCommentsCommentIdResponse404
    """

    return (
        await asyncio_detailed(
            comment_id=comment_id,
            client=client,
        )
    ).parsed
