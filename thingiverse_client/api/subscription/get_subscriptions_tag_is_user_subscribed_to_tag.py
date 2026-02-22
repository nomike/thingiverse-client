from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_subscriptions_tag_is_user_subscribed_to_tag_response_401 import (
    GetSubscriptionsTagIsUserSubscribedToTagResponse401,
)
from ...models.get_subscriptions_tag_is_user_subscribed_to_tag_response_403 import (
    GetSubscriptionsTagIsUserSubscribedToTagResponse403,
)
from ...models.get_subscriptions_tag_is_user_subscribed_to_tag_response_404 import (
    GetSubscriptionsTagIsUserSubscribedToTagResponse404,
)
from ...types import Response


def _get_kwargs(
    tag: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/subscriptions/{tag}/is-user-subscribed-to-tag".format(
            tag=quote(str(tag), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSubscriptionsTagIsUserSubscribedToTagResponse401
    | GetSubscriptionsTagIsUserSubscribedToTagResponse403
    | GetSubscriptionsTagIsUserSubscribedToTagResponse404
    | bool
    | None
):
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
        return response_200

    if response.status_code == 401:
        response_401 = GetSubscriptionsTagIsUserSubscribedToTagResponse401.from_dict(
            response.json()
        )

        return response_401

    if response.status_code == 403:
        response_403 = GetSubscriptionsTagIsUserSubscribedToTagResponse403.from_dict(
            response.json()
        )

        return response_403

    if response.status_code == 404:
        response_404 = GetSubscriptionsTagIsUserSubscribedToTagResponse404.from_dict(
            response.json()
        )

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSubscriptionsTagIsUserSubscribedToTagResponse401
    | GetSubscriptionsTagIsUserSubscribedToTagResponse403
    | GetSubscriptionsTagIsUserSubscribedToTagResponse404
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
) -> Response[
    GetSubscriptionsTagIsUserSubscribedToTagResponse401
    | GetSubscriptionsTagIsUserSubscribedToTagResponse403
    | GetSubscriptionsTagIsUserSubscribedToTagResponse404
    | bool
]:
    """Check if user is subscribed to the tag

    Args:
        tag (str):  Example: laser.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSubscriptionsTagIsUserSubscribedToTagResponse401 | GetSubscriptionsTagIsUserSubscribedToTagResponse403 | GetSubscriptionsTagIsUserSubscribedToTagResponse404 | bool]
    """

    kwargs = _get_kwargs(
        tag=tag,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tag: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetSubscriptionsTagIsUserSubscribedToTagResponse401
    | GetSubscriptionsTagIsUserSubscribedToTagResponse403
    | GetSubscriptionsTagIsUserSubscribedToTagResponse404
    | bool
    | None
):
    """Check if user is subscribed to the tag

    Args:
        tag (str):  Example: laser.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSubscriptionsTagIsUserSubscribedToTagResponse401 | GetSubscriptionsTagIsUserSubscribedToTagResponse403 | GetSubscriptionsTagIsUserSubscribedToTagResponse404 | bool
    """

    return sync_detailed(
        tag=tag,
        client=client,
    ).parsed


async def asyncio_detailed(
    tag: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetSubscriptionsTagIsUserSubscribedToTagResponse401
    | GetSubscriptionsTagIsUserSubscribedToTagResponse403
    | GetSubscriptionsTagIsUserSubscribedToTagResponse404
    | bool
]:
    """Check if user is subscribed to the tag

    Args:
        tag (str):  Example: laser.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSubscriptionsTagIsUserSubscribedToTagResponse401 | GetSubscriptionsTagIsUserSubscribedToTagResponse403 | GetSubscriptionsTagIsUserSubscribedToTagResponse404 | bool]
    """

    kwargs = _get_kwargs(
        tag=tag,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tag: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetSubscriptionsTagIsUserSubscribedToTagResponse401
    | GetSubscriptionsTagIsUserSubscribedToTagResponse403
    | GetSubscriptionsTagIsUserSubscribedToTagResponse404
    | bool
    | None
):
    """Check if user is subscribed to the tag

    Args:
        tag (str):  Example: laser.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSubscriptionsTagIsUserSubscribedToTagResponse401 | GetSubscriptionsTagIsUserSubscribedToTagResponse403 | GetSubscriptionsTagIsUserSubscribedToTagResponse404 | bool
    """

    return (
        await asyncio_detailed(
            tag=tag,
            client=client,
        )
    ).parsed
