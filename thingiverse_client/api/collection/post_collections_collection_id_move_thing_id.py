from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_collections_collection_id_move_thing_id_body import (
    PostCollectionsCollectionIdMoveThingIdBody,
)
from ...models.post_collections_collection_id_move_thing_id_response_200 import (
    PostCollectionsCollectionIdMoveThingIdResponse200,
)
from ...models.post_collections_collection_id_move_thing_id_response_401 import (
    PostCollectionsCollectionIdMoveThingIdResponse401,
)
from ...models.post_collections_collection_id_move_thing_id_response_403 import (
    PostCollectionsCollectionIdMoveThingIdResponse403,
)
from ...models.post_collections_collection_id_move_thing_id_response_404 import (
    PostCollectionsCollectionIdMoveThingIdResponse404,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: int,
    thing_id: int,
    *,
    body: PostCollectionsCollectionIdMoveThingIdBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/collections/{collection_id}/move/{thing_id}".format(
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
    PostCollectionsCollectionIdMoveThingIdResponse200
    | PostCollectionsCollectionIdMoveThingIdResponse401
    | PostCollectionsCollectionIdMoveThingIdResponse403
    | PostCollectionsCollectionIdMoveThingIdResponse404
    | None
):
    if response.status_code == 200:
        response_200 = PostCollectionsCollectionIdMoveThingIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostCollectionsCollectionIdMoveThingIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostCollectionsCollectionIdMoveThingIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostCollectionsCollectionIdMoveThingIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostCollectionsCollectionIdMoveThingIdResponse200
    | PostCollectionsCollectionIdMoveThingIdResponse401
    | PostCollectionsCollectionIdMoveThingIdResponse403
    | PostCollectionsCollectionIdMoveThingIdResponse404
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
    body: PostCollectionsCollectionIdMoveThingIdBody | Unset = UNSET,
) -> Response[
    PostCollectionsCollectionIdMoveThingIdResponse200
    | PostCollectionsCollectionIdMoveThingIdResponse401
    | PostCollectionsCollectionIdMoveThingIdResponse403
    | PostCollectionsCollectionIdMoveThingIdResponse404
]:
    """Move a thing between collections

     Things can move a thing to any collection the user owns.

    Args:
        collection_id (int):  Example: 1.
        thing_id (int):  Example: 1004996.
        body (PostCollectionsCollectionIdMoveThingIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCollectionsCollectionIdMoveThingIdResponse200 | PostCollectionsCollectionIdMoveThingIdResponse401 | PostCollectionsCollectionIdMoveThingIdResponse403 | PostCollectionsCollectionIdMoveThingIdResponse404]
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
    body: PostCollectionsCollectionIdMoveThingIdBody | Unset = UNSET,
) -> (
    PostCollectionsCollectionIdMoveThingIdResponse200
    | PostCollectionsCollectionIdMoveThingIdResponse401
    | PostCollectionsCollectionIdMoveThingIdResponse403
    | PostCollectionsCollectionIdMoveThingIdResponse404
    | None
):
    """Move a thing between collections

     Things can move a thing to any collection the user owns.

    Args:
        collection_id (int):  Example: 1.
        thing_id (int):  Example: 1004996.
        body (PostCollectionsCollectionIdMoveThingIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCollectionsCollectionIdMoveThingIdResponse200 | PostCollectionsCollectionIdMoveThingIdResponse401 | PostCollectionsCollectionIdMoveThingIdResponse403 | PostCollectionsCollectionIdMoveThingIdResponse404
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
    body: PostCollectionsCollectionIdMoveThingIdBody | Unset = UNSET,
) -> Response[
    PostCollectionsCollectionIdMoveThingIdResponse200
    | PostCollectionsCollectionIdMoveThingIdResponse401
    | PostCollectionsCollectionIdMoveThingIdResponse403
    | PostCollectionsCollectionIdMoveThingIdResponse404
]:
    """Move a thing between collections

     Things can move a thing to any collection the user owns.

    Args:
        collection_id (int):  Example: 1.
        thing_id (int):  Example: 1004996.
        body (PostCollectionsCollectionIdMoveThingIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCollectionsCollectionIdMoveThingIdResponse200 | PostCollectionsCollectionIdMoveThingIdResponse401 | PostCollectionsCollectionIdMoveThingIdResponse403 | PostCollectionsCollectionIdMoveThingIdResponse404]
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
    body: PostCollectionsCollectionIdMoveThingIdBody | Unset = UNSET,
) -> (
    PostCollectionsCollectionIdMoveThingIdResponse200
    | PostCollectionsCollectionIdMoveThingIdResponse401
    | PostCollectionsCollectionIdMoveThingIdResponse403
    | PostCollectionsCollectionIdMoveThingIdResponse404
    | None
):
    """Move a thing between collections

     Things can move a thing to any collection the user owns.

    Args:
        collection_id (int):  Example: 1.
        thing_id (int):  Example: 1004996.
        body (PostCollectionsCollectionIdMoveThingIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCollectionsCollectionIdMoveThingIdResponse200 | PostCollectionsCollectionIdMoveThingIdResponse401 | PostCollectionsCollectionIdMoveThingIdResponse403 | PostCollectionsCollectionIdMoveThingIdResponse404
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            thing_id=thing_id,
            client=client,
            body=body,
        )
    ).parsed
