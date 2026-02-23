from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tags_tag_response_401 import GetTagsTagResponse401
from ...models.get_tags_tag_response_403 import GetTagsTagResponse403
from ...models.get_tags_tag_response_404 import GetTagsTagResponse404
from ...models.tag_schema import TagSchema
from ...types import Response


def _get_kwargs(
    tag: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tags/{tag}/".format(
            tag=quote(str(tag), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetTagsTagResponse401 | GetTagsTagResponse403 | GetTagsTagResponse404 | TagSchema | None:
    if response.status_code == 200:
        response_200 = TagSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetTagsTagResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetTagsTagResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetTagsTagResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetTagsTagResponse401 | GetTagsTagResponse403 | GetTagsTagResponse404 | TagSchema]:
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
) -> Response[GetTagsTagResponse401 | GetTagsTagResponse403 | GetTagsTagResponse404 | TagSchema]:
    """Return a representation of the given tag

     Tags are normalized before searching by converting whitespace to underscores and stripping out all
    characters except alphanumerics, underscores, and dashes ('-').

    Args:
        tag (str):  Example: 3d.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTagsTagResponse401 | GetTagsTagResponse403 | GetTagsTagResponse404 | TagSchema]
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
) -> GetTagsTagResponse401 | GetTagsTagResponse403 | GetTagsTagResponse404 | TagSchema | None:
    """Return a representation of the given tag

     Tags are normalized before searching by converting whitespace to underscores and stripping out all
    characters except alphanumerics, underscores, and dashes ('-').

    Args:
        tag (str):  Example: 3d.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTagsTagResponse401 | GetTagsTagResponse403 | GetTagsTagResponse404 | TagSchema
    """

    return sync_detailed(
        tag=tag,
        client=client,
    ).parsed


async def asyncio_detailed(
    tag: str,
    *,
    client: AuthenticatedClient,
) -> Response[GetTagsTagResponse401 | GetTagsTagResponse403 | GetTagsTagResponse404 | TagSchema]:
    """Return a representation of the given tag

     Tags are normalized before searching by converting whitespace to underscores and stripping out all
    characters except alphanumerics, underscores, and dashes ('-').

    Args:
        tag (str):  Example: 3d.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTagsTagResponse401 | GetTagsTagResponse403 | GetTagsTagResponse404 | TagSchema]
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
) -> GetTagsTagResponse401 | GetTagsTagResponse403 | GetTagsTagResponse404 | TagSchema | None:
    """Return a representation of the given tag

     Tags are normalized before searching by converting whitespace to underscores and stripping out all
    characters except alphanumerics, underscores, and dashes ('-').

    Args:
        tag (str):  Example: 3d.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTagsTagResponse401 | GetTagsTagResponse403 | GetTagsTagResponse404 | TagSchema
    """

    return (
        await asyncio_detailed(
            tag=tag,
            client=client,
        )
    ).parsed
