from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_groups_group_id_things_thing_id_response_200 import (
    DeleteGroupsGroupIdThingsThingIdResponse200,
)
from ...models.delete_groups_group_id_things_thing_id_response_401 import (
    DeleteGroupsGroupIdThingsThingIdResponse401,
)
from ...models.delete_groups_group_id_things_thing_id_response_403 import (
    DeleteGroupsGroupIdThingsThingIdResponse403,
)
from ...models.delete_groups_group_id_things_thing_id_response_404 import (
    DeleteGroupsGroupIdThingsThingIdResponse404,
)
from ...types import Response


def _get_kwargs(
    group_id: int,
    thing_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/groups/{group_id}/things/{thing_id}".format(
            group_id=quote(str(group_id), safe=""),
            thing_id=quote(str(thing_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteGroupsGroupIdThingsThingIdResponse200
    | DeleteGroupsGroupIdThingsThingIdResponse401
    | DeleteGroupsGroupIdThingsThingIdResponse403
    | DeleteGroupsGroupIdThingsThingIdResponse404
    | None
):
    if response.status_code == 200:
        response_200 = DeleteGroupsGroupIdThingsThingIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = DeleteGroupsGroupIdThingsThingIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteGroupsGroupIdThingsThingIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteGroupsGroupIdThingsThingIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteGroupsGroupIdThingsThingIdResponse200
    | DeleteGroupsGroupIdThingsThingIdResponse401
    | DeleteGroupsGroupIdThingsThingIdResponse403
    | DeleteGroupsGroupIdThingsThingIdResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    thing_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    DeleteGroupsGroupIdThingsThingIdResponse200
    | DeleteGroupsGroupIdThingsThingIdResponse401
    | DeleteGroupsGroupIdThingsThingIdResponse403
    | DeleteGroupsGroupIdThingsThingIdResponse404
]:
    """Delete thing from group

    Args:
        group_id (int):  Example: 25.
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteGroupsGroupIdThingsThingIdResponse200 | DeleteGroupsGroupIdThingsThingIdResponse401 | DeleteGroupsGroupIdThingsThingIdResponse403 | DeleteGroupsGroupIdThingsThingIdResponse404]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        thing_id=thing_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    thing_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    DeleteGroupsGroupIdThingsThingIdResponse200
    | DeleteGroupsGroupIdThingsThingIdResponse401
    | DeleteGroupsGroupIdThingsThingIdResponse403
    | DeleteGroupsGroupIdThingsThingIdResponse404
    | None
):
    """Delete thing from group

    Args:
        group_id (int):  Example: 25.
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteGroupsGroupIdThingsThingIdResponse200 | DeleteGroupsGroupIdThingsThingIdResponse401 | DeleteGroupsGroupIdThingsThingIdResponse403 | DeleteGroupsGroupIdThingsThingIdResponse404
    """

    return sync_detailed(
        group_id=group_id,
        thing_id=thing_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    thing_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    DeleteGroupsGroupIdThingsThingIdResponse200
    | DeleteGroupsGroupIdThingsThingIdResponse401
    | DeleteGroupsGroupIdThingsThingIdResponse403
    | DeleteGroupsGroupIdThingsThingIdResponse404
]:
    """Delete thing from group

    Args:
        group_id (int):  Example: 25.
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteGroupsGroupIdThingsThingIdResponse200 | DeleteGroupsGroupIdThingsThingIdResponse401 | DeleteGroupsGroupIdThingsThingIdResponse403 | DeleteGroupsGroupIdThingsThingIdResponse404]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        thing_id=thing_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    thing_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    DeleteGroupsGroupIdThingsThingIdResponse200
    | DeleteGroupsGroupIdThingsThingIdResponse401
    | DeleteGroupsGroupIdThingsThingIdResponse403
    | DeleteGroupsGroupIdThingsThingIdResponse404
    | None
):
    """Delete thing from group

    Args:
        group_id (int):  Example: 25.
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteGroupsGroupIdThingsThingIdResponse200 | DeleteGroupsGroupIdThingsThingIdResponse401 | DeleteGroupsGroupIdThingsThingIdResponse403 | DeleteGroupsGroupIdThingsThingIdResponse404
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            thing_id=thing_id,
            client=client,
        )
    ).parsed
