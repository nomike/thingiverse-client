from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_groups_response_401 import GetGroupsResponse401
from ...models.get_groups_response_403 import GetGroupsResponse403
from ...models.get_groups_response_404 import GetGroupsResponse404
from ...models.group_schema import GroupSchema
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/groups/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetGroupsResponse401 | GetGroupsResponse403 | GetGroupsResponse404 | list[GroupSchema] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GroupSchema.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetGroupsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetGroupsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetGroupsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetGroupsResponse401 | GetGroupsResponse403 | GetGroupsResponse404 | list[GroupSchema]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    GetGroupsResponse401 | GetGroupsResponse403 | GetGroupsResponse404 | list[GroupSchema]
]:
    """List of groups

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupsResponse401 | GetGroupsResponse403 | GetGroupsResponse404 | list[GroupSchema]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> GetGroupsResponse401 | GetGroupsResponse403 | GetGroupsResponse404 | list[GroupSchema] | None:
    """List of groups

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupsResponse401 | GetGroupsResponse403 | GetGroupsResponse404 | list[GroupSchema]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    GetGroupsResponse401 | GetGroupsResponse403 | GetGroupsResponse404 | list[GroupSchema]
]:
    """List of groups

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupsResponse401 | GetGroupsResponse403 | GetGroupsResponse404 | list[GroupSchema]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> GetGroupsResponse401 | GetGroupsResponse403 | GetGroupsResponse404 | list[GroupSchema] | None:
    """List of groups

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupsResponse401 | GetGroupsResponse403 | GetGroupsResponse404 | list[GroupSchema]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
