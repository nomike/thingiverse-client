from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.forum_schema import ForumSchema
from ...models.post_groups_group_id_group_forums_body import PostGroupsGroupIdGroupForumsBody
from ...models.post_groups_group_id_group_forums_response_401 import (
    PostGroupsGroupIdGroupForumsResponse401,
)
from ...models.post_groups_group_id_group_forums_response_403 import (
    PostGroupsGroupIdGroupForumsResponse403,
)
from ...models.post_groups_group_id_group_forums_response_404 import (
    PostGroupsGroupIdGroupForumsResponse404,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    body: PostGroupsGroupIdGroupForumsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/groups/{group_id}/group-forums".format(
            group_id=quote(str(group_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ForumSchema
    | PostGroupsGroupIdGroupForumsResponse401
    | PostGroupsGroupIdGroupForumsResponse403
    | PostGroupsGroupIdGroupForumsResponse404
    | None
):
    if response.status_code == 200:
        response_200 = ForumSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostGroupsGroupIdGroupForumsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostGroupsGroupIdGroupForumsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostGroupsGroupIdGroupForumsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ForumSchema
    | PostGroupsGroupIdGroupForumsResponse401
    | PostGroupsGroupIdGroupForumsResponse403
    | PostGroupsGroupIdGroupForumsResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: PostGroupsGroupIdGroupForumsBody | Unset = UNSET,
) -> Response[
    ForumSchema
    | PostGroupsGroupIdGroupForumsResponse401
    | PostGroupsGroupIdGroupForumsResponse403
    | PostGroupsGroupIdGroupForumsResponse404
]:
    """Create a new forum

    Args:
        group_id (int):  Example: 25.
        body (PostGroupsGroupIdGroupForumsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForumSchema | PostGroupsGroupIdGroupForumsResponse401 | PostGroupsGroupIdGroupForumsResponse403 | PostGroupsGroupIdGroupForumsResponse404]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: PostGroupsGroupIdGroupForumsBody | Unset = UNSET,
) -> (
    ForumSchema
    | PostGroupsGroupIdGroupForumsResponse401
    | PostGroupsGroupIdGroupForumsResponse403
    | PostGroupsGroupIdGroupForumsResponse404
    | None
):
    """Create a new forum

    Args:
        group_id (int):  Example: 25.
        body (PostGroupsGroupIdGroupForumsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForumSchema | PostGroupsGroupIdGroupForumsResponse401 | PostGroupsGroupIdGroupForumsResponse403 | PostGroupsGroupIdGroupForumsResponse404
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: PostGroupsGroupIdGroupForumsBody | Unset = UNSET,
) -> Response[
    ForumSchema
    | PostGroupsGroupIdGroupForumsResponse401
    | PostGroupsGroupIdGroupForumsResponse403
    | PostGroupsGroupIdGroupForumsResponse404
]:
    """Create a new forum

    Args:
        group_id (int):  Example: 25.
        body (PostGroupsGroupIdGroupForumsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForumSchema | PostGroupsGroupIdGroupForumsResponse401 | PostGroupsGroupIdGroupForumsResponse403 | PostGroupsGroupIdGroupForumsResponse404]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: PostGroupsGroupIdGroupForumsBody | Unset = UNSET,
) -> (
    ForumSchema
    | PostGroupsGroupIdGroupForumsResponse401
    | PostGroupsGroupIdGroupForumsResponse403
    | PostGroupsGroupIdGroupForumsResponse404
    | None
):
    """Create a new forum

    Args:
        group_id (int):  Example: 25.
        body (PostGroupsGroupIdGroupForumsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForumSchema | PostGroupsGroupIdGroupForumsResponse401 | PostGroupsGroupIdGroupForumsResponse403 | PostGroupsGroupIdGroupForumsResponse404
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            body=body,
        )
    ).parsed
