from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_categoriesreturncomplete_response_200_item import (
    GetCategoriesreturncompleteResponse200Item,
)
from ...models.get_categoriesreturncomplete_response_401 import (
    GetCategoriesreturncompleteResponse401,
)
from ...models.get_categoriesreturncomplete_response_403 import (
    GetCategoriesreturncompleteResponse403,
)
from ...models.get_categoriesreturncomplete_response_404 import (
    GetCategoriesreturncompleteResponse404,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
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
        "url": "/categories?return=complete",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetCategoriesreturncompleteResponse401
    | GetCategoriesreturncompleteResponse403
    | GetCategoriesreturncompleteResponse404
    | list[GetCategoriesreturncompleteResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetCategoriesreturncompleteResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetCategoriesreturncompleteResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetCategoriesreturncompleteResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetCategoriesreturncompleteResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetCategoriesreturncompleteResponse401
    | GetCategoriesreturncompleteResponse403
    | GetCategoriesreturncompleteResponse404
    | list[GetCategoriesreturncompleteResponse200Item]
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
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[
    GetCategoriesreturncompleteResponse401
    | GetCategoriesreturncompleteResponse403
    | GetCategoriesreturncompleteResponse404
    | list[GetCategoriesreturncompleteResponse200Item]
]:
    """List of root categories and their nested children.

    Args:
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCategoriesreturncompleteResponse401 | GetCategoriesreturncompleteResponse403 | GetCategoriesreturncompleteResponse404 | list[GetCategoriesreturncompleteResponse200Item]]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> (
    GetCategoriesreturncompleteResponse401
    | GetCategoriesreturncompleteResponse403
    | GetCategoriesreturncompleteResponse404
    | list[GetCategoriesreturncompleteResponse200Item]
    | None
):
    """List of root categories and their nested children.

    Args:
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCategoriesreturncompleteResponse401 | GetCategoriesreturncompleteResponse403 | GetCategoriesreturncompleteResponse404 | list[GetCategoriesreturncompleteResponse200Item]
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[
    GetCategoriesreturncompleteResponse401
    | GetCategoriesreturncompleteResponse403
    | GetCategoriesreturncompleteResponse404
    | list[GetCategoriesreturncompleteResponse200Item]
]:
    """List of root categories and their nested children.

    Args:
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCategoriesreturncompleteResponse401 | GetCategoriesreturncompleteResponse403 | GetCategoriesreturncompleteResponse404 | list[GetCategoriesreturncompleteResponse200Item]]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> (
    GetCategoriesreturncompleteResponse401
    | GetCategoriesreturncompleteResponse403
    | GetCategoriesreturncompleteResponse404
    | list[GetCategoriesreturncompleteResponse200Item]
    | None
):
    """List of root categories and their nested children.

    Args:
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCategoriesreturncompleteResponse401 | GetCategoriesreturncompleteResponse403 | GetCategoriesreturncompleteResponse404 | list[GetCategoriesreturncompleteResponse200Item]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
        )
    ).parsed
