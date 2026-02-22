from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_email_type_enqueue_dmca_body import PostEmailTypeEnqueueDmcaBody
from ...models.post_email_type_enqueue_dmca_response_200 import PostEmailTypeEnqueueDmcaResponse200
from ...models.post_email_type_enqueue_dmca_response_401 import PostEmailTypeEnqueueDmcaResponse401
from ...models.post_email_type_enqueue_dmca_response_403 import PostEmailTypeEnqueueDmcaResponse403
from ...models.post_email_type_enqueue_dmca_response_404 import PostEmailTypeEnqueueDmcaResponse404
from ...models.post_email_type_enqueue_dmca_type import PostEmailTypeEnqueueDmcaType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    type_: PostEmailTypeEnqueueDmcaType,
    *,
    body: PostEmailTypeEnqueueDmcaBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/email/{type_}/enqueue-dmca".format(
            type_=quote(str(type_), safe=""),
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
    PostEmailTypeEnqueueDmcaResponse200
    | PostEmailTypeEnqueueDmcaResponse401
    | PostEmailTypeEnqueueDmcaResponse403
    | PostEmailTypeEnqueueDmcaResponse404
    | None
):
    if response.status_code == 200:
        response_200 = PostEmailTypeEnqueueDmcaResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostEmailTypeEnqueueDmcaResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostEmailTypeEnqueueDmcaResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostEmailTypeEnqueueDmcaResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostEmailTypeEnqueueDmcaResponse200
    | PostEmailTypeEnqueueDmcaResponse401
    | PostEmailTypeEnqueueDmcaResponse403
    | PostEmailTypeEnqueueDmcaResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_: PostEmailTypeEnqueueDmcaType,
    *,
    client: AuthenticatedClient,
    body: PostEmailTypeEnqueueDmcaBody | Unset = UNSET,
) -> Response[
    PostEmailTypeEnqueueDmcaResponse200
    | PostEmailTypeEnqueueDmcaResponse401
    | PostEmailTypeEnqueueDmcaResponse403
    | PostEmailTypeEnqueueDmcaResponse404
]:
    """Queue email to Thingiverse support (DMCA)

    Args:
        type_ (PostEmailTypeEnqueueDmcaType):
        body (PostEmailTypeEnqueueDmcaBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostEmailTypeEnqueueDmcaResponse200 | PostEmailTypeEnqueueDmcaResponse401 | PostEmailTypeEnqueueDmcaResponse403 | PostEmailTypeEnqueueDmcaResponse404]
    """

    kwargs = _get_kwargs(
        type_=type_,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type_: PostEmailTypeEnqueueDmcaType,
    *,
    client: AuthenticatedClient,
    body: PostEmailTypeEnqueueDmcaBody | Unset = UNSET,
) -> (
    PostEmailTypeEnqueueDmcaResponse200
    | PostEmailTypeEnqueueDmcaResponse401
    | PostEmailTypeEnqueueDmcaResponse403
    | PostEmailTypeEnqueueDmcaResponse404
    | None
):
    """Queue email to Thingiverse support (DMCA)

    Args:
        type_ (PostEmailTypeEnqueueDmcaType):
        body (PostEmailTypeEnqueueDmcaBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostEmailTypeEnqueueDmcaResponse200 | PostEmailTypeEnqueueDmcaResponse401 | PostEmailTypeEnqueueDmcaResponse403 | PostEmailTypeEnqueueDmcaResponse404
    """

    return sync_detailed(
        type_=type_,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    type_: PostEmailTypeEnqueueDmcaType,
    *,
    client: AuthenticatedClient,
    body: PostEmailTypeEnqueueDmcaBody | Unset = UNSET,
) -> Response[
    PostEmailTypeEnqueueDmcaResponse200
    | PostEmailTypeEnqueueDmcaResponse401
    | PostEmailTypeEnqueueDmcaResponse403
    | PostEmailTypeEnqueueDmcaResponse404
]:
    """Queue email to Thingiverse support (DMCA)

    Args:
        type_ (PostEmailTypeEnqueueDmcaType):
        body (PostEmailTypeEnqueueDmcaBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostEmailTypeEnqueueDmcaResponse200 | PostEmailTypeEnqueueDmcaResponse401 | PostEmailTypeEnqueueDmcaResponse403 | PostEmailTypeEnqueueDmcaResponse404]
    """

    kwargs = _get_kwargs(
        type_=type_,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_: PostEmailTypeEnqueueDmcaType,
    *,
    client: AuthenticatedClient,
    body: PostEmailTypeEnqueueDmcaBody | Unset = UNSET,
) -> (
    PostEmailTypeEnqueueDmcaResponse200
    | PostEmailTypeEnqueueDmcaResponse401
    | PostEmailTypeEnqueueDmcaResponse403
    | PostEmailTypeEnqueueDmcaResponse404
    | None
):
    """Queue email to Thingiverse support (DMCA)

    Args:
        type_ (PostEmailTypeEnqueueDmcaType):
        body (PostEmailTypeEnqueueDmcaBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostEmailTypeEnqueueDmcaResponse200 | PostEmailTypeEnqueueDmcaResponse401 | PostEmailTypeEnqueueDmcaResponse403 | PostEmailTypeEnqueueDmcaResponse404
    """

    return (
        await asyncio_detailed(
            type_=type_,
            client=client,
            body=body,
        )
    ).parsed
