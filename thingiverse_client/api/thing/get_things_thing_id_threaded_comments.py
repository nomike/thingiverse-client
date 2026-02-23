from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_things_thing_id_threaded_comments_response_200 import (
    GetThingsThingIdThreadedCommentsResponse200,
)
from ...models.get_things_thing_id_threaded_comments_response_401 import (
    GetThingsThingIdThreadedCommentsResponse401,
)
from ...models.get_things_thing_id_threaded_comments_response_403 import (
    GetThingsThingIdThreadedCommentsResponse403,
)
from ...models.get_things_thing_id_threaded_comments_response_404 import (
    GetThingsThingIdThreadedCommentsResponse404,
)
from ...types import Response


def _get_kwargs(
    thing_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/things/{thing_id}/threaded-comments".format(
            thing_id=quote(str(thing_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetThingsThingIdThreadedCommentsResponse200
    | GetThingsThingIdThreadedCommentsResponse401
    | GetThingsThingIdThreadedCommentsResponse403
    | GetThingsThingIdThreadedCommentsResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetThingsThingIdThreadedCommentsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetThingsThingIdThreadedCommentsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetThingsThingIdThreadedCommentsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetThingsThingIdThreadedCommentsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetThingsThingIdThreadedCommentsResponse200
    | GetThingsThingIdThreadedCommentsResponse401
    | GetThingsThingIdThreadedCommentsResponse403
    | GetThingsThingIdThreadedCommentsResponse404
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
    GetThingsThingIdThreadedCommentsResponse200
    | GetThingsThingIdThreadedCommentsResponse401
    | GetThingsThingIdThreadedCommentsResponse403
    | GetThingsThingIdThreadedCommentsResponse404
]:
    """Get all comments for this thing in a quick pre-threaded view

     This is an alternative to GET /things/id/comments

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetThingsThingIdThreadedCommentsResponse200 | GetThingsThingIdThreadedCommentsResponse401 | GetThingsThingIdThreadedCommentsResponse403 | GetThingsThingIdThreadedCommentsResponse404]
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
    GetThingsThingIdThreadedCommentsResponse200
    | GetThingsThingIdThreadedCommentsResponse401
    | GetThingsThingIdThreadedCommentsResponse403
    | GetThingsThingIdThreadedCommentsResponse404
    | None
):
    """Get all comments for this thing in a quick pre-threaded view

     This is an alternative to GET /things/id/comments

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetThingsThingIdThreadedCommentsResponse200 | GetThingsThingIdThreadedCommentsResponse401 | GetThingsThingIdThreadedCommentsResponse403 | GetThingsThingIdThreadedCommentsResponse404
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
    GetThingsThingIdThreadedCommentsResponse200
    | GetThingsThingIdThreadedCommentsResponse401
    | GetThingsThingIdThreadedCommentsResponse403
    | GetThingsThingIdThreadedCommentsResponse404
]:
    """Get all comments for this thing in a quick pre-threaded view

     This is an alternative to GET /things/id/comments

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetThingsThingIdThreadedCommentsResponse200 | GetThingsThingIdThreadedCommentsResponse401 | GetThingsThingIdThreadedCommentsResponse403 | GetThingsThingIdThreadedCommentsResponse404]
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
    GetThingsThingIdThreadedCommentsResponse200
    | GetThingsThingIdThreadedCommentsResponse401
    | GetThingsThingIdThreadedCommentsResponse403
    | GetThingsThingIdThreadedCommentsResponse404
    | None
):
    """Get all comments for this thing in a quick pre-threaded view

     This is an alternative to GET /things/id/comments

    Args:
        thing_id (int):  Example: 1004996.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetThingsThingIdThreadedCommentsResponse200 | GetThingsThingIdThreadedCommentsResponse401 | GetThingsThingIdThreadedCommentsResponse403 | GetThingsThingIdThreadedCommentsResponse404
    """

    return (
        await asyncio_detailed(
            thing_id=thing_id,
            client=client,
        )
    ).parsed
