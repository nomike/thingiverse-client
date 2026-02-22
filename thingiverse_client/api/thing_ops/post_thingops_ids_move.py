from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_thingops_ids_move_body import PostThingopsIdsMoveBody
from ...models.post_thingops_ids_move_response_200 import PostThingopsIdsMoveResponse200
from ...models.post_thingops_ids_move_response_401 import PostThingopsIdsMoveResponse401
from ...models.post_thingops_ids_move_response_403 import PostThingopsIdsMoveResponse403
from ...models.post_thingops_ids_move_response_404 import PostThingopsIdsMoveResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ids: str,
    *,
    body: PostThingopsIdsMoveBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/thingops/{ids}/move".format(
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
    PostThingopsIdsMoveResponse200
    | PostThingopsIdsMoveResponse401
    | PostThingopsIdsMoveResponse403
    | PostThingopsIdsMoveResponse404
    | None
):
    if response.status_code == 200:
        response_200 = PostThingopsIdsMoveResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostThingopsIdsMoveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostThingopsIdsMoveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostThingopsIdsMoveResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostThingopsIdsMoveResponse200
    | PostThingopsIdsMoveResponse401
    | PostThingopsIdsMoveResponse403
    | PostThingopsIdsMoveResponse404
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
    body: PostThingopsIdsMoveBody | Unset = UNSET,
) -> Response[
    PostThingopsIdsMoveResponse200
    | PostThingopsIdsMoveResponse401
    | PostThingopsIdsMoveResponse403
    | PostThingopsIdsMoveResponse404
]:
    """Move a thing(s) to a new collection

    Args:
        ids (str):  Example: 2.
        body (PostThingopsIdsMoveBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostThingopsIdsMoveResponse200 | PostThingopsIdsMoveResponse401 | PostThingopsIdsMoveResponse403 | PostThingopsIdsMoveResponse404]
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
    body: PostThingopsIdsMoveBody | Unset = UNSET,
) -> (
    PostThingopsIdsMoveResponse200
    | PostThingopsIdsMoveResponse401
    | PostThingopsIdsMoveResponse403
    | PostThingopsIdsMoveResponse404
    | None
):
    """Move a thing(s) to a new collection

    Args:
        ids (str):  Example: 2.
        body (PostThingopsIdsMoveBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostThingopsIdsMoveResponse200 | PostThingopsIdsMoveResponse401 | PostThingopsIdsMoveResponse403 | PostThingopsIdsMoveResponse404
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
    body: PostThingopsIdsMoveBody | Unset = UNSET,
) -> Response[
    PostThingopsIdsMoveResponse200
    | PostThingopsIdsMoveResponse401
    | PostThingopsIdsMoveResponse403
    | PostThingopsIdsMoveResponse404
]:
    """Move a thing(s) to a new collection

    Args:
        ids (str):  Example: 2.
        body (PostThingopsIdsMoveBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostThingopsIdsMoveResponse200 | PostThingopsIdsMoveResponse401 | PostThingopsIdsMoveResponse403 | PostThingopsIdsMoveResponse404]
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
    body: PostThingopsIdsMoveBody | Unset = UNSET,
) -> (
    PostThingopsIdsMoveResponse200
    | PostThingopsIdsMoveResponse401
    | PostThingopsIdsMoveResponse403
    | PostThingopsIdsMoveResponse404
    | None
):
    """Move a thing(s) to a new collection

    Args:
        ids (str):  Example: 2.
        body (PostThingopsIdsMoveBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostThingopsIdsMoveResponse200 | PostThingopsIdsMoveResponse401 | PostThingopsIdsMoveResponse403 | PostThingopsIdsMoveResponse404
    """

    return (
        await asyncio_detailed(
            ids=ids,
            client=client,
            body=body,
        )
    ).parsed
