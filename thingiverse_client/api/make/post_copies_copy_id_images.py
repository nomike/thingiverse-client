from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.image_summary_schema_type_0 import ImageSummarySchemaType0
from ...models.post_copies_copy_id_images_body import PostCopiesCopyIdImagesBody
from ...models.post_copies_copy_id_images_response_401 import PostCopiesCopyIdImagesResponse401
from ...models.post_copies_copy_id_images_response_403 import PostCopiesCopyIdImagesResponse403
from ...models.post_copies_copy_id_images_response_404 import PostCopiesCopyIdImagesResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    copy_id: int,
    *,
    body: PostCopiesCopyIdImagesBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/copies/{copy_id}/images".format(
            copy_id=quote(str(copy_id), safe=""),
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
    ImageSummarySchemaType0
    | None
    | PostCopiesCopyIdImagesResponse401
    | PostCopiesCopyIdImagesResponse403
    | PostCopiesCopyIdImagesResponse404
    | None
):
    if response.status_code == 200:

        def _parse_response_200(data: object) -> ImageSummarySchemaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasimage_summary_schema_type_0 = ImageSummarySchemaType0.from_dict(
                    data
                )

                return componentsschemasimage_summary_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageSummarySchemaType0 | None, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostCopiesCopyIdImagesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostCopiesCopyIdImagesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostCopiesCopyIdImagesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ImageSummarySchemaType0
    | None
    | PostCopiesCopyIdImagesResponse401
    | PostCopiesCopyIdImagesResponse403
    | PostCopiesCopyIdImagesResponse404
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
    body: PostCopiesCopyIdImagesBody | Unset = UNSET,
) -> Response[
    ImageSummarySchemaType0
    | None
    | PostCopiesCopyIdImagesResponse401
    | PostCopiesCopyIdImagesResponse403
    | PostCopiesCopyIdImagesResponse404
]:
    """Upload image to a copy

    Args:
        copy_id (int):  Example: 1.
        body (PostCopiesCopyIdImagesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImageSummarySchemaType0 | None | PostCopiesCopyIdImagesResponse401 | PostCopiesCopyIdImagesResponse403 | PostCopiesCopyIdImagesResponse404]
    """

    kwargs = _get_kwargs(
        copy_id=copy_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    copy_id: int,
    *,
    client: AuthenticatedClient,
    body: PostCopiesCopyIdImagesBody | Unset = UNSET,
) -> (
    ImageSummarySchemaType0
    | None
    | PostCopiesCopyIdImagesResponse401
    | PostCopiesCopyIdImagesResponse403
    | PostCopiesCopyIdImagesResponse404
    | None
):
    """Upload image to a copy

    Args:
        copy_id (int):  Example: 1.
        body (PostCopiesCopyIdImagesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ImageSummarySchemaType0 | None | PostCopiesCopyIdImagesResponse401 | PostCopiesCopyIdImagesResponse403 | PostCopiesCopyIdImagesResponse404
    """

    return sync_detailed(
        copy_id=copy_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    copy_id: int,
    *,
    client: AuthenticatedClient,
    body: PostCopiesCopyIdImagesBody | Unset = UNSET,
) -> Response[
    ImageSummarySchemaType0
    | None
    | PostCopiesCopyIdImagesResponse401
    | PostCopiesCopyIdImagesResponse403
    | PostCopiesCopyIdImagesResponse404
]:
    """Upload image to a copy

    Args:
        copy_id (int):  Example: 1.
        body (PostCopiesCopyIdImagesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImageSummarySchemaType0 | None | PostCopiesCopyIdImagesResponse401 | PostCopiesCopyIdImagesResponse403 | PostCopiesCopyIdImagesResponse404]
    """

    kwargs = _get_kwargs(
        copy_id=copy_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    copy_id: int,
    *,
    client: AuthenticatedClient,
    body: PostCopiesCopyIdImagesBody | Unset = UNSET,
) -> (
    ImageSummarySchemaType0
    | None
    | PostCopiesCopyIdImagesResponse401
    | PostCopiesCopyIdImagesResponse403
    | PostCopiesCopyIdImagesResponse404
    | None
):
    """Upload image to a copy

    Args:
        copy_id (int):  Example: 1.
        body (PostCopiesCopyIdImagesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ImageSummarySchemaType0 | None | PostCopiesCopyIdImagesResponse401 | PostCopiesCopyIdImagesResponse403 | PostCopiesCopyIdImagesResponse404
    """

    return (
        await asyncio_detailed(
            copy_id=copy_id,
            client=client,
            body=body,
        )
    ).parsed
