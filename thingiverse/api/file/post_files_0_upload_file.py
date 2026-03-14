from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_files_0_upload_file_body import PostFiles0UploadFileBody
from ...models.post_files_0_upload_file_response_200 import PostFiles0UploadFileResponse200
from ...models.post_files_0_upload_file_response_400 import PostFiles0UploadFileResponse400
from ...models.post_files_0_upload_file_response_401 import PostFiles0UploadFileResponse401
from ...models.post_files_0_upload_file_response_403 import PostFiles0UploadFileResponse403
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostFiles0UploadFileBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/files/0/uploadFile",
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostFiles0UploadFileResponse200
    | PostFiles0UploadFileResponse400
    | PostFiles0UploadFileResponse401
    | PostFiles0UploadFileResponse403
    | None
):
    if response.status_code == 200:
        response_200 = PostFiles0UploadFileResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostFiles0UploadFileResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostFiles0UploadFileResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostFiles0UploadFileResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostFiles0UploadFileResponse200
    | PostFiles0UploadFileResponse400
    | PostFiles0UploadFileResponse401
    | PostFiles0UploadFileResponse403
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
    body: PostFiles0UploadFileBody | Unset = UNSET,
) -> Response[
    PostFiles0UploadFileResponse200
    | PostFiles0UploadFileResponse400
    | PostFiles0UploadFileResponse401
    | PostFiles0UploadFileResponse403
]:
    r"""Upload a file as pendingupload

     Upload a file to the storageBucket as \"pendingUpload\". The file will be stored in a temporary
    folder until it is finalized (eg; associated with a thing/make/comment/etc) via the /finalize
    endpoint.

    Args:
        body (PostFiles0UploadFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFiles0UploadFileResponse200 | PostFiles0UploadFileResponse400 | PostFiles0UploadFileResponse401 | PostFiles0UploadFileResponse403]
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
    body: PostFiles0UploadFileBody | Unset = UNSET,
) -> (
    PostFiles0UploadFileResponse200
    | PostFiles0UploadFileResponse400
    | PostFiles0UploadFileResponse401
    | PostFiles0UploadFileResponse403
    | None
):
    r"""Upload a file as pendingupload

     Upload a file to the storageBucket as \"pendingUpload\". The file will be stored in a temporary
    folder until it is finalized (eg; associated with a thing/make/comment/etc) via the /finalize
    endpoint.

    Args:
        body (PostFiles0UploadFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFiles0UploadFileResponse200 | PostFiles0UploadFileResponse400 | PostFiles0UploadFileResponse401 | PostFiles0UploadFileResponse403
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostFiles0UploadFileBody | Unset = UNSET,
) -> Response[
    PostFiles0UploadFileResponse200
    | PostFiles0UploadFileResponse400
    | PostFiles0UploadFileResponse401
    | PostFiles0UploadFileResponse403
]:
    r"""Upload a file as pendingupload

     Upload a file to the storageBucket as \"pendingUpload\". The file will be stored in a temporary
    folder until it is finalized (eg; associated with a thing/make/comment/etc) via the /finalize
    endpoint.

    Args:
        body (PostFiles0UploadFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFiles0UploadFileResponse200 | PostFiles0UploadFileResponse400 | PostFiles0UploadFileResponse401 | PostFiles0UploadFileResponse403]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostFiles0UploadFileBody | Unset = UNSET,
) -> (
    PostFiles0UploadFileResponse200
    | PostFiles0UploadFileResponse400
    | PostFiles0UploadFileResponse401
    | PostFiles0UploadFileResponse403
    | None
):
    r"""Upload a file as pendingupload

     Upload a file to the storageBucket as \"pendingUpload\". The file will be stored in a temporary
    folder until it is finalized (eg; associated with a thing/make/comment/etc) via the /finalize
    endpoint.

    Args:
        body (PostFiles0UploadFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFiles0UploadFileResponse200 | PostFiles0UploadFileResponse400 | PostFiles0UploadFileResponse401 | PostFiles0UploadFileResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
