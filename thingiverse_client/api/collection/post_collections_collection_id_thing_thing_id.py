from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_collections_collection_id_thing_thing_id_body import (
    PostCollectionsCollectionIdThingThingIdBody,
)
from ...models.post_collections_collection_id_thing_thing_id_response_200 import (
    PostCollectionsCollectionIdThingThingIdResponse200,
)
from ...models.post_collections_collection_id_thing_thing_id_response_401 import (
    PostCollectionsCollectionIdThingThingIdResponse401,
)
from ...models.post_collections_collection_id_thing_thing_id_response_403 import (
    PostCollectionsCollectionIdThingThingIdResponse403,
)
from ...models.post_collections_collection_id_thing_thing_id_response_404 import (
    PostCollectionsCollectionIdThingThingIdResponse404,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: int,
    thing_id: int,
    *,
    body: PostCollectionsCollectionIdThingThingIdBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/collections/{collection_id}/thing/{thing_id}".format(
            collection_id=quote(str(collection_id), safe=""),
            thing_id=quote(str(thing_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostCollectionsCollectionIdThingThingIdResponse200
    | PostCollectionsCollectionIdThingThingIdResponse401
    | PostCollectionsCollectionIdThingThingIdResponse403
    | PostCollectionsCollectionIdThingThingIdResponse404
    | None
):
    if response.status_code == 200:
        response_200 = PostCollectionsCollectionIdThingThingIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostCollectionsCollectionIdThingThingIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostCollectionsCollectionIdThingThingIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostCollectionsCollectionIdThingThingIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostCollectionsCollectionIdThingThingIdResponse200
    | PostCollectionsCollectionIdThingThingIdResponse401
    | PostCollectionsCollectionIdThingThingIdResponse403
    | PostCollectionsCollectionIdThingThingIdResponse404
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
    body: PostCollectionsCollectionIdThingThingIdBody | Unset = UNSET,
) -> Response[
    PostCollectionsCollectionIdThingThingIdResponse200
    | PostCollectionsCollectionIdThingThingIdResponse401
    | PostCollectionsCollectionIdThingThingIdResponse403
    | PostCollectionsCollectionIdThingThingIdResponse404
]:
    """Add a thing to a collection

     Apps can add to any collection the user owns. Do not abuse or we'll change that.

    Args:
        collection_id (int):  Example: 1.
        thing_id (int):  Example: 1004996.
        body (PostCollectionsCollectionIdThingThingIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCollectionsCollectionIdThingThingIdResponse200 | PostCollectionsCollectionIdThingThingIdResponse401 | PostCollectionsCollectionIdThingThingIdResponse403 | PostCollectionsCollectionIdThingThingIdResponse404]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        thing_id=thing_id,
        body=body,
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
    body: PostCollectionsCollectionIdThingThingIdBody | Unset = UNSET,
) -> (
    PostCollectionsCollectionIdThingThingIdResponse200
    | PostCollectionsCollectionIdThingThingIdResponse401
    | PostCollectionsCollectionIdThingThingIdResponse403
    | PostCollectionsCollectionIdThingThingIdResponse404
    | None
):
    """Add a thing to a collection

     Apps can add to any collection the user owns. Do not abuse or we'll change that.

    Args:
        collection_id (int):  Example: 1.
        thing_id (int):  Example: 1004996.
        body (PostCollectionsCollectionIdThingThingIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCollectionsCollectionIdThingThingIdResponse200 | PostCollectionsCollectionIdThingThingIdResponse401 | PostCollectionsCollectionIdThingThingIdResponse403 | PostCollectionsCollectionIdThingThingIdResponse404
    """

    return sync_detailed(
        collection_id=collection_id,
        thing_id=thing_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    collection_id: int,
    thing_id: int,
    *,
    client: AuthenticatedClient,
    body: PostCollectionsCollectionIdThingThingIdBody | Unset = UNSET,
) -> Response[
    PostCollectionsCollectionIdThingThingIdResponse200
    | PostCollectionsCollectionIdThingThingIdResponse401
    | PostCollectionsCollectionIdThingThingIdResponse403
    | PostCollectionsCollectionIdThingThingIdResponse404
]:
    """Add a thing to a collection

     Apps can add to any collection the user owns. Do not abuse or we'll change that.

    Args:
        collection_id (int):  Example: 1.
        thing_id (int):  Example: 1004996.
        body (PostCollectionsCollectionIdThingThingIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCollectionsCollectionIdThingThingIdResponse200 | PostCollectionsCollectionIdThingThingIdResponse401 | PostCollectionsCollectionIdThingThingIdResponse403 | PostCollectionsCollectionIdThingThingIdResponse404]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        thing_id=thing_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: int,
    thing_id: int,
    *,
    client: AuthenticatedClient,
    body: PostCollectionsCollectionIdThingThingIdBody | Unset = UNSET,
) -> (
    PostCollectionsCollectionIdThingThingIdResponse200
    | PostCollectionsCollectionIdThingThingIdResponse401
    | PostCollectionsCollectionIdThingThingIdResponse403
    | PostCollectionsCollectionIdThingThingIdResponse404
    | None
):
    """Add a thing to a collection

     Apps can add to any collection the user owns. Do not abuse or we'll change that.

    Args:
        collection_id (int):  Example: 1.
        thing_id (int):  Example: 1004996.
        body (PostCollectionsCollectionIdThingThingIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCollectionsCollectionIdThingThingIdResponse200 | PostCollectionsCollectionIdThingThingIdResponse401 | PostCollectionsCollectionIdThingThingIdResponse403 | PostCollectionsCollectionIdThingThingIdResponse404
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            thing_id=thing_id,
            client=client,
            body=body,
        )
    ).parsed
