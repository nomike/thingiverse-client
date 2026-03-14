from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_collections_collection_id_things_response_401 import (
    GetCollectionsCollectionIdThingsResponse401,
)
from ...models.get_collections_collection_id_things_response_403 import (
    GetCollectionsCollectionIdThingsResponse403,
)
from ...models.get_collections_collection_id_things_response_404 import (
    GetCollectionsCollectionIdThingsResponse404,
)
from ...models.short_thing_schema import ShortThingSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: int,
    *,
    sort: str | Unset = UNSET,
    search: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    image_type: str | Unset = UNSET,
    image_size: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["sort"] = sort

    params["search"] = search

    params["page"] = page

    params["per_page"] = per_page

    params["image_type"] = image_type

    params["image_size"] = image_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/collections/{collection_id}/things".format(
            collection_id=quote(str(collection_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetCollectionsCollectionIdThingsResponse401
    | GetCollectionsCollectionIdThingsResponse403
    | GetCollectionsCollectionIdThingsResponse404
    | list[ShortThingSchema]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ShortThingSchema.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetCollectionsCollectionIdThingsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetCollectionsCollectionIdThingsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetCollectionsCollectionIdThingsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetCollectionsCollectionIdThingsResponse401
    | GetCollectionsCollectionIdThingsResponse403
    | GetCollectionsCollectionIdThingsResponse404
    | list[ShortThingSchema]
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
    sort: str | Unset = UNSET,
    search: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    image_type: str | Unset = UNSET,
    image_size: str | Unset = UNSET,
) -> Response[
    GetCollectionsCollectionIdThingsResponse401
    | GetCollectionsCollectionIdThingsResponse403
    | GetCollectionsCollectionIdThingsResponse404
    | list[ShortThingSchema]
]:
    """Get Things in a collection

    Args:
        collection_id (int):  Example: 1.
        sort (str | Unset):
        search (str | Unset):
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.
        image_type (str | Unset):  Example: display.
        image_size (str | Unset):  Example: large.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCollectionsCollectionIdThingsResponse401 | GetCollectionsCollectionIdThingsResponse403 | GetCollectionsCollectionIdThingsResponse404 | list[ShortThingSchema]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        sort=sort,
        search=search,
        page=page,
        per_page=per_page,
        image_type=image_type,
        image_size=image_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: int,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    search: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    image_type: str | Unset = UNSET,
    image_size: str | Unset = UNSET,
) -> (
    GetCollectionsCollectionIdThingsResponse401
    | GetCollectionsCollectionIdThingsResponse403
    | GetCollectionsCollectionIdThingsResponse404
    | list[ShortThingSchema]
    | None
):
    """Get Things in a collection

    Args:
        collection_id (int):  Example: 1.
        sort (str | Unset):
        search (str | Unset):
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.
        image_type (str | Unset):  Example: display.
        image_size (str | Unset):  Example: large.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCollectionsCollectionIdThingsResponse401 | GetCollectionsCollectionIdThingsResponse403 | GetCollectionsCollectionIdThingsResponse404 | list[ShortThingSchema]
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        sort=sort,
        search=search,
        page=page,
        per_page=per_page,
        image_type=image_type,
        image_size=image_size,
    ).parsed


async def asyncio_detailed(
    collection_id: int,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    search: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    image_type: str | Unset = UNSET,
    image_size: str | Unset = UNSET,
) -> Response[
    GetCollectionsCollectionIdThingsResponse401
    | GetCollectionsCollectionIdThingsResponse403
    | GetCollectionsCollectionIdThingsResponse404
    | list[ShortThingSchema]
]:
    """Get Things in a collection

    Args:
        collection_id (int):  Example: 1.
        sort (str | Unset):
        search (str | Unset):
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.
        image_type (str | Unset):  Example: display.
        image_size (str | Unset):  Example: large.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCollectionsCollectionIdThingsResponse401 | GetCollectionsCollectionIdThingsResponse403 | GetCollectionsCollectionIdThingsResponse404 | list[ShortThingSchema]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        sort=sort,
        search=search,
        page=page,
        per_page=per_page,
        image_type=image_type,
        image_size=image_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: int,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    search: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    image_type: str | Unset = UNSET,
    image_size: str | Unset = UNSET,
) -> (
    GetCollectionsCollectionIdThingsResponse401
    | GetCollectionsCollectionIdThingsResponse403
    | GetCollectionsCollectionIdThingsResponse404
    | list[ShortThingSchema]
    | None
):
    """Get Things in a collection

    Args:
        collection_id (int):  Example: 1.
        sort (str | Unset):
        search (str | Unset):
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.
        image_type (str | Unset):  Example: display.
        image_size (str | Unset):  Example: large.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCollectionsCollectionIdThingsResponse401 | GetCollectionsCollectionIdThingsResponse403 | GetCollectionsCollectionIdThingsResponse404 | list[ShortThingSchema]
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            sort=sort,
            search=search,
            page=page,
            per_page=per_page,
            image_type=image_type,
            image_size=image_size,
        )
    ).parsed
