from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.copy_schema import CopySchema
from ...models.get_copies_copy_id_response_401 import GetCopiesCopyIdResponse401
from ...models.get_copies_copy_id_response_403 import GetCopiesCopyIdResponse403
from ...models.get_copies_copy_id_response_404 import GetCopiesCopyIdResponse404
from ...types import Response


def _get_kwargs(
    copy_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/copies/{copy_id}/".format(
            copy_id=quote(str(copy_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CopySchema
    | GetCopiesCopyIdResponse401
    | GetCopiesCopyIdResponse403
    | GetCopiesCopyIdResponse404
    | None
):
    if response.status_code == 200:
        response_200 = CopySchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetCopiesCopyIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetCopiesCopyIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetCopiesCopyIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CopySchema
    | GetCopiesCopyIdResponse401
    | GetCopiesCopyIdResponse403
    | GetCopiesCopyIdResponse404
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
    CopySchema
    | GetCopiesCopyIdResponse401
    | GetCopiesCopyIdResponse403
    | GetCopiesCopyIdResponse404
]:
    """Get make (copy) by id

    Args:
        copy_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CopySchema | GetCopiesCopyIdResponse401 | GetCopiesCopyIdResponse403 | GetCopiesCopyIdResponse404]
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
    CopySchema
    | GetCopiesCopyIdResponse401
    | GetCopiesCopyIdResponse403
    | GetCopiesCopyIdResponse404
    | None
):
    """Get make (copy) by id

    Args:
        copy_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CopySchema | GetCopiesCopyIdResponse401 | GetCopiesCopyIdResponse403 | GetCopiesCopyIdResponse404
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
    CopySchema
    | GetCopiesCopyIdResponse401
    | GetCopiesCopyIdResponse403
    | GetCopiesCopyIdResponse404
]:
    """Get make (copy) by id

    Args:
        copy_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CopySchema | GetCopiesCopyIdResponse401 | GetCopiesCopyIdResponse403 | GetCopiesCopyIdResponse404]
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
    CopySchema
    | GetCopiesCopyIdResponse401
    | GetCopiesCopyIdResponse403
    | GetCopiesCopyIdResponse404
    | None
):
    """Get make (copy) by id

    Args:
        copy_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CopySchema | GetCopiesCopyIdResponse401 | GetCopiesCopyIdResponse403 | GetCopiesCopyIdResponse404
    """

    return (
        await asyncio_detailed(
            copy_id=copy_id,
            client=client,
        )
    ).parsed
