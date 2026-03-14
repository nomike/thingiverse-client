from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_thingops_ids_remove_body import PostThingopsIdsRemoveBody
from ...models.post_thingops_ids_remove_response_200 import PostThingopsIdsRemoveResponse200
from ...models.post_thingops_ids_remove_response_401 import PostThingopsIdsRemoveResponse401
from ...models.post_thingops_ids_remove_response_403 import PostThingopsIdsRemoveResponse403
from ...models.post_thingops_ids_remove_response_404 import PostThingopsIdsRemoveResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ids: str,
    *,
    body: PostThingopsIdsRemoveBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/thingops/{ids}/remove".format(
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
    PostThingopsIdsRemoveResponse200
    | PostThingopsIdsRemoveResponse401
    | PostThingopsIdsRemoveResponse403
    | PostThingopsIdsRemoveResponse404
    | None
):
    if response.status_code == 200:
        response_200 = PostThingopsIdsRemoveResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostThingopsIdsRemoveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostThingopsIdsRemoveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostThingopsIdsRemoveResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostThingopsIdsRemoveResponse200
    | PostThingopsIdsRemoveResponse401
    | PostThingopsIdsRemoveResponse403
    | PostThingopsIdsRemoveResponse404
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
    body: PostThingopsIdsRemoveBody | Unset = UNSET,
) -> Response[
    PostThingopsIdsRemoveResponse200
    | PostThingopsIdsRemoveResponse401
    | PostThingopsIdsRemoveResponse403
    | PostThingopsIdsRemoveResponse404
]:
    """Remove a thing(s) from a collection

    Args:
        ids (str):  Example: 2.
        body (PostThingopsIdsRemoveBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostThingopsIdsRemoveResponse200 | PostThingopsIdsRemoveResponse401 | PostThingopsIdsRemoveResponse403 | PostThingopsIdsRemoveResponse404]
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
    body: PostThingopsIdsRemoveBody | Unset = UNSET,
) -> (
    PostThingopsIdsRemoveResponse200
    | PostThingopsIdsRemoveResponse401
    | PostThingopsIdsRemoveResponse403
    | PostThingopsIdsRemoveResponse404
    | None
):
    """Remove a thing(s) from a collection

    Args:
        ids (str):  Example: 2.
        body (PostThingopsIdsRemoveBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostThingopsIdsRemoveResponse200 | PostThingopsIdsRemoveResponse401 | PostThingopsIdsRemoveResponse403 | PostThingopsIdsRemoveResponse404
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
    body: PostThingopsIdsRemoveBody | Unset = UNSET,
) -> Response[
    PostThingopsIdsRemoveResponse200
    | PostThingopsIdsRemoveResponse401
    | PostThingopsIdsRemoveResponse403
    | PostThingopsIdsRemoveResponse404
]:
    """Remove a thing(s) from a collection

    Args:
        ids (str):  Example: 2.
        body (PostThingopsIdsRemoveBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostThingopsIdsRemoveResponse200 | PostThingopsIdsRemoveResponse401 | PostThingopsIdsRemoveResponse403 | PostThingopsIdsRemoveResponse404]
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
    body: PostThingopsIdsRemoveBody | Unset = UNSET,
) -> (
    PostThingopsIdsRemoveResponse200
    | PostThingopsIdsRemoveResponse401
    | PostThingopsIdsRemoveResponse403
    | PostThingopsIdsRemoveResponse404
    | None
):
    """Remove a thing(s) from a collection

    Args:
        ids (str):  Example: 2.
        body (PostThingopsIdsRemoveBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostThingopsIdsRemoveResponse200 | PostThingopsIdsRemoveResponse401 | PostThingopsIdsRemoveResponse403 | PostThingopsIdsRemoveResponse404
    """

    return (
        await asyncio_detailed(
            ids=ids,
            client=client,
            body=body,
        )
    ).parsed
