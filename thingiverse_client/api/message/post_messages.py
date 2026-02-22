from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_messages_body import PostMessagesBody
from ...models.post_messages_response_200 import PostMessagesResponse200
from ...models.post_messages_response_400 import PostMessagesResponse400
from ...models.post_messages_response_401 import PostMessagesResponse401
from ...models.post_messages_response_403 import PostMessagesResponse403
from ...models.post_messages_response_404 import PostMessagesResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostMessagesBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/messages",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostMessagesResponse200
    | PostMessagesResponse400
    | PostMessagesResponse401
    | PostMessagesResponse403
    | PostMessagesResponse404
    | None
):
    if response.status_code == 200:
        response_200 = PostMessagesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostMessagesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostMessagesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostMessagesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostMessagesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostMessagesResponse200
    | PostMessagesResponse400
    | PostMessagesResponse401
    | PostMessagesResponse403
    | PostMessagesResponse404
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
    body: PostMessagesBody | Unset = UNSET,
) -> Response[
    PostMessagesResponse200
    | PostMessagesResponse400
    | PostMessagesResponse401
    | PostMessagesResponse403
    | PostMessagesResponse404
]:
    """Create a new message to share a thing

    Args:
        body (PostMessagesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostMessagesResponse200 | PostMessagesResponse400 | PostMessagesResponse401 | PostMessagesResponse403 | PostMessagesResponse404]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostMessagesBody | Unset = UNSET,
) -> (
    PostMessagesResponse200
    | PostMessagesResponse400
    | PostMessagesResponse401
    | PostMessagesResponse403
    | PostMessagesResponse404
    | None
):
    """Create a new message to share a thing

    Args:
        body (PostMessagesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostMessagesResponse200 | PostMessagesResponse400 | PostMessagesResponse401 | PostMessagesResponse403 | PostMessagesResponse404
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostMessagesBody | Unset = UNSET,
) -> Response[
    PostMessagesResponse200
    | PostMessagesResponse400
    | PostMessagesResponse401
    | PostMessagesResponse403
    | PostMessagesResponse404
]:
    """Create a new message to share a thing

    Args:
        body (PostMessagesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostMessagesResponse200 | PostMessagesResponse400 | PostMessagesResponse401 | PostMessagesResponse403 | PostMessagesResponse404]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostMessagesBody | Unset = UNSET,
) -> (
    PostMessagesResponse200
    | PostMessagesResponse400
    | PostMessagesResponse401
    | PostMessagesResponse403
    | PostMessagesResponse404
    | None
):
    """Create a new message to share a thing

    Args:
        body (PostMessagesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostMessagesResponse200 | PostMessagesResponse400 | PostMessagesResponse401 | PostMessagesResponse403 | PostMessagesResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
