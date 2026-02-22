from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_groups_group_id_image_body import PostGroupsGroupIdImageBody
from ...models.post_groups_group_id_image_response_200 import PostGroupsGroupIdImageResponse200
from ...models.post_groups_group_id_image_response_401 import PostGroupsGroupIdImageResponse401
from ...models.post_groups_group_id_image_response_403 import PostGroupsGroupIdImageResponse403
from ...models.post_groups_group_id_image_response_404 import PostGroupsGroupIdImageResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    body: PostGroupsGroupIdImageBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/groups/{group_id}/image".format(
            group_id=quote(str(group_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostGroupsGroupIdImageResponse200
    | PostGroupsGroupIdImageResponse401
    | PostGroupsGroupIdImageResponse403
    | PostGroupsGroupIdImageResponse404
    | None
):
    if response.status_code == 200:
        response_200 = PostGroupsGroupIdImageResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostGroupsGroupIdImageResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostGroupsGroupIdImageResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostGroupsGroupIdImageResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostGroupsGroupIdImageResponse200
    | PostGroupsGroupIdImageResponse401
    | PostGroupsGroupIdImageResponse403
    | PostGroupsGroupIdImageResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: PostGroupsGroupIdImageBody | Unset = UNSET,
) -> Response[
    PostGroupsGroupIdImageResponse200
    | PostGroupsGroupIdImageResponse401
    | PostGroupsGroupIdImageResponse403
    | PostGroupsGroupIdImageResponse404
]:
    """Upload a new image of group

    Args:
        group_id (int):  Example: 25.
        body (PostGroupsGroupIdImageBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostGroupsGroupIdImageResponse200 | PostGroupsGroupIdImageResponse401 | PostGroupsGroupIdImageResponse403 | PostGroupsGroupIdImageResponse404]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: PostGroupsGroupIdImageBody | Unset = UNSET,
) -> (
    PostGroupsGroupIdImageResponse200
    | PostGroupsGroupIdImageResponse401
    | PostGroupsGroupIdImageResponse403
    | PostGroupsGroupIdImageResponse404
    | None
):
    """Upload a new image of group

    Args:
        group_id (int):  Example: 25.
        body (PostGroupsGroupIdImageBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostGroupsGroupIdImageResponse200 | PostGroupsGroupIdImageResponse401 | PostGroupsGroupIdImageResponse403 | PostGroupsGroupIdImageResponse404
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: PostGroupsGroupIdImageBody | Unset = UNSET,
) -> Response[
    PostGroupsGroupIdImageResponse200
    | PostGroupsGroupIdImageResponse401
    | PostGroupsGroupIdImageResponse403
    | PostGroupsGroupIdImageResponse404
]:
    """Upload a new image of group

    Args:
        group_id (int):  Example: 25.
        body (PostGroupsGroupIdImageBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostGroupsGroupIdImageResponse200 | PostGroupsGroupIdImageResponse401 | PostGroupsGroupIdImageResponse403 | PostGroupsGroupIdImageResponse404]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: PostGroupsGroupIdImageBody | Unset = UNSET,
) -> (
    PostGroupsGroupIdImageResponse200
    | PostGroupsGroupIdImageResponse401
    | PostGroupsGroupIdImageResponse403
    | PostGroupsGroupIdImageResponse404
    | None
):
    """Upload a new image of group

    Args:
        group_id (int):  Example: 25.
        body (PostGroupsGroupIdImageBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostGroupsGroupIdImageResponse200 | PostGroupsGroupIdImageResponse401 | PostGroupsGroupIdImageResponse403 | PostGroupsGroupIdImageResponse404
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            body=body,
        )
    ).parsed
