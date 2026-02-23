from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_search_term_typemakes_response_200 import GetSearchTermTypemakesResponse200
from ...models.get_search_term_typemakes_response_401 import GetSearchTermTypemakesResponse401
from ...models.get_search_term_typemakes_response_403 import GetSearchTermTypemakesResponse403
from ...models.get_search_term_typemakes_response_404 import GetSearchTermTypemakesResponse404
from ...models.get_search_term_typemakes_sort import GetSearchTermTypemakesSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    term: str,
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: GetSearchTermTypemakesSort | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["user_id"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/search/{term}/?type=makes".format(
            term=quote(str(term), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSearchTermTypemakesResponse200
    | GetSearchTermTypemakesResponse401
    | GetSearchTermTypemakesResponse403
    | GetSearchTermTypemakesResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetSearchTermTypemakesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetSearchTermTypemakesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetSearchTermTypemakesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSearchTermTypemakesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSearchTermTypemakesResponse200
    | GetSearchTermTypemakesResponse401
    | GetSearchTermTypemakesResponse403
    | GetSearchTermTypemakesResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    term: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: GetSearchTermTypemakesSort | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> Response[
    GetSearchTermTypemakesResponse200
    | GetSearchTermTypemakesResponse401
    | GetSearchTermTypemakesResponse403
    | GetSearchTermTypemakesResponse404
]:
    """Search for Makes

    Args:
        term (str):  Example: test.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.
        sort (GetSearchTermTypemakesSort | Unset):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSearchTermTypemakesResponse200 | GetSearchTermTypemakesResponse401 | GetSearchTermTypemakesResponse403 | GetSearchTermTypemakesResponse404]
    """

    kwargs = _get_kwargs(
        term=term,
        page=page,
        per_page=per_page,
        sort=sort,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: GetSearchTermTypemakesSort | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> (
    GetSearchTermTypemakesResponse200
    | GetSearchTermTypemakesResponse401
    | GetSearchTermTypemakesResponse403
    | GetSearchTermTypemakesResponse404
    | None
):
    """Search for Makes

    Args:
        term (str):  Example: test.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.
        sort (GetSearchTermTypemakesSort | Unset):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSearchTermTypemakesResponse200 | GetSearchTermTypemakesResponse401 | GetSearchTermTypemakesResponse403 | GetSearchTermTypemakesResponse404
    """

    return sync_detailed(
        term=term,
        client=client,
        page=page,
        per_page=per_page,
        sort=sort,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    term: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: GetSearchTermTypemakesSort | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> Response[
    GetSearchTermTypemakesResponse200
    | GetSearchTermTypemakesResponse401
    | GetSearchTermTypemakesResponse403
    | GetSearchTermTypemakesResponse404
]:
    """Search for Makes

    Args:
        term (str):  Example: test.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.
        sort (GetSearchTermTypemakesSort | Unset):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSearchTermTypemakesResponse200 | GetSearchTermTypemakesResponse401 | GetSearchTermTypemakesResponse403 | GetSearchTermTypemakesResponse404]
    """

    kwargs = _get_kwargs(
        term=term,
        page=page,
        per_page=per_page,
        sort=sort,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: GetSearchTermTypemakesSort | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> (
    GetSearchTermTypemakesResponse200
    | GetSearchTermTypemakesResponse401
    | GetSearchTermTypemakesResponse403
    | GetSearchTermTypemakesResponse404
    | None
):
    """Search for Makes

    Args:
        term (str):  Example: test.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.
        sort (GetSearchTermTypemakesSort | Unset):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSearchTermTypemakesResponse200 | GetSearchTermTypemakesResponse401 | GetSearchTermTypemakesResponse403 | GetSearchTermTypemakesResponse404
    """

    return (
        await asyncio_detailed(
            term=term,
            client=client,
            page=page,
            per_page=per_page,
            sort=sort,
            user_id=user_id,
        )
    ).parsed
