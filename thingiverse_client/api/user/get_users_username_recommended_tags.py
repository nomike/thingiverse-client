from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_users_username_recommended_tags_response_401 import (
    GetUsersUsernameRecommendedTagsResponse401,
)
from ...models.get_users_username_recommended_tags_response_403 import (
    GetUsersUsernameRecommendedTagsResponse403,
)
from ...models.get_users_username_recommended_tags_response_404 import (
    GetUsersUsernameRecommendedTagsResponse404,
)
from ...models.tag_schema import TagSchema
from ...types import Response


def _get_kwargs(
    username: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/{username}/recommended-tags".format(
            username=quote(str(username), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetUsersUsernameRecommendedTagsResponse401
    | GetUsersUsernameRecommendedTagsResponse403
    | GetUsersUsernameRecommendedTagsResponse404
    | list[TagSchema]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TagSchema.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetUsersUsernameRecommendedTagsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetUsersUsernameRecommendedTagsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetUsersUsernameRecommendedTagsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetUsersUsernameRecommendedTagsResponse401
    | GetUsersUsernameRecommendedTagsResponse403
    | GetUsersUsernameRecommendedTagsResponse404
    | list[TagSchema]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetUsersUsernameRecommendedTagsResponse401
    | GetUsersUsernameRecommendedTagsResponse403
    | GetUsersUsernameRecommendedTagsResponse404
    | list[TagSchema]
]:
    """Get the list of personal tags.

     returns a list of Recommended tags which are based on the users likes and collected things.

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersUsernameRecommendedTagsResponse401 | GetUsersUsernameRecommendedTagsResponse403 | GetUsersUsernameRecommendedTagsResponse404 | list[TagSchema]]
    """

    kwargs = _get_kwargs(
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetUsersUsernameRecommendedTagsResponse401
    | GetUsersUsernameRecommendedTagsResponse403
    | GetUsersUsernameRecommendedTagsResponse404
    | list[TagSchema]
    | None
):
    """Get the list of personal tags.

     returns a list of Recommended tags which are based on the users likes and collected things.

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersUsernameRecommendedTagsResponse401 | GetUsersUsernameRecommendedTagsResponse403 | GetUsersUsernameRecommendedTagsResponse404 | list[TagSchema]
    """

    return sync_detailed(
        username=username,
        client=client,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetUsersUsernameRecommendedTagsResponse401
    | GetUsersUsernameRecommendedTagsResponse403
    | GetUsersUsernameRecommendedTagsResponse404
    | list[TagSchema]
]:
    """Get the list of personal tags.

     returns a list of Recommended tags which are based on the users likes and collected things.

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersUsernameRecommendedTagsResponse401 | GetUsersUsernameRecommendedTagsResponse403 | GetUsersUsernameRecommendedTagsResponse404 | list[TagSchema]]
    """

    kwargs = _get_kwargs(
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetUsersUsernameRecommendedTagsResponse401
    | GetUsersUsernameRecommendedTagsResponse403
    | GetUsersUsernameRecommendedTagsResponse404
    | list[TagSchema]
    | None
):
    """Get the list of personal tags.

     returns a list of Recommended tags which are based on the users likes and collected things.

    Args:
        username (str):  Example: thingiverse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersUsernameRecommendedTagsResponse401 | GetUsersUsernameRecommendedTagsResponse403 | GetUsersUsernameRecommendedTagsResponse404 | list[TagSchema]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
        )
    ).parsed
