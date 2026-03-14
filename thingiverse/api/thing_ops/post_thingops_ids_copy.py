from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_thingops_ids_copy_body import PostThingopsIdsCopyBody
from ...models.post_thingops_ids_copy_response_200 import PostThingopsIdsCopyResponse200
from ...models.post_thingops_ids_copy_response_401 import PostThingopsIdsCopyResponse401
from ...models.post_thingops_ids_copy_response_403 import PostThingopsIdsCopyResponse403
from ...models.post_thingops_ids_copy_response_404 import PostThingopsIdsCopyResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ids: str,
    *,
    body: PostThingopsIdsCopyBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/thingops/{ids}/copy".format(
            ids=quote(str(ids), safe=""),
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
    PostThingopsIdsCopyResponse200
    | PostThingopsIdsCopyResponse401
    | PostThingopsIdsCopyResponse403
    | PostThingopsIdsCopyResponse404
    | None
):
    if response.status_code == 200:
        response_200 = PostThingopsIdsCopyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostThingopsIdsCopyResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostThingopsIdsCopyResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostThingopsIdsCopyResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostThingopsIdsCopyResponse200
    | PostThingopsIdsCopyResponse401
    | PostThingopsIdsCopyResponse403
    | PostThingopsIdsCopyResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ids: str,
    *,
    client: AuthenticatedClient,
    body: PostThingopsIdsCopyBody | Unset = UNSET,
) -> Response[
    PostThingopsIdsCopyResponse200
    | PostThingopsIdsCopyResponse401
    | PostThingopsIdsCopyResponse403
    | PostThingopsIdsCopyResponse404
]:
    """Copy a thing(s) to a new collection

    Args:
        ids (str):  Example: 2.
        body (PostThingopsIdsCopyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostThingopsIdsCopyResponse200 | PostThingopsIdsCopyResponse401 | PostThingopsIdsCopyResponse403 | PostThingopsIdsCopyResponse404]
    """

    kwargs = _get_kwargs(
        ids=ids,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ids: str,
    *,
    client: AuthenticatedClient,
    body: PostThingopsIdsCopyBody | Unset = UNSET,
) -> (
    PostThingopsIdsCopyResponse200
    | PostThingopsIdsCopyResponse401
    | PostThingopsIdsCopyResponse403
    | PostThingopsIdsCopyResponse404
    | None
):
    """Copy a thing(s) to a new collection

    Args:
        ids (str):  Example: 2.
        body (PostThingopsIdsCopyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostThingopsIdsCopyResponse200 | PostThingopsIdsCopyResponse401 | PostThingopsIdsCopyResponse403 | PostThingopsIdsCopyResponse404
    """

    return sync_detailed(
        ids=ids,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    ids: str,
    *,
    client: AuthenticatedClient,
    body: PostThingopsIdsCopyBody | Unset = UNSET,
) -> Response[
    PostThingopsIdsCopyResponse200
    | PostThingopsIdsCopyResponse401
    | PostThingopsIdsCopyResponse403
    | PostThingopsIdsCopyResponse404
]:
    """Copy a thing(s) to a new collection

    Args:
        ids (str):  Example: 2.
        body (PostThingopsIdsCopyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostThingopsIdsCopyResponse200 | PostThingopsIdsCopyResponse401 | PostThingopsIdsCopyResponse403 | PostThingopsIdsCopyResponse404]
    """

    kwargs = _get_kwargs(
        ids=ids,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ids: str,
    *,
    client: AuthenticatedClient,
    body: PostThingopsIdsCopyBody | Unset = UNSET,
) -> (
    PostThingopsIdsCopyResponse200
    | PostThingopsIdsCopyResponse401
    | PostThingopsIdsCopyResponse403
    | PostThingopsIdsCopyResponse404
    | None
):
    """Copy a thing(s) to a new collection

    Args:
        ids (str):  Example: 2.
        body (PostThingopsIdsCopyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostThingopsIdsCopyResponse200 | PostThingopsIdsCopyResponse401 | PostThingopsIdsCopyResponse403 | PostThingopsIdsCopyResponse404
    """

    return (
        await asyncio_detailed(
            ids=ids,
            client=client,
            body=body,
        )
    ).parsed
