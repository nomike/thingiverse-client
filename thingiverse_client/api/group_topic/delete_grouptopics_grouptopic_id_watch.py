from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_grouptopics_grouptopic_id_watch_response_401 import (
    DeleteGrouptopicsGrouptopicIdWatchResponse401,
)
from ...models.delete_grouptopics_grouptopic_id_watch_response_403 import (
    DeleteGrouptopicsGrouptopicIdWatchResponse403,
)
from ...models.delete_grouptopics_grouptopic_id_watch_response_404 import (
    DeleteGrouptopicsGrouptopicIdWatchResponse404,
)
from ...models.topic_schema import TopicSchema
from ...types import Response


def _get_kwargs(
    grouptopic_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/grouptopics/{grouptopic_id}/watch".format(
            grouptopic_id=quote(str(grouptopic_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteGrouptopicsGrouptopicIdWatchResponse401
    | DeleteGrouptopicsGrouptopicIdWatchResponse403
    | DeleteGrouptopicsGrouptopicIdWatchResponse404
    | TopicSchema
    | None
):
    if response.status_code == 200:
        response_200 = TopicSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = DeleteGrouptopicsGrouptopicIdWatchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteGrouptopicsGrouptopicIdWatchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteGrouptopicsGrouptopicIdWatchResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteGrouptopicsGrouptopicIdWatchResponse401
    | DeleteGrouptopicsGrouptopicIdWatchResponse403
    | DeleteGrouptopicsGrouptopicIdWatchResponse404
    | TopicSchema
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
    DeleteGrouptopicsGrouptopicIdWatchResponse401
    | DeleteGrouptopicsGrouptopicIdWatchResponse403
    | DeleteGrouptopicsGrouptopicIdWatchResponse404
    | TopicSchema
]:
    """Unwatch the group topic

    Args:
        grouptopic_id (int):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteGrouptopicsGrouptopicIdWatchResponse401 | DeleteGrouptopicsGrouptopicIdWatchResponse403 | DeleteGrouptopicsGrouptopicIdWatchResponse404 | TopicSchema]
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
    DeleteGrouptopicsGrouptopicIdWatchResponse401
    | DeleteGrouptopicsGrouptopicIdWatchResponse403
    | DeleteGrouptopicsGrouptopicIdWatchResponse404
    | TopicSchema
    | None
):
    """Unwatch the group topic

    Args:
        grouptopic_id (int):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteGrouptopicsGrouptopicIdWatchResponse401 | DeleteGrouptopicsGrouptopicIdWatchResponse403 | DeleteGrouptopicsGrouptopicIdWatchResponse404 | TopicSchema
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
    DeleteGrouptopicsGrouptopicIdWatchResponse401
    | DeleteGrouptopicsGrouptopicIdWatchResponse403
    | DeleteGrouptopicsGrouptopicIdWatchResponse404
    | TopicSchema
]:
    """Unwatch the group topic

    Args:
        grouptopic_id (int):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteGrouptopicsGrouptopicIdWatchResponse401 | DeleteGrouptopicsGrouptopicIdWatchResponse403 | DeleteGrouptopicsGrouptopicIdWatchResponse404 | TopicSchema]
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
    DeleteGrouptopicsGrouptopicIdWatchResponse401
    | DeleteGrouptopicsGrouptopicIdWatchResponse403
    | DeleteGrouptopicsGrouptopicIdWatchResponse404
    | TopicSchema
    | None
):
    """Unwatch the group topic

    Args:
        grouptopic_id (int):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteGrouptopicsGrouptopicIdWatchResponse401 | DeleteGrouptopicsGrouptopicIdWatchResponse403 | DeleteGrouptopicsGrouptopicIdWatchResponse404 | TopicSchema
    """

    return (
        await asyncio_detailed(
            grouptopic_id=grouptopic_id,
            client=client,
        )
    ).parsed
