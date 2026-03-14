from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tags_response_401 import GetTagsResponse401
from ...models.get_tags_response_403 import GetTagsResponse403
from ...models.get_tags_response_404 import GetTagsResponse404
from ...models.tag_schema import TagSchema
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tags/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetTagsResponse401 | GetTagsResponse403 | GetTagsResponse404 | list[TagSchema] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TagSchema.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetTagsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetTagsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetTagsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetTagsResponse401 | GetTagsResponse403 | GetTagsResponse404 | list[TagSchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[GetTagsResponse401 | GetTagsResponse403 | GetTagsResponse404 | list[TagSchema]]:
    """Get the list of tags.

     returns a list of all tags in alphabetical order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTagsResponse401 | GetTagsResponse403 | GetTagsResponse404 | list[TagSchema]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> GetTagsResponse401 | GetTagsResponse403 | GetTagsResponse404 | list[TagSchema] | None:
    """Get the list of tags.

     returns a list of all tags in alphabetical order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTagsResponse401 | GetTagsResponse403 | GetTagsResponse404 | list[TagSchema]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[GetTagsResponse401 | GetTagsResponse403 | GetTagsResponse404 | list[TagSchema]]:
    """Get the list of tags.

     returns a list of all tags in alphabetical order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTagsResponse401 | GetTagsResponse403 | GetTagsResponse404 | list[TagSchema]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> GetTagsResponse401 | GetTagsResponse403 | GetTagsResponse404 | list[TagSchema] | None:
    """Get the list of tags.

     returns a list of all tags in alphabetical order.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTagsResponse401 | GetTagsResponse403 | GetTagsResponse404 | list[TagSchema]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
