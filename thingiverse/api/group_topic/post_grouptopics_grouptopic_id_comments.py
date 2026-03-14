from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.comment_schema import CommentSchema
from ...models.post_grouptopics_grouptopic_id_comments_body import (
    PostGrouptopicsGrouptopicIdCommentsBody,
)
from ...models.post_grouptopics_grouptopic_id_comments_response_401 import (
    PostGrouptopicsGrouptopicIdCommentsResponse401,
)
from ...models.post_grouptopics_grouptopic_id_comments_response_403 import (
    PostGrouptopicsGrouptopicIdCommentsResponse403,
)
from ...models.post_grouptopics_grouptopic_id_comments_response_404 import (
    PostGrouptopicsGrouptopicIdCommentsResponse404,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    grouptopic_id: int,
    *,
    body: PostGrouptopicsGrouptopicIdCommentsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/grouptopics/{grouptopic_id}/comments".format(
            grouptopic_id=quote(str(grouptopic_id), safe=""),
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
    | PostGrouptopicsGrouptopicIdCommentsResponse401
    | PostGrouptopicsGrouptopicIdCommentsResponse403
    | PostGrouptopicsGrouptopicIdCommentsResponse404
    | None
):
    if response.status_code == 200:
        response_200 = CommentSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostGrouptopicsGrouptopicIdCommentsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostGrouptopicsGrouptopicIdCommentsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostGrouptopicsGrouptopicIdCommentsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CommentSchema
    | PostGrouptopicsGrouptopicIdCommentsResponse401
    | PostGrouptopicsGrouptopicIdCommentsResponse403
    | PostGrouptopicsGrouptopicIdCommentsResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    grouptopic_id: int,
    *,
    client: AuthenticatedClient,
    body: PostGrouptopicsGrouptopicIdCommentsBody | Unset = UNSET,
) -> Response[
    CommentSchema
    | PostGrouptopicsGrouptopicIdCommentsResponse401
    | PostGrouptopicsGrouptopicIdCommentsResponse403
    | PostGrouptopicsGrouptopicIdCommentsResponse404
]:
    """Post a comment

    Args:
        grouptopic_id (int):  Example: 2.
        body (PostGrouptopicsGrouptopicIdCommentsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommentSchema | PostGrouptopicsGrouptopicIdCommentsResponse401 | PostGrouptopicsGrouptopicIdCommentsResponse403 | PostGrouptopicsGrouptopicIdCommentsResponse404]
    """

    kwargs = _get_kwargs(
        grouptopic_id=grouptopic_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    grouptopic_id: int,
    *,
    client: AuthenticatedClient,
    body: PostGrouptopicsGrouptopicIdCommentsBody | Unset = UNSET,
) -> (
    CommentSchema
    | PostGrouptopicsGrouptopicIdCommentsResponse401
    | PostGrouptopicsGrouptopicIdCommentsResponse403
    | PostGrouptopicsGrouptopicIdCommentsResponse404
    | None
):
    """Post a comment

    Args:
        grouptopic_id (int):  Example: 2.
        body (PostGrouptopicsGrouptopicIdCommentsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommentSchema | PostGrouptopicsGrouptopicIdCommentsResponse401 | PostGrouptopicsGrouptopicIdCommentsResponse403 | PostGrouptopicsGrouptopicIdCommentsResponse404
    """

    return sync_detailed(
        grouptopic_id=grouptopic_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    grouptopic_id: int,
    *,
    client: AuthenticatedClient,
    body: PostGrouptopicsGrouptopicIdCommentsBody | Unset = UNSET,
) -> Response[
    CommentSchema
    | PostGrouptopicsGrouptopicIdCommentsResponse401
    | PostGrouptopicsGrouptopicIdCommentsResponse403
    | PostGrouptopicsGrouptopicIdCommentsResponse404
]:
    """Post a comment

    Args:
        grouptopic_id (int):  Example: 2.
        body (PostGrouptopicsGrouptopicIdCommentsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommentSchema | PostGrouptopicsGrouptopicIdCommentsResponse401 | PostGrouptopicsGrouptopicIdCommentsResponse403 | PostGrouptopicsGrouptopicIdCommentsResponse404]
    """

    kwargs = _get_kwargs(
        grouptopic_id=grouptopic_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    grouptopic_id: int,
    *,
    client: AuthenticatedClient,
    body: PostGrouptopicsGrouptopicIdCommentsBody | Unset = UNSET,
) -> (
    CommentSchema
    | PostGrouptopicsGrouptopicIdCommentsResponse401
    | PostGrouptopicsGrouptopicIdCommentsResponse403
    | PostGrouptopicsGrouptopicIdCommentsResponse404
    | None
):
    """Post a comment

    Args:
        grouptopic_id (int):  Example: 2.
        body (PostGrouptopicsGrouptopicIdCommentsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommentSchema | PostGrouptopicsGrouptopicIdCommentsResponse401 | PostGrouptopicsGrouptopicIdCommentsResponse403 | PostGrouptopicsGrouptopicIdCommentsResponse404
    """

    return (
        await asyncio_detailed(
            grouptopic_id=grouptopic_id,
            client=client,
            body=body,
        )
    ).parsed
