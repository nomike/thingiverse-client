from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_files_0_finalize_files_response_200 import PostFiles0FinalizeFilesResponse200
from ...models.post_files_0_finalize_files_response_400 import PostFiles0FinalizeFilesResponse400
from ...models.post_files_0_finalize_files_response_401 import PostFiles0FinalizeFilesResponse401
from ...models.post_files_0_finalize_files_response_403 import PostFiles0FinalizeFilesResponse403
from ...models.post_files_0_finalize_files_response_404 import PostFiles0FinalizeFilesResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Any | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/files/0/FinalizeFiles",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostFiles0FinalizeFilesResponse200
    | PostFiles0FinalizeFilesResponse400
    | PostFiles0FinalizeFilesResponse401
    | PostFiles0FinalizeFilesResponse403
    | PostFiles0FinalizeFilesResponse404
    | None
):
    if response.status_code == 200:
        response_200 = PostFiles0FinalizeFilesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostFiles0FinalizeFilesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostFiles0FinalizeFilesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostFiles0FinalizeFilesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostFiles0FinalizeFilesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostFiles0FinalizeFilesResponse200
    | PostFiles0FinalizeFilesResponse400
    | PostFiles0FinalizeFilesResponse401
    | PostFiles0FinalizeFilesResponse403
    | PostFiles0FinalizeFilesResponse404
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
    body: Any | Unset = UNSET,
) -> Response[
    PostFiles0FinalizeFilesResponse200
    | PostFiles0FinalizeFilesResponse400
    | PostFiles0FinalizeFilesResponse401
    | PostFiles0FinalizeFilesResponse403
    | PostFiles0FinalizeFilesResponse404
]:
    r"""Finalize multiple uploaded files. DEPRECATED, use FinalizeFiles endpoint instead

     Finalize multiple \"pendingUploads\" at once by associating them with something
    (Thing/make/comment). In order to use this, you will need to first use the uploadFile endpoint

    Args:
        body (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFiles0FinalizeFilesResponse200 | PostFiles0FinalizeFilesResponse400 | PostFiles0FinalizeFilesResponse401 | PostFiles0FinalizeFilesResponse403 | PostFiles0FinalizeFilesResponse404]
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
    body: Any | Unset = UNSET,
) -> (
    PostFiles0FinalizeFilesResponse200
    | PostFiles0FinalizeFilesResponse400
    | PostFiles0FinalizeFilesResponse401
    | PostFiles0FinalizeFilesResponse403
    | PostFiles0FinalizeFilesResponse404
    | None
):
    r"""Finalize multiple uploaded files. DEPRECATED, use FinalizeFiles endpoint instead

     Finalize multiple \"pendingUploads\" at once by associating them with something
    (Thing/make/comment). In order to use this, you will need to first use the uploadFile endpoint

    Args:
        body (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFiles0FinalizeFilesResponse200 | PostFiles0FinalizeFilesResponse400 | PostFiles0FinalizeFilesResponse401 | PostFiles0FinalizeFilesResponse403 | PostFiles0FinalizeFilesResponse404
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Any | Unset = UNSET,
) -> Response[
    PostFiles0FinalizeFilesResponse200
    | PostFiles0FinalizeFilesResponse400
    | PostFiles0FinalizeFilesResponse401
    | PostFiles0FinalizeFilesResponse403
    | PostFiles0FinalizeFilesResponse404
]:
    r"""Finalize multiple uploaded files. DEPRECATED, use FinalizeFiles endpoint instead

     Finalize multiple \"pendingUploads\" at once by associating them with something
    (Thing/make/comment). In order to use this, you will need to first use the uploadFile endpoint

    Args:
        body (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFiles0FinalizeFilesResponse200 | PostFiles0FinalizeFilesResponse400 | PostFiles0FinalizeFilesResponse401 | PostFiles0FinalizeFilesResponse403 | PostFiles0FinalizeFilesResponse404]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Any | Unset = UNSET,
) -> (
    PostFiles0FinalizeFilesResponse200
    | PostFiles0FinalizeFilesResponse400
    | PostFiles0FinalizeFilesResponse401
    | PostFiles0FinalizeFilesResponse403
    | PostFiles0FinalizeFilesResponse404
    | None
):
    r"""Finalize multiple uploaded files. DEPRECATED, use FinalizeFiles endpoint instead

     Finalize multiple \"pendingUploads\" at once by associating them with something
    (Thing/make/comment). In order to use this, you will need to first use the uploadFile endpoint

    Args:
        body (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFiles0FinalizeFilesResponse200 | PostFiles0FinalizeFilesResponse400 | PostFiles0FinalizeFilesResponse401 | PostFiles0FinalizeFilesResponse403 | PostFiles0FinalizeFilesResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
