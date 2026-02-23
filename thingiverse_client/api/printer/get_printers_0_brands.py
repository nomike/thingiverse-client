from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_printers_0_brands_response_200_item import GetPrinters0BrandsResponse200Item
from ...models.get_printers_0_brands_response_401 import GetPrinters0BrandsResponse401
from ...models.get_printers_0_brands_response_403 import GetPrinters0BrandsResponse403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include_user_defined: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_user_defined"] = include_user_defined

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/printers/0/brands",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetPrinters0BrandsResponse401
    | GetPrinters0BrandsResponse403
    | list[GetPrinters0BrandsResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetPrinters0BrandsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetPrinters0BrandsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetPrinters0BrandsResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetPrinters0BrandsResponse401
    | GetPrinters0BrandsResponse403
    | list[GetPrinters0BrandsResponse200Item]
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
    include_user_defined: bool | Unset = UNSET,
) -> Response[
    GetPrinters0BrandsResponse401
    | GetPrinters0BrandsResponse403
    | list[GetPrinters0BrandsResponse200Item]
]:
    """Get a list of all known printer brands

    Args:
        include_user_defined (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPrinters0BrandsResponse401 | GetPrinters0BrandsResponse403 | list[GetPrinters0BrandsResponse200Item]]
    """

    kwargs = _get_kwargs(
        include_user_defined=include_user_defined,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include_user_defined: bool | Unset = UNSET,
) -> (
    GetPrinters0BrandsResponse401
    | GetPrinters0BrandsResponse403
    | list[GetPrinters0BrandsResponse200Item]
    | None
):
    """Get a list of all known printer brands

    Args:
        include_user_defined (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPrinters0BrandsResponse401 | GetPrinters0BrandsResponse403 | list[GetPrinters0BrandsResponse200Item]
    """

    return sync_detailed(
        client=client,
        include_user_defined=include_user_defined,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include_user_defined: bool | Unset = UNSET,
) -> Response[
    GetPrinters0BrandsResponse401
    | GetPrinters0BrandsResponse403
    | list[GetPrinters0BrandsResponse200Item]
]:
    """Get a list of all known printer brands

    Args:
        include_user_defined (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPrinters0BrandsResponse401 | GetPrinters0BrandsResponse403 | list[GetPrinters0BrandsResponse200Item]]
    """

    kwargs = _get_kwargs(
        include_user_defined=include_user_defined,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include_user_defined: bool | Unset = UNSET,
) -> (
    GetPrinters0BrandsResponse401
    | GetPrinters0BrandsResponse403
    | list[GetPrinters0BrandsResponse200Item]
    | None
):
    """Get a list of all known printer brands

    Args:
        include_user_defined (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPrinters0BrandsResponse401 | GetPrinters0BrandsResponse403 | list[GetPrinters0BrandsResponse200Item]
    """

    return (
        await asyncio_detailed(
            client=client,
            include_user_defined=include_user_defined,
        )
    ).parsed
