from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_grouptopics_grouptopic_id_response_401 import (
    GetGrouptopicsGrouptopicIdResponse401,
)
from ...models.get_grouptopics_grouptopic_id_response_403 import (
    GetGrouptopicsGrouptopicIdResponse403,
)
from ...models.get_grouptopics_grouptopic_id_response_404 import (
    GetGrouptopicsGrouptopicIdResponse404,
)
from ...models.grouptopic_schema import GrouptopicSchema
from ...types import Response


def _get_kwargs(
    grouptopic_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/grouptopics/{grouptopic_id}/".format(
            grouptopic_id=quote(str(grouptopic_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetGrouptopicsGrouptopicIdResponse401
    | GetGrouptopicsGrouptopicIdResponse403
    | GetGrouptopicsGrouptopicIdResponse404
    | GrouptopicSchema
    | None
):
    if response.status_code == 200:
        response_200 = GrouptopicSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetGrouptopicsGrouptopicIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetGrouptopicsGrouptopicIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetGrouptopicsGrouptopicIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetGrouptopicsGrouptopicIdResponse401
    | GetGrouptopicsGrouptopicIdResponse403
    | GetGrouptopicsGrouptopicIdResponse404
    | GrouptopicSchema
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
    GetGrouptopicsGrouptopicIdResponse401
    | GetGrouptopicsGrouptopicIdResponse403
    | GetGrouptopicsGrouptopicIdResponse404
    | GrouptopicSchema
]:
    """Get a group topic by id

    Args:
        grouptopic_id (int):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGrouptopicsGrouptopicIdResponse401 | GetGrouptopicsGrouptopicIdResponse403 | GetGrouptopicsGrouptopicIdResponse404 | GrouptopicSchema]
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
    GetGrouptopicsGrouptopicIdResponse401
    | GetGrouptopicsGrouptopicIdResponse403
    | GetGrouptopicsGrouptopicIdResponse404
    | GrouptopicSchema
    | None
):
    """Get a group topic by id

    Args:
        grouptopic_id (int):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGrouptopicsGrouptopicIdResponse401 | GetGrouptopicsGrouptopicIdResponse403 | GetGrouptopicsGrouptopicIdResponse404 | GrouptopicSchema
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
    GetGrouptopicsGrouptopicIdResponse401
    | GetGrouptopicsGrouptopicIdResponse403
    | GetGrouptopicsGrouptopicIdResponse404
    | GrouptopicSchema
]:
    """Get a group topic by id

    Args:
        grouptopic_id (int):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGrouptopicsGrouptopicIdResponse401 | GetGrouptopicsGrouptopicIdResponse403 | GetGrouptopicsGrouptopicIdResponse404 | GrouptopicSchema]
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
    GetGrouptopicsGrouptopicIdResponse401
    | GetGrouptopicsGrouptopicIdResponse403
    | GetGrouptopicsGrouptopicIdResponse404
    | GrouptopicSchema
    | None
):
    """Get a group topic by id

    Args:
        grouptopic_id (int):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGrouptopicsGrouptopicIdResponse401 | GetGrouptopicsGrouptopicIdResponse403 | GetGrouptopicsGrouptopicIdResponse404 | GrouptopicSchema
    """

    return (
        await asyncio_detailed(
            grouptopic_id=grouptopic_id,
            client=client,
        )
    ).parsed
