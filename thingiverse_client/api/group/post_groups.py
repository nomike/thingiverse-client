from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.group_schema import GroupSchema
from ...models.post_groups_body import PostGroupsBody
from ...models.post_groups_response_401 import PostGroupsResponse401
from ...models.post_groups_response_403 import PostGroupsResponse403
from ...models.post_groups_response_404 import PostGroupsResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostGroupsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/groups/",
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GroupSchema | PostGroupsResponse401 | PostGroupsResponse403 | PostGroupsResponse404 | None:
    if response.status_code == 200:
        response_200 = GroupSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostGroupsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostGroupsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostGroupsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GroupSchema | PostGroupsResponse401 | PostGroupsResponse403 | PostGroupsResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostGroupsBody | Unset = UNSET,
) -> Response[GroupSchema | PostGroupsResponse401 | PostGroupsResponse403 | PostGroupsResponse404]:
    """Create a new group

    Args:
        body (PostGroupsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GroupSchema | PostGroupsResponse401 | PostGroupsResponse403 | PostGroupsResponse404]
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
    body: PostGroupsBody | Unset = UNSET,
) -> GroupSchema | PostGroupsResponse401 | PostGroupsResponse403 | PostGroupsResponse404 | None:
    """Create a new group

    Args:
        body (PostGroupsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GroupSchema | PostGroupsResponse401 | PostGroupsResponse403 | PostGroupsResponse404
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostGroupsBody | Unset = UNSET,
) -> Response[GroupSchema | PostGroupsResponse401 | PostGroupsResponse403 | PostGroupsResponse404]:
    """Create a new group

    Args:
        body (PostGroupsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GroupSchema | PostGroupsResponse401 | PostGroupsResponse403 | PostGroupsResponse404]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostGroupsBody | Unset = UNSET,
) -> GroupSchema | PostGroupsResponse401 | PostGroupsResponse403 | PostGroupsResponse404 | None:
    """Create a new group

    Args:
        body (PostGroupsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GroupSchema | PostGroupsResponse401 | PostGroupsResponse403 | PostGroupsResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
