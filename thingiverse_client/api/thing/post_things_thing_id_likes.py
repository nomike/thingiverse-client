from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_things_thing_id_likes_response_200 import PostThingsThingIdLikesResponse200
from ...models.post_things_thing_id_likes_response_401 import PostThingsThingIdLikesResponse401
from ...models.post_things_thing_id_likes_response_403 import PostThingsThingIdLikesResponse403
from ...models.post_things_thing_id_likes_response_404 import PostThingsThingIdLikesResponse404
from ...types import Response


def _get_kwargs(
    thing_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/things/{thing_id}/likes".format(
            thing_id=quote(str(thing_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostThingsThingIdLikesResponse200
    | PostThingsThingIdLikesResponse401
    | PostThingsThingIdLikesResponse403
    | PostThingsThingIdLikesResponse404
    | None
):
    if response.status_code == 200:
        response_200 = PostThingsThingIdLikesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = PostThingsThingIdLikesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostThingsThingIdLikesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostThingsThingIdLikesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostThingsThingIdLikesResponse200
    | PostThingsThingIdLikesResponse401
    | PostThingsThingIdLikesResponse403
    | PostThingsThingIdLikesResponse404
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
    Any
    | PostThingsThingIdLikesResponse200
    | PostThingsThingIdLikesResponse401
    | PostThingsThingIdLikesResponse403
    | PostThingsThingIdLikesResponse404
]:
    """Like a thing

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostThingsThingIdLikesResponse200 | PostThingsThingIdLikesResponse401 | PostThingsThingIdLikesResponse403 | PostThingsThingIdLikesResponse404]
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
    Any
    | PostThingsThingIdLikesResponse200
    | PostThingsThingIdLikesResponse401
    | PostThingsThingIdLikesResponse403
    | PostThingsThingIdLikesResponse404
    | None
):
    """Like a thing

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostThingsThingIdLikesResponse200 | PostThingsThingIdLikesResponse401 | PostThingsThingIdLikesResponse403 | PostThingsThingIdLikesResponse404
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
    Any
    | PostThingsThingIdLikesResponse200
    | PostThingsThingIdLikesResponse401
    | PostThingsThingIdLikesResponse403
    | PostThingsThingIdLikesResponse404
]:
    """Like a thing

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostThingsThingIdLikesResponse200 | PostThingsThingIdLikesResponse401 | PostThingsThingIdLikesResponse403 | PostThingsThingIdLikesResponse404]
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
    Any
    | PostThingsThingIdLikesResponse200
    | PostThingsThingIdLikesResponse401
    | PostThingsThingIdLikesResponse403
    | PostThingsThingIdLikesResponse404
    | None
):
    """Like a thing

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostThingsThingIdLikesResponse200 | PostThingsThingIdLikesResponse401 | PostThingsThingIdLikesResponse403 | PostThingsThingIdLikesResponse404
    """

    return (
        await asyncio_detailed(
            thing_id=thing_id,
            client=client,
        )
    ).parsed
