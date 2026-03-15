from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.grouptopic_schema import GrouptopicSchema
from ...models.patch_grouptopics_grouptopic_id_body import PatchGrouptopicsGrouptopicIdBody
from ...models.patch_grouptopics_grouptopic_id_response_401 import (
    PatchGrouptopicsGrouptopicIdResponse401,
)
from ...models.patch_grouptopics_grouptopic_id_response_403 import (
    PatchGrouptopicsGrouptopicIdResponse403,
)
from ...models.patch_grouptopics_grouptopic_id_response_404 import (
    PatchGrouptopicsGrouptopicIdResponse404,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    grouptopic_id: int,
    *,
    body: PatchGrouptopicsGrouptopicIdBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/grouptopics/{grouptopic_id}/".format(
            grouptopic_id=quote(str(grouptopic_id), safe=""),
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
    GrouptopicSchema
    | PatchGrouptopicsGrouptopicIdResponse401
    | PatchGrouptopicsGrouptopicIdResponse403
    | PatchGrouptopicsGrouptopicIdResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GrouptopicSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PatchGrouptopicsGrouptopicIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchGrouptopicsGrouptopicIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchGrouptopicsGrouptopicIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GrouptopicSchema
    | PatchGrouptopicsGrouptopicIdResponse401
    | PatchGrouptopicsGrouptopicIdResponse403
    | PatchGrouptopicsGrouptopicIdResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    grouptopic_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchGrouptopicsGrouptopicIdBody | Unset = UNSET,
) -> Response[
    GrouptopicSchema
    | PatchGrouptopicsGrouptopicIdResponse401
    | PatchGrouptopicsGrouptopicIdResponse403
    | PatchGrouptopicsGrouptopicIdResponse404
]:
    """Update a group topic

    Args:
        grouptopic_id (int):  Example: 2.
        body (PatchGrouptopicsGrouptopicIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GrouptopicSchema | PatchGrouptopicsGrouptopicIdResponse401 | PatchGrouptopicsGrouptopicIdResponse403 | PatchGrouptopicsGrouptopicIdResponse404]
    """

    kwargs = _get_kwargs(
        grouptopic_id=grouptopic_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    grouptopic_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchGrouptopicsGrouptopicIdBody | Unset = UNSET,
) -> (
    GrouptopicSchema
    | PatchGrouptopicsGrouptopicIdResponse401
    | PatchGrouptopicsGrouptopicIdResponse403
    | PatchGrouptopicsGrouptopicIdResponse404
    | None
):
    """Update a group topic

    Args:
        grouptopic_id (int):  Example: 2.
        body (PatchGrouptopicsGrouptopicIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GrouptopicSchema | PatchGrouptopicsGrouptopicIdResponse401 | PatchGrouptopicsGrouptopicIdResponse403 | PatchGrouptopicsGrouptopicIdResponse404
    """

    return sync_detailed(
        grouptopic_id=grouptopic_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    grouptopic_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchGrouptopicsGrouptopicIdBody | Unset = UNSET,
) -> Response[
    GrouptopicSchema
    | PatchGrouptopicsGrouptopicIdResponse401
    | PatchGrouptopicsGrouptopicIdResponse403
    | PatchGrouptopicsGrouptopicIdResponse404
]:
    """Update a group topic

    Args:
        grouptopic_id (int):  Example: 2.
        body (PatchGrouptopicsGrouptopicIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GrouptopicSchema | PatchGrouptopicsGrouptopicIdResponse401 | PatchGrouptopicsGrouptopicIdResponse403 | PatchGrouptopicsGrouptopicIdResponse404]
    """

    kwargs = _get_kwargs(
        grouptopic_id=grouptopic_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    grouptopic_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchGrouptopicsGrouptopicIdBody | Unset = UNSET,
) -> (
    GrouptopicSchema
    | PatchGrouptopicsGrouptopicIdResponse401
    | PatchGrouptopicsGrouptopicIdResponse403
    | PatchGrouptopicsGrouptopicIdResponse404
    | None
):
    """Update a group topic

    Args:
        grouptopic_id (int):  Example: 2.
        body (PatchGrouptopicsGrouptopicIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GrouptopicSchema | PatchGrouptopicsGrouptopicIdResponse401 | PatchGrouptopicsGrouptopicIdResponse403 | PatchGrouptopicsGrouptopicIdResponse404
    """

    return (
        await asyncio_detailed(
            grouptopic_id=grouptopic_id,
            client=client,
            body=body,
        )
    ).parsed
