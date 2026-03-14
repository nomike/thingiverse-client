from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_things_body import PostThingsBody
from ...models.post_things_response_400 import PostThingsResponse400
from ...models.post_things_response_401 import PostThingsResponse401
from ...models.post_things_response_403 import PostThingsResponse403
from ...models.post_things_response_404 import PostThingsResponse404
from ...models.thing_schema import ThingSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostThingsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/things/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostThingsResponse400
    | PostThingsResponse401
    | PostThingsResponse403
    | PostThingsResponse404
    | ThingSchema
    | None
):
    if response.status_code == 200:
        response_200 = ThingSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostThingsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostThingsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostThingsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostThingsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostThingsResponse400
    | PostThingsResponse401
    | PostThingsResponse403
    | PostThingsResponse404
    | ThingSchema
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
    body: PostThingsBody | Unset = UNSET,
) -> Response[
    PostThingsResponse400
    | PostThingsResponse401
    | PostThingsResponse403
    | PostThingsResponse404
    | ThingSchema
]:
    """Create a new thing

    Args:
        body (PostThingsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostThingsResponse400 | PostThingsResponse401 | PostThingsResponse403 | PostThingsResponse404 | ThingSchema]
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
    body: PostThingsBody | Unset = UNSET,
) -> (
    PostThingsResponse400
    | PostThingsResponse401
    | PostThingsResponse403
    | PostThingsResponse404
    | ThingSchema
    | None
):
    """Create a new thing

    Args:
        body (PostThingsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostThingsResponse400 | PostThingsResponse401 | PostThingsResponse403 | PostThingsResponse404 | ThingSchema
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostThingsBody | Unset = UNSET,
) -> Response[
    PostThingsResponse400
    | PostThingsResponse401
    | PostThingsResponse403
    | PostThingsResponse404
    | ThingSchema
]:
    """Create a new thing

    Args:
        body (PostThingsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostThingsResponse400 | PostThingsResponse401 | PostThingsResponse403 | PostThingsResponse404 | ThingSchema]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostThingsBody | Unset = UNSET,
) -> (
    PostThingsResponse400
    | PostThingsResponse401
    | PostThingsResponse403
    | PostThingsResponse404
    | ThingSchema
    | None
):
    """Create a new thing

    Args:
        body (PostThingsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostThingsResponse400 | PostThingsResponse401 | PostThingsResponse403 | PostThingsResponse404 | ThingSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
