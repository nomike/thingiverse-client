from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_events_id_read_all_response_200 import PostEventsIdReadAllResponse200
from ...models.post_events_id_read_all_response_404 import PostEventsIdReadAllResponse404
from ...types import Response


def _get_kwargs(
    id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/events/{id}/read-all".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostEventsIdReadAllResponse200 | PostEventsIdReadAllResponse404 | None:
    if response.status_code == 200:
        response_200 = PostEventsIdReadAllResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = PostEventsIdReadAllResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostEventsIdReadAllResponse200 | PostEventsIdReadAllResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[PostEventsIdReadAllResponse200 | PostEventsIdReadAllResponse404]:
    """Read all subscription-events of user

    Args:
        id (int):  Example: 2858045.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostEventsIdReadAllResponse200 | PostEventsIdReadAllResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
) -> PostEventsIdReadAllResponse200 | PostEventsIdReadAllResponse404 | None:
    """Read all subscription-events of user

    Args:
        id (int):  Example: 2858045.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostEventsIdReadAllResponse200 | PostEventsIdReadAllResponse404
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[PostEventsIdReadAllResponse200 | PostEventsIdReadAllResponse404]:
    """Read all subscription-events of user

    Args:
        id (int):  Example: 2858045.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostEventsIdReadAllResponse200 | PostEventsIdReadAllResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
) -> PostEventsIdReadAllResponse200 | PostEventsIdReadAllResponse404 | None:
    """Read all subscription-events of user

    Args:
        id (int):  Example: 2858045.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostEventsIdReadAllResponse200 | PostEventsIdReadAllResponse404
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
