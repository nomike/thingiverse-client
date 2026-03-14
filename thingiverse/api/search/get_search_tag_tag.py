from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_search_tag_tag_response_401 import GetSearchTagTagResponse401
from ...models.get_search_tag_tag_response_403 import GetSearchTagTagResponse403
from ...models.get_search_tag_tag_response_404 import GetSearchTagTagResponse404
from ...types import Response


def _get_kwargs(
    tag: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/search/{tag}/tag".format(
            tag=quote(str(tag), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetSearchTagTagResponse401
    | GetSearchTagTagResponse403
    | GetSearchTagTagResponse404
    | None
):
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = GetSearchTagTagResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetSearchTagTagResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSearchTagTagResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | GetSearchTagTagResponse401 | GetSearchTagTagResponse403 | GetSearchTagTagResponse404
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
    Any | GetSearchTagTagResponse401 | GetSearchTagTagResponse403 | GetSearchTagTagResponse404
]:
    """
    Args:
        tag (str):  Example: test.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSearchTagTagResponse401 | GetSearchTagTagResponse403 | GetSearchTagTagResponse404]
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
    Any
    | GetSearchTagTagResponse401
    | GetSearchTagTagResponse403
    | GetSearchTagTagResponse404
    | None
):
    """
    Args:
        tag (str):  Example: test.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSearchTagTagResponse401 | GetSearchTagTagResponse403 | GetSearchTagTagResponse404
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
    Any | GetSearchTagTagResponse401 | GetSearchTagTagResponse403 | GetSearchTagTagResponse404
]:
    """
    Args:
        tag (str):  Example: test.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSearchTagTagResponse401 | GetSearchTagTagResponse403 | GetSearchTagTagResponse404]
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
    Any
    | GetSearchTagTagResponse401
    | GetSearchTagTagResponse403
    | GetSearchTagTagResponse404
    | None
):
    """
    Args:
        tag (str):  Example: test.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSearchTagTagResponse401 | GetSearchTagTagResponse403 | GetSearchTagTagResponse404
    """

    return (
        await asyncio_detailed(
            tag=tag,
            client=client,
        )
    ).parsed
