from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_things_thing_id_collections_response_200 import (
    DeleteThingsThingIdCollectionsResponse200,
)
from ...models.delete_things_thing_id_collections_response_403 import (
    DeleteThingsThingIdCollectionsResponse403,
)
from ...models.delete_things_thing_id_collections_response_404 import (
    DeleteThingsThingIdCollectionsResponse404,
)
from ...types import Response


def _get_kwargs(
    thing_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/things/{thing_id}/collections".format(
            thing_id=quote(str(thing_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteThingsThingIdCollectionsResponse200
    | DeleteThingsThingIdCollectionsResponse403
    | DeleteThingsThingIdCollectionsResponse404
    | None
):
    if response.status_code == 200:
        response_200 = DeleteThingsThingIdCollectionsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = DeleteThingsThingIdCollectionsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteThingsThingIdCollectionsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteThingsThingIdCollectionsResponse200
    | DeleteThingsThingIdCollectionsResponse403
    | DeleteThingsThingIdCollectionsResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    thing_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    DeleteThingsThingIdCollectionsResponse200
    | DeleteThingsThingIdCollectionsResponse403
    | DeleteThingsThingIdCollectionsResponse404
]:
    """Delete a thing from all user's collections

     This cannot be undone.

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteThingsThingIdCollectionsResponse200 | DeleteThingsThingIdCollectionsResponse403 | DeleteThingsThingIdCollectionsResponse404]
    """

    kwargs = _get_kwargs(
        thing_id=thing_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thing_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    DeleteThingsThingIdCollectionsResponse200
    | DeleteThingsThingIdCollectionsResponse403
    | DeleteThingsThingIdCollectionsResponse404
    | None
):
    """Delete a thing from all user's collections

     This cannot be undone.

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteThingsThingIdCollectionsResponse200 | DeleteThingsThingIdCollectionsResponse403 | DeleteThingsThingIdCollectionsResponse404
    """

    return sync_detailed(
        thing_id=thing_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    thing_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    DeleteThingsThingIdCollectionsResponse200
    | DeleteThingsThingIdCollectionsResponse403
    | DeleteThingsThingIdCollectionsResponse404
]:
    """Delete a thing from all user's collections

     This cannot be undone.

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteThingsThingIdCollectionsResponse200 | DeleteThingsThingIdCollectionsResponse403 | DeleteThingsThingIdCollectionsResponse404]
    """

    kwargs = _get_kwargs(
        thing_id=thing_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thing_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    DeleteThingsThingIdCollectionsResponse200
    | DeleteThingsThingIdCollectionsResponse403
    | DeleteThingsThingIdCollectionsResponse404
    | None
):
    """Delete a thing from all user's collections

     This cannot be undone.

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteThingsThingIdCollectionsResponse200 | DeleteThingsThingIdCollectionsResponse403 | DeleteThingsThingIdCollectionsResponse404
    """

    return (
        await asyncio_detailed(
            thing_id=thing_id,
            client=client,
        )
    ).parsed
