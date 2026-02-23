from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_categories_slug_things_response_401 import GetCategoriesSlugThingsResponse401
from ...models.get_categories_slug_things_response_403 import GetCategoriesSlugThingsResponse403
from ...models.get_categories_slug_things_response_404 import GetCategoriesSlugThingsResponse404
from ...models.thing_schema import ThingSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    slug: str,
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/categories/{slug}/things".format(
            slug=quote(str(slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetCategoriesSlugThingsResponse401
    | GetCategoriesSlugThingsResponse403
    | GetCategoriesSlugThingsResponse404
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
        response_401 = GetCategoriesSlugThingsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetCategoriesSlugThingsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetCategoriesSlugThingsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetCategoriesSlugThingsResponse401
    | GetCategoriesSlugThingsResponse403
    | GetCategoriesSlugThingsResponse404
    | list[ThingSchema]
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
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[
    GetCategoriesSlugThingsResponse401
    | GetCategoriesSlugThingsResponse403
    | GetCategoriesSlugThingsResponse404
    | list[ThingSchema]
]:
    """Get list of things of the corresponding category by slug

    Args:
        slug (str):  Example: art.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCategoriesSlugThingsResponse401 | GetCategoriesSlugThingsResponse403 | GetCategoriesSlugThingsResponse404 | list[ThingSchema]]
    """

    kwargs = _get_kwargs(
        slug=slug,
        page=page,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    slug: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> (
    GetCategoriesSlugThingsResponse401
    | GetCategoriesSlugThingsResponse403
    | GetCategoriesSlugThingsResponse404
    | list[ThingSchema]
    | None
):
    """Get list of things of the corresponding category by slug

    Args:
        slug (str):  Example: art.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCategoriesSlugThingsResponse401 | GetCategoriesSlugThingsResponse403 | GetCategoriesSlugThingsResponse404 | list[ThingSchema]
    """

    return sync_detailed(
        slug=slug,
        client=client,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    slug: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[
    GetCategoriesSlugThingsResponse401
    | GetCategoriesSlugThingsResponse403
    | GetCategoriesSlugThingsResponse404
    | list[ThingSchema]
]:
    """Get list of things of the corresponding category by slug

    Args:
        slug (str):  Example: art.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCategoriesSlugThingsResponse401 | GetCategoriesSlugThingsResponse403 | GetCategoriesSlugThingsResponse404 | list[ThingSchema]]
    """

    kwargs = _get_kwargs(
        slug=slug,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    slug: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> (
    GetCategoriesSlugThingsResponse401
    | GetCategoriesSlugThingsResponse403
    | GetCategoriesSlugThingsResponse404
    | list[ThingSchema]
    | None
):
    """Get list of things of the corresponding category by slug

    Args:
        slug (str):  Example: art.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCategoriesSlugThingsResponse401 | GetCategoriesSlugThingsResponse403 | GetCategoriesSlugThingsResponse404 | list[ThingSchema]
    """

    return (
        await asyncio_detailed(
            slug=slug,
            client=client,
            page=page,
            per_page=per_page,
        )
    ).parsed
