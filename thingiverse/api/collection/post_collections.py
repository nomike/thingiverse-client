from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collection_schema import CollectionSchema
from ...models.post_collections_body import PostCollectionsBody
from ...models.post_collections_response_400 import PostCollectionsResponse400
from ...models.post_collections_response_401 import PostCollectionsResponse401
from ...models.post_collections_response_403 import PostCollectionsResponse403
from ...models.post_collections_response_404 import PostCollectionsResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostCollectionsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/collections/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CollectionSchema
    | PostCollectionsResponse400
    | PostCollectionsResponse401
    | PostCollectionsResponse403
    | PostCollectionsResponse404
    | None
):
    if response.status_code == 200:
        response_200 = CollectionSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostCollectionsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostCollectionsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostCollectionsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostCollectionsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CollectionSchema
    | PostCollectionsResponse400
    | PostCollectionsResponse401
    | PostCollectionsResponse403
    | PostCollectionsResponse404
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
    body: PostCollectionsBody | Unset = UNSET,
) -> Response[
    CollectionSchema
    | PostCollectionsResponse400
    | PostCollectionsResponse401
    | PostCollectionsResponse403
    | PostCollectionsResponse404
]:
    """Create a new collection

    Args:
        body (PostCollectionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CollectionSchema | PostCollectionsResponse400 | PostCollectionsResponse401 | PostCollectionsResponse403 | PostCollectionsResponse404]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostCollectionsBody | Unset = UNSET,
) -> (
    CollectionSchema
    | PostCollectionsResponse400
    | PostCollectionsResponse401
    | PostCollectionsResponse403
    | PostCollectionsResponse404
    | None
):
    """Create a new collection

    Args:
        body (PostCollectionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CollectionSchema | PostCollectionsResponse400 | PostCollectionsResponse401 | PostCollectionsResponse403 | PostCollectionsResponse404
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostCollectionsBody | Unset = UNSET,
) -> Response[
    CollectionSchema
    | PostCollectionsResponse400
    | PostCollectionsResponse401
    | PostCollectionsResponse403
    | PostCollectionsResponse404
]:
    """Create a new collection

    Args:
        body (PostCollectionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CollectionSchema | PostCollectionsResponse400 | PostCollectionsResponse401 | PostCollectionsResponse403 | PostCollectionsResponse404]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostCollectionsBody | Unset = UNSET,
) -> (
    CollectionSchema
    | PostCollectionsResponse400
    | PostCollectionsResponse401
    | PostCollectionsResponse403
    | PostCollectionsResponse404
    | None
):
    """Create a new collection

    Args:
        body (PostCollectionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CollectionSchema | PostCollectionsResponse400 | PostCollectionsResponse401 | PostCollectionsResponse403 | PostCollectionsResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
