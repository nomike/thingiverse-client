from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_copies_copy_id_likes_response_200 import DeleteCopiesCopyIdLikesResponse200
from ...models.delete_copies_copy_id_likes_response_400 import DeleteCopiesCopyIdLikesResponse400
from ...models.delete_copies_copy_id_likes_response_401 import DeleteCopiesCopyIdLikesResponse401
from ...models.delete_copies_copy_id_likes_response_403 import DeleteCopiesCopyIdLikesResponse403
from ...models.delete_copies_copy_id_likes_response_404 import DeleteCopiesCopyIdLikesResponse404
from ...types import Response


def _get_kwargs(
    copy_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/copies/{copy_id}/likes".format(
            copy_id=quote(str(copy_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteCopiesCopyIdLikesResponse200
    | DeleteCopiesCopyIdLikesResponse400
    | DeleteCopiesCopyIdLikesResponse401
    | DeleteCopiesCopyIdLikesResponse403
    | DeleteCopiesCopyIdLikesResponse404
    | None
):
    if response.status_code == 200:
        response_200 = DeleteCopiesCopyIdLikesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteCopiesCopyIdLikesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteCopiesCopyIdLikesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteCopiesCopyIdLikesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteCopiesCopyIdLikesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteCopiesCopyIdLikesResponse200
    | DeleteCopiesCopyIdLikesResponse400
    | DeleteCopiesCopyIdLikesResponse401
    | DeleteCopiesCopyIdLikesResponse403
    | DeleteCopiesCopyIdLikesResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    copy_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    DeleteCopiesCopyIdLikesResponse200
    | DeleteCopiesCopyIdLikesResponse400
    | DeleteCopiesCopyIdLikesResponse401
    | DeleteCopiesCopyIdLikesResponse403
    | DeleteCopiesCopyIdLikesResponse404
]:
    r"""Delete a like

     Must use the DELETE method Result will be 404 Not Found if the copy doesn't exist. Result will be
    400 Bad Request if the user is trying to \"unlike\" their own copy.

    Args:
        copy_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteCopiesCopyIdLikesResponse200 | DeleteCopiesCopyIdLikesResponse400 | DeleteCopiesCopyIdLikesResponse401 | DeleteCopiesCopyIdLikesResponse403 | DeleteCopiesCopyIdLikesResponse404]
    """

    kwargs = _get_kwargs(
        copy_id=copy_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    copy_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    DeleteCopiesCopyIdLikesResponse200
    | DeleteCopiesCopyIdLikesResponse400
    | DeleteCopiesCopyIdLikesResponse401
    | DeleteCopiesCopyIdLikesResponse403
    | DeleteCopiesCopyIdLikesResponse404
    | None
):
    r"""Delete a like

     Must use the DELETE method Result will be 404 Not Found if the copy doesn't exist. Result will be
    400 Bad Request if the user is trying to \"unlike\" their own copy.

    Args:
        copy_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteCopiesCopyIdLikesResponse200 | DeleteCopiesCopyIdLikesResponse400 | DeleteCopiesCopyIdLikesResponse401 | DeleteCopiesCopyIdLikesResponse403 | DeleteCopiesCopyIdLikesResponse404
    """

    return sync_detailed(
        copy_id=copy_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    copy_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    DeleteCopiesCopyIdLikesResponse200
    | DeleteCopiesCopyIdLikesResponse400
    | DeleteCopiesCopyIdLikesResponse401
    | DeleteCopiesCopyIdLikesResponse403
    | DeleteCopiesCopyIdLikesResponse404
]:
    r"""Delete a like

     Must use the DELETE method Result will be 404 Not Found if the copy doesn't exist. Result will be
    400 Bad Request if the user is trying to \"unlike\" their own copy.

    Args:
        copy_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteCopiesCopyIdLikesResponse200 | DeleteCopiesCopyIdLikesResponse400 | DeleteCopiesCopyIdLikesResponse401 | DeleteCopiesCopyIdLikesResponse403 | DeleteCopiesCopyIdLikesResponse404]
    """

    kwargs = _get_kwargs(
        copy_id=copy_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    copy_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    DeleteCopiesCopyIdLikesResponse200
    | DeleteCopiesCopyIdLikesResponse400
    | DeleteCopiesCopyIdLikesResponse401
    | DeleteCopiesCopyIdLikesResponse403
    | DeleteCopiesCopyIdLikesResponse404
    | None
):
    r"""Delete a like

     Must use the DELETE method Result will be 404 Not Found if the copy doesn't exist. Result will be
    400 Bad Request if the user is trying to \"unlike\" their own copy.

    Args:
        copy_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteCopiesCopyIdLikesResponse200 | DeleteCopiesCopyIdLikesResponse400 | DeleteCopiesCopyIdLikesResponse401 | DeleteCopiesCopyIdLikesResponse403 | DeleteCopiesCopyIdLikesResponse404
    """

    return (
        await asyncio_detailed(
            copy_id=copy_id,
            client=client,
        )
    ).parsed
