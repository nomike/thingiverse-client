from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_groups_group_id_group_topics_response_401 import (
    GetGroupsGroupIdGroupTopicsResponse401,
)
from ...models.get_groups_group_id_group_topics_response_403 import (
    GetGroupsGroupIdGroupTopicsResponse403,
)
from ...models.get_groups_group_id_group_topics_response_404 import (
    GetGroupsGroupIdGroupTopicsResponse404,
)
from ...models.topic_schema import TopicSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["filter"] = filter_

    params["sort"] = sort

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/groups/{group_id}/group-topics".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetGroupsGroupIdGroupTopicsResponse401
    | GetGroupsGroupIdGroupTopicsResponse403
    | GetGroupsGroupIdGroupTopicsResponse404
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
        response_401 = GetGroupsGroupIdGroupTopicsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetGroupsGroupIdGroupTopicsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetGroupsGroupIdGroupTopicsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetGroupsGroupIdGroupTopicsResponse401
    | GetGroupsGroupIdGroupTopicsResponse403
    | GetGroupsGroupIdGroupTopicsResponse404
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
    *,
    client: AuthenticatedClient,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[
    GetGroupsGroupIdGroupTopicsResponse401
    | GetGroupsGroupIdGroupTopicsResponse403
    | GetGroupsGroupIdGroupTopicsResponse404
    | list[TopicSchema]
]:
    """List of group topics

    Args:
        group_id (int):  Example: 25.
        filter_ (str | Unset):  Example: pinned.
        sort (str | Unset):  Example: popular.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupsGroupIdGroupTopicsResponse401 | GetGroupsGroupIdGroupTopicsResponse403 | GetGroupsGroupIdGroupTopicsResponse404 | list[TopicSchema]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        filter_=filter_,
        sort=sort,
        page=page,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> (
    GetGroupsGroupIdGroupTopicsResponse401
    | GetGroupsGroupIdGroupTopicsResponse403
    | GetGroupsGroupIdGroupTopicsResponse404
    | list[TopicSchema]
    | None
):
    """List of group topics

    Args:
        group_id (int):  Example: 25.
        filter_ (str | Unset):  Example: pinned.
        sort (str | Unset):  Example: popular.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupsGroupIdGroupTopicsResponse401 | GetGroupsGroupIdGroupTopicsResponse403 | GetGroupsGroupIdGroupTopicsResponse404 | list[TopicSchema]
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        filter_=filter_,
        sort=sort,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[
    GetGroupsGroupIdGroupTopicsResponse401
    | GetGroupsGroupIdGroupTopicsResponse403
    | GetGroupsGroupIdGroupTopicsResponse404
    | list[TopicSchema]
]:
    """List of group topics

    Args:
        group_id (int):  Example: 25.
        filter_ (str | Unset):  Example: pinned.
        sort (str | Unset):  Example: popular.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupsGroupIdGroupTopicsResponse401 | GetGroupsGroupIdGroupTopicsResponse403 | GetGroupsGroupIdGroupTopicsResponse404 | list[TopicSchema]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        filter_=filter_,
        sort=sort,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> (
    GetGroupsGroupIdGroupTopicsResponse401
    | GetGroupsGroupIdGroupTopicsResponse403
    | GetGroupsGroupIdGroupTopicsResponse404
    | list[TopicSchema]
    | None
):
    """List of group topics

    Args:
        group_id (int):  Example: 25.
        filter_ (str | Unset):  Example: pinned.
        sort (str | Unset):  Example: popular.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupsGroupIdGroupTopicsResponse401 | GetGroupsGroupIdGroupTopicsResponse403 | GetGroupsGroupIdGroupTopicsResponse404 | list[TopicSchema]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            filter_=filter_,
            sort=sort,
            page=page,
            per_page=per_page,
        )
    ).parsed
