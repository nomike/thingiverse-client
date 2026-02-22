from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_groups_group_id_group_topics_forum_slug_body import (
    PostGroupsGroupIdGroupTopicsForumSlugBody,
)
from ...models.post_groups_group_id_group_topics_forum_slug_response_401 import (
    PostGroupsGroupIdGroupTopicsForumSlugResponse401,
)
from ...models.post_groups_group_id_group_topics_forum_slug_response_403 import (
    PostGroupsGroupIdGroupTopicsForumSlugResponse403,
)
from ...models.post_groups_group_id_group_topics_forum_slug_response_404 import (
    PostGroupsGroupIdGroupTopicsForumSlugResponse404,
)
from ...models.topic_schema import TopicSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    forum_slug: str,
    *,
    body: PostGroupsGroupIdGroupTopicsForumSlugBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/groups/{group_id}/group-topics/{forum_slug}".format(
            group_id=quote(str(group_id), safe=""),
            forum_slug=quote(str(forum_slug), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostGroupsGroupIdGroupTopicsForumSlugResponse401
    | PostGroupsGroupIdGroupTopicsForumSlugResponse403
    | PostGroupsGroupIdGroupTopicsForumSlugResponse404
    | TopicSchema
    | None
):
    if response.status_code == 200:
        response_200 = TopicSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostGroupsGroupIdGroupTopicsForumSlugResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostGroupsGroupIdGroupTopicsForumSlugResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostGroupsGroupIdGroupTopicsForumSlugResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostGroupsGroupIdGroupTopicsForumSlugResponse401
    | PostGroupsGroupIdGroupTopicsForumSlugResponse403
    | PostGroupsGroupIdGroupTopicsForumSlugResponse404
    | TopicSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    forum_slug: str,
    *,
    client: AuthenticatedClient,
    body: PostGroupsGroupIdGroupTopicsForumSlugBody | Unset = UNSET,
) -> Response[
    PostGroupsGroupIdGroupTopicsForumSlugResponse401
    | PostGroupsGroupIdGroupTopicsForumSlugResponse403
    | PostGroupsGroupIdGroupTopicsForumSlugResponse404
    | TopicSchema
]:
    """Create a new Group Topic

    Args:
        group_id (int):  Example: 25.
        forum_slug (str):  Example: general.
        body (PostGroupsGroupIdGroupTopicsForumSlugBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostGroupsGroupIdGroupTopicsForumSlugResponse401 | PostGroupsGroupIdGroupTopicsForumSlugResponse403 | PostGroupsGroupIdGroupTopicsForumSlugResponse404 | TopicSchema]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        forum_slug=forum_slug,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    forum_slug: str,
    *,
    client: AuthenticatedClient,
    body: PostGroupsGroupIdGroupTopicsForumSlugBody | Unset = UNSET,
) -> (
    PostGroupsGroupIdGroupTopicsForumSlugResponse401
    | PostGroupsGroupIdGroupTopicsForumSlugResponse403
    | PostGroupsGroupIdGroupTopicsForumSlugResponse404
    | TopicSchema
    | None
):
    """Create a new Group Topic

    Args:
        group_id (int):  Example: 25.
        forum_slug (str):  Example: general.
        body (PostGroupsGroupIdGroupTopicsForumSlugBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostGroupsGroupIdGroupTopicsForumSlugResponse401 | PostGroupsGroupIdGroupTopicsForumSlugResponse403 | PostGroupsGroupIdGroupTopicsForumSlugResponse404 | TopicSchema
    """

    return sync_detailed(
        group_id=group_id,
        forum_slug=forum_slug,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    forum_slug: str,
    *,
    client: AuthenticatedClient,
    body: PostGroupsGroupIdGroupTopicsForumSlugBody | Unset = UNSET,
) -> Response[
    PostGroupsGroupIdGroupTopicsForumSlugResponse401
    | PostGroupsGroupIdGroupTopicsForumSlugResponse403
    | PostGroupsGroupIdGroupTopicsForumSlugResponse404
    | TopicSchema
]:
    """Create a new Group Topic

    Args:
        group_id (int):  Example: 25.
        forum_slug (str):  Example: general.
        body (PostGroupsGroupIdGroupTopicsForumSlugBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostGroupsGroupIdGroupTopicsForumSlugResponse401 | PostGroupsGroupIdGroupTopicsForumSlugResponse403 | PostGroupsGroupIdGroupTopicsForumSlugResponse404 | TopicSchema]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        forum_slug=forum_slug,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    forum_slug: str,
    *,
    client: AuthenticatedClient,
    body: PostGroupsGroupIdGroupTopicsForumSlugBody | Unset = UNSET,
) -> (
    PostGroupsGroupIdGroupTopicsForumSlugResponse401
    | PostGroupsGroupIdGroupTopicsForumSlugResponse403
    | PostGroupsGroupIdGroupTopicsForumSlugResponse404
    | TopicSchema
    | None
):
    """Create a new Group Topic

    Args:
        group_id (int):  Example: 25.
        forum_slug (str):  Example: general.
        body (PostGroupsGroupIdGroupTopicsForumSlugBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostGroupsGroupIdGroupTopicsForumSlugResponse401 | PostGroupsGroupIdGroupTopicsForumSlugResponse403 | PostGroupsGroupIdGroupTopicsForumSlugResponse404 | TopicSchema
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            forum_slug=forum_slug,
            client=client,
            body=body,
        )
    ).parsed
