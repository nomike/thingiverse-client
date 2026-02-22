from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_things_thing_id_copies_body import PostThingsThingIdCopiesBody
from ...models.post_things_thing_id_copies_response_200 import PostThingsThingIdCopiesResponse200
from ...models.post_things_thing_id_copies_response_403 import PostThingsThingIdCopiesResponse403
from ...models.post_things_thing_id_copies_response_404 import PostThingsThingIdCopiesResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    thing_id: int,
    *,
    body: PostThingsThingIdCopiesBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/things/{thing_id}/copies".format(
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
    PostThingsThingIdCopiesResponse200
    | PostThingsThingIdCopiesResponse403
    | PostThingsThingIdCopiesResponse404
    | None
):
    if response.status_code == 200:
        response_200 = PostThingsThingIdCopiesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = PostThingsThingIdCopiesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostThingsThingIdCopiesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostThingsThingIdCopiesResponse200
    | PostThingsThingIdCopiesResponse403
    | PostThingsThingIdCopiesResponse404
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
    body: PostThingsThingIdCopiesBody | Unset = UNSET,
) -> Response[
    PostThingsThingIdCopiesResponse200
    | PostThingsThingIdCopiesResponse403
    | PostThingsThingIdCopiesResponse404
]:
    """Upload image for new copy

     The data needed to upload this copy's image file via an HTTP POST with multipart/form-data encoding.

    Args:
        thing_id (int):  Example: 1004996.
        body (PostThingsThingIdCopiesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostThingsThingIdCopiesResponse200 | PostThingsThingIdCopiesResponse403 | PostThingsThingIdCopiesResponse404]
    """

    kwargs = _get_kwargs(
        thing_id=thing_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thing_id: int,
    *,
    client: AuthenticatedClient,
    body: PostThingsThingIdCopiesBody | Unset = UNSET,
) -> (
    PostThingsThingIdCopiesResponse200
    | PostThingsThingIdCopiesResponse403
    | PostThingsThingIdCopiesResponse404
    | None
):
    """Upload image for new copy

     The data needed to upload this copy's image file via an HTTP POST with multipart/form-data encoding.

    Args:
        thing_id (int):  Example: 1004996.
        body (PostThingsThingIdCopiesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostThingsThingIdCopiesResponse200 | PostThingsThingIdCopiesResponse403 | PostThingsThingIdCopiesResponse404
    """

    return sync_detailed(
        thing_id=thing_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    thing_id: int,
    *,
    client: AuthenticatedClient,
    body: PostThingsThingIdCopiesBody | Unset = UNSET,
) -> Response[
    PostThingsThingIdCopiesResponse200
    | PostThingsThingIdCopiesResponse403
    | PostThingsThingIdCopiesResponse404
]:
    """Upload image for new copy

     The data needed to upload this copy's image file via an HTTP POST with multipart/form-data encoding.

    Args:
        thing_id (int):  Example: 1004996.
        body (PostThingsThingIdCopiesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostThingsThingIdCopiesResponse200 | PostThingsThingIdCopiesResponse403 | PostThingsThingIdCopiesResponse404]
    """

    kwargs = _get_kwargs(
        thing_id=thing_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thing_id: int,
    *,
    client: AuthenticatedClient,
    body: PostThingsThingIdCopiesBody | Unset = UNSET,
) -> (
    PostThingsThingIdCopiesResponse200
    | PostThingsThingIdCopiesResponse403
    | PostThingsThingIdCopiesResponse404
    | None
):
    """Upload image for new copy

     The data needed to upload this copy's image file via an HTTP POST with multipart/form-data encoding.

    Args:
        thing_id (int):  Example: 1004996.
        body (PostThingsThingIdCopiesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostThingsThingIdCopiesResponse200 | PostThingsThingIdCopiesResponse403 | PostThingsThingIdCopiesResponse404
    """

    return (
        await asyncio_detailed(
            thing_id=thing_id,
            client=client,
            body=body,
        )
    ).parsed
