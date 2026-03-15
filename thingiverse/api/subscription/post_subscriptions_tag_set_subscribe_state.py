from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_subscriptions_tag_set_subscribe_state_body import (
    PostSubscriptionsTagSetSubscribeStateBody,
)
from ...models.post_subscriptions_tag_set_subscribe_state_response_401 import (
    PostSubscriptionsTagSetSubscribeStateResponse401,
)
from ...models.post_subscriptions_tag_set_subscribe_state_response_403 import (
    PostSubscriptionsTagSetSubscribeStateResponse403,
)
from ...models.post_subscriptions_tag_set_subscribe_state_response_404 import (
    PostSubscriptionsTagSetSubscribeStateResponse404,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tag: str,
    *,
    body: PostSubscriptionsTagSetSubscribeStateBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/subscriptions/{tag}/set-subscribe-state".format(
            tag=quote(str(tag), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostSubscriptionsTagSetSubscribeStateResponse401
    | PostSubscriptionsTagSetSubscribeStateResponse403
    | PostSubscriptionsTagSetSubscribeStateResponse404
    | bool
    | None
):
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
        return response_200

    if response.status_code == 401:
        response_401 = PostSubscriptionsTagSetSubscribeStateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostSubscriptionsTagSetSubscribeStateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostSubscriptionsTagSetSubscribeStateResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSubscriptionsTagSetSubscribeStateResponse401
    | PostSubscriptionsTagSetSubscribeStateResponse403
    | PostSubscriptionsTagSetSubscribeStateResponse404
    | bool
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tag: str,
    *,
    client: AuthenticatedClient,
    body: PostSubscriptionsTagSetSubscribeStateBody | Unset = UNSET,
) -> Response[
    PostSubscriptionsTagSetSubscribeStateResponse401
    | PostSubscriptionsTagSetSubscribeStateResponse403
    | PostSubscriptionsTagSetSubscribeStateResponse404
    | bool
]:
    """Subscribe a user to a tag

    Args:
        tag (str):  Example: laser.
        body (PostSubscriptionsTagSetSubscribeStateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSubscriptionsTagSetSubscribeStateResponse401 | PostSubscriptionsTagSetSubscribeStateResponse403 | PostSubscriptionsTagSetSubscribeStateResponse404 | bool]
    """

    kwargs = _get_kwargs(
        tag=tag,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tag: str,
    *,
    client: AuthenticatedClient,
    body: PostSubscriptionsTagSetSubscribeStateBody | Unset = UNSET,
) -> (
    PostSubscriptionsTagSetSubscribeStateResponse401
    | PostSubscriptionsTagSetSubscribeStateResponse403
    | PostSubscriptionsTagSetSubscribeStateResponse404
    | bool
    | None
):
    """Subscribe a user to a tag

    Args:
        tag (str):  Example: laser.
        body (PostSubscriptionsTagSetSubscribeStateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSubscriptionsTagSetSubscribeStateResponse401 | PostSubscriptionsTagSetSubscribeStateResponse403 | PostSubscriptionsTagSetSubscribeStateResponse404 | bool
    """

    return sync_detailed(
        tag=tag,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tag: str,
    *,
    client: AuthenticatedClient,
    body: PostSubscriptionsTagSetSubscribeStateBody | Unset = UNSET,
) -> Response[
    PostSubscriptionsTagSetSubscribeStateResponse401
    | PostSubscriptionsTagSetSubscribeStateResponse403
    | PostSubscriptionsTagSetSubscribeStateResponse404
    | bool
]:
    """Subscribe a user to a tag

    Args:
        tag (str):  Example: laser.
        body (PostSubscriptionsTagSetSubscribeStateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSubscriptionsTagSetSubscribeStateResponse401 | PostSubscriptionsTagSetSubscribeStateResponse403 | PostSubscriptionsTagSetSubscribeStateResponse404 | bool]
    """

    kwargs = _get_kwargs(
        tag=tag,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tag: str,
    *,
    client: AuthenticatedClient,
    body: PostSubscriptionsTagSetSubscribeStateBody | Unset = UNSET,
) -> (
    PostSubscriptionsTagSetSubscribeStateResponse401
    | PostSubscriptionsTagSetSubscribeStateResponse403
    | PostSubscriptionsTagSetSubscribeStateResponse404
    | bool
    | None
):
    """Subscribe a user to a tag

    Args:
        tag (str):  Example: laser.
        body (PostSubscriptionsTagSetSubscribeStateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSubscriptionsTagSetSubscribeStateResponse401 | PostSubscriptionsTagSetSubscribeStateResponse403 | PostSubscriptionsTagSetSubscribeStateResponse404 | bool
    """

    return (
        await asyncio_detailed(
            tag=tag,
            client=client,
            body=body,
        )
    ).parsed
