from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_copies_copy_id_images_response_401 import GetCopiesCopyIdImagesResponse401
from ...models.get_copies_copy_id_images_response_403 import GetCopiesCopyIdImagesResponse403
from ...models.get_copies_copy_id_images_response_404 import GetCopiesCopyIdImagesResponse404
from ...models.image_summary_schema_type_0 import ImageSummarySchemaType0
from ...types import Response


def _get_kwargs(
    copy_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/copies/{copy_id}/images".format(
            copy_id=quote(str(copy_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetCopiesCopyIdImagesResponse401
    | GetCopiesCopyIdImagesResponse403
    | GetCopiesCopyIdImagesResponse404
    | list[ImageSummarySchemaType0 | None]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(data: object) -> ImageSummarySchemaType0 | None:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemasimage_summary_schema_type_0 = (
                        ImageSummarySchemaType0.from_dict(data)
                    )

                    return componentsschemasimage_summary_schema_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(ImageSummarySchemaType0 | None, data)

            response_200_item = _parse_response_200_item(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetCopiesCopyIdImagesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetCopiesCopyIdImagesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetCopiesCopyIdImagesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetCopiesCopyIdImagesResponse401
    | GetCopiesCopyIdImagesResponse403
    | GetCopiesCopyIdImagesResponse404
    | list[ImageSummarySchemaType0 | None]
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
    GetCopiesCopyIdImagesResponse401
    | GetCopiesCopyIdImagesResponse403
    | GetCopiesCopyIdImagesResponse404
    | list[ImageSummarySchemaType0 | None]
]:
    """Get images for a copy

    Args:
        copy_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCopiesCopyIdImagesResponse401 | GetCopiesCopyIdImagesResponse403 | GetCopiesCopyIdImagesResponse404 | list[ImageSummarySchemaType0 | None]]
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
    GetCopiesCopyIdImagesResponse401
    | GetCopiesCopyIdImagesResponse403
    | GetCopiesCopyIdImagesResponse404
    | list[ImageSummarySchemaType0 | None]
    | None
):
    """Get images for a copy

    Args:
        copy_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCopiesCopyIdImagesResponse401 | GetCopiesCopyIdImagesResponse403 | GetCopiesCopyIdImagesResponse404 | list[ImageSummarySchemaType0 | None]
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
    GetCopiesCopyIdImagesResponse401
    | GetCopiesCopyIdImagesResponse403
    | GetCopiesCopyIdImagesResponse404
    | list[ImageSummarySchemaType0 | None]
]:
    """Get images for a copy

    Args:
        copy_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCopiesCopyIdImagesResponse401 | GetCopiesCopyIdImagesResponse403 | GetCopiesCopyIdImagesResponse404 | list[ImageSummarySchemaType0 | None]]
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
    GetCopiesCopyIdImagesResponse401
    | GetCopiesCopyIdImagesResponse403
    | GetCopiesCopyIdImagesResponse404
    | list[ImageSummarySchemaType0 | None]
    | None
):
    """Get images for a copy

    Args:
        copy_id (int):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCopiesCopyIdImagesResponse401 | GetCopiesCopyIdImagesResponse403 | GetCopiesCopyIdImagesResponse404 | list[ImageSummarySchemaType0 | None]
    """

    return (
        await asyncio_detailed(
            copy_id=copy_id,
            client=client,
        )
    ).parsed
