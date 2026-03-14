from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tags_tag_things_response_401 import GetTagsTagThingsResponse401
from ...models.get_tags_tag_things_response_403 import GetTagsTagThingsResponse403
from ...models.get_tags_tag_things_response_404 import GetTagsTagThingsResponse404
from ...models.thing_schema import ThingSchema
from ...types import Response


def _get_kwargs(
    tag: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tags/{tag}/things".format(
            tag=quote(str(tag), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetTagsTagThingsResponse401
    | GetTagsTagThingsResponse403
    | GetTagsTagThingsResponse404
    | list[ThingSchema]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ThingSchema.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetTagsTagThingsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetTagsTagThingsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetTagsTagThingsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetTagsTagThingsResponse401
    | GetTagsTagThingsResponse403
    | GetTagsTagThingsResponse404
    | list[ThingSchema]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tag: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetTagsTagThingsResponse401
    | GetTagsTagThingsResponse403
    | GetTagsTagThingsResponse404
    | list[ThingSchema]
]:
    """Get the latest things with the specified tag

     Tags are normalized before searching by converting whitespace to underscores and stripping out all
    characters except alphanumerics, underscores, and dashes ('-').

    Args:
        tag (str):  Example: 3d.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTagsTagThingsResponse401 | GetTagsTagThingsResponse403 | GetTagsTagThingsResponse404 | list[ThingSchema]]
    """

    kwargs = _get_kwargs(
        tag=tag,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tag: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetTagsTagThingsResponse401
    | GetTagsTagThingsResponse403
    | GetTagsTagThingsResponse404
    | list[ThingSchema]
    | None
):
    """Get the latest things with the specified tag

     Tags are normalized before searching by converting whitespace to underscores and stripping out all
    characters except alphanumerics, underscores, and dashes ('-').

    Args:
        tag (str):  Example: 3d.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTagsTagThingsResponse401 | GetTagsTagThingsResponse403 | GetTagsTagThingsResponse404 | list[ThingSchema]
    """

    return sync_detailed(
        tag=tag,
        client=client,
    ).parsed


async def asyncio_detailed(
    tag: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetTagsTagThingsResponse401
    | GetTagsTagThingsResponse403
    | GetTagsTagThingsResponse404
    | list[ThingSchema]
]:
    """Get the latest things with the specified tag

     Tags are normalized before searching by converting whitespace to underscores and stripping out all
    characters except alphanumerics, underscores, and dashes ('-').

    Args:
        tag (str):  Example: 3d.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTagsTagThingsResponse401 | GetTagsTagThingsResponse403 | GetTagsTagThingsResponse404 | list[ThingSchema]]
    """

    kwargs = _get_kwargs(
        tag=tag,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tag: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetTagsTagThingsResponse401
    | GetTagsTagThingsResponse403
    | GetTagsTagThingsResponse404
    | list[ThingSchema]
    | None
):
    """Get the latest things with the specified tag

     Tags are normalized before searching by converting whitespace to underscores and stripping out all
    characters except alphanumerics, underscores, and dashes ('-').

    Args:
        tag (str):  Example: 3d.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTagsTagThingsResponse401 | GetTagsTagThingsResponse403 | GetTagsTagThingsResponse404 | list[ThingSchema]
    """

    return (
        await asyncio_detailed(
            tag=tag,
            client=client,
        )
    ).parsed
