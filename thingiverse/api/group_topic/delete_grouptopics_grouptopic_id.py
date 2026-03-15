from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_grouptopics_grouptopic_id_response_401 import (
    DeleteGrouptopicsGrouptopicIdResponse401,
)
from ...models.delete_grouptopics_grouptopic_id_response_403 import (
    DeleteGrouptopicsGrouptopicIdResponse403,
)
from ...models.delete_grouptopics_grouptopic_id_response_404 import (
    DeleteGrouptopicsGrouptopicIdResponse404,
)
from ...types import Response


def _get_kwargs(
    grouptopic_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/grouptopics/{grouptopic_id}/".format(
            grouptopic_id=quote(str(grouptopic_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteGrouptopicsGrouptopicIdResponse401
    | DeleteGrouptopicsGrouptopicIdResponse403
    | DeleteGrouptopicsGrouptopicIdResponse404
    | int
    | None
):
    if response.status_code == 200:
        response_200 = cast(int, response.json())
        return response_200

    if response.status_code == 401:
        response_401 = DeleteGrouptopicsGrouptopicIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteGrouptopicsGrouptopicIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteGrouptopicsGrouptopicIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteGrouptopicsGrouptopicIdResponse401
    | DeleteGrouptopicsGrouptopicIdResponse403
    | DeleteGrouptopicsGrouptopicIdResponse404
    | int
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
) -> Response[
    DeleteGrouptopicsGrouptopicIdResponse401
    | DeleteGrouptopicsGrouptopicIdResponse403
    | DeleteGrouptopicsGrouptopicIdResponse404
    | int
]:
    """Delete Group Topic by id

    Args:
        grouptopic_id (int):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteGrouptopicsGrouptopicIdResponse401 | DeleteGrouptopicsGrouptopicIdResponse403 | DeleteGrouptopicsGrouptopicIdResponse404 | int]
    """

    kwargs = _get_kwargs(
        grouptopic_id=grouptopic_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    grouptopic_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    DeleteGrouptopicsGrouptopicIdResponse401
    | DeleteGrouptopicsGrouptopicIdResponse403
    | DeleteGrouptopicsGrouptopicIdResponse404
    | int
    | None
):
    """Delete Group Topic by id

    Args:
        grouptopic_id (int):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteGrouptopicsGrouptopicIdResponse401 | DeleteGrouptopicsGrouptopicIdResponse403 | DeleteGrouptopicsGrouptopicIdResponse404 | int
    """

    return sync_detailed(
        grouptopic_id=grouptopic_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    grouptopic_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    DeleteGrouptopicsGrouptopicIdResponse401
    | DeleteGrouptopicsGrouptopicIdResponse403
    | DeleteGrouptopicsGrouptopicIdResponse404
    | int
]:
    """Delete Group Topic by id

    Args:
        grouptopic_id (int):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteGrouptopicsGrouptopicIdResponse401 | DeleteGrouptopicsGrouptopicIdResponse403 | DeleteGrouptopicsGrouptopicIdResponse404 | int]
    """

    kwargs = _get_kwargs(
        grouptopic_id=grouptopic_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    grouptopic_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    DeleteGrouptopicsGrouptopicIdResponse401
    | DeleteGrouptopicsGrouptopicIdResponse403
    | DeleteGrouptopicsGrouptopicIdResponse404
    | int
    | None
):
    """Delete Group Topic by id

    Args:
        grouptopic_id (int):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteGrouptopicsGrouptopicIdResponse401 | DeleteGrouptopicsGrouptopicIdResponse403 | DeleteGrouptopicsGrouptopicIdResponse404 | int
    """

    return (
        await asyncio_detailed(
            grouptopic_id=grouptopic_id,
            client=client,
        )
    ).parsed
