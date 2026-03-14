from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_email_thingiverse_enqueue_support_body import (
    PostEmailThingiverseEnqueueSupportBody,
)
from ...models.post_email_thingiverse_enqueue_support_response_401 import (
    PostEmailThingiverseEnqueueSupportResponse401,
)
from ...models.post_email_thingiverse_enqueue_support_response_403 import (
    PostEmailThingiverseEnqueueSupportResponse403,
)
from ...models.post_email_thingiverse_enqueue_support_response_404 import (
    PostEmailThingiverseEnqueueSupportResponse404,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostEmailThingiverseEnqueueSupportBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/email/thingiverse/enqueue-support",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostEmailThingiverseEnqueueSupportResponse401
    | PostEmailThingiverseEnqueueSupportResponse403
    | PostEmailThingiverseEnqueueSupportResponse404
    | None
):
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 401:
        response_401 = PostEmailThingiverseEnqueueSupportResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostEmailThingiverseEnqueueSupportResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostEmailThingiverseEnqueueSupportResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostEmailThingiverseEnqueueSupportResponse401
    | PostEmailThingiverseEnqueueSupportResponse403
    | PostEmailThingiverseEnqueueSupportResponse404
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
    body: PostEmailThingiverseEnqueueSupportBody | Unset = UNSET,
) -> Response[
    Any
    | PostEmailThingiverseEnqueueSupportResponse401
    | PostEmailThingiverseEnqueueSupportResponse403
    | PostEmailThingiverseEnqueueSupportResponse404
]:
    """Queue email to Thingiverse support

    Args:
        body (PostEmailThingiverseEnqueueSupportBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostEmailThingiverseEnqueueSupportResponse401 | PostEmailThingiverseEnqueueSupportResponse403 | PostEmailThingiverseEnqueueSupportResponse404]
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
    body: PostEmailThingiverseEnqueueSupportBody | Unset = UNSET,
) -> (
    Any
    | PostEmailThingiverseEnqueueSupportResponse401
    | PostEmailThingiverseEnqueueSupportResponse403
    | PostEmailThingiverseEnqueueSupportResponse404
    | None
):
    """Queue email to Thingiverse support

    Args:
        body (PostEmailThingiverseEnqueueSupportBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostEmailThingiverseEnqueueSupportResponse401 | PostEmailThingiverseEnqueueSupportResponse403 | PostEmailThingiverseEnqueueSupportResponse404
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostEmailThingiverseEnqueueSupportBody | Unset = UNSET,
) -> Response[
    Any
    | PostEmailThingiverseEnqueueSupportResponse401
    | PostEmailThingiverseEnqueueSupportResponse403
    | PostEmailThingiverseEnqueueSupportResponse404
]:
    """Queue email to Thingiverse support

    Args:
        body (PostEmailThingiverseEnqueueSupportBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostEmailThingiverseEnqueueSupportResponse401 | PostEmailThingiverseEnqueueSupportResponse403 | PostEmailThingiverseEnqueueSupportResponse404]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostEmailThingiverseEnqueueSupportBody | Unset = UNSET,
) -> (
    Any
    | PostEmailThingiverseEnqueueSupportResponse401
    | PostEmailThingiverseEnqueueSupportResponse403
    | PostEmailThingiverseEnqueueSupportResponse404
    | None
):
    """Queue email to Thingiverse support

    Args:
        body (PostEmailThingiverseEnqueueSupportBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostEmailThingiverseEnqueueSupportResponse401 | PostEmailThingiverseEnqueueSupportResponse403 | PostEmailThingiverseEnqueueSupportResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
