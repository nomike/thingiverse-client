from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_groups_group_id_forum_topics_forum_id_response_401 import (
    GetGroupsGroupIdForumTopicsForumIdResponse401,
)
from ...models.get_groups_group_id_forum_topics_forum_id_response_403 import (
    GetGroupsGroupIdForumTopicsForumIdResponse403,
)
from ...models.get_groups_group_id_forum_topics_forum_id_response_404 import (
    GetGroupsGroupIdForumTopicsForumIdResponse404,
)
from ...models.topic_schema import TopicSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    forum_id: int,
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/groups/{group_id}/forum-topics/{forum_id}".format(
            group_id=quote(str(group_id), safe=""),
            forum_id=quote(str(forum_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetGroupsGroupIdForumTopicsForumIdResponse401
    | GetGroupsGroupIdForumTopicsForumIdResponse403
    | GetGroupsGroupIdForumTopicsForumIdResponse404
    | list[TopicSchema]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TopicSchema.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetGroupsGroupIdForumTopicsForumIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetGroupsGroupIdForumTopicsForumIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetGroupsGroupIdForumTopicsForumIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetGroupsGroupIdForumTopicsForumIdResponse401
    | GetGroupsGroupIdForumTopicsForumIdResponse403
    | GetGroupsGroupIdForumTopicsForumIdResponse404
    | list[TopicSchema]
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
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[
    GetGroupsGroupIdForumTopicsForumIdResponse401
    | GetGroupsGroupIdForumTopicsForumIdResponse403
    | GetGroupsGroupIdForumTopicsForumIdResponse404
    | list[TopicSchema]
]:
    """Get all topics for the group forum

    Args:
        group_id (int):  Example: 25.
        forum_id (int):  Example: 15561.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupsGroupIdForumTopicsForumIdResponse401 | GetGroupsGroupIdForumTopicsForumIdResponse403 | GetGroupsGroupIdForumTopicsForumIdResponse404 | list[TopicSchema]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        forum_id=forum_id,
        page=page,
        per_page=per_page,
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
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> (
    GetGroupsGroupIdForumTopicsForumIdResponse401
    | GetGroupsGroupIdForumTopicsForumIdResponse403
    | GetGroupsGroupIdForumTopicsForumIdResponse404
    | list[TopicSchema]
    | None
):
    """Get all topics for the group forum

    Args:
        group_id (int):  Example: 25.
        forum_id (int):  Example: 15561.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupsGroupIdForumTopicsForumIdResponse401 | GetGroupsGroupIdForumTopicsForumIdResponse403 | GetGroupsGroupIdForumTopicsForumIdResponse404 | list[TopicSchema]
    """

    return sync_detailed(
        group_id=group_id,
        forum_id=forum_id,
        client=client,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    forum_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[
    GetGroupsGroupIdForumTopicsForumIdResponse401
    | GetGroupsGroupIdForumTopicsForumIdResponse403
    | GetGroupsGroupIdForumTopicsForumIdResponse404
    | list[TopicSchema]
]:
    """Get all topics for the group forum

    Args:
        group_id (int):  Example: 25.
        forum_id (int):  Example: 15561.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupsGroupIdForumTopicsForumIdResponse401 | GetGroupsGroupIdForumTopicsForumIdResponse403 | GetGroupsGroupIdForumTopicsForumIdResponse404 | list[TopicSchema]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        forum_id=forum_id,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    forum_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> (
    GetGroupsGroupIdForumTopicsForumIdResponse401
    | GetGroupsGroupIdForumTopicsForumIdResponse403
    | GetGroupsGroupIdForumTopicsForumIdResponse404
    | list[TopicSchema]
    | None
):
    """Get all topics for the group forum

    Args:
        group_id (int):  Example: 25.
        forum_id (int):  Example: 15561.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupsGroupIdForumTopicsForumIdResponse401 | GetGroupsGroupIdForumTopicsForumIdResponse403 | GetGroupsGroupIdForumTopicsForumIdResponse404 | list[TopicSchema]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            forum_id=forum_id,
            client=client,
            page=page,
            per_page=per_page,
        )
    ).parsed
