from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_things_thing_id_images_response_401 import GetThingsThingIdImagesResponse401
from ...models.get_things_thing_id_images_response_403 import GetThingsThingIdImagesResponse403
from ...models.get_things_thing_id_images_response_404 import GetThingsThingIdImagesResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    thing_id: int,
    *,
    size: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["size"] = size

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/things/{thing_id}/images".format(
            thing_id=quote(str(thing_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetThingsThingIdImagesResponse401
    | GetThingsThingIdImagesResponse403
    | GetThingsThingIdImagesResponse404
    | None
):
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 401:
        response_401 = GetThingsThingIdImagesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetThingsThingIdImagesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetThingsThingIdImagesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetThingsThingIdImagesResponse401
    | GetThingsThingIdImagesResponse403
    | GetThingsThingIdImagesResponse404
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
    size: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Response[
    Any
    | GetThingsThingIdImagesResponse401
    | GetThingsThingIdImagesResponse403
    | GetThingsThingIdImagesResponse404
]:
    """Get image(s) by thing

     Gets summary information for all images associated with a thing.

    Args:
        thing_id (int):  Example: 1004996.
        size (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetThingsThingIdImagesResponse401 | GetThingsThingIdImagesResponse403 | GetThingsThingIdImagesResponse404]
    """

    kwargs = _get_kwargs(
        thing_id=thing_id,
        size=size,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thing_id: int,
    *,
    client: AuthenticatedClient,
    size: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> (
    Any
    | GetThingsThingIdImagesResponse401
    | GetThingsThingIdImagesResponse403
    | GetThingsThingIdImagesResponse404
    | None
):
    """Get image(s) by thing

     Gets summary information for all images associated with a thing.

    Args:
        thing_id (int):  Example: 1004996.
        size (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetThingsThingIdImagesResponse401 | GetThingsThingIdImagesResponse403 | GetThingsThingIdImagesResponse404
    """

    return sync_detailed(
        thing_id=thing_id,
        client=client,
        size=size,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    thing_id: int,
    *,
    client: AuthenticatedClient,
    size: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Response[
    Any
    | GetThingsThingIdImagesResponse401
    | GetThingsThingIdImagesResponse403
    | GetThingsThingIdImagesResponse404
]:
    """Get image(s) by thing

     Gets summary information for all images associated with a thing.

    Args:
        thing_id (int):  Example: 1004996.
        size (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetThingsThingIdImagesResponse401 | GetThingsThingIdImagesResponse403 | GetThingsThingIdImagesResponse404]
    """

    kwargs = _get_kwargs(
        thing_id=thing_id,
        size=size,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thing_id: int,
    *,
    client: AuthenticatedClient,
    size: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> (
    Any
    | GetThingsThingIdImagesResponse401
    | GetThingsThingIdImagesResponse403
    | GetThingsThingIdImagesResponse404
    | None
):
    """Get image(s) by thing

     Gets summary information for all images associated with a thing.

    Args:
        thing_id (int):  Example: 1004996.
        size (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetThingsThingIdImagesResponse401 | GetThingsThingIdImagesResponse403 | GetThingsThingIdImagesResponse404
    """

    return (
        await asyncio_detailed(
            thing_id=thing_id,
            client=client,
            size=size,
            type_=type_,
        )
    ).parsed
