from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_collections_collection_id_thing_thing_id_response_401 import (
    DeleteCollectionsCollectionIdThingThingIdResponse401,
)
from ...models.delete_collections_collection_id_thing_thing_id_response_403 import (
    DeleteCollectionsCollectionIdThingThingIdResponse403,
)
from ...models.delete_collections_collection_id_thing_thing_id_response_404 import (
    DeleteCollectionsCollectionIdThingThingIdResponse404,
)
from ...types import Response


def _get_kwargs(
    collection_id: int,
    thing_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/collections/{collection_id}/thing/{thing_id}".format(
            collection_id=quote(str(collection_id), safe=""),
            thing_id=quote(str(thing_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteCollectionsCollectionIdThingThingIdResponse401
    | DeleteCollectionsCollectionIdThingThingIdResponse403
    | DeleteCollectionsCollectionIdThingThingIdResponse404
    | int
    | None
):
    if response.status_code == 200:
        response_200 = cast(int, response.json())
        return response_200

    if response.status_code == 401:
        response_401 = DeleteCollectionsCollectionIdThingThingIdResponse401.from_dict(
            response.json()
        )

        return response_401

    if response.status_code == 403:
        response_403 = DeleteCollectionsCollectionIdThingThingIdResponse403.from_dict(
            response.json()
        )

        return response_403

    if response.status_code == 404:
        response_404 = DeleteCollectionsCollectionIdThingThingIdResponse404.from_dict(
            response.json()
        )

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteCollectionsCollectionIdThingThingIdResponse401
    | DeleteCollectionsCollectionIdThingThingIdResponse403
    | DeleteCollectionsCollectionIdThingThingIdResponse404
    | int
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: int,
    thing_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    DeleteCollectionsCollectionIdThingThingIdResponse401
    | DeleteCollectionsCollectionIdThingThingIdResponse403
    | DeleteCollectionsCollectionIdThingThingIdResponse404
    | int
]:
    """Removes a thing from a collection

     Apps may only remove things that they've added to a collection.

    Args:
        collection_id (int):  Example: 1.
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteCollectionsCollectionIdThingThingIdResponse401 | DeleteCollectionsCollectionIdThingThingIdResponse403 | DeleteCollectionsCollectionIdThingThingIdResponse404 | int]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        thing_id=thing_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: int,
    thing_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    DeleteCollectionsCollectionIdThingThingIdResponse401
    | DeleteCollectionsCollectionIdThingThingIdResponse403
    | DeleteCollectionsCollectionIdThingThingIdResponse404
    | int
    | None
):
    """Removes a thing from a collection

     Apps may only remove things that they've added to a collection.

    Args:
        collection_id (int):  Example: 1.
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteCollectionsCollectionIdThingThingIdResponse401 | DeleteCollectionsCollectionIdThingThingIdResponse403 | DeleteCollectionsCollectionIdThingThingIdResponse404 | int
    """

    return sync_detailed(
        collection_id=collection_id,
        thing_id=thing_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    collection_id: int,
    thing_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    DeleteCollectionsCollectionIdThingThingIdResponse401
    | DeleteCollectionsCollectionIdThingThingIdResponse403
    | DeleteCollectionsCollectionIdThingThingIdResponse404
    | int
]:
    """Removes a thing from a collection

     Apps may only remove things that they've added to a collection.

    Args:
        collection_id (int):  Example: 1.
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteCollectionsCollectionIdThingThingIdResponse401 | DeleteCollectionsCollectionIdThingThingIdResponse403 | DeleteCollectionsCollectionIdThingThingIdResponse404 | int]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        thing_id=thing_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: int,
    thing_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    DeleteCollectionsCollectionIdThingThingIdResponse401
    | DeleteCollectionsCollectionIdThingThingIdResponse403
    | DeleteCollectionsCollectionIdThingThingIdResponse404
    | int
    | None
):
    """Removes a thing from a collection

     Apps may only remove things that they've added to a collection.

    Args:
        collection_id (int):  Example: 1.
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteCollectionsCollectionIdThingThingIdResponse401 | DeleteCollectionsCollectionIdThingThingIdResponse403 | DeleteCollectionsCollectionIdThingThingIdResponse404 | int
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            thing_id=thing_id,
            client=client,
        )
    ).parsed
