from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collection_schema import CollectionSchema
from ...models.get_collections_collection_id_response_401 import (
    GetCollectionsCollectionIdResponse401,
)
from ...models.get_collections_collection_id_response_403 import (
    GetCollectionsCollectionIdResponse403,
)
from ...models.get_collections_collection_id_response_404 import (
    GetCollectionsCollectionIdResponse404,
)
from ...types import Response


def _get_kwargs(
    collection_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/collections/{collection_id}/".format(
            collection_id=quote(str(collection_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CollectionSchema
    | GetCollectionsCollectionIdResponse401
    | GetCollectionsCollectionIdResponse403
    | GetCollectionsCollectionIdResponse404
    | None
):
    if response.status_code == 200:
        response_200 = CollectionSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetCollectionsCollectionIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetCollectionsCollectionIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetCollectionsCollectionIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CollectionSchema
    | GetCollectionsCollectionIdResponse401
    | GetCollectionsCollectionIdResponse403
    | GetCollectionsCollectionIdResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    CollectionSchema
    | GetCollectionsCollectionIdResponse401
    | GetCollectionsCollectionIdResponse403
    | GetCollectionsCollectionIdResponse404
]:
    """Get a collection by id

    Args:
        collection_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CollectionSchema | GetCollectionsCollectionIdResponse401 | GetCollectionsCollectionIdResponse403 | GetCollectionsCollectionIdResponse404]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    CollectionSchema
    | GetCollectionsCollectionIdResponse401
    | GetCollectionsCollectionIdResponse403
    | GetCollectionsCollectionIdResponse404
    | None
):
    """Get a collection by id

    Args:
        collection_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CollectionSchema | GetCollectionsCollectionIdResponse401 | GetCollectionsCollectionIdResponse403 | GetCollectionsCollectionIdResponse404
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    collection_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    CollectionSchema
    | GetCollectionsCollectionIdResponse401
    | GetCollectionsCollectionIdResponse403
    | GetCollectionsCollectionIdResponse404
]:
    """Get a collection by id

    Args:
        collection_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CollectionSchema | GetCollectionsCollectionIdResponse401 | GetCollectionsCollectionIdResponse403 | GetCollectionsCollectionIdResponse404]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    CollectionSchema
    | GetCollectionsCollectionIdResponse401
    | GetCollectionsCollectionIdResponse403
    | GetCollectionsCollectionIdResponse404
    | None
):
    """Get a collection by id

    Args:
        collection_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CollectionSchema | GetCollectionsCollectionIdResponse401 | GetCollectionsCollectionIdResponse403 | GetCollectionsCollectionIdResponse404
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
        )
    ).parsed
