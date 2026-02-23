from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_sitewidenotification_id_response_401 import GetSitewidenotificationIdResponse401
from ...models.get_sitewidenotification_id_response_403 import GetSitewidenotificationIdResponse403
from ...models.get_sitewidenotification_id_response_404 import GetSitewidenotificationIdResponse404
from ...models.sitewidenotification_schema_type_0 import SitewidenotificationSchemaType0
from ...types import Response


def _get_kwargs(
    id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sitewidenotification/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSitewidenotificationIdResponse401
    | GetSitewidenotificationIdResponse403
    | GetSitewidenotificationIdResponse404
    | None
    | SitewidenotificationSchemaType0
    | None
):
    if response.status_code == 200:

        def _parse_response_200(data: object) -> None | SitewidenotificationSchemaType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemassitewidenotification_schema_type_0 = (
                    SitewidenotificationSchemaType0.from_dict(data)
                )

                return componentsschemassitewidenotification_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SitewidenotificationSchemaType0, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetSitewidenotificationIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetSitewidenotificationIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSitewidenotificationIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSitewidenotificationIdResponse401
    | GetSitewidenotificationIdResponse403
    | GetSitewidenotificationIdResponse404
    | None
    | SitewidenotificationSchemaType0
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetSitewidenotificationIdResponse401
    | GetSitewidenotificationIdResponse403
    | GetSitewidenotificationIdResponse404
    | None
    | SitewidenotificationSchemaType0
]:
    """Get a sitewidenotification by id

    Args:
        id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSitewidenotificationIdResponse401 | GetSitewidenotificationIdResponse403 | GetSitewidenotificationIdResponse404 | None | SitewidenotificationSchemaType0]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
) -> (
    GetSitewidenotificationIdResponse401
    | GetSitewidenotificationIdResponse403
    | GetSitewidenotificationIdResponse404
    | None
    | SitewidenotificationSchemaType0
    | None
):
    """Get a sitewidenotification by id

    Args:
        id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSitewidenotificationIdResponse401 | GetSitewidenotificationIdResponse403 | GetSitewidenotificationIdResponse404 | None | SitewidenotificationSchemaType0
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetSitewidenotificationIdResponse401
    | GetSitewidenotificationIdResponse403
    | GetSitewidenotificationIdResponse404
    | None
    | SitewidenotificationSchemaType0
]:
    """Get a sitewidenotification by id

    Args:
        id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSitewidenotificationIdResponse401 | GetSitewidenotificationIdResponse403 | GetSitewidenotificationIdResponse404 | None | SitewidenotificationSchemaType0]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
) -> (
    GetSitewidenotificationIdResponse401
    | GetSitewidenotificationIdResponse403
    | GetSitewidenotificationIdResponse404
    | None
    | SitewidenotificationSchemaType0
    | None
):
    """Get a sitewidenotification by id

    Args:
        id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSitewidenotificationIdResponse401 | GetSitewidenotificationIdResponse403 | GetSitewidenotificationIdResponse404 | None | SitewidenotificationSchemaType0
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
