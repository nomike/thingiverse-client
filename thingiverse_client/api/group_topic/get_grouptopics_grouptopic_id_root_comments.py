from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_grouptopics_grouptopic_id_root_comments_response_200_item import (
    GetGrouptopicsGrouptopicIdRootCommentsResponse200Item,
)
from ...models.get_grouptopics_grouptopic_id_root_comments_response_401 import (
    GetGrouptopicsGrouptopicIdRootCommentsResponse401,
)
from ...models.get_grouptopics_grouptopic_id_root_comments_response_403 import (
    GetGrouptopicsGrouptopicIdRootCommentsResponse403,
)
from ...models.get_grouptopics_grouptopic_id_root_comments_response_404 import (
    GetGrouptopicsGrouptopicIdRootCommentsResponse404,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    grouptopic_id: int,
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
        "url": "/grouptopics/{grouptopic_id}/root-comments".format(
            grouptopic_id=quote(str(grouptopic_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetGrouptopicsGrouptopicIdRootCommentsResponse401
    | GetGrouptopicsGrouptopicIdRootCommentsResponse403
    | GetGrouptopicsGrouptopicIdRootCommentsResponse404
    | list[GetGrouptopicsGrouptopicIdRootCommentsResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetGrouptopicsGrouptopicIdRootCommentsResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetGrouptopicsGrouptopicIdRootCommentsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetGrouptopicsGrouptopicIdRootCommentsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetGrouptopicsGrouptopicIdRootCommentsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetGrouptopicsGrouptopicIdRootCommentsResponse401
    | GetGrouptopicsGrouptopicIdRootCommentsResponse403
    | GetGrouptopicsGrouptopicIdRootCommentsResponse404
    | list[GetGrouptopicsGrouptopicIdRootCommentsResponse200Item]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    grouptopic_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[
    GetGrouptopicsGrouptopicIdRootCommentsResponse401
    | GetGrouptopicsGrouptopicIdRootCommentsResponse403
    | GetGrouptopicsGrouptopicIdRootCommentsResponse404
    | list[GetGrouptopicsGrouptopicIdRootCommentsResponse200Item]
]:
    """Get an unthreaded paginated list of root comment objects

    Args:
        grouptopic_id (int):  Example: 2.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGrouptopicsGrouptopicIdRootCommentsResponse401 | GetGrouptopicsGrouptopicIdRootCommentsResponse403 | GetGrouptopicsGrouptopicIdRootCommentsResponse404 | list[GetGrouptopicsGrouptopicIdRootCommentsResponse200Item]]
    """

    kwargs = _get_kwargs(
        grouptopic_id=grouptopic_id,
        page=page,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    grouptopic_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> (
    GetGrouptopicsGrouptopicIdRootCommentsResponse401
    | GetGrouptopicsGrouptopicIdRootCommentsResponse403
    | GetGrouptopicsGrouptopicIdRootCommentsResponse404
    | list[GetGrouptopicsGrouptopicIdRootCommentsResponse200Item]
    | None
):
    """Get an unthreaded paginated list of root comment objects

    Args:
        grouptopic_id (int):  Example: 2.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGrouptopicsGrouptopicIdRootCommentsResponse401 | GetGrouptopicsGrouptopicIdRootCommentsResponse403 | GetGrouptopicsGrouptopicIdRootCommentsResponse404 | list[GetGrouptopicsGrouptopicIdRootCommentsResponse200Item]
    """

    return sync_detailed(
        grouptopic_id=grouptopic_id,
        client=client,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    grouptopic_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[
    GetGrouptopicsGrouptopicIdRootCommentsResponse401
    | GetGrouptopicsGrouptopicIdRootCommentsResponse403
    | GetGrouptopicsGrouptopicIdRootCommentsResponse404
    | list[GetGrouptopicsGrouptopicIdRootCommentsResponse200Item]
]:
    """Get an unthreaded paginated list of root comment objects

    Args:
        grouptopic_id (int):  Example: 2.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGrouptopicsGrouptopicIdRootCommentsResponse401 | GetGrouptopicsGrouptopicIdRootCommentsResponse403 | GetGrouptopicsGrouptopicIdRootCommentsResponse404 | list[GetGrouptopicsGrouptopicIdRootCommentsResponse200Item]]
    """

    kwargs = _get_kwargs(
        grouptopic_id=grouptopic_id,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    grouptopic_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> (
    GetGrouptopicsGrouptopicIdRootCommentsResponse401
    | GetGrouptopicsGrouptopicIdRootCommentsResponse403
    | GetGrouptopicsGrouptopicIdRootCommentsResponse404
    | list[GetGrouptopicsGrouptopicIdRootCommentsResponse200Item]
    | None
):
    """Get an unthreaded paginated list of root comment objects

    Args:
        grouptopic_id (int):  Example: 2.
        page (int | Unset):  Example: 1.
        per_page (int | Unset):  Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGrouptopicsGrouptopicIdRootCommentsResponse401 | GetGrouptopicsGrouptopicIdRootCommentsResponse403 | GetGrouptopicsGrouptopicIdRootCommentsResponse404 | list[GetGrouptopicsGrouptopicIdRootCommentsResponse200Item]
    """

    return (
        await asyncio_detailed(
            grouptopic_id=grouptopic_id,
            client=client,
            page=page,
            per_page=per_page,
        )
    ).parsed
