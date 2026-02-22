from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.groupforum_schema import GroupforumSchema
from ...models.post_groups_group_id_update_group_forum_forum_id_body import (
    PostGroupsGroupIdUpdateGroupForumForumIdBody,
)
from ...models.post_groups_group_id_update_group_forum_forum_id_response_401 import (
    PostGroupsGroupIdUpdateGroupForumForumIdResponse401,
)
from ...models.post_groups_group_id_update_group_forum_forum_id_response_403 import (
    PostGroupsGroupIdUpdateGroupForumForumIdResponse403,
)
from ...models.post_groups_group_id_update_group_forum_forum_id_response_404 import (
    PostGroupsGroupIdUpdateGroupForumForumIdResponse404,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    forum_id: int,
    *,
    body: PostGroupsGroupIdUpdateGroupForumForumIdBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/groups/{group_id}/update-group-forum/{forum_id}".format(
            group_id=quote(str(group_id), safe=""),
            forum_id=quote(str(forum_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GroupforumSchema
    | PostGroupsGroupIdUpdateGroupForumForumIdResponse401
    | PostGroupsGroupIdUpdateGroupForumForumIdResponse403
    | PostGroupsGroupIdUpdateGroupForumForumIdResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GroupforumSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostGroupsGroupIdUpdateGroupForumForumIdResponse401.from_dict(
            response.json()
        )

        return response_401

    if response.status_code == 403:
        response_403 = PostGroupsGroupIdUpdateGroupForumForumIdResponse403.from_dict(
            response.json()
        )

        return response_403

    if response.status_code == 404:
        response_404 = PostGroupsGroupIdUpdateGroupForumForumIdResponse404.from_dict(
            response.json()
        )

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GroupforumSchema
    | PostGroupsGroupIdUpdateGroupForumForumIdResponse401
    | PostGroupsGroupIdUpdateGroupForumForumIdResponse403
    | PostGroupsGroupIdUpdateGroupForumForumIdResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    forum_id: int,
    *,
    client: AuthenticatedClient,
    body: PostGroupsGroupIdUpdateGroupForumForumIdBody | Unset = UNSET,
) -> Response[
    GroupforumSchema
    | PostGroupsGroupIdUpdateGroupForumForumIdResponse401
    | PostGroupsGroupIdUpdateGroupForumForumIdResponse403
    | PostGroupsGroupIdUpdateGroupForumForumIdResponse404
]:
    """Update a certain forum of group

    Args:
        group_id (int):  Example: 25.
        forum_id (int):  Example: 15561.
        body (PostGroupsGroupIdUpdateGroupForumForumIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GroupforumSchema | PostGroupsGroupIdUpdateGroupForumForumIdResponse401 | PostGroupsGroupIdUpdateGroupForumForumIdResponse403 | PostGroupsGroupIdUpdateGroupForumForumIdResponse404]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        forum_id=forum_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    forum_id: int,
    *,
    client: AuthenticatedClient,
    body: PostGroupsGroupIdUpdateGroupForumForumIdBody | Unset = UNSET,
) -> (
    GroupforumSchema
    | PostGroupsGroupIdUpdateGroupForumForumIdResponse401
    | PostGroupsGroupIdUpdateGroupForumForumIdResponse403
    | PostGroupsGroupIdUpdateGroupForumForumIdResponse404
    | None
):
    """Update a certain forum of group

    Args:
        group_id (int):  Example: 25.
        forum_id (int):  Example: 15561.
        body (PostGroupsGroupIdUpdateGroupForumForumIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GroupforumSchema | PostGroupsGroupIdUpdateGroupForumForumIdResponse401 | PostGroupsGroupIdUpdateGroupForumForumIdResponse403 | PostGroupsGroupIdUpdateGroupForumForumIdResponse404
    """

    return sync_detailed(
        group_id=group_id,
        forum_id=forum_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    forum_id: int,
    *,
    client: AuthenticatedClient,
    body: PostGroupsGroupIdUpdateGroupForumForumIdBody | Unset = UNSET,
) -> Response[
    GroupforumSchema
    | PostGroupsGroupIdUpdateGroupForumForumIdResponse401
    | PostGroupsGroupIdUpdateGroupForumForumIdResponse403
    | PostGroupsGroupIdUpdateGroupForumForumIdResponse404
]:
    """Update a certain forum of group

    Args:
        group_id (int):  Example: 25.
        forum_id (int):  Example: 15561.
        body (PostGroupsGroupIdUpdateGroupForumForumIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GroupforumSchema | PostGroupsGroupIdUpdateGroupForumForumIdResponse401 | PostGroupsGroupIdUpdateGroupForumForumIdResponse403 | PostGroupsGroupIdUpdateGroupForumForumIdResponse404]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        forum_id=forum_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    forum_id: int,
    *,
    client: AuthenticatedClient,
    body: PostGroupsGroupIdUpdateGroupForumForumIdBody | Unset = UNSET,
) -> (
    GroupforumSchema
    | PostGroupsGroupIdUpdateGroupForumForumIdResponse401
    | PostGroupsGroupIdUpdateGroupForumForumIdResponse403
    | PostGroupsGroupIdUpdateGroupForumForumIdResponse404
    | None
):
    """Update a certain forum of group

    Args:
        group_id (int):  Example: 25.
        forum_id (int):  Example: 15561.
        body (PostGroupsGroupIdUpdateGroupForumForumIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GroupforumSchema | PostGroupsGroupIdUpdateGroupForumForumIdResponse401 | PostGroupsGroupIdUpdateGroupForumForumIdResponse403 | PostGroupsGroupIdUpdateGroupForumForumIdResponse404
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            forum_id=forum_id,
            client=client,
            body=body,
        )
    ).parsed
