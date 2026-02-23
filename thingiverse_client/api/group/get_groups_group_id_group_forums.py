from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.forum_schema import ForumSchema
from ...models.get_groups_group_id_group_forums_response_401 import (
    GetGroupsGroupIdGroupForumsResponse401,
)
from ...models.get_groups_group_id_group_forums_response_403 import (
    GetGroupsGroupIdGroupForumsResponse403,
)
from ...models.get_groups_group_id_group_forums_response_404 import (
    GetGroupsGroupIdGroupForumsResponse404,
)
from ...types import Response


def _get_kwargs(
    group_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/groups/{group_id}/group-forums".format(
            group_id=quote(str(group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetGroupsGroupIdGroupForumsResponse401
    | GetGroupsGroupIdGroupForumsResponse403
    | GetGroupsGroupIdGroupForumsResponse404
    | list[ForumSchema]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ForumSchema.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetGroupsGroupIdGroupForumsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetGroupsGroupIdGroupForumsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetGroupsGroupIdGroupForumsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetGroupsGroupIdGroupForumsResponse401
    | GetGroupsGroupIdGroupForumsResponse403
    | GetGroupsGroupIdGroupForumsResponse404
    | list[ForumSchema]
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
) -> Response[
    GetGroupsGroupIdGroupForumsResponse401
    | GetGroupsGroupIdGroupForumsResponse403
    | GetGroupsGroupIdGroupForumsResponse404
    | list[ForumSchema]
]:
    """List of group forums

    Args:
        group_id (int):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupsGroupIdGroupForumsResponse401 | GetGroupsGroupIdGroupForumsResponse403 | GetGroupsGroupIdGroupForumsResponse404 | list[ForumSchema]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    GetGroupsGroupIdGroupForumsResponse401
    | GetGroupsGroupIdGroupForumsResponse403
    | GetGroupsGroupIdGroupForumsResponse404
    | list[ForumSchema]
    | None
):
    """List of group forums

    Args:
        group_id (int):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupsGroupIdGroupForumsResponse401 | GetGroupsGroupIdGroupForumsResponse403 | GetGroupsGroupIdGroupForumsResponse404 | list[ForumSchema]
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetGroupsGroupIdGroupForumsResponse401
    | GetGroupsGroupIdGroupForumsResponse403
    | GetGroupsGroupIdGroupForumsResponse404
    | list[ForumSchema]
]:
    """List of group forums

    Args:
        group_id (int):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupsGroupIdGroupForumsResponse401 | GetGroupsGroupIdGroupForumsResponse403 | GetGroupsGroupIdGroupForumsResponse404 | list[ForumSchema]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    GetGroupsGroupIdGroupForumsResponse401
    | GetGroupsGroupIdGroupForumsResponse403
    | GetGroupsGroupIdGroupForumsResponse404
    | list[ForumSchema]
    | None
):
    """List of group forums

    Args:
        group_id (int):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupsGroupIdGroupForumsResponse401 | GetGroupsGroupIdGroupForumsResponse403 | GetGroupsGroupIdGroupForumsResponse404 | list[ForumSchema]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed
