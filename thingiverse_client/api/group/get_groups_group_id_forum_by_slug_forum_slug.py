from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_groups_group_id_forum_by_slug_forum_slug_response_200 import (
    GetGroupsGroupIdForumBySlugForumSlugResponse200,
)
from ...models.get_groups_group_id_forum_by_slug_forum_slug_response_401 import (
    GetGroupsGroupIdForumBySlugForumSlugResponse401,
)
from ...models.get_groups_group_id_forum_by_slug_forum_slug_response_403 import (
    GetGroupsGroupIdForumBySlugForumSlugResponse403,
)
from ...models.get_groups_group_id_forum_by_slug_forum_slug_response_404 import (
    GetGroupsGroupIdForumBySlugForumSlugResponse404,
)
from ...types import Response


def _get_kwargs(
    group_id: int,
    forum_slug: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/groups/{group_id}/forum-by-slug/{forum_slug}".format(
            group_id=quote(str(group_id), safe=""),
            forum_slug=quote(str(forum_slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetGroupsGroupIdForumBySlugForumSlugResponse200
    | GetGroupsGroupIdForumBySlugForumSlugResponse401
    | GetGroupsGroupIdForumBySlugForumSlugResponse403
    | GetGroupsGroupIdForumBySlugForumSlugResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetGroupsGroupIdForumBySlugForumSlugResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetGroupsGroupIdForumBySlugForumSlugResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetGroupsGroupIdForumBySlugForumSlugResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetGroupsGroupIdForumBySlugForumSlugResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetGroupsGroupIdForumBySlugForumSlugResponse200
    | GetGroupsGroupIdForumBySlugForumSlugResponse401
    | GetGroupsGroupIdForumBySlugForumSlugResponse403
    | GetGroupsGroupIdForumBySlugForumSlugResponse404
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
) -> Response[
    GetGroupsGroupIdForumBySlugForumSlugResponse200
    | GetGroupsGroupIdForumBySlugForumSlugResponse401
    | GetGroupsGroupIdForumBySlugForumSlugResponse403
    | GetGroupsGroupIdForumBySlugForumSlugResponse404
]:
    """Get group forum by slug

    Args:
        group_id (int):  Example: 25.
        forum_slug (str):  Example: general.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupsGroupIdForumBySlugForumSlugResponse200 | GetGroupsGroupIdForumBySlugForumSlugResponse401 | GetGroupsGroupIdForumBySlugForumSlugResponse403 | GetGroupsGroupIdForumBySlugForumSlugResponse404]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        forum_slug=forum_slug,
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
) -> (
    GetGroupsGroupIdForumBySlugForumSlugResponse200
    | GetGroupsGroupIdForumBySlugForumSlugResponse401
    | GetGroupsGroupIdForumBySlugForumSlugResponse403
    | GetGroupsGroupIdForumBySlugForumSlugResponse404
    | None
):
    """Get group forum by slug

    Args:
        group_id (int):  Example: 25.
        forum_slug (str):  Example: general.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupsGroupIdForumBySlugForumSlugResponse200 | GetGroupsGroupIdForumBySlugForumSlugResponse401 | GetGroupsGroupIdForumBySlugForumSlugResponse403 | GetGroupsGroupIdForumBySlugForumSlugResponse404
    """

    return sync_detailed(
        group_id=group_id,
        forum_slug=forum_slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    forum_slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetGroupsGroupIdForumBySlugForumSlugResponse200
    | GetGroupsGroupIdForumBySlugForumSlugResponse401
    | GetGroupsGroupIdForumBySlugForumSlugResponse403
    | GetGroupsGroupIdForumBySlugForumSlugResponse404
]:
    """Get group forum by slug

    Args:
        group_id (int):  Example: 25.
        forum_slug (str):  Example: general.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupsGroupIdForumBySlugForumSlugResponse200 | GetGroupsGroupIdForumBySlugForumSlugResponse401 | GetGroupsGroupIdForumBySlugForumSlugResponse403 | GetGroupsGroupIdForumBySlugForumSlugResponse404]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        forum_slug=forum_slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    forum_slug: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetGroupsGroupIdForumBySlugForumSlugResponse200
    | GetGroupsGroupIdForumBySlugForumSlugResponse401
    | GetGroupsGroupIdForumBySlugForumSlugResponse403
    | GetGroupsGroupIdForumBySlugForumSlugResponse404
    | None
):
    """Get group forum by slug

    Args:
        group_id (int):  Example: 25.
        forum_slug (str):  Example: general.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupsGroupIdForumBySlugForumSlugResponse200 | GetGroupsGroupIdForumBySlugForumSlugResponse401 | GetGroupsGroupIdForumBySlugForumSlugResponse403 | GetGroupsGroupIdForumBySlugForumSlugResponse404
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            forum_slug=forum_slug,
            client=client,
        )
    ).parsed
