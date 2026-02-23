from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_groups_group_id_response_200 import DeleteGroupsGroupIdResponse200
from ...models.delete_groups_group_id_response_401 import DeleteGroupsGroupIdResponse401
from ...models.delete_groups_group_id_response_403 import DeleteGroupsGroupIdResponse403
from ...models.delete_groups_group_id_response_404 import DeleteGroupsGroupIdResponse404
from ...types import Response


def _get_kwargs(
    group_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/groups/{group_id}".format(
            group_id=quote(str(group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteGroupsGroupIdResponse200
    | DeleteGroupsGroupIdResponse401
    | DeleteGroupsGroupIdResponse403
    | DeleteGroupsGroupIdResponse404
    | None
):
    if response.status_code == 200:
        response_200 = DeleteGroupsGroupIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = DeleteGroupsGroupIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteGroupsGroupIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteGroupsGroupIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteGroupsGroupIdResponse200
    | DeleteGroupsGroupIdResponse401
    | DeleteGroupsGroupIdResponse403
    | DeleteGroupsGroupIdResponse404
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
    DeleteGroupsGroupIdResponse200
    | DeleteGroupsGroupIdResponse401
    | DeleteGroupsGroupIdResponse403
    | DeleteGroupsGroupIdResponse404
]:
    """Delete a group

     This cannot be undone.

    Args:
        group_id (int):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteGroupsGroupIdResponse200 | DeleteGroupsGroupIdResponse401 | DeleteGroupsGroupIdResponse403 | DeleteGroupsGroupIdResponse404]
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
    DeleteGroupsGroupIdResponse200
    | DeleteGroupsGroupIdResponse401
    | DeleteGroupsGroupIdResponse403
    | DeleteGroupsGroupIdResponse404
    | None
):
    """Delete a group

     This cannot be undone.

    Args:
        group_id (int):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteGroupsGroupIdResponse200 | DeleteGroupsGroupIdResponse401 | DeleteGroupsGroupIdResponse403 | DeleteGroupsGroupIdResponse404
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
    DeleteGroupsGroupIdResponse200
    | DeleteGroupsGroupIdResponse401
    | DeleteGroupsGroupIdResponse403
    | DeleteGroupsGroupIdResponse404
]:
    """Delete a group

     This cannot be undone.

    Args:
        group_id (int):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteGroupsGroupIdResponse200 | DeleteGroupsGroupIdResponse401 | DeleteGroupsGroupIdResponse403 | DeleteGroupsGroupIdResponse404]
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
    DeleteGroupsGroupIdResponse200
    | DeleteGroupsGroupIdResponse401
    | DeleteGroupsGroupIdResponse403
    | DeleteGroupsGroupIdResponse404
    | None
):
    """Delete a group

     This cannot be undone.

    Args:
        group_id (int):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteGroupsGroupIdResponse200 | DeleteGroupsGroupIdResponse401 | DeleteGroupsGroupIdResponse403 | DeleteGroupsGroupIdResponse404
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed
