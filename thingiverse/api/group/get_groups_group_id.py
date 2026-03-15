from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_groups_group_id_response_401 import GetGroupsGroupIdResponse401
from ...models.get_groups_group_id_response_403 import GetGroupsGroupIdResponse403
from ...models.get_groups_group_id_response_404 import GetGroupsGroupIdResponse404
from ...models.group_schema import GroupSchema
from ...types import Response


def _get_kwargs(
    group_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/groups/{group_id}".format(
            group_id=quote(str(group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetGroupsGroupIdResponse401
    | GetGroupsGroupIdResponse403
    | GetGroupsGroupIdResponse404
    | GroupSchema
    | None
):
    if response.status_code == 200:
        response_200 = GroupSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetGroupsGroupIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetGroupsGroupIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetGroupsGroupIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetGroupsGroupIdResponse401
    | GetGroupsGroupIdResponse403
    | GetGroupsGroupIdResponse404
    | GroupSchema
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
    GetGroupsGroupIdResponse401
    | GetGroupsGroupIdResponse403
    | GetGroupsGroupIdResponse404
    | GroupSchema
]:
    """Get group by id

    Args:
        group_id (int):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupsGroupIdResponse401 | GetGroupsGroupIdResponse403 | GetGroupsGroupIdResponse404 | GroupSchema]
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
    GetGroupsGroupIdResponse401
    | GetGroupsGroupIdResponse403
    | GetGroupsGroupIdResponse404
    | GroupSchema
    | None
):
    """Get group by id

    Args:
        group_id (int):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupsGroupIdResponse401 | GetGroupsGroupIdResponse403 | GetGroupsGroupIdResponse404 | GroupSchema
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
    GetGroupsGroupIdResponse401
    | GetGroupsGroupIdResponse403
    | GetGroupsGroupIdResponse404
    | GroupSchema
]:
    """Get group by id

    Args:
        group_id (int):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupsGroupIdResponse401 | GetGroupsGroupIdResponse403 | GetGroupsGroupIdResponse404 | GroupSchema]
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
    GetGroupsGroupIdResponse401
    | GetGroupsGroupIdResponse403
    | GetGroupsGroupIdResponse404
    | GroupSchema
    | None
):
    """Get group by id

    Args:
        group_id (int):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupsGroupIdResponse401 | GetGroupsGroupIdResponse403 | GetGroupsGroupIdResponse404 | GroupSchema
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed
