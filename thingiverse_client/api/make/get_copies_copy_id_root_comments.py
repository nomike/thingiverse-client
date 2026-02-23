from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_copies_copy_id_root_comments_response_401 import (
    GetCopiesCopyIdRootCommentsResponse401,
)
from ...models.get_copies_copy_id_root_comments_response_403 import (
    GetCopiesCopyIdRootCommentsResponse403,
)
from ...models.get_copies_copy_id_root_comments_response_404 import (
    GetCopiesCopyIdRootCommentsResponse404,
)
from ...models.make_comment_schema import MakeCommentSchema
from ...types import Response


def _get_kwargs(
    copy_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/copies/{copy_id}/root-comments".format(
            copy_id=quote(str(copy_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetCopiesCopyIdRootCommentsResponse401
    | GetCopiesCopyIdRootCommentsResponse403
    | GetCopiesCopyIdRootCommentsResponse404
    | list[MakeCommentSchema]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = MakeCommentSchema.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetCopiesCopyIdRootCommentsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetCopiesCopyIdRootCommentsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetCopiesCopyIdRootCommentsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetCopiesCopyIdRootCommentsResponse401
    | GetCopiesCopyIdRootCommentsResponse403
    | GetCopiesCopyIdRootCommentsResponse404
    | list[MakeCommentSchema]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    copy_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetCopiesCopyIdRootCommentsResponse401
    | GetCopiesCopyIdRootCommentsResponse403
    | GetCopiesCopyIdRootCommentsResponse404
    | list[MakeCommentSchema]
]:
    """Get an unthreaded paginated list of root comment objects

    Args:
        copy_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCopiesCopyIdRootCommentsResponse401 | GetCopiesCopyIdRootCommentsResponse403 | GetCopiesCopyIdRootCommentsResponse404 | list[MakeCommentSchema]]
    """

    kwargs = _get_kwargs(
        copy_id=copy_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    copy_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    GetCopiesCopyIdRootCommentsResponse401
    | GetCopiesCopyIdRootCommentsResponse403
    | GetCopiesCopyIdRootCommentsResponse404
    | list[MakeCommentSchema]
    | None
):
    """Get an unthreaded paginated list of root comment objects

    Args:
        copy_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCopiesCopyIdRootCommentsResponse401 | GetCopiesCopyIdRootCommentsResponse403 | GetCopiesCopyIdRootCommentsResponse404 | list[MakeCommentSchema]
    """

    return sync_detailed(
        copy_id=copy_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    copy_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetCopiesCopyIdRootCommentsResponse401
    | GetCopiesCopyIdRootCommentsResponse403
    | GetCopiesCopyIdRootCommentsResponse404
    | list[MakeCommentSchema]
]:
    """Get an unthreaded paginated list of root comment objects

    Args:
        copy_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCopiesCopyIdRootCommentsResponse401 | GetCopiesCopyIdRootCommentsResponse403 | GetCopiesCopyIdRootCommentsResponse404 | list[MakeCommentSchema]]
    """

    kwargs = _get_kwargs(
        copy_id=copy_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    copy_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    GetCopiesCopyIdRootCommentsResponse401
    | GetCopiesCopyIdRootCommentsResponse403
    | GetCopiesCopyIdRootCommentsResponse404
    | list[MakeCommentSchema]
    | None
):
    """Get an unthreaded paginated list of root comment objects

    Args:
        copy_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCopiesCopyIdRootCommentsResponse401 | GetCopiesCopyIdRootCommentsResponse403 | GetCopiesCopyIdRootCommentsResponse404 | list[MakeCommentSchema]
    """

    return (
        await asyncio_detailed(
            copy_id=copy_id,
            client=client,
        )
    ).parsed
