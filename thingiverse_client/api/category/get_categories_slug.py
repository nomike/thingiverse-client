from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_categories_slug_response_200 import GetCategoriesSlugResponse200
from ...models.get_categories_slug_response_401 import GetCategoriesSlugResponse401
from ...models.get_categories_slug_response_403 import GetCategoriesSlugResponse403
from ...models.get_categories_slug_response_404 import GetCategoriesSlugResponse404
from ...types import Response


def _get_kwargs(
    slug: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/categories/{slug}".format(
            slug=quote(str(slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetCategoriesSlugResponse200
    | GetCategoriesSlugResponse401
    | GetCategoriesSlugResponse403
    | GetCategoriesSlugResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetCategoriesSlugResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetCategoriesSlugResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetCategoriesSlugResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetCategoriesSlugResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetCategoriesSlugResponse200
    | GetCategoriesSlugResponse401
    | GetCategoriesSlugResponse403
    | GetCategoriesSlugResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetCategoriesSlugResponse200
    | GetCategoriesSlugResponse401
    | GetCategoriesSlugResponse403
    | GetCategoriesSlugResponse404
]:
    """Get category by slug

    Args:
        slug (str):  Example: art.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCategoriesSlugResponse200 | GetCategoriesSlugResponse401 | GetCategoriesSlugResponse403 | GetCategoriesSlugResponse404]
    """

    kwargs = _get_kwargs(
        slug=slug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    slug: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetCategoriesSlugResponse200
    | GetCategoriesSlugResponse401
    | GetCategoriesSlugResponse403
    | GetCategoriesSlugResponse404
    | None
):
    """Get category by slug

    Args:
        slug (str):  Example: art.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCategoriesSlugResponse200 | GetCategoriesSlugResponse401 | GetCategoriesSlugResponse403 | GetCategoriesSlugResponse404
    """

    return sync_detailed(
        slug=slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetCategoriesSlugResponse200
    | GetCategoriesSlugResponse401
    | GetCategoriesSlugResponse403
    | GetCategoriesSlugResponse404
]:
    """Get category by slug

    Args:
        slug (str):  Example: art.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCategoriesSlugResponse200 | GetCategoriesSlugResponse401 | GetCategoriesSlugResponse403 | GetCategoriesSlugResponse404]
    """

    kwargs = _get_kwargs(
        slug=slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    slug: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetCategoriesSlugResponse200
    | GetCategoriesSlugResponse401
    | GetCategoriesSlugResponse403
    | GetCategoriesSlugResponse404
    | None
):
    """Get category by slug

    Args:
        slug (str):  Example: art.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCategoriesSlugResponse200 | GetCategoriesSlugResponse401 | GetCategoriesSlugResponse403 | GetCategoriesSlugResponse404
    """

    return (
        await asyncio_detailed(
            slug=slug,
            client=client,
        )
    ).parsed
