from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.email_schema import EmailSchema
from ...models.post_email_body import PostEmailBody
from ...models.post_email_response_401 import PostEmailResponse401
from ...models.post_email_response_403 import PostEmailResponse403
from ...models.post_email_response_404 import PostEmailResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostEmailBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/email",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EmailSchema | PostEmailResponse401 | PostEmailResponse403 | PostEmailResponse404 | None:
    if response.status_code == 200:
        response_200 = EmailSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostEmailResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostEmailResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostEmailResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EmailSchema | PostEmailResponse401 | PostEmailResponse403 | PostEmailResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostEmailBody | Unset = UNSET,
) -> Response[EmailSchema | PostEmailResponse401 | PostEmailResponse403 | PostEmailResponse404]:
    """Queuing emails

    Args:
        body (PostEmailBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailSchema | PostEmailResponse401 | PostEmailResponse403 | PostEmailResponse404]
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
    body: PostEmailBody | Unset = UNSET,
) -> EmailSchema | PostEmailResponse401 | PostEmailResponse403 | PostEmailResponse404 | None:
    """Queuing emails

    Args:
        body (PostEmailBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailSchema | PostEmailResponse401 | PostEmailResponse403 | PostEmailResponse404
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostEmailBody | Unset = UNSET,
) -> Response[EmailSchema | PostEmailResponse401 | PostEmailResponse403 | PostEmailResponse404]:
    """Queuing emails

    Args:
        body (PostEmailBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailSchema | PostEmailResponse401 | PostEmailResponse403 | PostEmailResponse404]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostEmailBody | Unset = UNSET,
) -> EmailSchema | PostEmailResponse401 | PostEmailResponse403 | PostEmailResponse404 | None:
    """Queuing emails

    Args:
        body (PostEmailBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailSchema | PostEmailResponse401 | PostEmailResponse403 | PostEmailResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
