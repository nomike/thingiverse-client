from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_banner_0_page_ad_location import GetBanner0PageAdLocation
from ...models.get_banner_0_page_ad_response_200 import GetBanner0PageAdResponse200
from ...models.get_banner_0_page_ad_response_401 import GetBanner0PageAdResponse401
from ...models.get_banner_0_page_ad_response_403 import GetBanner0PageAdResponse403
from ...models.get_banner_0_page_ad_response_404 import GetBanner0PageAdResponse404
from ...models.get_banner_0_page_ad_type import GetBanner0PageAdType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    location: GetBanner0PageAdLocation,
    query: str | Unset = UNSET,
    category_id: int | Unset = UNSET,
    type_: GetBanner0PageAdType | Unset = UNSET,
    search: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_location = location.value
    params["location"] = json_location

    params["query"] = query

    params["category_id"] = category_id

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/banner/0/page-ad",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetBanner0PageAdResponse200
    | GetBanner0PageAdResponse401
    | GetBanner0PageAdResponse403
    | GetBanner0PageAdResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetBanner0PageAdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetBanner0PageAdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetBanner0PageAdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetBanner0PageAdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetBanner0PageAdResponse200
    | GetBanner0PageAdResponse401
    | GetBanner0PageAdResponse403
    | GetBanner0PageAdResponse404
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
    location: GetBanner0PageAdLocation,
    query: str | Unset = UNSET,
    category_id: int | Unset = UNSET,
    type_: GetBanner0PageAdType | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[
    GetBanner0PageAdResponse200
    | GetBanner0PageAdResponse401
    | GetBanner0PageAdResponse403
    | GetBanner0PageAdResponse404
]:
    """Get banner (ad) for a certain page

    Args:
        location (GetBanner0PageAdLocation):
        query (str | Unset):  Example: 3D.
        category_id (int | Unset):  Example: 63.
        type_ (GetBanner0PageAdType | Unset):
        search (str | Unset):  Example: q=test&page=1&type=things&sort=relevant.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBanner0PageAdResponse200 | GetBanner0PageAdResponse401 | GetBanner0PageAdResponse403 | GetBanner0PageAdResponse404]
    """

    kwargs = _get_kwargs(
        location=location,
        query=query,
        category_id=category_id,
        type_=type_,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    location: GetBanner0PageAdLocation,
    query: str | Unset = UNSET,
    category_id: int | Unset = UNSET,
    type_: GetBanner0PageAdType | Unset = UNSET,
    search: str | Unset = UNSET,
) -> (
    GetBanner0PageAdResponse200
    | GetBanner0PageAdResponse401
    | GetBanner0PageAdResponse403
    | GetBanner0PageAdResponse404
    | None
):
    """Get banner (ad) for a certain page

    Args:
        location (GetBanner0PageAdLocation):
        query (str | Unset):  Example: 3D.
        category_id (int | Unset):  Example: 63.
        type_ (GetBanner0PageAdType | Unset):
        search (str | Unset):  Example: q=test&page=1&type=things&sort=relevant.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBanner0PageAdResponse200 | GetBanner0PageAdResponse401 | GetBanner0PageAdResponse403 | GetBanner0PageAdResponse404
    """

    return sync_detailed(
        client=client,
        location=location,
        query=query,
        category_id=category_id,
        type_=type_,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    location: GetBanner0PageAdLocation,
    query: str | Unset = UNSET,
    category_id: int | Unset = UNSET,
    type_: GetBanner0PageAdType | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[
    GetBanner0PageAdResponse200
    | GetBanner0PageAdResponse401
    | GetBanner0PageAdResponse403
    | GetBanner0PageAdResponse404
]:
    """Get banner (ad) for a certain page

    Args:
        location (GetBanner0PageAdLocation):
        query (str | Unset):  Example: 3D.
        category_id (int | Unset):  Example: 63.
        type_ (GetBanner0PageAdType | Unset):
        search (str | Unset):  Example: q=test&page=1&type=things&sort=relevant.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBanner0PageAdResponse200 | GetBanner0PageAdResponse401 | GetBanner0PageAdResponse403 | GetBanner0PageAdResponse404]
    """

    kwargs = _get_kwargs(
        location=location,
        query=query,
        category_id=category_id,
        type_=type_,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    location: GetBanner0PageAdLocation,
    query: str | Unset = UNSET,
    category_id: int | Unset = UNSET,
    type_: GetBanner0PageAdType | Unset = UNSET,
    search: str | Unset = UNSET,
) -> (
    GetBanner0PageAdResponse200
    | GetBanner0PageAdResponse401
    | GetBanner0PageAdResponse403
    | GetBanner0PageAdResponse404
    | None
):
    """Get banner (ad) for a certain page

    Args:
        location (GetBanner0PageAdLocation):
        query (str | Unset):  Example: 3D.
        category_id (int | Unset):  Example: 63.
        type_ (GetBanner0PageAdType | Unset):
        search (str | Unset):  Example: q=test&page=1&type=things&sort=relevant.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBanner0PageAdResponse200 | GetBanner0PageAdResponse401 | GetBanner0PageAdResponse403 | GetBanner0PageAdResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            location=location,
            query=query,
            category_id=category_id,
            type_=type_,
            search=search,
        )
    ).parsed
